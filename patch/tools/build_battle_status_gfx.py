#!/usr/bin/env python3
"""Build the Japanese battle healthbox tiles with localized status labels."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent.parent.parent
WOKANN_GFX = ROOT.parent / "pokeemerald_wokann_dev/graphics/battle_interface"
SOURCE_ICONS = ROOT.parent / "pokeemerald_us_chs/graphics/interface/status_icons.png"
TABLE_ADDRESS = 0x08C11BE4
PARTS = (
    "hpbar.4bpp",
    "expbar.4bpp",
    "status.4bpp",
    "misc.4bpp",
    "hpbar_anim.4bpp",
    "misc_frameend.4bpp",
    "ball_display.4bpp",
    "ball_caught_indicator.4bpp",
    "status2.4bpp",
    "status3.4bpp",
    "status4.4bpp",
    "healthbox_doubles_frameend.4bpp",
    "healthbox_doubles_frameend_bar.4bpp",
)
STATUS_PARTS = ("status.4bpp", "status2.4bpp", "status3.4bpp", "status4.4bpp")


def set_pixel(tiles: bytearray, tile: int, x: int, y: int, color: int) -> None:
    position = tile * 32 + y * 4 + x // 2
    shift = 4 * (x % 2)
    tiles[position] = (tiles[position] & ~(15 << shift)) | (color << shift)


def main() -> None:
    original = b"".join((WOKANN_GFX / part).read_bytes() for part in PARTS)
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    offset = TABLE_ADDRESS - 0x08000000
    if rom[offset:offset + len(original)] != original:
        raise ValueError("Wokann battle graphics do not match the Japanese ROM")

    icons = Image.open(SOURCE_ICONS)
    if icons.mode != "P" or icons.size != (32, 64):
        raise ValueError("unexpected localized status icon layout")

    output = bytearray(original)
    for part in STATUS_PARTS:
        part_offset = sum((WOKANN_GFX / name).stat().st_size for name in PARTS[:PARTS.index(part)])
        tiles = bytearray(output[part_offset:part_offset + 15 * 32])
        background = 12 + STATUS_PARTS.index(part)
        for status in range(5):
            for y in range(8):
                for x in range(1, 19):
                    set_pixel(tiles, status * 3 + x // 8, x % 8, y, background)
                for x in range(2, 19):
                    if icons.getpixel((x + 5, status * 8 + y)) == 2:
                        set_pixel(tiles, status * 3 + x // 8, x % 8, y, 2)
        output[part_offset:part_offset + len(tiles)] = tiles

    (ROOT / "patch/gfx/battle_status_tiles.4bpp").write_bytes(output)


if __name__ == "__main__":
    main()
