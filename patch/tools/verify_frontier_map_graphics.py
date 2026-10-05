"""Verify Frontier exterior resources against the Wokann Japanese layout."""

import re
import struct
from pathlib import Path

from build_berry_tag_gfx import lzdec


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"


def main():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    patched = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    headers = (REFERENCE / "data/tilesets/headers.inc").read_text()
    for symbol, directory in (
        ("gTileset_General", "primary/general"),
        ("gTileset_BattleFrontierOutsideEast", "secondary/battle_frontier_outside_east"),
        ("gTileset_BattleFrontierOutsideWest", "secondary/battle_frontier_outside_west"),
    ):
        match = re.search(rf"^{symbol}: @ (0x[0-9A-Fa-f]+)$", headers, re.M)
        if match is None:
            raise ValueError(f"Missing Wokann tileset {symbol}")
        offset = int(match[1], 16) - 0x08000000
        if base[offset:offset + 24] != patched[offset:offset + 24]:
            raise ValueError(f"Changed tileset header {symbol}")
        header = struct.unpack_from("<6I", base, offset)
        folder = REFERENCE / "data/tilesets" / directory
        for index, filename in (
            (1, "tiles.4bpp.lz"),
            (3, "metatiles.bin"),
            (4, "metatile_attributes.bin"),
        ):
            original = (folder / filename).read_bytes()
            start = header[index] - 0x08000000
            if original != base[start:start + len(original)]:
                raise ValueError(f"Wokann resource mismatch {symbol}/{filename}")
            if original != patched[start:start + len(original)]:
                raise ValueError(f"Changed map resource {symbol}/{filename}")
        if lzdec(base, header[1]) != lzdec(patched, header[1]):
            raise ValueError(f"Changed decompressed artwork {symbol}")
        print(f"{symbol}: original compressed and decompressed artwork preserved")


if __name__ == "__main__":
    main()
