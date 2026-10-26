"""Check kana-colliding symbols against actual Latin-font rendering."""
import argparse
import struct

from PIL import Image
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_LR

from build_texts import convert_us_encoded_text, encode_text, read_charmap
from verify_remaining_display_port import Machine, ROOT


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    charmap = read_charmap(ROOT / 'patch/charmap_chs.txt')
    assert encode_text('+', charmap, False) == b'\xfc\x16\x7f\x2e\xff'
    assert convert_us_encoded_text(b'\x2e\xff', set(), False) == b'\xfc\x16\x7f\x2e\xff'
    assert convert_us_encoded_text(b'\x2e\xff', set(), False, True) == b'\xfc\x15\x2e\xff'

    m = Machine({'Fonts': 0x080061A4, 'Print': 0x0800449C,
                 'Results': 0x08137DCC})
    cpu = m.cpu
    framebuffer, text = 0x02028000, 0x02024000
    cpu.mem_write(0x02020004, bytes((0, 0, 0, 12, 2, 0, 0, 0))
                  + struct.pack('<I', framebuffer))

    def intercept(cpu, address, size, unused):
        if address == 0x080035A8:  # Skip VRAM copy, retain native rendering.
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

    cpu.hook_add(UC_HOOK_CODE, intercept)
    m.call('Fonts')

    def render(data, font):
        cpu.mem_write(framebuffer, b'\x11' * 768)
        cpu.mem_write(text, data)
        m.call('Print', (0, font, text, 0))
        return bytes(cpu.mem_read(framebuffer, 768))

    glyphs = '&+=;¿¡%()<>~・-'
    for char in glyphs:
        code = charmap[char]
        expected = b'\xfc\x16\x7f' + code + b'\xff'
        assert encode_text(char, charmap, False) == expected
        assert convert_us_encoded_text(code + b'\xff', set(), False) == expected
    for char in '&+=¿¡%()<>-':
        code = charmap[char]
        assert convert_us_encoded_text(code + b'\xff', set(), False, True) == b'\xfc\x15' + code + b'\xff'

    for font, asset in ((0, 'latin_small.png'), (1, 'latin_normal.png')):
        plus = render(encode_text('+', charmap, False), font)
        old = render(b'\xfc\x16\x2e\xff', font)
        assert plus != old, 'Unescaped plus still renders the Japanese glyph'
        image = Image.open(ROOT / 'patch/fonts' / asset)
        # US glyph indices in the Latin atlas; source 1=ink, 2=shadow,
        # 3=background, 0=transparent. Window uses colors 2,3,1.
        colors = {0: 1, 1: 2, 2: 3, 3: 1}
        height = 13 if font == 0 else 15
        width = 10 if font == 0 else 12
        for char in glyphs:
            fixed = render(encode_text(char, charmap, False), font)
            code = charmap[char][0]
            assert any(image.getpixel((code % 16 * 16 + x, code // 16 * 16 + y)) == 1
                       for x in range(width) for y in range(height)), (char, 'Blank source glyph')
            for y in range(16):
                for x in range(16):
                    offset = ((y // 8) * 12 + x // 8) * 32 + (y % 8) * 4 + (x % 8) // 2
                    pixel = (fixed[offset] >> (4 * (x % 2))) & 15
                    expected = (colors[image.getpixel((code % 16 * 16 + x, code // 16 * 16 + y))]
                                if x < width and y < height else 1)
                    assert pixel == expected, (font, char, x, y, pixel, expected)

    for frames, collisions in ((3600, 0), (600, 100), (3600, 100)):
        m.call('Results', (frames, collisions))
        count, time = m.string(m.word(0x08137DF0)), m.string(m.word(0x08137E58))
        if collisions > 99:
            assert count == encode_text('99次以上', charmap, False)
        if frames >= 3600:
            assert time == encode_text('1分钟以上', charmap, False)
    print('14 symbols in both font bitmaps, readable/imported encoders, Japanese preservation and cycling overflow strings: PASS')


if __name__ == '__main__':
    main()
