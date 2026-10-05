"""Pre-render trade sprite labels without splitting multibyte text."""

import ast
import re
from pathlib import Path

from PIL import Image

from build_berry_fix_gfx import glyph
from build_texts import read_charmap


ROOT = Path(__file__).resolve().parents[2]


def build_label(text, width, center_vertical=False):
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    chinese = Image.open(ROOT / "patch/fonts/chinese_normal.png")
    latin = Image.open(ROOT / "patch/fonts/latin_normal.png")
    image = Image.new("P", (width, 16), 0)
    cursor = 0
    for char in text:
        bitmap, advance = glyph(char, charmap, chinese, latin)
        if len(charmap[char]) == 2:
            advance = 12
        if cursor + advance > width:
            raise ValueError(f"trade sprite label exceeds {width}px: {text}")
        for vertical in range(16):
            for horizontal in range(advance):
                value = bitmap.getpixel((horizontal, vertical))
                if value in (1, 2):
                    image.putpixel((cursor + horizontal, vertical), 15 if value == 1 else 14)
        cursor += advance
    if center_vertical:
        bounds = image.getbbox()
        if bounds is not None:
            top, bottom = bounds[1], bounds[3]
            centered = Image.new("P", image.size, 0)
            centered.paste(image, (0, (16 - (bottom - top)) // 2 - top))
            image = centered
    output = bytearray()
    for sprite_x in range(0, width, 32):
        for tile_y in range(2):
            for tile_x in range(4):
                for vertical in range(8):
                    for horizontal in range(0, 8, 2):
                        left = image.getpixel((sprite_x + tile_x * 8 + horizontal, tile_y * 8 + vertical))
                        right = image.getpixel((sprite_x + tile_x * 8 + horizontal + 1, tile_y * 8 + vertical))
                        output.append(left | right << 4)
    return bytes(output)


def main():
    source = (ROOT.parent / "pokeemerald_us_chs/src/data/trade.h").read_text()
    output = ROOT / "build/patch"
    output.mkdir(parents=True, exist_ok=True)
    for name, width in (("Cancel", 32), ("ChooseAPkmn", 192), ("CancelTrade", 192), ("IsThisTradeOkay", 192)):
        match = re.search(r"sText_" + name + r'\[\] = _\((".*?")\);', source)
        if match is None:
            raise ValueError(f"missing US trade label: {name}")
        text = ast.literal_eval(match[1])
        (output / f"trade_label_{name}.4bpp").write_bytes(build_label(text, width, name == "Cancel"))
    (output / "trade_label_PressBToQuit.4bpp").write_bytes(build_label("B键：返回", 192))


if __name__ == "__main__":
    main()
