#!/usr/bin/env python3
"""Attach table-index and emitted-ROM evidence to checklist resource rows."""

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import struct
import warnings

from build_texts import encode_text, wrap_pokedex_description
from execute_verified_checklist import write_patch
from port_map_dialogue import read_charmap, read_symbols
from review_text_checklists import ROOT, US, read_sources


def numeric_constants(path):
    return {name: int(value, 0) for name, value in re.findall(r"^#define\s+(\w+)\s+(0x[0-9a-fA-F]+|\d+)\s*$", path.read_text(), re.MULTILINE)}


def main():
    warnings.filterwarnings("ignore", category=SyntaxWarning)
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--nm", required=True)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    sources = read_sources(US)
    symbols = read_symbols(ROOT / "build/patch/payload.elf", args.nm)
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    indexed = defaultdict(list)
    for filename, constants_file, prefix, table in (
        ("src/data/text/move_descriptions.h", "moves.h", "MOVE", "move_descriptions.json"),
        ("src/data/text/abilities.h", "abilities.h", "ABILITY", "ability_descriptions.json"),
    ):
        constants = numeric_constants(US / "include/constants" / constants_file)
        document = json.loads((ROOT / "patch" / table).read_text())
        for identifier, text_symbol in re.findall(r"\[(" + prefix + r"_\w+)(?:\s*-\s*1)?\]\s*=\s*(\w+)", (US / filename).read_text()):
            if identifier not in constants or text_symbol not in sources:
                continue
            index = constants[identifier]
            indexed[text_symbol].append({"table": document["name"], "index": index, "text": document["strings"][index], "stride": document["stride"], "file": "patch/" + table, "us_source": filename})
    document = json.loads((ROOT / "patch/item_descriptions.json").read_text())
    names = re.findall(r"\.description\s*=\s*(\w+)", (US / "src/data/items.h").read_text())
    for index, name in enumerate(names):
        indexed[name].append({"table": document["name"], "index": index, "text": document["strings"][index], "stride": 4, "pointer_offset": 0, "file": "patch/item_descriptions.json", "us_source": "src/data/items.h"})
    document = json.loads((ROOT / "patch/decoration_info.json").read_text())
    names = re.findall(r"\.description\s*=\s*(DecorDesc_\w+)", (US / "src/data/decoration/header.h").read_text())
    for index, name in enumerate(names):
        indexed[name].append({"table": document["name"], "index": index, "text": sources[name][0]["text"], "stride": document["stride"], "pointer_offset": document["description_offset"], "file": "patch/decoration_info.json", "us_source": "src/data/decoration/header.h"})
    for part in (1, 2):
        names = re.findall(r"static const u8 (sBerryDescriptionPart" + str(part) + r"_\w+)\[\]", (US / "src/berry.c").read_text())
        for index, name in enumerate(names):
            indexed[name].append({"table": "ChsBerryDescriptionPart" + str(part), "index": index, "text": sources[name][0]["text"], "stride": 4, "pointer_offset": 0, "file": "patch/berry_info.json", "us_source": "src/berry.c"})
    dex = json.loads((ROOT / "patch/pokedex_entries.json").read_text())
    dex_names = re.findall(r"\.categoryName\s*=\s*_\(\s*\"(?:[^\"\\]|\\.)*\"\s*\).*?\.description\s*=\s*(g\w+)", (US / "src/data/pokemon/pokedex_entries.h").read_text(), re.DOTALL)
    for index, name in enumerate(dex_names):
        indexed[name].append({"table": dex["name"], "index": index, "text": dex["entries"][index]["description"], "stride": 28, "pointer_offset": 12, "file": "patch/pokedex_entries.json", "us_source": "src/data/pokemon/pokedex_entries.h", "pokedex": True})
    counts = Counter()
    for record in plan["records"]:
        if record["kind"] != "port" or record["decision"] not in ("already_ported_structured", "already_ported_pokedex"):
            continue
        entries = indexed.get(record["symbol"], [])
        if not entries:
            record["resource_verification"] = "missing_index_mapping"
            counts["missing_index_mapping"] += 1
            continue
        evidence = []
        for entry in entries:
            address = symbols[entry["table"]] + entry["index"] * entry["stride"]
            if "pointer_offset" in entry:
                address = struct.unpack_from("<I", rom, address - 0x08000000 + entry["pointer_offset"])[0]
            expected = encode_text(entry["text"], charmap, False)
            if entry.get("pokedex") and entry["index"]:
                expected = wrap_pokedex_description(expected, charmap)
            actual = rom[address - 0x08000000:address - 0x08000000 + len(expected)]
            if expected != actual:
                raise ValueError((record["symbol"], entry["index"], "emitted ROM differs"))
            evidence.append({**entry, "rom_address": f"0x{address:08X}", "encoded_hex": expected.hex(), "rom_bytes_match": True})
        record["resource_verification"] = "table_index_and_rom_bytes_verified"
        record["resource_evidence"] = evidence
        record["final_text"] = entries[0]["text"]
        record["execution"] = "existing_resource_verified"
        counts["existing_resource_verified"] += 1
    plan["resource_verification_summary"] = dict(counts)
    write_patch(args.plan, plan)
    print(dict(counts))


if __name__ == "__main__":
    main()
