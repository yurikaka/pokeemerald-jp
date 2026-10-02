#!/usr/bin/env python3
"""Attach current active writes and reviewed language contracts to mapping reports."""

import json

from execute_verified_checklist import write_patch
from review_text_checklists import ROOT


def main():
    plan = json.loads((ROOT / "patch/mapping_reports/checklists_action_plan_2026-10-02.json").read_text())
    records = {record["symbol"]: record for record in plan["records"]}
    for path in sorted((ROOT / "patch/batches").glob("4*_checklist*.json")):
        if int(path.name.split("_")[0]) < 431:
            continue
        report_path = ROOT / "patch/mapping_reports" / path.name
        if not report_path.exists():
            continue
        batch = json.loads(path.read_text())
        report = json.loads(report_path.read_text())
        report["active_reference_writes"] = batch.get("reference_writes", [])
        report["active_definition_count"] = len(batch.get("texts", []))
        report["active_reference_count"] = len(batch.get("reference_writes", []))
        language_rules = []
        for definition in batch.get("texts", []):
            record = records.get(definition.get("source_symbol"), {})
            options = {key: definition[key] for key in ("japanese_placeholders", "japanese_dynamic", "initial_japanese", "auto_wrap") if key in definition}
            if not options and not record.get("placeholder_contract"):
                continue
            language_rules.append({"definition": definition["name"], "source_symbol": definition.get("source_symbol"), "options": options, "placeholder_contract": record.get("placeholder_contract"), "remaining_verification": record.get("remaining_verification", [])})
        report["language_rules"] = language_rules
        report["policy"] = "Only current active writes listed here apply. Fixed JP source bytes and Wokann literal/typed-object layouts establish mapping evidence; dynamic controls require the per-definition producer contract. Existing overrides, persistent nickname constructors and computed Blender name blocks are preserved rather than blindly redirected."
        write_patch(report_path, report)


if __name__ == "__main__":
    main()
