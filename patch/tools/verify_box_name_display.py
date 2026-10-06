#!/usr/bin/env python3
"""Execute JP default initialization and BOX display/read-write boundaries.

Unicorn binary wheel required. Non-name reset helpers are stubbed. Native
StringCopy, decimal conversion, hook veneers and display copying execute.
"""
import argparse
import struct
from pathlib import Path
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_SP
from unicorn.arm_const import UC_ARM_REG_R0
from verify_remaining_display_port import Machine, symbols

ROOT = Path(__file__).resolve().parents[2]
STORAGE = 0x02000000
BOXES = STORAGE + 0x8344
DISPLAY_CALLERS = (0x08056309, 0x08056355, 0x08056381, 0x0809ABC7,
                   0x080C74C7, 0x080CC4A9, 0x080CC4DF, 0x080CC63F,
                   0x080CC68B, 0x080E2A99, 0x080E2AD9, 0x080E2AFF,
                   0x081CD051, 0x081D2567)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    names = symbols(args.nm)
    names.update(NativeReset=0x080C7008, NativeCopyPadded=0x08008E14)
    m = Machine(names)
    cpu = m.cpu
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    assert rom[0xC707C:0xC7080] == base[0xC707C:0xC7080] == struct.pack('<I', 0x085CB584)
    assert rom[0x5CB584:0x5CB589] == base[0x5CB584:0x5CB589]
    cpu.mem_write(0x03005AF4, struct.pack('<I', STORAGE))
    cpu.mem_write(STORAGE, b'\xa5' * 0x83E0)

    def stub(cpu, address, size, unused):
        if address in (0x080D15B8, 0x080D18B8, 0x080D19C0, 0x080D1CCC):
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))
    cpu.hook_add(UC_HOOK_CODE, stub)
    m.call('NativeReset')
    defaults = [base[0x5CB584:0x5CB588] + bytes(0xA1 + int(c) for c in str(i + 1)) + b'\xff'
                for i in range(14)]
    for i, expected in enumerate(defaults):
        assert m.string(BOXES + i * 9) == expected, (i, m.string(BOXES + i * 9), expected)

    def get(box, caller):
        before = bytes(cpu.mem_read(STORAGE, 0x83E0))
        m.stop_addresses = {caller & ~1}
        cpu.reg_write(UC_ARM_REG_SP, 0x03007800)
        cpu.reg_write(UC_ARM_REG_LR, caller)
        cpu.reg_write(UC_ARM_REG_R0, box)
        cpu.emu_start(0x080D1971, 0, count=10000)
        assert cpu.reg_read(UC_ARM_REG_PC) == caller & ~1
        assert bytes(cpu.mem_read(STORAGE, 0x83E0)) == before, 'display changed storage'
        return cpu.reg_read(UC_ARM_REG_R0)

    for i in range(14):
        expected = b'\xfc\x16\xbc\xc9\xd2\x00' + bytes(0xA1 + int(c) for c in str(i + 1)) + b'\xff'
        for caller in DISPLAY_CALLERS:
            pointer = get(i, caller)
            display = expected[2:] if caller in (0x080CC4DF, 0x080CC68B) else expected
            assert m.string(pointer) == display
            assert pointer >= 0x09000000, 'default display string should reside in ROM'
            dest = 0x02022000
            cpu.mem_write(dest, b'\xa5' * 16)
            m.call('NativeCopyPadded', (dest, pointer, 0, 8))
            assert m.string(dest) == display[:-1].ljust(8, b'\x00') + b'\xff'
            assert bytes(cpu.mem_read(dest + 9, 7)) == b'\xa5' * 7
        for caller in (0x080C703F, 0x080C97A1, 0x0203F001):
            assert get(i, caller) == BOXES + i * 9
        # Exact per-box comparison: custom names, partial defaults and a
        # different box's default name must not be translated.
        for custom in (b'\x01\x02\x03\xff', defaults[(i + 1) % 14],
                       defaults[i][:-1] + b'\x01\xff',
                       b'\xbc\xc9\xd2\x00\xa2\xff'):
            assert len(custom) <= 9
            cpu.mem_write(BOXES + i * 9, custom)
            for caller in DISPLAY_CALLERS:
                assert get(i, caller) == BOXES + i * 9
        cpu.mem_write(BOXES + i * 9, defaults[i])
    for invalid in (14, 255):
        for caller in DISPLAY_CALLERS + (0x080C703F, 0x080C97A1, 0x0203F001):
            assert get(invalid, caller) == 0
    assert get(256, DISPLAY_CALLERS[0]) == get(0, DISPLAY_CALLERS[0]), 'original u8 argument behavior'
    print('PASS: native initialization writes 14 JP defaults; 14 display callers use BOX 1–14; '
          'custom names/read-write pointers preserved; invalid IDs; storage and 9-byte buffer canaries')


if __name__ == '__main__':
    main()
