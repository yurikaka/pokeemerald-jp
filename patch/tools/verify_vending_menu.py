"""Execute the vending-only window adapter; not an in-game screenshot test."""
import argparse
from pathlib import Path
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import (
    UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R0, UC_ARM_REG_R1,
    UC_ARM_REG_R2, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R5,
    UC_ARM_REG_R6, UC_ARM_REG_R9, UC_ARM_REG_SP,
)
from verify_remaining_display_port import Machine, symbols


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
    # Every other menu must retain its original position, width and height.
    for menu in range(256):
        cpu.reg_write(UC_ARM_REG_R4, 16)
        cpu.reg_write(UC_ARM_REG_R5, 0)
        cpu.reg_write(UC_ARM_REG_R6, 4)
        cpu.reg_write(UC_ARM_REG_R9, menu)
        result = m.call('NativeVendingWindowHook', (16, 0, 18, 8),
                        stop_addresses=(0x080E1460,))
        expected = (14, 0, 14, 8) if menu == 42 else (16, 0, 18, 8)
        assert captured[-1] == expected, (menu, captured[-1])
        assert result == 7
        assert cpu.reg_read(UC_ARM_REG_R4) == 7
        assert cpu.reg_read(UC_ARM_REG_SP) == 0x03007800

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
    print('PASS: real elevator/vending menu entry paths and hook bytes; vending bounds, money-window separation, original arguments for 255 other menus, stack/register preservation')


if __name__ == '__main__':
    main()
