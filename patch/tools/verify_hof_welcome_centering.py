"""Measure the welcome glyphs and execute the native Hall of Fame centering."""
import argparse
import struct

from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_R2, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R6
from verify_remaining_display_port import Machine, symbols


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    pointer = m.names['Chs_ChecklistLiteral_440_gText_WelcomeToHOF']
    assert m.word(0x08174874) == pointer
    data = m.string(pointer)
    assert data.startswith(b'\xfc\x16')
    m.cpu.mem_write(0x02022000, data[2:])
    m.cpu.mem_write(0x02023000, bytes(32))
    m.cpu.mem_write(0x02023000, struct.pack('<I', 0x02022000))
    m.cpu.mem_write(0x02023014, b'\x01')
    m.cpu.mem_write(0x02023017, b'\x01')
    width = 0
    for _ in range(30):
        m.cpu.reg_write(UC_ARM_REG_R4, 0x02023014)
        m.cpu.reg_write(UC_ARM_REG_R6, 0x02023000)
        m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
        pc = m.cpu.reg_read(UC_ARM_REG_PC)
        if pc == 0x08005B32:
            width += m.cpu.mem_read(0x030030B0, 1)[0]
        elif pc == 0x0800582C:
            assert m.cpu.reg_read(UC_ARM_REG_R3) == 255
            break
    else:
        raise AssertionError('welcome text has no EOS')
    assert width == 96

    # Wokann menu.c: the standard dialogue window starts at tile 4, width 22.
    template = bytes(m.cpu.mem_read(m.word(0x08196DDC), 8))
    assert template[1] == 4 and template[3] == 22
    m.names['WelcomeCenter'] = 0x08174838
    m.cpu.reg_write(UC_ARM_REG_R4, template[3])
    m.call('WelcomeCenter', stop_addresses=(0x08199AFC,))
    x = m.cpu.reg_read(UC_ARM_REG_R2)
    assert x == (template[3] * 8 - width) // 2 == 40
    screen_x = template[1] * 8 + x
    assert screen_x == 240 - screen_x - width == 72
    print('PASS: actual welcome width 96px; native print x=40; equal 72px screen margins')

if __name__ == '__main__':
    main()
