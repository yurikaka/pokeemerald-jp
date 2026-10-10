"""Check PC item names against the native three-digit quantity column."""
import argparse
import json
import struct

from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_R2, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R6, UC_ARM_REG_SP
from verify_remaining_display_port import Machine, symbols, ROOT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    template = bytes(m.cpu.mem_read(0x085C0C28, 24))
    assert template[18] == 8 and template[22:] == b'\x00\x01'
    font = template[23] & 63
    padding = (template[22] >> 3) & 7
    font_height = m.cpu.mem_read(0x0829CEA4 + font * 12 + 5, 1)[0]
    assert font_height + padding == 16
    window = bytes(m.cpu.mem_read(0x085C0C40, 8))
    assert window == bytes.fromhex('000f010e120f5100')
    m.names.update(Copy=0x0816BC08, NativeCopy=0x080D5EC8, Width=0x08005DAC, Quantity=0x0816BC84)
    items = json.loads((ROOT / 'patch/item_names.json').read_text())['strings']
    widest = 0
    checked = 0
    for item in range(1, len(items)):
        m.call('NativeCopy', (item, 0x02027000))
        original = m.string(0x02027000)
        m.cpu.mem_write(0x02022000, b'\xee' * 32)
        m.call('Copy', (0x02022000, item))
        name = m.string(0x02022000)
        assert len(name) <= 24
        assert bytes(m.cpu.mem_read(0x02022018, 8)) == b'\xee' * 8
        assert name.replace(b'\xf5\xf3', b'').replace(b'\xf5\xf4', b'') == original
        m.cpu.mem_write(0x02023000, bytes(32))
        m.cpu.mem_write(0x02023000, struct.pack('<I', 0x02022000))
        m.cpu.mem_write(0x02023014, bytes([font]))
        width = 0
        for _ in range(40):
            char_start = m.word(0x02023000)
            first = m.cpu.mem_read(char_start, 1)[0]
            m.cpu.reg_write(UC_ARM_REG_R4, 0x02023014)
            m.cpu.reg_write(UC_ARM_REG_R6, 0x02023000)
            m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
            pc = m.cpu.reg_read(UC_ARM_REG_PC)
            if pc == 0x08005B32:
                advance, height = m.cpu.mem_read(0x030030B0, 2)
                if first == 0xCA or 0xA1 <= first <= 0xAA:
                    assert advance < 8 and height == 13
                else:
                    assert advance == 12 and height == 15
                width += advance
            elif pc == 0x0800582C:
                char = m.cpu.reg_read(UC_ARM_REG_R3)
                if char == 255:
                    break
                m.cpu.mem_write(0x02025000, b'\xfc\x16' + bytes([char, 255]))
                width += m.call('Width', (font, 0x02025000, 0))
        else:
            raise AssertionError((item, 'no EOS'))
        # Key items occupy the other ranges and cannot normally be deposited.
        if item <= 258 or 289 <= item <= 346:
            assert 8 + width <= 80, (item, items[item], width)
            widest = max(widest, width)
            checked += 1

    m.cpu.mem_write(0x0203B990, struct.pack('<I', 0x02026000))
    m.cpu.mem_write(0x02026666, b'\xff')
    m.cpu.mem_write(0x03005AEC, struct.pack('<I', 0x02028000))
    for count in (1, 99, 999):
        m.cpu.mem_write(0x0202849A, struct.pack('<H', count))
        m.call('Quantity', (0, 0, 10), stop_addresses=(0x0800449C,))
        pointer = m.cpu.reg_read(UC_ARM_REG_R2)
        x = m.cpu.reg_read(UC_ARM_REG_R3)
        assert x == 80 and m.word(m.cpu.reg_read(UC_ARM_REG_SP)) == 10
        quantity = m.string(pointer)
        digits = bytes(0xA1 + int(digit) for digit in str(count))
        original = b'\xb9' + b'\x00' * (3 - len(digits)) + digits + b'\xff'
        assert quantity == original
        assert x + m.call('Width', (1, pointer, 0)) <= window[3] * 8
    print(f'PASS: {checked} non-key item names fit before x=80 (max {widest}px); only name P/digits use narrow glyphs; quantity text remains standard; all 376 names preserve text and fit 24-byte slots; quantities through 999 fit; original windows and row spacing preserved')


if __name__ == '__main__':
    main()
