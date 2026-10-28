#!/usr/bin/env python3
"""Create a diagnostic ROM that sends the locally extracted Pokémon Box image."""
import argparse
import hashlib
import struct
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("rom", type=Path)
parser.add_argument("box_image", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("--nm", required=True)
parser.add_argument("--elf", type=Path, required=True)
parser.add_argument("--keep-screen", action="store_true", help="skip the main-loop communication timeout reset")
parser.add_argument("--expected-sha256", help="refuse to write an output that does not match this SHA-256")
args = parser.parse_args()
symbols = {}
for line in subprocess.check_output([args.nm, "-n", str(args.elf)], text=True).splitlines():
    parts = line.split()
    if len(parts) == 3:
        symbols[parts[2]] = int(parts[0], 16)
rom = bytearray(args.rom.read_bytes())
image = args.box_image.read_bytes()
if args.keep_screen:
    image = bytearray(image)
    # Match the temporary image used to inspect the logo: skip only this BL.
    pos, expected = 0x3aa, bytes.fromhex("02f04ff9")
    if image[pos:pos + 4] != expected:
        raise SystemExit(f"unexpected reset call at {pos:#x}")
    image[pos:pos + 4] = bytes.fromhex("c046c046")
    image = bytes(image)
image += bytes((-len(image)) % 16)
start = 0x09f00000
off = start - 0x08000000
if off + len(image) > len(rom) or any(x != 0xff for x in rom[off:off + len(image)]):
    raise SystemExit("diagnostic payload area is not empty")
for label, expected, value in (("_081BF184", "RemoteReceiverImageStart", start),
                                ("_081BF18C", "RemoteReceiverImageEnd", start + len(image))):
    pos = symbols[label] - 0x08000000
    if struct.unpack_from("<I", rom, pos)[0] != symbols[expected]:
        raise SystemExit("ROM does not match supplied ELF: " + label)
    struct.pack_into("<I", rom, pos, value)
rom[off:off + len(image)] = image
digest = hashlib.sha256(rom).hexdigest()
if args.expected_sha256 and digest != args.expected_sha256:
    raise SystemExit(f"ROM hash mismatch: expected {args.expected_sha256}, got {digest}")
args.output.write_bytes(rom)
print(f"wrote {args.output}: Box image {len(image)} bytes at {start:#x}; SHA-256 {digest}")
