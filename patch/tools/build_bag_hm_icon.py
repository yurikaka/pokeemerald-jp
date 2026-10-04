#!/usr/bin/env python3
"""Reuse the US HM marker bitmap with the Japanese bag palette."""

import json
import re
import struct
from pathlib import Path

from PIL import Image

from build_berry_tag_gfx import lzdec


ROOT = Path(__file__).resolve().parent.parent.parent
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"
SOURCE_ICON = ROOT.parent / "pokeemerald_us_chs/graphics/bag/hm.png"
ADDRESS = 0x085DF99C
POINTER = 0x081AB370


def position(px, py):
    return (py // 8 * 2 + px // 8) * 32 + py % 8 * 4 + px % 8 // 2


def get_pixel(data, px, py):
    return data[position(px, py)] >> (px % 2 * 4) & 15


def set_pixel(data, px, py, value):
    offset = position(px, py)
    shift = px % 2 * 4
    data[offset] = (data[offset] & ~(15 << shift)) | value << shift


def main():
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    original = rom[ADDRESS - 0x08000000:ADDRESS - 0x08000000 + 128]
    source = (REFERENCE / "src/data/item_menu_data.c").read_text()
    match = re.search(r"const u8 gUnknown_85DF99C\[\] = \{(.*?)\};", source, re.S)
    expected = bytes(int(value, 16) for value in re.findall(r"0x([0-9A-Fa-f]{2})", match[1]))
    if original != expected or struct.unpack_from("<I", rom, POINTER - 0x08000000)[0] != ADDRESS:
        raise ValueError("HM marker data or pointer differs from the Wokann reference")
    icon = Image.open(SOURCE_ICON)
    if icon.mode != "P" or icon.size != (16, 16):
        raise ValueError("Unexpected US HM marker layout")
    output = bytearray(128)
    for py in range(16):
        for px in range(16):
            value = icon.getpixel((px, py))
            if value not in (1, 10, 11, 15):
                raise ValueError("US HM marker uses an unexpected palette index")
            set_pixel(output, px, py, value)
    for py in range(16):
        for px in range(16):
            if get_pixel(output, px, py) != icon.getpixel((px, py)):
                raise ValueError("Packed HM marker differs from the US bitmap")
    (ROOT / "patch/gfx/bag_hm_icon.4bpp").write_bytes(output)
    palette = struct.unpack("<32H", lzdec(rom, 0x08D9A734))
    preview = Image.new("RGB", (32, 16))
    for side, data in enumerate((original, output)):
        for py in range(16):
            for px in range(16):
                color = palette[get_pixel(data, px, py)]
                preview.putpixel((side * 16 + px, py), tuple(((color >> shift) & 31) * 255 // 31 for shift in (0, 5, 10)))
    preview.resize((384, 192), Image.Resampling.NEAREST).save(ROOT / "build/patch/bag_hm_icon_preview.png")
    report = {"reference_data_matches": True, "reference_pointer_matches": True, "label": "HM", "size": [16, 16], "bytes": len(output), "us_bitmap_matches": True, "palette_unchanged": True}
    (ROOT / "build/patch/bag_hm_icon_verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
