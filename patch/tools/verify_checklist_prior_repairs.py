#!/usr/bin/env python3
"""Read-only batch145 audit; write only a separate evidence report, never build.

Run from any directory: python3 path/to/verify_checklist_prior_repairs.py
Exit 1 means a current-resource failure or an unresolved coverage gap; stale
optional US modern artifacts are reported separately, not counted as repairs.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess
import sys
import warnings

from audit_batches_against_wokann import load_reference_index, load_text_label_index
from build_texts import convert_us_encoded_text, encode_text, wrap_dialogue
from build_texts import read_charmap as read_chinese_charmap
from port_map_dialogue import read_charmap, read_symbols
from review_text_checklists import decode_text, encode_source_controls, read_sources
from verify_wokann_object_references import object_sections


ROOT = Path(__file__).resolve().parents[2]
ROM_BASE = 0x08000000
PLAN_NAME = "batch_145_fix_plan_2026-10-01.md"
TRACKER_NAME = "patch/mapping_reports/checklists_action_plan_2026-10-02.json"
REPAIRS_NAME = "patch/mapping_reports/batch_145_repairs_2026-10-02.md"
REPORT_NAME = "patch/mapping_reports/checklist_prior_repair_verification.json"
US_ALIASES = {
    "SlateportCity_OceanicMuseum_2F_Text_SubmersibleReplica":
        "SlateportCity_OceanicMuseum_2F_Text_SumbersibleReplica",
}


def hex_address(value):
    return None if value is None else f"0x{value:08X}"


def normalize(text):
    return text.replace("\\n", "\n")


def word(data, address):
    offset = address - ROM_BASE
    if 0 <= offset <= len(data) - 4:
        return struct.unpack_from("<I", data, offset)[0]
    return None


def at(data, address, size):
    offset = address - ROM_BASE
    return data[offset:offset + size] if 0 <= offset <= len(data) - size else b""


def occurrences(data, needle):
    if not needle:
        return []
    result = []
    offset = data.find(needle)
    while offset >= 0:
        result.append(ROM_BASE + offset)
        offset = data.find(needle, offset + 1)
    return result


def elf_bytes(path, address, size):
    data = path.read_bytes()
    if data[:7] != b"\x7fELF\x01\x01\x01":
        raise ValueError(f"Not a little-endian ELF32: {path}")
    header = struct.unpack_from("<16sHHIIIIIHHHHHH", data)
    for index in range(header[12]):
        section = struct.unpack_from("<IIIIIIIIII", data, header[6] + index * header[11])
        if section[1] == 1 and section[2] & 2 and section[3] <= address and address + size <= section[3] + section[5]:
            offset = section[4] + address - section[3]
            return data[offset:offset + size]
    return b""


def parse_documents(plan_text, repairs_text):
    plan = {}
    pattern = r"(?m)^## (\d+)\. idx=(\d+) \| ([^\n]+)\n"
    matches = list(re.finditer(pattern, plan_text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(plan_text)
        body = plan_text[match.end():end]
        final = re.search(r"\*\*最终中文\*\*：\s*```text\n(.*?)\n```", body, re.S)
        plan[int(match[1])] = {
            "idx": match[2], "symbol": match[3],
            "line": plan_text.count("\n", 0, match.start()) + 1,
            "text": normalize(final[1]) if final else None,
            "implemented": "**状态**：已修复" in body,
            "implementation": body.split("### 实施结果", 1)[-1].strip(),
        }
    repairs = {}
    matches = list(re.finditer(r"(?m)^### (\d+)\. ([^\n]+)\n", repairs_text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(repairs_text)
        body = repairs_text[match.end():end]
        final = re.search(r"```text\n(.*?)\n```", body, re.S)
        batch = re.search(r"批次：`([^`]+)`", body)
        repairs[int(match[1])] = {
            "symbol": match[2], "line": repairs_text.count("\n", 0, match.start()) + 1,
            "text": normalize(final[1]) if final else None,
            "batch": batch[1] if batch else None,
            "implemented": "状态：已修复" in body,
            "note": re.search(r"处理：(.*)", body)[1],
        }
    return plan, repairs


class Audit:
    def __init__(self, root, nm):
        self.root = root
        self.us = root.parent / "pokeemerald_us_chs"
        self.wokann = root.parent / "pokeemerald_wokann_dev"
        self.nm = nm
        self.inputs = {}
        self.base = self.read(root / "baserom_jp.gba")
        self.jp_rom = self.optional_read(root / "pokeemerald_jp_chs.gba")
        self.payload = self.optional_read(root / "build/patch/payload.bin")
        self.manifest = json.loads(self.read(root / "patch/manifest.json"))
        self.payload_base = int(self.manifest["payload_address"], 0)
        self.jp_symbols = self.symbols(root / "build/patch/payload.elf")
        self.us_sources = read_sources(self.us)
        self.jp_sources = read_sources(self.wokann)
        self.us_map = read_charmap(self.us / "charmap.txt")
        self.jp_map = read_charmap(self.wokann / "charmap.txt")
        self.chinese_map = read_chinese_charmap(root / "patch/charmap_chs.txt")
        for path in (self.us / "charmap.txt", self.wokann / "charmap.txt", root / "patch/charmap_chs.txt"):
            self.read(path)
        self.labels = load_text_label_index(self.wokann)
        self.references = load_reference_index(self.wokann)
        self.documents = {}
        self.definitions = defaultdict(list)
        self.writes = defaultdict(list)
        for path in [root / "patch/texts.json", *sorted((root / "patch/batches").glob("*.json"))]:
            document = json.loads(self.read(path))
            relative = str(path.relative_to(root))
            self.documents[relative] = document
            for definition in document if isinstance(document, list) else document.get("texts", []):
                self.definitions[definition["name"]].append((relative, definition))
            if isinstance(document, dict):
                for reference in document.get("reference_writes", []):
                    self.writes[int(reference["address"], 0)].append({"file": relative, **reference})
        for reference in self.manifest.get("pointer_writes", []):
            self.writes[int(reference["address"], 0)].append({"file": "patch/manifest.json", **reference})
        generated = self.optional_read(root / "build/patch/texts.inc").decode()
        self.generated = {
            match[1]: bytes(int(value, 16) for value in re.findall(r"0x([0-9A-Fa-f]{2})", match[2]))
            for match in re.finditer(r"(?m)^(\w+):\n\s*\.byte ([^\n]+)", generated)
        }
        self.us_builds = {}
        for stem in ("pokeemerald", "pokeemerald_modern"):
            self.us_builds[stem] = {
                "rom": self.optional_read(self.us / (stem + ".gba")),
                "symbols": self.symbols(self.us / (stem + ".elf")),
                "elf": self.us / (stem + ".elf"),
            }
        self.event_relocations = {}
        self.event_symbols = {}
        event = self.wokann / "build/pokeemerald-jp/data/event_scripts.o"
        if event.exists():
            self.event_symbols = self.symbols(event)
            for section, contents, relocations in object_sections(event):
                if section == "script_data":
                    self.event_relocations = {entry["offset"]: entry for entry in relocations if entry["type"] == 2}
                    self.event_contents = contents
        self.event_bases = Counter()
        for address, labels in self.labels.items():
            for label in labels:
                if label["file"].startswith("data/") and label["symbol"] in self.event_symbols:
                    self.event_bases[address - self.event_symbols[label["symbol"]]] += 1
        self.event_base = self.event_bases.most_common(1)[0][0] if self.event_bases else None

    def read(self, path):
        data = path.read_bytes()
        self.inputs[str(path.relative_to(self.root.parent))] = {
            "sha256": hashlib.sha256(data).hexdigest(), "size": len(data),
            "mtime_ns": path.stat().st_mtime_ns,
        }
        return data

    def optional_read(self, path):
        return self.read(path) if path.exists() else b""

    def symbols(self, path):
        if not path.exists():
            return {}
        self.read(path)
        return read_symbols(path, self.nm)

    def source(self, root, symbol, sources):
        result = []
        for entry in sources.get(symbol, []):
            text = self.read(root / entry["file"]).decode()
            match = re.search(r"\b" + re.escape(symbol) + r"\b(?:\[\]|::?)", text)
            result.append({**entry, "symbol": symbol, "line": text.count("\n", 0, match.start()) + 1 if match else None})
        return result

    def snippet(self, root, filename, pattern, before=0, after=4):
        source = self.read(root / filename).decode()
        match = re.search(pattern, source)
        if match is None:
            return {"file": filename, "found": False}
        line = source.count("\n", 0, match.start())
        start = max(0, line - before)
        return {"file": filename, "line": start + 1, "found": True,
                "text": "\n".join(source.splitlines()[start:line + after + 1])}

    def emit(self, definition, document):
        if "us_encoded_hex" in definition:
            encoded = convert_us_encoded_text(bytes.fromhex(definition["us_encoded_hex"]),
                set(definition.get("japanese_placeholders", [])), definition.get("japanese_dynamic", False),
                definition.get("initial_japanese", False))
        else:
            encoded = encode_text(definition["text"], self.chinese_map, definition.get("styled", False))
        auto_wrap = definition.get("auto_wrap", isinstance(document, dict) and "dialogue" in document.get("category", "").lower())
        if auto_wrap:
            encoded, changed = wrap_dialogue(encoded, self.chinese_map)
        else:
            changed = 0
        return encoded, {"auto_wrap": auto_wrap, "wrapped_pages": changed}

    def payload_evidence(self, definition, document):
        encoded, layout = self.emit(definition, document)
        name = definition["name"]
        target = self.jp_symbols.get(name)
        actual = at(self.jp_rom, target, len(encoded)) if target else b""
        payload_offset = target - self.payload_base if target else -1
        payload = self.payload[payload_offset:payload_offset + len(encoded)] if payload_offset >= 0 else b""
        linked = elf_bytes(self.root / "build/patch/payload.elf", target, len(encoded)) if target else b""
        return {"symbol": name, "address": hex_address(target), "expected_hex": encoded.hex(),
                "rom_actual_hex": actual.hex(), "rom_bytes_match": actual == encoded,
                "payload_bin_matches": payload == encoded, "payload_elf_matches": linked == encoded,
                "generated_texts_inc_matches": self.generated.get(name) == encoded,
                "eos_at_end": encoded.endswith(b"\xff"), **layout}

    def us_evidence(self, symbol, expected):
        resolved = US_ALIASES.get(symbol, symbol)
        sources = self.source(self.us, resolved, self.us_sources)
        evidence = {"symbol": resolved, "explicit_alias": resolved != symbol, "sources": sources, "builds": {}}
        if len(sources) != 1:
            evidence["source_matches"] = False
            return evidence
        text = normalize(sources[0]["text"])
        evidence["source_matches"] = text.removesuffix("$") == expected
        evidence["eos_contract"] = "explicit ASM EOS" if sources[0]["file"].endswith(".inc") else "C string encoder appends EOS"
        evidence["source_has_required_eos"] = not sources[0]["file"].endswith(".inc") or text.endswith("$")
        encoded = encode_source_controls(text if text.endswith("$") else text + "$", self.us_map)
        evidence["encoded_hex"] = encoded.hex() if encoded is not None else None
        for stem, build in self.us_builds.items():
            address = build["symbols"].get(resolved)
            actual = at(build["rom"], address, len(encoded)) if encoded is not None and address else b""
            linked = elf_bytes(build["elf"], address, len(encoded)) if encoded is not None and address else b""
            evidence["builds"][stem] = {"address": hex_address(address), "present": bool(build["rom"]),
                "actual_hex": actual.hex(), "source_bytes_match": encoded is not None and actual == encoded,
                "elf_source_bytes_match": encoded is not None and linked == encoded}
        return evidence

    def wokann_text(self, symbol, original):
        sources = self.source(self.wokann, symbol, self.jp_sources)
        for source in sources:
            encoded = encode_source_controls(source["text"].removesuffix("$") + "$", self.jp_map)
            if encoded and at(self.base, original, len(encoded)) == encoded:
                return {"method": "named_source_full_bytes", "source": source, "original": hex_address(original),
                        "encoded_hex": encoded.hex(), "base_rom_matches": True}
        for candidate, entries in self.jp_sources.items():
            match = re.fullmatch(r"gUnknown_([0-9A-Fa-f]{7,8})", candidate)
            if not match or len(entries) != 1:
                continue
            start = int(match[1], 16)
            if not start <= original < start + 2048:
                continue
            encoded = encode_source_controls(entries[0]["text"].removesuffix("$") + "$", self.jp_map)
            offset = original - start
            if encoded and offset < len(encoded) and at(self.base, start, len(encoded)) == encoded:
                end = encoded.find(b"\xff", offset)
                return {"method": "composite_source_full_block_bytes", "source": self.source(self.wokann, candidate, self.jp_sources)[0],
                        "block_address": hex_address(start), "block_size": len(encoded), "offset": offset,
                        "encoded_hex": encoded[offset:end + 1].hex(), "decoded": decode_text(encoded[offset:end + 1], self.jp_map),
                        "base_rom_matches": True}
        if symbol == "gText_MenuRest":
            path = self.wokann / "data/reset_rtc_screen/jp/trailing_data.bin"
            data = self.read(path)
            start = 0x084E8B5C
            offset = original - start
            return {"method": "Wokann_INCBIN_full_block", "file": str(path.relative_to(self.wokann)),
                    "source": self.snippet(self.wokann, "src/data/reset_rtc_screen.h", "sResetRtcScreenTrailingData", after=0),
                    "alias": self.snippet(self.wokann, "src/data/reset_rtc_screen.h", r"\.set gUnknown_84E8B5C", after=0),
                    "block_address": hex_address(start), "offset": offset,
                    "decoded": decode_text(data[offset:], self.jp_map),
                    "base_rom_matches": 0 <= offset < len(data) and at(self.base, start, len(data)) == data}
        return {"method": "unresolved", "sources": sources, "labels": self.labels.get(original, []), "base_rom_matches": False}

    def pointer_evidence(self, reference):
        address = int(reference["address"], 0)
        original = int(reference["original"], 0)
        target = self.jp_symbols.get(reference["symbol"])
        if target is not None:
            target += int(str(reference.get("offset", "0")), 0)
        direct = self.references.get(address, [])
        for entry in direct:
            self.read(self.wokann / entry["file"])
        event = self.event_relocations.get(address - self.event_base) if self.event_base else None
        event_proof = None
        if event:
            offset = address - self.event_base
            addend = struct.unpack_from("<I", self.event_contents, offset)[0]
            known = self.event_symbols.get(event["symbol"])
            event_proof = {**event, "object": "build/pokeemerald-jp/data/event_scripts.o",
                "section_base": hex_address(self.event_base), "base_label_votes": self.event_bases[self.event_base],
                "addend": addend, "target_agrees": known is not None and self.event_base + known + addend == original,
                "base_context_hex": at(self.base, address - 2, 8).hex()}
        return {**reference, "base_actual": hex_address(word(self.base, address)),
                "base_matches": word(self.base, address) == original,
                "expected_payload": hex_address(target), "rom_actual": hex_address(word(self.jp_rom, address)),
                "rom_pointer_matches": target is not None and word(self.jp_rom, address) == target,
                "wokann_direct_references": direct, "wokann_event_relocation": event_proof,
                "all_current_writes_at_address": self.writes.get(address, [])}

    def remaining_references(self, originals):
        evidence = []
        for original in sorted(originals):
            for address in occurrences(self.base, struct.pack("<I", original)):
                if word(self.jp_rom, address) != original:
                    continue
                item = {"address": hex_address(address), "original": hex_address(original), "still_original_in_rom": True,
                        "patch_writes": self.writes.get(address, []), "classification": "unresolved_pointer_candidate"}
                relocation = self.event_relocations.get(address - self.event_base) if self.event_base else None
                if relocation:
                    offset = address - self.event_base
                    addend = struct.unpack_from("<I", self.event_contents, offset)[0]
                    target = self.event_symbols.get(relocation["symbol"])
                    context = at(self.base, address - 2, 8)
                    item["wokann_event_relocation"] = {**relocation, "section_base": hex_address(self.event_base), "addend": addend,
                        "target_agrees": target is not None and self.event_base + target + addend == original,
                        "context_hex": context.hex()}
                    if target is not None and self.event_base + target + addend == original and context[:2] == b"\x0f\x00" and context[6] == 9:
                        item["classification"] = "missing_event_msgbox_override"
                        item["wokann_consumer"] = self.snippet(self.wokann, "data/scripts/pc_transfer.inc", r"msgbox " + re.escape(relocation["symbol"]) + r",", before=3, after=1)
                if address in (0x0856585C, 0x08565864):
                    source = self.snippet(self.wokann, "src/naming_screen.c", r'"_080E2B1A:', after=9)
                    table = self.snippet(self.wokann, "src/naming_screen.c", r"_080E2B90: \.4byte", after=0)
                    item.update({"classification": "missing_naming_screen_text_table_override", "table_index": (address - 0x08565858) // 4,
                        "table_base": "0x08565858", "base_table_pointer_matches": word(self.base, 0x080E2B90) == 0x08565858,
                        "rom_table_pointer_unchanged": word(self.jp_rom, 0x080E2B90) == 0x08565858,
                        "wokann_consumer": source, "wokann_table_reference": table})
                    if not source["found"] or not table["found"] or not item["base_table_pointer_matches"] or not item["rom_table_pointer_unchanged"]:
                        item["classification"] = "unresolved_pointer_candidate"
                if address == 0x082978AD:
                    source = self.snippet(self.wokann, "asm/libgcc.s", r"^_082978A6:", after=6)
                    expected = bytes.fromhex("400852000028f7d1")
                    verified = at(self.base, 0x082978A6, len(expected)) == expected and at(self.jp_rom, 0x082978A6, len(expected)) == expected
                    item.update({"classification": "non_pointer_instruction_byte_collision" if source["found"] and verified else "unresolved_pointer_candidate",
                        "wokann_instructions": source, "instruction_bytes_match": verified,
                        "reason": "The four-byte match starts at an odd byte inside Thumb instructions, not a pointer field."})
                evidence.append(item)
        return evidence

    def audit_record(self, tracker, ordinal, plan, repaired):
        expected = repaired["text"]
        symbol = repaired["symbol"]
        result = {"tracker_idx": tracker["idx"], "tracker_symbol": tracker["symbol"],
            "tracker_document_line": tracker["document_line"], "batch145_entry": ordinal, "resolved_symbol": symbol,
            "expected_jp_text": expected, "documents": {"plan": plan, "repair_record": repaired},
            "checks": {}, "findings": [], "remaining_verification": []}
        checks = result["checks"]
        checks["document_identity_and_final_text"] = plan["idx"] == tracker["idx"] and plan["text"] == expected and repaired["implemented"] and plan["implemented"] and (tracker["symbol"] == symbol or tracker["symbol"] == "NOT_FOUND")
        us_expected = "可参加" if ordinal == 44 else expected.replace("投掷了宝可方块！", "投掷了{POKEBLOCK}！") if ordinal == 64 else expected
        result["expected_us_text"] = us_expected
        result["regional_exception"] = repaired["note"] if ordinal in (44, 64) else None
        us = self.us_evidence(symbol, us_expected)
        result["us"] = us
        checks["us_source"] = us["source_matches"] and us.get("source_has_required_eos", False)
        checks["us_primary_rom"] = us.get("builds", {}).get("pokeemerald", {}).get("source_bytes_match", False)
        checks["us_primary_elf"] = us.get("builds", {}).get("pokeemerald", {}).get("elf_source_bytes_match", False)
        batch = self.documents[repaired["batch"]]
        candidates = [entry for entry in batch["texts"] if entry.get("source_symbol") == symbol or entry["name"] == "Chs_" + symbol]
        checks["unique_jp_definition"] = len(candidates) == 1 and len(self.definitions[candidates[0]["name"]]) == 1
        if not checks["unique_jp_definition"]:
            result["remaining_verification"].append("Missing or ambiguous JP definition; do not select by translated text alone.")
            return result
        definition = candidates[0]
        expected_raw = encode_source_controls(expected + "$", self.us_map)
        result["jp_resource"] = {"file": repaired["batch"], "definition": definition,
            "expected_us_format_hex": expected_raw.hex() if expected_raw is not None else None}
        checks["jp_resource_text"] = (bytes.fromhex(definition["us_encoded_hex"]) == expected_raw if "us_encoded_hex" in definition else normalize(definition["text"]) == expected)
        payload = self.payload_evidence(definition, batch)
        result["jp_payload"] = payload
        for key in ("rom_bytes_match", "payload_bin_matches", "payload_elf_matches", "generated_texts_inc_matches", "eos_at_end"):
            checks["jp_" + key] = payload[key]
        refs = [entry for entry in batch["reference_writes"] if entry["symbol"] == definition["name"]]
        result["jp_references"] = [self.pointer_evidence(entry) for entry in refs]
        checks["jp_pointer_words"] = bool(refs) and all(entry["base_matches"] and entry["rom_pointer_matches"] for entry in result["jp_references"])
        originals = {int(entry["original"], 0) for entry in refs}
        result["wokann_original_text"] = [self.wokann_text(symbol, original) for original in sorted(originals)]
        checks["wokann_original_text_bytes"] = bool(originals) and all(entry["base_rom_matches"] for entry in result["wokann_original_text"])
        result["unredirected_original_byte_matches"] = self.remaining_references(originals)
        for candidate in result["unredirected_original_byte_matches"]:
            if candidate["classification"].startswith("missing_"):
                result["findings"].append({"severity": "repair_required", **candidate})
                result["remaining_verification"].append("Unpatched Wokann text consumer at " + candidate["address"] + "; review context and placeholder ABI before proposing any patch.")
            elif candidate["classification"] == "unresolved_pointer_candidate":
                result["remaining_verification"].append("Determine whether remaining byte match " + candidate["address"] + " is a real pointer; raw scanning alone is not proof.")
        if tracker["symbol"] == "NOT_FOUND":
            result["identity_recovery"] = "Resolved by tracker idx + batch145 entry + implementation symbol + unique definition, not text similarity. Tracker unchanged."
        return result


def main():
    warnings.filterwarnings("ignore", category=SyntaxWarning)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--nm", default="nm")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output or root / REPORT_NAME
    if output.resolve() in {root / TRACKER_NAME, root.parent / PLAN_NAME} or output.suffix != ".json":
        parser.error("Output must be a separate JSON evidence report, never a tracker or plan.")
    audit = Audit(root, args.nm)
    tracker = json.loads(audit.read(root / TRACKER_NAME))
    plan, repairs = parse_documents(audit.read(root.parent / PLAN_NAME).decode(), audit.read(root / REPAIRS_NAME).decode())
    targets = [entry for entry in tracker["records"] if entry.get("kind") == "repair" and entry.get("decision") == "already_fixed"]
    selected = []
    for entry in targets:
        numbers = [int(match[1]) for evidence in entry.get("evidence", []) if (match := re.fullmatch(re.escape(PLAN_NAME) + r" entry (\d+)", evidence))]
        if len(numbers) != 1:
            raise ValueError(f"Ambiguous batch145 link: {entry['idx']}")
        selected.append((entry, numbers[0]))
    implemented = {number for number, entry in repairs.items() if entry["implemented"]}
    if len(targets) != 121 or len({entry["idx"] for entry in targets}) != 121 or {number for _, number in selected} != implemented:
        raise ValueError("Expected a one-to-one mapping of 121 tracker rows to 121 implemented batch145 entries")
    records = []
    for entry, ordinal in selected:
        try:
            records.append(audit.audit_record(entry, ordinal, plan[ordinal], repairs[ordinal]))
        except (ValueError, KeyError, OSError, struct.error) as error:
            records.append({"tracker_idx": entry["idx"], "tracker_symbol": entry["symbol"], "batch145_entry": ordinal,
                "checks": {"audit_completed": False}, "findings": [], "remaining_verification": [f"{type(error).__name__}: {error}"]})
    for record in records:
        failed = [key for key, passed in record["checks"].items() if not passed]
        record["failed_checks"] = failed
        record["status"] = "repair_required" if record["findings"] or failed else "verification_gap" if record["remaining_verification"] else "verified_static"
    changed = []
    for relative, fingerprint in audit.inputs.items():
        path = root.parent / relative
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != fingerprint["sha256"]:
            changed.append(relative)
    revision = lambda path, *arguments: subprocess.check_output(["git", "-C", str(path), *arguments], text=True).strip()
    summary = dict(Counter(record["status"] for record in records))
    summary.update({"target_records": len(records), "jp_main_payload_matches": sum(record.get("jp_payload", {}).get("rom_bytes_match", False) for record in records),
        "us_primary_rom_matches": sum(record["checks"].get("us_primary_rom", False) for record in records),
        "us_modern_rom_matches": sum(record.get("us", {}).get("builds", {}).get("pokeemerald_modern", {}).get("source_bytes_match", False) for record in records),
        "missing_consumer_references": sum(len(record["findings"]) for record in records), "inputs_changed_during_audit": changed})
    report = {"schema_version": 1, "generated_at_utc": datetime.now(timezone.utc).isoformat(), "scope": "121 kind=repair, decision=already_fixed records, independently checked against current resources and already-built artifacts",
        "policy": "Read only: no tracker/plan/game edits, no build, no commit/push. A historical status is an expectation, never proof.",
        "repositories": {"jp_head": revision(root, "rev-parse", "HEAD"), "us_head": revision(audit.us, "rev-parse", "HEAD"),
            "wokann_head": revision(audit.wokann, "rev-parse", "HEAD"), "wokann_branch": revision(audit.wokann, "branch", "--show-current")},
        "summary": summary, "limits": ["Static bytes, symbols and source inspection only; no emulator/gameplay test or complete rebuild.",
            "Primary US artifact is pokeemerald.gba; pokeemerald_modern.gba is checked separately and may predate the repairs.",
            "All original-address byte matches are scanned, including unaligned event operands. Non-pointer collisions are not omissions.",
            "ELF/object timestamps do not establish freshness; actual bytes are compared. Missing artifacts or unproved mappings never pass."],
        "inputs": dict(sorted(audit.inputs.items())), "records": records}
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(output)
    return int(bool(changed or summary.get("repair_required") or summary.get("verification_gap")))


if __name__ == "__main__":
    sys.exit(main())
