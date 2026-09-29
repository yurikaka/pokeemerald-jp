#!/usr/bin/env python3
"""Audit text-batch ROM pointer overrides against Wokann's JP decompilation.

The batches were originally derived from US-to-JP binary matching.  This tool
adds a JP source-of-truth audit: for every pointer override it verifies the
unpatched JP ROM value, finds the Wokann source owner at the pointer address,
and compares the source's referenced symbol with the batch's source symbol.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess


ROM_BASE = 0x08000000
ADDRESS_RE = re.compile(r"(?i)_([0-9a-f]{8})\s*:")
ROM_LABEL_RE = re.compile(
    r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*::?\s*@\s*0x([0-9a-fA-F]{8})",
    re.MULTILINE,
)
EMITTER_LABEL_RE = re.compile(r"0x(08[0-9a-fA-F]{6})\s*:\s*'([A-Za-z_][A-Za-z0-9_]*)'")
POINTER_SYMBOL_RE = re.compile(
    r"\.4byte\s+([A-Za-z_][A-Za-z0-9_]*)(?:\s*\+\s*(0x[0-9a-fA-F]+))?"
)
FUNCTION_RE = re.compile(r"^[0-9a-fA-F]{8}$")
LABEL_DEFINITION_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*::?", re.MULTILINE)
C_DEFINITION_RE = re.compile(
    r"^\s*(?:static\s+)?(?:const\s+)?(?:u8|u16|u32|s8|s16|s32)\s+"
    r"(?:const\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*(?:\[|=)",
    re.MULTILINE,
)


def as_address(value: str) -> int:
    return int(value, 0)


def format_address(value: int | None) -> str | None:
    return f"0x{value:08X}" if value is not None else None


def source_files(root: Path) -> list[Path]:
    return [
        path
        for directory in ("src", "asm", "data")
        for path in (root / directory).rglob("*")
        if path.suffix in {".c", ".h", ".inc", ".s"}
    ]


def source_location(root: Path, path: Path, text: str, offset: int) -> dict[str, object]:
    line = text.count("\n", 0, offset) + 1
    return {
        "file": str(path.relative_to(root)),
        "line": line,
    }


def load_reference_index(root: Path) -> dict[int, list[dict[str, object]]]:
    index: dict[int, list[dict[str, object]]] = {}
    for path in source_files(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in ADDRESS_RE.finditer(text):
            address = int(match.group(1), 16)
            line_end = text.find("\n", match.end())
            if line_end < 0:
                line_end = len(text)
            pointer = POINTER_SYMBOL_RE.search(text, match.end(), line_end)
            if pointer is None:
                next_line_end = text.find("\n", line_end + 1)
                if next_line_end < 0:
                    next_line_end = len(text)
                next_line = text[line_end + 1 : next_line_end]
                if next_line.lstrip().startswith(".4byte"):
                    pointer = POINTER_SYMBOL_RE.search(next_line)
            entry = source_location(root, path, text, match.start())
            entry["referenced_symbol"] = pointer.group(1) if pointer else None
            entry["referenced_offset"] = pointer.group(2) if pointer and pointer.group(2) else None
            index.setdefault(address, []).append(entry)
    return index


def load_text_label_index(root: Path) -> dict[int, list[dict[str, object]]]:
    index: dict[int, list[dict[str, object]]] = {}
    definitions: dict[str, list[dict[str, object]]] = {}
    for path in source_files(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in ROM_LABEL_RE.finditer(text):
            entry = source_location(root, path, text, match.start())
            entry["symbol"] = match.group(1)
            index.setdefault(int(match.group(2), 16), []).append(entry)
            definitions.setdefault(match.group(1), []).append(entry)

    emitter = root / "tools" / "jp_emit_maps.py"
    text = emitter.read_text(encoding="utf-8", errors="replace")
    for match in EMITTER_LABEL_RE.finditer(text):
        address = int(match.group(1), 16)
        symbol = match.group(2)
        entries = definitions.get(symbol, [])
        if entries:
            index.setdefault(address, []).extend(entries)
        else:
            entry = source_location(root, emitter, text, match.start())
            entry["symbol"] = symbol
            index.setdefault(address, []).append(entry)
    return index


def load_symbol_definitions(root: Path) -> dict[str, list[dict[str, object]]]:
    definitions: dict[str, list[dict[str, object]]] = {}
    for path in source_files(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        for matcher in (LABEL_DEFINITION_RE, C_DEFINITION_RE):
            for match in matcher.finditer(text):
                definitions.setdefault(match.group(1), []).append(
                    source_location(root, path, text, match.start())
                )
    return definitions


def load_function_index(path: Path) -> tuple[list[int], dict[int, dict[str, str]]]:
    functions: dict[int, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        fields = line.split()
        address_index = next((index for index, value in enumerate(fields) if FUNCTION_RE.fullmatch(value)), None)
        if address_index is None or address_index + 1 >= len(fields):
            continue
        address = int(fields[address_index], 16)
        entry = {"symbol": fields[address_index + 1]}
        if address_index:
            entry["file"] = fields[address_index - 1]
        functions[address] = entry
    return sorted(functions), functions


def function_owner(
    address: int,
    starts: list[int],
    functions: dict[int, dict[str, str]],
) -> dict[str, object] | None:
    index = bisect_right(starts, address) - 1
    if index < 0:
        return None
    start = starts[index]
    owner: dict[str, object] = {"start": format_address(start), **functions[start]}
    return owner


def audit_reference(
    entry: dict[str, str],
    rom: bytes,
    references: dict[int, list[dict[str, object]]],
    labels: dict[int, list[dict[str, object]]],
    definitions: dict[str, list[dict[str, object]]],
    starts: list[int],
    functions: dict[int, dict[str, str]],
) -> dict[str, object]:
    reference = as_address(entry["address"])
    original = as_address(entry["original"])
    offset = reference - ROM_BASE
    actual = struct.unpack_from("<I", rom, offset)[0] if 0 <= offset <= len(rom) - 4 else None
    source_entries = references.get(reference, [])
    direct_symbols = sorted(
        {item["referenced_symbol"] for item in source_entries if item["referenced_symbol"] is not None}
    )
    expected_symbol = entry.get("source_symbol")
    target_symbols = {
        item["symbol"] for item in labels.get(original, []) if item.get("symbol") is not None
    }

    if direct_symbols == [expected_symbol]:
        status = "verified_direct_symbol"
    elif expected_symbol in target_symbols:
        status = "verified_text_label"
    elif expected_symbol and definitions.get(expected_symbol):
        status = "verified_source_definition"
    elif direct_symbols:
        status = "verified_fragment"
    elif target_symbols:
        status = "symbol_name_mismatch"
    else:
        status = "needs_review"
    if actual != original:
        status = "rom_mismatch"

    return {
        "jp_reference": format_address(reference),
        "jp_original_text": format_address(original),
        "batch_source_symbol": expected_symbol,
        "patch_symbol": entry.get("symbol"),
        "base_rom_value": format_address(actual),
        "base_rom_matches_batch": actual == original,
        "wokann_reference_locations": source_entries,
        "wokann_referenced_symbols": direct_symbols,
        "wokann_function_owner": function_owner(reference, starts, functions),
        "wokann_original_text_labels": labels.get(original, []),
        "wokann_source_symbol_definitions": definitions.get(expected_symbol, []),
        "status": status,
    }


def audit_batch(
    batch_path: Path,
    output_dir: Path,
    rom: bytes,
    rom_sha1: str,
    wokann_root: Path,
    references: dict[int, list[dict[str, object]]],
    labels: dict[int, list[dict[str, object]]],
    definitions: dict[str, list[dict[str, object]]],
    starts: list[int],
    functions: dict[int, dict[str, str]],
) -> Counter[str]:
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    entries = [
        audit_reference(entry, rom, references, labels, definitions, starts, functions)
        for entry in batch.get("reference_writes", [])
    ]
    statuses = Counter(entry["status"] for entry in entries)
    output = {
        "schema_version": 1,
        "audit": "wokann-jp-decompilation",
        "wokann_revision": subprocess.check_output(
            ["git", "-C", str(wokann_root), "rev-parse", "HEAD"], text=True
        ).strip(),
        "batch": batch_path.name,
        "jp_rom_sha1": rom_sha1,
        "source_commit": batch.get("source_commit"),
        "category": batch.get("category"),
        "summary": dict(sorted(statuses.items())),
        "reference_writes": entries,
    }
    (output_dir / batch_path.name).write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return statuses


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--jp-rom", type=Path, required=True)
    parser.add_argument("--wokann-root", type=Path, required=True)
    args = parser.parse_args()

    rom = args.jp_rom.read_bytes()
    rom_sha1 = hashlib.sha1(rom).hexdigest()
    references = load_reference_index(args.wokann_root)
    labels = load_text_label_index(args.wokann_root)
    definitions = load_symbol_definitions(args.wokann_root)
    starts, functions = load_function_index(args.wokann_root / "funcmap_jp.txt")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    totals: Counter[str] = Counter()
    batch_summaries: dict[str, dict[str, int]] = {}
    for batch_path in sorted(args.batch_dir.glob("*.json")):
        summary = audit_batch(
            batch_path,
            args.output_dir,
                rom,
                rom_sha1,
            args.wokann_root,
                references,
                labels,
                definitions,
            starts,
            functions,
        )
        totals.update(summary)
        batch_summaries[batch_path.name] = dict(sorted(summary.items()))
    (args.output_dir / "index.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "audit": "wokann-jp-decompilation",
                "wokann_revision": subprocess.check_output(
                    ["git", "-C", str(args.wokann_root), "rev-parse", "HEAD"], text=True
                ).strip(),
                "jp_rom_sha1": rom_sha1,
                "policy": {
                    "verified_direct_symbol": "base ROM pointer and Wokann's direct source reference both name source_symbol",
                    "verified_text_label": "base ROM pointer's original text address has a Wokann label matching source_symbol",
                    "verified_source_definition": "base ROM pointer matches the batch original and Wokann defines the same source symbol, but its fixed-address label was not recovered",
                    "verified_fragment": "base ROM pointer has an exact Wokann source reference, but JP folds the US text into a differently named text block or offset",
                    "symbol_name_mismatch": "a named Wokann original-text label exists but differs from source_symbol",
                    "needs_review": "the pointer has no exact Wokann symbol match yet",
                    "rom_mismatch": "the supplied base ROM pointer differs from the batch original value",
                },
                "summary": dict(sorted(totals.items())),
                "batches": batch_summaries,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps(dict(sorted(totals.items())), ensure_ascii=False))


if __name__ == "__main__":
    main()
