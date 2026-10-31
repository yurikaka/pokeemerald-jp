#!/usr/bin/env python3
"""Check direct battle nickname calls against the existing display helper."""
import argparse
import struct
from pathlib import Path
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2, UC_ARM_REG_R4, UC_ARM_REG_R9, UC_ARM_REG_SP
from verify_remaining_display_port import Machine, symbols, ROOT

SITES = (0x0814E960, 0x0814E994, 0x0814E9C8, 0x0814E9FC,
         0x0814EA34, 0x0814EA74, 0x0814EAB4, 0x0814EAF4,
         0x0814EB7C, 0x0814EBB2, 0x0814EBFE, 0x0814EC38,
         0x0814ECA2, 0x0814ECD6, 0x0814ED3E, 0x0814ED72,
         0x0814EDDA, 0x0814EE0E, 0x0814EE76, 0x0814EEAA,
         0x0814EF12, 0x0814EF46, 0x0814F3A2, 0x0814F3D4,
         0x0814F77A, 0x0814F7BC, 0x0814F81A, 0x0814F832)
TRADE_SITES = (0x08078138, 0x08078160, 0x080794A4, 0x080796D6,
               0x0807B55A, 0x0807B572, 0x0807B5D0, 0x0807E1E6)
OTHER_SITES = (0x080F0A4C, 0x0813DC6E, 0x0813E2FC, 0x0813EB38,
               0x0813F67E, 0x08161212, 0x080CE50E, 0x081CFA34,
               0x081CFDC4, 0x081CEFDA, 0x08166B72, 0x081775A2)


def bl_target(rom, address):
    hi, lo = struct.unpack_from('<HH', rom, address - 0x08000000)
    assert hi & 0xF800 == 0xF000 and lo & 0xF800 == 0xF800
    d = ((hi & 2047) << 12) | ((lo & 2047) << 1)
    if d & (1 << 22): d -= 1 << 23
    return address + 4 + d


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    names = symbols(args.nm)
    m = Machine(names)
    cpu = m.cpu
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    assert names['ChsBattleGetMonNickname'] == 0x08162D3C
    assert rom[0x06A058:0x06A1B4] == base[0x06A058:0x06A1B4], 'GetMonData3 changed'
    for site in SITES + TRADE_SITES + OTHER_SITES:
        assert bl_target(base, site) == 0x0806A058
        assert bl_target(rom, site) == names['ChsBattleGetMonNickname']
    m.names['NativeSetMonData'] = 0x0806A774
    mon, dest, value = 0x02020000, 0x02021000, 0x02022000
    def set_data(field, data):
        cpu.mem_write(value, data + bytes(16))
        m.call('NativeSetMonData', (mon, field, value))
    jp_egg = m.string(0x085C8C62)
    cases = [(False, 25, m.string(0x082EA31C + 25 * 6)),
             (False, 25, b'\xa1\xa2\xff'),
             (True, 25, jp_egg), (True, 25, b'\xa1\xa2\xff')]
    for egg, species, nickname in cases:
        cpu.mem_write(mon, bytes(100))
        set_data(11, struct.pack('<H', species))
        set_data(2, nickname)
        set_data(45, bytes([egg]))
        before = bytes(cpu.mem_read(mon, 100))
        cpu.mem_write(dest, b'\xa5' * 64)
        expected_return = m.call('ChsCopyMonNickname', (mon, dest))
        expected = bytes(cpu.mem_read(dest, 64))
        for site in SITES + TRADE_SITES + OTHER_SITES:
            cpu.mem_write(dest, b'\xa5' * 64)
            m.stop_addresses = {site + 4}
            cpu.reg_write(UC_ARM_REG_SP, 0x03007800)
            cpu.reg_write(UC_ARM_REG_LR, 0x0203F001)
            cpu.reg_write(UC_ARM_REG_R0, mon)
            cpu.reg_write(UC_ARM_REG_R1, 2)
            cpu.reg_write(UC_ARM_REG_R2, dest)
            cpu.emu_start(site | 1, 0, count=200000)
            assert cpu.reg_read(UC_ARM_REG_PC) == site + 4, hex(site)
            assert cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
            assert cpu.reg_read(UC_ARM_REG_R0) == expected_return
            assert bytes(cpu.mem_read(dest, 64)) == expected
            assert bytes(cpu.mem_read(mon, 100)) == before
    # The original jump-table path must still enter the EXP placeholder hook.
    calls = []
    def stub_expand(cpu, address, size, unused):
        if address == 0x0814F664:
            calls.append(address)
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))
    cpu.hook_add(UC_HOOK_CODE, stub_expand)
    for exp_text in (False, True):
        for encoded in (False, True):
            calls.clear()
            data = bytes([0xFD if encoded else 0xA1, 1, 2, 3, 4, 0xFF])
            cpu.mem_write(0x02022C0C, data)
            cpu.reg_write(UC_ARM_REG_R9, names['Chs_sText_PkmnGainedEXP'] + 4 if exp_text else 0)
            m.stop_addresses = {0x0814F5DC}
            cpu.reg_write(UC_ARM_REG_SP, 0x03007800)
            cpu.emu_start(0x0814E8E9, 0, count=200000)
            assert cpu.reg_read(UC_ARM_REG_PC) == 0x0814F5DC
            assert cpu.reg_read(UC_ARM_REG_R4) == (0x02021C40 if encoded else 0x02022C0C)
            assert bool(calls) == encoded
            assert bytes(cpu.mem_read(0x02022C0C, 6)) == (data[:4] + b'\xff' + data[5:] if exp_text and encoded else data)
    print('PASS: 48 direct call sites; native GetMonData3 unchanged; default, custom and egg names match existing helper')


if __name__ == '__main__':
    main()
