#!/usr/bin/env python3
"""Verify preserved checklist overrides against payload bytes and pointer words."""

import argparse
from collections import Counter
import json
from pathlib import Path
import struct

from build_texts import encode_text, wrap_dialogue
from execute_verified_checklist import write_patch
from port_map_dialogue import read_charmap, read_symbols
from review_text_checklists import ROOT, US, read_sources


SAVEGAME_CONTRACTS = {
    "gText_ContinueMenuPlayer": ("主人公 {JPN}{STR_VAR_1}{ENG}", "main_menu.c:1743: StringCopy copies the unmodified save playerName into gStringVar1, then expands only the display template."),
    "gText_ContinueMenuTime": ("冒险时间 {STR_VAR_1}:{STR_VAR_2}", "main_menu.c:1750: ConvertIntToDecimalStringN supplies playTimeHours/minutes in gStringVar1/2, then expands and draws gStringVar4."),
    "gText_ContinueMenuPokedex": ("宝可梦图鉴 {STR_VAR_1}", "main_menu.c:1758: Count is selected by national/Hoenn dex mode, converted into gStringVar1, expanded and drawn without changing save data."),
    "gText_ContinueMenuBadges": ("获得徽章 {STR_VAR_1}", "main_menu.c:1774: Badge flags are counted, converted into gStringVar1, expanded and drawn without writing the flags."),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--nm", required=True)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    definitions = {entry["name"]: entry for entry in json.loads((ROOT / "patch/texts.json").read_text())}
    symbols = read_symbols(ROOT / "build/patch/payload.elf", args.nm)
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    sources = read_sources(US)
    counts = Counter()
    for record in plan["records"]:
        if record.get("execution") != "existing_override_requires_semantic_review":
            continue
        evidence = []
        for conflict in record.get("existing_override_conflicts", []):
            name = conflict.get("existing_payload_symbol")
            if name not in definitions:
                continue
            definition = definitions[name]
            encoded = encode_text(definition["text"], charmap, definition.get("styled", False))
            if definition.get("auto_wrap", False):
                encoded, _ = wrap_dialogue(encoded, charmap)
            address = int(conflict["address"], 0)
            target = symbols[name]
            if struct.unpack_from("<I", rom, address - 0x08000000)[0] != target:
                raise ValueError((record["symbol"], "pointer differs", conflict))
            if rom[target - 0x08000000:target - 0x08000000 + len(encoded)] != encoded:
                raise ValueError((record["symbol"], "payload differs", name))
            proof = {"address": conflict["address"], "payload_symbol": name, "payload_address": f"0x{target:08X}", "text": definition["text"], "encoded_hex": encoded.hex(), "source": "patch/texts.json", "result": "Current ROM pointer and complete emitted bytes match existing definition."}
            if proof not in evidence:
                evidence.append(proof)
        if evidence:
            record["existing_override_rom_evidence"] = evidence
            record["remaining_verification"] = list(dict.fromkeys([*record.get("remaining_verification", []), "Preserved override bytes verified; independently judge regional wording, formatting and placeholder contract before declaring semantic completion."]))
            counts["preserved_overrides_rom_verified"] += 1
            current = sources.get(record["symbol"], [])
            if len(current) == 1:
                record["us_source"] = current
                source_text = current[0]["text"].split("$")[0]
                same = all(entry["text"].removesuffix("{JPN}") == source_text for entry in evidence)
                if same:
                    record["execution"] = "existing_override_verified_equal_us"
                    record["decision"] = "already_ported_verified_override"
                    record["remaining_verification"] = []
                    record["final_text"] = evidence[0]["text"]
                    record["semantic_review"] = {"result": "Complete current US text matches preserved JP translation; only an intentional trailing JPN mode restoration may differ.", "jp_source": record.get("exact_jp_source_match", []), "us_source": current, "evidence": "Wokann original text/layout plus current ROM pointer and emitted payload bytes."}
                    record["plan"] = "旧文档的未移植标记已过时：当前ROM指针与完整中文定义一致，正文逐字等于当前美版；末尾JPN是日文后续文本的语言恢复，不新增重复覆盖。"
                    counts["preserved_overrides_equal_current_us"] += 1
                elif record["symbol"] in SAVEGAME_CONTRACTS:
                    expected, contract = SAVEGAME_CONTRACTS[record["symbol"]]
                    if not all(entry["text"] == expected for entry in evidence):
                        raise ValueError((record["symbol"], "savegame template differs"))
                    record["execution"] = "existing_override_verified_jp_template"
                    record["decision"] = "already_ported_verified_override"
                    record["remaining_verification"] = []
                    record["final_text"] = expected
                    record["placeholder_contract"] = {"source": "../pokeemerald_wokann_dev/src/" + contract, "policy": "Preserve JP's combined label/value template; US label-only resources are not structurally equivalent. PlayerName is enclosed in JPN/ENG; numeric values use the existing renderer digit path. This consumer only expands a display buffer and never stores a translated name."}
                    record["plan"] = "已移植：日版原函数一次性展开标题和数值，美版对应资源仅包含标题；保留现有日版显示模板及占位符，不用美版标题直接替换导致数值消失。ROM指针和完整文本字节已验证。"
                    counts["preserved_jp_savegame_templates_verified"] += 1
    plan["existing_override_rom_verification_summary"] = dict(counts)
    write_patch(args.plan, plan)
    print(dict(counts))


if __name__ == "__main__":
    main()
