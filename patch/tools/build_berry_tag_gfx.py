#!/usr/bin/env python3
"""Remove the baked-in Japanese flavor labels from the Berry Tag background."""

import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent.parent
ROM_PATH = ROOT / "baserom_jp.gba"
TILESET_ADDR = 0x08D9BD90
LABEL_TILES = (
    (0x21, 0x22, 0x23),
    (0x24, 0x25, 0x23),
    (0x1C, 0x1D, 0x23),
    (0x1E, 0x1F, 0x23),
    (0x31, 0x32, 0x33),
)
LABEL_MARK_TILES = (0x30, 0x34, 0x35)


def lzdec(data: bytes, addr: int) -> bytes:
    offset = addr - 0x08000000
    if data[offset] != 0x10:
        raise ValueError(f"expected LZ77 data at 0x{addr:08X}")
    size = struct.unpack_from("<I", data, offset)[0] >> 8
    output = bytearray()
    position = offset + 4
    while len(output) < size:
        flags = data[position]
        position += 1
        for _ in range(8):
            if len(output) >= size:
                break
            if flags & 0x80:
                first, second = data[position:position + 2]
                position += 2
                length = (first >> 4) + 3
                distance = ((first & 0x0F) << 8 | second) + 1
                for _ in range(length):
                    output.append(output[-distance])
            else:
                output.append(data[position])
                position += 1
            flags = (flags << 1) & 0xFF
    return bytes(output)


def get_px(tileset: bytes, tile: int, x: int, y: int) -> int:
    value = tileset[tile * 32 + y * 4 + x // 2]
    return value >> 4 if x % 2 else value & 0x0F


def set_px(tileset: bytearray, tile: int, x: int, y: int, value: int) -> None:
    offset = tile * 32 + y * 4 + x // 2
    if x % 2:
        tileset[offset] = (tileset[offset] & 0x0F) | value << 4
    else:
        tileset[offset] = (tileset[offset] & 0xF0) | value


def main() -> None:
    tileset = bytearray(lzdec(ROM_PATH.read_bytes(), TILESET_ADDR))
    if len(tileset) != 90 * 32:
        raise ValueError("unexpected Japanese Berry Tag tileset size")
    for label in LABEL_TILES + (LABEL_MARK_TILES,):
        for tile in label:
            for y in range(8):
                for x in range(8):
                    if get_px(tileset, tile, x, y) in (8, 11):
                        set_px(tileset, tile, x, y, 3)
    (ROOT / "patch/gfx/berry_tag_tiles.4bpp").write_bytes(tileset)


if __name__ == "__main__":
    main()
