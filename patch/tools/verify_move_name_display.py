"""Verify selective narrow move names and their Summary/battle display references."""

import hashlib
import json
import struct
import subprocess
from pathlib import Path

from PIL import Image

from build_muzaipixel_memo_font import glyph_index
from build_texts import encode_compact_chinese_text, encode_text, read_charmap


ROOT = Path(__file__).resolve().parents[2]
WOKANN = ROOT.parent / "pokeemerald_wokann_dev"
ROM_BASE = 0x08000000
DISPLAY_FIELDS = (0x08059730, 0x081C3440, 0x081C3800, 0x081C3874)


def main():
    document = json.loads((ROOT / "patch/move_names.json").read_text())
    base = (ROOT / "baserom_jp.gba").read_bytes()
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    narrow_atlas = Image.open(ROOT / "patch/fonts/muzaipixel_chinese.png")
    symbols = {}
    for line in subprocess.check_output(["arm-none-eabi-nm", "-n", str(ROOT / "build/patch/payload.elf")], text=True).splitlines():
        parts = line.split()
        if len(parts) == 3:
            symbols[parts[2]] = int(parts[0], 16)
    normal_address = symbols[document["name"]]
    display_address = symbols[document["display_variant"]["name"]]
    narrow_names = []
    for index, text in enumerate(document["strings"]):
        normal = encode_text(text, charmap, False)
        display = normal
        if len(text) == document["display_variant"]["narrow_length"]:
            assert all(len(charmap[char]) == 2 for char in text)
            for char in text:
                glyph = glyph_index(charmap[char])
                left, top = glyph % 16 * 16, glyph // 16 * 16
                tile = narrow_atlas.crop((left, top, left + 8, top + 13))
                assert 1 in tile.tobytes(), f"Missing narrow move-name glyph: {char}"
            display = bytes((0xF5, 0xF3)) + encode_compact_chinese_text(text, charmap)[1:-1] + bytes((0xF5, 0xF4, 0xFF))
            narrow_names.append(text)
        assert len(display) <= document["stride"]
        for address, expected in ((normal_address, normal), (display_address, display)):
            offset = address - ROM_BASE + index * document["stride"]
            expected += bytes((0xFF,)) * (document["stride"] - len(expected))
            assert rom[offset:offset + document["stride"]] == expected, (index, text, hex(address))
    assert len(narrow_names) == 5
    proofs = json.loads((ROOT / "patch/mapping_reports/wokann_object_reference_verification.json").read_text())["references"]
    for address in DISPLAY_FIELDS:
        assert struct.unpack_from("<I", base, address - ROM_BASE)[0] == 0x082EACC4
        proof = next(entry for entry in proofs if int(entry["address"], 16) == address)
        assert proof["referenced_symbol"] == "gMoveNames"
        assert hashlib.sha256((WOKANN / proof["object"]).read_bytes()).hexdigest() == proof["object_sha256"]
        assert struct.unpack_from("<I", rom, address - ROM_BASE)[0] == display_address
    manifest = json.loads((ROOT / "patch/manifest.json").read_text())
    replacement = next(entry for entry in manifest["pointer_replacements"] if int(entry["old"], 16) == 0x082EACC4)
    excluded = {int(address, 16) for address in replacement["exclude"]}
    assert set(DISPLAY_FIELDS) <= excluded
    for offset in range(0, len(base), 4):
        if struct.unpack_from("<I", base, offset)[0] == 0x082EACC4 and offset + ROM_BASE not in excluded:
            assert struct.unpack_from("<I", rom, offset)[0] == normal_address
    print("Five narrow move names verified: " + ", ".join(narrow_names))
    print("Four Wokann-backed display references verified; normal table, other callers and 16-byte strides unchanged")


if __name__ == "__main__":
    main()
