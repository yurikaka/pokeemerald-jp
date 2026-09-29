#!/usr/bin/env python3
"""Emit verified in-place Chinese Battle Tent trainer-name patches."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess

from build_texts import encode_compact_chinese_text, read_charmap
from port_map_dialogue import ROM_BASE, encode_japanese


ROOT = Path(__file__).resolve().parents[2]
US_ROOT = ROOT.parent / "pokeemerald_us_chs"
WOKANN_ROOT = ROOT.parent / "pokeemerald_wokann_dev"
SOURCE = "src/data/battle_frontier/battle_tent.h"
NAME_RE = re.compile(r"\.trainerName\s*=\s+__?\(\"([^\"]+)\"\)")
TABLES = (
    ("gSlateportBattleTentTrainers", 0x085BC958),
    ("gVerdanturfBattleTentTrainers", 0x085BD554),
    ("gFallarborBattleTentTrainers", 0x085BDFC8),
)
RECORD_SIZE = 0x34
NAME_OFFSET = 4
NAME_SIZE = 8


def names(text: str) -> list[str]:
    return NAME_RE.findall(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", default="fe570a7e5")
    args = parser.parse_args()

    us_source = subprocess.check_output(
        ["git", "-C", str(US_ROOT), "show", f"{args.source_commit}:{SOURCE}"], text=True
    )
    jp_source = (WOKANN_ROOT / SOURCE).read_text(encoding="utf-8")
    us_names = names(us_source)
    jp_names = names(jp_source)
    if len(us_names) != len(jp_names) or len(us_names) != len(TABLES) * 30:
        raise SystemExit("unexpected Battle Tent trainer-name count")

    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    jp_charmap = read_charmap(WOKANN_ROOT / "charmap.txt")
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    patches = []
    records = []
    for index, (us_name, jp_name) in enumerate(zip(us_names, jp_names)):
        if not re.search(r"[\u3400-\u9fff]", us_name):
            raise SystemExit(f"entry {index} is not Chinese: {us_name!r}")
        replacement = encode_compact_chinese_text(us_name, charmap)
        if len(replacement) > NAME_SIZE:
            raise SystemExit(f"entry {index} exceeds the fixed {NAME_SIZE}-byte field: {us_name!r}")
        expected = encode_japanese('.string ' + json.dumps(jp_name), jp_charmap)
        if expected is None or len(expected) != NAME_SIZE:
            raise SystemExit(f"entry {index} has unexpected Japanese field encoding: {jp_name!r}")
        table_index, trainer_index = divmod(index, 30)
        address = TABLES[table_index][1] + trainer_index * RECORD_SIZE + NAME_OFFSET
        actual = rom[address - ROM_BASE : address - ROM_BASE + NAME_SIZE]
        if actual != expected:
            raise SystemExit(f"entry {index} mismatches baserom at 0x{address:08X}")
        patches.append({
            "address": f"0x{address:08X}",
            "original": actual.hex(),
            "replacement": replacement.ljust(NAME_SIZE, b"\xff").hex(),
        })
        records.append({"index": index, "address": f"0x{address:08X}", "source_name": us_name})

    print(json.dumps({"patches": patches, "records": records}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
