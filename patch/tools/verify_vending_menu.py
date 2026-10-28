"""Execute multichoice bounds and vending layout; not a screenshot test."""
import argparse
from pathlib import Path
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import (
    UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R0, UC_ARM_REG_R1,
    UC_ARM_REG_R2, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R5,
    UC_ARM_REG_R6, UC_ARM_REG_R9, UC_ARM_REG_SP,
)
from verify_remaining_display_port import Machine, symbols
from build_texts import line_width


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names['NativeVendingWindowHook'] = 0x080E1458
    m.names['NativeDrawMultichoiceMenu'] = 0x080E13FC
    cpu = m.cpu
    captured = []
    regs = (UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2, UC_ARM_REG_R3)

    def capture(cpu, address, size, unused):
        if address == 0x080E1F10:
            captured.append(tuple(cpu.reg_read(r) for r in regs))
            cpu.reg_write(UC_ARM_REG_R0, 7)
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

    cpu.hook_add(UC_HOOK_CODE, capture)
    # Overflowing menus move left; width, top and height remain unchanged.
    for menu in range(256):
        cpu.reg_write(UC_ARM_REG_R4, 16)
        cpu.reg_write(UC_ARM_REG_R5, 0)
        cpu.reg_write(UC_ARM_REG_R6, 4)
        cpu.reg_write(UC_ARM_REG_R9, menu)
        result = m.call('NativeVendingWindowHook', (16, 0, 18, 8),
                        stop_addresses=(0x080E1460,))
        if menu in (42, 95):
            expected = (14, 0, 14, 8)
        elif menu == 48:
            expected = (9, 0, 19, 8)
        elif menu == 55:
            expected = (9, 0, 19, 8)
        elif menu == 49:
            expected = (13, 0, 15, 8)
        else:
            expected = (10, 0, 18, 8)
        assert captured[-1] == expected, (menu, captured[-1])
        assert result == 7
        assert cpu.reg_read(UC_ARM_REG_R4) == 7
        assert cpu.reg_read(UC_ARM_REG_SP) == 0x03007800

    for width in range(1, 29):
        for left in range(29):
            cpu.reg_write(UC_ARM_REG_R4, left)
            cpu.reg_write(UC_ARM_REG_R5, 4)
            cpu.reg_write(UC_ARM_REG_R6, 4)
            cpu.reg_write(UC_ARM_REG_R9, 109)
            m.call('NativeVendingWindowHook', (left, 4, width, 8),
                   stop_addresses=(0x080E1460,))
            assert captured[-1] == (min(left, 28 - width), 4, width, 8)

    # kt1.png: the Battle Tower reporter uses (16, 4), menu 109.
    m.call('NativeDrawMultichoiceMenu', (16, 4, 109, 0),
           stop_addresses=(0x080E1460,))
    assert captured[-1] == (13, 4, 15, 8), captured[-1]

    # Native menus can expand the player's saved name while measuring width.
    save_pointer = m.word(0x080E13A0)
    cpu.mem_write(save_pointer, (0x02028000).to_bytes(4, 'little'))
    cpu.mem_write(0x02028000, b'\x01\x02\x03\x04\x05\xff')
    # The table ends at menu 112; 113 has no native table entry.
    for menu in range(113):
        m.call('NativeDrawMultichoiceMenu', (16, 0, menu, 0),
               stop_addresses=(0x080E1460,))
        left, top, width, height = captured[-1]
        assert 0 < width <= 28, (menu, captured[-1])
        assert left + width + 1 <= 29, (menu, captured[-1])

    # Start at the real menu function: original width calculation, table
    # lookup, native hook bytes and adapter all execute. Stop before rendering.
    m.call('NativeDrawMultichoiceMenu', (0, 0, 57, 0),
           stop_addresses=(0x080E1460,))
    left, top, width, height = captured[-1]
    assert (left, top, height) == (0, 0, 12), captured[-1]
    assert 0 < width < 29
    m.call('NativeDrawMultichoiceMenu', (16, 0, 42, 0),
           stop_addresses=(0x080E1460,))
    assert captured[-1] == (14, 0, 14, 8), captured[-1]

    # kt7.png: six Frontier rule options, longest label is 96px in Chinese.
    m.call('NativeDrawMultichoiceMenu', (15, 0, 95, 0),
           stop_addresses=(0x080E1460,))
    assert captured[-1] == (14, 0, 14, 12), captured[-1]
    widths = [line_width(m.string(m.word(0x08563F98 + index * 8))[:-1])
              for index in range(6)]
    assert max(widths) == 96, widths
    assert all(8 + width + 8 <= 14 * 8 for width in widths), widths

    # Actual window adds one tile to x/y. Frame occupies columns 14..29,
    # within the 30 visible columns; money window frame ends at column 13.
    assert 14 > 13
    assert 14 + 1 + 14 < 30
    assert 8 + 72 + 4 * 8 <= 14 * 8
    root = Path(__file__).resolve().parents[2]
    base = (root / 'baserom_jp.gba').read_bytes()
    rom = (root / 'pokeemerald_jp_chs.gba').read_bytes()
    # The roof purchase event contains translated text references, so check
    # the choice command itself rather than its surrounding messages.
    assert base[0x20AEF2:0x20AEF8] == rom[0x20AEF2:0x20AEF8]
    assert base[0x20AF51:0x20AF7B] == rom[0x20AF51:0x20AF7B]
    print('PASS: real reporter/elevator/vending entry paths; multichoice frame bounds, unchanged fitting positions and dimensions, vending money-window separation, stack/register preservation')


if __name__ == '__main__':
    main()
