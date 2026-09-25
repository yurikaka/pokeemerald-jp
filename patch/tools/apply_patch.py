#!/usr/bin/env python3
"""Inject the Chinese payload into an exact Japanese Emerald build."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import subprocess
from pathlib import Path


ROM_BASE = 0x08000000
ROM_SIZE = 32 * 1024 * 1024
ORIGINAL_ROM_SIZE = 16 * 1024 * 1024


def parse_int(value: str) -> int:
    return int(value, 0)


def load_symbols(nm: str, elf: Path) -> dict[str, int]:
    output = subprocess.check_output([nm, "-n", str(elf)], text=True)
    symbols: dict[str, int] = {}
    for line in output.splitlines():
        fields = line.split()
        if len(fields) == 3:
            try:
                symbols[fields[2]] = int(fields[0], 16)
            except ValueError:
                pass
    return symbols


def rom_offset(address: int) -> int:
    if not ROM_BASE <= address < ROM_BASE + ROM_SIZE:
        raise ValueError(f"address outside GBA ROM: 0x{address:08X}")
    return address - ROM_BASE


def write_word(rom: bytearray, address: int, value: int) -> None:
    offset = rom_offset(address)
    rom[offset:offset + 4] = struct.pack("<I", value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rom", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--payload-elf", type=Path, required=True)
    parser.add_argument("--payload-bin", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--batch", type=Path, action="append", default=[])
    parser.add_argument("--nm", required=True)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    source = args.rom.read_bytes()
    digest = hashlib.sha1(source).hexdigest()
    if digest != manifest["base_sha1"]:
        raise SystemExit(f"unexpected base ROM SHA-1: {digest}")
    if len(source) != ORIGINAL_ROM_SIZE:
        raise SystemExit(f"unexpected base ROM size: {len(source)}")

    symbols = load_symbols(args.nm, args.payload_elf)
    payload = args.payload_bin.read_bytes()
    payload_address = parse_int(manifest["payload_address"])
    payload_offset = rom_offset(payload_address)
    if payload_offset + len(payload) > ROM_SIZE:
        raise SystemExit("payload exceeds the 32 MiB GBA ROM limit")

    rom = bytearray(source)
    rom.extend(b"\xFF" * (ROM_SIZE - len(rom)))
    rom[payload_offset:payload_offset + len(payload)] = payload

    for entry in manifest.get("code_patches", []):
        address = parse_int(entry["address"])
        offset = rom_offset(address)
        expected = bytes.fromhex(entry["original"])
        replacement = bytes.fromhex(entry["replacement"])
        if len(expected) != len(replacement):
            raise SystemExit(f"code patch 0x{address:08X}: replacement size differs")
        actual = rom[offset:offset + len(expected)]
        if actual != expected:
            raise SystemExit(
                f"code patch 0x{address:08X}: expected {expected.hex()}, got {actual.hex()}"
            )
        rom[offset:offset + len(replacement)] = replacement

    hook_address = parse_int(manifest["render_hook_address"])
    hook_offset = rom_offset(hook_address)
    expected_hook = bytes.fromhex(manifest["render_hook_original"])
    if rom[hook_offset:hook_offset + len(expected_hook)] != expected_hook:
        actual = rom[hook_offset:hook_offset + len(expected_hook)].hex()
        raise SystemExit(f"render hook bytes changed: expected {expected_hook.hex()}, got {actual}")
    hook_target = symbols[manifest["render_hook_symbol"]] | 1
    if hook_address & 2:
        hook_code = struct.pack("<HHHI", 0x4B01, 0x4718, 0, hook_target)
    else:
        hook_code = struct.pack("<HHI", 0x4800, 0x4700, hook_target)
    if len(expected_hook) != len(hook_code):
        raise SystemExit(f"render hook 0x{hook_address:08X}: expected {len(hook_code)} original bytes")
    rom[hook_offset:hook_offset + len(hook_code)] = hook_code

    for entry in manifest.get("function_hooks", []):
        address = parse_int(entry["address"])
        offset = rom_offset(address)
        expected = bytes.fromhex(entry["original"])
        if rom[offset:offset + len(expected)] != expected:
            actual = rom[offset:offset + len(expected)].hex()
            raise SystemExit(f"function hook 0x{address:08X}: expected {expected.hex()}, got {actual}")
        # Function-entry trampoline that preserves r0-r3 (unlike the render
        # hook, which clobbers r0): push a spare slot, park the target in it,
        # and pop it straight into pc.
        target = symbols[entry["symbol"]] | 1
        rom[offset:offset + 16] = (
            struct.pack("<HHHHH", 0xB401, 0xB401, 0x4801, 0x9001, 0xBD01)
            + b"\x00\x00"
            + struct.pack("<I", target)
        )

    for entry in manifest["mode_jump_table"]:
        address = parse_int(entry["address"])
        offset = rom_offset(address)
        expected = parse_int(entry["original"])
        actual = struct.unpack_from("<I", rom, offset)[0]
        if actual != expected:
            raise SystemExit(f"jump table entry 0x{address:08X}: expected 0x{expected:08X}, got 0x{actual:08X}")
        write_word(rom, address, symbols[entry["symbol"]])

    replacements = {parse_int(entry["old"]): entry for entry in manifest["pointer_replacements"]}
    references = {old: [] for old in replacements}
    for offset in range(0, ORIGINAL_ROM_SIZE, 4):
        value = struct.unpack_from("<I", rom, offset)[0]
        if value in references:
            references[value].append(offset)

    for old, replacement in replacements.items():
        offsets = references[old]
        if len(offsets) != replacement["expected"]:
            raise SystemExit(
                f"pointer 0x{old:08X}: expected {replacement['expected']} aligned references, found {len(offsets)}"
            )
        excluded = {rom_offset(parse_int(address)) for address in replacement.get("exclude", [])}
        new_bytes = struct.pack("<I", symbols[replacement["symbol"]])
        for offset in offsets:
            if offset in excluded:
                continue
            rom[offset:offset + 4] = new_bytes

    for entry in manifest["pointer_writes"]:
        address = parse_int(entry["address"])
        if "original" in entry:
            actual = struct.unpack_from("<I", rom, rom_offset(address))[0]
            expected = parse_int(entry["original"])
            if actual != expected:
                raise SystemExit(
                    f"pointer 0x{address:08X}: expected 0x{expected:08X}, got 0x{actual:08X}"
                )
        write_word(rom, address, symbols[entry["symbol"]] + parse_int(entry.get("offset", "0")))

    for batch_path in args.batch:
        batch = json.loads(batch_path.read_text(encoding="utf-8"))
        for entry in batch.get("reference_writes", []):
            address = parse_int(entry["address"])
            offset = rom_offset(address)
            expected = parse_int(entry["original"])
            actual = struct.unpack_from("<I", rom, offset)[0]
            if actual != expected:
                raise SystemExit(
                    f"reference 0x{address:08X}: expected 0x{expected:08X}, got 0x{actual:08X}"
                )
            write_word(rom, address, symbols[entry["symbol"]])

    args.output.write_bytes(rom)
    print(f"wrote {args.output} ({len(rom)} bytes, SHA-1 {hashlib.sha1(rom).hexdigest()})")


if __name__ == "__main__":
    main()
