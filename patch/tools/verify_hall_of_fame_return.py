"""Check the Hall of Fame display adapter's compiled return preservation."""

import struct
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ROM_BASE = 0x08000000


def branch_target(rom, address):
    first, second = struct.unpack_from("<HH", rom, address - ROM_BASE)
    assert first & 0xF800 == 0xF000 and second & 0xF800 == 0xF800
    displacement = ((first & 0x7FF) << 12) | ((second & 0x7FF) << 1)
    if displacement & 0x400000:
        displacement -= 0x800000
    return address + 4 + displacement


def main():
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    base = (ROOT / "baserom_jp.gba").read_bytes()
    reference = (ROOT.parent / "pokeemerald_wokann_dev/src/hall_of_fame.c").read_text()
    assert reference.count('"\tadd r1, sp, #0xc\\n\\t"\n        "\tbl GetStringWidth\\n\\t"') == 2
    assert '"\tsub sp, #0x1c\\n\\t"' in reference
    symbols = {}
    for line in subprocess.check_output([
        "arm-none-eabi-nm", "-n", str(ROOT / "build/patch/payload.elf")
    ], text=True).splitlines():
        fields = line.split()
        if len(fields) == 3:
            symbols[fields[2]] = int(fields[0], 16)
    router = symbols["ChsNicknameDisplayRouter"] - ROM_BASE
    end = symbols["ChsTruncateNickname"] - ROM_BASE
    width = symbols["ChsHallOfFameNicknameWidth"] - ROM_BASE
    printer = symbols["ChsHallOfFameSpeciesPrint"] - ROM_BASE
    assert rom[width:width + 2] == bytes.fromhex("70b5")
    assert bytes.fromhex("70bc02bc0847") in rom[width:printer]
    assert bytes.fromhex("2826") in rom[width:printer]
    assert struct.pack("<I", 0x08005DAD) in rom[router:end + 1024]
    for caller in (0x08174996, 0x081749D8):
        assert branch_target(base, caller) == 0x08005DAC
        assert branch_target(rom, caller) == 0x081B1814
        assert struct.pack("<I", caller + 5) in rom[router:end + 1024]
    assert struct.unpack_from("<I", rom, 0x1B1814 + 12)[0] == symbols["ChsGetMonNickname"] | 1
    offset = 0x174AC4
    assert base[offset:offset + 8] == bytes.fromhex("03a8029000200121")
    assert rom[offset:offset + 8] == struct.pack("<HHI", 0x4B00, 0x4718, symbols["ChsHallOfFameSpeciesPrint"] | 1)
    assert '"\tadd r0, sp, #0xc\\n\\t"\n        "\tstr r0, [sp, #8]\\n\\t"' in reference
    assert rom[0x173500:0x1736A0] == base[0x173500:0x1736A0]
    print("Both Hall of Fame width entries preserve LR; five-character names use 40-pixel narrow text")
    print("Species print veneer verified against the original stack-based text argument")
    print("Native Hall of Fame record initialization, including persisted nickname writes, is unchanged")


if __name__ == "__main__":
    main()
