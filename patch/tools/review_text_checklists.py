#!/usr/bin/env python3
"""Reconcile historical checklists with current JP resources and source evidence."""

import argparse
import ast
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import subprocess
import warnings

from audit_batches_against_wokann import load_text_label_index, load_reference_index
from port_map_dialogue import read_charmap, encode_japanese, read_symbols
from port_c_strings import definitions
from build_texts import EXT_CTRL_ARG_LENGTHS


ROOT = Path(__file__).resolve().parents[2]
US = ROOT.parent / "pokeemerald_us_chs"
WOKANN = ROOT.parent / "pokeemerald_wokann_dev"
LITERAL = re.compile(r'"(?:[^"\\]|\\.)*"')
ASM_TEXT = re.compile(r"^([A-Za-z_]\w*)::?[^\n]*\n((?:\s*\.string[^\n]*\n)+)", re.MULTILINE)


def encode_source_controls(text, charmap):
    expanded = dict(charmap)
    for body in re.findall(r"\{([^}]+)\}", text):
        if body in expanded:
            continue
        fields = body.split()
        if len(fields) < 2 or fields[0] not in expanded:
            return None
        prefix = expanded[fields[0]]
        arguments = bytearray()
        for field in fields[1:]:
            try:
                value = int(field, 0)
            except ValueError:
                if field not in expanded:
                    return None
                arguments.extend(expanded[field])
            else:
                if not 0 <= value <= 255:
                    return None
                arguments.append(value)
        if prefix[:1] == b"\xfc" and len(arguments) != EXT_CTRL_ARG_LENGTHS.get(prefix[1]):
            return None
        expanded[body] = prefix + arguments
    return encode_japanese(".string " + json.dumps(text, ensure_ascii=False), expanded)


def read_sources(root):
    result = defaultdict(list)
    for directory in ("src", "data"):
        for path in (root / directory).rglob("*"):
            if path.suffix not in (".c", ".h", ".inc", ".s"):
                continue
            source = path.read_text(errors="replace")
            for symbol, text in definitions(source).items():
                result[symbol].append({"file": str(path.relative_to(root)), "text": text})
            for match in ASM_TEXT.finditer(source):
                literals = re.findall(r'\.string\s+("(?:[^"\\]|\\.)*")', match[2])
                try:
                    text = "".join(ast.literal_eval(value) for value in literals)
                except (ValueError, SyntaxError):
                    continue
                result[match[1]].append({"file": str(path.relative_to(root)), "text": text})
    return dict(result)


def checklist_rows(path):
    section = ""
    result = []
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith("## "):
            section = line
        if not line.startswith("| "):
            continue
        columns = [column.strip() for column in line.strip("|").split("|")]
        if columns[0] in ("idx", "symbol"):
            continue
        if len(columns) != 5:
            raise ValueError((path, lineno, len(columns)))
        result.append({"line": lineno, "section": section, "columns": columns})
    return result


def decode_text(data, charmap):
    inverse = {}
    for char, encoded in charmap.items():
        if len(char) == 1:
            inverse.setdefault(encoded, char)
    output = []
    index = 0
    while index < len(data):
        value = data[index]
        if value == 0xFF:
            break
        if value in (0xFE, 0xFA, 0xFB):
            output.append({0xFE: "\\n", 0xFA: "\\l", 0xFB: "\\p"}[value])
            index += 1
        elif value == 0xFD and index + 1 < len(data):
            output.append("{PLACEHOLDER_%02X}" % data[index + 1])
            index += 2
        elif data[index:index + 2] in inverse:
            output.append(inverse[data[index:index + 2]])
            index += 2
        else:
            output.append(inverse.get(data[index:index + 1], "{BYTE_%02X}" % value))
            index += 1
    return "".join(output)


def inventory():
    source = read_sources(US)
    labels = load_text_label_index(WOKANN)
    resources = defaultdict(list)
    references = defaultdict(list)
    by_symbol = defaultdict(list)
    for path in sorted((ROOT / "patch/batches").glob("*.json")):
        document = json.loads(path.read_text())
        for entry in document.get("texts", []):
            evidence = {"batch": str(path.relative_to(ROOT)), "definition": entry}
            by_symbol[entry.get("source_symbol", entry["name"].removeprefix("Chs_"))].append(evidence)
        for entry in document.get("reference_writes", []):
            if "original" in entry:
                evidence = {"batch": str(path.relative_to(ROOT)), **entry}
                references[int(entry["original"], 0)].append(evidence)
    for path in (ROOT / "patch").glob("*.json"):
        document = json.loads(path.read_text())
        if "strings" in document:
            for index, text in enumerate(document["strings"]):
                resources[f'{document.get("name")}[{index}]'].append({"file": str(path.relative_to(ROOT)), "index": index, "text": text})
    trainer_names = re.findall(r'\.trainerName\s*=\s*_\("([^"\n]*)"\)', (US / "src/data/trainers.h").read_text())
    for index, text in enumerate(trainer_names):
        resources[f"ChsTrainerNames[{index}]"].append({"file": "../pokeemerald_us_chs/src/data/trainers.h", "index": index, "text": text})
    return source, labels, resources, references, by_symbol


def pointer_occurrences(rom, target):
    pattern = target.to_bytes(4, "little")
    result = []
    start = 0
    while True:
        offset = rom.find(pattern, start)
        if offset < 0:
            return result
        result.append(0x08000000 + offset)
        start = offset + 1


def review():
    warnings.filterwarnings("ignore", category=SyntaxWarning)
    source, labels, resources, references, by_symbol = inventory()
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    charmap = read_charmap(WOKANN / "charmap.txt")
    japanese_source = read_sources(WOKANN)
    fixed_text_blocks = []
    text_paths = [WOKANN / "src/strings.c", *(WOKANN / "src/data/text").glob("*.h")]
    for path in text_paths:
        contents = path.read_text()
        for alias in re.finditer(r"\.set\s+(gUnknown_([0-9a-fA-F]{7,8})),\s*(\w+)", contents):
            base = int(alias[2], 16)
            for candidate in japanese_source.get(alias[3], []):
                encoded = encode_source_controls(candidate["text"] if candidate["text"].endswith("$") else candidate["text"] + "$", charmap)
                if encoded and rom[base - 0x08000000:base - 0x08000000 + len(encoded)] == encoded:
                    fixed_text_blocks.append({"file": str(path.relative_to(WOKANN)), "symbol": alias[1], "base": base, "encoded": encoded})
        for match in re.finditer(r"const u8 (gUnknown_([0-9a-fA-F]{7,8}))\[\][^;=]*=\s*\{([^}]+)\};", contents):
            values = re.findall(r"0x([0-9a-fA-F]{2})", match[3])
            if not values or re.sub(r"0x[0-9a-fA-F]{2}|[\s,]", "", match[3]):
                continue
            encoded = bytes(int(value, 16) for value in values)
            base = int(match[2], 16)
            if rom[base - 0x08000000:base - 0x08000000 + len(encoded)] != encoded:
                continue
            fixed_text_blocks.append({"file": str(path.relative_to(WOKANN)), "symbol": match[1], "base": base, "encoded": encoded})
        for symbol, candidates in japanese_source.items():
            fixed = re.fullmatch(r"gUnknown_([0-9a-fA-F]{7,8})", symbol)
            if not fixed:
                continue
            for candidate in candidates:
                if candidate["file"] != str(path.relative_to(WOKANN)):
                    continue
                text = candidate["text"]
                encoded = encode_japanese(".string " + json.dumps(text if text.endswith("$") else text + "$", ensure_ascii=False), charmap)
                if not encoded:
                    continue
                base = int(fixed[1], 16)
                if rom[base - 0x08000000:base - 0x08000000 + len(encoded)] == encoded:
                    fixed_text_blocks.append({"file": candidate["file"], "symbol": symbol, "base": base, "encoded": encoded})
    reference_index = load_reference_index(WOKANN)
    object_path = WOKANN / "build/pokeemerald-jp/data/event_scripts.o"
    for symbol, candidates in japanese_source.items():
        fixed = re.fullmatch(r"gUnknown_([0-9a-fA-F]{7,8})", symbol)
        if not fixed:
            continue
        for candidate in candidates:
            text = candidate["text"]
            encoded = encode_source_controls(text if text.endswith("$") else text + "$", charmap)
            if not encoded:
                continue
            base = int(fixed[1], 16)
            if rom[base - 0x08000000:base - 0x08000000 + len(encoded)] == encoded:
                fixed_text_blocks.append({"file": candidate["file"], "symbol": symbol, "base": base, "encoded": encoded})
    object_symbols = read_symbols(object_path, str(ROOT.parent.parent / ".local/devkitpro/devkitARM/bin/arm-none-eabi-nm"))
    for symbol, offset in object_symbols.items():
        if symbol in japanese_source:
            labels.setdefault(0x081DABAC + offset, []).append({"file": str(object_path.relative_to(WOKANN)), "symbol": symbol, "offset": offset, "base": "0x081DABAC"})
    structured = {}
    structured_paths = {"src/data/text/move_descriptions.h": "patch/move_descriptions.json", "src/data/text/item_descriptions.h": "patch/item_descriptions.json", "src/data/text/abilities.h": "patch/ability_descriptions.json", "src/data/decoration/description.h": "patch/decoration_info.json", "src/berry.c": "patch/berry_info.json"}
    for symbol, definitions_list in source.items():
        for definition in definitions_list:
            if definition["file"] in structured_paths:
                structured[symbol] = structured_paths[definition["file"]]
    history = (ROOT.parent / "batch_145_fix_plan_2026-10-01.md").read_text()
    previous = {}
    for part in re.split(r"(?=^## \d+\. idx=)", history, flags=re.MULTILINE)[1:]:
        header = re.search(r"^## (\d+)\. idx=(\d+) \| ([^\n]+)", part)
        status = re.search(r"\*\*状态\*\*：([^\n]+)", part)
        if header and status:
            previous[header[2]] = {"number": int(header[1]), "symbol": header[3], "status": status[1]}
    records = []
    for row in checklist_rows(ROOT.parent / "已移植_确定要修清单.md"):
        index, symbol, category, allegation, old = row["columns"]
        record = {"kind": "repair", "idx": index, "listed_symbol": symbol, "category": category, "claim": allegation, "listed_text": old, "document_line": row["line"]}
        if index in previous:
            prior = previous[index]
            record.update(symbol=prior["symbol"], decision="already_fixed" if prior["status"] == "已修复" else "rejected", evidence=[f"batch_145_fix_plan_2026-10-01.md entry {prior['number']}"])
            record["plan"] = "保留当前修复；验证补丁定义及最终ROM。" if record["decision"] == "already_fixed" else "保留用户确认的日版差异或已查明的误报；不按旧清单覆盖。"
        else:
            candidates = list(resources.get(symbol, []))
            if candidates:
                record.update(symbol=symbol, current_text=candidates[0]["text"], evidence=candidates, decision="review_resource", plan="核对真实表索引、日版字段和第三世代效果，再决定是否同时修复US来源及JP表。")
                if re.search(r"Chs(?:Move|Ability)Descriptions\[", symbol) and old.replace(" ", "") != candidates[0]["text"].replace("\n", "").replace(" ", ""):
                    record.update(decision="wrong_index_evidence", plan="旧文档的中文不属于该索引；查明相邻表项及真实错误，禁止按旧表索引覆盖。")
            else:
                record.update(symbol=symbol, decision="review_source", evidence=by_symbol.get(symbol, []), plan="恢复完整符号、源文本和JP调用证据，确认后同步修正US/JP。")
        records.append(record)
    entries = json.loads((ROOT / "patch/pokedex_entries.json").read_text())["entries"]
    pokedex_source = (US / "src/data/pokemon/pokedex_entries.h").read_text()
    dex_pairs = re.findall(r'\.categoryName\s*=\s*_\(\s*"((?:[^"\\]|\\.)*)"\s*\).*?\.description\s*=\s*(g\w+)', pokedex_source, re.DOTALL)
    dex_indexes = {symbol: index for index, (_, symbol) in enumerate(dex_pairs)}
    for row in checklist_rows(ROOT.parent / "未移植_确定要移植清单.md"):
        listed, address, english, chinese, note = row["columns"]
        target = int(address, 0) if address.startswith("0x") else None
        if target is not None and target < 0x08000000:
            target += 0x08000000
        prefix = listed.rstrip("…")
        candidates = [symbol for symbol in source if symbol == listed or "…" in listed and symbol.startswith(prefix)]
        matching_labels = labels.get(target, []) if target else []
        exact = [entry["symbol"] for entry in matching_labels if entry["symbol"] in candidates]
        if len(set(exact)) == 1:
            candidates = list(set(exact))
        symbol = candidates[0] if len(candidates) == 1 else listed
        record = {"kind": "port", "listed_symbol": listed, "symbol": symbol, "jp_address": f"0x{target:08X}" if target else None, "listed_english": english, "listed_chinese": chinese, "claim": note, "section": row["section"], "document_line": row["line"], "source_candidates": candidates, "evidence": matching_labels}
        if symbol in dex_indexes:
            index = dex_indexes[symbol]
            record.update(decision="already_ported_pokedex", current_text=entries[index]["description"], evidence=[{"file": "patch/pokedex_entries.json", "entry": index}, {"file": "patch/manifest.json", "old": "0x0854069C", "symbol": "ChsPokedexEntries", "expected": 9}], plan="已接入完整图鉴表；与现有US绿宝石说明和JP原文核对语义，不重复移植。")
        elif symbol in structured:
            record.update(decision="structured_table_check", evidence=[{"file": structured[symbol]}, *matching_labels], plan="该文本通过结构化资源表接入，不按旧地址重复patch；核验表项索引、现有译文及manifest引用。")
        elif target in references:
            record.update(decision="already_referenced", applied_references=references[target], plan="核验现有覆盖的符号和完整译文；不依据未移植旧标注新增重复覆盖。")
        elif symbol in by_symbol:
            record.update(decision="defined_check_target", current_definitions=by_symbol[symbol], plan="符号已有定义；对照Wokann和实际调用验证文档地址是否错配、是否还有遗漏的调用点。")
        else:
            record.update(decision="needs_verified_port", plan="使用完整US源文本编码；先验证JP文本标签和明确调用者，再添加逐指针覆盖。动态占位符须确认运行时字符集。")
        if target and 0 <= target - 0x08000000 < len(rom):
            offset = target - 0x08000000
            data = rom[offset:offset + 4096]
            record["jp_rom_text"] = decode_text(data, charmap)
            record["jp_has_eos"] = 0xFF in data
        if len(candidates) == 1:
            record["us_source"] = source[symbol]
            jp_definitions = japanese_source.get(symbol, [])
            record["jp_source"] = jp_definitions
            if target and jp_definitions:
                verified = []
                for definition in jp_definitions:
                    encoded = encode_source_controls(definition["text"].split("$")[0] + "$", charmap)
                    if encoded is not None and rom[target - 0x08000000:target - 0x08000000 + len(encoded)] == encoded:
                        verified.append(definition)
                record["exact_jp_source_match"] = verified
        if target:
            for block in fixed_text_blocks:
                offset = target - block["base"]
                if not 0 <= offset < len(block["encoded"]):
                    continue
                if offset and block["encoded"][offset - 1] != 0xFF:
                    continue
                end = block["encoded"].find(b"\xff", offset)
                if end < 0:
                    continue
                record.setdefault("exact_jp_source_match", []).append({"file": block["file"], "symbol": block["symbol"], "offset": offset, "encoded_hex": block["encoded"][offset:end + 1].hex(), "proof": "Fixed-address text-source block matches ROM; offset starts after EOS or at block start."})
            record["rom_pointer_candidates"] = [f"0x{address:08X}" for address in pointer_occurrences(rom, target)]
            source_references = []
            for address in pointer_occurrences(rom, target):
                entries_at_address = reference_index.get(address, [])
                matching = []
                for entry in entries_at_address:
                    referenced = entry.get("referenced_symbol", "") or ""
                    fixed = re.fullmatch(r"gUnknown_([0-9A-Fa-f]{7,8})", referenced)
                    resolved = None
                    if fixed:
                        resolved = int(fixed[1], 16) + int(entry.get("referenced_offset") or "0", 0)
                    if referenced == symbol or resolved == target:
                        matching.append({**entry, "resolved_target": f"0x{target:08X}"})
                if matching:
                    source_references.append({"address": f"0x{address:08X}", "original": f"0x{target:08X}", "source": matching})
            record["verified_code_references"] = source_references
        records.append(record)
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = review()
    document = {"schema_version": 1, "date": "2026-10-02", "jp_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(), "wokann_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=WOKANN, text=True).strip(), "base_rom_sha1": hashlib.sha1((ROOT / "baserom_jp.gba").read_bytes()).hexdigest(), "summary": dict(Counter(record["decision"] for record in records)), "records": records}
    args.output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(document["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
