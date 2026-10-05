"""Check trade text pointers, display hooks, sprite sizes and source evidence."""

import json
import struct
import subprocess
from pathlib import Path

from build_texts import convert_us_encoded_text, encode_text, read_charmap


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"


def main():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    symbols = {}
    for line in subprocess.check_output([
        "arm-none-eabi-nm", "-n", str(ROOT / "build/patch/payload.elf")
    ], text=True).splitlines():
        fields = line.split()
        if len(fields) == 3:
            symbols[fields[2]] = int(fields[0], 16)
    source = (REFERENCE / "src/data/trade.h").read_text()
    assert "[MSG_STANDBY]                    = sText_CommunicationStandby" in source
    assert "[TEXT_JP_QUIT]      = sJPText_PressBButtonToQuit" in source
    functions = (REFERENCE / "src/trade.c").read_text()
    assert "static void PrintPartyMonNickname(u8 whichParty, u8 windowIdOffset, u8 *nickname)" in functions
    assert "void DrawBottomRowText(const u8 *str, u8 *dest, u8 width)" in functions
    batch = json.loads((ROOT / "patch/batches/498_trade_menu_followup.json").read_text())
    for entry in batch["reference_writes"]:
        offset = int(entry["address"], 0) - 0x08000000
        assert struct.unpack_from("<I", base, offset)[0] == int(entry["original"], 0)
        assert struct.unpack_from("<I", rom, offset)[0] == symbols[entry["symbol"]]
    standby = next(entry for entry in batch["texts"] if entry["name"] == "Chs_TradeMenuCommunicationStandby")
    expected = convert_us_encoded_text(bytes.fromhex(standby["us_encoded_hex"]), set(), False)
    offset = symbols[standby["name"]] - 0x08000000
    assert rom[offset:offset + len(expected)] == expected
    cannot_trade = next(entry for entry in batch["texts"] if entry["name"] == "Chs_TradeMenuCannotTradeNow")
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    expected = encode_text(cannot_trade["text"], charmap, False)
    offset = symbols[cannot_trade["name"]] - 0x08000000
    assert rom[offset:offset + len(expected)] == expected
    assert max(len(line) * 12 for line in cannot_trade["text"].splitlines()) <= 124
    moves_label = next(entry for entry in batch["texts"] if entry["name"] == "Chs_TradeMenuMovesLabel")
    expected = convert_us_encoded_text(bytes.fromhex(moves_label["us_encoded_hex"]), set(), False)
    offset = symbols[moves_label["name"]] - 0x08000000
    assert rom[offset:offset + len(expected)] == expected
    assert expected.startswith(bytes.fromhex("fc16f5f3"))
    manifest = json.loads((ROOT / "patch/manifest.json").read_text())
    checked = set()
    for category in ("function_hooks", "veneer_hooks"):
        for entry in manifest[category]:
            if entry["symbol"] not in {
                "ChsTradePartyNickname", "ChsTradeBottomText",
                "ChsTradeCancelInitial", "ChsTradeCancelReconnect",
                "ChsTradeConfirmPrompt", "ChsTradeDetailNicknameCopy",
                "ChsTradeDetailNicknamePrint",
            }:
                continue
            offset = int(entry["address"], 0) - 0x08000000
            original = bytes.fromhex(entry["original"])
            assert base[offset:offset + len(original)] == original
            target_offset = offset + (12 if category == "function_hooks" else 4)
            assert struct.unpack_from("<I", rom, target_offset)[0] == symbols[entry["symbol"]] | 1
            checked.add(entry["symbol"])
    assert len(checked) == 7
    for name, symbol, size in (
        ("Cancel", "ChsTradeCancelTiles", 256),
        ("ChooseAPkmn", "ChsTradeChooseTiles", 1536),
        ("CancelTrade", "ChsTradeCancelTradeTiles", 1536),
        ("PressBToQuit", "ChsTradeQuitTiles", 1536),
        ("IsThisTradeOkay", "ChsTradeConfirmTiles", 1536),
    ):
        data = (ROOT / f"build/patch/trade_label_{name}.4bpp").read_bytes()
        assert len(data) == size and any(data)
        assert all(value & 15 in (0, 14, 15) and value >> 4 in (0, 14, 15) for value in data)
        offset = symbols[symbol] - 0x08000000
        assert rom[offset:offset + size] == data
        if name == "Cancel":
            occupied_rows = []
            for tile_y in range(2):
                for vertical in range(8):
                    if any(data[(tile_y * 4 + tile_x) * 32 + vertical * 4 + horizontal]
                           for tile_x in range(4) for horizontal in range(4)):
                        occupied_rows.append(tile_y * 8 + vertical)
            assert min(occupied_rows) == 15 - max(occupied_rows)
    assert rom[0x2EA31C:0x2EA31C + 412 * 6] == base[0x2EA31C:0x2EA31C + 412 * 6]
    print("Trade message pointers, seven display hooks, sprite layouts and original species table passed")


if __name__ == "__main__":
    main()
