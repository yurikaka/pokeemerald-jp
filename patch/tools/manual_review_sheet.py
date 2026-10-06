#!/usr/bin/env python3
"""Print a manual review sheet for one batch.

For every override this shows the raw ROM bytes surrounding the override
address so the reviewer can personally judge whether the field is a text
reference (script msgbox word, pointer-table slot, code literal) or something
else. The bytes are evidence for manual review, not an automated verdict.
"""

from __future__ import annotations

import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROM_BASE = 0x08000000


def main() -> None:
    batch = sys.argv[1]
    base = (ROOT / "baserom_jp.gba").read_bytes()
    records = [json.loads(line) for line in
               (ROOT / "patch/mapping_reports/manual_review/queue.jsonl").read_text(encoding="utf-8").splitlines()
               if line.strip() and json.loads(line)["batch"] == batch]
    for r in records:
        address = int(r["address"], 16) - ROM_BASE
        original = int(r["original"], 16)
        before = base[address - 6:address].hex()
        word = struct.unpack_from("<I", base, address)[0]
        after = base[address + 4:address + 10].hex()
        pointer_match = "PTR-OK" if word == original else f"PTR-MISMATCH({word:08X})"
        verdict = r["verdict"] or "?"
        compact = len(sys.argv) > 2 and sys.argv[2] == "--compact"
        if compact:
            print(f"[{r['index']}] {r['address']} {pointer_match} ..{before}|{word:08X}|{after}.. {r['source_symbol'] or r['symbol']}")
            print(f"  J {r['jp'][:70]}")
            print(f"  C {r['cn'][:70]}")
        else:
            print(f"[{r['index']}] {r['address']} {pointer_match} ctx=..{before} |{word:08X}| {after}..")
            print(f"    JP({r['original']}): {r['jp'][:100]}")
            print(f"    CN: {r['cn'][:100]}")
            print(f"    sym={r['source_symbol'] or r['symbol']} audit={r['audit_status']} verdict={verdict}")


if __name__ == "__main__":
    main()
