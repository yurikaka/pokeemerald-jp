"""Verify US direction arrows convert to Japanese escaped font glyphs."""

import json
from pathlib import Path

from build_texts import (CONTROLS, convert_us_encoded_text, encode_text,
                        read_charmap, text_token)


ROOT = Path(__file__).resolve().parents[2]


def main():
    charmap = read_charmap(ROOT / "patch/charmap_chs.txt")
    reference = (ROOT.parent / "pokeemerald_wokann_dev/charmap.txt").read_text()
    for index, name in enumerate(("UP_ARROW", "DOWN_ARROW", "LEFT_ARROW", "RIGHT_ARROW")):
        expected = bytes((0xFC, 0x0C, index))
        declaration = f"{name.ljust(11)} = FC 0C {index:02X}"
        if declaration not in reference:
            raise ValueError(f"Unexpected Wokann arrow encoding: {name}")
        if CONTROLS[name] != expected:
            raise ValueError(f"Unexpected literal encoding: {name}")
        converted = convert_us_encoded_text(bytes((0x79 + index, 0xFF)), set(), False)
        if converted != b"\xfc\x16" + expected + b"\xff":
            raise ValueError(f"Unexpected US arrow conversion: {name}")
        if text_token(expected, 0) != (expected, 8, 3):
            raise ValueError(f"Incorrect arrow width: {name}")
        if encode_text("{" + name + "}古玫镇", charmap, False) != converted[:-1] + encode_text("古玫镇", charmap, False)[2:]:
            raise ValueError(f"Arrow damaged the following place name: {name}")
    japanese = b"\xfc\x15\x79\x7a\x7b\x7c\xff"
    if convert_us_encoded_text(japanese, set(), False)[2:] != japanese:
        raise ValueError("Explicit Japanese kana were incorrectly converted")
    chinese = b"\x01\x79\x01\x7a\x01\x7b\x01\x7c\xff"
    if convert_us_encoded_text(chinese, set(), False) != b"\xfc\x16\x60\x79\x60\x7a\x60\x7b\x60\x7c\xff":
        raise ValueError("Chinese low bytes were incorrectly converted")
    batch = json.loads((ROOT / "patch/batches/008_route101.json").read_text())
    definition = next(entry for entry in batch["texts"]
                      if entry["source_symbol"] == "Route101_Text_RouteSign")
    result = convert_us_encoded_text(bytes.fromhex(definition["us_encoded_hex"]), set(), False)
    expected = encode_text("101号道路\n{UP_ARROW}古玫镇", charmap, False)
    if result != expected:
        raise ValueError("Route 101 sign differs from its intended Chinese text")
    print("All four arrows, glyph widths, Japanese kana, Chinese low bytes and Route 101 passed")


if __name__ == "__main__":
    main()
