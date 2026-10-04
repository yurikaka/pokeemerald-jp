#!/usr/bin/env python3
"""Exercise display-only name helpers in Unicorn; this is not a game test."""

import argparse
import json
import struct
import subprocess
from pathlib import Path

from unicorn import Uc, UC_ARCH_ARM, UC_HOOK_CODE, UC_MODE_THUMB
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_SP
from unicorn.arm_const import UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2, UC_ARM_REG_R3
from unicorn.arm_const import UC_ARM_REG_R4, UC_ARM_REG_R5, UC_ARM_REG_R6, UC_ARM_REG_R7


ROOT = Path(__file__).resolve().parent.parent.parent
STOP = 0x0203F000
REGISTERS = (UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2, UC_ARM_REG_R3)


def symbols(nm):
    result = {}
    for line in subprocess.check_output([nm, "-n", str(ROOT / "build/patch/payload.elf")], text=True).splitlines():
        fields = line.split()
        if len(fields) == 3:
            result[fields[2]] = int(fields[0], 16)
    return result


class Machine:
    def __init__(self, names):
        self.names = names
        self.cpu = Uc(UC_ARCH_ARM, UC_MODE_THUMB)
        for address, size in ((0, 0x4000), (0x02000000, 0x40000), (0x03000000, 0x8000), (0x04000000, 0x1000), (0x05000000, 0x1000), (0x06000000, 0x20000), (0x08000000, 0x2000000)):
            self.cpu.mem_map(address, size)
        self.cpu.mem_write(0x08000000, (ROOT / "pokeemerald_jp_chs.gba").read_bytes())
        self.stop_addresses = {STOP}
        self.capture = None
        self.cpu.hook_add(UC_HOOK_CODE, self.stop_hook)

    def stop_hook(self, cpu, address, size, unused):
        if self.capture is not None and address == 0x08199AFC:
            stack = cpu.reg_read(UC_ARM_REG_SP)
            pointer = self.word(stack + 8)
            self.capture.append({"text": self.string(pointer), "window": cpu.reg_read(UC_ARM_REG_R0), "font": cpu.reg_read(UC_ARM_REG_R1), "x": cpu.reg_read(UC_ARM_REG_R2), "y": cpu.reg_read(UC_ARM_REG_R3), "color": self.word(stack), "speed": self.word(stack + 4)})
            cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))
            return
        if address in self.stop_addresses:
            cpu.emu_stop()

    def call(self, name, args=(), stop_addresses=()):
        self.stop_addresses = {STOP, *stop_addresses}
        self.cpu.reg_write(UC_ARM_REG_SP, 0x03007800)
        self.cpu.reg_write(UC_ARM_REG_LR, STOP | 1)
        for register, value in zip(REGISTERS, args):
            self.cpu.reg_write(register, value)
        self.cpu.emu_start(self.names[name] | 1, 0, count=200000)
        end = self.cpu.reg_read(UC_ARM_REG_PC)
        if end not in self.stop_addresses:
            raise AssertionError(f"{name} exceeded its instruction budget at {end:08X}")
        return self.cpu.reg_read(UC_ARM_REG_R0)

    def word(self, address):
        return struct.unpack("<I", self.cpu.mem_read(address, 4))[0]

    def string(self, address):
        data = bytes(self.cpu.mem_read(address, 256))
        return data[:data.index(0xFF) + 1]


def verify_tokens(machine):
    printer, text = 0x02001000, 0x02002000
    cases = []
    count = machine.names["ChsDisplayResourceCount"]
    table = machine.names["ChsDisplayResourceNames"]
    for index in range(count):
        resource = machine.string(machine.word(table + index * 4))[2:-1]
        expected = []
        position = 0
        while position < len(resource):
            first = resource[position]
            pair = first == 0x7F or (0x60 <= first <= 0x7D and first not in (0x65, 0x7A))
            expected.append(("chinese", 10, 13) if pair else ("original", first))
            position += 2 if pair else 1
        machine.cpu.mem_write(printer, bytes(32) + bytes((0xA5,)) * 32)
        machine.cpu.mem_write(printer, struct.pack("<I", text))
        machine.cpu.mem_write(text, bytes((0xF5, 0xF1, index, 0x01, 0xFF)))
        seen = []
        for iteration in range(100):
            machine.cpu.reg_write(UC_ARM_REG_R4, printer + 0x14)
            machine.cpu.reg_write(UC_ARM_REG_R6, printer)
            machine.call("ChineseRenderHook", (0,), (0x080059B2, 0x08005B32, 0x0800582C))
            end = machine.cpu.reg_read(UC_ARM_REG_PC)
            if end == 0x08005B32:
                width, height = machine.cpu.mem_read(0x030030B0, 2)
                seen.append(("chinese", width, height))
            elif end == 0x0800582C:
                char = machine.cpu.reg_read(UC_ARM_REG_R3)
                if char == 0xFF:
                    break
                seen.append(("original", char))
            assert bytes(machine.cpu.mem_read(printer + 32, 32)) == bytes((0xA5,)) * 32
        else:
            raise AssertionError("compact resource renderer did not reach EOS")
        assert seen == expected + [("original", 0x01)], (index, seen, expected)
        assert machine.cpu.mem_read(printer + 0x17, 1) == b"\x00"
        cases.append(index)
    return {"resources": len(cases), "mixed_ascii": True, "japanese_continuation": True, "eos_reset": True, "printer_neighbor_canary": True}


def verify_blender(machine):
    pairs = ((0x0830F74E, "Mister"), (0x0830F754, "Laddie"), (0x0830F75A, "Lassie"), (0x0830F760, "Master"), (0x0830F766, "Dude"), (0x0830F76C, "Miss"))
    for source, name in pairs:
        machine.cpu.mem_write(0x020226C4, machine.string(source))
        before = bytes(machine.cpu.mem_read(0x020226A8, 112))
        machine.cpu.mem_write(0x03005AF8, b"\x01")
        assert machine.call("ChsResolveBlenderName", (0x020226C4,)) == machine.names["ChsRemaining_Blender" + name]
        assert bytes(machine.cpu.mem_read(0x020226A8, 112)) == before
        machine.cpu.mem_write(0x03005AF8, b"\x00")
        assert machine.call("ChsResolveBlenderName", (0x020226C4,)) == 0x020226C4
        machine.cpu.mem_write(0x03005AF8, b"\x01")
        assert machine.call("ChsResolveBlenderName", (0x020226A8,)) == 0x020226A8
    return {"local_npc_names": 6, "link_names_unchanged": True, "player_slot_unchanged": True, "name_record_canary": True}


def verify_contest(machine):
    record, nickname = 0x02039AA0, 0x02039AA2
    machine.cpu.mem_write(0x02039BC5, b"\x03")
    for index in range(96):
        original = bytes(machine.cpu.mem_read(0x08561028 + index * 64, 64))
        machine.cpu.mem_write(record, original)
        machine.cpu.mem_write(0x02039BCA, b"\x00")
        for field, kind in ((0, "Nickname"), (1, "Trainer")):
            assert machine.call("ChsContestDisplayName", (record, field)) == machine.names[f"ChsRemaining_Contest{kind}_{index}"]
        machine.cpu.mem_write(0x02003000, bytes((0xA5,)) * 64)
        machine.call("ChsCopyContestNicknameForDisplay", (0x02003000, nickname))
        expected = machine.string(machine.names[f"ChsRemaining_ContestNickname_{index}"])
        assert machine.string(0x02003000) == expected
        assert bytes(machine.cpu.mem_read(0x02003000 + len(expected), 64 - len(expected))) == bytes((0xA5,)) * (64 - len(expected))
        assert bytes(machine.cpu.mem_read(record, 64)) == original
        machine.cpu.mem_write(0x02039BCA, b"\x01")
        assert machine.call("ChsContestDisplayName", (record, 0)) == nickname
        assert machine.call("ChsContestDisplayName", (record, 1)) == record + 13
    machine.cpu.mem_write(0x02039BCA, b"\x00")
    machine.cpu.mem_write(0x02039BC5, b"\x00")
    assert machine.call("ChsContestDisplayName", (record, 0)) == nickname
    return {"opponents": 96, "fields": 192, "link_names_unchanged": True, "player_names_unchanged": True, "contest_record_canary": True, "copy_buffer_canary": True}


def verify_mail(machine):
    state = 0x02005000
    prefix = machine.string(machine.names["ChsRemaining_MailFrom"])[:-1]
    machine.capture = []
    for name in (b"\x01", b"\x01\x02\x03\x04\x05\x06\x07", b"\xBB\xBC\xBD"):
        stored = name + b"\x00\x26\x28\xFF"
        machine.cpu.mem_write(state + 0xC0, stored + bytes((0xA5,)) * (12 - len(stored)))
        before = bytes(machine.cpu.mem_read(state + 0xC0, 12))
        machine.cpu.mem_write(0x03007800, struct.pack("<II", 0x0857B100, 0))
        machine.call("ChsMailSignature", (0, state, 20, 3), (0x08121C3C,))
        captured = machine.capture[-1]
        assert captured["text"] == prefix + name + b"\xFF"
        assert (captured["window"], captured["font"], captured["x"], captured["y"], captured["color"], captured["speed"]) == (1, 1, 32, 3, 0x0857B100, 0)
        assert bytes(machine.cpu.mem_read(state + 0xC0, 12)) == before
        assert machine.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
    machine.capture = None
    return {"signatures": 3, "longest_japanese_sender": True, "signature_buffer_unchanged": True, "synchronous_render": True, "stack_restored": True}


def verify_contest_winners(machine):
    winner = 0x02008000
    destination = 0x02008100
    for index in range(96):
        source = bytes(machine.cpu.mem_read(0x08561028 + index * 64, 64))
        record = bytearray(32)
        record[8:10] = source[:2]
        record[11:22] = source[2:13]
        record[22:30] = source[13:21]
        machine.cpu.mem_write(winner, bytes(record))
        for field, kind in ((0, "Nickname"), (1, "Trainer")):
            assert machine.call("ChsContestWinnerDisplayName", (winner, field)) == machine.names[f"ChsRemaining_Contest{kind}_{index}"]
        machine.cpu.mem_write(destination, bytes((0xA5,)) * 64)
        machine.call("ChsCopyContestWinnerNicknameForDisplay", (destination, winner + 11))
        assert machine.string(destination) == machine.string(machine.names[f"ChsRemaining_ContestNickname_{index}"])
        machine.call("ChsContestPaintingTrainerName", (destination, winner), (0x0813019C,))
        assert machine.string(destination) == machine.string(machine.names[f"ChsRemaining_ContestTrainer_{index}"])
        assert machine.cpu.reg_read(UC_ARM_REG_R0) == 0x02021C68
        assert machine.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
        assert bytes(machine.cpu.mem_read(winner, 32)) == bytes(record)
    machine.cpu.mem_write(winner + 22, b"\xBB\xBC\xFF")
    assert machine.call("ChsContestWinnerDisplayName", (winner, 0)) == winner + 11
    assert machine.call("ChsContestWinnerDisplayName", (winner, 1)) == winner + 22
    return {"saved_npc_winners": 96, "nickname_and_trainer_display": True, "saved_records_unchanged": True, "custom_names_preserved": True, "painting_continuation": True}


def verify_contest_script_buffers(machine):
    record = 0x02039AA0
    machine.cpu.mem_write(0x02039BC5, b"\x03")
    machine.cpu.mem_write(0x02039BCA, b"\x00")
    machine.cpu.mem_write(machine.word(0x080F8B10), b"\x00\x00")
    machine.cpu.mem_write(machine.word(0x080F8B34), b"\x00\x00")
    machine.cpu.mem_write(machine.word(0x080F8C08), b"\x00\x01\x02\x03")
    machine.cpu.mem_write(machine.word(0x080F8C48), b"\x00\x01\x02\x03")
    cases = (("ChsBufferContestTrainerName", 0x080F8B0C, "Trainer"),
             ("ChsBufferContestWinnerTrainerName", 0x080F8C0C, "Trainer"),
             ("ChsBufferContestNickname", 0x080F8B30, "Nickname"),
             ("ChsBufferContestWinnerNickname", 0x080F8C4C, "Nickname"))
    for index in range(96):
        original = bytes(machine.cpu.mem_read(0x08561028 + index * 64, 64))
        machine.cpu.mem_write(record, original)
        for name, literal, kind in cases:
            destination = machine.word(literal)
            machine.cpu.mem_write(destination, bytes((0xA5,)) * 20)
            machine.call(name)
            expected = machine.string(machine.names[f"ChsRemaining_Contest{kind}_{index}"])
            assert machine.string(destination) == expected
            assert bytes(machine.cpu.mem_read(destination + len(expected), 20 - len(expected))) == bytes((0xA5,)) * (20 - len(expected))
            assert bytes(machine.cpu.mem_read(record, 64)) == original
    return {"script_functions": 4, "opponents_per_function": 96, "string_variable_canaries": True, "contest_records_preserved": True}


def verify_pokeblocks(machine):
    save = 0x02010000
    save_pointer = machine.word(0x08135FA4)
    machine.cpu.mem_write(save_pointer, struct.pack("<I", save))
    destination = 0x02004000
    for color in range(1, 15):
        for level in (0, 1, 99, 255):
            machine.cpu.mem_write(save + 0x848, bytes((color, level, 0, 0, 0, 0, 20, 0)))
            machine.cpu.mem_write(destination, bytes((0xA5,)) * 48)
            machine.call("ChsBuildPokeblockListName", (destination, 0))
            result = machine.string(destination)
            token = machine.string(machine.word(machine.names["ChsPokeblockNames"] + color * 4))[:-1]
            assert result.startswith(token + b"\xFC\x0D\x48\xFC\x07\x00\xF9\x05")
            assert len(result) <= 24
            assert bytes(machine.cpu.mem_read(destination + 24, 24)) == bytes((0xA5,)) * 24
            assert bytes(machine.cpu.mem_read(save + 0x848, 8)) == bytes((color, level, 0, 0, 0, 0, 20, 0))
    return {"colors": 14, "levels": [0, 1, 99, 255], "24_byte_entry_canary": True, "pokeblock_data_unchanged": True}


def verify_fixed_tables(machine):
    base = (ROOT / "baserom_jp.gba").read_bytes()
    decorations = machine.names["ChsDecorations"]
    for index in range(121):
        original = base[0x580CD0 + index * 28:0x580CD0 + (index + 1) * 28]
        current = bytes(machine.cpu.mem_read(decorations + index * 28, 28))
        assert current[0] == original[0]
        assert current[12:20] == original[12:20]
        assert current[24:28] == original[24:28]
        assert current[1:3] == b"\xF5\xF1" and current[4:12] == b"\xFF" * 8
    report = json.loads((ROOT / "patch/mapping_reports/remaining_display_port_2026-10-04.json").read_text())
    for reference in report["entries"][0]["interior_references"]:
        assert machine.word(int(reference["address"], 16)) == decorations + 1
    colors = machine.names["ChsLinkCardColorNames"]
    assert machine.word(0x080B317C) == colors
    for stars in range(1, 5):
        assert machine.string(colors + stars * 5).startswith(b"\xF5\xF1")
    assert bytes(machine.cpu.mem_read(0x0852B23F, 25)) == base[0x52B23F:0x52B23F + 25]
    return {"decoration_records": 121, "decoration_nontext_fields_preserved": True, "interior_pointers": 11, "card_colors": 4, "card_stride": 5, "original_card_data_preserved": True}


def verify_blender_stubs(machine):
    source = 0x020226C4
    machine.cpu.mem_write(source, machine.string(0x0830F74E))
    machine.cpu.mem_write(0x03005AF8, b"\x01")
    seed = 0x13572468
    machine.cpu.reg_write(UC_ARM_REG_R4, seed)
    machine.call("ChsBlenderTextPrinter", (5, source, 16, 3), (0x08083A6C,))
    assert machine.word(0x03007800 - 20) == seed
    assert machine.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800 - 52
    menu_pointer, menu = 0x02006000, 0x02006100
    machine.cpu.mem_write(menu_pointer, struct.pack("<I", menu))
    destination = menu + 0x9F
    prefix = b"\xA2\x00"
    chinese = machine.string(machine.names["ChsRemaining_BlenderMister"])
    for name, argument, base, end in (("ChsBlenderResultsNameAppend", source, 0, 0x08082FA0), ("ChsBlenderRankingNameAppend", 28, 0x020226A8, 0x08083698)):
        machine.cpu.mem_write(destination, prefix + b"\xFF")
        machine.cpu.reg_write(UC_ARM_REG_R7, menu_pointer)
        machine.call(name, (destination, argument, base), (end,))
        assert machine.string(destination) == prefix + chinese
        assert machine.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
        assert machine.cpu.reg_read(UC_ARM_REG_R0) == menu
    return {"printer_preserves_callee_saved_register": True, "results_name_append": True, "ranking_name_append": True, "continuations": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nm", default="arm-none-eabi-nm")
    args = parser.parse_args()
    machine = Machine(symbols(args.nm))
    result = {"scope": "ARM helper execution, not a full GBA emulator playthrough", "tokens": verify_tokens(machine), "blender": verify_blender(machine), "contest": verify_contest(machine), "mail": verify_mail(machine), "pokeblocks": verify_pokeblocks(machine), "blender_stubs": verify_blender_stubs(machine), "fixed_tables": verify_fixed_tables(machine)}
    result["contest_winners"] = verify_contest_winners(machine)
    result["contest_script_buffers"] = verify_contest_script_buffers(machine)
    (ROOT / "build/patch/remaining_display_execution.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
