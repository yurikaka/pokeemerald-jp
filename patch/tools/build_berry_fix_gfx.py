#!/usr/bin/env python3
"""Localize the six JP Berry Fix screens without changing their loader."""

import ast
import json
import re
import struct
from pathlib import Path

from PIL import Image

from build_berry_tag_gfx import lzdec
from build_texts import read_charmap


ROOT = Path(__file__).resolve().parent.parent.parent
US = ROOT.parent / "pokeemerald_us_chs"
WOKANN = ROOT.parent / "pokeemerald_wokann_dev"
SCENES = (
    (0x085E2A20, 0x085E3610, 0x085E29E0, "EnsureGBAConnectionMatches"),
    (0x085E3990, 0x085E4494, 0x085E3930, "TurnOffPowerHoldingStartSelect"),
    (0x085E47D0, 0x085E50D8, 0x085E4790, "TransmittingPleaseWait"),
    (0x085E539C, 0x085E5BCC, 0x085E535C, "PleaseFollowInstructionsOnScreen"),
    (0x085E5E68, 0x085E674C, 0x085E5E28, "TransmissionFailureTryAgain"),
    (0x085E69E8, 0x085E707C, 0x085E69A8, "BerryProgramWillBeUpdatedPressA"),
)


def source_text(source, name):
    match = re.search(r"static const u8 sText_" + name + r"\[\] = _\((.*?)\);", source, re.S)
    if match is None:
        raise ValueError(f"missing US Berry Fix text: {name}")
    return "".join(ast.literal_eval(part) for part in re.findall(r'"(?:[^"\\]|\\.)*"', match[1]))


def glyph(char, charmap, chinese, latin):
    encoded = charmap[char]
    if len(encoded) == 2:
        high, low = encoded
        high -= high > 0x1B
        high -= high > 6
        index = (high - 1) * 256 + low
        atlas = chinese
        width = 10
    elif len(encoded) == 1:
        index = encoded[0]
        atlas = latin
        width = 10 if char in "，。！？：；、…·" else 6
    else:
        raise ValueError(f"unsupported Berry Fix glyph: {char}")
    image = atlas.crop((index % 16 * 16, index // 16 * 16, index % 16 * 16 + 16, index // 16 * 16 + 16))
    if char.isascii() and char != " ":
        visible = [(x, y) for y in range(13) for x in range(16) if image.getpixel((x, y)) in (1, 2)]
        width = max((x + 1 for x, _ in visible), default=6)
    return image, width


def paint_text(image, text, charmap, chinese, latin, x, y, max_width, foreground=2, shadow=3):
    lines = [[]]
    widths = [0]
    for part in re.split(r"(\{[^}]+\})", text):
        if part.startswith("{"):
            if part == "{COLOR RED}":
                foreground, shadow = 4, 5
            elif part == "{COLOR DARK_GRAY}":
                foreground, shadow = 2, 3
            continue
        for char in part:
            if char == "\n":
                lines.append([])
                widths.append(0)
                continue
            bitmap, width = glyph(char, charmap, chinese, latin)
            if widths[-1] + width > max_width:
                lines.append([])
                widths.append(0)
            lines[-1].append((bitmap, width, foreground, shadow))
            widths[-1] += width
    while len(lines) > 4 and not lines[0]:
        lines.pop(0)
    if len(lines) > 4:
        raise ValueError("Berry Fix instructions exceed the original message box")
    for row, line in enumerate(lines):
        cursor = x
        for bitmap, width, foreground, shadow in line:
            for py in range(13):
                for px in range(width):
                    value = bitmap.getpixel((px, py))
                    if value in (1, 2):
                        image.putpixel((cursor + px, y + row * 16 + py), foreground if value == 1 else shadow)
            cursor += width


def main():
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    source = (US / "src/berry_fix_program.c").read_text()
    jp_source = (WOKANN / "src/berry_fix_graphics.c").read_text()
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    chinese = Image.open(ROOT / "patch/fonts/chinese_small.png")
    latin = Image.open(ROOT / "patch/fonts/latin_small.png")
    preview = Image.new("RGB", (480, 480))
    report = []
    for index, (gfx_address, map_address, pal_address, text_name) in enumerate(SCENES):
        for address in (gfx_address, map_address, pal_address):
            if f"0x{address:08X}" not in jp_source:
                raise ValueError("Berry Fix graphics addresses differ from Wokann")
        tiles = bytearray(lzdec(rom, gfx_address))
        tilemap = bytearray(lzdec(rom, map_address))
        palette = struct.unpack_from("<256H", rom, pal_address - 0x08000000)
        image = Image.new("P", (240, 160))
        image.putpalette([component for value in palette for component in tuple(((value >> shift) & 31) * 255 // 31 for shift in (0, 5, 10))])
        for py in range(160):
            for px in range(240):
                entry = struct.unpack_from("<H", tilemap, (py // 8 * 32 + px // 8) * 2)[0]
                tx = 7 - px % 8 if entry & 0x400 else px % 8
                ty = 7 - py % 8 if entry & 0x800 else py % 8
                value = tiles[(entry & 0x3FF) * 32 + ty * 4 + tx // 2] >> (tx % 2 * 4) & 15
                image.putpixel((px, py), (entry >> 12) * 16 + value)
        original = image.copy()
        image.paste(1, (6, 87, 234, 155))
        body = source_text(source, text_name)
        paint_text(image, body, charmap, chinese, latin, 8, 89, 224)
        if index == 1:
            image.paste(10, (80, 0, 160, 15))
            title = source_text(source, "RubySapphire")
            paint_text(image, title, charmap, chinese, latin, (240 - sum(glyph(char, charmap, chinese, latin)[1] for char in title)) // 2, 1, 112, 1, 2)
        elif index < 5:
            image.paste(10, (20, 68, 112, 82))
            image.paste(10, (138, 68, 232, 82))
            for title, center in ((source_text(source, "Emerald"), 60), (source_text(source, "RubySapphire"), 180)):
                width = sum(glyph(char, charmap, chinese, latin)[1] for char in title)
                paint_text(image, title, charmap, chinese, latin, center - width // 2, 68, 112, 1, 2)
        else:
            image.paste(1, (22, 32, 218, 52))
            title = source_text(source, "BerryProgramUpdate")
            width = sum(glyph(char, charmap, chinese, latin)[1] for char in title)
            paint_text(image, title, charmap, chinese, latin, (240 - width) // 2, 37, 196)
        cache = {}
        last_original_bank = max(entry[0] >> 12 for entry in struct.iter_unpack("<H", tilemap))
        original_bank_count = last_original_bank + 1
        banks = [list(palette[position * 16:(position + 1) * 16]) for position in range(original_bank_count)]
        for ty in range(20):
            for tx in range(30):
                region = (tx * 8, ty * 8, tx * 8 + 8, ty * 8 + 8)
                if original.crop(region).tobytes() == image.crop(region).tobytes():
                    continue
                colors = [palette[value] for value in image.crop(region).tobytes()]
                required = set(colors)
                bank = next((position for position, entries in enumerate(banks) if required <= set(entries)), None)
                if bank is None:
                    bank = next((position for position, entries in enumerate(banks[original_bank_count:], original_bank_count) if len(required | set(entries)) <= 16), None)
                    if bank is None:
                        bank = len(banks)
                        banks.append([])
                    banks[bank].extend(sorted(required - set(banks[bank])))
                pixels = [banks[bank].index(color) for color in colors]
                data = bytes(pixels[position] | pixels[position + 1] << 4 for position in range(0, 64, 2))
                if data not in cache:
                    cache[data] = len(tiles) // 32
                    tiles.extend(data)
                struct.pack_into("<H", tilemap, (ty * 32 + tx) * 2, cache[data] | bank << 12)
        if len(tiles) > 32 * 1024:
            raise ValueError("Berry Fix tiles exceed character VRAM")
        (ROOT / f"patch/gfx/berry_fix_{index}_tiles.4bpp").write_bytes(tiles)
        (ROOT / f"patch/gfx/berry_fix_{index}_map.4bpp").write_bytes(tilemap)
        if len(banks) > 16:
            raise ValueError("Berry Fix tiles exceed palette RAM")
        output_palette = [color for bank in banks for color in bank + [0] * (16 - len(bank))]
        output_palette += [0] * (256 - len(output_palette))
        (ROOT / f"patch/gfx/berry_fix_{index}.gbapal").write_bytes(struct.pack("<256H", *output_palette))
        preview.paste(image.convert("RGB"), (index % 2 * 240, index // 2 * 160))
        report.append({"scene": index, "source_symbol": f"sText_{text_name}", "source_text": body, "gfx": f"0x{gfx_address:08X}", "tilemap": f"0x{map_address:08X}", "palette": f"0x{pal_address:08X}", "tiles": len(tiles) // 32})
    preview.resize((960, 960), Image.Resampling.NEAREST).save(ROOT / "build/patch/berry_fix_preview.png")
    (ROOT / "build/patch/berry_fix_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
