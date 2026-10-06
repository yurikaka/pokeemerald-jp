"""Verify battle trainer expansion veneers and all original shared entries."""

import json
import struct
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ROM_BASE = 0x08000000


def main():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    source = (ROOT.parent / "pokeemerald_wokann_dev/src/battle_message.c").read_text()
    assert source.count('"\tb _0814F5BE\\n\\t"') == 2
    assert '"\tldr r0, _0814F51C\\n\\t"' in source
    assert '"_0814F51C: .4byte 0x0203886C\\n\\t"' in source
    assert '"_0814F5C8: .4byte 0x0203886E\\n\\t"' in source
    manifest = json.loads((ROOT / "patch/manifest.json").read_text())
    symbols = {}
    for line in subprocess.check_output([
        "arm-none-eabi-nm", "-n", str(ROOT / "build/patch/payload.elf")
    ], text=True).splitlines():
        fields = line.split()
        if len(fields) == 3:
            symbols[fields[2]] = int(fields[0], 16)
    for address, symbol in (
        (0x0814F514, "ChsBattleTrainerNameHook"),
        (0x0814F5BC, "ChsBattleTrainerClassNameHook"),
    ):
        entry = next(entry for entry in manifest["veneer_hooks"] if entry["symbol"] == symbol)
        assert int(entry["address"], 0) == address
        offset = address - ROM_BASE
        assert base[offset:offset + 8] == bytes.fromhex(entry["original"])
        assert rom[offset:offset + 8] == struct.pack("<HHI", 0x4B00, 0x4718, symbols[symbol] | 1)
        assert not any(entry["symbol"] == symbol for entry in manifest["function_hooks"])
    for address, original in ((0x0814F172, 0xE224), (0x0814F4CE, 0xE076)):
        offset = address - ROM_BASE
        assert struct.unpack_from("<H", base, offset)[0] == original
        instruction = struct.unpack_from("<H", rom, offset)[0]
        assert instruction == original - 1
        displacement = instruction & 0x7FF
        if displacement & 0x400:
            displacement -= 0x800
        assert address + 4 + displacement * 2 == 0x0814F5BC
    for address, length in ((0x0814F51C, 8), (0x0814F5C4, 24)):
        offset = address - ROM_BASE
        assert rom[offset:offset + length] == base[offset:offset + length]
    print("Trainer A/B class branches enter the veneer start; trainer B and Frontier literals remain intact")


if __name__ == "__main__":
    main()
