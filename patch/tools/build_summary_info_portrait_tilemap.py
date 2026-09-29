#!/usr/bin/env python3

import argparse
import struct
from pathlib import Path


def copy_row(
    target: list[int],
    source: tuple[int, ...],
    source_y: int,
    target_y: int,
    xor_flags: int = 0,
) -> None:
    for x in range(10):
        target[target_y * 32 + x] = source[source_y * 32 + x] ^ xor_flags


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source = struct.unpack("<1024H", args.source.read_bytes())
    target = list(source)

    copy_row(target, source, 14, 15, 0x0800)
    copy_row(target, source, 14, 16)
    copy_row(target, source, 15, 17)
    copy_row(target, source, 17, 18)
    copy_row(target, source, 18, 19)

    args.output.write_bytes(struct.pack("<1024H", *target))


if __name__ == "__main__":
    main()
