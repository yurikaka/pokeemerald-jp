"""Execute ranking headers and check Dome placeholder/punctuation encoding."""
import argparse
import re
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R2, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R6, UC_ARM_REG_SP
from verify_remaining_display_port import Machine, symbols, ROOT, STOP
from build_texts import read_charmap, encode_text, convert_us_encoded_text, tokenize_line, line_width


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names.update(Ranking=0x081A45B0, Expand=0x08008BCC)
    name = 'Chs_BattleFrontier_BattleDomeLobby_Text_LastWinnerWasTough'
    data = m.string(m.names[name])
    assert b'\xfc\x15\xfd\x02\xfc\x16' in data
    assert m.word(0x082273A1) == m.names[name]
    # Saved player/NPC names stay in their original encoding inside the message.
    for value in (b'\x01\x02\x03\xff', b'\x55\x7a\x99\x79\xff', b'\xbb\xbc\xff'):
        m.cpu.mem_write(0x02021C40, value)
        m.call('Expand', (0x02023000, m.names[name]))
        expanded = m.string(0x02023000)
        assert b'\xfc\x15' + value[:-1] + b'\xfc\x16' in expanded

    # Keep native Japanese double quotes for imported and direct text.
    charmap = read_charmap(ROOT / 'patch/charmap_chs.txt')
    for char, code in (('“', 0xB1), ('”', 0xB2)):
        assert encode_text(char, charmap, False) == b'\xfc\x16' + bytes([code, 255])
        assert convert_us_encoded_text(bytes([code, 255]), set(), False) == b'\xfc\x16' + bytes([code, 255])
    assert b'\x7f\xad' in encode_text('.', charmap, False)
    assert convert_us_encoded_text(b'\xad\xff', set(), False) == b'\xfc\x16\x7f\xad\xff'
    assert convert_us_encoded_text(b'\x2d\xff', set(), False) == b'\xfc\x16\x7f\x2d\xff'
    assert b'\x7f\x2d' in encode_text('&', charmap, False)
    assert m.string(m.names['Chs_ChecklistLiteral_453_gText_MonTypeAndNo']) == encode_text('宝可梦种类和数量', charmap, False)
    quote = m.string(m.names['Chs_ChecklistLiteral_473_BattleFrontier_BattleDomeLobby_Text_ExplainTourneyTree'])
    tokens = tokenize_line(quote)
    assert sum(t == b'\xb1' for t, _ in tokens) == 1
    assert sum(t == b'\xb2' for t, _ in tokens) == 1
    # The closing quote was clipped because this checklist text skipped wrapping.
    for line in re.split(b'[\xfe\xfa\xfb\xff]', quote):
        assert line_width(line) <= 168
    first_page = quote.split(b'\xfb')[0]
    assert b'\xb2' in first_page
    assert b'\xc6\xea\x7f\xad\xa6\xa1' in m.string(m.names['Chs_ChecklistLiteral_440_gText_Lv50'])
    # A narrow period keeps Lv.50 compact, in normal and small fonts.
    for font in (0, 1):
        m.cpu.mem_write(0x02022000, b'\x7f\xad\xff')
        m.cpu.mem_write(0x02023000, bytes(32))
        m.cpu.mem_write(0x02023000, (0x02022000).to_bytes(4, 'little'))
        m.cpu.mem_write(0x02023004, bytes([font]))
        m.cpu.mem_write(0x02023017, b'\x01')
        for _ in range(5):
            m.cpu.reg_write(UC_ARM_REG_R4, 0x02023014)
            m.cpu.reg_write(UC_ARM_REG_R6, 0x02023000)
            m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
            if m.cpu.reg_read(UC_ARM_REG_PC) == 0x08005B32:
                assert m.cpu.mem_read(0x030030B0, 1)[0] == 4
                break
        else:
            raise AssertionError('Period did not render')

    captured = []
    def capture(cpu, address, size, unused):
        if address == 0x0800449C:
            captured.append((cpu.reg_read(UC_ARM_REG_R2), cpu.reg_read(UC_ARM_REG_R3), m.word(cpu.reg_read(UC_ARM_REG_SP))))
            cpu.reg_write(UC_ARM_REG_PC, STOP if len(captured) == 2 else cpu.reg_read(UC_ARM_REG_LR))
    m.cpu.hook_add(UC_HOOK_CODE, capture)
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    assert rom[0x1A45B0:0x1A46B4] == base[0x1A45B0:0x1A46B4]
    # All ten Ranking Hall facilities use the same two level-label pointers.
    for facility in range(10):
        for level, label in enumerate(('Chs_ChecklistLiteral_gText_RecordsLv50', 'Chs_ChecklistLiteral_gText_RecordsOpenLevel')):
            captured.clear()
            m.call('Ranking', (facility, level))
            assert captured[1] == (m.names[label], 132, 2), (facility, level, captured)
            assert m.word(0x085DD504 + level * 4) == m.names[label]
    print('PASS: Dome name placeholders, native quotes and wrapped dialogue, compact Lv.50 period and Latin ampersand; headers for all 10 Ranking Hall facilities and both level modes')


if __name__ == '__main__':
    main()
