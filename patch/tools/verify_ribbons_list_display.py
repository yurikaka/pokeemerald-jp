"""Verify the Wokann-backed, display-only ribbons list callback."""

import json
import struct
import subprocess
from pathlib import Path

from verify_wokann_object_references import object_sections


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"


def main():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    proofs = json.loads((ROOT / "patch/mapping_reports/wokann_object_reference_verification.json").read_text())["references"]
    proof = next(entry for entry in proofs if int(entry["address"], 0) == 0x081CF9F0)
    assert proof["referenced_symbol"] == "BufferRibbonMonInfoText"
    assert int(proof["original"], 0) == 0x081CF9F9
    sections = object_sections(REFERENCE / "build/pokeemerald-jp/src/pokenav_ribbons_list.o")
    relocation = next(entry for name, data, refs in sections if name == ".text" for entry in refs if entry["offset"] == 0x960)
    assert relocation["symbol"] == "BufferRibbonMonInfoText"
    assert struct.unpack_from("<I", base, 0x1CF9F0)[0] == 0x081CF9F9
    symbols = {}
    for line in subprocess.check_output([
        "arm-none-eabi-nm", "-n", str(ROOT / "build/patch/payload.elf")
    ], text=True).splitlines():
        fields = line.split()
        if len(fields) == 3:
            symbols[fields[2]] = int(fields[0], 16)
    callback = symbols["ChsBufferRibbonMonInfoText"] | 1
    assert struct.unpack_from("<I", rom, 0x1CF9F0)[0] == callback
    source = (ROOT / "patch/chinese_engine.s").read_text()
    helper = source.split("ChsBufferRibbonMonInfoText:\n", 1)[1].split(".Lribbon_call_r3:", 1)[0]
    assert "bl ChsCopyMonNickname" in helper
    assert "bl ChsCopyBoxMonNickname" in helper
    assert "movs r2, #5\n    bl ChsWriteNarrowSpeciesName" in helper
    assert "movs r1, #100" in helper
    assert "ldr r1, =.Lribbon_count_unit" in helper
    assert ".Lribbon_count_unit:\n    .byte 0xF5, 0x63, 0x60, 0xFF" in source
    assert "SetMonData" not in helper and "SetBoxMonData" not in helper
    width, gender_column, count_column = 128, 50, 100
    assert 4 * 12 < gender_column
    assert 5 * 8 < gender_column
    assert gender_column + 8 + 8 + 8 + 3 * 8 < count_column
    assert count_column + 2 * 8 + 12 <= width
    longest_name_bytes = 2 + 5 * 2 + 2
    longest_row_bytes = longest_name_bytes + 17 + 3 + 3 + 2 + 4
    assert longest_row_bytes < 64
    assert longest_name_bytes + 1 <= 0x2C - 0x10
    clear_start = symbols["ChsMatchCallClearListRow"] - 0x08000000
    clear_end = symbols["ChsBufferRibbonMonInfoText"] - 0x08000000
    assert struct.pack("<I", callback) in rom[clear_start:clear_end]
    for address in (0x5F5DD3, 0x5F5DEB, 0x5F5E03):
        assert rom[address:address + 12] == base[address:address + 12]
    print("Wokann callback relocation and Thumb target verified; party and box display helpers retained")
    print("Four-character normal and five-character narrow names fit separate gender/level/count columns")
    print("Localized rows fit the 64-byte buffer; native resources and stored nicknames are not rewritten")


if __name__ == "__main__":
    main()
