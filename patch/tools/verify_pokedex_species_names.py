"""Execute mixed-width species rendering and Pokédex name layout in Unicorn."""
import argparse
import re
import struct

from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_LR, UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R3
from unicorn.arm_const import UC_ARM_REG_R4, UC_ARM_REG_R5, UC_ARM_REG_R6
from verify_remaining_display_port import Machine, ROOT, symbols
from build_texts import encode_compact_chinese_text, read_charmap


def render(m, text):
    printer, source = 0x02001000, 0x02002000
    m.cpu.mem_write(printer, bytes(32) + b'\xa5' * 32)
    m.cpu.mem_write(printer, struct.pack('<I', source))
    m.cpu.mem_write(source, text + b'\xa5' * 32)
    result = []
    for _ in range(40):
        m.cpu.reg_write(UC_ARM_REG_R4, printer + 0x14)
        m.cpu.reg_write(UC_ARM_REG_R6, printer)
        m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
        pc = m.cpu.reg_read(UC_ARM_REG_PC)
        assert bytes(m.cpu.mem_read(printer + 32, 32)) == b'\xa5' * 32
        if pc == 0x08005B32:
            result.append(('glyph', bytes(m.cpu.mem_read(0x03003030, 0x82))))
        elif pc == 0x0800582C:
            char = m.cpu.reg_read(UC_ARM_REG_R3)
            if char == 255:
                return result
            result.append(('native', char))
    raise AssertionError('species rendering crossed EOS or exceeded glyph budget')


def verify_native_print(names):
    """Run the installed hooks through native printing and CopyGlyphToWindow.

    Wokann text.c/window.h: gFonts uses SetDefaultFontsPointer and gWindows
    records contain the eight-byte template followed by the tile-data pointer.
    Only the final transfer to VRAM is skipped; text decoding, font selection,
    glyph generation and writes to the window tile buffer execute normally.
    """
    m = Machine(names)
    m.names['DefaultFonts'] = 0x080061A4
    m.call('DefaultFonts')
    m.cpu.mem_write(0x02020004, bytes((0, 0, 0, 30, 20, 0, 0, 0))
                    + struct.pack('<I', 0x02028000))
    glyphs = []

    def capture(cpu, address, size, unused):
        if address == 0x08003528:  # CopyWindowToVram: no GBA DMA in Unicorn
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))
        elif address == 0x08004850:  # CopyGlyphToWindow
            printer = cpu.reg_read(UC_ARM_REG_R0)
            glyphs.append((bytes(cpu.mem_read(printer + 8, 2)),
                           bytes(cpu.mem_read(0x03003030, 0x82))))

    m.cpu.hook_add(UC_HOOK_CODE, capture)
    for species in (233, 234):
        for route, coords in (('ChsPokedexName', (17, 3)),
                              ('ChsPokedexName', (11, 4)),
                              ('ChsPokedexName', (4, 15)),
                              ('ChsPokedexListName', (17, 3))):
            glyphs.clear()
            m.cpu.mem_write(0x02028000, bytes(19200))
            params = (0, species, *coords) if route == 'ChsPokedexName' else (species, *coords)
            m.call(route, params)
            wanted = (5 if species == 233 else 3) + (3 if coords == (11, 4) else 0)
            assert len(glyphs) == wanted, (species, route, coords, len(glyphs))
            assert all(x < 240 and y < 160 for (x, y), glyph in glyphs)
            assert any(m.cpu.mem_read(0x02028000, 19200))
    print('PASS: native info/cry/size/list printers draw Porygon2 and Stantler without extra glyphs')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    source = (ROOT.parent / 'pokeemerald_us_chs/src/data/text/species_names.h').read_text()
    source = source.split('const u8 gSpeciesNames[][POKEMON_NAME_LENGTH + 1] = {', 1)[1]
    names = re.findall(r'\[SPECIES_\w+\]\s*=\s*_\("([^"]*)"\)', source)
    charmap = read_charmap(ROOT / 'patch/charmap_chs.txt')
    assert len(names) == 412
    for species, name in enumerate(names):
        encoded = encode_compact_chinese_text(name, charmap)
        actual = m.string(m.word(m.names['ChsSpeciesNames'] + species * 4))
        assert actual == encoded, (species, name)
        expected = render(m, encoded)
        compact = render(m, bytes((0xF5, 0xF2, species & 255, species >> 8, 255)))
        assert compact == expected, (species, name, 'compact render differs')
        assert len(compact) == len(name), (species, name, 'wrong glyph count')
    m.names['NationalToSpecies'] = 0x0806CED0
    for national in range(1, 387):
        species = m.call('NationalToSpecies', (national,))
        m.call('ChsPokedexName', (0, national, 1, 1), (0x080BFFE0,))
        assert m.cpu.reg_read(UC_ARM_REG_R5) == len(names[species]), (species, names[species])
        text = m.string(m.cpu.reg_read(UC_ARM_REG_R1))
        assert text == bytes((0xF5, 0xF2, species & 255, species >> 8, 255))
    # Info, cry and size layouts select the narrow form for the five glyphs.
    for x, y in ((4, 15), (11, 4), (17, 1)):
        m.call('ChsPokedexName', (0, 233, x, y),
               (0x080BFFE0, m.names['ChsPokedexPrintNameShifted']))
        assert m.cpu.reg_read(UC_ARM_REG_R5) == 5
        text = m.string(m.cpu.reg_read(UC_ARM_REG_R1))
        expected = (b'\xf5\xf3' + encode_compact_chinese_text(names[233], charmap)[1:-1]
                    + b'\xf5\xf4\xff') if x == 4 else b'\xf5\xf2\xe9\x00\xff'
        assert text == expected, (x, y, text)
    # The battle healthbox had the same length-scan assumption. Run through
    # actual GetMonData/default-nickname conversion, stopping before gender.
    m.names['SetMonData'] = 0x0806A774
    baseline = (ROOT / 'baserom_jp.gba').read_bytes()
    mon, value = 0x02020000, 0x02022000
    for species in (25, 233, 234):
        m.cpu.mem_write(mon, bytes(100))
        m.cpu.mem_write(value, struct.pack('<H', species))
        m.call('SetMonData', (mon, 11, value))
        jp_name = baseline[0x2EA31C + species * 6:0x2EA31C + (species + 1) * 6]
        m.cpu.mem_write(mon + 8, jp_name.ljust(10, b'\xff'))
        stored = bytes(m.cpu.mem_read(mon, 100))
        m.call('ChsUpdateNickInHealthbox', (0, mon), (0x08069AF4,))
        expected = (b'\xf5\xf3' + encode_compact_chinese_text(names[species], charmap)[1:-1]
                    + b'\xf5\xf4\xff') if len(names[species]) == 5 else bytes((0xF5, 0xF2, species, 0, 255))
        assert m.string(0x02022AE0)[3:] == expected
        assert bytes(m.cpu.mem_read(mon, 100)) == stored
    print('PASS: all 412 species render exactly as their source names, including single-byte digits')
    print('PASS: 386 Pokedex name lengths and Porygon2 info/cry/size layout paths; no Stantler spill')
    print('PASS: mixed/normal/adjacent species healthbox names; stored Pokemon data unchanged')
    verify_native_print(symbols(args.nm))


if __name__ == '__main__':
    main()
