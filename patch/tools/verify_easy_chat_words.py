"""Keep all Easy Chat vocabulary Japanese, including shared move/species names.

Wokann dev src/easy_chat.c GetEasyChatWord reads the original species table
at 0x0811F154, move table at 0x0811F160 and group table at 0x0811F17C.
Groups 0/21 contain species IDs, 18/19 move IDs; other groups contain
12-byte EasyChatWordInfo records (src/data/easy_chat/easy_chat_groups.h).
"""

from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[2]
ROM_BASE = 0x08000000


def main():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    rom = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()

    def word(data, address):
        return struct.unpack_from("<I", data, address - ROM_BASE)[0]

    def unchanged(address, size):
        offset = address - ROM_BASE
        assert rom[offset:offset + size] == base[offset:offset + size], hex(address)

    for address in (0x0811F154, 0x0811F160, 0x0811F17C):
        unchanged(address, 4)
    # Restore the original move-name stride (index * 8), not CHS index * 16.
    unchanged(0x0811F158, 2)
    unchanged(word(base, 0x0811F154), 412 * 6)
    unchanged(word(base, 0x0811F160), 355 * 8)
    groups = word(base, 0x0811F17C)
    unchanged(groups, 22 * 8)
    count = 0
    for group in range(22):
        address = word(base, groups + group * 8)
        size = struct.unpack_from("<H", base, groups + group * 8 - ROM_BASE + 4)[0]
        if group in (0, 18, 19, 21):
            unchanged(address, size * 2)
            continue
        unchanged(address, size * 12)
        for index in range(size):
            text = word(base, address + index * 12)
            end = base.index(0xFF, text - ROM_BASE)
            unchanged(text, end - (text - ROM_BASE) + 1)
            count += 1
    print(f"PASS: {count} ordinary Easy Chat words and all species/move vocabulary remain original Japanese")


if __name__ == "__main__":
    main()
