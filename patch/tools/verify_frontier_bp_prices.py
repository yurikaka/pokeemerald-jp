"""Check all BP shop/tutor prices against their native window dimensions."""
import argparse
import json
import re
import struct
from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R6
from verify_remaining_display_port import Machine, symbols, ROOT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names.update(Init=0x0813A164, Width=0x08005DAC, Shift=0x08005A3C)
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    assert rom[0x13A164:0x13A318] == base[0x13A164:0x13A318]
    definitions = json.loads((ROOT / 'patch/batches/438_checklist_controls_and_gambler.json').read_text())
    prices = {t['name']: t for t in definitions['texts']
              if re.fullmatch(r'gText_.+\d+BP', t.get('source_symbol', ''))}
    counts = {3: 10, 4: 5, 5: 6, 6: 9, 9: 10, 10: 10}
    checked = set()
    for menu, count in counts.items():
        m.cpu.mem_write(0x03005B60, bytes(16 * 40))
        m.cpu.mem_write(0x02037280, struct.pack('<H', menu))
        m.call('Init', stop_addresses=(0x0813A30E,))
        left, top, tiles, height = struct.unpack('<4H', m.cpu.mem_read(0x03005B6C, 8))
        assert (left, top, tiles, height) == ((15, 1, 14, 12) if menu >= 9 else (14, 1, 15, 12))
        # Native list template starts names at x=8; native table stride is 64.
        for row in range(count):
            pointer = m.word(0x0859274C + menu * 64 + row * 4)
            name = next(n for n in prices if m.names[n] == pointer)
            data = m.string(pointer)
            shift = data.index(b'\xfc\x0d')
            target = data[shift + 2]
            suffix = data[shift + 3:]
            m.cpu.mem_write(0x02022000, b'\xfc\x16' + suffix)
            price_width = m.call('Width', (1, 0x02022000, 0))
            assert 8 + target + price_width == tiles * 8, name
            # Execute the native SHIFT_TEXT opcode, including the x=8 origin.
            m.cpu.mem_write(0x02023000, bytes(32))
            m.cpu.mem_write(0x02023000, struct.pack('<I', pointer + shift + 2))
            m.cpu.mem_write(0x02023007, b'\x08')
            m.cpu.reg_write(UC_ARM_REG_R6, 0x02023000)
            m.call('Shift', stop_addresses=(0x080059B2,))
            assert m.cpu.mem_read(0x02023009, 1)[0] == 8 + target
            # Render the name's individual Chinese/Latin glyphs to measure
            # actual advances; GetStringWidth counts Chinese byte pairs twice.
            assert data.startswith(b'\xfc\x16')
            m.cpu.mem_write(0x02022000, data[2:shift] + b'\xff')
            m.cpu.mem_write(0x02023000, bytes(32))
            m.cpu.mem_write(0x02023000, struct.pack('<I', 0x02022000))
            m.cpu.mem_write(0x02023004, b'\x01')
            m.cpu.mem_write(0x02023017, b'\x01')
            width = 0
            for _ in range(40):
                m.cpu.reg_write(UC_ARM_REG_R4, 0x02023014)
                m.cpu.reg_write(UC_ARM_REG_R6, 0x02023000)
                m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
                pc = m.cpu.reg_read(UC_ARM_REG_PC)
                if pc == 0x08005B32:
                    width += m.cpu.mem_read(0x030030B0, 1)[0]
                elif pc == 0x0800582C:
                    char = m.cpu.reg_read(UC_ARM_REG_R3)
                    if char == 255:
                        break
                    # Single-byte Latin letters use the native renderer.
                    m.cpu.mem_write(0x02025000, b'\xfc\x16' + bytes([char, 255]))
                    width += m.call('Width', (1, 0x02025000, 0))
            else:
                raise AssertionError(name + ': no EOS')
            assert 0 < width <= target, (name, width, target)
            checked.add(name)
    assert checked == set(prices) and len(checked) == 50
    print('PASS: all 50 BP prices in 6 native menus; complete prices, aligned right edges, no name overlap, native SHIFT_TEXT origin')

    # Keep the description tiles after the 14x12 tutor list (base 0x5c).
    template = bytes(m.cpu.mem_read(0x08592C7C, 8))
    assert template == bytes.fromhex('0001070c060f0401')
    description_base = struct.unpack_from('<H', template, 6)[0]
    assert description_base == 0x5c + 14 * 12
    assert description_base + template[3] * template[4] <= 0x1a8
    assert rom[0x13AD8A:0x13AD8C] == bytes.fromhex('6021')
    assert rom[0x13AD6C:0x13AD8A] == base[0x13AD6C:0x13AD8A]
    assert rom[0x13AD8C:0x13AE18] == base[0x13AD8C:0x13AE18]
    descriptions = json.loads((ROOT / 'patch/batches/224_battle_frontier_lounge7.json').read_text())
    descriptions = [t for t in descriptions['texts'] if t['name'].endswith('Desc')]
    assert len(descriptions) == 20
    widest = 0
    for entry in descriptions:
        pointer = m.names[entry['name']]
        data = m.string(pointer)
        assert data.startswith(b'\xfc\x16') and b'\xf5\xf3' not in data, entry['name']
        m.cpu.mem_write(0x02023000, bytes(32))
        m.cpu.mem_write(0x02023000, struct.pack('<I', pointer + 2))
        m.cpu.mem_write(0x02023014, b'\x01')
        m.cpu.mem_write(0x02023017, b'\x01')
        widths = [0]
        for _ in range(100):
            m.cpu.reg_write(UC_ARM_REG_R4, 0x02023014)
            m.cpu.reg_write(UC_ARM_REG_R6, 0x02023000)
            m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
            pc = m.cpu.reg_read(UC_ARM_REG_PC)
            if pc == 0x08005B32:
                widths[-1] += m.cpu.mem_read(0x030030B0, 1)[0]
                assert m.cpu.mem_read(0x030030B1, 1)[0] == 15
            elif pc == 0x0800582C:
                char = m.cpu.reg_read(UC_ARM_REG_R3)
                if char == 255:
                    break
                if char == 254:
                    widths.append(0)
                else:
                    m.cpu.mem_write(0x02025000, b'\xfc\x16' + bytes([char, 255]))
                    widths[-1] += m.call('Width', (1, 0x02025000, 0))
        else:
            raise AssertionError(entry['name'] + ': no EOS')
        limit = 96 if entry['name'].endswith('DreamEaterDesc') else 92
        assert max(widths) <= limit and len(widths) <= 3, (entry['name'], widths)
        if limit == 96:
            assert widths == [84, 84, 96]
        widest = max(widest, max(widths))
    print(f'PASS: standard-font tutor descriptions use at most 3 lines; Dream Eater intentionally uses 96px for its final period (max {widest}px); other descriptions stay within 92px; no tile overlap')


if __name__ == '__main__':
    main()
