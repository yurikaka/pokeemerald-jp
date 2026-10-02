#!/usr/bin/env python3
"""Read-only batch452 source, buffer, language and pointer checks; no ROM build."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess

from build_texts import convert_us_encoded_text, encode_compact_chinese_text, read_charmap
from port_map_dialogue import read_charmap as read_source_charmap
from review_text_checklists import encode_source_controls


ROOT = Path(__file__).resolve().parents[2]
WOKANN = ROOT.parent / "pokeemerald_wokann_dev"
US = ROOT.parent / "pokeemerald_us_chs"
FILENAME = "452_checklist_storage_dynamic.json"
ROM_BASE = 0x08000000
TABLE = 0x0854CA1C
ENTRIES = (
    ("gText_ByeByePkmn", 11, 6, 0x085CB263, "4602460200f700abff"),
    ("gText_ChangedToNewItem", 29, 7, 0x085CB352, "f70014001428060410abff"),
    ("gText_ItemIsNowHeld", 28, 7, 0x085CB348, "f7002d0023100e10abff"),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def function_body(source, name):
    match = re.search(r"^[^\n;]*\b" + re.escape(name) + r"\([^;]*?\n\{.*?^\}", source, re.M | re.S)
    require(match is not None, f"missing function {name}")
    return match.group()


def thumb_bl_target(address, encoded):
    upper, lower = struct.unpack("<HH", encoded)
    require(upper & 0xF800 == 0xF000 and lower & 0xF800 == 0xF800, "not a Thumb BL")
    displacement = ((upper & 0x7FF) << 12) | ((lower & 0x7FF) << 1)
    if displacement & 0x400000:
        displacement -= 0x800000
    return address + 4 + displacement


def expand(template, producer, capacity=40):
    require(producer.endswith(b"\xff"), "unterminated producer")
    memory = bytearray(b"\xa5" * (capacity + 8))
    cursor = 0
    position = 0
    while template[position] != 0xFF:
        if template[position] == 0xF7:
            require(template[position + 1] == 0, "unexpected dynamic slot")
            chunk = producer[:producer.index(0xFF)]
            position += 2
        else:
            chunk = template[position:position + 1]
            position += 1
        require(cursor + len(chunk) < capacity, "messageText overflow")
        memory[cursor:cursor + len(chunk)] = chunk
        cursor += len(chunk)
    memory[cursor] = 0xFF
    require(memory[capacity:] == b"\xa5" * 8, "messageText canary changed")
    return bytes(memory[:cursor + 1])


def padded_item(encoded):
    payload = encoded[:-1]
    displayed = payload + b"\x00" * max(0, 8 - len(payload)) + b"\xff"
    require(len(displayed) <= 39 and len(displayed) <= 20, "pre-trim item copy overflow")
    require(displayed[0] == 0xF5, "item must have a non-space compact-mode prefix")
    trimmed = displayed[:-1].rstrip(b"\x00") + b"\xff"
    repaired = trimmed[:-1] + b"\x00"
    require(repaired in (encoded[:-1], encoded[:-1] + b"\x00"), "one-byte template separator cannot repair this name")
    return displayed, trimmed


def render_width(data, species_names, latin_widths):
    mode = "jp"
    position = 0
    width = 0
    while data[position] != 0xFF:
        token = data[position]
        if token == 0xFC:
            control = data[position + 1]
            require(control in (0x15, 0x16), "unexpected mode control")
            narrow = mode in ("narrow", "narrow_jp")
            mode = ("narrow_jp" if narrow else "jp") if control == 0x15 else ("narrow" if narrow else "chs")
            position += 2
        elif token == 0xF5:
            following = data[position + 1]
            if following == 0xF3:
                mode = "narrow"
                position += 2
            elif following == 0xF2:
                species = int.from_bytes(data[position + 2:position + 4], "little")
                require(species < len(species_names), "invalid compact species")
                width += 12 * len(species_names[species])
                mode = "jp"
                position += 4
            else:
                mode = "narrow" if mode == "narrow_jp" else "chs"
                position += 1
        elif mode in ("chs", "narrow") and (token == 0x7F or 0x60 <= token <= 0x7D and token not in (0x65, 0x7A)):
            require(data[position + 1] <= 0xF6, "broken Chinese pair")
            width += latin_widths[data[position + 1]] if mode == "narrow" and token == 0x7F else (8 if mode == "narrow" else 12)
            position += 2
        else:
            width += latin_widths[token] if mode == "narrow" else 12
            position += 1
    return width


def verify():
    branch = subprocess.check_output(["git", "-C", str(WOKANN), "branch", "--show-current"], text=True).strip()
    require(branch == "dev", "Wokann must be on dev")
    commit = subprocess.check_output(["git", "-C", str(WOKANN), "rev-parse", "HEAD"], text=True).strip()
    base = (ROOT / "baserom_jp.gba").read_bytes()
    require(base == (WOKANN / "baserom_jp.gba").read_bytes(), "JP and Wokann base ROMs differ")
    table = (WOKANN / "data/pokemon_storage/jp/0854CA1C.bin").read_bytes()
    require(len(table) == 248 and table == base[TABLE - ROM_BASE:TABLE - ROM_BASE + 248], "storage table differs")
    source = (WOKANN / "src/pokemon_storage_system.c").read_text()
    for declaration in ("STORAGE_MON_NAME_LENGTH 11", "messageText[40]", "displayMonName[STORAGE_MON_NAME_LENGTH]", "releaseMonName[STORAGE_MON_NAME_LENGTH]", "itemName[20]", "displayMonItemName[39]"):
        require(declaration in source, f"changed buffer declaration: {declaration}")
    functions = {}
    for filename, names in (
        ("pokemon_storage_system.c", ("PrintStorageActionText", "SetCursorMonData", "sub_080CDACC", "GetMovingItemName")),
        ("string_util.c", ("StringCopy", "StringGet_Nickname", "StringCopyPadded")),
        ("dynamic_placeholder_text_util.c", ("DynamicPlaceholderTextUtil_ExpandPlaceholders",)),
        ("item.c", ("SanitizeItemId",)),
    ):
        contents = (WOKANN / "src" / filename).read_text()
        for name in names:
            body = function_body(contents, name)
            functions[name] = {"file": "../pokeemerald_wokann_dev/src/" + filename, "line": contents[:contents.index(body)].count("\n") + 1, "sha256": hashlib.sha256(body.encode()).hexdigest()}
    require("u32 limit = 5" in function_body((WOKANN / "src/string_util.c").read_text(), "StringGet_Nickname"), "nickname limit changed")
    strings = (WOKANN / "src/strings.c").read_text()
    block = re.search(r"gUnknown_85CB1B9\[\]\s*=\s*\{([^}]+)\}", strings).group(1)
    block_bytes = bytes(int(value, 16) for value in re.findall(r"0x([0-9A-Fa-f]{2})\b", block))
    require(base[0x5CB1B9:0x5CB1B9 + len(block_bytes)] == block_bytes, "Wokann strings block differs")
    manifest = json.loads((ROOT / "patch/manifest.json").read_text())
    assembly = (ROOT / "patch/chinese_engine.s").read_text()
    hooks = []
    for address, original_target, patched_target, symbol in (
        (0x080CE50E, 0x0806A058, 0x081B1814, "ChsGetMonNickname"),
        (0x080CE606, 0x0806A1B4, 0x0806F4D0, "ChsGetMonNicknameFromBox"),
    ):
        patch = next(entry for entry in manifest["code_patches"] if int(entry["address"], 0) == address)
        require(bytes.fromhex(patch["original"]) == base[address - ROM_BASE:address - ROM_BASE + 4], "nickname call original mismatch")
        require(thumb_bl_target(address, bytes.fromhex(patch["original"])) == original_target, "unexpected nickname producer")
        require(thumb_bl_target(address, bytes.fromhex(patch["replacement"])) == patched_target, "nickname hook route changed")
        hook = next(entry for entry in manifest["function_hooks"] if int(entry["address"], 0) == patched_target)
        require(hook["symbol"] == symbol, "nickname hook symbol changed")
        require(f"0x{address + 5:08X}" in assembly, "storage caller missing in display router")
        hooks.extend((patch, hook))
    item_hook = next(entry for entry in manifest["function_hooks"] if entry["symbol"] == "ChsItemIdGetName")
    require(item_hook["address"] == "0x080D6C8C", "item getter hook moved")
    hooks.append(item_hook)
    for entry in hooks:
        address = int(entry["address"], 0)
        original = bytes.fromhex(entry["original"])
        require(base[address - ROM_BASE:address - ROM_BASE + len(original)] == original, "hook original mismatch")
    assembly_evidence = {}
    for start, end in (("ChineseRenderHook:", ".global ChsNamingScreenSpeciesTitle"), ("ChsCopyMonNickname:", ".global ChsGetBoxMonNickname"), ("ChsGetBoxMonNickname:", ".global ChsGetBoxMonNickAt"), ("ChsGetMonNickname:", ".global ChsFaintFromFieldPoison"), ("ChsTradeNicknameRouter:", ".type ChsTruncateNickname"), (".Lbox_nickname_data_callers:", ".type ChsCopyStoredNicknameForSpecies"), ("ChsItemIdGetName:", ".global ChsGetBerryNameByType"), ("DecompressChineseGlyph:", ".Lset_dimensions:")):
        begin = assembly.index(start)
        finish = assembly.index(end, begin)
        assembly_evidence[start] = {"line": assembly[:begin].count("\n") + 1, "sha256": hashlib.sha256(assembly[begin:finish].encode()).hexdigest()}
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    item_table = json.loads((ROOT / "patch/item_names.json").read_text())
    require(item_table["stride"] == 16 and item_table["compact_chinese"] and len(item_table["strings"]) == 377, "item table contract changed")
    items = [encode_compact_chinese_text(text, charmap) for text in item_table["strings"]]
    require(all(len(item) <= 16 and item.index(0xFF) == len(item) - 1 for item in items), "item stride or EOS changed")
    display_items = [padded_item(item) for item in items]
    species_source = (US / "src/data/text/species_names.h").read_text().split("const u8 gSpeciesNames[][POKEMON_NAME_LENGTH + 1] = {", 1)[1]
    species_names = re.findall(r'\[SPECIES_\w+\]\s*=\s*_\("([^"]*)"\)', species_source)
    require(len(species_names) == 412 and max(map(len, species_names)) <= 5, "species display width changed")
    latin_widths = (ROOT / "patch/fonts/muzaipixel_latin_widths.bin").read_bytes()
    windows = (WOKANN / "data/pokemon_storage/jp/0854C9C4.bin").read_bytes()
    require(windows == base[0x54C9C4:0x54C9C4 + len(windows)], "window resource mismatch")
    require(windows[11:13] == bytes((18, 2)), "action window dimensions changed")
    batch = json.loads((ROOT / "patch/batches" / FILENAME).read_text())
    require(len(batch["texts"]) == len(batch["reference_writes"]) == 3, "expected exactly three definitions and writes")
    target_addresses = {int(entry["address"], 0) for entry in batch["reference_writes"]}
    for path in (ROOT / "patch/batches").glob("*.json"):
        if path.name == FILENAME:
            continue
        other = json.loads(path.read_text())
        if isinstance(other, dict):
            require(not any(int(entry["address"], 0) in target_addresses for entry in other.get("reference_writes", [])), f"conflicting batch: {path.name}")
    for category in ("pointer_writes", "code_patches", "function_hooks", "veneer_hooks"):
        require(not any(int(entry["address"], 0) in target_addresses for entry in manifest.get(category, [])), f"manifest conflict: {category}")
    require(not any(int(entry["old"], 0) in {entry[3] for entry in ENTRIES} for entry in manifest["pointer_replacements"]), "global replacement conflict")
    us_strings = (US / "src/strings.c").read_text()
    us_charmap = read_source_charmap(US / "charmap.txt")
    mapping = []
    for symbol, message_id, format_id, original, jp_hex in ENTRIES:
        definition = next(entry for entry in batch["texts"] if entry["source_symbol"] == symbol)
        reference = next(entry for entry in batch["reference_writes"] if entry["source_symbol"] == symbol)
        pointer = TABLE + message_id * 8
        require(reference == {"address": f"0x{pointer:08X}", "original": f"0x{original:08X}", "symbol": definition["name"], "source_symbol": symbol}, "reference contract changed")
        require(struct.unpack_from("<I", table, message_id * 8)[0] == original and table[message_id * 8 + 4] == format_id, "wrong message or format field")
        require(base[original - ROM_BASE:original - ROM_BASE + len(bytes.fromhex(jp_hex))] == bytes.fromhex(jp_hex), "JP source mismatch")
        text = re.search(r"const u8 " + symbol + r'\[\] = _\("([^"]*)"\);', us_strings).group(1)
        source_encoded = encode_source_controls(text + "$", us_charmap)
        is_item = format_id == 7
        expected_raw = b"\xf5\xf3" + source_encoded.replace(b"\xf7\x00", b"\xfc\x15\xf7\x00\x00\xfc\x16") if is_item else source_encoded
        require(bytes.fromhex(definition["us_encoded_hex"]) == expected_raw, "full US text or font prefix changed")
        require(definition.get("japanese_dynamic") is (not is_item) and definition.get("auto_wrap") is False, "language/wrapping contract changed")
        encoded = convert_us_encoded_text(expected_raw, set(), not is_item)
        guard = b"\xfc\x15\xf7\x00" + (b"\x00" if is_item else b"") + b"\xfc\x16"
        require(encoded.count(b"\xf7\x00") == 1 and guard in encoded, "dynamic guard or byte-repair separator missing")
        if is_item:
            producers = [item[:-1].rstrip(b"\x00") + b"\xff" for item in items] + [trimmed for displayed, trimmed in display_items]
            max_payload = 15
        else:
            producers = [b"\xff", b"\x60\x61\x62\x63\x64\xff", b"\xbb\xbc\xbd\xbe\xbf\xff"]
            producers.extend(b"\xf5\xf2" + species.to_bytes(2, "little") + b"\xff" for species in range(412) if species != 255)
            max_payload = 10
        results = [expand(encoded, producer) for producer in producers]
        worst = len(encoded) - 2 + max_payload
        expand(encoded, b"\xbb" * max_payload + b"\xff")
        width = max(render_width(result, species_names, latin_widths) for result in results)
        require(worst <= 40 and width <= 144, "message exceeds buffer or window")
        plain = convert_us_encoded_text(source_encoded, set(), True)
        mapping.append({
            "symbol": symbol, "final_text": text, "decision": "verified_source_safe_pointer_patch",
            "jp_source": {"file": "../pokeemerald_wokann_dev/src/strings.c", "symbol": "gUnknown_85CB1B9", "offset": original - 0x085CB1B9, "encoded_hex": jp_hex},
            "reference": reference, "message_id": message_id, "format_id": format_id,
            "encoded_hex": encoded.hex(), "template_bytes_including_eos": len(encoded),
            "max_placeholder_bytes_excluding_eos": max_payload, "worst_expanded_bytes_including_eos": worst,
            "actual_producer_max_expanded_bytes": max(map(len, results)), "message_buffer_bytes": 40,
            "headroom_bytes": 40 - worst, "producer_cases": len(producers), "max_width_bound_px": width,
            "unmodified_full_translation_width_bound_px": max(render_width(expand(plain, producer), species_names, latin_widths) for producer in (items if is_item else producers)),
            "language_contract": "FC16 F5F3 enters narrow Chinese; explicit FC15 before F7 enters narrow-JP; item-leading F5 restores narrow Chinese. A literal 00 immediately after F7 rejoins a trimmed trailing glyph byte (item 25, 活力块) or adds a separator space for intact names. Only THEN FC16 restores/preserves Chinese mode. Automatic japanese_dynamic must stay false because it would insert FC16 before the repair byte. No original words are removed; no line wrapping." if is_item else "FC15 protects JP kana/custom nicknames. Existing display-only F5 F2 species tokens are rendered, not expanded into messageText; the renderer returns to JP, so FC16 restores Chinese before the suffix.",
            "merge_update": {"symbol": symbol, "batch": FILENAME, "status": "source_verified_patch_ready_not_runtime_verified", "new_definition_count": 1, "new_reference_count": 1},
        })
    return {
        "policy": "Only three typed StorageMessage.text pointer writes. Public ASM, manifest, persisted names, trackers and action plans are untouched. This is source/model verification, not an emitted-ROM or emulator claim.",
        "wokann_branch": branch, "wokann_commit": commit, "base_sha1": hashlib.sha1(base).hexdigest(),
        "storage_table": {"address": "0x0854CA1C", "bytes": 248, "stride": 8, "text_offset": 0, "format_offset": 4, "action_window_pixels": [144, 16]},
        "producer_contract": {
            "nickname": "SetCursorMonData's two existing call patches route party/box getters to display-only nickname copies. Both truncate to five bytes before writing, or write a four-byte F5 F2 species token plus EOS. StringGet_Nickname then caps at five; sub_080CDACC copies only displayMonName to releaseMonName[11]. Memory proof also checks a conservative ten-byte payload. Persistent setters are not changed.",
            "nickname_test_scope": "Empty, high-byte JP kana, Latin custom names and all EOS-safe compact species IDs. ID 255 is an unused old-Unown slot whose existing token embeds EOS; it is not claimed as a supported nickname hook case. Malformed save data is outside this patch's producer contract.",
            "items": "SanitizeItemId maps out-of-range IDs to item 0; existing ChsItemIdGetName selects compact ChsItemNames[377][16]. F5 is counted, EOS is counted, maximum payload is 15. StringCopyPadded copies the entire source, padding to at least eight bytes, not truncating. Its maximum is 16 including EOS, below displayMonItemName[39] AND itemName[20] before trimming. Leading non-space F5 prevents trailing-space trim underflow. BOTH moving and displayed paths then trim bytes, not glyphs: item 25 loses the 00 in 块=6700. The template supplies exactly one 00 BEFORE FC16; all 377 repaired payloads equal the original name, optionally followed by a separator space. No producer or persisted data is modified.",
            "item_count": len(items), "max_item_bytes_including_eos": max(map(len, items)),
            "max_displayed_item_bytes_including_eos": max(len(displayed) for displayed, trimmed in display_items),
            "trimmed_glyph_repairs": [{"item_id": index, "text": item_table["strings"][index], "original_hex": item.hex(), "trimmed_hex": display_items[index][1].hex()} for index, item in enumerate(items) if item != display_items[index][1]],
            "max_chinese_species_glyphs": max(map(len, species_names)),
        },
        "source_functions": functions, "existing_hook_evidence": hooks, "existing_asm_sections_sha256": assembly_evidence,
        "mode_jump_table": manifest["mode_jump_table"], "mapping": mapping,
        "active_reference_writes": batch["reference_writes"], "active_definition_count": 3, "active_reference_count": 3,
        "validation": {"method": "Local Wokann source/binary identity, Thumb call decoding, exact US text encoding, all 377 item names through both producer paths, canary expansion and mode-aware conservative width model.", "full_build_run": False, "emulator_run": False, "remaining_runtime_checks": ["Release a default-named and custom-named party/boxed mon; check Chinese suffix after nickname.", "Give/swap longest available item names; check narrow-font readability and both moving/displayed branches."]},
        "integration": "Makefile already globs patch/batches/*.json for build_texts.py and apply_patch.py. The explicit user-requested batch452 filename needs no manifest edit; numeric-only checklist report refreshers may need to import this standalone report explicitly. No master tracker was written.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print regenerated evidence without writing any file")
    args = parser.parse_args()
    report = verify()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        stored = json.loads((ROOT / "patch/mapping_reports" / FILENAME).read_text())
        require(stored == report, "mapping report is stale; inspect --json output before updating only this report")
        for entry in report["mapping"]:
            print(f"PASS {entry['symbol']}: {entry['worst_expanded_bytes_including_eos']}/40 bytes, width <= {entry['max_width_bound_px']}/144 px, {entry['producer_cases']} producer cases")


if __name__ == "__main__":
    main()
