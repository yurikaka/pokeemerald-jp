#!/usr/bin/env python3
"""Bake Chinese OK/Cancel labels into the mon markings menu sprite sheet.

The JP sheet at gMonMarkingsMenu_Gfx (0x08579F58) stores the OK/Cancel
text frame as tiles 9-24 with small kana glyphs (けってい/やめる).
Replace the two text lines with centered normal-font 确定/取消 glyphs
from patch/fonts/chinese_normal.png.  Tiles 0-8 (marking symbols and
cursor) are kept untouched.

Font palette mapping into the frame palette:
  0 (background) -> 1 (white), 1 (ink) -> 2 (black), 2 (shade) -> 5 (gray)
"""

from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parent.parent.parent
ROM_PATH = ROOT / "baserom_jp.gba"
FONT_PATH = ROOT / "patch/fonts/chinese_normal.png"
OUTPUT_PATH = ROOT / "patch/gfx/mon_markings_menu.4bpp"
SHEET_ADDR = 0x08579F58
SHEET_SIZE = 0x320
FRAME_TILES = 16
FRAME_FIRST_TILE = 9

LINES = (
    ((0x0B37, 4, 1), (0x034D, 16, 1)),
    ((0x0B21, 4, 17), (0x0E28, 16, 17)),
)

INK_RANGE_Y = range(1, 13)
INK_WIDTH = 12


def font_index_adjust(high: int) -> int:
    if high > 0x1B:
        high -= 1
    if high > 6:
        high -= 1
    return high - 1


def load_glyph(font: Image.Image, code: int) -> Image.Image:
    index = (font_index_adjust(code >> 8) << 8) | (code & 0xFF)
    col, row = index % 16, index // 16
    return font.crop((col * 16, row * 16, col * 16 + 16, row * 16 + 16))


def get_pixel(tiles: bytes, x: int, y: int) -> int:
    tile = (y // 8) * 4 + x // 8
    offset = tile * 32 + (y % 8) * 4 + (x % 8) // 2
    value = tiles[offset]
    return value >> 4 if x % 2 else value & 0x0F


def set_pixel(tiles: bytearray, x: int, y: int, value: int) -> None:
    tile = (y // 8) * 4 + x // 8
    offset = tile * 32 + (y % 8) * 4 + (x % 8) // 2
    if x % 2:
        tiles[offset] = (tiles[offset] & 0x0F) | (value << 4)
    else:
        tiles[offset] = (tiles[offset] & 0xF0) | value


def main() -> None:
    sheet_offset = SHEET_ADDR - 0x08000000
    sheet = bytearray(ROM_PATH.read_bytes()[sheet_offset:sheet_offset + SHEET_SIZE])
    font = Image.open(FONT_PATH)
    frame_base = FRAME_FIRST_TILE * 32
    frame = bytearray([0x11] * (FRAME_TILES * 32))

    color_map = {1: 2, 2: 5}
    for line in LINES:
        for code, x0, y0 in line:
            glyph = load_glyph(font, code)
            for dy in INK_RANGE_Y:
                for dx in range(INK_WIDTH):
                    value = color_map.get(glyph.getpixel((dx, dy)))
                    if value is not None:
                        set_pixel(frame, x0 + dx, y0 + dy, value)

    sheet[frame_base:frame_base + FRAME_TILES * 32] = frame
    OUTPUT_PATH.write_bytes(sheet)


if __name__ == "__main__":
    main()
