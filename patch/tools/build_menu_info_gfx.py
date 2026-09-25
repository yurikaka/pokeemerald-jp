#!/usr/bin/env python3
"""Build localized TM/HM move-info label graphics from the US Chinese sheet."""

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent.parent
ROM_PATH = ROOT / "baserom_jp.gba"
OUTPUT_PATH = ROOT / "patch/gfx/menu_info_tiles.4bpp"
MENU_INFO_ADDR = 0x085D7C38
SHEET_WIDTH = 128
TYPE_ICONS = (
    0x20, 0x64, 0x60, 0x80, 0x48, 0x44, 0x6C, 0x68, 0x88,
    0xA4, 0x24, 0x28, 0x2C, 0x40, 0x84, 0x4C, 0xA0, 0x8C,
)
LABELS = (
    0xA8,
    0xC0,
    0xC8,
    0xE0,
)


def set_pixel(tiles: bytearray, x: int, y: int, value: int) -> None:
    tile = (y // 8) * (SHEET_WIDTH // 8) + x // 8
    offset = tile * 32 + (y % 8) * 4 + (x % 8) // 2
    if x % 2:
        tiles[offset] = (tiles[offset] & 0x0F) | (value << 4)
    else:
        tiles[offset] = (tiles[offset] & 0xF0) | value


def get_pixel(tiles: bytes, x: int, y: int) -> int:
    tile = (y // 8) * (SHEET_WIDTH // 8) + x // 8
    offset = tile * 32 + (y % 8) * 4 + (x % 8) // 2
    value = tiles[offset]
    return value >> 4 if x % 2 else value & 0x0F


def copy_label(tiles: bytearray, us_tiles: bytes, tile_offset: int) -> None:
    x_start = (tile_offset % (SHEET_WIDTH // 8)) * 8
    y_start = (tile_offset // (SHEET_WIDTH // 8)) * 8
    for y in range(y_start, y_start + 12):
        for x in range(42):
            set_pixel(tiles, x_start + x, y, get_pixel(us_tiles, x_start + x, y))


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} US_MENU_INFO_4BPP")
    tiles = bytearray(ROM_PATH.read_bytes()[MENU_INFO_ADDR - 0x08000000:MENU_INFO_ADDR - 0x08000000 + 0x2000])
    us_tiles = Path(sys.argv[1]).read_bytes()
    assert len(us_tiles) == 0x2000

    for tile_offset in TYPE_ICONS:
        x_start = (tile_offset % (SHEET_WIDTH // 8)) * 8
        y_start = (tile_offset // (SHEET_WIDTH // 8)) * 8
        for y in range(y_start, y_start + 12):
            for x in range(x_start, x_start + 32):
                set_pixel(tiles, x, y, get_pixel(us_tiles, x, y))

    for tile_offset in LABELS:
        copy_label(tiles, us_tiles, tile_offset)

    OUTPUT_PATH.write_bytes(tiles)
    print(f"menu info tiles {len(tiles)} bytes")


if __name__ == "__main__":
    main()
