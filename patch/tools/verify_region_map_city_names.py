"""Exercise both city branches of the native Pokenav info-window function.

Run the real text renderer and window fill; stub tilemap/VRAM transfers and
city pictures. This is an ARM execution test, not a full game simulation.
"""

import argparse
import struct

from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC

from verify_remaining_display_port import Machine, STOP, symbols


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    names = symbols(args.nm)
    names.update(Fonts=0x080061A4, Info=0x081CC260, MapName=0x08124578)
    machine = Machine(names)
    cpu = machine.cpu
    state, region, framebuffer = 0x02021000, 0x02022000, 0x02028000
    size = 12 * 2 * 32
    calls = []

    def intercept(cpu, address, instruction_size, unused):
        if address == 0x081C6DFC:  # GetSubstructPtr(REGION_MAP)
            assert cpu.reg_read(UC_ARM_REG_R0) == 16
            cpu.reg_write(UC_ARM_REG_R0, region)
        elif address in (0x082959B8, 0x082959BC):  # BIOS memory copies
            src, dst, control = [cpu.reg_read(r) for r in
                                (UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2)]
            unit = 4 if address == 0x082959B8 or control & (1 << 26) else 2
            length = (control & 0x1FFFFF) * unit
            data = (bytes(cpu.mem_read(src, unit)) * (length // unit)
                    if control & (1 << 24) else bytes(cpu.mem_read(src, length)))
            cpu.mem_write(dst, data)
        elif address in (0x080037C4, 0x08003528, 0x080035A8, 0x080026E0,
                         0x081CC4B0, 0x081CC6E4):
            # Tilemap writes, window copies, city picture and zoom label.
            calls.append(address)
        else:
            return
        cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

    cpu.hook_add(UC_HOOK_CODE, intercept)
    machine.call('Fonts')
    cpu.mem_write(0x02020004, bytes((0, 0, 0, 12, 2, 0, 0, 0))
                  + struct.pack('<I', framebuffer))
    cpu.mem_write(state, bytes(32))  # infoWindowId = 0

    def render(city, kind, stops=()):
        cpu.mem_write(region, struct.pack('<HBB', city, kind, 0) + bytes(20))
        machine.call('MapName', (region + 4, city, 10))
        assert machine.string(region + 4)[0] != 0xFF
        cpu.mem_write(framebuffer, b'\x33' * size)
        calls.clear()
        machine.call('Info', (state,), stops)
        return bytes(cpu.mem_read(framebuffer, size))

    # Reproduce the old bad continuation: it executes the veneer literal
    # at 0x081CC2DC instead of the next native instruction at 0x081CC2E0.
    start = names['ChsRegionMapCityWindowFillB']
    code = bytes(cpu.mem_read(start, 128))
    literal = start + code.index(struct.pack('<I', 0x081CC2E1))
    cpu.mem_write(literal, struct.pack('<I', 0x081CC2DD))
    render(3, 3, (0x081CC2DC,))
    assert cpu.reg_read(UC_ARM_REG_PC) == 0x081CC2DC
    assert 0x080037C4 not in calls, 'Control unexpectedly reached tilemap setup'
    cpu.mem_write(literal, struct.pack('<I', 0x081CC2E1))

    for city in range(16):
        can_fly = render(city, 2)
        assert cpu.reg_read(UC_ARM_REG_PC) == STOP
        assert 0x080037C4 in calls and 0x08003528 in calls
        cannot_fly = render(city, 3)
        assert cpu.reg_read(UC_ARM_REG_PC) == STOP
        assert 0x080037C4 in calls and 0x08003528 in calls
        assert can_fly == cannot_fly, (city, 'City title differs by visit state')
        assert can_fly != b'\x11' * size, (city, 'Blank city name')
        assert can_fly != b'\x33' * size, (city, 'Window was not updated')
    print('Old continuation reproduced; all 16 city names render in both visit states (32 cases).')


if __name__ == '__main__':
    main()
