"""Execute gift PC message producers/expansion and naming-screen selection.

Unicorn required. Naming-screen state queries are stubbed; box/name copying,
nickname conversion and placeholder expansion run as ARM code. No UI simulation.
"""
import argparse
import struct
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R0, UC_ARM_REG_R1
from verify_remaining_display_port import Machine, symbols, ROOT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names.update(BufferSpecies=0x0809A90C, BufferBox=0x0809ABA0,
                   Expand=0x08008BCC, NamingMessage=0x080E2A78)
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    originals = (0x08243E08, 0x08243E2A, 0x08243E4C, 0x08243E80)
    labels = ('SomeonesPC', 'LanettesPC', 'SomeonesPCBoxFull', 'LanettesPCBoxFull')
    script_refs = (0x082441F7, 0x08244222, 0x08244209, 0x08244234)
    for index, (original, label) in enumerate(zip(originals, labels)):
        expected = m.names['Chs_gText_PkmnTransferred' + label]
        for address in (script_refs[index], 0x08565858 + index * 4, 0x085AB988 + index * 4):
            assert struct.unpack_from('<I', base, address - 0x08000000)[0] == original
            assert m.word(address) == expected, hex(address)
        needle = struct.pack('<I', original)
        assert needle not in rom, f'Japanese template pointer remains: {original:08X}'
    # The shared event's only changes are the four audited msgbox operands.
    event_start, event_end = 0x2441CA, 0x244239
    restored = bytearray(rom[event_start:event_end])
    for address, original in zip(script_refs, originals):
        offset = address - 0x08000000 - event_start
        assert base[address - 0x08000000 - 2:address - 0x08000000] == b'\x0f\x00'
        restored[offset:offset + 4] = struct.pack('<I', original)
    assert restored == base[event_start:event_end]

    storage, context, script = 0x02000000, 0x02020000, 0x02020100
    output, naming, nickname = 0x02021008, 0x02028000, 0x0202A000
    m.cpu.mem_write(storage, b'\xa5' * 0x83E0)
    m.cpu.mem_write(0x03005AF4, struct.pack('<I', storage))
    defaults = [base[0x5CB584:0x5CB588] + bytes(0xA1 + int(c) for c in str(i + 1)) + b'\xff'
                for i in range(14)]
    for i, name in enumerate(defaults):
        m.cpu.mem_write(storage + 0x8344 + i * 9, name)
    full, lanette, selected_box = False, False, 0

    def state_queries(cpu, address, size, unused):
        if address == 0x0813B298:
            result = int(full)
        elif address == 0x0809D068:
            assert cpu.reg_read(UC_ARM_REG_R0) == 0x08AB
            result = int(lanette)
        elif address == 0x0813B248:
            result = (selected_box + 1) % 14
        elif address == 0x0809CF6C:
            value = cpu.reg_read(UC_ARM_REG_R0)
            assert value < 0x4000 or value == 0x4036
            result = selected_box if value == 0x4036 else value
        else:
            return
        cpu.reg_write(UC_ARM_REG_R0, result)
        cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

    m.cpu.hook_add(UC_HOOK_CODE, state_queries)

    def buffer(command, index, value):
        m.cpu.mem_write(context, bytes(32))
        m.cpu.mem_write(context + 8, struct.pack('<I', script))
        m.cpu.mem_write(script, bytes((index,)) + struct.pack('<H', value))
        m.call(command, (context,))

    def expanded(pointer):
        m.cpu.mem_write(output - 8, b'\xa5' * 264)
        m.call('Expand', (output, pointer))
        assert bytes(m.cpu.mem_read(output - 8, 8)) == b'\xa5' * 8
        assert bytes(m.cpu.mem_read(output + 240, 16)) == b'\xa5' * 16
        return m.string(output)

    cases = 0
    # ScriptGiveMon gifts: Johto starters, fossils, Castform, Beldum.
    for species in (152, 155, 158, 388, 390, 385, 398):
        token = b'\xf5\xf2' + struct.pack('<H', species)
        for selected_box in range(14):
            next_box = (selected_box + 1) % 14
            for custom in (False, True):
                for i, name in enumerate(defaults):
                    m.cpu.mem_write(storage + 0x8344 + i * 9, name.ljust(9, b'\xff'))
                if custom:
                    for box in (selected_box, next_box):
                        m.cpu.mem_write(storage + 0x8344 + box * 9, b'\x01\x02\x03\xff' + b'\xa5' * 5)
                saved = bytes(m.cpu.mem_read(storage, 0x83E0))
                for full in (False, True):
                    for lanette in (False, True):
                        index = int(lanette) + 2 * int(full)
                        buffer('BufferBox', 0, selected_box)
                        buffer('BufferSpecies', 1, species)
                        buffer('BufferBox', 2, next_box)
                        box1, box3 = m.string(0x02021C40), m.string(0x02021C68)
                        script_text = expanded(m.word(script_refs[index]))
                        assert token in script_text
                        assert box1[:-1] in script_text
                        if full:
                            assert box3[:-1] in script_text
                        # Real post-naming selection uses the same four templates.
                        m.cpu.mem_write(naming, bytes(0x1E38))
                        m.cpu.mem_write(0x02039C34, struct.pack('<I', naming))
                        m.cpu.mem_write(naming + 0x1E30, struct.pack('<IH', nickname, species))
                        jp_name = m.string(0x082EA31C + species * 6)
                        for nick in (jp_name, b'\x04\x05\x06\xff'):
                            m.cpu.mem_write(nickname, nick)
                            m.call('NamingMessage', stop_addresses=(0x08008BCC,))
                            assert m.cpu.reg_read(UC_ARM_REG_R1) == m.word(script_refs[index])
                            naming_text = expanded(m.cpu.reg_read(UC_ARM_REG_R1))
                            if nick == jp_name:
                                assert naming_text == script_text
                            else:
                                assert nick[:-1] in naming_text
                            assert m.string(nickname) == nick
                        assert bytes(m.cpu.mem_read(storage, 0x83E0)) == saved
                        cases += 1
    print(f'PASS: 12 transfer references; no JP template pointers; {cases} script cases and '
          f'{cases * 2} native naming cases; seven gifts, four branches, 14 boxes, '
          'default/custom names, unchanged storage and output guards')


if __name__ == '__main__':
    main()
