#!/usr/bin/env python3
"""Publish verified v2 audit JSON and a combined row-level Markdown report."""

import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def publish(path, content):
    relative = path.relative_to(ROOT)
    if path.exists():
        old = path.read_text()
        if old == content:
            return
        patch = f'*** Begin Patch\n*** Update File: {relative}\n@@\n'
        patch += ''.join('-' + line + '\n' for line in old.splitlines())
    else:
        patch = f'*** Begin Patch\n*** Add File: {relative}\n'
    patch += ''.join('+' + line + '\n' for line in content.splitlines())
    patch += '*** End Patch\n'
    subprocess.run(['apply_patch'], input=patch, text=True, cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('verification', type=Path)
    args = parser.parse_args()
    report = json.loads(args.verification.read_text())
    if any(record['decision'] in ('requires_consumer_trace', 'mapping_requires_trace') for record in report['records']):
        raise ValueError('unresolved flagged or missing consumers remain')
    lines = [
        '# v2 审计逐条核验与修复（2026-10-04）', '',
        '## 范围与限制', '',
        '输入14780条；236条 ERROR / NEEDS_ATTENTION 全部逐条判定，125条修复（122条涉及日版、3条仅美版）。',
        '1288条 UNTRANSPLANTED 完成映射/调用分类：此前待追踪的143条均有逐项证据，新增修复15条审计记录，另补日版简易聊天的7字词语限制提示。',
        '合计140条审计记录执行修复。弃用定义、无消费者数组/函数、区域差异及非显示比较常量不盲目覆盖。',
        'OK项只核验映射，不代表重新完成语义审查；历史休眠脚本判定保留其证据与原始ROM未改检查，不冒充新语义审查。没有运行模拟器。', '',
        '## 当前分类', '',
    ]
    lines.extend(f'- `{name}`：{count}' for name, count in report['summary'].items())
    lines.extend(['', '## 未移植项分类', ''])
    lines.extend(f'- `{name}`：{count}' for name, count in report['untransplanted_summary'].items())
    lines.extend(['', '## 问题项逐条判定', ''])
    for record in report['records']:
        if 'review' not in record:
            continue
        review = record['review']
        lines.extend([
            f"### CSV 第 {record['row_number']} 行 · {record['domain']} / {record['idx']} · {record['symbol']}", '',
            f"判定：`{record['decision']}`", '', f"理由：{review.get('reason', '')}", '',
        ])
        for label, text in (
            ('日文', record.get('reported_japanese', '')),
            ('英文', record.get('reported_english', '')),
            ('报告原中文', record.get('reported_chinese', '')),
            ('修复前实际中文', review.get('old_current_text', review.get('old', ''))),
            ('最终中文', review.get('final_text', '')),
        ):
            lines.extend([label + '：', '', '```text', text, '```', ''])
        lines.extend(['证据：', '', '```json', json.dumps({'review': review, 'source': record.get('source_evidence'), 'mapping': record['mapping_evidence']}, ensure_ascii=False, indent=2), '```', ''])
    lines.extend(['## 原143条待追踪项的最终判定', ''])
    for record in report['records']:
        if 'consumer_review' not in record:
            continue
        review = record['consumer_review']
        lines.extend([
            f"### CSV 第 {record['row_number']} 行 · {record['symbol']}", '',
            f"判定：`{record['decision']}`", '', f"理由：{review['reason']}", '',
            '具体实现 / 调用 / 源文件及对象哈希证据：', '', '```json',
            json.dumps(review, ensure_ascii=False, indent=2), '```', '',
        ])
    publish(ROOT / 'patch/mapping_reports/v2_audit_verification_2026-10-04.json', json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    publish(ROOT / 'patch/mapping_reports/v2_audit_review_2026-10-04.md', '\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
