#!/usr/bin/env python3
"""Build 8x12 trainer-memo glyph atlases from MuzaiPixel MZPXorig.ttf."""

import argparse
import json
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageFont

from build_texts import SYNTHETIC_PUNCTUATION, read_charmap


ROOT = Path(__file__).resolve().parent.parent.parent
MEMO_TEXT = "的性格，好像在遇见了当时的它孵化了通过交换某个地方"


def glyph_index(encoded: bytes) -> int:
    high, low = encoded
    if high > 0x1B:
        high -= 1
    if high > 0x06:
        high -= 1
    return (high - 1) * 256 + low


def draw_glyph(atlas: Image.Image, font: ImageFont.FreeTypeFont, char: str, index: int) -> None:
    bounds = font.getbbox(char)
    if bounds is None:
        raise ValueError(f"missing font glyph: {char}")
    mask = font.getmask(char)
    if mask.size[0] > 8 or bounds[3] > 12:
        raise ValueError(f"glyph exceeds 8x12 cell: {char}")
    column, row = index % 16, index // 16
    left, top = column * 16 + bounds[0], row * 16 + bounds[1] + 1
    glyph = Image.frombytes("L", mask.size, bytes(mask)).point(lambda value: 1 if value else 0)
    atlas.paste(glyph, (left, top))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("font", type=Path)
    args = parser.parse_args()

    entries = json.loads((ROOT / "patch/batches/175_summary_info.json").read_text())["texts"]
    chars = set(MEMO_TEXT)
    for entry in entries:
        if entry["name"].startswith(("ChsNatureName", "ChsMapsecName")):
            chars.update(entry["text"])

    cmap = TTFont(args.font).getBestCmap()
    missing = sorted(char for char in chars if ord(char) not in cmap)
    if missing:
        raise ValueError(f"MuzaiPixel lacks memo characters: {''.join(missing)}")

    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    font = ImageFont.truetype(args.font, 12)
    chinese = Image.new("P", (256, 7088), 0)
    latin = Image.new("P", (256, 512), 0)
    palette = [255, 255, 255, 39, 39, 39, 128, 128, 128] + [0] * (256 * 3 - 9)
    chinese.putpalette(palette)
    latin.putpalette(palette)
    latin_widths = bytearray((8,)) * 256

    for char in sorted(chars | SYNTHETIC_PUNCTUATION):
        encoded = charmap.get(char)
        if encoded is None:
            continue
        if char in SYNTHETIC_PUNCTUATION and len(encoded) == 1:
            draw_glyph(latin, font, char, encoded[0])
            latin_widths[encoded[0]] = max(1, min(8, round(font.getlength(char))))
        elif len(encoded) == 2 and 0x01 <= encoded[0] <= 0x1E:
            draw_glyph(chinese, font, char, glyph_index(encoded))
        elif len(encoded) == 1 and encoded[0] < 0xF0:
            draw_glyph(latin, font, char, encoded[0])
            latin_widths[encoded[0]] = max(1, min(8, round(font.getlength(char))))

    chinese.save(ROOT / "patch/fonts/muzaipixel_chinese.png")
    latin.save(ROOT / "patch/fonts/muzaipixel_latin.png")
    (ROOT / "patch/fonts/muzaipixel_latin_widths.bin").write_bytes(latin_widths)


if __name__ == "__main__":
    main()
