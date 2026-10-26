"""Execute incoming-call name generation and the intro-to-message transition.

World state, the completed intro printer and new printer registration are
stubbed. Native message selection, variable population, placeholder expansion,
name hooks and shared returns execute in ARM emulation, not a full game.
"""
import argparse
import struct

from unicorn import UcError, UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_PC
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_SP
from unicorn.arm_const import UC_ARM_REG_R4, UC_ARM_REG_R5, UC_ARM_REG_R6

from verify_remaining_display_port import Machine, ROOT, STOP, symbols


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    names = symbols(args.nm)
    names.update(Name=0x08196644, Intro=0x08195ED8)
    m = Machine(names)
    cpu = m.cpu
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    assert bytes(cpu.mem_read(0x08196688, 12)) == base[0x196688:0x196694]
    trainers = [struct.unpack('<H', cpu.mem_read(0x085D6934 + i * 20, 2))[0]
                for i in range(64)]
    special = {struct.unpack('<H', cpu.mem_read(0x085D7A54 + i * 8, 2))[0]:
               m.word(0x085D7A54 + i * 8 + 4) for i in range(6)}
    dest = 0x02024000
    sentinel = b'\xA5' * 64
    returns = []

    def trace_return(cpu, address, size, unused):
        if address == 0x0819668C:
            returns.append(address)

    cpu.hook_add(UC_HOOK_CODE, trace_return)

    def check_name(index, trainer):
        cpu.mem_write(dest, sentinel)
        returns.clear()
        registers = (UC_ARM_REG_R4, UC_ARM_REG_R5, UC_ARM_REG_R6)
        for reg in registers:
            cpu.reg_write(reg, 0x12345678)
        m.call('Name', (index, dest))
        assert cpu.reg_read(UC_ARM_REG_PC) == STOP
        assert cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
        assert returns == [0x0819668C], 'Must use the native shared epilogue once'
        for reg in registers:
            assert cpu.reg_read(reg) == 0x12345678
        pointer = special.get(trainer)
        if pointer is None:
            pointer = m.word(names['ChsTrainerNames'] + trainer * 4)
        expected = m.string(pointer)
        assert m.string(dest) == expected
        assert len(expected) <= 32
        assert bytes(cpu.mem_read(dest + len(expected), 64 - len(expected))) == sentinel[len(expected):]

    # Negative control: the previous 16-byte hook overwrote the shared return.
    installed = bytes(cpu.mem_read(0x08196680, 16))
    old = (struct.pack('<HHHHH', 0xB401, 0xB401, 0x4801, 0x9001, 0xBD01)
           + b'\0\0' + struct.pack('<I', names['ChsMatchCallPopulateTrainerName'] | 1))
    cpu.mem_write(0x08196680, old)
    cpu.ctl_remove_cache(0x08196644, 0x08196698)
    try:
        m.call('Name', (5, dest))
    except UcError:
        pass
    else:
        raise AssertionError('Old multi-trainer return did not reproduce failure')
    cpu.mem_write(0x08196680, installed)
    cpu.ctl_remove_cache(0x08196644, 0x08196698)

    for index, trainer in enumerate(trainers):
        check_name(index, trainer)
    # Exercise all six special entries, including the one outside this pool.
    first = bytes(cpu.mem_read(0x085D6934, 2))
    for trainer in special:
        cpu.mem_write(0x085D6934, struct.pack('<H', trainer))
        check_name(0, trainer)
    cpu.mem_write(0x085D6934, first)

    printed = []

    def intercept(cpu, address, size, unused):
        if address in (0x08196248, 0x0819632C):
            # Finished intro; deterministic current map section.
            cpu.reg_write(UC_ARM_REG_R0, 0)
        elif address == 0x08196310:
            cpu.reg_write(UC_ARM_REG_R0, 1)  # Same-route rematch message.
        elif address == 0x08003B18:
            pass  # Window clear; rendering is not needed for this transition.
        elif address == 0x081961D8:
            assert cpu.reg_read(UC_ARM_REG_R0) == 0
            printed.append(m.string(cpu.reg_read(UC_ARM_REG_R1)))
        else:
            return
        cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

    cpu.hook_add(UC_HOOK_CODE, intercept)
    cpu.mem_write(0x03005B68, bytes(40))  # Task 0, window 0.
    cpu.mem_write(0x02036FB8, bytes(32))  # Current map section 0.
    cpu.mem_write(0x03005AF0, struct.pack('<I', 0x02025000))
    cpu.mem_write(0x02025000, b'\x01\x02\xFF' + bytes(64))  # JP player name.
    for trainer in trainers:
        cpu.mem_write(0x0203CA4C, struct.pack('<IHBB', 0, trainer, 0, 0))
        cpu.mem_write(0x02021C7C, b'\xA5' * 1000)
        assert m.call('Intro', (0,)) == 1
        assert printed[-1] != b'\xFF'
        assert len(printed[-1]) < 1000
        assert bytes(cpu.mem_read(0x02021C7C + 1000, 16)) == bytes(16)
    assert len(printed) == 64
    print('Old shared-return crash reproduced; 64 names, 6 special names and 64 incoming-call transitions pass.')


if __name__ == '__main__':
    main()
