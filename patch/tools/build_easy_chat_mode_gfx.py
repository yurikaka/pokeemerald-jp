"""Localize Japanese Easy Chat mode labels without replacing their frames."""

from pathlib import Path

from PIL import Image

from build_berry_fix_gfx import glyph
from build_berry_tag_gfx import get_px, lzdec, set_px
from build_texts import read_charmap


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"
LABELS = ((0, 25, "假名"), (32, 33, "分组"))


def build():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    compressed = (REFERENCE / "graphics/easy_chat/mode.png.4bpp.lz").read_bytes()
    if base[0x5737F4:0x5737F4 + len(compressed)] != compressed:
        raise ValueError("Wokann Easy Chat mode graphics differ from the Japanese ROM")
    reference = (REFERENCE / "src/easy_chat.c").read_text()
    if ".shape = SPRITE_SHAPE(64x32)" not in reference:
        raise ValueError("Unexpected mode sprite dimensions")
    original = lzdec(base, 0x085737F4)
    if len(original) != 0x1000:
        raise ValueError("Unexpected mode sprite tile count")
    output = bytearray(original)
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    chinese = Image.open(ROOT / "patch/fonts/chinese_small.png")
    latin = Image.open(ROOT / "patch/fonts/latin_small.png")
    for frame_y, left, text in LABELS:
        for vertical in range(frame_y + 14, frame_y + 29):
            for horizontal in range(left, 57):
                tile = vertical // 8 * 8 + horizontal // 8
                if get_px(original, tile, horizontal % 8, vertical % 8) in (12, 15):
                    set_px(output, tile, horizontal % 8, vertical % 8, 14)
        cursor = left + (57 - left - 20) // 2
        for char in text:
            bitmap, advance = glyph(char, charmap, chinese, latin)
            for vertical in range(13):
                for horizontal in range(advance):
                    value = bitmap.getpixel((horizontal, vertical))
                    if value in (1, 2):
                        pixel_x = cursor + horizontal
                        pixel_y = frame_y + 14 + vertical
                        tile = pixel_y // 8 * 8 + pixel_x // 8
                        set_px(output, tile, pixel_x % 8, pixel_y % 8,
                               12 if value == 1 else 15)
            cursor += advance
    return bytes(output)


def main():
    (ROOT / "patch/gfx/easy_chat_mode.4bpp").write_bytes(build())


if __name__ == "__main__":
    main()
