"""Keep text redirects out of battle AI scripts and verify the daycare reference."""

import json
import struct
import subprocess
from pathlib import Path

from build_texts import convert_us_encoded_text


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"
ROM_BASE = 0x08000000
AI_START = 0x0828A480
AI_END = 0x0828C8D7


def main():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    source = (REFERENCE / "data/battle_ai_scripts.s").read_text()
    assert "if_effect EFFECT_SWAGGER, AI_CBM_Confuse" in source
    assert "AI_CBM_Confuse:\n\tif_status2 AI_TARGET, STATUS2_CONFUSION, Score_Minus5" in source
    dispatcher = (REFERENCE / "src/battle_ai_script_commands.c").read_text()
    assert "sBattleAICmdTable[*gUnknown_203A804]();" in dispatcher
    assert "gUnknown_203A804 = T1_READ_PTR(gUnknown_203A804 + 2);" in dispatcher
    macros = (REFERENCE / "asm/macros/battle_ai_script.inc").read_text()
    assert ".macro if_effect param0:req, param1:req\n\t.byte 0x37\n\t.byte \\param0\n\t.4byte \\param1" in macros
    assert "#define EFFECT_SWAGGER 118" in (REFERENCE / "include/constants/battle_move_effects.h").read_text()
    start, end = AI_START - ROM_BASE, AI_END - ROM_BASE
    assert rom[start:end] == base[start:end], "Battle AI scripts or their entry table were changed"
    branch = 0x0828A74D - ROM_BASE
    assert rom[branch:branch + 6] == bytes.fromhex("3776a5aa2808")
    for path in (ROOT / "patch/batches").glob("*.json"):
        document = json.loads(path.read_text())
        for entry in document.get("reference_writes", []):
            address = int(entry["address"], 0)
            original = int(entry["original"], 0)
            assert not (address < AI_END and address + 4 > AI_START), (path.name, entry)
            assert not AI_START <= original < AI_END, (path.name, entry)
    daycare = (REFERENCE / "data/scripts/day_care.inc").read_text()
    assert "msgbox Route117_Text_TakeGoodCareOfIt, MSGBOX_DEFAULT" in daycare
    assert "Route117_Text_TakeGoodCareOfIt: @ 0x08257BC6" in daycare
    batch = json.loads((ROOT / "patch/batches/071_route117.json").read_text())
    label = "Chs_Route117_Text_TakeGoodCareOfIt"
    references = [entry for entry in batch["reference_writes"] if entry["symbol"] == label]
    assert len(references) == 1
    entry = references[0]
    assert int(entry["address"], 0) == 0x08257772
    assert int(entry["original"], 0) == 0x08257BC6
    offset = 0x08257772 - ROM_BASE
    assert base[offset - 2:offset + 7] == bytes.fromhex("0f00c67b2508090425")
    symbols = {}
    for line in subprocess.check_output([
        "arm-none-eabi-nm", "-n", str(ROOT / "build/patch/payload.elf")
    ], text=True).splitlines():
        fields = line.split()
        if len(fields) == 3:
            symbols[fields[2]] = int(fields[0], 16)
    target = struct.unpack_from("<I", rom, offset)[0]
    assert target == symbols[label]
    definition = next(text for text in batch["texts"] if text["name"] == label)
    expected = convert_us_encoded_text(bytes.fromhex(definition["us_encoded_hex"]), set(), False)
    offset = target - ROM_BASE
    assert rom[offset:offset + len(expected)] == expected
    print("Battle AI script region unchanged; Swagger branch restored; daycare text redirected at its sole verified reference")


if __name__ == "__main__":
    main()
