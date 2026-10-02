#!/usr/bin/env python3
"""Locate byte-exact Wokann ELF sections and expose typed pointer relocations."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import struct
import warnings

from review_text_checklists import ROOT, WOKANN, encode_source_controls, read_sources
from audit_batches_against_wokann import load_text_label_index
from port_map_dialogue import read_charmap, read_symbols


def cstring(data, offset):
    return data[offset:data.index(0, offset)].decode()


def object_sections(path):
    data = path.read_bytes()
    if data[:7] != b"\x7fELF\x01\x01\x01":
        raise ValueError(path)
    header = struct.unpack_from("<16sHHIIIIIHHHHHH", data)
    sections = [struct.unpack_from("<IIIIIIIIII", data, header[6] + index * header[11]) for index in range(header[12])]
    strings_header = sections[header[13]]
    names = data[strings_header[4]:strings_header[4] + strings_header[5]]
    result = []
    for section_index, section in enumerate(sections):
        if section[1] != 1 or not section[2] & 2 or not section[5]:
            continue
        name = cstring(names, section[0])
        contents = data[section[4]:section[4] + section[5]]
        relocations = []
        for relocation_section in sections:
            if relocation_section[1] != 9 or relocation_section[7] != section_index:
                continue
            symbols = sections[relocation_section[6]]
            symbol_strings = sections[symbols[6]]
            symbol_names = data[symbol_strings[4]:symbol_strings[4] + symbol_strings[5]]
            for offset in range(relocation_section[4], relocation_section[4] + relocation_section[5], 8):
                location, info = struct.unpack_from("<II", data, offset)
                symbol = struct.unpack_from("<IIIBBH", data, symbols[4] + (info >> 8) * symbols[9])
                relocations.append({"offset": location, "type": info & 255, "symbol": cstring(symbol_names, symbol[0])})
        result.append((name, contents, relocations))
    return result


def locate_section(rom, contents, relocations, known_symbols):
    comparable = bytearray(contents)
    excluded = bytearray(len(contents))
    for relocation in relocations:
        if relocation["type"] not in (2, 10, 30):
            return None
        start = relocation["offset"]
        if relocation["type"] == 2 and relocation["symbol"] in known_symbols:
            addend = struct.unpack_from("<I", contents, start)[0]
            struct.pack_into("<I", comparable, start, known_symbols[relocation["symbol"]] + addend)
        else:
            excluded[start:start + 4] = b"\x01" * 4
    spans = []
    start = 0
    for offset in range(len(contents) + 1):
        if offset == len(contents) or excluded[offset]:
            if offset - start >= 4:
                spans.append((start, offset))
            start = offset + 1
    if not spans or len(contents) - sum(excluded) < 16:
        return None
    anchor_start, anchor_end = max(spans, key=lambda span: span[1] - span[0])
    anchor = comparable[anchor_start:anchor_end]
    occurrence = rom.find(anchor)
    candidates = []
    while occurrence >= 0:
        base = occurrence - anchor_start
        if 0 <= base and base + len(contents) <= len(rom):
            if all(excluded[offset] or comparable[offset] == rom[base + offset] for offset in range(len(contents))):
                candidates.append(base)
                if len(candidates) > 1:
                    return None
        occurrence = rom.find(anchor, occurrence + 1)
    return candidates[0] if candidates else None


def main():
    warnings.filterwarnings("ignore", category=SyntaxWarning)
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    mappings = []
    counts = Counter()
    symbol_candidates = {}
    for address, definitions in load_text_label_index(WOKANN).items():
        for definition in definitions:
            symbol_candidates.setdefault(definition["symbol"], set()).add(address)
    text_sources = read_sources(WOKANN)
    charmap = read_charmap(WOKANN / "charmap.txt")
    for symbol, definitions in text_sources.items():
        if symbol in symbol_candidates or len(definitions) != 1:
            continue
        text = definitions[0]["text"]
        encoded = encode_source_controls(text if text.endswith("$") else text + "$", charmap)
        if encoded is None or len(encoded) < 8:
            continue
        offset = rom.find(encoded)
        if offset >= 0 and rom.find(encoded, offset + 1) < 0:
            symbol_candidates[symbol] = {0x08000000 + offset}
    for path in [WOKANN / "src/strings.c", *(WOKANN / "src/data/text").glob("*.h")]:
        for alias in re.finditer(r"\.set\s+gUnknown_([0-9a-fA-F]{7,8}),\s*(\w+)", path.read_text()):
            address = int(alias[1], 16)
            for source in text_sources.get(alias[2], []):
                encoded = encode_source_controls(source["text"] if source["text"].endswith("$") else source["text"] + "$", charmap)
                if encoded and rom[address - 0x08000000:address - 0x08000000 + len(encoded)] == encoded:
                    symbol_candidates.setdefault(alias[2], set()).add(address)
    known_symbols = {symbol: next(iter(addresses)) for symbol, addresses in symbol_candidates.items() if len(addresses) == 1}
    nm = str(ROOT.parent.parent / ".local/devkitpro/devkitARM/bin/arm-none-eabi-nm")
    for symbol, offset in read_symbols(WOKANN / "build/pokeemerald-jp/data/event_scripts.o", nm).items():
        if symbol.startswith(("gText", "gTV", "TV", "Battle", "Bravo", "Trend", "Gabby")) or "_Text_" in symbol:
            known_symbols.setdefault(symbol, 0x081DABAC + offset)
    schemas = json.loads((ROOT / "patch/mapping_reports/checklist_raw_text_table_schemas.json").read_text())["tables"]
    for schema in schemas:
        path = WOKANN / schema["file"]
        source = path.read_text()
        if "binary_file" in schema:
            binary = (WOKANN / schema["binary_file"]).read_bytes()
        else:
            match = re.search(r"const u8 " + schema["symbol"] + r"\[\]\s*=\s*\{([^}]+)\};", source)
            if not match:
                raise ValueError(schema)
            binary = bytes(int(value, 16) for value in re.findall(r"0x([0-9a-fA-F]{2})", match[1]))
        base = int(schema["symbol"].split("_")[1], 16)
        if rom[base - 0x08000000:base - 0x08000000 + len(binary)] != binary:
            raise ValueError((schema, "source block differs from ROM"))
        pointer_end = schema.get("pointer_end_offset", len(binary))
        if not 0 <= schema["first_pointer_offset"] <= pointer_end <= len(binary):
            raise ValueError((schema, "invalid pointer interval"))
        for offset in range(schema["first_pointer_offset"], pointer_end - 3, schema.get("pointer_stride", 4)):
            target = struct.unpack_from("<I", binary, offset)[0]
            if not 0x08000000 <= target < 0x08000000 + len(rom):
                continue
            mappings.append({"address": f"0x{base + offset:08X}", "original": f"0x{target:08X}", "object": schema["file"], "source": schema, "section": "reviewed_raw_text_table", "section_base": f"0x{base:08X}", "section_length": len(binary), "relocation": "reviewed_pointer_load_to_text_consumer", "referenced_symbol": schema["symbol"], "section_offset": offset})
        counts["reviewed_raw_tables"] += 1
    typed_tables = {}
    source_paths = [* (WOKANN / "src").rglob("*.c"), *(WOKANN / "src").rglob("*.h")]
    for path in source_paths:
        source = path.read_text()
        for match in re.finditer(r"extern\s+const\s+u8\s*\*\s*const\s+(gUnknown_[0-9a-fA-F]{7,8})\s*\[\s*\]\s*;", source):
            typed_tables[match[1]] = {"file": str(path.relative_to(WOKANN)), "line": source.count("\n", 0, match.start()) + 1, "declaration": match[0]}
    for path in source_paths:
        source = path.read_text()
        for match in re.finditer(r"\w+_RESOURCE\((gUnknown_([0-9a-fA-F]{7,8})),\s*(0x[0-9a-fA-F]+),\s*\"([^\"]+)\"\)", source):
            if match[1] not in typed_tables:
                continue
            base = int(match[2], 16)
            length = int(match[3], 16)
            binary_path = WOKANN / match[4]
            if length % 4 or not binary_path.is_file():
                continue
            binary = binary_path.read_bytes()
            if len(binary) != length or rom[base - 0x08000000:base - 0x08000000 + length] != binary:
                continue
            for offset in range(0, length, 4):
                target = struct.unpack_from("<I", binary, offset)[0]
                if not 0x08000000 <= target < 0x08000000 + len(rom):
                    continue
                mappings.append({"address": f"0x{base + offset:08X}", "original": f"0x{target:08X}", "object": match[4], "source": str(path.relative_to(WOKANN)), "typed_table": typed_tables[match[1]], "binary_sha256": hashlib.sha256(binary).hexdigest(), "section": "typed_text_pointer_resource", "section_base": f"0x{base:08X}", "section_length": length, "relocation": "typed_u8_pointer_array", "referenced_symbol": match[1], "section_offset": offset})
            counts["verified_typed_raw_tables"] += 1
    for path in sorted((WOKANN / "build/pokeemerald-jp").rglob("*.o")):
        for name, contents, relocations in object_sections(path):
            if path.name == "event_scripts.o" and name == "script_data":
                script_base = 0x081DABAC
                for relocation in relocations:
                    offset = relocation["offset"]
                    if relocation["type"] != 2 or offset < 2 or offset + 6 > len(contents):
                        continue
                    if contents[offset - 2:offset] != b"\x0f\x00" or contents[offset + 4] != 0x09:
                        continue
                    address = script_base + offset
                    rom_offset = address - 0x08000000
                    if rom[rom_offset - 2:rom_offset] != contents[offset - 2:offset] or rom[rom_offset + 4:rom_offset + 6] != contents[offset + 4:offset + 6]:
                        continue
                    target = struct.unpack_from("<I", rom, rom_offset)[0]
                    mappings.append({"address": f"0x{address:08X}", "original": f"0x{target:08X}", "object": str(path.relative_to(WOKANN)), "object_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "section": name, "section_base": f"0x{script_base:08X}", "section_offset": offset, "relocation": "event_msgbox_word", "referenced_symbol": relocation["symbol"], "proof": "Wokann asm/macros/event.inc:1988 msgbox emits loadword bank 0 (0F 00), an ABS32 text relocation, then callstd (09). Compiled field offset plus the established event-script base matches the native prefix, suffix and original pointer; script pointers need not be word-aligned."})
                    counts["verified_event_msgbox_fields"] += 1
            counts["sections"] += 1
            base = locate_section(rom, contents, relocations, known_symbols)
            if base is None:
                counts["unanchored_sections"] += 1
                continue
            counts["byte_exact_sections"] += 1
            for relocation in relocations:
                if relocation["type"] != 2:
                    continue
                address = base + relocation["offset"]
                if address % 4:
                    continue
                target = struct.unpack_from("<I", rom, address)[0]
                if not 0x08000000 <= target < 0x08000000 + len(rom):
                    continue
                mappings.append({"address": f"0x{address + 0x08000000:08X}", "original": f"0x{target:08X}", "object": str(path.relative_to(WOKANN)), "object_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "section": name, "section_base": f"0x{base + 0x08000000:08X}", "section_length": len(contents), "relocation": "R_ARM_ABS32", "referenced_symbol": relocation["symbol"], "section_offset": relocation["offset"]})
    document = {"policy": "Unique whole-section match excluding only typed relocation fields; nonrelocated bytes all match JP base ROM. Unanchored or unsupported sections are excluded.", "summary": dict(counts), "references": mappings}
    args.output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n")
    print(document["summary"], "references", len(mappings))


if __name__ == "__main__":
    main()
