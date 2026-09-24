#!/usr/bin/env python3
"""Builds patch/gfx/pokedex_search_tiles.4bpp.

Starts from the Japanese Pokedex search-menu tileset (0x0854385C) and swaps
the baked-in kana button tiles for the already-localized tiles from the US
Chinese repo (graphics/pokedex/search_menu.png):
  top tabs    けんさく/きりかえ/もどる -> 检索/转换/取消
  row labels  モード/なまえ/いろ/タイプ/ならび -> 模式/名字/颜色/属性/顺序
  decide      けってい -> 确定

Both search tilemaps (0x08543DE8 national, 0x08543F84 hoenn) are byte-identical
to the US ones and the runtime palettes match, so the US tiles are copied
verbatim. All non-label tiles (frames, arrows, the unused title strip) keep
their Japanese originals.
"""
import struct
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent.parent
ROM_PATH = ROOT / "pokeemerald_jp.gba"
US_SHEET_PATH = ROOT.parent / "pokeemerald_us_chs/graphics/pokedex/search_menu.png"
TILESET_ADDR = 0x0854385C

# Label button groups: (top-row tiles, bottom-row tiles).
LABEL_GROUPS = [
    ([0x6A, 0x6B, 0x6C, 0x6D, 0x6E], [0x7A, 0x7B, 0x7C, 0x7D, 0x7E]),  # 检索
    ([0x65, 0x66, 0x67, 0x68, 0x69], [0x75, 0x76, 0x77, 0x78, 0x79]),  # 转换
    ([0x4A, 0x4B, 0x4C, 0x4D, 0x4E], [0x5A, 0x5B, 0x5C, 0x5D, 0x5E]),  # 取消
    ([0x20, 0x21, 0x22, 0x23, 0x24], [0x30, 0x31, 0x32, 0x33, 0x34]),  # 模式
    ([0x2A, 0x2B, 0x2C, 0x2D, 0x2E], [0x3A, 0x3B, 0x3C, 0x3D, 0x3E]),  # 名字
    ([0x40, 0x41, 0x42, 0x43, 0x44], [0x50, 0x51, 0x52, 0x53, 0x54]),  # 颜色
    ([0x45, 0x46, 0x47, 0x48, 0x49], [0x55, 0x56, 0x57, 0x58, 0x59]),  # 属性
    ([0x25, 0x26, 0x27, 0x28, 0x29], [0x35, 0x36, 0x37, 0x38, 0x39]),  # 顺序
    ([0x60, 0x61, 0x62, 0x63, 0x64], [0x70, 0x71, 0x72, 0x73, 0x74]),  # 确定
]


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


def sheet_tile(sheet: Image.Image, tile: int) -> bytes:
    col, row = tile % 16, tile // 16
    out = bytearray(32)
    for y in range(8):
        for x in range(0, 8, 2):
            lo = sheet.getpixel((col * 8 + x, row * 8 + y))
            hi = sheet.getpixel((col * 8 + x + 1, row * 8 + y))
            out[y * 4 + x // 2] = lo | (hi << 4)
    return bytes(out)


def main() -> None:
    rom = ROM_PATH.read_bytes()
    tileset = bytearray(lzdec(rom, TILESET_ADDR))
    assert len(tileset) == 128 * 32
    sheet = Image.open(US_SHEET_PATH)
    assert sheet.size == (128, 64)

    replaced = set()
    for tops, bots in LABEL_GROUPS:
        for tile in tops + bots:
            tileset[tile * 32:(tile + 1) * 32] = sheet_tile(sheet, tile)
            replaced.add(tile)
    assert len(replaced) == 90

    (ROOT / "patch/gfx/pokedex_search_tiles.4bpp").write_bytes(bytes(tileset))
    print(f"tileset {len(tileset)} bytes, {len(replaced)} tiles replaced")


if __name__ == "__main__":
    main()
