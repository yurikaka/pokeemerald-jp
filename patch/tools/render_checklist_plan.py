#!/usr/bin/env python3
"""Render the persisted checklist plan without discarding execution evidence."""

import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    document = json.loads(args.plan.read_text())
    records = document["records"]
    states = Counter(record.get("execution", record["decision"]) for record in records)
    lines = ["# 文本清单逐条行动计划（2026-10-02）", "", "## 当前状态", "", "本任务尚未全部完成。以下保留逐条判定、已执行引用和未完成门槛；不能把建立计划、已有定义或没有绝对指针当作移植完成。", "", "覆盖已移植错误290条、未移植清单3036条。旧文档的截断原文和MISMATCH仅作线索。", "", "床和电脑图块修复仍排在文本审核完成之后，尚未开始修改。", "", "```json", json.dumps(dict(states), ensure_ascii=False, indent=2), "```", "", "## 执行顺序", "", "1. 核验剩余动态占位符的生产者、语言模式及原版窗口布局。", "2. 核验已有全局覆盖与清单符号是否语义一致，避免重复重定向。", "3. 追踪无直接指针及未定位条目的计算引用/区域差异；没有证据不得盲写地址。", "4. 双版本构建、ROM引用核验和运行场景测试完成后，追踪chuang.png中的床和电脑图块。", "", "## 逐条行动", ""]
    for index, record in enumerate(records, 1):
        extra = [{key: record[key]} for key in ("semantic_review", "placeholder_contract", "english_source_evidence", "unused_source_review", "dormant_script_review", "existing_override_rom_evidence", "shared_override_evidence", "shared_override_partial_evidence", "excluded_computed_references", "computed_reference_gate", "bounded_display_buffer_gate") if key in record]
        record["evidence"] = [*record.get("evidence", []), *extra]
        if "english_original" in record:
            record["listed_english"] = record["english_original"]
        filename = "已移植_确定要修清单.md" if record["kind"] == "repair" else "未移植_确定要移植清单.md"
        lines += [f"### {index}. {record['symbol']}", "", f"- 文档：{filename}:{record['document_line']}", f"- 判断：{record['decision']}", f"- 执行状态：{record.get('execution', '未记录执行完成；按本条证据门槛继续核验')}", f"- 方案：{record['plan']}", f"- 地址：{record.get('jp_address', '按资源表索引/原批次')}", "", "原文档主张：", record["claim"], "", "原中文（旧文档可能是节选或索引错配）：", "```text", record.get("listed_text", record.get("listed_chinese", "未提供")), "```", "", "日文原文/原始JP ROM解码（不是当前汉化ROM；简易解码不作为控制符证据）：", "```text", record.get("jp_original", record.get("jp_rom_text", "参见Wokann证据中的完整源定义")), "```", "", "英文原文（已恢复时使用完整源定义，否则保留原清单节选）：", "```text", record.get("listed_english", "原清单未提供；参见原145条修复计划"), "```", "", "最终/拟用中文：", "```text", record.get("final_text", record.get("current_text", "尚需核验后确定")), "```", "", "同条证据、实际引用和剩余门槛：", "```json", json.dumps({key: value for key, value in record.items() if key in ("evidence", "us_source", "jp_source", "resource_evidence", "exact_jp_source_match", "execution_references", "active_new_references", "existing_verified_references", "existing_override_conflicts", "remaining_verification", "executed_batch", "regional_difference")}, ensure_ascii=False, indent=2), "```", ""]
    new = "\n".join(lines) + "\n"
    old = args.output.read_text() if args.output.exists() else None
    if old == new:
        return
    body = ("*** Update File: " + str(args.output) + "\n@@\n" + "".join("-" + line + "\n" for line in old.splitlines())) if old is not None else "*** Add File: " + str(args.output) + "\n"
    body += "".join("+" + line + "\n" for line in new.splitlines())
    subprocess.run(["apply_patch"], input="*** Begin Patch\n" + body + "*** End Patch\n", text=True, check=True)


if __name__ == "__main__":
    main()
