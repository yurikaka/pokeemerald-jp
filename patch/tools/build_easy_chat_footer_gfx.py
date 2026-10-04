#!/usr/bin/env python3
"""Replace JP baked footer labels, retaining the original frames and cursor grid."""

import ast
import json
from pathlib import Path
import re
import struct

from PIL import Image

from build_berry_fix_gfx import glyph
from build_berry_tag_gfx import lzdec
from build_texts import read_charmap


ROOT = Path(__file__).resolve().parents[2]
LAYOUTS = (
    (10, ((4, 5, "DelAll"), (11, 3, "Cancel5"), (18, 4, "Ok2"))),
    (21, ((4, 5, "DelAll"), (11, 3, "Cancel5"), (16, 4, "Ok2"), (22, 3, "Answer"))),
    (24, ((4, 5, "DelAll"), (11, 3, "Cancel5"), (16, 4, "Ok2"), (22, 4, "Quiz"))),
)


def localized_text(source, name):
    match = re.search(r'const u8 gText_' + name + r'\[\] = _\((.*?)\);', source, re.S)
    if match is None:
        raise ValueError(f"missing footer label: {name}")
    return "".join(ast.literal_eval(literal) for literal in re.findall(r'"(?:[^"\\]|\\.)*"', match[1]))


def build():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    tiles = bytearray(lzdec(base, 0x08573E84))
    tilemap = bytearray(lzdec(base, 0x085740E4))
    if len(tiles) != 43 * 32 or len(tilemap) != 2048:
        raise ValueError("unexpected JP Easy Chat window resource layout")
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    chinese = Image.open(ROOT / "patch/fonts/chinese_small.png")
    latin = Image.open(ROOT / "patch/fonts/latin_small.png")
    source = (ROOT.parent / "pokeemerald_us_chs/src/strings.c").read_text()
    labels = {}
    for row, entries in LAYOUTS:
        for column, columns, name in entries:
            text = localized_text(source, name)
            labels[name] = text
            image = Image.new("P", (columns * 8, 16), 15)
            cursor = 0
            for char in text:
                bitmap, width = glyph(char, charmap, chinese, latin)
                if cursor + width > image.width:
                    raise ValueError(f"footer label exceeds its original slot: {text}")
                for vertical in range(13):
                    for horizontal in range(width):
                        value = bitmap.getpixel((horizontal, vertical))
                        if value in (1, 2):
                            image.putpixel((cursor + horizontal, vertical + 1), 12 if value == 1 else 14)
                cursor += width
            for tile_row in range(2):
                for tile_column in range(columns):
                    tile_index = len(tiles) // 32
                    for vertical in range(8):
                        for horizontal in range(0, 8, 2):
                            left = image.getpixel((tile_column * 8 + horizontal, tile_row * 8 + vertical))
                            right = image.getpixel((tile_column * 8 + horizontal + 1, tile_row * 8 + vertical))
                            tiles.append(left | right << 4)
                    offset = ((row + tile_row) * 32 + column + tile_column) * 2
                    original = struct.unpack_from("<H", tilemap, offset)[0]
                    struct.pack_into("<H", tilemap, offset, (original & 0xF000) | tile_index)
    if len(tiles) > 0x8000:
        raise ValueError("footer tiles exceed the BG character block")
    return bytes(tiles), bytes(tilemap), labels


def main():
    tiles, tilemap, labels = build()
    output = ROOT / "build/patch"
    output.mkdir(parents=True, exist_ok=True)
    (output / "easy_chat_footer_tiles.4bpp").write_bytes(tiles)
    (output / "easy_chat_footer_map.bin").write_bytes(tilemap)
    (output / "easy_chat_footer_labels.json").write_text(json.dumps(labels, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
