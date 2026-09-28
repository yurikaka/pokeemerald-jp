#!/usr/bin/env python3
"""Prepare the extracted Japanese-style Chinese title art for the JP title screen."""

import subprocess
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT.parent / "old_chs_rom_images"
OUTPUT = ROOT / "patch/gfx"
BUILD = ROOT / "build/patch"
GBAGFX = ROOT / "tools/gbagfx/gbagfx"
BASE_PALETTE_ADDRESS = 0x08517B58
TITLE_CENTER_SHIFT_X = 12


def color_word(rgb):
    red, green, blue = (component >> 3 for component in rgb)
    return red | green << 5 | blue << 10


def image_colors(image):
    palette = image.getpalette()
    return [color_word(palette[index:index + 3]) for index in range(0, 768, 3)]


def tile_bytes(pixels, width, left, top):
    return bytes(pixels[(top + row) * width + left + col] for row in range(8) for col in range(8))


def compress(source, destination):
    subprocess.run((str(GBAGFX), str(source), str(destination)), check=True)


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    palette = bytearray((ROOT / "baserom_jp.gba").read_bytes()[
        BASE_PALETTE_ADDRESS - 0x08000000:BASE_PALETTE_ADDRESS - 0x08000000 + 0x120
    ])
    color_indexes = {}
    for index in range(0, len(palette), 2):
        color = int.from_bytes(palette[index:index + 2], "little")
        color_indexes.setdefault(color, index // 2)
    opaque_black = next(
        index for index in range(1, len(palette) // 2)
        if palette[index * 2:index * 2 + 2] == b"\x00\x00"
    )

    logo = Image.open(SOURCE / "title_logo.relocated.png")
    assert logo.mode == "P" and logo.size == (256, 64)
    donor_palette = (SOURCE / "title_palettes.gbapal").read_bytes()
    assert len(donor_palette) == 0x1E0
    logo_colors = [
        int.from_bytes(donor_palette[index:index + 2], "little")
        for index in range(0, len(donor_palette), 2)
    ]
    mapped_logo = bytearray(256 * 64)
    for y in range(64):
        for x in range(192):
            source_index = logo.getpixel((x, y))
            color = logo_colors[source_index]
            if color not in color_indexes:
                color_indexes[color] = len(palette) // 2
                palette.extend(color.to_bytes(2, "little"))
            mapped_logo[y * 256 + x + TITLE_CENTER_SHIFT_X] = (
                opaque_black if color == 0 and source_index else color_indexes[color]
            )
    assert len(palette) <= 0x200
    palette.extend(b"\x00" * (0x200 - len(palette)))
    (OUTPUT / "title_palette.gbapal").write_bytes(palette)

    tiles = bytearray(64)
    tile_indexes = {bytes(64): 0}
    tilemap = bytearray(32 * 32)
    for tile_y in range(8):
        for tile_x in range(26):
            tile = tile_bytes(mapped_logo, 256, tile_x * 8, tile_y * 8)
            if tile not in tile_indexes:
                tile_indexes[tile] = len(tiles) // 64
                tiles.extend(tile)
            tilemap[tile_y * 32 + tile_x] = tile_indexes[tile]
    assert len(tiles) <= 0x4000
    logo_tiles = BUILD / "title_logo.8bpp"
    logo_map = BUILD / "title_logo.bin"
    logo_tiles.write_bytes(tiles)
    logo_map.write_bytes(tilemap)
    compress(logo_tiles, OUTPUT / "title_logo.8bpp.lz")
    compress(logo_map, OUTPUT / "title_logo.bin.lz")

    banner = Image.open(SOURCE / "emerald_version.active.png")
    assert banner.mode == "P" and banner.size == (128, 32)
    banner_colors = image_colors(banner)
    banner_pixels = bytearray(128 * 32)
    for y in range(32):
        for x in range(128):
            source_index = banner.getpixel((x, y))
            color = banner_colors[source_index]
            assert color in color_indexes
            banner_pixels[y * 128 + x] = (
                opaque_black if color == 0 and source_index else color_indexes[color]
            )
    banner_tiles = bytearray()
    for block_x, tile_width in ((0, 8), (64, 4)):
        for tile_y in range(4):
            for tile_x in range(tile_width):
                banner_tiles.extend(tile_bytes(banner_pixels, 128, block_x + tile_x * 8, tile_y * 8))
    banner_tiles.extend(b"\x00" * (0x1000 - len(banner_tiles)))
    assert len(banner_tiles) == 0x1000
    banner_source = BUILD / "title_emerald.8bpp"
    banner_source.write_bytes(banner_tiles)
    compress(banner_source, OUTPUT / "title_emerald.8bpp.lz")

    print(f"title logo: {len(tiles) // 64} tiles, {len(color_indexes)} colors")


if __name__ == "__main__":
    main()
