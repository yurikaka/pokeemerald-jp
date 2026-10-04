#!/usr/bin/env python3
"""Verify v2 display resources without claiming emulator gameplay coverage."""

import json
import struct
from pathlib import Path

from build_easy_chat_footer_gfx import LAYOUTS, build
from build_berry_tag_gfx import lzdec
from verify_v2_audit import Verification, WOKANN, digest


ROOT = Path(__file__).resolve().parents[2]


def main():
    verification = Verification('arm-none-eabi-nm')
    tiles, tilemap, labels = build()
    original_tiles = lzdec(verification.base, 0x08573E84)
    original_map = lzdec(verification.base, 0x085740E4)
    assert tiles[:len(original_tiles)] == original_tiles
    changed_cells = set()
    for row, entries in LAYOUTS:
        for column, columns, name in entries:
            for vertical in range(2):
                for horizontal in range(columns):
                    changed_cells.add((row + vertical) * 32 + column + horizontal)
    for cell in range(1024):
        original = struct.unpack_from('<H', original_map, cell * 2)[0]
        current = struct.unpack_from('<H', tilemap, cell * 2)[0]
        if cell not in changed_cells:
            assert original == current, cell
        else:
            assert current & 0xF000 == original & 0xF000, cell
            assert current & 0xC00 == 0, cell
        assert (current & 0x3FF) * 32 < len(tiles), cell
    for pointer, symbol, expected in (
        (0x0811C944, 'ChsEasyChatFooterTiles', tiles),
        (0x0811C948, 'ChsEasyChatFooterMap', tilemap),
    ):
        address = verification.word(pointer)
        assert address == verification.symbols[symbol]
        assert lzdec(verification.rom, address) == expected
    suffix = verification.payload('Chs_V2_gText_ApostropheSBase')
    prefix = verification.payload('Chs_V2_gText_NatureSlash')
    for proof in (suffix, prefix):
        address = int(proof['payload_address'], 0) - 0x08000000
        assert verification.rom[address:address + 2] == bytes((0xF5, 0xF1))
        assert verification.rom[address + 3] == 0xFF
    sizes = []
    for index in range(25):
        proof = verification.payload(f'ChsNatureName{index}')
        offset = int(proof['payload_address'], 0) - 0x08000000
        size = verification.rom.index(0xFF, offset) - offset + 1
        assert 3 + size <= 14, (index, size)
        sizes.append(3 + size)
    batch = json.loads((ROOT / 'patch/batches/496_v2_verified_display_consumers.json').read_text())
    references = json.loads((ROOT / 'patch/mapping_reports/wokann_object_reference_verification.json').read_text())['references']
    typed = {(int(entry['address'], 0), int(entry['original'], 0)): entry for entry in references}
    for reference in batch['reference_writes']:
        key = (int(reference['address'], 0), int(reference['original'], 0))
        proof = typed[key]
        assert digest(WOKANN / proof['object']) == proof['object_sha256']
        assert verification.word(key[0], base=True) == key[1]
        assert verification.word(key[0]) == verification.symbols[reference['symbol']]
    print(json.dumps({
        'footer_labels': labels,
        'original_tiles_preserved': True,
        'unchanged_map_outside_text_slots': True,
        'original_palettes_preserved': True,
        'compact_suffix': suffix,
        'nature_buffer_max_bytes': max(sizes),
        'nature_buffer_capacity': 14,
        'typed_new_text_references': len(batch['reference_writes']),
        'gameplay_test': 'not run',
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
