#!/usr/bin/env python3
"""Execute display adapters and untouched JP getters in ARM/Thumb emulation.

Requires the binary Unicorn wheel. Facility selection/VarGet are stubbed;
name getters, hook veneers, mapping and copying are the real compiled code.
This does not replace an in-game battle/TV smoke test.
"""
import argparse
import struct
from pathlib import Path
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_SP
from unicorn.arm_const import UC_ARM_REG_R0, UC_ARM_REG_R1
from verify_remaining_display_port import Machine, symbols

ROOT = Path(__file__).resolve().parents[2]
BASE = 0x08000000
DEST = 0x02022000
SAVE1, SAVE2 = 0x02000000, 0x02008000


def bl_target(rom, address):
    hi, lo = struct.unpack_from('<HH', rom, address - BASE)
    displacement = ((hi & 2047) << 12) | ((lo & 2047) << 1)
    if displacement & (1 << 22):
        displacement -= 1 << 23
    return address + 4 + displacement


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    names = symbols(args.nm)
    m = Machine(names)
    cpu = m.cpu
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    # Entire original records, not just the EOS-delimited names.
    for offset, length in ((0x2E383C, 855 * 32), (0x561028, 96 * 64),
                           (0x30D114, 4 * 60), (0x5B4A10, 300 * 52),
                           (0x5BD554, 30 * 52), (0x5BDFC8, 30 * 52)):
        assert rom[offset:offset + length] == base[offset:offset + length], hex(offset)
    pairs = [(m.word(names['npc_names'] + i * 8),
              m.word(names['npc_names'] + i * 8 + 4)) for i in range(398)]
    mapping = dict(pairs)
    slateport = struct.unpack_from('<I', base, 0x165BA8)[0]
    assert rom[slateport - BASE:slateport - BASE + 30 * 52] == base[slateport - BASE:slateport - BASE + 30 * 52]
    cpu.mem_write(SAVE1, bytes(0x3D88))
    cpu.mem_write(SAVE2, bytes(0xF2C))
    cpu.mem_write(SAVE2, b'\x01\x02\x03\xff')
    cpu.mem_write(0x03005AEC, struct.pack('<II', SAVE1, SAVE2))
    facility = [0]
    recorded_facility = [0]
    link_count = [0]
    recorded_getter = bl_target(base, 0x081A4956)

    def stub(cpu, address, size, unused):
        if address in (0x08165A4C, 0x0809CF6C, recorded_getter, 0x08009B64, 0x081D0CD8):
            value = cpu.reg_read(UC_ARM_REG_R0) if address == 0x081D0CD8 else facility[0]
            if address == recorded_getter: value = recorded_facility[0]
            if address == 0x08009B64: value = link_count[0]
            cpu.reg_write(UC_ARM_REG_R0, value)
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))
    cpu.hook_add(UC_HOOK_CODE, stub)

    for trainer in range(855):
        pointer = m.word(names['ChsTrainerNames'] + trainer * 4)
        assert m.call('ChsTrainerNameFromId', (trainer,)) == pointer
        assert m.call('ChsResolveTrainerDisplayName', (0x082E3840 + trainer * 32,)) == pointer
        entry = 0x02022800
        cpu.mem_write(entry, struct.pack('<HH', 0, trainer))
        m.call('ChsBufferMatchCallNameAndDesc', (entry, DEST))
        class_id = base[0x2E383C + trainer * 32 + 1]
        class_name = m.string(m.word(names['ChsTrainerClassNames'] + class_id * 4))
        trainer_name = m.string(pointer)
        # Both pointer tables use FC16 mode prefixes, stripped by appender.
        assert class_name[:2] == trainer_name[:2] == b'\xfc\x16'
        expected = b'\xf5\xf3' + class_name[2:-1] + b'\xfc\x0d\x50' + trainer_name[2:-1] + b'\xff'
        assert m.string(DEST) == expected

    def saved():
        return bytes(cpu.mem_read(SAVE1, 0x3D88)), bytes(cpu.mem_read(SAVE2, 0xF2C))

    def call(address, caller, src=0, expected=None, dest=DEST):
        before = saved()
        cpu.mem_write(dest, b'\xa5' * 128)
        m.stop_addresses = {caller & ~1}
        cpu.reg_write(UC_ARM_REG_SP, 0x03007800)
        cpu.reg_write(UC_ARM_REG_LR, caller)
        cpu.reg_write(UC_ARM_REG_R0, dest)
        cpu.reg_write(UC_ARM_REG_R1, src)
        cpu.emu_start(address | 1, 0, count=200000)
        assert cpu.reg_read(UC_ARM_REG_PC) == caller & ~1
        if expected is not None:
            assert m.string(dest) == expected, (hex(address), hex(caller), src, m.string(dest), expected)
            assert bytes(cpu.mem_read(dest + max(8, len(expected)), 128 - max(8, len(expected)))) == b'\xa5' * (128 - max(8, len(expected)))
        if dest != SAVE2 + 0xBD8:
            assert saved() == before, 'display changed save blocks'
        return cpu.reg_read(UC_ARM_REG_R0)

    display_callers = (0x0806E6BF, 0x0814F5DB, 0x081647DB, 0x0816484D,
                       0x081A40E7, 0x081A40FB, 0x081A57DD, 0x081B999D)
    # All 390 ordinary/tent identities in battle, plus default/save/link paths.
    for jp, chs in pairs[:390]:
        table = next(table for table in (0x085B4A10, slateport, 0x085BD554, 0x085BDFC8)
                     if 0 <= (jp - table - 4) // 52 < (300 if table == 0x085B4A10 else 30)
                     and (jp - table - 4) % 52 == 0)
        trainer = (jp - table - 4) // 52
        cpu.mem_write(0x0203B954, struct.pack('<I', table))
        for caller in display_callers:
            call(0x08162D24, caller, trainer, m.string(chs))
        for caller in (0x08164D03, 0x0803736F, 0x0803737B, 0x0203F001):
            call(0x08162D24, caller, trainer, m.string(jp))
        call(0x08195498, 0x0818F65F, trainer, m.string(chs))
    # Every brain, including recorded-battle facility != current facility.
    for i in range(7):
        facility[0] = i
        jp = 0x082E3840 + (805 + i) * 32
        call(0x08162D24, 0x0814F5DB, 0x3FE, m.string(mapping[jp]))
        call(0x08162D24, 0x08164D03, 0x3FE, m.string(jp))
        call(0x081A4944, 0x0814F201, expected=m.string(mapping[jp]))
        call(0x081A4944, 0x0203F001, expected=m.string(jp))
        recorded_facility[0] = (i + 1) % 7
        cpu.mem_write(0x02022C90, struct.pack('<I', 0x1000000))
        recorded_jp = 0x082E3840 + (805 + recorded_facility[0]) * 32
        call(0x081A4944, 0x0814F201, expected=m.string(mapping[recorded_jp]))
        cpu.mem_write(0x02022C90, bytes(4))
    call(0x08195538, 0x0819246F, expected=m.string(mapping[0x082E9D00]))
    call(0x08195498, 0x0818F65F, 0x3FE, m.string(mapping[0x082E9D00]))
    call(0x08195498, 0x0818F65F, 0x3FF, m.string(SAVE2))
    call(0x08162D24, 0x0806E6BF, 0xC03, m.string(mapping[0x082E9CC0]))
    call(0x08162D24, 0x08164D03, 0xC03, m.string(0x082E9CC0))
    # Linked Tower VS screen: two NPC slots display compact CHS without
    # modifying their Japanese link records or exceeding its 8-byte buffer.
    cpu.mem_write(0x02022C90, struct.pack('<I', 0x00800143))
    for id, (jp, chs) in enumerate(pairs[:300]):
        for opponent, src in enumerate((0x020226E0, 0x020226FC)):
            original = m.string(jp)
            cpu.mem_write(src, original)
            cpu.mem_write(0x0203886A + opponent * 2, struct.pack('<H', id))
            expected = b'\xf5' + m.string(chs)[2:-3] + b'\xff'
            assert len(expected) <= 8
            assert call(0x08008888, 0x08035C1B, src, expected) == DEST + len(expected) - 1
            assert m.string(src) == original
            native = original[:5].split(b'\xff')[0] + b'\xff'
            call(0x08008888, 0x0203F001, src, native)
            assert m.string(src) == original
    cpu.mem_write(0x02022C90, bytes(4))
    cpu.mem_write(0x020226A8, b'\x01\x02\x03\xff')
    call(0x08008888, 0x08035C1B, 0x020226A8, b'\x01\x02\x03\xff')
    # The actual interview save destination receives JP only.
    call(0x08162D24, 0x08164D03, 0x3FE, m.string(0x082E3840 + (805 + facility[0]) * 32), SAVE2 + 0xBD8)
    cpu.mem_write(0x02037280, bytes(2))
    show = SAVE1 + 0x27CC
    cpu.mem_write(show, b'\x07')
    for jp, chs in pairs:
        original = m.string(jp)
        candidates = {m.string(p[1]) for p in pairs[:300] + [pairs[391]] if m.string(p[0]) == original}
        expected = next(iter(candidates)) if len(candidates) == 1 else original
        cpu.mem_write(show + 2, b'\x01\x02\x03\xff')
        cpu.mem_write(show + 12, original)
        end = call(0x080088B8, 0x080F233B, show + 12, expected)
        assert end == DEST + len(expected) - 1, 'StringCopy return pointer'
        call(0x080088B8, 0x0203F001, show + 12, original)
        # The show's player field is never translated at the same call PC.
        cpu.mem_write(show + 2, original)
        call(0x080088B8, 0x080F233B, show + 2, original)
    # Explicit policy: matches translate even if a player has the same name.
    jp = pairs[0][0]
    original = m.string(jp)
    cpu.mem_write(show + 2, b'\x01\x02\x03\xff')
    cpu.mem_write(show + 12, original)
    for player in (SAVE2, 0x020226A8):
        link_count[0] = int(player != SAVE2)
        cpu.mem_write(player, original)
        call(0x080088B8, 0x080F233B, show + 12, m.string(pairs[0][1]))
        cpu.mem_write(player, b'\x01\x02\x03\xff')
    link_count[0] = 0
    # A different program scene must not use the Tower name pool.
    cpu.mem_write(show, b'\x08')
    call(0x080088B8, 0x080F233B, show + 12, original)
    cpu.mem_write(show, b'\x07')
    # Invalid TV slots are never dereferenced or translated.
    cpu.mem_write(0x02037280, struct.pack('<H', 25))
    call(0x080088B8, 0x080F233B, show + 12, original)
    cpu.mem_write(0x02037280, bytes(2))
    cpu.mem_write(show, b'\x08')
    # Losers match by name + species; winner is always a player and stays JP.
    for i in range(96):
        record = 0x08561028 + i * 64
        species = bytes(cpu.mem_read(record, 2))
        original = m.string(record + 13)
        expected = m.string(m.word(names['ChsContestOpponentDisplayNames'] + i * 8 + 4))
        for name_offset, species_offset in ((4, 2), (20, 18)):
            cpu.mem_write(show + species_offset, species)
            cpu.mem_write(show + name_offset, original)
            call(0x080088B8, 0x080F3301, show + name_offset, expected if name_offset == 4 else original)
        cpu.mem_write(SAVE2, original)
        call(0x080088B8, 0x080F3301, show + 4, expected)
        cpu.mem_write(show + 2, b'\x00\x00')
        call(0x080088B8, 0x080F3301, show + 4, original)
        cpu.mem_write(SAVE2, b'\x01\x02\x03\xff')
    print(f'PASS: 855 original trainer records; 398 JP/CHS identities; native save/link getters; '
          '7 brains + recordings; Dome/Steven; 300 linked Tower VS names; TV scene/name/species matching; '
          '96 contest-name collision cases; save-block and copy canaries')


if __name__ == '__main__':
    main()
