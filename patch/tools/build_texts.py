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

DIALOGUE_LINE_WIDTH = 168
PLACEHOLDER_WIDTHS = {
    0x01: 48,  # Player name: up to six Japanese glyphs.
    0x02: 96,  # String variables may contain long item or place names.
    0x03: 96,
    0x04: 96,
    0x05: 0,   # Japanese honorifics are replaced with an empty string.
    0x06: 24,  # Rival name is two Chinese glyphs.
}
NO_LINE_START = "，。！？：；、”’）》】」』"
NO_LINE_END = "“‘《（【「『"
PREFERRED_LINE_END = "，。！？：；、"


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
    text = text.replace("\\n", "\n")
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


def encode_compact_chinese_text(text: str, charmap: dict[str, bytes]) -> bytes:
    encoded = encode_text(text, charmap, False)
    return bytes((0xF5,)) + encoded[len(CONTROLS["ENG"]):]


def convert_us_encoded_text(
    data: bytes,
    japanese_placeholders: set[int],
    japanese_dynamic: bool,
    initial_japanese: bool = False,
) -> bytes:
    """Convert the US Chinese encoding to the injected Japanese-ROM encoding."""
    if not data or data[-1] != 0xFF:
        raise ValueError("US encoded text must end with EOS")

    mode_is_japanese = initial_japanese
    output = bytearray(CONTROLS["JPN"] if mode_is_japanese else CONTROLS["ENG"])
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
            chunk = bytearray(data[index:end])
            if code == 0x13:
                # The Japanese engine turns CLEAR_TO into a no-op, but supports
                # the otherwise-unused SHIFT_TEXT opcode with the same cursor
                # positioning semantics.
                chunk[1] = 0x0D
            output.extend(chunk)
            if code == 0x15:
                mode_is_japanese = True
            elif code == 0x16:
                mode_is_japanese = False
            index = end
            continue
        if char == 0xFD:
            if index + 1 >= len(data):
                raise ValueError("truncated placeholder")
            placeholder = data[index + 1]
            if placeholder in japanese_placeholders:
                if not mode_is_japanese:
                    output.extend(CONTROLS["JPN"])
            output.extend(data[index:index + 2])
            if placeholder in japanese_placeholders:
                output.extend(CONTROLS["ENG"])
                mode_is_japanese = False
            index += 2
            continue
        if char == 0xF7 and japanese_dynamic:
            if not mode_is_japanese:
                output.extend(CONTROLS["JPN"])
            output.extend(data[index:index + 2])
            output.extend(CONTROLS["ENG"])
            mode_is_japanese = False
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


def text_token(data: bytes, index: int) -> tuple[bytes, int, int]:
    """Return one encoded token, its pixel width, and the next byte index."""
    char = data[index]
    if char == 0xFC:
        if index + 1 >= len(data):
            raise ValueError("truncated extended control code while wrapping")
        code = data[index + 1]
        try:
            arg_length = EXT_CTRL_ARG_LENGTHS[code]
        except KeyError as exc:
            raise ValueError(f"unknown extended control code while wrapping: 0x{code:02X}") from exc
        end = index + 2 + arg_length
        return data[index:end], 0, end
    if char == 0xFD:
        if index + 1 >= len(data):
            raise ValueError("truncated placeholder while wrapping")
        end = index + 2
        return data[index:end], PLACEHOLDER_WIDTHS.get(data[index + 1], 48), end
    if char in (0xF7, 0xF8, 0xF9):
        end = min(index + 2, len(data))
        return data[index:end], 0, end
    if char == 0x7F or 0x60 <= char <= 0x7D and char not in (0x65, 0x7A):
        if index + 1 >= len(data):
            raise ValueError("truncated Chinese glyph while wrapping")
        end = index + 2
        return data[index:end], 12, end
    return data[index:index + 1], 8, index + 1


def tokenize_line(data: bytes) -> list[tuple[bytes, int]]:
    tokens = []
    index = 0
    while index < len(data):
        token, width, index = text_token(data, index)
        tokens.append((token, width))
    return tokens


def line_width(data: bytes) -> int:
    return sum(width for _, width in tokenize_line(data))


def encoded_chars(chars: str, charmap: dict[str, bytes]) -> set[bytes]:
    return {encode_char(char, charmap) for char in chars if char in charmap}


def visible_group_start(tokens: list[tuple[bytes, int]], visible_index: int) -> int:
    """Keep renderer mode controls attached to the visible glyph they introduce."""
    start = visible_index
    while start > 0 and tokens[start - 1][1] == 0:
        start -= 1
    return start


def wrap_tokens(
    tokens: list[tuple[bytes, int]],
    max_width: int,
    no_line_start: set[bytes],
    no_line_end: set[bytes],
    preferred_line_end: set[bytes],
) -> list[list[tuple[bytes, int]]]:
    lines = []
    remaining = tokens
    while remaining:
        width = 0
        end = 0
        preferred = 0
        while end < len(remaining):
            token, token_width = remaining[end]
            if token_width and width and width + token_width > max_width:
                break
            width += token_width
            end += 1
            if token in preferred_line_end and width >= max_width * 3 // 5:
                preferred = end
        if end == len(remaining):
            lines.append(remaining)
            break

        split = preferred or end
        next_visible = next((token for token, token_width in remaining[split:] if token_width), b"")
        if next_visible in no_line_start:
            previous_visible = next(
                (index for index in range(split - 1, -1, -1) if remaining[index][1]),
                -1,
            )
            if previous_visible >= 0:
                split = visible_group_start(remaining, previous_visible)
        while split > 0:
            previous_visible = next(
                (index for index in range(split - 1, -1, -1) if remaining[index][1]),
                -1,
            )
            if previous_visible < 0 or remaining[previous_visible][0] not in no_line_end:
                break
            split = visible_group_start(remaining, previous_visible)
        if split == 0:
            split = max(1, end)

        lines.append(remaining[:split])
        remaining = remaining[split:]
    return lines


def wrap_dialogue_page(data: bytes, charmap: dict[str, bytes]) -> tuple[bytes, bool]:
    source_lines = re.split(b"[\\xFA\\xFE]", data)
    if all(line_width(line) <= DIALOGUE_LINE_WIDTH for line in source_lines):
        return data, False

    flowing = data.replace(b"\xFA", b"").replace(b"\xFE", b"")
    tokens = tokenize_line(flowing)
    lines = wrap_tokens(
        tokens,
        DIALOGUE_LINE_WIDTH,
        encoded_chars(NO_LINE_START, charmap),
        encoded_chars(NO_LINE_END, charmap),
        encoded_chars(PREFERRED_LINE_END, charmap),
    )
    output = bytearray()
    for index, line in enumerate(lines):
        if index:
            output.append(0xFE if index == 1 else 0xFA)
        for token, _ in line:
            output.extend(token)
    return bytes(output), True


def wrap_dialogue(data: bytes, charmap: dict[str, bytes]) -> tuple[bytes, int]:
    """Reflow overlong pages for the original 22-tile Japanese text window."""
    output = bytearray()
    changed_pages = 0
    page_start = 0
    for index, char in enumerate(data):
        if char not in (0xFB, 0xFF):
            continue
        page, changed = wrap_dialogue_page(data[page_start:index], charmap)
        output.extend(page)
        output.append(char)
        changed_pages += int(changed)
        page_start = index + 1
        if char == 0xFF:
            break
    return bytes(output), changed_pages


def main() -> None:
    if len(sys.argv) < 4:
        raise SystemExit("usage: build_texts.py CHARMAP OUTPUT_INC TEXTS_JSON...")
    charmap_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    texts_paths = [Path(path) for path in sys.argv[3:]]
    charmap = read_charmap(charmap_path)
    definitions = []
    fixed_tables = []
    for texts_path in texts_paths:
        document = json.loads(texts_path.read_text(encoding="utf-8"))
        if isinstance(document, dict) and document.get("kind") == "pokedex_entries":
            fixed_tables.append(document)
            continue
        if isinstance(document, dict) and document.get("kind") == "us_species_name_table":
            source_path = (texts_path.parent / document["source"]).resolve()
            source = source_path.read_text(encoding="utf-8")
            marker = "const u8 gSpeciesNames[][POKEMON_NAME_LENGTH + 1] = {"
            try:
                chinese_table = source.split(marker, 1)[1]
            except IndexError as exc:
                raise ValueError(f"{source_path} is missing the Chinese species-name table") from exc
            species_names = re.findall(r'\[SPECIES_\w+\]\s*=\s*_\("([^"]*)"\)', chinese_table)
            if len(species_names) != document["count"]:
                raise ValueError(
                    f"{source_path} contains {len(species_names)} Chinese species names, "
                    f"expected {document['count']}"
                )
            fixed_tables.append(
                {
                    "kind": "string_pointer_table",
                    "name": document["name"],
                    "strings": species_names,
                    "compact_chinese": True,
                }
            )
            continue
        if isinstance(document, dict) and document.get("kind") == "us_trainer_name_table":
            source_path = (texts_path.parent / document["source"]).resolve()
            trainer_names = re.findall(
                r'\.trainerName\s*=\s*_\("([^"]*)"\)',
                source_path.read_text(encoding="utf-8"),
            )
            if len(trainer_names) != document["count"]:
                raise ValueError(
                    f"{source_path} contains {len(trainer_names)} trainer names, "
                    f"expected {document['count']}"
                )
            fixed_tables.append(
                {
                    "kind": "string_pointer_table",
                    "name": document["name"],
                    "strings": trainer_names,
                }
            )
            continue
        if isinstance(document, dict) and document.get("kind") == "us_trainer_class_name_table":
            source_path = (texts_path.parent / document["source"]).resolve()
            trainer_class_names = re.findall(
                r'_\("([^"]*)"\)',
                source_path.read_text(encoding="utf-8"),
            )
            if len(trainer_class_names) != document["count"]:
                raise ValueError(
                    f"{source_path} contains {len(trainer_class_names)} trainer class names, "
                    f"expected {document['count']}"
                )
            fixed_tables.append(
                {
                    "kind": "string_pointer_table",
                    "name": document["name"],
                    "strings": trainer_class_names,
                }
            )
            continue
        if isinstance(document, dict) and document.get("kind") == "us_berry_info_table":
            source_path = (texts_path.parent / document["source"]).resolve()
            source = source_path.read_text(encoding="utf-8")
            description_names = document["description_names"]
            description_parts = []
            for part in (1, 2):
                strings = re.findall(
                    rf'static const u8 sBerryDescriptionPart{part}_\w+\[\] = _\("([^"]*)"\);',
                    source,
                )
                if len(strings) != document["count"]:
                    raise ValueError(
                        f"{source_path} contains {len(strings)} berry description part {part} strings, "
                        f"expected {document['count']}"
                    )
                description_parts.append(strings)
            for name, strings in zip(description_names, description_parts):
                fixed_tables.append(
                    {
                        "kind": "string_pointer_table",
                        "name": name,
                        "strings": strings,
                    }
                )
            berry_names = re.findall(r'\.name\s*=\s*_\("([^"]*)"\)', source)
            if len(berry_names) != document["count"]:
                raise ValueError(
                    f"{source_path} contains {len(berry_names)} berry names, "
                    f"expected {document['count']}"
                )
            document["names"] = berry_names
            fixed_tables.append(document)
            continue
        if isinstance(document, dict) and document.get("kind") == "us_decoration_table":
            header_path = (texts_path.parent / document["header_source"]).resolve()
            description_path = (texts_path.parent / document["description_source"]).resolve()
            header_source = header_path.read_text(encoding="utf-8")
            description_source = description_path.read_text(encoding="utf-8")
            description_names = re.findall(
                r'\.description\s*=\s*(DecorDesc_\w+),', header_source
            )
            descriptions = dict(re.findall(
                r'const u8 (DecorDesc_\w+)\[\] = _\("([^"]*)"\);',
                description_source,
            ))
            if len(description_names) != document["count"]:
                raise ValueError(
                    f"{header_path} contains {len(description_names)} decoration descriptions, "
                    f"expected {document['count']}"
                )
            missing = set(description_names) - descriptions.keys()
            if missing:
                raise ValueError(f"{description_path} is missing decoration descriptions: {sorted(missing)}")
            document["descriptions"] = [
                descriptions[name].replace("\\n", "\n") for name in description_names
            ]
            fixed_tables.append(document)
            continue
        if isinstance(document, dict) and document.get("kind") == "us_region_map_table":
            source_path = (texts_path.parent / document["source"]).resolve()
            map_sections = json.loads(source_path.read_text(encoding="utf-8"))["map_sections"]
            if len(map_sections) != document["count"]:
                raise ValueError(
                    f"{source_path} contains {len(map_sections)} map sections, "
                    f"expected {document['count']}"
                )
            if any("name" not in section for section in map_sections):
                raise ValueError(f"{source_path} contains a map section without a name")
            document["strings"] = [
                section["name"].replace("{AQUA}", "海洋")
                for section in map_sections
            ]
            fixed_tables.append(document)
            continue
        if isinstance(document, dict) and document.get("kind") in ("fixed_string_table", "string_pointer_table"):
            fixed_tables.append(document)
            continue
        document_wrap = isinstance(document, dict) and "dialogue" in document.get("category", "").lower()
        for definition in document if isinstance(document, list) else document["texts"]:
            definitions.append((definition, definition.get("auto_wrap", document_wrap)))

    lines = ["@ Generated by patch/tools/build_texts.py; do not edit.", ".align 2"]
    names = set()
    wrapped_strings = 0
    wrapped_pages = 0
    for definition, auto_wrap in definitions:
        name = definition["name"]
        if name in names:
            raise ValueError(f"duplicate text symbol: {name}")
        names.add(name)
        if "us_encoded_hex" in definition:
            encoded = convert_us_encoded_text(
                bytes.fromhex(definition["us_encoded_hex"]),
                set(definition.get("japanese_placeholders", [])),
                definition.get("japanese_dynamic", False),
                definition.get("initial_japanese", False),
            )
        else:
            encoded = encode_text(definition["text"], charmap, definition.get("styled", False))
        if auto_wrap:
            encoded, changed_pages = wrap_dialogue(encoded, charmap)
            wrapped_strings += int(changed_pages > 0)
            wrapped_pages += changed_pages
        lines.extend((f".global {name}", f"{name}:", "    .byte " + ", ".join(f"0x{x:02X}" for x in encoded)))
    for table in fixed_tables:
        if table["kind"] == "us_region_map_table":
            base_offset = int(table["base_offset"], 0)
            stride = table["stride"]
            name_offset = table["name_offset"]
            for index, map_name in enumerate(table["strings"]):
                label = f".L{table['name']}_{index}"
                encoded = encode_text(map_name, charmap, False)
                lines.extend((".align 2", f"{label}:", "    .byte " + ", ".join(f"0x{value:02X}" for value in encoded)))
            lines.extend((".align 2", f".global {table['name']}", f"{table['name']}:"))
            for index in range(table["count"]):
                offset = base_offset + index * stride
                label = f".L{table['name']}_{index}"
                lines.append(f'    .incbin "baserom_jp.gba", 0x{offset:X}, {name_offset}')
                lines.append(f"    .4byte {label}")
                suffix_offset = offset + name_offset + 4
                suffix_size = stride - name_offset - 4
                if suffix_size:
                    lines.append(f'    .incbin "baserom_jp.gba", 0x{suffix_offset:X}, {suffix_size}')
            continue
        if table["kind"] == "us_decoration_table":
            base_offset = int(table["base_offset"], 0)
            stride = table["stride"]
            description_offset = table["description_offset"]
            for index, description in enumerate(table["descriptions"]):
                label = f".L{table['name']}_description_{index}"
                encoded = encode_text(description, charmap, False)
                lines.extend((".align 2", f"{label}:", "    .byte " + ", ".join(f"0x{value:02X}" for value in encoded)))
            lines.extend((".align 2", f".global {table['name']}", f"{table['name']}:"))
            for index in range(table["count"]):
                offset = base_offset + index * stride
                label = f".L{table['name']}_description_{index}"
                lines.append(f'    .incbin "baserom_jp.gba", 0x{offset:X}, {description_offset}')
                lines.append(f"    .4byte {label}")
                suffix_offset = offset + description_offset + 4
                suffix_size = stride - description_offset - 4
                if suffix_size:
                    lines.append(f'    .incbin "baserom_jp.gba", 0x{suffix_offset:X}, {suffix_size}')
            continue
        if table["kind"] == "us_berry_info_table":
            base_offset = int(table["base_offset"], 0)
            description_names = table["description_names"]
            lines.extend((".align 2", f".global {table['name']}", f"{table['name']}:"))
            lines.append(f'    .incbin "baserom_jp.gba", 0x{base_offset:X}, 28')
            for index in range(table["count"]):
                offset = base_offset + (index + 1) * 28
                encoded_name = encode_text(table["names"][index], charmap, False)[len(CONTROLS["ENG"]):]
                if len(encoded_name) != 7:
                    raise ValueError(f"{table['name']}[{index}] name must occupy 7 bytes")
                lines.append("    .byte " + ", ".join(f"0x{value:02X}" for value in encoded_name))
                lines.append(f'    .incbin "baserom_jp.gba", 0x{offset + 7:X}, 5')
                lines.append(f"    .4byte .L{description_names[0]}_{index}")
                lines.append(f"    .4byte .L{description_names[1]}_{index}")
                lines.append(f'    .incbin "baserom_jp.gba", 0x{offset + 20:X}, 8')
            continue
        if table["kind"] == "pokedex_entries":
            name = table["name"]
            if name in names:
                raise ValueError(f"duplicate text symbol: {name}")
            names.add(name)
            category_labels = []
            for index, entry in enumerate(table["entries"]):
                category_label = f".L{name}_category_{index}"
                description_label = f".L{name}_description_{index}"
                category_labels.append(category_label)
                encoded = encode_text(entry["category"], charmap, False)
                lines.extend((".align 2", f"{category_label}:", "    .byte " + ", ".join(f"0x{x:02X}" for x in encoded)))
                encoded = encode_text(entry["description"], charmap, False)
                lines.extend((".align 2", f"{description_label}:", "    .byte " + ", ".join(f"0x{x:02X}" for x in encoded)))
            lines.extend((".align 2", f".global {name}", f"{name}:"))
            for index, entry in enumerate(table["entries"]):
                category_bytes = bytes.fromhex(entry["jp_category"])
                stats_bytes = bytes.fromhex(entry["stats"])
                tail_bytes = bytes.fromhex(entry["tail"])
                if len(category_bytes) != 6 or len(stats_bytes) != 6 or len(tail_bytes) != 12:
                    raise ValueError(f"{name}[{index}] has malformed binary fields")
                lines.append("    .byte " + ", ".join(f"0x{x:02X}" for x in category_bytes + stats_bytes))
                lines.append(f"    .4byte .L{name}_description_{index}")
                lines.append("    .byte " + ", ".join(f"0x{x:02X}" for x in tail_bytes))
            lines.extend((".align 2", f".global {name}CategoryTable", f"{name}CategoryTable:"))
            lines.extend(f"    .4byte {label}" for label in category_labels)
            encoded = encode_text("宝可梦", charmap, False)
            lines.extend((".align 2", f".global {name}CategorySuffix", f"{name}CategorySuffix:", "    .byte " + ", ".join(f"0x{x:02X}" for x in encoded)))
            continue
        name = table["name"]
        if name in names:
            raise ValueError(f"duplicate text symbol: {name}")
        names.add(name)
        if table["kind"] == "string_pointer_table":
            labels = []
            for index, entry in enumerate(table["strings"]):
                label = f".L{name}_{index}"
                labels.append(label)
                encoded = (encode_compact_chinese_text(entry, charmap)
                           if table.get("compact_chinese", False)
                           else encode_text(entry, charmap, False))
                lines.extend((".align 2", f"{label}:", "    .byte " + ", ".join(f"0x{x:02X}" for x in encoded)))
            lines.extend((".align 2", f".global {name}", f"{name}:"))
            lines.extend(f"    .4byte {label}" for label in labels)
            continue
        stride = table["stride"]
        lines.extend((".align 2", f".global {name}", f"{name}:"))
        for index, entry in enumerate(table["strings"]):
            if isinstance(entry, dict):
                encoded = convert_us_encoded_text(
                    bytes.fromhex(entry["us_encoded_hex"]),
                    set(entry.get("japanese_placeholders", [])),
                    entry.get("japanese_dynamic", False),
                    entry.get("initial_japanese", False),
                )
            else:
                if table.get("compact_chinese", False):
                    encoded = encode_compact_chinese_text(entry, charmap)
                else:
                    encoded = encode_text(entry, charmap, False)
            if len(encoded) > stride:
                raise ValueError(
                    f"{name}[{index}] exceeds its {stride}-byte stride: {entry!r}"
                )
            encoded += bytes((0xFF,)) * (stride - len(encoded))
            lines.append("    .byte " + ", ".join(f"0x{x:02X}" for x in encoded))
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"auto-wrapped {wrapped_pages} overlong pages in {wrapped_strings} dialogue strings")


if __name__ == "__main__":
    main()
