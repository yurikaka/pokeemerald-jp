"""Draw type and contest icons with the game's standard Chinese small font."""

from pathlib import Path

from PIL import Image

from build_berry_fix_gfx import glyph
from build_berry_tag_gfx import get_px, lzdec, set_px
from build_texts import read_charmap


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"
LABELS = (
    "一般", "格斗", "飞行", "毒", "地面", "岩石", "虫", "幽灵", "钢", None,
    "火", "水", "草", "电", "超能力", "冰", "龙", "恶",
    "帅气", "美丽", "可爱", "聪明", "强壮",
)


def build():
    # Wokann dev pokemon_summary_screen.c: sSpriteSheet_MoveTypes and
    # sSpriteAnimTable_MoveTypes use 23 consecutive 32x16, eight-tile sprites.
    # Its three palette banks share text ink 15 and shadow 14.
    base = (ROOT / "baserom_jp.gba").read_bytes()
    compressed = (REFERENCE / "graphics/types/move_types.4bpp.lz").read_bytes()
    assert base[0xD971CC:0xD971CC + len(compressed)] == compressed
    original = lzdec(base, 0x08D971CC)
    assert len(original) == len(LABELS) * 256
    output = bytearray(original)
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    chinese = Image.open(ROOT / "patch/fonts/chinese_small.png")
    latin = Image.open(ROOT / "patch/fonts/latin_small.png")
    for index, label in enumerate(LABELS):
        if label is None:  # Preserve the original ??? icon byte for byte.
            continue
        background = get_px(original, index * 8 + 6, 0, 4)
        for y in range(16):
            for x in range(32):
                tile = index * 8 + y // 8 * 4 + x // 8
                if get_px(original, tile, x % 8, y % 8) in (14, 15):
                    set_px(output, tile, x % 8, y % 8, background)
        text = Image.new("L", (len(label) * 10 + 6, 16))
        for column, char in enumerate(label):
            bitmap, advance = glyph(char, charmap, chinese, latin)
            assert advance == 10
            for y in range(16):
                for x in range(16):
                    value = bitmap.getpixel((x, y))
                    if value in (1, 2):
                        text.putpixel((column * 10 + x, y), 15 if value == 1 else 14)
        text = text.crop(text.getbbox())
        assert text.width <= 30 and text.height <= 10, label
        left, top = (32 - text.width) // 2, (16 - text.height) // 2
        for y in range(text.height):
            for x in range(text.width):
                value = text.getpixel((x, y))
                if value:
                    px, py = left + x, top + y
                    tile = index * 8 + py // 8 * 4 + px // 8
                    set_px(output, tile, px % 8, py % 8, value)
        # All frame pixels, including their transparent corners, stay intact.
        for y in (0, 1, 2, 13, 14, 15):
            for x in range(32):
                tile = index * 8 + y // 8 * 4 + x // 8
                value = get_px(original, tile, x % 8, y % 8)
                if value not in (14, 15):
                    assert get_px(output, tile, x % 8, y % 8) == value
    assert output[9 * 256:10 * 256] == original[9 * 256:10 * 256]
    return bytes(output)


if __name__ == "__main__":
    (ROOT / "patch/gfx/move_types.4bpp").write_bytes(build())
