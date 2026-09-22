#!/usr/bin/env python3
"""Compare two US builds and report text symbols changed by a localization commit."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


ROM_BASE = 0x08000000
ROM_LIMIT = 0x0A000000
EOS = 0xFF


def load_symbols(nm: str, elf: Path) -> dict[str, tuple[int, str]]:
    output = subprocess.check_output([nm, "-n", "--defined-only", str(elf)], text=True)
    symbols: dict[str, tuple[int, str]] = {}
    for line in output.splitlines():
        fields = line.split()
        if len(fields) != 3:
            continue
        try:
            address = int(fields[0], 16)
        except ValueError:
            continue
        symbol_type = fields[1]
        if ROM_BASE <= address < ROM_LIMIT and symbol_type in "dDrR":
            symbols[fields[2]] = (address, symbol_type)
    return symbols


def read_string(rom: bytes, address: int, max_length: int) -> bytes | None:
    offset = address - ROM_BASE
    if not 0 <= offset < len(rom):
        return None
    end = rom.find(bytes([EOS]), offset, min(offset + max_length, len(rom)))
    if end < 0:
        return None
    return rom[offset : end + 1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before-rom", type=Path, required=True)
    parser.add_argument("--before-elf", type=Path, required=True)
    parser.add_argument("--after-rom", type=Path, required=True)
    parser.add_argument("--after-elf", type=Path, required=True)
    parser.add_argument("--nm", required=True)
    parser.add_argument("--max-length", type=int, default=4096)
    parser.add_argument(
        "--name-pattern",
        default=r"(?:Text|Description|Message|Name|String)",
        help="regular expression selecting likely text symbols",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    before_rom = args.before_rom.read_bytes()
    after_rom = args.after_rom.read_bytes()
    before_symbols = load_symbols(args.nm, args.before_elf)
    after_symbols = load_symbols(args.nm, args.after_elf)
    name_pattern = re.compile(args.name_pattern)

    changed = []
    for name in sorted(before_symbols.keys() & after_symbols.keys()):
        if not name_pattern.search(name):
            continue
        before_address = before_symbols[name][0]
        after_address = after_symbols[name][0]
        before = read_string(before_rom, before_address, args.max_length)
        after = read_string(after_rom, after_address, args.max_length)
        if before is None or after is None or before == after:
            continue
        changed.append(
            {
                "symbol": name,
                "before_address": f"0x{before_address:08X}",
                "after_address": f"0x{after_address:08X}",
                "before_length": len(before),
                "after_length": len(after),
                "after_hex": after.hex(),
            }
        )

    result = {"count": len(changed), "strings": changed}
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
