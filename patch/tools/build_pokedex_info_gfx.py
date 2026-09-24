#!/usr/bin/env python3
"""Builds patch/gfx/pokedex_info_tiles.4bpp and pokedex_info_tilemap.bin.

Starts from the Japanese shared Pokedex background tileset (0x08537E8C) and
info-screen tilemap (0x08537A10), then:
  1. Appends 12 tiles (IDs 0x100-0x10B) holding 身高/体重 composited from
     patch/fonts/chinese_normal.png, replacing the baked-in たかさ/おもさ
     labels; the tilemap entries are updated accordingly.
  2. Redraws the screen-select-bar tab tiles in place with 分布/叫声/体型/返回
     (main bar) and 返回 (submenu bar, keeping the B-button icon).
  3. Overwrites tiles 0x10-0x1E (the ポケモンずかん list-screen title) with the
     宝可梦图鉴 tiles from patch/gfx/pokedex_list_title.4bpp (ported from the
     US Chinese build's graphics/pokedex/menu.png; same tile IDs and palette
     roles in both versions).
"""
import struct
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent.parent
ROM_PATH = ROOT / "pokeemerald_jp.gba"
FONT_PATH = ROOT / "patch/fonts/chinese_normal.png"
TILESET_ADDR = 0x08537E8C
TILEMAP_ADDR = 0x08537A10

# Chinese character codes from patch/charmap_chs.txt.
CHARS = {
    "身": 0x0BCB, "高": 0x0449, "体": 0x0CE6, "重": 0x10A9,
    "分": 0x03D9, "布": 0x01D7, "叫": 0x0722, "声": 0x0BD7,
    "型": 0x0E58, "返": 0x03B8, "回": 0x0565,
}

# (top-row tiles, bottom-row tiles, x offset of first char, text,
#  body color, glyph colors to erase, glyph core color, anti-alias color)
# Text uses the small font (10 px wide glyphs); x offsets center 20 px of
# text inside the tab body.
TABS = [
    ([0x32, 0x33, 0x34], [0x42, 0x43, 0x44], 2, "分布", 12, (15, 13), 15, 13),
    ([0x3A, 0x3B, 0x3C, 0x3D, 0x3E], [0x4A, 0x4B, 0x4C, 0x4D, 0x4E], 10, "叫声", 12, (15, 13), 15, 13),
    ([0x35, 0x36, 0x37, 0x38, 0x39], [0x45, 0x46, 0x47, 0x48, 0x49], 10, "体型", 12, (15, 13), 15, 13),
    ([0x5B, 0x5C, 0x5D], [0x5F, 0x2D, 0x2E], 2, "返回", 11, (15, 2), 15, 2),
    ([0x21, 0x22, 0x23], [0x24, 0x25, 0x26], 2, "返回", 7, (5, 9), 5, 9),
]

TAB_BG = 12      # tab body color
TAB_GLYPH = 15   # kana glyph core / Chinese glyph core
TAB_AA = 13      # kana glyph anti-alias / Chinese glyph anti-alias
INFO_BG = 1
INFO_GLYPH = 15
INFO_AA = 3


def lzdec(data: bytes, addr: int) -> bytes:
    off = addr - 0x08000000
    assert data[off] == 0x10
    size = struct.unpack_from("<I", data, off)[0] >> 8
    out = bytearray()
    p = off + 4
    while len(out) < size:
        flags = data[p]
        p += 1
        for _ in range(8):
            if len(out) >= size:
                break
            if flags & 0x80:
                b1, b2 = data[p], data[p + 1]
                p += 2
                n = ((b1 & 0xF) << 8 | b2) + 1
                for _ in range((b1 >> 4) + 3):
                    out.append(out[-n])
            else:
                out.append(data[p])
                p += 1
            flags = (flags << 1) & 0xFF
    return bytes(out)


def glyph_pixels(font: Image.Image, code: int):
    hi, lo = code >> 8, code & 0xFF
    if hi > 0x1B:
        hi -= 1
    if hi > 0x06:
        hi -= 1
    hi -= 1
    index = hi * 256 + lo
    col, row = index % 16, index // 16
    return font.crop((col * 16, row * 16, col * 16 + 16, row * 16 + 16)).load()


def get_px(tileset: bytes, tile: int, x: int, y: int) -> int:
    b = tileset[tile * 32 + y * 4 + x // 2]
    return (b >> 4) if x % 2 else (b & 0xF)


def set_px(tileset: bytearray, tile: int, x: int, y: int, v: int) -> None:
    i = tile * 32 + y * 4 + x // 2
    if x % 2:
        tileset[i] = (tileset[i] & 0x0F) | (v << 4)
    else:
        tileset[i] = (tileset[i] & 0xF0) | v


def draw_char(tileset: bytearray, tiles_row0, tiles_row1, block_x, font_px,
              bg, core, aa, width: int = 12, yoff: int = 2) -> None:
    # Font glyphs are 12 px wide with ink at y 1..12 inside the 16 px box.
    for fx in range(width):
        for fy in range(1, 13):
            v = font_px[fx, fy]
            if not v:
                continue
            x = block_x + fx
            y = fy + yoff
            tile = (tiles_row0 if y < 8 else tiles_row1)[x // 8]
            set_px(tileset, tile, x % 8, y % 8, core if v == 1 else aa)


def main() -> None:
    rom = ROM_PATH.read_bytes()
    tileset = bytearray(lzdec(rom, TILESET_ADDR))
    tilemap = bytearray(lzdec(rom, TILEMAP_ADDR))
    font = Image.open(FONT_PATH)

    # 1. 身高/体重 blocks appended as tiles 0x100-0x10B (3 wide x 2 tall each).
    def make_label_block(text):
        block = [[INFO_BG] * 24 for _ in range(16)]
        for i, ch in enumerate(text):
            px = glyph_pixels(font, CHARS[ch])
            for fx in range(12):
                for fy in range(1, 13):
                    v = px[fx, fy]
                    if v:
                        block[fy + 1][i * 12 + fx] = INFO_GLYPH if v == 1 else INFO_AA
        tiles = bytearray()
        for ty in range(2):
            for tx in range(3):
                for y in range(8):
                    for x in range(0, 8, 2):
                        tiles.append(block[ty * 8 + y][tx * 8 + x] | (block[ty * 8 + y][tx * 8 + x + 1] << 4))
        return tiles

    tileset += make_label_block("身高") + make_label_block("体重")

    def set_tilemap_tile(tx, ty, tid):
        struct.pack_into("<H", tilemap, (ty * 32 + tx) * 2, 0x1000 | tid)

    for i in range(6):
        set_tilemap_tile(12 + i % 3, 7 + i // 3, 0x100 + i)
        set_tilemap_tile(12 + i % 3, 9 + i // 3, 0x106 + i)

    # 2. Screen-select-bar tabs: erase the kana glyphs, then draw Chinese.
    small_font = Image.open(ROOT / "patch/fonts/chinese_small.png")
    for tops, bots, xoff, text, body, erase, core, aa in TABS:
        for tile in tops + bots:
            for y in range(8):
                for x in range(8):
                    if get_px(tileset, tile, x, y) in erase:
                        set_px(tileset, tile, x, y, body)
        for i, ch in enumerate(text):
            draw_char(tileset, tops, bots, xoff + i * 10,
                      glyph_pixels(small_font, CHARS[ch]), body, core, aa,
                      width=10, yoff=1)

    # 3. List-screen title 宝可梦图鉴 over tiles 0x10-0x1E (only referenced by
    #    the list tilemap 0x08537804).
    title = (ROOT / "patch/gfx/pokedex_list_title.4bpp").read_bytes()
    assert len(title) == 15 * 32
    tileset[0x10 * 32 : 0x1F * 32] = title

    (ROOT / "patch/gfx/pokedex_info_tiles.4bpp").write_bytes(bytes(tileset))
    (ROOT / "patch/gfx/pokedex_info_tilemap.bin").write_bytes(bytes(tilemap))
    print(f"tileset {len(tileset)} bytes, tilemap {len(tilemap)} bytes")


if __name__ == "__main__":
    main()
