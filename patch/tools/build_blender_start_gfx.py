"""Port the Chinese Berry Blender start sprite using the Japanese palette."""

import struct
from pathlib import Path

from PIL import Image

from build_berry_tag_gfx import set_px


ROOT = Path(__file__).resolve().parents[2]


def main():
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    reference = (ROOT.parent / "pokeemerald_wokann_dev/graphics/berry_blender/jp/830d794.bin").read_bytes()
    if rom[0x30D794:0x30D794 + len(reference)] != reference:
        raise ValueError("Wokann Berry Blender resources differ from the base ROM")
    # Wokann src/berry_blender.c: gUnknown_830FB48, loaded at 0807F3EC.
    if rom[0x30FB48:0x30FB50] != struct.pack("<IHH", 0x0830E5B4, 0x400, 0x303A):
        raise ValueError("Unexpected Japanese start sprite sheet")
    image = Image.open(ROOT.parent / "pokeemerald_us_chs/graphics/berry_blender/start.png")
    if image.mode != "P" or image.size != (64, 32):
        raise ValueError("Unexpected Chinese start sprite layout")
    palette = []
    for color in struct.unpack_from("<16H", rom, 0x30D974):
        palette.extend(((color & 31) * 255 // 31,
                        ((color >> 5) & 31) * 255 // 31,
                        ((color >> 10) & 31) * 255 // 31))
    if image.getpalette()[:48] != palette:
        raise ValueError("Chinese artwork does not match the Japanese sprite palette")
    output = bytearray(0x400)
    for y in range(32):
        for x in range(64):
            value = image.getpixel((x, y))
            if value > 15:
                raise ValueError("Start sprite exceeds its 4bpp palette")
            set_px(output, y // 8 * 8 + x // 8, x % 8, y % 8, value)
    (ROOT / "patch/gfx/berry_blender_start.4bpp").write_bytes(output)


if __name__ == "__main__":
    main()
