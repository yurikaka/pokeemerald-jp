"""Port the Chinese storage button tiles while retaining Japanese tilemaps."""

from pathlib import Path

from PIL import Image

from build_berry_tag_gfx import lzdec, set_px


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT.parent / "pokeemerald_us_chs/graphics/pokemon_storage"
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev/data/pokemon_storage/jp"


def main():
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    original = (REFERENCE / "0854BF9C.bin").read_bytes()
    if rom[0x54BF9C:0x54BF9C + len(original)] != original:
        raise ValueError("Wokann storage artwork mismatch")
    if lzdec(rom, 0x0854BDC0) != (SOURCE / "display_menu.bin").read_bytes():
        raise ValueError("Japanese and US display tilemaps differ")
    party_original = lzdec(rom, 0x0854C65C)
    party_source = (SOURCE / "party_menu.bin").read_bytes()
    if len(party_original) != 528 or len(party_source) != 528:
        raise ValueError("Unexpected party tilemap size")
    if party_original[:480] != party_source[:480]:
        raise ValueError("Party tilemaps differ outside the return footer")
    image = Image.open(SOURCE / "menu.png")
    if image.mode != "P" or image.size != (128, 72):
        raise ValueError("Unexpected storage artwork layout")
    output = bytearray(len(lzdec(rom, 0x0854BF9C)))
    if len(output) != image.width * image.height // 2:
        raise ValueError("Japanese and US tile counts differ")
    for vertical in range(image.height):
        for horizontal in range(image.width):
            tile = vertical // 8 * 16 + horizontal // 8
            set_px(output, tile, horizontal % 8, vertical % 8,
                   image.getpixel((horizontal, vertical)) & 15)
    (ROOT / "patch/gfx/storage_menu.4bpp").write_bytes(output)


if __name__ == "__main__":
    main()
