#!/usr/bin/env python3
"""Verify installed START-menu graphics, isolation and fixed tile capacity."""
import struct
from pathlib import Path

from build_pokedex_info_gfx import ROOT, lzdec


def pointer(rom, offset):
    return struct.unpack_from("<I", rom, offset)[0]


def main():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    gfx = lzdec(rom, pointer(rom, 0xBBD6C))
    assert gfx == (ROOT / "patch/gfx/pokedex_info_tiles.4bpp").read_bytes()
    menu_tiles = set()
    reference = ROOT.parent / "pokeemerald_wokann_dev/graphics/pokedex"
    for name, offset, count in (("main", 0xBBD78, 4), ("search_results", 0xBBDA4, 5)):
        original = lzdec(base, pointer(base, offset))
        assert original == (reference / f"start_menu_{name}.bin").read_bytes()
        patched = lzdec(rom, pointer(rom, offset))
        assert patched == (ROOT / f"patch/gfx/pokedex_start_menu_{name}.bin").read_bytes()
        assert len(patched) == len(original)
        changed = 0
        for i, (entry,) in enumerate(struct.iter_unpack("<H", patched)):
            y, x = divmod(i, 32)
            assert entry & 0x3FF < 256  # runtime loads the original 8 KiB
            if 1 <= y <= count * 2 and 19 <= x < 28:
                assert entry >> 12 == 2
                if entry & 0x3FF != 0xB5:
                    menu_tiles.add(entry & 0x3FF)
                changed += patched[i * 2:i * 2 + 2] != original[i * 2:i * 2 + 2]
            else:
                assert patched[i * 2:i * 2 + 2] == original[i * 2:i * 2 + 2]
        assert changed
        print(f"{name}: installed ROM graphics/map, frame and cursor columns verified")
    assert len(menu_tiles) == 36
    for name in ("list", "list_underlay", "info_screen", "cry_screen", "size_screen",
                 "screen_select_bar_main", "screen_select_bar_submenu"):
        data = (reference / f"{name}.bin").read_bytes()
        used = {entry & 0x3FF for entry, in struct.iter_unpack("<H", data)}
        assert not menu_tiles & used, (name, menu_tiles & used)
    print("36 menu text tiles isolated from other Pokedex screens; tile budget preserved")


if __name__ == "__main__":
    main()
