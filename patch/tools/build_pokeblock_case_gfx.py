"""Replace only the baked-in JP Pokeblock Case feel label, keeping its frame."""
from pathlib import Path

from PIL import Image

from build_berry_fix_gfx import glyph
from build_berry_tag_gfx import get_px, lzdec, set_px
from build_texts import read_charmap

ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"


def build():
    # Wokann dev pokeblock.c sub_08135C88: graphics literal 08135CE4,
    # map literal 08135D04. graphics.c binds the checked compressed artwork.
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    compressed = (REFERENCE / "graphics/pokeblock/menu.png.4bpp.lz").read_bytes()
    assert rom[0xD9B4B4:0xD9B4B4 + len(compressed)] == compressed
    original = lzdec(rom, 0x08D9B4B4)
    assert len(original) == 40 * 32
    output = bytearray(original)
    # The JP map places these tiles at x=56..87, y=136..151.
    # Preserve top/bottom border colors, removing only Japanese glyph ink.
    label_tiles = (27, 28, 29, 30, 34, 35, 36, 37)
    for tile in label_tiles:
        for y in range(8):
            for x in range(8):
                if get_px(original, tile, x, y) in (9, 11):
                    set_px(output, tile, x, y, 3)
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    chinese = Image.open(ROOT / "patch/fonts/chinese_small.png")
    latin = Image.open(ROOT / "patch/fonts/latin_small.png")
    for index, char in enumerate("细腻度"):
        bitmap, advance = glyph(char, charmap, chinese, latin)
        assert advance == 10
        for y in range(13):
            for x in range(10):
                value = bitmap.getpixel((x, y))
                if value not in (1, 2):
                    continue
                px, py = 1 + index * 10 + x, 1 + y
                tile = (27 if py < 8 else 34) + px // 8
                set_px(output, tile, px % 8, py % 8, 9 if value == 1 else 11)
    assert all(original[t * 32:t * 32 + 32] == output[t * 32:t * 32 + 32]
               for t in range(40) if t not in label_tiles)
    return bytes(output)


if __name__ == "__main__":
    (ROOT / "patch/gfx/pokeblock_case.4bpp").write_bytes(build())
