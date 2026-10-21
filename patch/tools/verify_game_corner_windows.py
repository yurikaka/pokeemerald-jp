"""Execute prize/purchase layout and check text, frame and tile separation.

This is a structural/Unicorn regression, not an in-game screenshot test.
Native logic/layout cross-reference: Wokann dev script_menu.c, coins.c,
menu.c and data/maps/MauvilleCity_GameCorner/scripts.inc.
"""
import argparse
import struct

from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC
from unicorn.arm_const import UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2, UC_ARM_REG_R3
from unicorn.arm_const import UC_ARM_REG_SP
from verify_remaining_display_port import Machine, ROOT, symbols


def render_right(names, text, width, height, x=8):
    # Execute actual native printing and installed CHS glyph generation.
    # In particular, Latin digits/spaces are not all 8 pixels wide.
    m = Machine(names)
    m.names['DefaultFonts'] = 0x080061A4
    m.names['Print'] = 0x0800449C
    m.call('DefaultFonts')
    size = width * height * 32
    m.cpu.mem_write(0x02020004, bytes((0, 0, 0, width, height, 0, 0, 0))
                    + struct.pack('<I', 0x02028000))
    m.cpu.mem_write(0x02028000, bytes(size) + b'\xa5' * 64)
    m.cpu.mem_write(0x02024000, text)
    extents = []

    def capture(cpu, address, instruction_size, unused):
        if address == 0x08003528:  # no VRAM DMA in Unicorn
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))
        elif address == 0x08004850:  # real CopyGlyphToWindow
            printer = cpu.reg_read(UC_ARM_REG_R0)
            x = bytes(cpu.mem_read(printer + 8, 1))[0]
            glyph_width = bytes(cpu.mem_read(0x030030B0, 1))[0]
            extents.append(x + glyph_width)

    m.cpu.hook_add(UC_HOOK_CODE, capture)
    m.cpu.mem_write(0x03007800, struct.pack('<III', 2, 0, 0))
    m.call('Print', (0, 1, 0x02024000, x))
    assert extents
    assert bytes(m.cpu.mem_read(0x02028000 + size, 64)) == b'\xa5' * 64
    assert max(extents) <= width * 8, (text.hex(), extents, width)
    return max(extents)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    names = symbols(args.nm)
    m = Machine(names)
    m.names['NativeDrawMultichoiceMenu'] = 0x080E13FC
    captured = []

    def capture(cpu, address, size, unused):
        if address == 0x080E1F10:
            captured.append(tuple(cpu.reg_read(r) for r in
                                  (UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2, UC_ARM_REG_R3)))
            cpu.reg_write(UC_ARM_REG_R0, 7)
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

    m.cpu.hook_add(UC_HOOK_CODE, capture)
    for menu, left, width, rows in ((48, 12, 17, 4), (55, 12, 17, 6), (49, 15, 15, 3)):
        m.call('NativeDrawMultichoiceMenu', (left, 0, menu, 0),
               stop_addresses=(0x080E1460,))
        actual = captured[-1]
        assert actual == ((13, 0, width, rows * 2) if menu == 49
                          else (11, 0, width, rows * 2)), actual
        # Removal clears menu interior and frame only. No overlap means it
        # cannot erase the native coin box (frame columns 0..9).
        assert actual[0] > 9
        if menu == 49:
            assert actual[0] > 12  # 11-tile money frame spans columns 0..12
            assert actual[1] == 0  # original top alignment
        assert actual[0] + 1 + width <= 29
        # CreateWindowFromRect uses baseBlock 0x5c. Its tiles must not
        # overwrite the original coin window's 16 tiles at 0x136.
        assert 0x5C + width * rows * 2 <= 0x136
        actions = m.word(0x08564218 + menu * 8)
        extents = [render_right(names, m.string(m.word(actions + i * 8)), width, rows * 2)
                   for i in range(rows)]
        assert max(extents) <= width * 8, (menu, extents)
        print(f'menu {menu}: rect {actual}, text right edges {extents}, coin frame and VRAM separate')

    coin_text = m.string(m.word(0x08145C64))
    m.names['ConvertNumber'] = 0x080089D8
    for balance in (0, 9, 50, 500, 6789, 9999):
        m.call('ConvertNumber', (0x02024000, balance, 1, 4))
        digits = m.string(0x02024000)
        assert len(digits) == 5
        assert digits[:-1] == b'\x00' * (4 - len(str(balance))) + bytes(0xA1 + int(c) for c in str(balance))
        render_right(names, coin_text.replace(b'\xfd\x02', digits[:-1]), 8, 2)
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    assert rom[0x145C6C:0x145CF0] == base[0x145C6C:0x145CF0]
    assert rom[0x145C20:0x145C64] == base[0x145C20:0x145C64]
    print('PASS: text fits, four-digit right alignment and native coin window sizing/inset/allocation/removal preserved')

    m.names['NativeDrawMoneyBox'] = 0x080E4AC8
    m.names['NativeMoneyAmount'] = 0x080E49E8
    m.call('NativeDrawMoneyBox', (999999, 0, 0), stop_addresses=(0x08198B34,))
    stack = m.cpu.reg_read(UC_ARM_REG_SP)
    assert tuple(m.word(stack + i * 4) for i in range(4)) == (11, 2, 15, 8)
    assert m.cpu.reg_read(UC_ARM_REG_R2) == 1  # native window x
    assert m.cpu.reg_read(UC_ARM_REG_R3) == 1  # native window y
    m.call('NativeMoneyAmount', (0, 999999, 0), stop_addresses=(0x080E4A08,))
    assert m.cpu.reg_read(UC_ARM_REG_R1) == 32
    # Label sprite is 32px wide, centered at screen x=19 (right edge 35).
    # Window begins at x=8; amount begins at 8+32=40, leaving a 5px gap.
    assert 8 + 32 > 19 + 16
    money_text = m.string(m.word(0x080E4A70))
    for balance in (0, 9, 1000, 10000, 999999):
        m.call('ConvertNumber', (0x02024000, balance, 1, 6))
        digits = m.string(0x02024000)
        assert len(digits) == 7
        render_right(names, money_text.replace(b'\xfd\x02', digits[:-1]), 11, 2, x=32)
    print('PASS: native money window width=11, amount x=32; maximum six-digit amount fits, label and top-aligned menu stay separate')


if __name__ == '__main__':
    main()
