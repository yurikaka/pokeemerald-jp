#!/usr/bin/env python3
"""Test map popup centering against Wokann and the live patched ROM."""

import hashlib
import json
import subprocess
import tempfile
from pathlib import Path
import struct

from unicorn.arm_const import UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R4, UC_ARM_REG_R5, UC_ARM_REG_R6, UC_ARM_REG_R7, UC_ARM_REG_LR

from build_texts import encode_text, read_charmap
from verify_remaining_display_port import Machine, symbols


ROOT = Path(__file__).resolve().parents[2]
WOKANN = ROOT.parent / 'pokeemerald_wokann_dev'


def main():
    names = symbols('arm-none-eabi-nm')
    machine = Machine(names)
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    expected = bytes.fromhex('241aa406240e03a9')
    assert base[0xD42B0:0xD42B8] == expected
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    assert rom[0xD42B0:0xD42B4] == bytes.fromhex('004b1847')
    assert struct.unpack_from('<I', rom, 0xD42B4)[0] == names['ChsMapNamePopupPosition'] | 1
    source = WOKANN / 'src/map_name_popup.c'
    native_object = WOKANN / 'build/pokeemerald-jp/src/map_name_popup.o'
    with tempfile.TemporaryDirectory() as directory:
        binary = Path(directory) / 'popup.bin'
        subprocess.run(['arm-none-eabi-objcopy', '-O', 'binary', '-j', '.text', str(native_object), str(binary)], check=True)
        assert binary.read_bytes()[0x258:0x260] == expected
    assert 'x = (10 - textLength) << 2;' in source.read_text()
    charmap = read_charmap(ROOT / 'patch/charmap_chs.txt')
    name_address = names['ChsMapsecName201'] - 0x08000000
    map_name = encode_text('边境的小岛', charmap, False)
    assert rom[name_address:name_address + len(map_name)] == map_name
    stack = 0x03007800
    results = []
    cases = [
        ('边境的小岛', encode_text('边境的小岛', charmap, False), 60, 10),
        ('凯那市', encode_text('凯那市', charmap, False), 36, 22),
        ('101号道路', encode_text('101号道路', charmap, False), 60, 10),
        ('沙漠的地下道', encode_text('沙漠的地下道', charmap, False), 72, 4),
        ('native Japanese', bytes((1, 2, 3, 4, 5, 0xFF)), 40, 20),
    ]
    for label, text, width, position in cases:
        machine.cpu.mem_write(stack + 0xF, text)
        machine.cpu.reg_write(UC_ARM_REG_R4, 10)
        for register in (UC_ARM_REG_R5, UC_ARM_REG_R6, UC_ARM_REG_R7):
            machine.cpu.reg_write(register, 0x12345678)
        machine.call('ChsMapNamePopupPosition', (len(text) - 1,), (0x080D42B8,))
        actual = machine.cpu.reg_read(UC_ARM_REG_R4)
        assert actual == position, (label, actual, position)
        assert machine.cpu.reg_read(UC_ARM_REG_R1) == stack + 0xC
        for register in (UC_ARM_REG_R5, UC_ARM_REG_R6, UC_ARM_REG_R7):
            assert machine.cpu.reg_read(register) == 0x12345678
        assert machine.cpu.reg_read(UC_ARM_REG_LR) == 0x0203F001
        assert bytes(machine.cpu.mem_read(stack + 0xF, len(text))) == text
        assert actual + width <= 80
        results.append(dict(name=label, width=width, x=actual, fits=True))
    result = {
        'hook': '0x080D42B0',
        'native_bytes': expected.hex(),
        'wokann_source': str(source.relative_to(WOKANN)),
        'wokann_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'wokann_object': str(native_object.relative_to(WOKANN)),
        'wokann_object_sha256': hashlib.sha256(native_object.read_bytes()).hexdigest(),
        'object_section': '.text',
        'object_section_offset': '0x258',
        'cases': results,
        'registers_and_source_buffer_preserved': True,
        'gameplay_test': 'not run',
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
