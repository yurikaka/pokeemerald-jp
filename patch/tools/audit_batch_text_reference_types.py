"""Conservatively audit every batch reference's target and pointer field type."""

import hashlib
import json
import re
import struct
import subprocess
import warnings
from collections import Counter, defaultdict
from pathlib import Path

from audit_batches_against_wokann import load_reference_index, load_text_label_index
from port_map_dialogue import read_charmap, read_symbols
from review_text_checklists import encode_source_controls, read_sources
from verify_wokann_object_references import cstring, object_sections


ROOT = Path(__file__).resolve().parents[2]
WOKANN = ROOT.parent / "pokeemerald_wokann_dev"
ROM_BASE = 0x08000000
OUTPUT = ROOT / "patch/mapping_reports/batch_text_reference_types"


def compiled_text_symbols(path, source_symbols):
    data = path.read_bytes()
    if data[:7] != b"\x7fELF\x01\x01\x01":
        return []
    header = struct.unpack_from("<16sHHIIIIIHHHHHH", data)
    sections = [struct.unpack_from("<IIIIIIIIII", data, header[6] + index * header[11])
                for index in range(header[12])]
    result = []
    for table in sections:
        if table[1] != 2:
            continue
        names_header = sections[table[6]]
        names = data[names_header[4]:names_header[4] + names_header[5]]
        for offset in range(table[4], table[4] + table[5], table[9]):
            name_offset, value, size, info, visibility, section_index = struct.unpack_from("<IIIBBH", data, offset)
            symbol = cstring(names, name_offset)
            if symbol not in source_symbols or not size or not 0 < section_index < len(sections):
                continue
            section = sections[section_index]
            if section[1] != 1 or not section[2] & 2 or section[2] & 4 or value + size > section[5]:
                continue
            encoded = data[section[4] + value:section[4] + value + size]
            if encoded.endswith(b"\xff"):
                result.append((symbol, encoded))
    return result


def main():
    warnings.filterwarnings("ignore", category=SyntaxWarning)
    base = (ROOT / "baserom_jp.gba").read_bytes()
    labels = load_text_label_index(WOKANN)
    direct = load_reference_index(WOKANN)
    sources = read_sources(WOKANN)
    charmap = read_charmap(WOKANN / "charmap.txt")
    event_object = WOKANN / "build/pokeemerald-jp/data/event_scripts.o"
    event_symbols = read_symbols(event_object, str(ROOT.parent.parent / ".local/devkitpro/devkitARM/bin/arm-none-eabi-nm"))
    encoded_sources = {}
    for symbol, definitions in sources.items():
        encoded_sources[symbol] = []
        for definition in definitions:
            text = definition["text"]
            encoded = encode_source_controls(text if text.endswith("$") else text + "$", charmap)
            if encoded:
                encoded_sources[symbol].append((encoded, definition["file"]))
    for path in [WOKANN / "src/strings.c", *(WOKANN / "src/data/text").rglob("*.h")]:
        source = path.read_text(errors="replace")
        for match in re.finditer(r"const u8\s+(\w+)\s*\[[^\]]*\][^;=]*=\s*\{([^}]+)\};", source):
            body = re.sub(r"/\*.*?\*/|//[^\n]*", "", match[2], flags=re.S)
            values = [part.strip() for part in body.split(",") if part.strip()]
            if values and all(re.fullmatch(r"0x[0-9a-fA-F]{1,2}|\d{1,3}", value) for value in values):
                numbers = [int(value, 0) for value in values]
                if all(value < 256 for value in numbers) and 255 in numbers:
                    encoded_sources.setdefault(match[1], []).append((bytes(numbers), str(path.relative_to(WOKANN))))
    for path in (WOKANN / "build/pokeemerald-jp").rglob("*.o"):
        for symbol, encoded in compiled_text_symbols(path, encoded_sources):
            encoded_sources[symbol].append((encoded, str(path.relative_to(WOKANN))))
    symbol_addresses = defaultdict(set)
    for address, entries in labels.items():
        for entry in entries:
            symbol_addresses[entry["symbol"]].add(address)
    for symbol, offset in event_symbols.items():
        if symbol in encoded_sources:
            symbol_addresses[symbol].add(0x081DABAC + offset)
    for path in [WOKANN / "src/strings.c", *(WOKANN / "src/data/text").rglob("*.h")]:
        for match in re.finditer(r"\.set\s+gUnknown_([0-9a-fA-F]{7,8}),\s*(\w+)", path.read_text()):
            symbol_addresses[match[2]].add(int(match[1], 16))
    text_locations = defaultdict(list)
    for symbol, definitions in encoded_sources.items():
        numeric = re.fullmatch(r"gUnknown_([0-9a-fA-F]{7,8})", symbol)
        known = set(symbol_addresses[symbol])
        if numeric:
            known.add(int(numeric[1], 16))
        for encoded, filename in definitions:
            for address in known:
                offset = address - ROM_BASE
                if base[offset:offset + len(encoded)] != encoded:
                    continue
                cursor = 0
                for part in encoded.split(b"\xff")[:-1]:
                    text_locations[address + cursor].append({"symbol": symbol, "file": filename,
                        "method": "exact_fixed_source_text_block_string_boundary", "length": len(part) + 1})
                    cursor += len(part) + 1
            if len(encoded) >= 8:
                offset = base.find(encoded)
                if offset >= 0 and base.find(encoded, offset + 1) < 0:
                    text_locations[offset + ROM_BASE].append({"symbol": symbol, "file": filename,
                        "method": "unique_exact_source_text_bytes", "length": len(encoded)})
    proofs = defaultdict(list)
    cached = json.loads((ROOT / "patch/mapping_reports/wokann_object_reference_verification.json").read_text())
    digests = {}
    stale = 0
    for proof in cached["references"]:
        relative = proof["object"]
        path = WOKANN / relative
        expected = proof.get("object_sha256", proof.get("binary_sha256"))
        if expected:
            if relative not in digests:
                digests[relative] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
            if digests[relative] != expected:
                stale += 1
                continue
        proofs[(int(proof["address"], 0), int(proof["original"], 0))].append(proof)
    batches = []
    target_cache = {}
    for path in sorted((ROOT / "patch/batches").glob("*.json")):
        document = json.loads(path.read_text())
        for index, entry in enumerate(document.get("reference_writes", [])):
            batches.append((path.name, index, entry))
    for target in sorted({int(entry["original"], 0) for _, _, entry in batches}):
        offset = target - ROM_BASE
        evidence = list(text_locations[target])
        for label in labels.get(target, []):
            for encoded, filename in encoded_sources.get(label["symbol"], []):
                if base[offset:offset + len(encoded)] == encoded:
                    evidence.append({"symbol": label["symbol"], "file": filename,
                                     "method": "fixed_label_and_exact_encoded_text", "length": len(encoded)})
        target_cache[target] = evidence
    event_relocations = set()
    event_script_targets = defaultdict(list)
    for symbol, offset in event_symbols.items():
        if "EventScript" in symbol:
            event_script_targets[0x081DABAC + offset].append(symbol)
    if event_object.is_file():
        event_sections = object_sections(event_object)
        for section, contents, relocations in event_sections:
            if section == "script_data":
                event_relocations.update(0x081DABAC + item["offset"] for item in relocations if item["type"] == 2)
                for item in relocations:
                    if item["type"] == 2:
                        address = 0x081DABAC + item["offset"]
                        target = struct.unpack_from("<I", base, address - ROM_BASE)[0]
                        symbol_offset = event_symbols.get(item["symbol"])
                        if item["symbol"] == "" and len(event_sections) == 1:
                            symbol_offset = 0
                        addend = struct.unpack_from("<I", contents, item["offset"])[0]
                        if symbol_offset is None or target != 0x081DABAC + symbol_offset + addend:
                            continue
                        proofs[(address, target)].append({"object": str(event_object.relative_to(WOKANN)),
                            "section": section, "relocation": "R_ARM_ABS32", "referenced_symbol": item["symbol"]})
    rows = []
    for filename, index, entry in batches:
        address, target = int(entry["address"], 0), int(entry["original"], 0)
        offset, target_offset = address - ROM_BASE, target - ROM_BASE
        evidence = list(target_cache[target])
        symbol = entry.get("source_symbol")
        matching_proofs = proofs[(address, target)]
        candidates = {symbol, *(proof.get("referenced_symbol") for proof in matching_proofs),
                      *(proof.get("referenced_symbol") for proof in direct.get(address, []))}
        for candidate in candidates - {None, ""}:
            for encoded, source in encoded_sources.get(candidate, []):
                if base[target_offset:target_offset + len(encoded)] == encoded:
                    proof = {"symbol": candidate, "file": source,
                             "method": "exact_encoded_source_at_target", "length": len(encoded)}
                    if proof not in evidence:
                        evidence.append(proof)
        field_proofs = []
        for proof in matching_proofs:
            field_proofs.append({key: proof[key] for key in
                                 ("object", "section", "relocation", "referenced_symbol", "proof") if key in proof})
        if offset >= 2 and base[offset - 2:offset] == b"\x0f\x00" and base[offset + 4:offset + 5] == b"\x09":
            field_proofs.append({"method": "native_event_msgbox_loadword_callstd"})
        if address in event_relocations:
            for displacement in (6, 10, 14):
                start = offset - displacement
                if start < 0 or base[start] != 0x5C:
                    continue
                mode = base[start + 1]
                text_count = 1 if mode == 3 else 3 if mode in (4, 6, 7, 8) else 2
                if mode <= 12 and displacement < 6 + text_count * 4:
                    field_proofs.append({"method": "compiled_event_trainerbattle_text_operand",
                        "command_address": f"0x{start + ROM_BASE:08X}", "mode": mode,
                        "source": "asm/macros/event.inc:770"})
        for proof in matching_proofs:
            if proof["relocation"] == "R_ARM_ABS32" and re.search(r"battle_ai|battle_scripts|battle_anim|front_pic|pokemon_animation", proof["object"]):
                if not evidence:
                    violations_hint = "nontext_subsystem_reference"
                    field_proofs.append({"warning": violations_hint})
        for proof in direct.get(address, []):
            if proof.get("referenced_symbol") in {item["symbol"] for item in evidence}:
                field_proofs.append({"method": "fixed_address_text_symbol_reference", **proof})
        actual = struct.unpack_from("<I", base, offset)[0] if 0 <= offset <= len(base) - 4 else None
        violations = []
        if actual != target:
            violations.append("base_pointer_mismatch")
        if 0x0828A480 <= target < 0x0828C8D7 or address < 0x0828C8D7 and address + 4 > 0x0828A480:
            violations.append("battle_ai_bytecode_not_dialogue")
        if target == 0x08146E66:
            violations.append("battle_transition_instruction_not_text")
        if target == 0x0823C8D4:
            violations.append("trick_house_event_script_not_text")
        if target in event_script_targets and not evidence:
            violations.append("compiled_event_script_label_not_text")
        if violations:
            status = "invalid"
        elif evidence and field_proofs:
            status = "confirmed_text_and_reference"
        elif evidence:
            status = "text_confirmed_reference_unproven"
        elif field_proofs:
            status = "reference_located_target_unproven"
        else:
            status = "unproven"
        rows.append({"batch": filename, "index": index, **entry, "status": status,
                     "base_value": f"0x{actual:08X}" if actual is not None else None,
                     "target_evidence": evidence, "reference_evidence": field_proofs,
                     "violations": violations})
    OUTPUT.mkdir(parents=True, exist_ok=True)
    summary = dict(Counter(row["status"] for row in rows))
    report = {"policy": "Both exact source text bytes and reference-field evidence are required; existence of a source definition alone is never proof.",
              "base_sha256": hashlib.sha256(base).hexdigest(),
              "wokann_revision": subprocess.check_output(["git", "-C", str(WOKANN), "rev-parse", "HEAD"], text=True).strip(),
              "batch_count": len(list((ROOT / "patch/batches").glob("*.json"))),
              "reference_count": len(rows), "stale_cached_proofs_ignored": stale,
              "summary": summary, "references": rows}
    report["non_reference_resources"] = []
    for path in sorted((ROOT / "patch/batches").glob("*.json")):
        document = json.loads(path.read_text())
        for table in document.get("compact_tables", []):
            report["non_reference_resources"].append({"batch": path.name, "name": table["name"],
                "kind": table["kind"], "status": "generated_resource_not_original_rom_overwrite",
                "scope": "Consumer hooks are outside this batch reference audit."})
    (OUTPUT / "references.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Strict batch text-reference audit", "", json.dumps(summary, ensure_ascii=False), "",
             "Unproven means insufficient evidence, not necessarily a bug. Existing source-definition-only audits are not accepted.", "",
             "| Batch | Index | Reference | Target | Symbol | Status |", "|---|---:|---|---|---|---|"]
    for row in rows:
        if row["status"] != "confirmed_text_and_reference":
            lines.append(f"| {row['batch']} | {row['index']} | {row['address']} | {row['original']} | {row.get('source_symbol', row['symbol'])} | {row['status']} |")
    (OUTPUT / "review_queue.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"batch_count": report["batch_count"], "reference_count": len(rows), "summary": summary,
                      "stale_cached_proofs_ignored": stale}, ensure_ascii=False))


if __name__ == "__main__":
    main()
