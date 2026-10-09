"""Execute native Pokemon setters and display getters without changing saved data."""
import argparse
import struct
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_SP, UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_PC
from verify_remaining_display_port import Machine, symbols, ROOT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names.update(NativeSetMonData=0x0806A774, NativeGetMonData=0x0806A058,
                   NativePartyNickname=0x081B1814, NativeBoxNickname=0x0806F4D0,
                   NativeTradeNickname=0x0806F4B0, NativeSummaryEggInfo=0x081C20D8)
    mon, dest, value = 0x02020000, 0x02021008, 0x02022000
    jp_egg = m.string(0x085C8C62)
    chs_egg = m.string(m.names['Chs_ChecklistLiteral_gText_EggNickname'])
    jp_species = m.string(0x082EA31C + 25 * 6)

    def set_data(field, data):
        m.cpu.mem_write(value, data + bytes(16))
        m.call('NativeSetMonData', (mon, field, value))

    def check(name, expected, caller=None):
        before = bytes(m.cpu.mem_read(mon, 100))
        m.cpu.mem_write(dest - 8, b'\xa5' * 40)
        if caller is None:
            m.call(name, (mon, dest))
        else:
            m.stop_addresses = {caller & ~1}
            m.cpu.reg_write(UC_ARM_REG_SP, 0x03007800)
            m.cpu.reg_write(UC_ARM_REG_LR, caller)
            m.cpu.reg_write(UC_ARM_REG_R0, mon)
            m.cpu.reg_write(UC_ARM_REG_R1, dest)
            m.cpu.emu_start(m.names[name] | 1, 0, count=200000)
            assert m.cpu.reg_read(UC_ARM_REG_PC) == caller & ~1
        assert m.string(dest) == expected, (name, m.string(dest), expected)
        assert bytes(m.cpu.mem_read(mon, 100)) == before, name
        assert bytes(m.cpu.mem_read(dest - 8, 8)) == b'\xa5' * 8
        assert bytes(m.cpu.mem_read(dest + 12, 20)) == b'\xa5' * 20
        assert m.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800

    cases = ((True, jp_egg, chs_egg), (True, b'\xa1\xa2\xff', b'\xa1\xa2\xff'),
             (False, jp_egg, jp_egg), (False, jp_species, b'\xf5\xf2\x19\x00\xff'))
    for egg, nickname, expected in cases:
        m.cpu.mem_write(mon, bytes(100))
        set_data(11, struct.pack('<H', 25))
        set_data(2, nickname)
        set_data(45, bytes((egg,)))
        assert m.call('NativeGetMonData', (mon, 45, 0)) == egg
        for name in ('ChsCopyMonNickname', 'ChsCopyBoxMonNickname',
                     'NativePartyNickname', 'NativeBoxNickname', 'NativeTradeNickname'):
            check(name, expected)
        for caller in (0x0806F5E3, 0x08071765):
            check('NativeTradeNickname', nickname, caller)
        check('NativeBoxNickname', nickname, 0x08070FBB)

    # Run the real egg summary entry up to its print call, not just our helper.
    set_data(2, jp_egg)
    set_data(45, b'\x01')
    before = bytes(m.cpu.mem_read(mon, 100))
    summary = 0x02023000
    m.cpu.mem_write(summary + 12, before)
    m.cpu.mem_write(0x0203CBE8, struct.pack('<I', summary))
    m.call('NativeSummaryEggInfo', stop_addresses=(0x081C1ED8,))
    assert m.cpu.reg_read(UC_ARM_REG_R0) == 0x12
    assert m.string(m.cpu.reg_read(UC_ARM_REG_R1)) == chs_egg
    assert bytes(m.cpu.mem_read(summary + 12, 100)) == before

    # Native egg creation keeps the original ROM nickname pointer. The storage
    # literal and original Japanese bytes must not be replaced globally.
    baseline = (ROOT / 'baserom_jp.gba').read_bytes()
    for address in (0x08070444, 0x080704C8):
        assert m.word(address) == 0x085C8C62
    assert m.string(0x085C8C62) == baseline[0x5C8C62:0x5C8C62 + len(jp_egg)]
    assert m.word(0x080CE77C) == m.names['Chs_ChecklistLiteral_gText_EggNickname']
    print('PASS: default egg displays Chinese; custom eggs/non-eggs remain distinct; party/box/native routes; storage callers retain Japanese; full Pokemon bytes and output canaries unchanged')


if __name__ == '__main__':
    main()
