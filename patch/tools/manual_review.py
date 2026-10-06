#!/usr/bin/env python3
"""Record and export manual per-override review verdicts.

Every verdict in queue.jsonl must come from a human reading the decoded
Japanese original, the Chinese replacement, and the Wokann source evidence.
This tool only stores and formats those manual judgments.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QUEUE = ROOT / "patch/mapping_reports/manual_review/queue.jsonl"
LEDGERS = ROOT / "patch/mapping_reports/manual_review/batches"

VALID_VERDICTS = {
    "ok",                # target is text, address is a text reference, CN faithful
    "ok-intentional",    # valid override; CN deliberately deviates (documented)
    "fix-text",          # semantic problem in the Chinese text
    "fix-address",       # override address/target is not provably a text reference
    "remove",            # override should not exist
}


def load() -> list[dict]:
    return [json.loads(line) for line in QUEUE.read_text(encoding="utf-8").splitlines() if line.strip()]


def save(records: list[dict]) -> None:
    with QUEUE.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def cmd_show(args) -> None:
    for record in load():
        if record["batch"] != args.batch:
            continue
        if args.pending and record["verdict"]:
            continue
        print(f"[{record['index']}] {record['address']} -> {record['original']}"
              f"  {record['symbol']}  ({record['audit_status']})")
        print(f"  JP: {record['jp']}")
        print(f"  CN: {record['cn']}")
        if record["target_files"]:
            print(f"  src: {', '.join(record['target_files'])}")
        if record["verdict"]:
            print(f"  verdict: {record['verdict']}  {record['notes']}")


def cmd_set(args) -> None:
    records = load()
    wanted = set(args.index) if args.index else None
    changed = 0
    for record in records:
        if record["batch"] != args.batch:
            continue
        if wanted is not None and record["index"] not in wanted:
            continue
        record["verdict"] = args.verdict
        record["notes"] = args.notes
        changed += 1
    save(records)
    print(f"updated {changed} record(s) in {args.batch}")


def cmd_export(args) -> None:
    records = [r for r in load() if r["batch"] == args.batch]
    if not records:
        raise SystemExit(f"no records for {args.batch}")
    LEDGERS.mkdir(parents=True, exist_ok=True)
    out = LEDGERS / (args.batch.replace(".json", ".md"))
    counts = Counter(r["verdict"] or "pending" for r in records)
    lines = [
        f"# Manual review: {args.batch}",
        "",
        f"verdicts: {dict(counts)}",
        "",
        "| # | address | original | symbol | JP | CN | verdict | notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in records:
        jp = r["jp"].replace("|", "\\|")
        cn = r["cn"].replace("|", "\\|")
        notes = r["notes"].replace("|", "\\|")
        lines.append(
            f"| {r['index']} | {r['address']} | {r['original']} | {r['source_symbol'] or r['symbol']}"
            f" | {jp} | {cn} | {r['verdict'] or 'pending'} | {notes} |"
        )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(records)} rows)")


def cmd_progress(_args) -> None:
    counts = Counter()
    per_batch = Counter()
    for record in load():
        verdict = record["verdict"] or "pending"
        counts[verdict] += 1
        if verdict == "pending":
            per_batch[record["batch"]] += 1
    print("verdicts:", dict(counts))
    if per_batch:
        print("pending by batch:")
        for batch, count in sorted(per_batch.items()):
            print(f"  {batch}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    show = sub.add_parser("show")
    show.add_argument("batch")
    show.add_argument("--pending", action="store_true")
    show.set_defaults(func=cmd_show)
    set_cmd = sub.add_parser("set")
    set_cmd.add_argument("batch")
    set_cmd.add_argument("verdict", choices=sorted(VALID_VERDICTS))
    set_cmd.add_argument("notes")
    set_cmd.add_argument("index", nargs="*", type=int)
    set_cmd.set_defaults(func=cmd_set)
    export = sub.add_parser("export")
    export.add_argument("batch")
    export.set_defaults(func=cmd_export)
    progress = sub.add_parser("progress")
    progress.set_defaults(func=cmd_progress)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
