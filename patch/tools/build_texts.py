#!/usr/bin/env python3
"""Encode Japanese-to-Chinese text batches for the injected ROM."""

from __future__ import annotations

import ast
import json
import re
import sys
import warnings
from pathlib import Path


CHARMAP_RE = re.compile(r"^('(?:[^'\\]|\\.)*')\s*=\s*((?:[0-9A-Fa-f]{2}\s*)+)(?:@.*)?$")

CONTROLS = {
    "PLAYER": bytes((0xFD, 0x01)),
    "STR_VAR_1": bytes((0xFD, 0x02)),
    "STR_VAR_2": bytes((0xFD, 0x03)),
    "JPN": bytes((0xFC, 0x15)),
    "ENG": bytes((0xFC, 0x16)),
}

EXT_CTRL_ARG_LENGTHS = {
    0x00: 0,
    0x01: 1,
    0x02: 1,
    0x03: 1,
    0x04: 3,
    0x05: 1,
    0x06: 1,
    0x07: 0,
    0x08: 1,
    0x09: 0,
    0x0A: 0,
    0x0B: 2,
    0x0C: 1,
    0x0D: 1,
    0x0E: 1,
    0x0F: 0,
    0x10: 2,
    0x11: 1,
    0x12: 1,
    0x13: 1,
    0x14: 1,
    0x15: 0,
    0x16: 0,
    0x17: 0,
    0x18: 0,
}

SYNTHETIC_PUNCTUATION = {
    "；", "。", "～", "、", "，", "！", "？", "：", "—", "“", "”", "…"
}


def read_charmap(path: Path) -> dict[str, bytes]:
    result: dict[str, bytes] = {}
    warnings.filterwarnings("ignore", category=SyntaxWarning)
    for line in path.read_text(encoding="utf-8").splitlines():
        match = CHARMAP_RE.match(line.strip())
        if not match:
            continue
        char = ast.literal_eval(match.group(1))
        encoded = bytes.fromhex(match.group(2))
        result.setdefault(char, encoded)
    return result


def encode_char(char: str, charmap: dict[str, bytes]) -> bytes:
    if char == "\n":
        return bytes((0xFE,))
    encoded = charmap.get(char)
    if encoded is None:
        raise ValueError(f"character missing from charmap: {char!r}")
    if char in SYNTHETIC_PUNCTUATION:
        if len(encoded) != 1:
            raise ValueError(f"punctuation must have a one-byte source glyph: {char!r}")
        return bytes((0x7F, encoded[0]))
    if len(encoded) == 2 and 0x01 <= encoded[0] <= 0x1E:
        if encoded[0] in (0x06, 0x1B) or encoded[1] > 0xF6:
            raise ValueError(f"invalid Chinese source encoding for {char!r}: {encoded.hex(' ')}")
        return bytes((encoded[0] + 0x5F, encoded[1]))
    if len(encoded) == 1:
        return encoded
    raise ValueError(f"unsupported encoding for {char!r}: {encoded.hex(' ')}")


def encode_text(text: str, charmap: dict[str, bytes], styled: bool) -> bytes:
    output = bytearray()
    if styled:
        # DrawOptionMenuChoice changes bytes 2 and 5 for the selected color.
        output.extend((0xFC, 0x01, 0x06, 0xFC, 0x03, 0x07))
    output.extend(CONTROLS["ENG"])

    index = 0
    while index < len(text):
        if text.startswith("\\p", index):
            output.append(0xFB)
            index += 2
            continue
        if text.startswith("\\l", index):
            output.append(0xFA)
            index += 2
            continue
        if text[index] == "{":
            end = text.find("}", index)
            if end < 0:
                raise ValueError(f"unterminated control in {text!r}")
            name = text[index + 1:end]
            try:
                output.extend(CONTROLS[name])
            except KeyError as exc:
                raise ValueError(f"unknown control {{{name}}}") from exc
            index = end + 1
            continue
        output.extend(encode_char(text[index], charmap))
        index += 1

    output.append(0xFF)
    if styled and len(output) > 15:
        raise ValueError(f"styled option exceeds the Japanese 15-byte stack buffer: {text!r}")
    return bytes(output)


def convert_us_encoded_text(data: bytes, japanese_placeholders: set[int]) -> bytes:
    """Convert the US Chinese encoding to the injected Japanese-ROM encoding."""
    if not data or data[-1] != 0xFF:
        raise ValueError("US encoded text must end with EOS")

    output = bytearray(CONTROLS["ENG"])
    index = 0
    while index < len(data):
        char = data[index]
        if char == 0xFF:
            output.append(char)
            break
        if char == 0xFC:
            if index + 1 >= len(data):
                raise ValueError("truncated extended control code")
            code = data[index + 1]
            try:
                arg_length = EXT_CTRL_ARG_LENGTHS[code]
            except KeyError as exc:
                raise ValueError(f"unknown extended control code: 0x{code:02X}") from exc
            end = index + 2 + arg_length
            output.extend(data[index:end])
            index = end
            continue
        if char == 0xFD:
            if index + 1 >= len(data):
                raise ValueError("truncated placeholder")
            placeholder = data[index + 1]
            if placeholder in japanese_placeholders:
                output.extend(CONTROLS["JPN"])
            output.extend(data[index:index + 2])
            if placeholder in japanese_placeholders:
                output.extend(CONTROLS["ENG"])
            index += 2
            continue
        if char in (0xF7, 0xF8, 0xF9):
            output.extend(data[index:index + 2])
            index += 2
            continue
        if char == 0x30 or 0x36 <= char <= 0x3F and char != 0x38:
            output.extend((0x7F, char))
            index += 1
            continue
        if 0x01 <= char <= 0x1E and char not in (0x06, 0x1B):
            if index + 1 >= len(data) or data[index + 1] > 0xF6:
                raise ValueError(f"invalid US Chinese pair at byte {index}")
            output.extend((char + 0x5F, data[index + 1]))
            index += 2
            continue
        output.append(char)
        index += 1

    return bytes(output)


def main() -> None:
    if len(sys.argv) < 4:
        raise SystemExit("usage: build_texts.py CHARMAP OUTPUT_INC TEXTS_JSON...")
    charmap_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    texts_paths = [Path(path) for path in sys.argv[3:]]
    charmap = read_charmap(charmap_path)
    definitions = []
    for texts_path in texts_paths:
        document = json.loads(texts_path.read_text(encoding="utf-8"))
        definitions.extend(document if isinstance(document, list) else document["texts"])

    lines = ["@ Generated by patch/tools/build_texts.py; do not edit.", ".align 2"]
    names = set()
    for definition in definitions:
        name = definition["name"]
        if name in names:
            raise ValueError(f"duplicate text symbol: {name}")
        names.add(name)
        if "us_encoded_hex" in definition:
            encoded = convert_us_encoded_text(
                bytes.fromhex(definition["us_encoded_hex"]),
                set(definition.get("japanese_placeholders", [])),
            )
        else:
            encoded = encode_text(definition["text"], charmap, definition.get("styled", False))
        lines.extend((f".global {name}", f"{name}:", "    .byte " + ", ".join(f"0x{x:02X}" for x in encoded)))
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
