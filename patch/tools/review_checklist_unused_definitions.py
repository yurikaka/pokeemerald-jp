#!/usr/bin/env python3
"""Record explicit unused US definitions, without equating missing pointers with disuse."""

import argparse
import json
import re

from execute_verified_checklist import write_patch
from review_text_checklists import ROOT, US


EXPLICIT_UNUSED = {
    "sText_AwaitingCommunucation2": "src/data/union_room.h",
    "gText_NoWeather": "src/strings.c",
    "sText_SpaceMove": "src/data/trade.h",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--review", required=True)
    args = parser.parse_args()
    review = json.loads(open(args.review).read())
    latest = {(record["kind"], record["document_line"]): record for record in review["records"]}
    plan_path = ROOT / "patch/mapping_reports/checklists_action_plan_2026-10-02.json"
    plan = json.loads(plan_path.read_text())
    for record in plan["records"]:
        symbol = record.get("symbol")
        if symbol not in EXPLICIT_UNUSED:
            continue
        occurrences = []
        for directory in ("src", "include", "data"):
            for path in (US / directory).rglob("*"):
                if not path.is_file() or path.suffix not in (".c", ".h", ".s", ".inc"):
                    continue
                for lineno, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
                    if re.search(r"\b" + re.escape(symbol) + r"\b", line):
                        occurrences.append({"file": str(path.relative_to(US)), "line": lineno, "text": line})
        current = latest[(record["kind"], record["document_line"])]
        if len(occurrences) != 1 or "unused" not in occurrences[0]["text"].lower():
            raise ValueError((symbol, occurrences))
        if current.get("rom_pointer_candidates") or current.get("jp_source"):
            raise ValueError((symbol, "JP consumer requires further review"))
        record["unused_source_review"] = {"occurrences": occurrences, "jp_source": [], "jp_literal_pointers": [], "policy": "US source explicitly marks this definition unused and has no consuming symbol reference in src/include/data. Do not create a JP hook for an unused US-only string. Missing JP pointers alone are not the evidence."}
        record["decision"] = "rejected_unused_us_definition"
        record["execution"] = "no_port_needed_explicit_unused"
        record["plan"] = "不移植：美版源码明确标为未使用，仅有定义，没有实际调用；未证实日版存在对应显示路径，不能据清单中的猜测地址写入ROM。"
    write_patch(plan_path, plan)


if __name__ == "__main__":
    main()
