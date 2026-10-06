"""Port only the US Chinese cancel glyphs into the Japanese Frontier Pass tiles."""

import struct
from pathlib import Path

from PIL import Image

from build_berry_tag_gfx import lzdec, set_px


ROOT = Path(__file__).resolve().parents[2]
WOKANN = ROOT.parent / "pokeemerald_wokann_dev"
US = ROOT.parent / "pokeemerald_us_chs"


def main():
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    original = (WOKANN / "graphics/frontier_pass/bg.4bpp.lz").read_bytes()
    if rom[0x5469A4:0x5469A4 + len(original)] != original:
        raise ValueError("Wokann Frontier Pass graphics differ from the native ROM")
    tiles = bytearray(lzdec(rom, 0x085469A4))
    atlas = Image.open(US / "graphics/frontier_pass/bg.png")
    if atlas.size != (128, 256) or len(tiles) != 0x4000:
        raise ValueError("Unexpected Frontier Pass tileset layout")
    for name in ("cancel", "cancel_highlighted"):
        source_map = struct.unpack("<18H", (US / f"graphics/frontier_pass/{name}.bin").read_bytes())
        target_map = struct.unpack("<12H", (WOKANN / f"graphics/frontier_pass/{name}.bin").read_bytes())
        label = Image.new("P", (72, 16))
        for index, tile in enumerate(source_map):
            horizontal, vertical = tile % 16 * 8, tile // 16 * 8
            label.paste(atlas.crop((horizontal, vertical, horizontal + 8, vertical + 8)),
                        (index % 9 * 8, index // 9 * 8))
        for vertical in range(14):
            for horizontal in range(16, 48):
                value = label.getpixel((horizontal + 8, vertical)) if 20 <= horizontal < 44 else 1
                tile = target_map[vertical // 8 * 6 + horizontal // 8]
                set_px(tiles, tile, horizontal % 8, vertical % 8, value)
    (ROOT / "patch/gfx/frontier_pass.4bpp").write_bytes(tiles)


if __name__ == "__main__":
    main()
