#!/usr/bin/env python3
"""Refresh checklist progress from persisted per-row evidence and current ROMs."""

from collections import Counter
import hashlib
import json
import subprocess

from execute_verified_checklist import write_patch
from review_text_checklists import ROOT, US


def main():
    path = ROOT / "patch/mapping_reports/checklists_action_plan_2026-10-02.json"
    plan = json.loads(path.read_text())
    pending = []
    states = Counter()
    for record in plan["records"]:
        state = record.get("execution", record["decision"])
        states[state] += 1
        if state == "ported_verified_literal" and record.get("placeholder_contract"):
            record["remaining_verification"] = [gate for gate in record.get("remaining_verification", []) if gate != "Dynamic text: verify producer and JP layout before a new literal override."]
        unfinished = record.get("execution") is None and record["decision"] not in ("already_fixed", "rejected")
        unfinished |= state in ("no_verified_reference", "existing_override_requires_semantic_review", "computed_name_block_requires_display_port")
        if not unfinished:
            continue
        source = record.get("us_source", [{}])[0].get("file", "unresolved")
        gates = record.get("remaining_verification", [])
        if not gates:
            if not record.get("exact_jp_source_match"):
                gates = ["Establish the JP text label, exact bytes and semantic correspondence; a readable ROM fragment or old CSV claim is insufficient."]
            elif not record.get("verified_code_references") and not record.get("verified_object_references"):
                gates = ["Trace computed/interior consumers or establish a dormant/edition-specific definition; no literal pointer is not a verdict by itself."]
            else:
                gates = ["Reconcile existing reference writes and full text against current ROM; do not add a duplicate override."]
        pending.append({"kind": record["kind"], "document_line": record["document_line"], "symbol": record["symbol"], "jp_address": record.get("jp_address"), "source": source, "status": state, "gates": gates})
    plan["summary"] = dict(Counter(record["decision"] for record in plan["records"]))
    plan["current_execution_summary"] = dict(states)
    plan["progress"] = {"complete": not pending, "total_rows": len(plan["records"]), "unresolved_rows": len(pending), "unresolved_by_source": dict(Counter(entry["source"] for entry in pending)), "bedroom_graphics": "Not started: text review is not complete.", "pending_rows": pending}
    plan["current_roms"] = {"jp": {"filename": "pokeemerald_jp_chs.gba", "sha1": hashlib.sha1((ROOT / "pokeemerald_jp_chs.gba").read_bytes()).hexdigest()}, "us": {"filename": "pokeemerald.gba", "sha1": hashlib.sha1((US / "pokeemerald.gba").read_bytes()).hexdigest()}}
    plan.setdefault("validation", {})["jp_rom_sha1"] = plan["current_roms"]["jp"]["sha1"]
    plan["progress"]["scope"] = "The unresolved count tracks uncompleted per-row actions/evidence gates; emitted resource equality alone does not certify every semantic allegation. Do not treat the complement of this number as a blanket semantic approval."
    plan["jp_head"] = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    write_patch(path, plan)
    print({"total_rows": len(plan["records"]), "unresolved_rows": len(pending), "current_execution_summary": dict(states)})


if __name__ == "__main__":
    main()
