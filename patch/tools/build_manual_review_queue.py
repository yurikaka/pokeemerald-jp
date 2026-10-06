#!/usr/bin/env python3
"""Build the manual text-override review queue as JSONL.

Enumerates every reference override recorded by the strict audit and attaches
decoded Japanese original bytes, the Chinese replacement text, and the audit
evidence. The tool only *enumerates and decodes*; every verdict must be
recorded manually in the ledger fields. Existing verdicts are preserved by
key when the queue is regenerated.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from port_map_dialogue import read_charmap

ROOT = Path(__file__).resolve().parents[2]
WOKANN = ROOT.parent / "pokeemerald_wokann_dev"
US = ROOT.parent / "pokeemerald_us_chs"
ROM_BASE = 0x08000000
OUT_DIR = ROOT / "patch/mapping_reports/manual_review"
QUEUE_PATH = OUT_DIR / "queue.jsonl"

PLACEHOLDERS = {
    0x01: "PLAYER", 0x02: "STR_VAR_1", 0x03: "STR_VAR_2", 0x04: "STR_VAR_3",
    0x05: "KUN", 0x06: "RIVAL", 0x07: "VERSION", 0x08: "EVIL_TEAM",
    0x09: "GOOD_TEAM", 0x0A: "EVIL_LEADER", 0x0B: "GOOD_LEADER",
    0x0C: "EVIL_LEGENDARY", 0x0D: "GOOD_LEGENDARY",
}
BUFFERS = {0xF7: "BUFF1", 0xF8: "BUFF2", 0xF9: "BUFF3"}
EXT_CTRL_ARG_LENGTHS = {
    0x01: 1, 0x02: 1, 0x03: 1, 0x04: 2, 0x05: 2, 0x06: 1, 0x07: 1, 0x08: 1,
    0x09: 1, 0x0B: 1, 0x0C: 1, 0x0D: 1, 0x0E: 1, 0x0F: 1, 0x10: 1, 0x11: 1,
    0x12: 1, 0x13: 1, 0x14: 1, 0x15: 0, 0x16: 0, 0x17: 0, 0x18: 0, 0x1A: 1,
    0x1B: 1, 0x1C: 1, 0x1D: 1, 0x1E: 1, 0x1F: 1, 0x20: 1, 0x21: 1, 0x22: 1,
    0x23: 1, 0x24: 1,
}


def reversed_charmap(charmap: dict[str, bytes]) -> dict[bytes, str]:
    # Only quoted single characters are printable glyphs; symbolic constants
    # (SE_*, MUS_*, @WHITE, ...) collide with real byte values and must not
    # win. On duplicate bytes the later definition wins so that fullwidth
    # punctuation sections override earlier ASCII/kana aliases.
    result: dict[bytes, str] = {}
    for char, encoded in charmap.items():
        if len(char) != 1:
            continue
        result[encoded] = char
    return result


ARROWS = {0x79: "{UP_ARROW}", 0x7A: "{DOWN_ARROW}", 0x7B: "{LEFT_ARROW}", 0x7C: "{RIGHT_ARROW}"}


def decode_text(data: bytes, reverse: dict[bytes, str], us_mode: bool = False) -> str:
    out: list[str] = []
    index = 0
    while index < len(data):
        char = data[index]
        if char == 0xFF:
            break
        if char == 0xFC:
            code = data[index + 1] if index + 1 < len(data) else 0
            arg_length = EXT_CTRL_ARG_LENGTHS.get(code, 0)
            end = min(index + 2 + arg_length, len(data))
            out.append("{FC" + data[index + 1:end].hex().upper() + "}")
            index = end
            continue
        if char == 0xFD:
            if index + 1 < len(data):
                out.append("{" + PLACEHOLDERS.get(data[index + 1], f"FD{data[index + 1]:02X}") + "}")
            index += 2
            continue
        if char in BUFFERS:
            if index + 1 < len(data):
                out.append("{" + BUFFERS[char] + f":{data[index + 1]:02X}" + "}")
            index += 2
            continue
        if char == 0xF5:
            sub = data[index + 1] if index + 1 < len(data) else 0
            if sub == 0xF1 and index + 2 < len(data):
                out.append(f"{{COMPACT:{data[index + 2]}}}")
                index += 3
            elif sub == 0xF3:
                out.append("{NARROW}")
                index += 2
            else:
                out.append(f"{{F5{sub:02X}}}")
                index += 2
            continue
        if char == 0xFA:
            out.append("{FA}")
            index += 1
            continue
        if char == 0xFB:
            out.append("{FB}")
            index += 1
            continue
        if char == 0xFE:
            out.append("\\n")
            index += 1
            continue
        if us_mode and char in ARROWS:
            out.append(ARROWS[char])
            index += 1
            continue
        pair = data[index:index + 2]
        if len(pair) == 2 and pair in reverse:
            out.append(reverse[pair])
            index += 2
            continue
        single = data[index:index + 1]
        if single in reverse:
            out.append(reverse[single])
        else:
            out.append(f"<{char:02X}>")
        index += 1
    return "".join(out)


def find_named(node, symbol: str):
    if isinstance(node, dict):
        if node.get("name") == symbol:
            return node
        for value in node.values():
            found = find_named(value, symbol)
            if found is not None:
                return found
    elif isinstance(node, list):
        for value in node:
            found = find_named(value, symbol)
            if found is not None:
                return found
    return None


def chinese_of(definition, us_reverse) -> str:
    if definition is None:
        return ""
    if "text" in definition:
        return definition["text"]
    if "us_encoded_hex" in definition:
        return decode_text(bytes.fromhex(definition["us_encoded_hex"]), us_reverse, us_mode=True)
    if "strings" in definition:
        parts = []
        for entry in definition["strings"]:
            if isinstance(entry, dict):
                parts.append(chinese_of(entry, us_reverse))
            else:
                parts.append(str(entry))
        return " | ".join(parts)
    return ""


def main() -> None:
    base = (ROOT / "baserom_jp.gba").read_bytes()
    jp_reverse = reversed_charmap(read_charmap(WOKANN / "charmap.txt"))
    us_reverse = reversed_charmap(read_charmap(US / "charmap.txt"))
    references = json.loads(
        (ROOT / "patch/mapping_reports/batch_text_reference_types/references.json").read_text()
    )["references"]

    old_verdicts = {}
    if QUEUE_PATH.exists():
        for line in QUEUE_PATH.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            record = json.loads(line)
            key = (record["batch"], record["index"], record["address"])
            if record.get("verdict"):
                old_verdicts[key] = (record["verdict"], record.get("notes", ""))

    batch_cache: dict[str, dict] = {}
    records = []
    for ref in references:
        batch_name = ref["batch"]
        if batch_name not in batch_cache:
            batch_cache[batch_name] = json.loads((ROOT / "patch/batches" / batch_name).read_text())
        batch = batch_cache[batch_name]
        definition = find_named(batch, ref["symbol"])
        original = int(ref["original"], 16) - ROM_BASE
        jp = ""
        if 0 <= original < len(base):
            end = base.find(b"\xff", original, min(original + 512, len(base)))
            if end != -1:
                jp = decode_text(base[original:end + 1], jp_reverse)
        key = (batch_name, ref["index"], ref["address"])
        verdict, notes = old_verdicts.get(key, ("", ""))
        target_files = sorted({e.get("file", "") for e in ref.get("target_evidence", []) if e.get("file")})
        records.append({
            "batch": batch_name,
            "index": ref["index"],
            "address": ref["address"],
            "original": ref["original"],
            "symbol": ref["symbol"],
            "source_symbol": ref.get("source_symbol", ""),
            "audit_status": ref["status"],
            "jp": jp,
            "cn": chinese_of(definition, us_reverse),
            "target_files": target_files,
            "verdict": verdict,
            "notes": notes,
        })

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with QUEUE_PATH.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    counts = Counter(record["audit_status"] for record in records)
    verdict_counts = Counter(record["verdict"] or "pending" for record in records)
    print(f"records: {len(records)}")
    print(f"audit status: {dict(counts)}")
    print(f"verdicts: {dict(verdict_counts)}")


if __name__ == "__main__":
    main()
