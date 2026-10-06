"""Build identity-checked JP/CHS NPC mappings, without rewriting JP data."""
import json
from pathlib import Path
import re
import struct
from build_texts import encode_text, encode_compact_chinese_text, read_charmap
from port_map_dialogue import encode_japanese, read_charmap as read_jp_charmap

ROOT = Path(__file__).resolve().parents[2]
JP = ROOT.parent / "pokeemerald_wokann_dev"
US = ROOT.parent / "pokeemerald_us_chs"

def records(source, symbol):
    body = source.split(" " + symbol + "[", 1)[1].split("\n};", 1)[0]
    return re.findall(r'\[(\w+)\]\s*=\s*\{.*?\.trainerName\s*=\s*__?\("([^"]*)"\)', body, re.S)

def main():
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    cm = read_charmap(ROOT / "patch/charmap_chs.txt")
    jp_cm = read_jp_charmap(JP / "charmap.txt")
    mappings = []
    tables = [
        ("battle_frontier_trainers.h", "gBattleFrontierTrainers", 0x08165A84),
        ("battle_tent.h", "gSlateportBattleTentTrainers", 0x08165BA8),
        ("battle_tent.h", "gVerdanturfBattleTentTrainers", 0x08165BC8),
        ("battle_tent.h", "gFallarborBattleTentTrainers", 0x08165BE8),
    ]
    for file, symbol, literal in tables:
        relative = "src/data/battle_frontier/" + file
        jp = records((JP / relative).read_text(), symbol)
        chs = records((US / relative).read_text(), symbol)
        assert jp and [x[0] for x in jp] == [x[0] for x in chs], symbol
        address = struct.unpack_from("<I", rom, literal - 0x08000000)[0]
        for index, ((key, original), (_, chinese)) in enumerate(zip(jp, chs)):
            pointer = address + index * 52 + 4
            expected = encode_japanese('.string ' + json.dumps(original.split("$")[0] + "$", ensure_ascii=False), jp_cm)
            assert expected and rom[pointer - 0x08000000:pointer - 0x08000000 + len(expected)] == expected, (symbol, key)
            mappings.append((pointer, chinese, key))
    trainers = records((US / "src/data/trainers.h").read_text(), "gTrainers")
    assert len(trainers) == 855
    jp_ids = (JP / "include/constants/opponents.h").read_text()
    for index in range(804, 812):
        key, chinese = trainers[index]
        assert re.search(r'^#define\s+' + key + r'\s+' + str(index) + r'\s*$', jp_ids, re.M), (index, key)
        mappings.append((0x082E3840 + index * 32, chinese, key))
    lines = ["/* Generated: NPC identity and original Japanese ROM bytes checked. */"]
    for index, (_, chinese, _) in enumerate(mappings):
        encoded = encode_text(chinese + "{JPN}", cm, False)
        lines.append("static const u8 npc_name_%d[] = {%s};" % (index, ",".join(str(x) for x in encoded)))
    lines.append("static const struct NamePair npc_names[] = {")
    for index, (pointer, _, key) in enumerate(mappings):
        lines.append("    {(const u8 *)0x%08X, npc_name_%d}, /* %s */" % (pointer, index, key))
    lines.append("};")
    # The link VS screen has an eight-byte display buffer. Original link
    # records remain JP; these compact strings never leave the display path.
    for index, (_, chinese, _) in enumerate(mappings[:300]):
        encoded = encode_compact_chinese_text(chinese, cm)
        assert len(encoded) <= 8, (index, chinese)
        lines.append("static const u8 npc_compact_%d[] = {%s};" % (index, ",".join(str(x) for x in encoded)))
    lines.append("static const u8 *const npc_compact_names[] = {")
    lines.extend("    npc_compact_%d," % index for index in range(300))
    lines.append("};")
    steven = encode_text(trainers[804][1] + "{JPN}", cm, False)
    lines.append("const u8 ChsNpcStevenName[] = {%s};" % ",".join(str(x) for x in steven))
    (ROOT / "build/patch/npc_names.h").write_text("\n".join(lines) + "\n")
    print(f"Verified {len(mappings)} NPC identity mappings; original tables untouched")

if __name__ == "__main__":
    main()
