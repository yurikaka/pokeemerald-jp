"""Execute script species buffering, gift prompts and unchanged JP name getters."""
import argparse
import struct
from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R6, UC_ARM_REG_SP
from verify_remaining_display_port import Machine, symbols, ROOT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    # The reconstructed ELF's script-command symbol names are not authoritative:
    # this entry uses the six-byte species stride described in dev scrcmd.c.
    m.names.update(NativeBufferSpecies=0x0809A90C, NativeSpeciesName=0x0806B3DC,
                   NativeExpandPlaceholders=0x08008BCC)
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    commands = struct.pack('<III', 0x0809A90D, 0x0809A951, 0x0809A9A1)
    command_offset = base.index(commands)
    assert rom[command_offset:command_offset + len(commands)] == commands
    assert m.word(0x0809A94C) == m.names['ChsSpeciesNameTokens']
    # Preserve the six-byte indexing and all the command's executable code.
    assert rom[0x9A90C:0x9A94C] == base[0x9A90C:0x9A94C]
    assert rom[0x6B3DC:0x6B404] == base[0x6B3DC:0x6B404]
    context, script, output, printer = 0x02020000, 0x02020100, 0x02021000, 0x02022000
    saved, saved_size = 0x02028000, 0x10000
    m.cpu.mem_write(saved, b'\xa5' * saved_size)
    # These are exactly the two buffer commands in each gift fanfare. Party
    # and PC receive branches both call this fanfare before the nickname prompt.
    for start, end, species in ((0x201696, 0x2016A9, 388),
                                (0x201739, 0x20174C, 390),
                                (0x20C97D, 0x20C993, 398)):
        event = base[start:end]
        for index in (0, 1):
            command = b'\x7d' + bytes((index,)) + struct.pack('<H', species)
            offset = start + event.index(command)
            assert rom[offset:offset + 4] == command

    for species in (*range(1, 252), *range(277, 412)):
        token = b'\xf5\xf2' + struct.pack('<H', species) + b'\xff'
        for index in (0, 1, 2):
            dest = m.word(0x084E8918 + index * 4)
            m.cpu.mem_write(dest - 8, b'\xa5' * 40)
            m.cpu.mem_write(script, bytes((index,)) + struct.pack('<H', species))
            m.cpu.mem_write(context, bytes(32))
            m.cpu.mem_write(context + 8, struct.pack('<I', script))
            assert m.call('NativeBufferSpecies', (context,)) == 0
            assert m.string(dest) == token, (species, index)
            assert m.word(context + 8) == script + 3
            assert bytes(m.cpu.mem_read(dest - 8, 8)) == b'\xa5' * 8
            assert bytes(m.cpu.mem_read(dest + 5, 27)) == b'\xa5' * 27
            assert m.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
        # Default nickname generation must still copy the original JP species.
        m.call('NativeSpeciesName', (output, species))
        expected = base[0x2EA31C + species * 6:0x2EA31C + species * 6 + 6]
        expected = expected[:expected.index(255) + 1]
        assert m.string(output) == expected, species

    for species in (388, 390, 398):
        token = b'\xf5\xf2' + struct.pack('<H', species) + b'\xff'
        m.cpu.mem_write(m.word(0x084E8918), token)
        m.call('NativeExpandPlaceholders', (output, m.names['Chs_gText_NicknameThisPokemon']))
        expanded = m.string(output)
        assert b'\xfc\x15' + token[:-1] + b'\xfc\x16' in expanded
        # Chinese species tokens must render even within a JP-mode placeholder.
        m.cpu.mem_write(output, token)
        m.cpu.mem_write(printer, bytes(32))
        m.cpu.mem_write(printer, struct.pack('<I', output))
        glyphs = 0
        for _ in range(20):
            m.cpu.reg_write(UC_ARM_REG_R4, printer + 0x14)
            m.cpu.reg_write(UC_ARM_REG_R6, printer)
            m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
            end = m.cpu.reg_read(UC_ARM_REG_PC)
            if end == 0x08005B32:
                glyphs += 1
            elif end == 0x0800582C:
                assert m.cpu.reg_read(UC_ARM_REG_R3) == 255
                break
        else:
            raise AssertionError('Species renderer did not reach EOS')
        assert glyphs == (3 if species == 398 else 4), (species, glyphs)
    assert bytes(m.cpu.mem_read(saved, saved_size)) == b'\xa5' * saved_size
    print('PASS: 386 usable species x 3 script buffers; fossil/Beldum party and PC events; nickname placeholder expansion and Chinese rendering; original JP name getters, buffer canaries and saved data unchanged')


if __name__ == '__main__':
    main()
