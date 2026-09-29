#!/usr/bin/env python3
"""Audit a US C text file against Wokann's Japanese source and ROM."""

from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import warnings

from port_map_dialogue import (
    ROM_BASE,
    US_ROOT,
    WOKANN_ROOT,
    encode_japanese,
    existing_entries,
    occurrences,
    read_charmap,
    read_symbols,
)


ROOT = Path(__file__).resolve().parents[2]
DEFINITION_RE = re.compile(r"const u8\s+(\w+)\[\][^;=]*=\s*__?\((.*?)\);", re.DOTALL)
LITERAL_RE = re.compile(r'"(?:[^"\\]|\\.)*"')


def definitions(source: str) -> dict[str, str]:
    result = {}
    for symbol, body in DEFINITION_RE.findall(source):
        literals = LITERAL_RE.findall(body)
        if literals:
            try:
                result[symbol] = "".join(ast.literal_eval(value) for value in literals)
            except (SyntaxError, ValueError):
                continue
    return result


def encode_source(value: str, charmap: dict[str, bytes]) -> bytes | None:
    return encode_japanese(
        ".string " + json.dumps(value.split("$")[0] + "$", ensure_ascii=False),
        charmap,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--nm", required=True)
    parser.add_argument("--symbol-offset", type=int, default=0)
    parser.add_argument("--symbol-limit", type=int)
    parser.add_argument("--auto-wrap", action="store_true")
    args = parser.parse_args()

    warnings.filterwarnings("ignore", category=SyntaxWarning)
    us_source = subprocess.check_output(
        ["git", "-C", str(US_ROOT), "show", f"{args.source_commit}:{args.source}"],
        text=True,
    )
    changed_lines = subprocess.check_output(
        ["git", "-C", str(US_ROOT), "show", "--format=", args.source_commit, "--", args.source],
        text=True,
    )
    changed_symbols = {
        match.group(1)
        for line in changed_lines.splitlines()
        if line.startswith("+") and not line.startswith("+++")
        if (match := re.search(r"\bconst u8\s+(\w+)\[\]", line))
    }
    us_definitions = definitions(us_source)
    current_definitions = definitions((US_ROOT / args.source).read_text(encoding="utf-8"))
    jp_definitions: dict[str, list[tuple[Path, str]]] = {}
    for path in (WOKANN_ROOT / "src").rglob("*"):
        if path.suffix not in (".c", ".h"):
            continue
        for symbol, value in definitions(path.read_text(encoding="utf-8", errors="replace")).items():
            jp_definitions.setdefault(symbol, []).append((path, value))

    us_rom_path = US_ROOT / "pokeemerald.gba"
    us_elf_path = US_ROOT / "pokeemerald.elf"
    jp_rom_path = ROOT / "baserom_jp.gba"
    us_rom = us_rom_path.read_bytes()
    jp_rom = jp_rom_path.read_bytes()
    symbols = read_symbols(us_elf_path, args.nm)
    us_charmap = read_charmap(US_ROOT / "charmap.txt")
    jp_charmap = read_charmap(WOKANN_ROOT / "charmap.txt")
    ported, used_references = existing_entries()
    manifest = json.loads((ROOT / "patch/manifest.json").read_text(encoding="utf-8"))
    used_references.update(entry["address"] for entry in manifest["pointer_writes"])
    replaced_targets = {entry["old"] for entry in manifest["pointer_replacements"]}

    texts = []
    references = []
    mapped = []
    unresolved = []
    statuses = Counter()
    selected_symbols = [symbol for symbol in us_definitions if symbol in changed_symbols]
    selected_symbols = selected_symbols[
        args.symbol_offset : None if args.symbol_limit is None else args.symbol_offset + args.symbol_limit
    ]
    for symbol in selected_symbols:
        chinese = us_definitions[symbol]
        if symbol not in changed_symbols or not re.search(r"[\u3400-\u9fff]", chinese):
            continue

        reason = None
        candidates = jp_definitions.get(symbol, [])
        if symbol in ported:
            reason = "already_in_batch"
        elif len(candidates) != 1:
            reason = "missing_or_ambiguous_wokann_symbol"
        elif current_definitions.get(symbol) != chinese:
            reason = "source_changed_after_commit"
        else:
            jp_path, japanese = candidates[0]
            encoded_jp = encode_source(japanese, jp_charmap)
            encoded_us = encode_source(chinese, us_charmap)
            if encoded_jp is None or encoded_us is None:
                reason = "unsupported_source_encoding"
            elif symbol not in symbols:
                reason = "missing_us_elf_symbol"
            else:
                offset = symbols[symbol] - ROM_BASE
                if us_rom[offset : offset + len(encoded_us)] != encoded_us:
                    reason = "us_binary_source_mismatch"
                else:
                    targets = [
                        address
                        for address in occurrences(jp_rom, encoded_jp)
                        if occurrences(jp_rom, address.to_bytes(4, "little"))
                    ]
                    if len(targets) != 1:
                        reason = "ambiguous_or_unreferenced_japanese_text"
                    else:
                        target = targets[0]
                        jp_references = [
                            reference
                            for reference in occurrences(jp_rom, target.to_bytes(4, "little"))
                            if reference % 4 == 0
                        ]
                        if f"0x{target:08X}" in replaced_targets or any(
                            f"0x{reference:08X}" in used_references for reference in jp_references
                        ):
                            reason = "already_patched_reference"
                        else:
                            placeholders = {
                                encoded_us[index + 1]
                                for index, value in enumerate(encoded_us[:-1])
                                if value == 0xFD
                            }
                            if placeholders or 0xF7 in encoded_us:
                                reason = "dynamic_placeholder_needs_review"
                            else:
                                name = "Chs_" + symbol
                                texts.append({"name": name, "source_symbol": symbol, "us_encoded_hex": encoded_us.hex(), "auto_wrap": args.auto_wrap})
                                addresses = []
                                for reference in jp_references:
                                    address = f"0x{reference:08X}"
                                    used_references.add(address)
                                    addresses.append(address)
                                    references.append({"address": address, "original": f"0x{target:08X}", "symbol": name, "source_symbol": symbol})
                                mapped.append({"source_symbol": symbol, "wokann_source": str(jp_path.relative_to(WOKANN_ROOT)), "us_text_address": f"0x{symbols[symbol]:08X}", "japanese_text_address": f"0x{target:08X}", "japanese_references": addresses})
                                statuses["mapped"] += 1
        if reason is not None:
            statuses[reason] += 1
            unresolved.append({"source_symbol": symbol, "reason": reason})

    batch_name = args.name + ".json"
    batch = {
        "source_commit": args.source_commit,
        "category": "C text: " + args.source,
        "texts": texts,
        "reference_writes": references,
        "mapping_report": {
            "report_file": "patch/mapping_reports/" + batch_name,
            "mapped_count": len(mapped),
            "unresolved_count": len(unresolved),
        },
    }
    report = {
        "schema_version": 1,
        "batch": batch_name,
        "source_commit": args.source_commit,
        "source": args.source,
        "selection": {"symbol_offset": args.symbol_offset, "symbol_limit": args.symbol_limit, "auto_wrap": args.auto_wrap},
        "inputs": {
            "us_rom_sha1": hashlib.sha1(us_rom).hexdigest(),
            "us_elf_sha1": hashlib.sha1(us_elf_path.read_bytes()).hexdigest(),
            "jp_rom_sha1": hashlib.sha1(jp_rom).hexdigest(),
            "wokann_commit": subprocess.check_output(["git", "-C", str(WOKANN_ROOT), "rev-parse", "HEAD"], text=True).strip(),
        },
        "mapping_policy": "Same C symbol and exact source strings; US compiled bytes match commit source; Japanese source bytes are unique in the JP ROM and have word-aligned pointers; no dynamic placeholders; preexisting patch references excluded.",
        "summary": dict(sorted(statuses.items())),
        "mapped": mapped,
        "unresolved": unresolved,
    }
    print(json.dumps({"batch": batch, "report": report}, ensure_ascii=False))


if __name__ == "__main__":
    main()
