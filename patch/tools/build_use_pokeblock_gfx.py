"""Translate the separate Use Pokeblock title and condition graph assets."""
import struct
from pathlib import Path

from PIL import Image

from build_berry_tag_gfx import get_px, lzdec, set_px

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT.parent / 'pokeemerald_us_chs/graphics/pokeblock/use_screen'


def image_tiles(image):
    assert image.mode == 'P' and image.width % 8 == image.height % 8 == 0
    output = bytearray(image.width * image.height // 2)
    for y in range(image.height):
        for x in range(image.width):
            value = image.getpixel((x, y))
            assert 0 <= value < 16
            set_px(output, y // 8 * (image.width // 8) + x // 8,
                   x % 8, y % 8, value)
    return bytes(output)


def palette(rom, offset):
    return [channel for c in struct.unpack_from('<16H', rom, offset)
            for channel in ((c & 31) * 255 // 31,
                            (c >> 5 & 31) * 255 // 31,
                            (c >> 10 & 31) * 255 // 31)]


def map_pixel(tiles, entry, x, y):
    return get_px(tiles, (entry & 1023) - 0x280,
                  7 - x if entry & 0x400 else x,
                  7 - y if entry & 0x800 else y)


def cancel_tiles(rom):
    # Wokann menu_specialized.c: sConditionSelectionIconsSheets[2].
    assert struct.unpack_from('<IHH', rom, 0x5FA8D0) == (0x085F9C38, 0x100, 102)
    native = (ROOT.parent / 'pokeemerald_wokann_dev/graphics/pokenav/condition/cancel.4bpp').read_bytes()
    assert rom[0x5F9C38:0x5F9D38] == native
    native_pal = (ROOT.parent / 'pokeemerald_wokann_dev/graphics/pokenav/condition/cancel.gbapal').read_bytes()
    assert rom[0x5F9AF8:0x5F9B18] == native_pal
    image = Image.open(ROOT.parent / 'pokeemerald_us_chs/graphics/pokenav/condition/cancel.png')
    assert image.mode == 'P' and image.size == (32, 16)
    # Keep the US CANCEL pixels and frame. Native JP uses index 1 for both
    # frame and text; remap US black text (15) to that same native role.
    assert set(image.get_flattened_data()) == {0, 1, 2, 15}
    image = image.point([1 if i == 15 else i for i in range(256)])
    return image_tiles(image)



def build():
    rom = (ROOT / 'baserom_jp.gba').read_bytes()
    reference = (ROOT.parent / 'pokeemerald_wokann_dev/baserom_jp.gba').read_bytes()
    # Wokann data/data_b2d_mid70.s, resources loaded in use_pokeblock.c.
    assert rom[0x5BEBC0:0x5C0994] == reference[0x5BEBC0:0x5C0994]
    title = Image.open(SOURCE / 'condition.png')
    assert title.size == (64, 64)
    assert title.getpalette()[:48] == palette(rom, 0x5BED34)
    title_tiles = image_tiles(title)
    assert len(lzdec(rom, 0x085BEBC0)) == len(title_tiles) == 0x800

    original = lzdec(rom, 0x085BFAAC)
    original_map = struct.unpack('<640H', lzdec(rom, 0x085C0230))
    assert len(original) == 0xFA0
    image = Image.open(SOURCE / 'graph.png')
    assert image.size == (128, 104)
    source_tiles = image_tiles(image)
    source_map = struct.unpack('<640H', (SOURCE / 'graph.bin').read_bytes())
    # Map the US artwork's color roles back to the native JP palette.
    color_map = (0, 1, 4, 15, 8, 2, 7, 9, 10, 11, 5, 12, 14, 13, 3, 6)
    # Retain unused JP tiles and the shared nature-window fill tile. Its raw
    # tilemap at 085C0410 remains untouched and must keep those tile indices.
    reserved = set(range(115, 125)) | {5}
    assert all(((v & 1023) - 0x280) in reserved
               for v in struct.unpack_from('<44H', rom, 0x5C0410))
    output = bytearray(original)
    assigned = {original[t * 32:(t + 1) * 32]: t for t in sorted(reserved)}
    available = iter(t for t in range(125) if t not in reserved)
    tilemap = bytearray()
    for i, entry in enumerate(original_map):
        tile = bytearray(32)
        for y in range(8):
            for x in range(8):
                screen_x, screen_y = i % 32 * 8 + x, i // 32 * 8 + y
                value = map_pixel(original, entry, x, y)
                # Port the inner graph and labels; retain the native JP frame,
                # striped backdrop, and blank space for the Pokemon name.
                if 100 <= screen_x < 212 and 38 <= screen_y < 134:
                    value = color_map[map_pixel(source_tiles, source_map[i], x, y)]
                set_px(tile, 0, x, y, value)
        tile = bytes(tile)
        if tile not in assigned:
            index = next(available)
            assigned[tile] = index
            output[index * 32:(index + 1) * 32] = tile
        tilemap.extend(struct.pack('<H', 0x2280 + assigned[tile]))
    assert all(output[t * 32:(t + 1) * 32] == original[t * 32:(t + 1) * 32]
               for t in reserved)
    return title_tiles, bytes(output), bytes(tilemap), cancel_tiles(rom)


def main():
    for name, data in zip(('use_pokeblock_title.4bpp', 'use_pokeblock_graph.4bpp',
                           'use_pokeblock_graph_tilemap.bin', 'condition_cancel.4bpp'), build()):
        (ROOT / 'patch/gfx' / name).write_bytes(data)


if __name__ == '__main__':
    main()
