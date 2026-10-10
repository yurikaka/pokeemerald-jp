"""Audit translated script messages that originally had no page/button prompt."""
import argparse
import json
import re
from pathlib import Path
from verify_remaining_display_port import Machine, ROOT, symbols
from build_texts import line_width, tokenize_line


def read_string(data, offset):
    end = data.index(255, offset)
    return data[offset:end + 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    parser.add_argument('--source-root', type=Path, default=ROOT.parent / 'pokeemerald_wokann_dev')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    definitions, references, uses = {}, {}, {}
    for path in (ROOT / 'patch/batches').glob('*.json'):
        document = json.loads(path.read_text())
        if not isinstance(document, dict):
            continue
        for definition in document.get('texts', []):
            definitions[definition.get('source_symbol', definition['name'])] = definition
        for reference in document.get('reference_writes', []):
            if 'source_symbol' in reference:
                references.setdefault(reference['source_symbol'], []).append(reference)
    sites = 0
    for path in (args.source_root / 'data').rglob('*'):
        if path.suffix not in ('.inc', '.s'):
            continue
        for number, line in enumerate(path.read_text().splitlines(), 1):
            match = re.match(r'\s*(message|msgbox)\s+(\w+)(?:,\s*(\w+))?', line)
            if not match:
                continue
            command, name, kind = match.groups()
            if command == 'msgbox' and kind != 'MSGBOX_GETPOINTS':
                continue
            sites += 1
            uses.setdefault(name, []).append(f'{path.relative_to(args.source_root)}:{number}')
    checked = protected = 0
    failures = []
    for source, locations in uses.items():
        if source not in definitions or source not in references:
            continue  # NULL/string variables and texts outside the literal patch tables.
        definition = definitions[source]
        if definition['name'] not in m.names:
            continue
        checked += 1
        current = read_string(rom, m.names[definition['name']] - 0x08000000)
        for reference in references[source]:
            original = read_string(base, int(reference['original'], 16) - 0x08000000)
            if b'\xfa' in original or b'\xfb' in original:
                continue  # The Japanese message already intentionally waits within its text.
            protected += 1
            if any(token in (b'\xfa', b'\xfb') for token, _ in tokenize_line(current)):
                failures.append(f'{source}: introduced a button prompt ({locations[0]})')
            address = int(reference['address'], 16)
            assert m.word(address) == m.names[definition['name']], (source, hex(address))
    assert not failures, '\n'.join(failures)
    guarded = 0
    for definition in definitions.values():
        if not definition.get('no_manual_prompt'):
            continue
        guarded += 1
        current = read_string(rom, m.names[definition['name']] - 0x08000000)
        widths = {int(k): v for k, v in definition.get('placeholder_widths', {}).items()}
        lines = current[:-1].split(b'\xfe')
        assert len(lines) <= 2
        assert all(line_width(line, widths) <= 168 for line in lines), definition['name']
        assert not any(token in (b'\xfa', b'\xfb') for token, _ in tokenize_line(current))
    # MSGBOX_GETPOINTS stays message/playfanfare/waitfanfare/waitmessage/return.
    standard = int.from_bytes(base[0x1DB7BC + 9 * 4:0x1DB7BC + 10 * 4], 'little')
    offset = standard - 0x08000000
    assert base[offset:offset + 11] == rom[offset:offset + 11]
    assert base[0x23896F:0x238973] == rom[0x23896F:0x238973]
    # Expand all real NPC contestant names through the native placeholder routine.
    m.names['Expand'] = 0x08008BCC
    label = m.names['Chs_ContestHall_Text_EntryXTrainersMon']
    for index in range(96):
        m.cpu.mem_write(0x02021C40, m.string(m.names[f'ChsRemaining_ContestTrainer_{index}']))
        m.cpu.mem_write(0x02021C54, b'\xA2\xFF')
        m.cpu.mem_write(0x02021C68, m.string(m.names[f'ChsRemaining_ContestNickname_{index}']))
        m.call('Expand', (0x02023000, label))
        expanded = m.string(0x02023000)
        assert not any(token in (b'\xFA', b'\xFB') for token, _ in tokenize_line(expanded))
        assert all(line_width(line) <= 168 for line in expanded[:-1].split(b'\xFE')), index
    print(f'PASS: {sites} script message sites scanned; {checked} translated symbols checked; '
          f'{protected} original references without text prompts preserved; {guarded} guarded two-line messages; '
          'all 96 contestant name pairs fit; BP fanfare script unchanged')


if __name__ == '__main__':
    main()
