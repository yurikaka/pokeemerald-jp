#!/usr/bin/env python3
"""Build patch/pokedex_entries.json from the JP base ROM and the US Chinese sources."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

JP_TABLE = 0x0854069C
JP_ENTRY_SIZE = 28
ENTRY_COUNT = 387
ROM_BASE = 0x08000000

ENTRY_RE = re.compile(
    r"\.categoryName\s*=\s*_\(\s*\"((?:[^\"\\]|\\.)*)\"\s*\).*?\.description\s*=\s*(g\w+)",
    re.DOTALL,
)
TEXT_RE = re.compile(
    r"const u8 (g\w+)\[\] = _\(\s*((?:\"(?:[^\"\\]|\\.)*\"\s*)+)\);",
    re.DOTALL,
)
STRING_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def unescape(text: str) -> str:
    return (
        text.replace("\\n", "\n")
        .replace("\\l", "\\l")
        .replace("\\p", "\\p")
        .replace('\\"', '"')
        .replace("\\\\", "\\")
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jp-rom", type=Path, required=True)
    parser.add_argument("--us-repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    entries_source = (args.us_repo / "src/data/pokemon/pokedex_entries.h").read_text(encoding="utf-8")
    text_source = (args.us_repo / "src/data/pokemon/pokedex_text.h").read_text(encoding="utf-8")

    descriptions = {}
    for match in TEXT_RE.finditer(text_source):
        symbol = match.group(1)
        body = "".join(STRING_RE.findall(match.group(2)))
        descriptions[symbol] = unescape(body)

    pairs = ENTRY_RE.findall(entries_source)
    if len(pairs) != ENTRY_COUNT:
        raise SystemExit(f"expected {ENTRY_COUNT} US entries, found {len(pairs)}")

    rom = args.jp_rom.read_bytes()
    base = JP_TABLE - ROM_BASE
    entries = []
    for index, (category, desc_symbol) in enumerate(pairs):
        raw = rom[base + index * JP_ENTRY_SIZE : base + (index + 1) * JP_ENTRY_SIZE]
        if desc_symbol not in descriptions:
            raise SystemExit(f"missing description text for {desc_symbol}")
        entries.append(
            {
                "category": unescape(category),
                "jp_category": raw[0:6].hex(),
                "stats": raw[6:12].hex(),
                "tail": raw[16:28].hex(),
                "description": descriptions[desc_symbol],
            }
        )

    document = {
        "kind": "pokedex_entries",
        "name": "ChsPokedexEntries",
        "source_commit": "8dbfd7c4e",
        "entries": entries,
    }
    args.output.write_text(json.dumps(document, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    total_desc = sum(len(e["description"]) for e in entries)
    print(f"wrote {args.output}: {len(entries)} entries, {total_desc} description chars")


if __name__ == "__main__":
    main()
