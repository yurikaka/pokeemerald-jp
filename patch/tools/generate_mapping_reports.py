#!/usr/bin/env python3
"""Generate auditable mapping reports for existing text batches."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def parse_us_build(value: str) -> tuple[str, Path, Path]:
    parts = value.split("=", 2)
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("US build must be COMMIT=ROM=ELF")
    commit, rom_path, elf_path = parts
    return commit, Path(rom_path), Path(elf_path)


def report_path(output_dir: Path, batch_path: Path) -> Path:
    return output_dir / batch_path.name


def references(entries: list[dict]) -> Counter[tuple[str, str, str]]:
    return Counter(
        (entry["source_symbol"], entry["address"], entry["original"])
        for entry in entries
        if "source_symbol" in entry
    )


def render_references(entries: Counter[tuple[str, str, str]]) -> list[dict[str, object]]:
    return [
        {
            "source_symbol": source_symbol,
            "address": address,
            "original": original,
            "count": count,
        }
        for (source_symbol, address, original), count in sorted(entries.items())
    ]


def find_build(
    source_commit: str,
    builds: dict[str, tuple[Path, Path]],
) -> tuple[Path, Path] | None:
    matches = [build for commit, build in builds.items() if commit.startswith(source_commit)]
    if len(matches) != 1:
        return None
    return matches[0]


def generate_report(
    batch_path: Path,
    output_dir: Path,
    jp_rom: Path,
    nm: str,
    builds: dict[str, tuple[Path, Path]],
) -> None:
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    source_commit = batch.get("source_commit")
    expected = references(batch.get("reference_writes", []))
    output = {
        "schema_version": 1,
        "batch": batch_path.name,
        "source_commit": source_commit,
        "expected_reference_writes": render_references(expected),
    }

    if not source_commit:
        output.update(
            {
                "status": "manual",
                "reason": "batch has no source_commit; its references cannot be reconstructed from a US text build",
            }
        )
        report_path(output_dir, batch_path).write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return

    build = find_build(source_commit, builds)
    if build is None:
        output.update(
            {
                "status": "unavailable",
                "reason": "no matching US ROM and ELF build was supplied",
            }
        )
        report_path(output_dir, batch_path).write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return

    source_symbols = sorted(
        {
            entry["source_symbol"]
            for entry in batch.get("texts", []) + batch.get("reference_writes", [])
            if "source_symbol" in entry
        }
    )
    if not source_symbols:
        output.update(
            {
                "status": "manual",
                "reason": "batch has no US source symbols to map",
            }
        )
        report_path(output_dir, batch_path).write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return

    us_rom, us_elf = build
    pattern = "^(?:" + "|".join(re.escape(symbol) for symbol in source_symbols) + ")$"
    mapper = Path(__file__).with_name("map_us_jp_text_refs.py")
    with tempfile.TemporaryDirectory() as temporary_dir:
        mapping_path = Path(temporary_dir) / "mapping.json"
        subprocess.run(
            [
                sys.executable,
                str(mapper),
                "--us-rom",
                str(us_rom),
                "--us-elf",
                str(us_elf),
                "--jp-rom",
                str(jp_rom),
                "--symbol-pattern",
                pattern,
                "--nm",
                nm,
                "--output",
                str(mapping_path),
            ],
            check=True,
        )
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))

    actual = Counter(
        (entry["symbol"], reference["jp_reference"], reference["jp_text"])
        for entry in mapping["mapped"]
        for reference in entry["references"]
    )
    output.update(
        {
            "status": "generated",
            "requested_source_symbols": source_symbols,
            "mapping_report": mapping,
            "comparison": {
                "matching_reference_count": sum((expected & actual).values()),
                "expected_only": render_references(expected - actual),
                "mapped_only": render_references(actual - expected),
            },
        }
    )
    report_path(output_dir, batch_path).write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--jp-rom", type=Path, required=True)
    parser.add_argument("--nm", required=True)
    parser.add_argument("--us-build", action="append", type=parse_us_build, default=[])
    args = parser.parse_args()

    builds = {
        commit: (rom_path, elf_path)
        for commit, rom_path, elf_path in args.us_build
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for batch_path in sorted(args.batch_dir.glob("*.json")):
        generate_report(batch_path, args.output_dir, args.jp_rom, args.nm, builds)


if __name__ == "__main__":
    main()
