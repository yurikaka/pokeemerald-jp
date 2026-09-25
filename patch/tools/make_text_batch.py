#!/usr/bin/env python3
"""Combine US text changes and audited JP references into a patch batch."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def patch_symbol(source_symbol: str) -> str:
    return "Chs_" + re.sub(r"[^A-Za-z0-9_]", "_", source_symbol)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changes", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--japanese-placeholder", action="append", type=lambda value: int(value, 0), default=[])
    parser.add_argument("--wrap-all-placeholders", action="store_true")
    parser.add_argument("--wrap-dynamic", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    changes = {
        entry["symbol"]: entry
        for entry in json.loads(args.changes.read_text(encoding="utf-8"))["strings"]
    }
    mapping = json.loads(args.mapping.read_text(encoding="utf-8"))
    if mapping["unresolved_count"]:
        names = ", ".join(entry["symbol"] for entry in mapping["unresolved"])
        raise SystemExit(f"unresolved symbols: {names}")

    texts = []
    reference_writes = []
    for mapped in mapping["mapped"]:
        source_symbol = mapped["symbol"]
        changed = changes[source_symbol]
        name = patch_symbol(source_symbol)
        raw = bytes.fromhex(changed["after_hex"])
        definition = {
            "name": name,
            "source_symbol": source_symbol,
            "us_encoded_hex": changed["after_hex"],
        }
        if args.wrap_all_placeholders:
            placeholders = sorted({raw[index + 1] for index, value in enumerate(raw[:-1]) if value == 0xFD})
        else:
            placeholders = [
                value for value in args.japanese_placeholder
                if bytes((0xFD, value)) in raw
            ]
        if placeholders:
            definition["japanese_placeholders"] = placeholders
        if args.wrap_dynamic and 0xF7 in raw:
            definition["japanese_dynamic"] = True
        texts.append(definition)

        for reference in mapped["references"]:
            reference_writes.append(
                {
                    "address": reference["jp_reference"],
                    "original": reference["jp_text"],
                    "symbol": name,
                    "source_symbol": source_symbol,
                }
            )

    document = {
        "source_commit": args.source_commit,
        "category": args.category,
        "mapping_report": mapping,
        "texts": texts,
        "reference_writes": reference_writes,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
