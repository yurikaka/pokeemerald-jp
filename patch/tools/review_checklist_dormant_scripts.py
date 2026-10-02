#!/usr/bin/env python3
"""Audit unused event text labels using both source trees and ROM references."""

import argparse
from collections import defaultdict
import json
import re
import struct

from execute_verified_checklist import write_patch
from review_text_checklists import ROOT, US, WOKANN


def occurrences(repository, names):
    result = defaultdict(list)
    pattern = re.compile(r"\b(?:" + "|".join(re.escape(name) for name in names) + r")\b")
    for directory in ("data", "src", "include"):
        for path in (repository / directory).rglob("*"):
            if not path.is_file() or path.suffix not in (".c", ".h", ".s", ".inc"):
                continue
            for lineno, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
                for match in pattern.finditer(line):
                    result[match[0]].append({"file": str(path.relative_to(repository)), "line": lineno, "text": line.strip()})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--review", required=True)
    args = parser.parse_args()
    review = json.loads(open(args.review).read())
    candidates = [record for record in review["records"] if record.get("us_source") and record["us_source"][0]["file"].startswith("data/") and record.get("exact_jp_source_match") and not record.get("rom_pointer_candidates")]
    names = {record["symbol"] for record in candidates}
    if not names:
        return
    us_uses = occurrences(US, names)
    jp_uses = occurrences(WOKANN, names)
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    words = set()
    for alignment in range(4):
        end = alignment + (len(rom) - alignment) // 4 * 4
        words.update(value for (value,) in struct.iter_unpack("<I", rom[alignment:end]) if 0x081DABAC <= value < 0x08300000)
    plan_path = ROOT / "patch/mapping_reports/checklists_action_plan_2026-10-02.json"
    plan = json.loads(plan_path.read_text())
    index = {(record["kind"], record["document_line"]): record for record in plan["records"]}
    reviewed = []
    for candidate in candidates:
        symbol = candidate["symbol"]
        if len(us_uses[symbol]) != 1 or len(jp_uses[symbol]) != 1:
            continue
        label = re.compile(re.escape(symbol) + r"::?(?:\s*[@/].*)?$")
        if not label.fullmatch(us_uses[symbol][0]["text"]) or not label.fullmatch(jp_uses[symbol][0]["text"]):
            continue
        address = int(candidate["jp_address"], 0)
        proofs = [proof for proof in candidate.get("evidence", []) if proof.get("symbol") == symbol and "offset" in proof and int(proof["base"], 0) + proof["offset"] == address]
        if not proofs:
            continue
        end = rom.find(b"\xff", address - 0x08000000)
        if end < 0 or any(address <= value <= 0x08000000 + end for value in words):
            continue
        record = index[(candidate["kind"], candidate["document_line"])]
        if record.get("execution"):
            continue
        evidence = {"us_occurrences": us_uses[symbol], "jp_occurrences": jp_uses[symbol], "compiled_label": proofs, "jp_text_start": candidate["jp_address"], "jp_text_end": f"0x{0x08000000 + end:08X}", "rom_pointer_scan": "All four alignments: no absolute pointer to the start or any interior byte.", "scope": "No named consumers in either src/include/data tree. This establishes a dormant event-text definition, not an assertion that every string lacking a literal pointer is unused."}
        record["dormant_script_review"] = evidence
        record["decision"] = "dormant_script_definition"
        record["execution"] = "no_active_script_consumer"
        record["plan"] = "旧清单所称文本确实存在，但两版事件源码仅定义该标签，无调用；编译标签与地址一致，ROM无首址或内部字节指针。保留未被事件引用的残留文本，不新增猜测覆盖；如未来恢复该事件，再使用本条完整译文和原标签移植。"
        reviewed.append({"symbol": symbol, **evidence})
    write_patch(plan_path, plan)
    accumulated = [{"symbol": record["symbol"], **record["dormant_script_review"]} for record in plan["records"] if "dormant_script_review" in record]
    write_patch(ROOT / "patch/mapping_reports/checklist_dormant_script_definitions.json", {"reviewed": accumulated})
    print({"dormant_script_definitions": len(reviewed)})


if __name__ == "__main__":
    main()
