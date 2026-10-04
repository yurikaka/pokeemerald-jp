#!/usr/bin/env python3
"""Check ROM Berry Fix graphics against the generated preview and JP diagrams."""

import json
import struct
import subprocess
from pathlib import Path

from PIL import Image

from build_berry_fix_gfx import SCENES
from build_berry_tag_gfx import lzdec


ROOT = Path(__file__).resolve().parent.parent.parent


def render(tiles, tilemap, palette):
    image = Image.new("RGB", (240, 160))
    colors = struct.unpack("<256H", palette)
    for py in range(160):
        for px in range(240):
            entry = struct.unpack_from("<H", tilemap, (py // 8 * 32 + px // 8) * 2)[0]
            tile = entry & 0x3FF
            assert (tile + 1) * 32 <= len(tiles)
            tx = 7 - px % 8 if entry & 0x400 else px % 8
            ty = 7 - py % 8 if entry & 0x800 else py % 8
            pixel = tiles[tile * 32 + ty * 4 + tx // 2] >> (tx % 2 * 4) & 15
            color = colors[(entry >> 12) * 16 + pixel]
            image.putpixel((px, py), tuple(((color >> shift) & 31) * 255 // 31 for shift in (0, 5, 10)))
    return image


def main():
    nm = subprocess.check_output(["arm-none-eabi-nm", "-n", str(ROOT / "build/patch/payload.elf")], text=True)
    table = next(int(line.split()[0], 16) for line in nm.splitlines() if line.endswith(" ChsBerryFixGraphics"))
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    base = (ROOT / "baserom_jp.gba").read_bytes()
    preview = Image.open(ROOT / "build/patch/berry_fix_preview.png").resize((480, 480), Image.Resampling.NEAREST).convert("RGB")
    assert struct.unpack_from("<I", rom, 0x1BAA80)[0] == table
    for index, (gfx, tilemap, palette, _) in enumerate(SCENES):
        pointers = struct.unpack_from("<3I", rom, table - 0x08000000 + index * 12)
        current = render(lzdec(rom, pointers[0]), lzdec(rom, pointers[1]), rom[pointers[2] - 0x08000000:pointers[2] - 0x08000000 + 512])
        expected = preview.crop((index % 2 * 240, index // 2 * 160, index % 2 * 240 + 240, index // 2 * 160 + 160))
        assert current.tobytes() == expected.tobytes(), f"scene {index}: compressed ROM differs from preview"
        original = render(lzdec(base, gfx), lzdec(base, tilemap), base[palette - 0x08000000:palette - 0x08000000 + 512])
        rectangles = [(6, 87, 234, 155)]
        if index == 1:
            rectangles.append((80, 0, 160, 15))
        elif index < 5:
            rectangles.extend(((20, 68, 112, 82), (138, 68, 232, 82)))
        else:
            rectangles.append((22, 32, 218, 52))
        for py in range(160):
            for px in range(240):
                if not any(left <= px < right and top <= py < bottom for left, top, right, bottom in rectangles):
                    assert current.getpixel((px, py)) == original.getpixel((px, py)), f"scene {index}: changed diagram pixel {px},{py}"
    result = {"scenes": 6, "compressed_rom_matches_preview": True, "unchanged_pixels_outside_text_rectangles": True, "tile_bounds": True, "gameplay_test": "not run"}
    (ROOT / "build/patch/berry_fix_verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
