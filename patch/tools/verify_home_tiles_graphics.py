#!/usr/bin/env python3
"""Prove and isolate the home tileset corruption without running a build."""

import argparse
import hashlib
import json
import re
import struct
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[2]
ROM_BASE = 0x08000000
BAD_ADDRESS = 0x08347307
REAL_REFERENCE = 0x085F3AAC
BASE_SHA1 = "d7cf8f156ba9c455d164e1ea780a6bf1945465c2"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha1(data):
    return hashlib.sha1(data).hexdigest()


def word(data, address):
    return struct.unpack_from("<I", data, address - ROM_BASE)[0]


def unique_offset(data, needle):
    offset = data.find(needle)
    require(offset >= 0 and data.find(needle, offset + 1) < 0, "Nonunique source resource")
    return offset


def decompress(data, address):
    cursor = address - ROM_BASE
    require(data[cursor] == 0x10, "Not an LZ77 stream")
    size = word(data, address) >> 8
    cursor += 4
    output = bytearray()
    trace = []
    while len(output) < size:
        flag_offset = cursor
        flags = data[cursor]
        cursor += 1
        for bit in range(7, -1, -1):
            if len(output) >= size:
                break
            start = cursor
            output_start = len(output)
            if flags & (1 << bit):
                first, second = data[cursor:cursor + 2]
                cursor += 2
                distance = ((first & 15) << 8 | second) + 1
                length = (first >> 4) + 3
                require(distance <= len(output), "Invalid LZ77 backreference")
                for unused in range(length):
                    output.append(output[-distance])
                details = {"kind": "copy", "distance": distance, "length": length}
            else:
                output.append(data[cursor])
                cursor += 1
                details = {"kind": "literal"}
            bad_offset = BAD_ADDRESS - ROM_BASE
            if start < bad_offset + 4 and cursor > bad_offset:
                trace.append({
                    "address": f"0x{start + ROM_BASE:08X}",
                    "bytes": data[start:cursor].hex(),
                    "flag_address": f"0x{flag_offset + ROM_BASE:08X}",
                    "flag_bit": bit,
                    "output_offset": output_start,
                    **details,
                })
    require(len(output) == size, "LZ77 output overruns its declared size")
    return bytes(output), cursor, trace


def load_tileset(base, chs, wokann, symbol, directory, resources):
    headers = (wokann / "data/tilesets/headers.inc").read_text()
    match = re.search(rf"^{symbol}: @ (0x[0-9A-Fa-f]+)$", headers, re.M)
    require(match is not None, f"Missing Wokann header: {symbol}")
    address = int(match[1], 16)
    offset = address - ROM_BASE
    require(base[offset:offset + 24] == chs[offset:offset + 24], "Changed tileset header")
    header = struct.unpack_from("<6I", base, offset)
    folder = wokann / "data/tilesets" / directory
    tiledata = {}
    for filename, resource_address in [
        ("tiles.4bpp.lz", header[1]),
        ("metatiles.bin", header[3]),
        ("metatile_attributes.bin", header[4]),
    ]:
        raw = (folder / filename).read_bytes()
        resource_offset = resource_address - ROM_BASE
        require(raw == base[resource_offset:resource_offset + len(raw)], f"Wokann mismatch: {filename}")
        patched = chs[resource_offset:resource_offset + len(raw)]
        resources.append({
            "source": str((folder / filename).relative_to(wokann)),
            "address": f"0x{resource_address:08X}",
            "size": len(raw),
            "wokann_equals_base": True,
            "changed_bytes": sum(before != after for before, after in zip(raw, patched)),
        })
        tiledata[filename] = raw
    palettes = b"".join((folder / f"palettes/{index:02}.gbapal").read_bytes() for index in range(16))
    palette_offset = header[2] - ROM_BASE
    require(palettes == base[palette_offset:palette_offset + len(palettes)], "Wokann palette mismatch")
    require(palettes == chs[palette_offset:palette_offset + len(palettes)], "Changed palettes")
    require(tiledata["metatiles.bin"] == chs[header[3] - ROM_BASE:header[3] - ROM_BASE + len(tiledata["metatiles.bin"])], "Changed metatiles")
    require(tiledata["metatile_attributes.bin"] == chs[header[4] - ROM_BASE:header[4] - ROM_BASE + len(tiledata["metatile_attributes.bin"])], "Changed metatile attributes")
    tiledata.update(header=header, header_address=address, palettes=palettes)
    return tiledata


def render_room(mapdata, width, height, tiles, primary, secondary):
    palettes = primary["palettes"][:6 * 32] + secondary["palettes"][6 * 32:13 * 32]
    colors = [tuple(((value >> shift) & 31) * 255 // 31 for shift in (0, 5, 10))
              for value in struct.unpack(f"<{len(palettes) // 2}H", palettes)]
    image = Image.new("RGB", (width * 16, height * 16), colors[0])

    def draw_tile(entry, left, top):
        tile_id = entry & 1023
        palette_id = entry >> 12
        require((tile_id + 1) * 32 <= len(tiles), "Tile outside decoded VRAM")
        for pixel_y in range(8):
            for pixel_x in range(8):
                source_x = 7 - pixel_x if entry & 0x400 else pixel_x
                source_y = 7 - pixel_y if entry & 0x800 else pixel_y
                packed = tiles[tile_id * 32 + source_y * 4 + source_x // 2]
                color = (packed >> (4 * (source_x % 2))) & 15
                if color:
                    image.putpixel((left + pixel_x, top + pixel_y), colors[palette_id * 16 + color])

    for cell, map_entry in enumerate(struct.unpack(f"<{width * height}H", mapdata)):
        metatile_id = map_entry & 1023
        tileset = primary if metatile_id < 512 else secondary
        local_id = metatile_id if metatile_id < 512 else metatile_id - 512
        entries = struct.unpack_from("<8H", tileset["metatiles.bin"], local_id * 16)
        attribute = struct.unpack_from("<H", tileset["metatile_attributes.bin"], local_id * 2)[0]
        left, top = cell % width * 16, cell // width * 16
        if attribute >> 12 == 0:
            for quadrant in range(4):
                draw_tile(0x3014, left + quadrant % 2 * 8, top + quadrant // 2 * 8)
        for index, entry in enumerate(entries):
            draw_tile(entry, left + index % 2 * 8, top + index % 4 // 2 * 8)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rom", type=Path, default=ROOT / "pokeemerald_jp_chs.gba")
    parser.add_argument("--wokann", type=Path, default=ROOT.parent / "pokeemerald_wokann_dev")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "patch/graphics_reports/home_tiles")
    parser.add_argument("--repair-rom", type=Path)
    args = parser.parse_args()
    if args.repair_rom:
        require(args.repair_rom.resolve() != args.rom.resolve(), "Never overwrite the shared ROM")
        require(not args.repair_rom.exists(), "Repair destination already exists")
    base = (ROOT / "baserom_jp.gba").read_bytes()
    chs = args.rom.read_bytes()
    require(sha1(base) == BASE_SHA1, "Unexpected original ROM")
    require((args.wokann / "baserom_jp.gba").read_bytes() == base, "Wokann ROM differs")
    require(len(chs) == 32 * 1024 * 1024, "Expected 32 MiB patched ROM")
    wokann_branch = subprocess.check_output(["git", "-C", str(args.wokann), "branch", "--show-current"], text=True).strip()
    require(wokann_branch == "dev", "Wokann must be on dev")
    resources = []
    primary = load_tileset(base, chs, args.wokann, "gTileset_Building", "primary/building", resources)
    secondary = load_tileset(base, chs, args.wokann, "gTileset_BrendansMaysHouse", "secondary/brendans_mays_house", resources)
    bad_offset = BAD_ADDRESS - ROM_BASE
    require(base[bad_offset:bad_offset + 4].hex() == "402c5f08", "Unexpected original collision bytes")
    require(0x09000000 <= word(chs, REAL_REFERENCE) < 0x0A000000, "Expected translated text in payload")
    already_repaired = chs[bad_offset:bad_offset + 4] == base[bad_offset:bad_offset + 4]
    require(already_repaired or word(chs, BAD_ADDRESS) == word(chs, REAL_REFERENCE), "Unexpected bytes at the known corruption address")
    fixed = bytearray(chs)
    fixed[bad_offset:bad_offset + 4] = base[bad_offset:bad_offset + 4]
    tile_address = secondary["header"][1]
    tile_offset = tile_address - ROM_BASE
    tile_size = len(secondary["tiles.4bpp.lz"])
    require(fixed[tile_offset:tile_offset + tile_size] == secondary["tiles.4bpp.lz"], "Additional house tileset corruption")
    require(fixed[:bad_offset] == chs[:bad_offset] and fixed[bad_offset + 4:] == chs[bad_offset + 4:], "Changes outside repair")
    original_tiles, original_end, original_trace = decompress(base, tile_address)
    broken_tiles, broken_end, broken_trace = decompress(chs, tile_address)
    fixed_tiles, fixed_end, unused_trace = decompress(fixed, tile_address)
    require(original_tiles == fixed_tiles and original_end == fixed_end, "Decoded repair differs from original")
    building_tiles, unused_end, unused_trace = decompress(base, primary["header"][1])
    require(building_tiles == decompress(chs, primary["header"][1])[0], "Changed primary tiles")
    primary_vram = building_tiles.ljust(512 * 32, b"\0")
    changed = [index for index, pair in enumerate(zip(original_tiles, broken_tiles)) if pair[0] != pair[1]]
    damaged_tiles = sorted({512 + index // 32 for index in changed})
    rooms = []
    comparisons = []
    screenshot_comparison = None
    layouts = json.loads((args.wokann / "data/layouts/layouts.json").read_text())["layouts"]
    for layout in layouts:
        if not re.fullmatch(r"LittlerootTown_(Brendans|Mays)House_[12]F_Layout", layout["name"]):
            continue
        require(layout["primary_tileset"] == "gTileset_Building" and layout["secondary_tileset"] == "gTileset_BrendansMaysHouse", "Unexpected room tilesets")
        mapdata = (args.wokann / layout["blockdata_filepath"]).read_bytes()
        map_offset = unique_offset(base, mapdata)
        require(chs[map_offset:map_offset + len(mapdata)] == mapdata, "Changed room layout")
        border = (args.wokann / layout["border_filepath"]).read_bytes()
        layout_tail = struct.pack("<3I", map_offset + ROM_BASE, primary["header_address"], secondary["header_address"])
        header_offset = unique_offset(base, layout_tail) - 12
        width, height, border_address = struct.unpack_from("<3I", base, header_offset)
        require((width, height) == (layout["width"], layout["height"]), "Layout dimensions differ")
        require(base[header_offset:header_offset + 24] == chs[header_offset:header_offset + 24], "Changed layout header")
        border_offset = border_address - ROM_BASE
        require(base[border_offset:border_offset + len(border)] == border == chs[border_offset:border_offset + len(border)], "Changed layout border")
        frames = [render_room(mapdata, width, height, primary_vram + data, primary, secondary)
                  for data in (original_tiles, broken_tiles, fixed_tiles)]
        require(frames[0].tobytes() == frames[2].tobytes(), "Repaired room pixels differ")
        screenshot_path = ROOT / "chuang.png"
        if layout["name"] == "LittlerootTown_BrendansHouse_2F_Layout" and screenshot_path.exists():
            screenshot = Image.open(screenshot_path).convert("RGB")
            require(screenshot.size == (240, 160), "Unexpected screenshot dimensions")
            regions = []
            for label, bounds in [("computer", (0, 0, 32, 48)), ("bed", (0, 64, 48, 96))]:
                left, top, right, bottom = bounds
                matches = []
                for frame in frames:
                    matches.append(sum(
                        tuple(channel >> 3 for channel in frame.getpixel((pixel_x, pixel_y)))
                        == tuple(channel >> 3 for channel in screenshot.getpixel((pixel_x + 64, pixel_y + 24)))
                        for pixel_y in range(top, bottom) for pixel_x in range(left, right)
                    ))
                regions.append({"name": label, "room_bounds": bounds, "pixels": (right - left) * (bottom - top),
                                "rgb5_matching_pixels_original_broken_repaired": matches})
            screenshot_comparison = {"file": "chuang.png", "sha1": sha1(screenshot_path.read_bytes()),
                                     "room_origin": [64, 24], "regions": regions,
                                     "note": "RGB normalized to 5-bit; visual reproduction, not an exact screenshot or emulator replay"}
        changed_cells = []
        for cell, entry in enumerate(struct.unpack(f"<{width * height}H", mapdata)):
            metatile_id = entry & 1023
            tileset = primary if metatile_id < 512 else secondary
            local_id = metatile_id if metatile_id < 512 else metatile_id - 512
            tile_ids = {entry & 1023 for entry in struct.unpack_from("<8H", tileset["metatiles.bin"], local_id * 16)}
            affected = sorted(tile_ids.intersection(damaged_tiles))
            if affected:
                changed_cells.append({"x": cell % width, "y": cell // width, "metatile": f"0x{metatile_id:03X}", "affected_tiles": affected})
        rooms.append({"name": layout["name"], "map_address": f"0x{map_offset + ROM_BASE:08X}",
                      "layout_header": f"0x{header_offset + ROM_BASE:08X}", "map_border_header_unchanged": True,
                      "repaired_pixels_equal_original": True, "affected_cells": changed_cells})
        if "2F" in layout["name"]:
            panel = Image.new("RGB", (width * 16 * 3 * 3, height * 16 * 3 + 24), "#202020")
            for index, (title, frame) in enumerate(zip(("Original JP", "CHS before", "CHS repaired"), frames)):
                left = index * width * 16 * 3
                ImageDraw.Draw(panel).text((left + 4, 5), title, fill="white")
                panel.paste(frame.resize((width * 16 * 3, height * 16 * 3), Image.Resampling.NEAREST), (left, 24))
            comparisons.append((layout["name"].replace("_Layout", "") + ".png", panel))
    require(len(rooms) == 4, "Expected all four home layouts")
    manifest = json.loads((ROOT / "patch/manifest.json").read_text())
    overlaps = []
    for path in [ROOT / "patch/manifest.json", *sorted((ROOT / "patch/batches").glob("*.json"))]:
        document = manifest if path.name == "manifest.json" else json.loads(path.read_text())
        for key in ("reference_writes", "pointer_writes", "code_patches"):
            for entry in document.get(key, []):
                address = int(entry["address"], 0)
                size = len(bytes.fromhex(entry["replacement"])) if key == "code_patches" else 4
                if address < tile_address + tile_size and address + size > tile_address:
                    overlaps.append({"file": str(path.relative_to(ROOT)), "section": key, "entry": entry})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, panel in comparisons:
        panel.save(args.output_dir / name)
    ips = b"PATCH" + bad_offset.to_bytes(3, "big") + b"\0\4" + base[bad_offset:bad_offset + 4] + b"EOF"
    (args.output_dir / "home_tiles_only.ips").write_bytes(ips)
    report = {
        "scope": "Offline graphics-only proof; no emulator, shared source changes, or full build",
        "base_sha1": sha1(base), "chs_sha1": sha1(chs), "repaired_sha1": sha1(fixed),
        "wokann_branch": wokann_branch,
        "wokann_commit": subprocess.check_output(["git", "-C", str(args.wokann), "rev-parse", "HEAD"], text=True).strip(),
        "resources": resources, "rooms": rooms, "overlapping_declared_writes": overlaps,
        "screenshot_comparison": screenshot_comparison,
        "repair": {"address": f"0x{BAD_ADDRESS:08X}", "file_offset": f"0x{bad_offset:X}",
                   "before": chs[bad_offset:bad_offset + 4].hex(), "after": base[bad_offset:bad_offset + 4].hex(),
                   "changed_bytes": sum(before != after for before, after in zip(chs[bad_offset:bad_offset + 4], fixed[bad_offset:bad_offset + 4])),
                   "all_other_rom_bytes_unchanged": True,
                   "legitimate_text_reference_preserved": f"0x{REAL_REFERENCE:08X}",
                   "rom_copy": str(args.repair_rom) if args.repair_rom else None},
        "lz77": {"start": f"0x{tile_address:08X}", "allocated_size": tile_size,
                 "original_consumed_bytes": original_end - tile_offset,
                 "broken_consumed_bytes": broken_end - tile_offset,
                 "decoded_size": len(original_tiles), "changed_decoded_bytes": len(changed),
                 "changed_global_tile_ids": damaged_tiles, "original_tokens_at_overwrite": original_trace,
                 "broken_tokens_at_overwrite": broken_trace, "repaired_equals_original": True},
        "permanent_source_fix_pending_coordination": bool(overlaps),
    }
    if args.repair_rom:
        with args.repair_rom.open("xb") as output:
            output.write(fixed)
    (args.output_dir / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"report": str(args.output_dir / "verification.json"),
                      "changed_decoded_bytes": len(changed), "changed_tiles": len(damaged_tiles),
                      "repair": report["repair"], "shared_source_fix_pending": bool(overlaps)}, indent=2))


if __name__ == "__main__":
    main()
