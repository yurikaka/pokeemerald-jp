#!/usr/bin/env python3
"""Map US ROM text-pointer references to their Japanese ROM counterparts."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import re
import struct
import subprocess
from pathlib import Path


ROM_BASE = 0x08000000
ROM_LIMIT = 0x0A000000


def load_symbols(nm: str, elf: Path) -> dict[str, int]:
    output = subprocess.check_output([nm, "-n", "--defined-only", str(elf)], text=True)
    symbols: dict[str, int] = {}
    for line in output.splitlines():
        fields = line.split()
        if len(fields) != 3 or fields[1] not in "dDrR":
            continue
        try:
            address = int(fields[0], 16)
        except ValueError:
            continue
        if ROM_BASE <= address < ROM_LIMIT:
            symbols[fields[2]] = address
    return symbols


def pointer_mask(data: bytes, target_offset: int) -> bytearray:
    mask = bytearray(len(data))
    for index in range(len(data) - 3):
        value = struct.unpack_from("<I", data, index)[0]
        if ROM_BASE <= value < ROM_LIMIT:
            mask[index : index + 4] = b"\x01" * 4
    mask[target_offset : target_offset + 4] = b"\x01" * 4
    return mask


def longest_literal(data: bytes, mask: bytes) -> tuple[int, bytes]:
    best_start = 0
    best = b""
    index = 0
    while index < len(data):
        if mask[index]:
            index += 1
            continue
        end = index
        while end < len(data) and not mask[end]:
            end += 1
        if end - index > len(best):
            best_start, best = index, data[index:end]
        index = end
    return best_start, best


def find_context_matches(jp_rom: bytes, context: bytes, mask: bytes) -> list[int]:
    anchor_offset, anchor = longest_literal(context, mask)
    if len(anchor) < 4:
        return []
    matches = []
    cursor = 0
    while True:
        found = jp_rom.find(anchor, cursor)
        if found < 0:
            break
        start = found - anchor_offset
        if 0 <= start <= len(jp_rom) - len(context):
            candidate = jp_rom[start : start + len(context)]
            if all(mask[i] or context[i] == candidate[i] for i in range(len(context))):
                matches.append(start)
        cursor = found + 1
    return matches


def pointer_occurrences(rom: bytes, address: int) -> list[int]:
    needle = struct.pack("<I", address)
    result = []
    cursor = 0
    while True:
        found = rom.find(needle, cursor)
        if found < 0:
            return result
        result.append(found)
        cursor = found + 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--us-rom", type=Path, required=True)
    parser.add_argument("--us-elf", type=Path, required=True)
    parser.add_argument("--jp-rom", type=Path, required=True)
    parser.add_argument("--symbols", type=Path, help="JSON report produced by analyze_us_text_commit.py")
    parser.add_argument("--symbol-pattern", default=".*")
    parser.add_argument("--nm", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    us_rom = args.us_rom.read_bytes()
    jp_rom = args.jp_rom.read_bytes()
    us_symbols = load_symbols(args.nm, args.us_elf)
    pattern = re.compile(args.symbol_pattern)
    selected = set(us_symbols)
    if args.symbols:
        report = json.loads(args.symbols.read_text(encoding="utf-8"))
        selected &= {entry["symbol"] for entry in report["strings"]}
    selected = {name for name in selected if pattern.search(name)}

    mapped = []
    unresolved = []
    for name in sorted(selected):
        address = us_symbols[name]
        refs = pointer_occurrences(us_rom, address)
        mapped_refs = []
        for ref in refs:
            candidates: list[tuple[int, int]] = []
            for radius in (16, 24, 32, 48, 64):
                start = ref - radius
                end = ref + 4 + radius
                if start < 0 or end > len(us_rom):
                    continue
                context = us_rom[start:end]
                mask = pointer_mask(context, radius)
                matches = find_context_matches(jp_rom, context, mask)
                valid = []
                for match in matches:
                    jp_ref = match + radius
                    value = struct.unpack_from("<I", jp_rom, jp_ref)[0]
                    if ROM_BASE <= value < ROM_BASE + len(jp_rom):
                        valid.append((jp_ref, value))
                if len(valid) == 1:
                    candidates = valid
                    break
            if len(candidates) == 1:
                jp_ref, jp_text = candidates[0]
                mapped_refs.append(
                    {
                        "us_reference": f"0x{ROM_BASE + ref:08X}",
                        "jp_reference": f"0x{ROM_BASE + jp_ref:08X}",
                        "jp_text": f"0x{jp_text:08X}",
                    }
                )
        entry = {
            "symbol": name,
            "us_text": f"0x{address:08X}",
            "us_reference_count": len(refs),
            "references": mapped_refs,
        }
        if refs and len(mapped_refs) == len(refs):
            mapped.append(entry)
        else:
            unresolved.append(entry)

    # Script data for one map normally has a constant regional offset even
    # where a localized script differs enough for contextual matching to fail.
    deltas = Counter()
    for entry in mapped:
        for reference in entry["references"]:
            us_ref = int(reference["us_reference"], 0)
            jp_ref = int(reference["jp_reference"], 0)
            deltas[jp_ref - us_ref] += 1
    inferred_delta = deltas.most_common(1)[0][0] if deltas else None

    still_unresolved = []
    if inferred_delta is not None:
        for entry in unresolved:
            inferred = []
            for ref in pointer_occurrences(us_rom, int(entry["us_text"], 0)):
                jp_ref = ROM_BASE + ref + inferred_delta
                jp_offset = jp_ref - ROM_BASE
                if not 0 <= jp_offset <= len(jp_rom) - 4:
                    break
                jp_text = struct.unpack_from("<I", jp_rom, jp_offset)[0]
                if not ROM_BASE <= jp_text < ROM_BASE + len(jp_rom):
                    break
                inferred.append(
                    {
                        "us_reference": f"0x{ROM_BASE + ref:08X}",
                        "jp_reference": f"0x{jp_ref:08X}",
                        "jp_text": f"0x{jp_text:08X}",
                        "inferred": True,
                    }
                )
            if inferred and len(inferred) == entry["us_reference_count"]:
                entry["references"] = inferred
                mapped.append(entry)
            else:
                still_unresolved.append(entry)
        unresolved = still_unresolved

    result = {
        "inferred_reference_delta": None if inferred_delta is None else inferred_delta,
        "mapped_count": len(mapped),
        "unresolved_count": len(unresolved),
        "mapped": sorted(mapped, key=lambda entry: entry["symbol"]),
        "unresolved": unresolved,
    }
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
