"""Measure HOF hint glyphs and execute native header right alignment."""
import argparse
import struct

from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R0, UC_ARM_REG_R2, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R5, UC_ARM_REG_R6, UC_ARM_REG_R8
from verify_remaining_display_port import Machine, symbols


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names.update(Align=0x0819836E, IconWidth=0x08006184, NativeGlyphWidth=0x08006350)
    measured = {}
    for suffix, expected in (('PickCancel', 72), ('PickNextCancel', 100)):
        pointer = m.names['Chs_ChecklistLiteral_480_gText_' + suffix]
        data = m.string(pointer)
        assert data[:2] == b'\xfc\x16'
        m.cpu.mem_write(0x02022000, data[2:])
        pos = 0
        width = 0
        while data[2 + pos] != 255:
            char = data[2 + pos]
            if char == 0xF8:
                width += m.call('IconWidth', (data[3 + pos],))
                pos += 2
            elif char == 0:
                width += m.call('NativeGlyphWidth', (char,))
                pos += 1
            else:
                m.cpu.mem_write(0x02023000, bytes(32))
                m.cpu.mem_write(0x02023000, struct.pack('<I', 0x02022000 + pos))
                m.cpu.mem_write(0x02023017, b'\x01')
                m.cpu.reg_write(UC_ARM_REG_R4, 0x02023014)
                m.cpu.reg_write(UC_ARM_REG_R6, 0x02023000)
                m.call('ChineseRenderHook', (0,), (0x08005B32,))
                advance, height = m.cpu.mem_read(0x030030B0, 2)
                assert advance == 10 and height == 13
                width += advance
                pos += 2
        assert width == expected
        measured[pointer] = width
    assert m.word(0x081743A0) in measured and m.word(0x081743D4) in measured

    # Stub only the window attribute getter; execute the actual hook and
    # original x-coordinate arithmetic through its native print call.
    left = 0
    def window_attribute(cpu, address, size, unused):
        if address == 0x0800401C:
            cpu.reg_write(UC_ARM_REG_R0, left)
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))
    m.cpu.hook_add(UC_HOOK_CODE, window_attribute)
    m.cpu.mem_write(0x0203CA6C, b'\x00')
    for left in (0, 1, 2):
        for pointer, width in measured.items():
            m.cpu.reg_write(UC_ARM_REG_R6, pointer)
            m.cpu.reg_write(UC_ARM_REG_R5, 99)
            m.cpu.reg_write(UC_ARM_REG_R8, 0)
            m.call('Align', stop_addresses=(0x08199AFC,))
            x = m.cpu.reg_read(UC_ARM_REG_R2)
            assert left * 8 + x + width == 236
            assert m.cpu.reg_read(UC_ARM_REG_R3) == 1
        m.cpu.reg_write(UC_ARM_REG_R6, 0x02024000)
        m.cpu.reg_write(UC_ARM_REG_R5, 7)
        m.cpu.reg_write(UC_ARM_REG_R8, 0)
        m.call('Align', stop_addresses=(0x08199AFC,))
        assert left * 8 + m.cpu.reg_read(UC_ARM_REG_R2) + 7 * 8 == 236
    print('PASS: actual font-0 hint widths are 72/100px; both HOF record paths align to screen x=236; other header strings retain original alignment')


if __name__ == '__main__':
    main()
