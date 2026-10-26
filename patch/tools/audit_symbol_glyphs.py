"""Scan all generated text vectors and verify their bytes in the built ROM.

Parse text controls and multi-byte glyphs before looking for Latin symbols
that would fall through to a kana glyph. Binary Pokedex records are excluded.
Explicit Japanese text and runtime player/link strings retain native encoding.
"""
import argparse
import json
import re
import subprocess
import zlib
from pathlib import Path

from build_texts import EXT_CTRL_ARG_LENGTHS

ROOT = Path(__file__).resolve().parents[2]
RISK = {
    0x2D: '&/を', 0x2E: '+/ん', 0x30: '・/ぃ', 0x35: '=/ゅ',
    0x36: ';/ょ', 0x37: '。/が', 0x39: '~/ぐ', 0x3A: '、/げ',
    0x3B: '，/ご', 0x3C: '！/ざ', 0x3D: '？/じ', 0x3E: '：/ず',
    0x3F: '—/ぜ', 0x51: '¿/ア', 0x52: '¡/イ', 0x5B: '%/サ',
    0x5C: '(/シ', 0x5D: ')/ス', 0x85: '</ュ', 0x86: '>/ョ',
    0xAD: './。', 0xAE: '-/ー',
}
# Catch other native kana slots too, including accidental Latin accents or
# US logo glyphs. Valid Chinese pairs and explicit Japanese mode are skipped.
RISK.update({code: f'native kana slot/{code:02X}' for code in range(1, 0xA1)
             if code not in RISK})


def scan(data):
    mode = False
    index = 0
    hits = []
    while index < len(data):
        offset = index
        char = data[index]
        index += 1
        if char == 0xFF:
            mode = False
        elif char == 0xFC:
            code = data[index]
            index += 1 + EXT_CTRL_ARG_LENGTHS[code]
            if code in (0x15, 0x16):
                mode = code == 0x16
        elif char in (0xFD, 0xF7, 0xF8, 0xF9):
            index += 1
        elif char == 0xF5:
            sub = data[index]
            if sub == 0xF1:  # Resource body is checked as its own vector.
                index += 2
            elif sub == 0xF2:  # Species body is checked independently.
                index += 3
            elif sub in (0xF3, 0xF4):
                mode = True
                index += 1
            else:  # Compact Chinese prefix; next byte is its first glyph.
                mode = True
        elif mode and (char == 0x7F or 0x60 <= char <= 0x7D and char not in (0x65, 0x7A)):
            index += 1
        elif mode and char in RISK:
            hits.append({'offset': offset, 'byte': f'{char:02X}', 'symbol/kana': RISK[char]})
        assert index <= len(data), 'Truncated text token'
    return hits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    symbols = {}
    for line in subprocess.check_output([args.nm, '-n', str(ROOT / 'build/patch/payload.elf')], text=True).splitlines():
        fields = line.split()
        if len(fields) == 3:
            symbols[fields[2]] = int(fields[0], 16)
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    base = symbols['ChsBerryTagTitle']
    offset = 0
    label = ''
    findings = []
    vectors = binary = byte_count = 0
    for number, line in enumerate((ROOT / 'build/patch/texts.inc').read_text().splitlines(), 1):
        line = line.strip()
        if line.endswith(':'):
            label = line[:-1]
            if label in symbols:
                assert symbols[label] == base + offset, (label, 'Layout mismatch')
        elif line.startswith('.align '):
            alignment = 1 << int(line.split()[1], 0)
            offset = (offset + alignment - 1) & -alignment
        elif line.startswith('.4byte '):
            offset += 4 * len(line[7:].split(','))
        elif line.startswith('.incbin '):
            fields = line[8:].split(',')
            offset += (int(fields[2], 0) if len(fields) == 3
                       else (ROOT / fields[0].strip().strip('"')).stat().st_size)
        elif line.startswith('.byte '):
            data = bytes(int(value, 0) for value in line[6:].split(','))
            address = base + offset
            assert rom[address - 0x08000000:address - 0x08000000 + len(data)] == data, (label, 'ROM mismatch')
            offset += len(data)
            byte_count += len(data)
            if label == 'ChsPokedexEntries':
                binary += 1  # Stats, JP category bytes and pointers, not text.
                continue
            vectors += 1
            for hit in scan(data):
                findings.append(dict(label=label, line=number, address=f'0x{address:08X}', **hit))

    # NPC display strings generated separately for the C name adapter.
    npc_vectors = 0
    header = (ROOT / 'build/patch/npc_names.h').read_text()
    for name, body in re.findall(r'static const u8 (\w+)\[\] = \{([^}]+)\};', header):
        data = bytes(int(value, 0) for value in body.split(','))
        address = symbols[name]
        assert rom[address - 0x08000000:address - 0x08000000 + len(data)] == data
        npc_vectors += 1
        for hit in scan(data):
            findings.append(dict(label=name, address=f'0x{address:08X}', **hit))

    # Handwritten ASM strings and C display buffers (not code/graphics bytes).
    asm = (ROOT / 'patch/chinese_engine.s').read_text()
    manual = 0
    for name in ('.Lribbon_gender_male', '.Lribbon_gender_female',
                 '.Lribbon_gender_unknown', '.Lribbon_count_unit'):
        body = asm.split(name + ':', 1)[1].split('\n.', 1)[0]
        data = b''.join(bytes(int(v, 0) for v in row.split(','))
                        for row in re.findall(r'^\s*\.byte (.+)$', body, re.M))
        assert not scan(data), name
        manual += 1
    for source, name in (('safari_display.c', 'title'), ('safari_display.c', 'format')):
        text = (ROOT / 'patch' / source).read_text()
        body = re.search(r'\b' + name + r'\[\] = \{([^}]+)\}', text)[1]
        assert not scan(bytes(int(v, 0) for v in body.split(','))), name
        manual += 1
    # box_name_display.c only constructs BOX + space + decimal digits;
    # symbols cannot be generated by its LABEL1/LABEL2 macros.
    report = dict(rom_crc32=f'{zlib.crc32(rom):08X}', generated_text_vectors=vectors,
                  npc_text_vectors=npc_vectors, handwritten_buffers=manual,
                  excluded_binary_pokedex_vectors=binary,
                  generated_bytes_verified_in_rom=byte_count, findings=findings,
                  scope='Build-generated translated text, separately generated NPC strings, handwritten display buffers; Japanese player/link/save strings are preserved.')
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False))
    assert not findings, 'Unescaped Latin symbols remain'


if __name__ == '__main__':
    main()
