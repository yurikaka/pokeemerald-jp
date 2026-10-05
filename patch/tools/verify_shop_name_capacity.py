"""Check shop name-slot capacity and the three matching ROM stride patches."""

import json
from pathlib import Path

from build_texts import encode_compact_chinese_text, read_charmap


ROOT = Path(__file__).resolve().parents[2]


def main():
    definition = json.loads((ROOT / "patch/item_names.json").read_text())
    capacity = definition["stride"]
    if capacity != 16:
        raise ValueError("Shop stride no longer matches the item-name table")
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    names = [encode_compact_chinese_text(name, charmap)
             for name in definition["strings"]]
    names.append(bytes((0xF5, 0x0B, 0x21, 0x0E, 0x28, 0xFF)))
    memory = bytearray([0xA5] * (len(names) * capacity + 16))
    for index, name in enumerate(names):
        if len(name) > capacity or not name.endswith(b"\xff"):
            raise ValueError(f"Item {index} exceeds shop name capacity")
        start = index * capacity
        memory[start:start + len(name)] = name
    for index, name in enumerate(names):
        start = index * capacity
        if memory[start:start + len(name)] != name:
            raise ValueError(f"Adjacent item copy corrupted item {index}")
    if memory[-16:] != b"\xa5" * 16:
        raise ValueError("Shop name-buffer canary changed")
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    for address, expected in (
        (0x080DF490, "1021"),
        (0x080DF4B0, "1022"),
        (0x080DF4CC, "1020"),
    ):
        offset = address - 0x08000000
        if rom[offset:offset + 2] != bytes.fromhex(expected):
            raise ValueError(f"Unexpected shop stride instruction at {address:#x}")
    print(f"All {len(names) - 1} item names fit {capacity}-byte shop slots; "
          "adjacent copies, canary and ROM instructions passed")


if __name__ == "__main__":
    main()
