#!/usr/bin/env python3
"""Localize contest artwork without changing Japanese tilemap layouts."""

import struct
from pathlib import Path

from PIL import Image

from build_berry_tag_gfx import get_px, lzdec, set_px


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev/graphics/contest"
SOURCE = ROOT.parent / "pokeemerald_us_chs/graphics/contest"


def original(rom, name, address):
    compressed = (REFERENCE / name).read_bytes()
    offset = address - 0x08000000
    if rom[offset:offset + len(compressed)] != compressed:
        raise ValueError(f"Wokann resource mismatch: {name}")
    return bytearray(lzdec(rom, address))


def pixel(data, horizontal, vertical, value=None):
    tile = vertical // 8 * 16 + horizontal // 8
    if value is None:
        return get_px(data, tile, horizontal % 8, vertical % 8)
    set_px(data, tile, horizontal % 8, vertical % 8, value & 15)


def pack(image):
    output = bytearray(image.width * image.height // 2)
    for vertical in range(image.height):
        for horizontal in range(image.width):
            tile = vertical // 8 * (image.width // 8) + horizontal // 8
            set_px(output, tile, horizontal % 8, vertical % 8, image.getpixel((horizontal, vertical)) & 15)
    return output


def opaque_title_tile(tile):
    return bytes((value & 15 or 8) | ((value >> 4 or 8) << 4) for value in tile)


def main():
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    interface = original(rom, "interface.png.4bpp.lz", 0x08C17AB8)
    source = Image.open(SOURCE / "interface.png")
    for vertical in range(8, 24):
        for horizontal in range(72, 112):
            pixel(interface, horizontal, vertical, source.getpixel((horizontal, vertical)))
    for target in (0x40, 0x45, 0x4A, 0x6A, 0x8A):
        for vertical in range(16):
            for horizontal in range(40):
                value = source.getpixel((target % 16 * 8 + horizontal, target // 16 * 8 + vertical))
                pixel(interface, target % 16 * 8 + horizontal, target // 16 * 8 + vertical, value)
    (ROOT / "patch/gfx/contest_interface.4bpp").write_bytes(interface)
    original(rom, "applause.4bpp.lz", 0x08D8EAAC)
    applause = pack(Image.open(SOURCE / "applause.png"))
    if len(applause) != 0x400:
        raise ValueError("Unexpected applause sprite size")
    (ROOT / "patch/gfx/contest_applause.4bpp").write_bytes(applause)
    next_turn = original(rom, "nextturn.4bpp.lz", 0x08D8E920)
    if len(next_turn) != 0xA0:
        raise ValueError("Unexpected Japanese next-turn sprite size")
    source_next_turn = Image.open(SOURCE / "nextturn.png")
    if source_next_turn.mode != "P" or source_next_turn.size != (64, 8):
        raise ValueError("Unexpected US next-turn sprite layout")
    localized_next_turn = source_next_turn.crop((2, 0, 42, 8))
    localized_next_turn.paste(source_next_turn.crop((48, 0, 56, 8)), (32, 0))
    (ROOT / "patch/gfx/contest_next_turn.4bpp").write_bytes(pack(localized_next_turn))
    results = original(rom, "results_screen/tiles.4bpp.lz", 0x08C196CC)
    if results[0x10 * 32:0x11 * 32] != bytes([0x88]) * 32:
        raise ValueError("Unexpected Japanese title background color")
    source_tiles = pack(Image.open(SOURCE / "results_screen/tiles.png"))
    slots = list(range(1, 16)) + list(range(17, 64)) + list(range(178, 256))
    for filename in ("bg.bin.lz", "interface.bin.lz", "winner_banner.bin.lz"):
        tilemap = lzdec((REFERENCE / "results_screen" / filename).read_bytes(), 0x08000000)
        used = {entry & 0x3FF for entry in struct.unpack(f"<{len(tilemap) // 2}H", tilemap)}
        if used.intersection(slots):
            raise ValueError(f"Title tiles overlap the results interface: {filename}")
    available = iter(slots)
    labels = (("normal", 8, 0x08569334), ("super", 8, 0x08569354),
              ("hyper", 8, 0x08569374), ("master", 8, 0x08569394),
              ("link", 8, 0x085693B4), ("cool", 5, 0x085693D4),
              ("beauty", 5, 0x085693E8), ("cute", 5, 0x085693FC),
              ("smart", 5, 0x08569410), ("tough", 5, 0x08569424),
              ("title", 5, 0x08569438))
    for name, columns, address in labels:
        path = SOURCE / "results_screen" / ("title.bin" if name == "title" else f"title_{name}.bin")
        entries = struct.unpack(f"<{path.stat().st_size // 2}H", path.read_bytes())
        source_columns = len(entries) // 2
        target_entries = []
        for row in range(2):
            for column in range(columns):
                target = next(available)
                if name == "title":
                    source_column = column + 4
                else:
                    source_column = column
                if source_column < source_columns:
                    source_tile = entries[row * source_columns + source_column] & 0x3FF
                    results[target * 32:(target + 1) * 32] = source_tiles[source_tile * 32:(source_tile + 1) * 32]
                else:
                    results[target * 32:(target + 1) * 32] = bytes(32)
                results[target * 32:(target + 1) * 32] = opaque_title_tile(results[target * 32:(target + 1) * 32])
                target_entries.append(target)
        if name == "title":
            for row in range(2):
                for vertical in range(8):
                    for horizontal in range(2):
                        set_px(results, target_entries[row * columns], horizontal, vertical, 8)
        (ROOT / f"patch/gfx/contest_title_{name}.bin").write_bytes(struct.pack(f"<{len(target_entries)}H", *target_entries))
    (ROOT / "patch/gfx/contest_results.4bpp").write_bytes(results)


if __name__ == "__main__":
    main()
