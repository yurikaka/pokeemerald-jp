"""Check the Hall of Fame display adapter's compiled return preservation."""

import struct
import subprocess
from pathlib import Path
from unicorn import Uc, UC_ARCH_ARM, UC_MODE_THUMB, UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2, UC_ARM_REG_R7, UC_ARM_REG_SP


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
    width = symbols["ChsHallOfFameNicknameWidth"] - ROM_BASE
    printer = symbols["ChsHallOfFameSpeciesPrint"] - ROM_BASE
    assert rom[width:width + 2] == bytes.fromhex("70b5")
    assert bytes.fromhex("70bc02bc0847") in rom[width:printer]
    assert bytes.fromhex("2826") in rom[width:printer]
    assert struct.pack("<I", 0x08005DAD) in rom[width:printer + 1024]
    assert rom[0x5DAC:0x5DBC] == struct.pack("<HHHHH", 0xB401, 0xB401, 0x4801, 0x9001, 0xBD01) + b"\x00\x00" + struct.pack("<I", symbols["ChsOriginalGetStringWidth"] | 1)
    assert rom[0x5DBC:0x5DC4] == struct.pack("<HHI", 0x4B00, 0x4718, symbols["ChsHallOfFameNicknameWidth"] | 1)
    for caller in (0x08174996, 0x081749D8):
        assert branch_target(base, caller) == 0x08005DAC
        assert branch_target(rom, caller) == 0x08005DBC
    def run_width(entry, species, nickname):
        cpu = Uc(UC_ARCH_ARM, UC_MODE_THUMB)
        for address, size in ((0x08000000, 0x2000000), (0x02000000, 0x40000), (0x03000000, 0x8000), (0x04000000, 0x1000), (0x05000000, 0x1000), (0x06000000, 0x20000)):
            cpu.mem_map(address, size)
        cpu.mem_write(0x08000000, rom)
        cpu.mem_write(0x02001000, nickname + bytes(32))
        cpu.mem_write(0x02002008, struct.pack('<H', species))
        cpu.reg_write(UC_ARM_REG_SP, 0x03007800)
        cpu.reg_write(UC_ARM_REG_LR, 0x0203F001)
        cpu.reg_write(UC_ARM_REG_R0, 1)
        cpu.reg_write(UC_ARM_REG_R1, 0x02001000)
        cpu.reg_write(UC_ARM_REG_R2, 0xFFFF)
        cpu.reg_write(UC_ARM_REG_R7, 0x02002000)
        def stop(cpu, address, size, unused):
            if address == 0x0203F000: cpu.emu_stop()
        cpu.hook_add(UC_HOOK_CODE, stop)
        cpu.emu_start(entry | 1, 0, count=1000000)
        assert cpu.reg_read(UC_ARM_REG_PC) == 0x0203F000
        assert cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
        return cpu.reg_read(UC_ARM_REG_R0), bytes(cpu.mem_read(0x02001000, 32))
    for species in range(1, 412):
        offset = 0x2EA31C + species * 6
        nickname = base[offset:offset + 6].split(b'\xff')[0] + b'\xff'
        expected = run_width(symbols['ChsHallOfFameNicknameWidth'], species, nickname)
        assert run_width(0x08005DBC, species, nickname) == expected
    for nickname in (b'\xa1\xa2\xff', b'\xff'):
        assert run_width(0x08005DBC, 25, nickname) == run_width(symbols['ChsHallOfFameNicknameWidth'], 25, nickname)
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
