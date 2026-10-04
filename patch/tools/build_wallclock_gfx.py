#!/usr/bin/env python3
"""Remove baked Japanese button labels beneath localized wall-clock text."""

import struct
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent.parent
ASSETS = ROOT.parent / "pokeemerald_wokann_dev/graphics/wallclock"
OUTPUT = ROOT / "patch/gfx/wallclock.4bpp"


def main() -> None:
    source = ASSETS / "clock.png.4bpp.lz"
    compressed = source.read_bytes()
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    if rom[0x59130C:0x59130C + len(compressed)] != compressed:
        raise ValueError("Wokann wall-clock graphics do not match the Japanese ROM")
    with tempfile.TemporaryDirectory() as directory:
        unpacked = Path(directory) / "clock.4bpp"
        subprocess.run([str(ROOT / "tools/gbagfx/gbagfx"), str(source), str(unpacked)], check=True)
        graphics = bytearray(unpacked.read_bytes())
    label_tiles = set()
    for name in ("clock_start", "clock_view"):
        tilemap = (ASSETS / f"{name}.bin").read_bytes()
        tiles = {struct.unpack_from("<H", tilemap, (row * 32 + column) * 2)[0] & 0x3FF
                 for row in range(16, 18) for column in range(24, 28)} - {1}
        for index, entry in enumerate(struct.unpack(f"<{len(tilemap) // 2}H", tilemap)):
            if entry & 0x3FF in tiles:
                row, column = divmod(index, 32)
                if not (16 <= row < 18 and 24 <= column < 28):
                    raise ValueError("Wall-clock label tile is shared outside the button")
        label_tiles.update(tiles)
    for tile in label_tiles:
        start = tile * 32
        if any((value & 15) not in (9, 14, 15) or (value >> 4) not in (9, 14, 15)
               for value in graphics[start:start + 32]):
            raise ValueError("Unexpected colors in wall-clock button label")
        graphics[start:start + 32] = bytes([0x99]) * 32
    OUTPUT.write_bytes(graphics)


if __name__ == "__main__":
    main()
