"""Verify fixed Bad Egg names without changing stored Pokemon nicknames."""
import argparse

from verify_remaining_display_port import Machine, ROOT, symbols


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names.update(Box=0x0806A1B4, Mon=0x0806A058, Set=0x0806A774,
                   Party=0x081B1814, BoxNick=0x0806F4D0, Limit=0x0800885C)
    mon, dest, value = 0x02020000, 0x02021008, 0x02022000
    expected = m.string(m.names['Chs_ChecklistLiteral_gText_BadEgg'])
    assert expected == b'\xfc\x16\x64\x42\x61\xee\xff'
    assert m.word(0x0806A3C4) == m.names['Chs_ChecklistLiteral_gText_BadEgg']
    baseline = (ROOT / 'baserom_jp.gba').read_bytes()
    jp_name = baseline[0x2EA31C + 25 * 6:0x2EA31C + 26 * 6]
    for nickname in (jp_name, b'\xca\xa2\xa3\xff'):
        for bad in (False, True):
            m.cpu.mem_write(mon, bytes(100))
            stored = nickname.ljust(10, b'\xff')
            m.cpu.mem_write(mon + 8, stored)
            # Establish a valid encrypted egg first, then set the sanity flag.
            m.cpu.mem_write(value, b'\x01')
            m.call('Set', (mon, 45, value))
            m.cpu.mem_write(value, bytes((bad,)))
            m.call('Set', (mon, 4, value))
            wanted = expected if bad else nickname[:nickname.index(255) + 1]
            for route in ('Box', 'Mon', 'Party', 'BoxNick'):
                before = bytes(m.cpu.mem_read(mon, 100))
                m.cpu.mem_write(dest - 8, b'\xa5' * 40)
                args = (mon, 2, dest) if route in ('Box', 'Mon') else (mon, dest)
                result = m.call(route, args)
                assert m.string(dest) == wanted, (route, bad, m.string(dest))
                if bad and route in ('Box', 'Mon'):
                    assert result == len(expected) - 1
                assert bytes(m.cpu.mem_read(mon, 100)) == before
                assert bytes(m.cpu.mem_read(mon + 8, 10)) == stored
                assert bytes(m.cpu.mem_read(dest - 8, 8)) == b'\xa5' * 8
                assert bytes(m.cpu.mem_read(dest + 11, 21)) == b'\xa5' * 21
    for text in (b'\xff', b'\xa2\xa3\xff', b'\xca' * 10 + b'\xff',
                 expected, expected[:5] + b'\xff', expected[:5] + b'\xa1\xff'):
        m.cpu.mem_write(dest, text + b'\xa5' * 16)
        limit = 6 if text == expected else 5
        end = min(text.index(255), limit)
        assert m.call('Limit', (dest,)) == dest + end
        assert m.string(dest) == text[:end] + b'\xff'
    print('PASS: complete Chinese Bad Egg name through native party/box getters and display routes; normal nicknames unchanged; stored Pokemon bytes and output boundaries preserved')


if __name__ == '__main__':
    main()
