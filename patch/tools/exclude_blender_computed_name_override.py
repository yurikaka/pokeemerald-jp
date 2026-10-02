#!/usr/bin/env python3
"""Preserve the original Blender name block until computed consumers are ported."""

import json

from execute_verified_checklist import write_patch
from review_text_checklists import ROOT


def main():
    batch_path = ROOT / "patch/batches/435_checklist_fixed_text_blocks.json"
    batch = json.loads(batch_path.read_text())
    excluded = [entry for entry in batch["reference_writes"] if entry["address"] == "0x0807F9A8"]
    batch["reference_writes"] = [entry for entry in batch["reference_writes"] if entry["address"] != "0x0807F9A8"]
    batch["texts"] = [entry for entry in batch["texts"] if entry.get("source_symbol") != "sText_Miss"]
    write_patch(batch_path, batch)
    report_path = ROOT / "patch/mapping_reports/435_checklist_fixed_text_blocks.json"
    report = json.loads(report_path.read_text())
    report["mapping"] = [entry for entry in report["mapping"] if entry["symbol"] != "sText_Miss"]
    write_patch(report_path, report)
    reason = "Wokann src/berry_blender.c:972-1015: sub_0807F888 loads the Miss block at 0x0807F9A8 and also copies names from that pointer minus 0x18 and minus 0x12. Redirecting only Miss makes both computed reads point outside the intended names. Keep the original contiguous JP block until display-only conversion and all computed consumers are verified."
    plan_path = ROOT / "patch/mapping_reports/checklists_action_plan_2026-10-02.json"
    plan = json.loads(plan_path.read_text())
    for record in plan["records"]:
        if record.get("symbol") != "sText_Miss":
            continue
        record["execution"] = "computed_name_block_requires_display_port"
        record["active_new_references"] = []
        record["execution_references"] = []
        record["remaining_verification"] = [reason]
        record["plan"] = "保留原日文相邻姓名块和运行时数据，追踪显示消费者后在专用显示缓冲区转换阿姨、男孩、少女等姓名；禁止只覆盖基址。"
        record["excluded_computed_references"] = excluded
    write_patch(plan_path, plan)
    write_patch(ROOT / "patch/mapping_reports/checklist_blender_computed_name_exclusion.json", {"excluded": excluded, "reason": reason})


if __name__ == "__main__":
    main()
