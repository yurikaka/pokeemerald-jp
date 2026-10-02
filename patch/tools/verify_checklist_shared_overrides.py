#!/usr/bin/env python3
"""Verify identical checklist aliases already covered by existing text overrides."""

import argparse
from collections import defaultdict
import json
import struct

from build_texts import convert_us_encoded_text, encode_text, wrap_dialogue
from execute_verified_checklist import write_patch
from port_map_dialogue import read_charmap, read_symbols
from review_text_checklists import ROOT, US, encode_source_controls, read_sources


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nm", required=True)
    args = parser.parse_args()
    definitions = {entry["name"]: entry for entry in json.loads((ROOT / "patch/texts.json").read_text())}
    references = defaultdict(list)
    manifest = json.loads((ROOT / "patch/manifest.json").read_text())
    for reference in manifest.get("pointer_writes", []):
        if "original" in reference and "symbol" in reference:
            references[int(reference["original"], 0)].append({"file": "patch/manifest.json", **reference})
    for path in (ROOT / "patch/batches").glob("*.json"):
        batch = json.loads(path.read_text())
        for definition in batch.get("texts", []):
            definitions[definition["name"]] = definition
        for reference in batch.get("reference_writes", []):
            references[int(reference["original"], 0)].append({"file": str(path.relative_to(ROOT)), **reference})
    sources = read_sources(US)
    us_charmap = read_charmap(US / "charmap.txt")
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    symbols = read_symbols(ROOT / "build/patch/payload.elf", args.nm)
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    plan_path = ROOT / "patch/mapping_reports/checklists_action_plan_2026-10-02.json"
    plan = json.loads(plan_path.read_text())
    verified = []
    for record in plan["records"]:
        if record.get("execution") == "shared_existing_override_verified":
            record.pop("execution")
        if record.get("execution") is None and record.get("decision") == "already_ported_verified_shared_text":
            record["decision"] = "partial_existing_override_requires_review"
            record["plan"] = "同址文本已有部分覆盖，但其他原始引用仍需逐个核验用途；不能凭一个已汉化调用就宣称所有调用已移植。保持现有安全覆盖，定位并对照Wokann剩余表项后再重定向。"
        if record.get("execution") or record["kind"] != "port" or not record.get("jp_address"):
            continue
        candidates = sources.get(record["symbol"], [])
        if len(candidates) != 1:
            continue
        text = candidates[0]["text"].split("$")[0]
        source_encoded = encode_source_controls(text + "$", us_charmap)
        if source_encoded is None:
            continue
        for reference in references.get(int(record["jp_address"], 0), []):
            name = reference["symbol"]
            definition = definitions.get(name)
            if definition is None or name not in symbols:
                continue
            same = definition.get("us_encoded_hex") == source_encoded.hex() or definition.get("text", "").removesuffix("{JPN}") == text
            if not same or not text:
                continue
            if "us_encoded_hex" in definition:
                encoded = convert_us_encoded_text(bytes.fromhex(definition["us_encoded_hex"]), set(definition.get("japanese_placeholders", [])), definition.get("japanese_dynamic", False), definition.get("initial_japanese", False))
            else:
                encoded = encode_text(definition["text"], charmap, definition.get("styled", False))
            if definition.get("auto_wrap", False):
                encoded, _ = wrap_dialogue(encoded, charmap)
            address = int(reference["address"], 0)
            target = symbols[name]
            if struct.unpack_from("<I", rom, address - 0x08000000)[0] != target:
                continue
            if rom[target - 0x08000000:target - 0x08000000 + len(encoded)] != encoded:
                continue
            equivalent_targets = {target}
            for sibling in references.get(int(record["jp_address"], 0), []):
                sibling_target = symbols.get(sibling["symbol"])
                if sibling_target is None:
                    continue
                sibling_definition = definitions.get(sibling["symbol"], {})
                sibling_same = sibling_definition.get("us_encoded_hex") == source_encoded.hex() or sibling_definition.get("text", "").removesuffix("{JPN}") == text
                if sibling_same and rom[sibling_target - 0x08000000:sibling_target - 0x08000000 + len(encoded)] == encoded:
                    equivalent_targets.add(sibling_target)
            candidate_targets = {address: struct.unpack_from("<I", rom, int(address, 0) - 0x08000000)[0] for address in record.get("rom_pointer_candidates", [])}
            remaining = [address for address, current_target in candidate_targets.items() if current_target not in equivalent_targets]
            if remaining:
                record["shared_override_partial_evidence"] = {"reference": reference, "verified_target": f"0x{target:08X}", "other_references_require_review": remaining}
                continue
            record["execution"] = "shared_existing_override_verified"
            record["decision"] = "already_ported_verified_shared_text"
            record["final_text"] = text
            record["us_source"] = candidates
            record["shared_override_evidence"] = {"reference": reference, "payload_address": f"0x{target:08X}", "encoded_hex": encoded.hex(), "text_equality": "The entire current US translation matches the existing definition, possibly with intentional trailing JPN restoration. Current ROM pointer and complete payload bytes verified."}
            record["shared_override_evidence"]["equivalent_payload_addresses"] = [f"0x{address:08X}" for address in sorted(equivalent_targets)]
            record["shared_override_evidence"]["verified_candidate_targets"] = {address: f"0x{current_target:08X}" for address, current_target in candidate_targets.items()}
            record.pop("shared_override_partial_evidence", None)
            record["remaining_verification"] = []
            record["plan"] = "已移植：此清单符号与另一个文本共用相同日版地址；现有覆盖正文等于完整美版文本，实际ROM指针和全部文本字节已验证。不为同一地址新增重复定义/覆盖。"
            verified.append(record["symbol"])
            break
    write_patch(plan_path, plan)
    print({"shared_existing_override_verified": len(verified), "symbols": verified})


if __name__ == "__main__":
    main()
