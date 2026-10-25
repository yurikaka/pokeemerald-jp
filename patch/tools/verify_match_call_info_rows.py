"""Render native Match Call info rows and check long-to-short replacement."""

import argparse
import struct

from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R0

from build_texts import encode_text, read_charmap
from verify_remaining_display_port import Machine, ROOT


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    machine = Machine({"Fonts": 0x080061A4, "Info": 0x081C85FC})
    cpu = machine.cpu
    text_address, list_address, state_address = 0x02024000, 0x02021000, 0x02022000
    framebuffer = 0x02028000
    size = 15 * 32 * 32  # 120 pixels wide, sixteen circular rows high.

    def intercept(cpu, address, instruction_size, unused):
        if address == 0x081CA77C:  # Substitute contact data, execute real renderer.
            cpu.reg_write(UC_ARM_REG_R0, text_address)
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))
        elif address == 0x080035A8:  # No VRAM transfers in the rendering test.
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

    cpu.hook_add(UC_HOOK_CODE, intercept)
    machine.names["Fonts"] = 0x080061A4
    machine.call("Fonts")
    cpu.mem_write(0x02020004, bytes((0, 0, 0, 15, 32, 0, 0, 0))
                  + struct.pack("<I", framebuffer))
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    long = encode_text("芳香的草属性宝可梦。", charmap, False)
    short = encode_text("强力作战。", charmap, False)

    def render(text, base, field):
        cpu.mem_write(list_address, bytes(0x100))
        cpu.mem_write(list_address + 4, bytes((15,)))
        cpu.mem_write(list_address + 10, struct.pack("<H", base))
        cpu.mem_write(state_address, bytes(0x20))
        cpu.mem_write(text_address, text)
        machine.call("Info", (state_address, list_address, field))
        return bytes(cpu.mem_read(framebuffer, size))

    def compare(base, field):
        cpu.mem_write(framebuffer, b"\x11" * size)
        render(long, base, field)
        after = render(short, base, field)
        cpu.mem_write(framebuffer, b"\x11" * size)
        expected = render(short, base, field)
        return after == expected

    original = bytes.fromhex("3901022211430091")
    installed = bytes(cpu.mem_read(0x081C8648, 8))
    assert installed != original, "Info-row hook missing"
    cpu.mem_write(0x081C8648, original)
    cpu.ctl_remove_cache(0x081C85FC, 0x081C867C)
    assert not compare(0, 0), "Native control did not reproduce the stale text"
    cpu.mem_write(0x081C8648, installed)
    cpu.ctl_remove_cache(0x081C85FC, 0x081C867C)
    for base in (0, 7, 15):
        for field in range(4):
            assert compare(base, field), (base, field)
    print("Native control reproduces stale text; 12 patched row/wrap cases pass.")


if __name__ == "__main__":
    main()
