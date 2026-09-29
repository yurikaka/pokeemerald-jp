#!/usr/bin/env python3
"""Prepare audited Chinese text batches for Japanese map dialogue."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess
import warnings


ROOT = Path(__file__).resolve().parents[2]
US_ROOT = ROOT.parent / "pokeemerald_us_chs"
WOKANN_ROOT = ROOT.parent / "pokeemerald_wokann_dev"
ROM_BASE = 0x08000000
WOKANN_EVENT_SCRIPTS_ROM_START = 0x081DABAC
TEXT_RE = re.compile(r"^([A-Za-z_]\w+)::?\s*\n((?:\s*\.string .*\n)+)", re.MULTILINE)
STRING_RE = re.compile(r'\.string\s+("(?:[^"\\]|\\.)*")')
CHARMAP_RE = re.compile(r"^('[^']+'|[A-Za-z_@][\w@]*)\s*=\s*([0-9A-Fa-f ]+)")


def read_symbols(elf: Path, nm: str) -> dict[str, int]:
    output = subprocess.check_output([nm, "-n", "--defined-only", str(elf)], text=True)
    symbols = {}
    for line in output.splitlines():
        fields = line.split()
        if len(fields) == 3:
            try:
                symbols[fields[2]] = int(fields[0], 16)
            except ValueError:
                continue
    return symbols


def read_object_symbols(path: Path, nm: str) -> dict[str, int]:
    if not path.is_file():
        return {}
    return read_symbols(path, nm)


def read_charmap(path: Path) -> dict[str, bytes]:
    result = {}
    warnings.filterwarnings("ignore", category=SyntaxWarning)
    for line in path.read_text(encoding="utf-8").splitlines():
        match = CHARMAP_RE.match(line)
        if match:
            key = match.group(1)
            if key.startswith("'"):
                key = ast.literal_eval(key)
            result[key] = bytes.fromhex(match.group(2))
    return result


def encode_japanese(body: str, charmap: dict[str, bytes]) -> bytes | None:
    parts = STRING_RE.findall(body)
    if not parts:
        return None
    text = "".join(ast.literal_eval(part) for part in parts)
    result = bytearray()
    index = 0
    while index < len(text):
        char = text[index]
        if char == "$":
            result.append(0xFF)
            index += 1
        elif char == "{":
            end = text.find("}", index)
            control = text[index + 1 : end] if end >= 0 else ""
            if control.startswith("PAUSE "):
                try:
                    duration = int(control[6:])
                except ValueError:
                    return None
                if not 0 <= duration <= 255:
                    return None
                result.extend((0xFC, 0x08, duration))
                index = end + 1
                continue
            encoded = charmap.get(control) if end >= 0 else None
            if encoded is None:
                return None
            result.extend(encoded)
            index = end + 1
        elif char == "\\" and text[index : index + 2] in charmap:
            result.extend(charmap[text[index : index + 2]])
            index += 2
        else:
            encoded = charmap.get(char)
            if encoded is None:
                return None
            result.extend(encoded)
            index += 1
    return bytes(result)


def occurrences(data: bytes, needle: bytes) -> list[int]:
    result = []
    cursor = 0
    while True:
        offset = data.find(needle, cursor)
        if offset < 0:
            return result
        result.append(ROM_BASE + offset)
        cursor = offset + 1


def existing_entries() -> tuple[set[str], set[str]]:
    symbols = set()
    references = set()
    for path in (ROOT / "patch/batches").glob("*.json"):
        batch = json.loads(path.read_text(encoding="utf-8"))
        symbols.update(entry.get("source_symbol") for entry in batch.get("texts", []))
        references.update(entry["address"] for entry in batch.get("reference_writes", []))
    return symbols, references


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="batch file stem")
    parser.add_argument("--nm", required=True)
    parser.add_argument(
        "--wokann-event-scripts-object",
        type=Path,
        default=WOKANN_ROOT / "build/pokeemerald-jp/data/event_scripts.o",
        help="baseline Wokann event_scripts.o with source text-label symbols",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="merge verified additions into the named batch and mapping report",
    )
    parser.add_argument(
        "--report-sources",
        action="store_true",
        help="reuse the source paths recorded in the batch's existing mapping report",
    )
    parser.add_argument("--source-commit", default="fe570a7e5")
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument(
        "--symbol",
        action="append",
        default=[],
        help="restrict processing to these US text symbols",
    )
    parser.add_argument("--label-offset", type=int, default=0)
    parser.add_argument("--label-limit", type=int)
    parser.add_argument(
        "--japanese-placeholder",
        action="append",
        type=int,
        default=[],
        help="placeholder ID whose runtime value is verified as Japanese-mode data",
    )
    parser.add_argument(
        "--chinese-placeholder",
        action="append",
        type=int,
        default=[],
        help="placeholder ID whose runtime value is verified as compact-Chinese data",
    )
    parser.add_argument("maps", nargs="*")
    args = parser.parse_args()
    if args.report_sources:
        report_path = ROOT / "patch/mapping_reports" / (args.name + ".json")
        report = json.loads(report_path.read_text(encoding="utf-8"))
        report_sources = report.get("selection", {}).get("sources")
        if report_sources is not None:
            args.source.extend(report_sources)
        else:
            report_sources = sorted(
                {
                    entry["source"]
                    for entry in report.get("mapped", []) + report.get("unresolved", [])
                    if "source" in entry
                }
            )
            if report_sources:
                args.source.extend(report_sources)
            else:
                batch_path = ROOT / "patch/batches" / (args.name + ".json")
                category = json.loads(batch_path.read_text(encoding="utf-8"))["category"]
                if not category.startswith("map dialogue: "):
                    parser.error(f"cannot recover sources from report or category: {category}")
                args.maps.extend(category.removeprefix("map dialogue: ").split(", "))
    sources = [f"data/maps/{map_name}/scripts.inc" for map_name in args.maps] + args.source
    if not sources:
        parser.error("provide at least one map or --source path")

    us_rom_path = US_ROOT / "pokeemerald.gba"
    us_elf_path = US_ROOT / "pokeemerald.elf"
    jp_rom_path = ROOT / "pokeemerald_jp.gba"
    us_rom = us_rom_path.read_bytes()
    jp_rom = jp_rom_path.read_bytes()
    symbols = read_symbols(us_elf_path, args.nm)
    wokann_symbols = read_object_symbols(args.wokann_event_scripts_object, args.nm)
    charmap = read_charmap(WOKANN_ROOT / "charmap.txt")
    japanese_placeholders = {1, 5, 6, *args.japanese_placeholder}
    chinese_placeholders = set(args.chinese_placeholder)
    allowed_placeholders = japanese_placeholders | chinese_placeholders
    selected_symbols = set(args.symbol)
    ported, used_references = existing_entries()
    texts = []
    references = []
    mapped = []
    unresolved = []

    for source in sources:
        us_source = (US_ROOT / source).read_text(encoding="utf-8")
        jp_path = WOKANN_ROOT / source
        jp_paths = [jp_path] if jp_path.exists() else sorted(jp_path.with_suffix("").glob("*.inc"))
        if not jp_paths:
            for label_index, match in enumerate(TEXT_RE.finditer(us_source)):
                if label_index < args.label_offset or (
                    args.label_limit is not None and label_index >= args.label_offset + args.label_limit
                ):
                    continue
                symbol, body = match.groups()
                if symbol not in ported and re.search(r"[\u3400-\u9fff]", body):
                    unresolved.append({"symbol": symbol, "source": source, "reason": "missing_wokann_source"})
            continue
        jp_sources = [(path, path.read_text(encoding="utf-8")) for path in jp_paths]
        for label_index, match in enumerate(TEXT_RE.finditer(us_source)):
            if label_index < args.label_offset or (
                args.label_limit is not None and label_index >= args.label_offset + args.label_limit
            ):
                continue
            symbol, body = match.groups()
            if selected_symbols and symbol not in selected_symbols:
                continue
            if symbol in ported or not re.search(r"[\u3400-\u9fff]", body):
                continue

            japanese_label = None
            for label_path, jp_source in jp_sources:
                japanese_label = re.search(
                    rf"^{re.escape(symbol)}::?\s*(?:@\s*0x([0-9A-Fa-f]{{8}}))?\s*\n"
                    rf"((?:\s*\.string .*\n)+)",
                    jp_source,
                    re.MULTILINE,
                )
                if japanese_label is not None:
                    break
            if japanese_label is None:
                unresolved.append({"symbol": symbol, "source": source, "reason": "no_japanese_text_label"})
                continue

            object_offset = wokann_symbols.get(symbol)
            if object_offset is not None:
                target = WOKANN_EVENT_SCRIPTS_ROM_START + object_offset
                encoded_japanese = encode_japanese(japanese_label.group(2), charmap)
                if encoded_japanese is None or not jp_rom[target - ROM_BASE :].startswith(encoded_japanese):
                    unresolved.append({"symbol": symbol, "source": source, "reason": "wokann_object_symbol_mismatch"})
                    continue
                candidates = [target]
                method = "wokann_event_scripts_object_symbol"
            elif japanese_label.group(1):
                candidates = [int(japanese_label.group(1), 16)]
                method = "wokann_address_comment"
            else:
                encoded_japanese = encode_japanese(japanese_label.group(2), charmap)
                if encoded_japanese is None:
                    unresolved.append({"symbol": symbol, "source": source, "reason": "unsupported_japanese_encoding"})
                    continue
                candidates = occurrences(jp_rom, encoded_japanese)
                method = "exact_wokann_japanese_bytes"

            linked = []
            for target in candidates:
                if ROM_BASE <= target < ROM_BASE + len(jp_rom):
                    for reference in occurrences(jp_rom, struct.pack("<I", target)):
                        linked.append((target, reference))
            targets = {target for target, _ in linked}
            if len(targets) != 1:
                reason = "no_japanese_pointer" if not targets else "ambiguous_japanese_text"
                unresolved.append({"symbol": symbol, "source": source, "reason": reason})
                continue
            if symbol not in symbols:
                unresolved.append({"symbol": symbol, "source": source, "reason": "no_us_elf_symbol"})
                continue

            offset = symbols[symbol] - ROM_BASE
            end = us_rom.find(b"\xFF", offset, offset + 4096)
            if end < 0:
                unresolved.append({"symbol": symbol, "source": source, "reason": "no_us_text_eos"})
                continue
            encoded_us = us_rom[offset : end + 1]
            placeholders = sorted({encoded_us[index + 1] for index, value in enumerate(encoded_us[:-1]) if value == 0xFD})
            if any(value not in allowed_placeholders for value in placeholders) or 0xF7 in encoded_us:
                unresolved.append({"symbol": symbol, "source": source, "reason": "placeholder_review_required", "placeholders": placeholders})
                continue
            if any(f"0x{reference:08X}" in used_references for _, reference in linked):
                unresolved.append({"symbol": symbol, "source": source, "reason": "reference_already_patched"})
                continue

            text_name = "Chs_" + symbol
            definition = {"name": text_name, "source_symbol": symbol, "us_encoded_hex": encoded_us.hex()}
            japanese_runtime_placeholders = sorted(set(placeholders) & japanese_placeholders)
            if japanese_runtime_placeholders:
                definition["japanese_placeholders"] = japanese_runtime_placeholders
            texts.append(definition)
            target = next(iter(targets))
            jp_references = []
            for _, reference in linked:
                address = f"0x{reference:08X}"
                used_references.add(address)
                jp_references.append(address)
                references.append({"address": address, "original": f"0x{target:08X}", "symbol": text_name, "source_symbol": symbol})
            mapped.append({"source_symbol": symbol, "source": source, "wokann_source": str(label_path.relative_to(WOKANN_ROOT)), "wokann_label_line": jp_source.count("\n", 0, japanese_label.start()) + 1, "mapping_method": method, "us_text_address": f"0x{symbols[symbol]:08X}", "japanese_text_address": f"0x{target:08X}", "japanese_references": jp_references})

    source_commit = args.source_commit
    batch_name = args.name + ".json"
    batch = {"source_commit": source_commit, "category": "dialogue: " + ", ".join(sources), "texts": texts, "reference_writes": references, "mapping_report": {"report_file": "patch/mapping_reports/" + batch_name, "mapped_count": len(mapped), "unresolved_count": len(unresolved)}}
    report = {"schema_version": 1, "batch": batch_name, "source_commit": source_commit, "selection": {"sources": sources, "symbols": sorted(selected_symbols), "label_offset": args.label_offset, "label_limit": args.label_limit, "japanese_placeholders": sorted(japanese_placeholders), "chinese_placeholders": sorted(chinese_placeholders)}, "inputs": {"us_rom_sha1": hashlib.sha1(us_rom).hexdigest(), "us_elf_sha1": hashlib.sha1(us_elf_path.read_bytes()).hexdigest(), "jp_rom_sha1": hashlib.sha1(jp_rom).hexdigest(), "wokann_commit": subprocess.check_output(["git", "-C", str(WOKANN_ROOT), "rev-parse", "HEAD"], text=True).strip()}, "mapping_policy": {"source": "Wokann dev text label address or exact encoded Japanese source string; every JP ROM pointer word is verified.", "us_text": "Exact EOS-terminated bytes from the translated US ROM at ELF symbol address.", "placeholders": "Only verified Japanese-mode runtime placeholders are auto-wrapped; compact-Chinese placeholders remain in the default Chinese mode. The selected IDs are recorded above."}, "mapped_count": len(mapped), "unresolved_count": len(unresolved), "reference_count": len(references), "mapped": mapped, "unresolved": unresolved}
    if args.update:
        batch_path = ROOT / "patch/batches" / batch_name
        report_path = ROOT / "patch/mapping_reports" / batch_name
        existing_batch = json.loads(batch_path.read_text(encoding="utf-8"))
        existing_report = json.loads(report_path.read_text(encoding="utf-8"))
        batch["texts"] = existing_batch["texts"] + texts
        batch["reference_writes"] = existing_batch["reference_writes"] + references
        report["mapped"] = existing_report["mapped"] + mapped
        if selected_symbols:
            report["unresolved"] = [
                entry
                for entry in existing_report.get("unresolved", [])
                if entry.get("symbol") not in selected_symbols
            ] + unresolved
        batch["mapping_report"] = {
            "report_file": "patch/mapping_reports/" + batch_name,
            "mapped_count": len(report["mapped"]),
            "unresolved_count": len(report["unresolved"]),
        }
        report["mapped_count"] = len(report["mapped"])
        report["unresolved_count"] = len(report["unresolved"])
        report["reference_count"] = len(batch["reference_writes"])
        batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"batch": batch_name, "added_texts": len(texts), "added_references": len(references), "unresolved": len(unresolved)}, ensure_ascii=False))
    else:
        print(json.dumps({"batch": batch, "report": report}, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
