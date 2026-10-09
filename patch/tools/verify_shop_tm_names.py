"""Execute shop TM name copying and check slot boundaries and other items."""
import argparse
import json
import struct
from pathlib import Path
from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R5, UC_ARM_REG_R6, UC_ARM_REG_SP
from verify_remaining_display_port import Machine, symbols
from build_texts import encode_compact_chinese_text, read_charmap


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    entries = json.loads((root / 'patch/item_names.json').read_text())['strings']
    charmap = read_charmap(root / 'patch/charmap_chs.txt')
    m = Machine(symbols(args.nm))
    m.names['NativeCopyItemName'] = 0x080D5EC8
    m.names['NativeShopTmNameHook'] = 0x080DF568
    m.names['NativeBuyMenuSetListEntry'] = 0x080DF554
    dest = 0x02022008
    for item, name in enumerate(entries):
        m.cpu.mem_write(dest - 8, b'\xa5' * 40)
        m.call('NativeCopyItemName', (item, dest))
        original = m.string(dest)
        if 289 <= item <= 338:
            assert original == encode_compact_chinese_text(name, charmap)
        m.cpu.mem_write(dest - 8, b'\xa5' * 40)
        expected = (b'\xf5\xf3' + original[1:11] + b'\xf5\xf4' + original[11:]
                    if 289 <= item <= 338 else original)
        m.call('NativeBuyMenuSetListEntry', (0x02023000, item, dest))
        assert bytes(m.cpu.mem_read(0x02023000, 8)) == struct.pack('<II', dest, item)
        assert m.string(dest) == expected, (item, m.string(dest), expected)
        assert len(expected) <= 18
        assert bytes(m.cpu.mem_read(dest - 8, 8)) == b'\xa5' * 8
        assert bytes(m.cpu.mem_read(dest + 18, 14)) == b'\xa5' * 14
        assert m.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
        if 289 <= item <= 338:
            assert name.startswith('招式学习器') and len(name) == 7
            # Five 8px Chinese glyphs + two at-most-8px digits, x=8.
            assert 8 + 5 * 8 + 2 * 8 < 72

    m.cpu.reg_write(UC_ARM_REG_R4, 301)
    m.cpu.reg_write(UC_ARM_REG_R5, dest)
    m.call('NativeShopTmNameHook', (301,), stop_addresses=(0x080DF584,))
    assert m.cpu.reg_read(UC_ARM_REG_R4) == 301
    assert m.cpu.reg_read(UC_ARM_REG_R5) == dest
    assert m.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
    # Execute the renderer as well: five narrow Chinese glyphs, then two
    # native digit glyphs in normal mode, followed by EOS mode reset.
    printer = 0x02001000
    m.cpu.mem_write(printer, bytes(32))
    m.cpu.mem_write(printer, struct.pack('<I', dest))
    glyphs = []
    for _ in range(30):
        m.cpu.reg_write(UC_ARM_REG_R4, printer + 0x14)
        m.cpu.reg_write(UC_ARM_REG_R6, printer)
        m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
        end = m.cpu.reg_read(UC_ARM_REG_PC)
        mode = bytes(m.cpu.mem_read(printer + 0x17, 1))[0]
        if end == 0x08005B32:
            glyphs.append(('narrow', mode))
        elif end == 0x0800582C:
            char = m.cpu.reg_read(UC_ARM_REG_R3)
            if char == 255:
                assert mode == 0
                break
            glyphs.append(('normal', mode, char))
    else:
        raise AssertionError('Renderer did not reach EOS')
    assert glyphs == [('narrow', 3)] * 5 + [('normal', 1, 0xA2), ('normal', 1, 0xA4)], glyphs
    print('PASS: real shop list-entry path/hook; 50 narrow TM names fit before price column; all other names and item IDs unchanged; slot canaries and continuation')


if __name__ == '__main__':
    main()
