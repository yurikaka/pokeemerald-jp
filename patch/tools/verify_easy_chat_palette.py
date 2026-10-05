"""Verify the shared Easy Chat background palette and footer color usage."""

import re
import struct
from pathlib import Path

from build_easy_chat_footer_gfx import FOOTER_TILE_START, LAYOUTS, build
from build_berry_tag_gfx import lzdec


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"


def main():
    reference = (REFERENCE / "src/easy_chat.c").read_text()
    loader = reference.split("void LoadEasyChatPalettes(void)", 1)[1]
    assert "_0811D868: .4byte gEasyChatMode_Pal" in loader
    assert re.search(r"movs r1, #0.*?movs r2, #0x20.*?bl LoadPalette", loader, re.S)
    graphics = (REFERENCE / "src/graphics.c").read_text()
    assert 'gEasyChatMode_Pal[] = INCBIN_U16("graphics/easy_chat/mode.png.gbapal")' in graphics
    base = (ROOT / "baserom_jp.gba").read_bytes()
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    pointer_offset = 0x0811D868 - 0x08000000
    address = struct.unpack_from("<I", rom, pointer_offset)[0]
    assert address == struct.unpack_from("<I", base, pointer_offset)[0] == 0x08573E64
    offset = address - 0x08000000
    palette = base[offset:offset + 32]
    assert rom[offset:offset + 32] == palette
    assert (REFERENCE / "graphics/easy_chat/mode.png.gbapal").read_bytes() == palette
    colors = struct.unpack("<16H", palette)
    assert colors[12] == 0x39CE and colors[14] == 0x6F5B and colors[15] == 0x7FFF
    tiles, tilemap, labels = build()
    dimensions = base[0x574358:0x574358 + 9 * 4]
    window_end = 0x30 + max(dimensions[index + 1] * dimensions[index + 2]
                            for index in range(0, len(dimensions), 4))
    assert window_end <= FOOTER_TILE_START
    assert len(tiles) <= 0x4000
    for row, entries in LAYOUTS:
        for column, columns, name in entries:
            for vertical in range(2):
                for horizontal in range(columns):
                    cell = (row + vertical) * 32 + column + horizontal
                    tile = struct.unpack_from("<H", tilemap, cell * 2)[0] & 0x3FF
                    assert FOOTER_TILE_START <= tile < 0x200
    for pointer, expected in ((0x0811C944, tiles), (0x0811C948, tilemap)):
        target = struct.unpack_from("<I", rom, pointer - 0x08000000)[0]
        assert lzdec(rom, target) == expected
    print("Original BG palette, localized footer resources and disjoint window tile ranges passed")


if __name__ == "__main__":
    main()
