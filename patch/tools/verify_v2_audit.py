#!/usr/bin/env python3
"""Verify v2 audit mappings against current payloads and preserve row-level decisions."""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess
import sys
import warnings

ROOT = Path(__file__).resolve().parents[2]
US = ROOT.parent / 'pokeemerald_us_chs'
WOKANN = ROOT.parent / 'pokeemerald_wokann_dev'
sys.path.insert(0, str(ROOT / 'patch/tools'))
from build_texts import read_charmap, encode_text, encode_compact_chinese_text, convert_us_encoded_text, wrap_dialogue, wrap_pokedex_description
from port_map_dialogue import read_charmap as read_source_charmap
from review_text_checklists import read_sources, encode_source_controls

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def primary(text):
    return text.split('$')[0]

def canonical(text):
    return primary(text).replace('\\n', '\n').replace('\n', '').rstrip('。')

def number(value):
    return int(value, 0) if isinstance(value, str) else value

class Verification:
    def __init__(self, nm):
        self.rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
        self.base = (ROOT / 'baserom_jp.gba').read_bytes()
        self.charmap = read_charmap(ROOT / 'patch/charmap_chs.txt')
        self.source_charmap = read_source_charmap(US / 'charmap.txt')
        self.jp_charmap = read_source_charmap(WOKANN / 'charmap.txt')
        self.symbols = {}
        for line in subprocess.check_output([nm, '-n', str(ROOT / 'build/patch/payload.elf')], text=True).splitlines():
            fields = line.split()
            if len(fields) == 3:
                self.symbols[fields[2]] = int(fields[0], 16)
        self.us_sources = read_sources(US)
        self.jp_sources = read_sources(WOKANN)
        self.definitions = {}
        self.by_source = defaultdict(list)
        self.by_original = defaultdict(list)
        self.references = []
        self.documents = []
        for path in [ROOT / 'patch/texts.json', *sorted((ROOT / 'patch/batches').glob('*.json'))]:
            document = json.loads(path.read_text())
            self.documents.append((path, document))
            entries = document if isinstance(document, list) else document.get('texts', [])
            for entry in entries:
                self.definitions[entry['name']] = (path, document, entry)
                symbol = entry.get('source_symbol', entry['name'].removeprefix('Chs_'))
                self.by_source[symbol].append(entry['name'])
                for alias in entry.get('additional_source_symbols', []):
                    self.by_source[alias].append(entry['name'])
            if isinstance(document, dict):
                for entry in document.get('reference_writes', []):
                    if 'original' in entry:
                        record = dict(entry, batch=str(path.relative_to(ROOT)))
                        self.references.append(record)
                        self.by_original[number(entry['original'])].append(record)
        self.manifest = json.loads((ROOT / 'patch/manifest.json').read_text())
        for entry in self.manifest.get('pointer_writes', []):
            if 'original' in entry:
                record = dict(entry, batch='patch/manifest.json')
                self.references.append(record)
                self.by_original[number(entry['original'])].append(record)
        self.prior = json.loads((ROOT / 'patch/mapping_reports/checklists_action_plan_2026-10-02.json').read_text())
        self.prior_by_source = defaultdict(list)
        for record in self.prior['records']:
            if record.get('symbol'):
                self.prior_by_source[record['symbol']].append(record)
        self.tables = {}
        self.resource_by_source = defaultdict(list)
        self.table_evidence = {}
        self.payload_evidence = {}
        self.objects = {}
        self.index_tables()
        for replacement in self.manifest.get('pointer_replacements', []):
            original = number(replacement['old'])
            encoded = struct.pack('<I', original)
            excluded = {number(value) for value in replacement.get('exclude', [])}
            for offset in range(0, len(self.base) - 3, 4):
                if self.base[offset:offset + 4] != encoded or offset + 0x08000000 in excluded:
                    continue
                target = self.symbols.get(replacement['symbol'])
                if target is not None and self.word(offset + 0x08000000) == target:
                    self.by_original[original].append(dict(symbol=replacement['symbol'], address=hex(offset + 0x08000000), original=hex(original)))

    def word(self, address, base=False):
        return struct.unpack_from('<I', self.base if base else self.rom, address - 0x08000000)[0]

    def bytes_match(self, address, expected):
        if self.rom[address - 0x08000000:address - 0x08000000 + len(expected)] != expected:
            raise ValueError(('ROM payload mismatch', hex(address), expected.hex()))

    def payload(self, name):
        if name in self.payload_evidence:
            return self.payload_evidence[name]
        if name not in self.definitions:
            return None
        path, document, entry = self.definitions[name]
        if 'us_encoded_hex' in entry:
            expected = convert_us_encoded_text(bytes.fromhex(entry['us_encoded_hex']), set(entry.get('japanese_placeholders', [])), entry.get('japanese_dynamic', False), entry.get('initial_japanese', False))
        else:
            expected = encode_text(entry['text'], self.charmap, entry.get('styled', False))
        auto_wrap = isinstance(document, dict) and 'dialogue' in document.get('category', '').lower()
        if entry.get('auto_wrap', auto_wrap):
            expected, _ = wrap_dialogue(expected, self.charmap)
        address = self.symbols[name]
        if entry.get('compact_resource'):
            token = self.rom[address - 0x08000000:address - 0x08000000 + 4]
            if token[:2] != b'\xf5\xf1' or token[-1] != 255:
                raise ValueError(('invalid compact resource', name))
            resource_address = self.word(self.symbols['ChsDisplayResourceNames'] + token[2] * 4)
            display_expected = expected
            self.bytes_match(resource_address, display_expected)
            expected = token
        self.bytes_match(address, expected)
        references = []
        for record in self.references:
            if record['symbol'] != name:
                continue
            reference_address = number(record['address'])
            target = address + number(record.get('offset', 0))
            if self.word(reference_address, base=True) != number(record['original']):
                raise ValueError(('base pointer mismatch', record))
            if self.word(reference_address) != target:
                raise ValueError(('live pointer mismatch', record))
            references.append({'address': record['address'], 'original': record['original'], 'target': f'0x{target:08X}', 'batch': record['batch']})
        result = {'payload_symbol': name, 'file': str(path.relative_to(ROOT)), 'payload_address': f'0x{address:08X}', 'payload_sha256': hashlib.sha256(expected).hexdigest(), 'rom_bytes_match': True, 'references': references}
        self.payload_evidence[name] = result
        return result

    def table(self, filename, index, field=None):
        key = (filename, index, field)
        if key in self.table_evidence:
            return self.table_evidence[key]
        document = self.tables[filename]
        address = self.symbols[document['name']]
        kind = document['kind']
        if kind == 'us_decoration_table':
            names = re.findall(r'\.description\s*=\s*(DecorDesc_\w+)', (US / 'src/data/decoration/header.h').read_text())
            text = self.us_sources[names[index]][0]['text']
            address = self.word(address + index * document['stride'] + document['description_offset'])
            expected = encode_text(text, self.charmap, False)
        elif kind == 'us_berry_info_table':
            part = field or 1
            names = re.findall(r'static const u8 (sBerryDescriptionPart' + str(part) + r'_\w+)\[\]', (US / 'src/berry.c').read_text())
            text = self.us_sources[names[index]][0]['text']
            address = self.word(address + (index + 1) * 28 + 8 + part * 4)
            side_address = self.word(self.symbols['ChsBerryDescriptionPart' + str(part)] + index * 4)
            if address != side_address:
                raise ValueError(('berry description pointer mismatch', index, part))
            expected = encode_text(text, self.charmap, False)
        elif kind == 'pokedex_entries':
            text = document['entries'][index]['description']
            pointer_address = address + index * 28 + 12
            address = self.word(pointer_address)
            expected = encode_text(text, self.charmap, False)
            if index:
                expected = wrap_pokedex_description(expected, self.charmap)
        elif kind == 'us_region_map_table':
            sections = json.loads((US / 'src/data/region_map/region_map_sections.json').read_text())['map_sections']
            text = sections[index]['name'].replace('{AQUA}', '海洋')
            pointer_address = address + index * document['stride'] + document['name_offset']
            original_offset = number(document['base_offset']) + index * document['stride']
            if self.rom[self.symbols[document['name']] - 0x08000000 + index * document['stride']:pointer_address - 0x08000000] != self.base[original_offset:original_offset + document['name_offset']]:
                raise ValueError(('region nontext fields changed', index))
            address = self.word(pointer_address)
            expected = encode_text(text, self.charmap, False)
        else:
            text = document['strings'][index]
            expected = (encode_compact_chinese_text(text, self.charmap) if document.get('compact_chinese') else encode_text(text, self.charmap, False))
            if kind == 'fixed_string_table':
                address += index * document['stride']
            elif kind == 'string_pointer_table':
                address = self.word(address + index * 4)
            else:
                raise ValueError(('unsupported table', filename))
        self.bytes_match(address, expected)
        result = {'file': 'patch/' + filename, 'table': document['name'], 'index': index, 'text': text, 'rom_address': f'0x{address:08X}', 'encoded_sha256': hashlib.sha256(expected).hexdigest(), 'rom_bytes_match': True}
        self.table_evidence[key] = result
        return result

    def index_tables(self):
        for path in (ROOT / 'patch').glob('*.json'):
            document = json.loads(path.read_text())
            if isinstance(document, dict) and document.get('kind') in ['fixed_string_table', 'string_pointer_table', 'pokedex_entries', 'us_region_map_table', 'us_decoration_table', 'us_berry_info_table']:
                self.tables[path.name] = document
        for index, symbol in enumerate(re.findall(r'\.description\s*=\s*(DecorDesc_\w+)', (US / 'src/data/decoration/header.h').read_text())):
            self.resource_by_source[symbol].append(('decoration_info.json', index))
        for part in (1, 2):
            names = re.findall(r'static const u8 (sBerryDescriptionPart' + str(part) + r'_\w+)\[\]', (US / 'src/berry.c').read_text())
            for index, symbol in enumerate(names):
                self.resource_by_source[symbol].append(('berry_info.json', index, part))
        for source_file, constant_file, prefix, table in [('src/data/text/move_descriptions.h', 'moves.h', 'MOVE', 'move_descriptions.json'), ('src/data/text/abilities.h', 'abilities.h', 'ABILITY', 'ability_descriptions.json')]:
            constants = {name: int(value, 0) for name, value in re.findall(r'^#define\s+(\w+)\s+(0x[0-9a-fA-F]+|\d+)\s*$', (US / 'include/constants' / constant_file).read_text(), re.M)}
            for identifier, symbol in re.findall(r'\[(' + prefix + r'_\w+)(?:\s*-\s*1)?\]\s*=\s*(\w+)', (US / source_file).read_text()):
                if identifier in constants:
                    self.resource_by_source[symbol].append((table, constants[identifier]))
        for index, symbol in enumerate(re.findall(r'\.description\s*=\s*(\w+)', (US / 'src/data/items.h').read_text())):
            self.resource_by_source[symbol].append(('item_descriptions.json', index))
        dex_names = re.findall(r'const u8 (g\w+PokedexText)\[\]', (US / 'src/data/pokemon/pokedex_text.h').read_text())
        if len(dex_names) != len(self.tables['pokedex_entries.json']['entries']):
            raise ValueError(('Pokedex source count mismatch', len(dex_names)))
        for index, symbol in enumerate(dex_names):
            self.resource_by_source[symbol].append(('pokedex_entries.json', index))
        sections = json.loads((US / 'src/data/region_map/region_map_sections.json').read_text())['map_sections']
        for index, section in enumerate(sections):
            self.resource_by_source[section['id']].append(('region_map_names.json', index))

    def source_proof(self, symbol):
        sources = self.us_sources.get(symbol, [])
        jp_sources = self.jp_sources.get(symbol, [])
        return {'us_sources': sources, 'wokann_sources': jp_sources}

    def mapping(self, symbol):
        evidence = []
        for name in self.by_source.get(symbol, []):
            if name in self.symbols:
                result = self.payload(name)
                if result:
                    evidence.append(result)
        common_name = 'Chs' + symbol.removeprefix('gText_')
        if common_name in self.symbols:
            result = self.payload(common_name)
            if result:
                evidence.append(result)
        for resource in self.resource_by_source.get(symbol, []):
            evidence.append(self.table(*resource))
        array = re.fullmatch(r'(gMoveNames|gAbilityNames|gRegionMapEntries)\[(\d+)\](?:\.name)?', symbol)
        stat_indices = {'sText_Attack2': 1, 'sText_Defense2': 2, 'sText_Speed': 3, 'sText_SpAtk2': 4, 'sText_SpDef2': 5}
        if symbol in stat_indices:
            evidence.append(self.table('battle_stat_names.json', stat_indices[symbol]))
        if array:
            table = {'gMoveNames': 'move_names.json', 'gAbilityNames': 'ability_names.json', 'gRegionMapEntries': 'region_map_names.json'}[array[1]]
            evidence.append(self.table(table, int(array[2])))
        for record in self.prior_by_source.get(symbol, []):
            for proof in record.get('existing_override_rom_evidence', []):
                name = proof.get('payload_symbol')
                result = self.payload(name)
                if result and self.word(number(proof['address'])) == self.symbols[name]:
                    if result not in evidence:
                        evidence.append(dict(result, existing_pointer_address=proof['address']))
            for proof in record.get('existing_override_conflicts', []):
                address = number(proof['address'])
                current = self.word(address)
                for name in self.definitions:
                    if self.symbols.get(name) == current:
                        result = self.payload(name)
                        if result and result not in evidence:
                            evidence.append(dict(result, existing_pointer_address=proof['address']))
            if record.get('jp_address'):
                for reference in self.by_original.get(number(record['jp_address']), []):
                    result = self.payload(reference['symbol'])
                    if result and result not in evidence:
                        evidence.append(result)
            for proof in record.get('resource_evidence', []):
                filename = Path(proof.get('file', '')).name
                if filename in self.tables:
                    part = 2 if proof.get('table') == 'ChsBerryDescriptionPart2' else None
                    result = self.table(filename, proof['index'], part)
                    if result not in evidence:
                        evidence.append(result)
        return evidence

    def dormant(self, symbol):
        evidence = []
        for record in self.prior_by_source.get(symbol, []):
            if record.get('execution') not in ['no_active_script_consumer', 'dormant_dead_script_text', 'dormant_unused_both_regions', 'no_port_needed_explicit_unused']:
                continue
            for field in ['dormant_script_review', 'unused_definition_review', 'dormant_script_evidence']:
                if field in record:
                    evidence.append({field: record[field]})
            if record.get('jp_address'):
                address = number(record['jp_address'])
                end = self.base.find(b'\xff', address - 0x08000000)
                if end < 0:
                    raise ValueError(('dormant text lacks EOS', symbol))
                length = end - (address - 0x08000000) + 1
                if self.rom[address - 0x08000000:address - 0x08000000 + length] != self.base[address - 0x08000000:address - 0x08000000 + length]:
                    return []
                evidence.append({'native_address': record['jp_address'], 'native_text_unchanged': True, 'historical_execution': record['execution']})
        return evidence

    def verify_consumer(self, record):
        from build_berry_tag_gfx import lzdec

        for source in record['source_file_hashes']:
            path = ROOT.parent / source['region'] / source['file']
            if digest(path) != source['sha256']:
                raise ValueError(('consumer source changed', record['symbol'], source))
        for name in record['aliases_payloads']:
            if not self.payload(name):
                raise ValueError(('missing consumer payload', name))
        for pointer in record['pointer_expectations']:
            if self.word(number(pointer['address'])) != number(pointer['target']):
                raise ValueError(('consumer pointer mismatch', pointer))
        for resource in record['graphics']:
            address = self.word(number(resource['pointer_address']))
            if address != self.symbols[resource['payload_symbol']]:
                raise ValueError(('graphic pointer mismatch', resource))
            expected = (ROOT / resource['file']).read_bytes()
            actual = lzdec(self.rom, address) if resource['compressed'] else self.rom[address - 0x08000000:address - 0x08000000 + len(expected)]
            if actual != expected or hashlib.sha256(actual).hexdigest() != resource['decompressed_sha256']:
                raise ValueError(('consumer graphic mismatch', resource))
        for reference in record.get('implementation', {}).get('wokann_references', []):
            path = WOKANN / reference['object']
            if digest(path) != reference['object_sha256']:
                raise ValueError(('consumer object changed', reference))

def main():
    warnings.filterwarnings('ignore', category=SyntaxWarning)
    parser = argparse.ArgumentParser()
    parser.add_argument('--decisions', type=Path, required=True)
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    parser.add_argument('--consumers', type=Path, default=ROOT / 'patch/mapping_reports/v2_audit_consumer_decisions_2026-10-04.json')
    args = parser.parse_args()
    verification = Verification(args.nm)
    decisions = json.loads(args.decisions.read_text())
    decisions_by_row = {entry['row_number']: entry for entry in decisions.values()}
    consumers = json.loads(args.consumers.read_text())['records']
    consumers_by_row = {entry['row_number']: entry for entry in consumers}
    for consumer in consumers:
        verification.verify_consumer(consumer)
    path = ROOT / 'report/v2/audit_merged_04df993_2026-10-04.csv'
    rows = list(csv.DictReader(path.open()))
    result = []
    for row_number, row in enumerate(rows, 2):
        symbol = row['us_symbol']
        record = {'row_number': row_number, 'domain': row['domain'], 'idx': row['idx'], 'symbol': symbol, 'reported_verdict': row['verdict']}
        evidence = verification.mapping(symbol) if symbol else []
        if row['domain'] == 'ability_move':
            filename = {'ability/name': 'ability_names.json', 'ability/description': 'ability_descriptions.json', 'move/name': 'move_names.json', 'move/description': 'move_descriptions.json'}[row['type_kind']]
            evidence.append(verification.table(filename, int(row['idx'])))
        elif row['domain'] == 'pokedex':
            evidence.append(verification.table('pokedex_entries.json', int(row['idx'])))
        elif row['domain'] == 'item':
            evidence.append(verification.table('item_descriptions.json', int(row['idx'])))
        record['mapping_evidence'] = evidence
        if row_number in decisions_by_row:
            decision = decisions_by_row[row_number]
            record['review'] = decision
            record['reported_reason'] = row['reason']
            record['reported_japanese'] = row['jp_text']
            record['reported_english'] = row['en_text']
            record['reported_chinese'] = row['chs_text']
            record['source_evidence'] = verification.source_proof(decision.get('resolved_symbol', symbol))
            if decision['action'] == 'fix':
                scope = decision.get('scope', 'both')
                if scope != 'us_only' and not evidence:
                    for file in decision.get('changed_files', []):
                        if file.startswith('patch/batches/'):
                            document = json.loads((ROOT / file).read_text())
                            for entry in document['texts']:
                                if primary(entry.get('text', '')) == primary(decision['final_text']):
                                    proof = verification.payload(entry['name'])
                                    if proof:
                                        evidence.append(proof)
                if scope != 'us_only' and not evidence:
                    raise ValueError(('fixed row has no verified JP payload', record))
                record['decision'] = 'fixed_verified' if scope != 'us_only' else 'fixed_us_only'
            elif decision['action'] == 'verify_mapping':
                record['decision'] = 'already_ported_verified' if evidence else 'mapping_requires_trace'
            else:
                record['decision'] = decision['action']
        elif row['verdict'] == 'UNTRANSPLANTED':
            record['reported_reason'] = row['reason']
            record['source_evidence'] = verification.source_proof(symbol)
            if row_number in consumers_by_row:
                consumer = consumers_by_row[row_number]
                if consumer['symbol'] != symbol:
                    raise ValueError(('consumer row mismatch', row_number, symbol))
                record['decision'] = consumer['decision']
                record['consumer_review'] = consumer
            elif evidence:
                record['decision'] = 'already_ported_verified'
            else:
                dormant = verification.dormant(symbol)
                if dormant:
                    record['decision'] = 'dormant_original_retained'
                    record['dormant_evidence'] = dormant
                else:
                    record['decision'] = 'requires_consumer_trace'
                    record['historical_execution'] = [entry.get('execution') for entry in verification.prior_by_source.get(symbol, [])]
        else:
            record['decision'] = 'mapping_verified_semantics_not_reaudited' if evidence else 'reported_ok_not_independently_verified'
        result.append(record)
    report = {'date': '2026-10-04', 'input': str(path.relative_to(ROOT)), 'input_sha256': digest(path), 'jp_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(), 'us_head': subprocess.check_output(['git', '-C', str(US), 'rev-parse', 'HEAD'], text=True).strip(), 'wokann_head': subprocess.check_output(['git', '-C', str(WOKANN), 'rev-parse', 'HEAD'], text=True).strip(), 'jp_rom_sha256': digest(ROOT / 'pokeemerald_jp_chs.gba'), 'base_rom_sha256': digest(ROOT / 'baserom_jp.gba'), 'policy': 'All rows receive a mapping classification. ERROR and NEEDS_ATTENTION rows receive explicit reviews. An OK row mapping proof is not a new semantic sign-off. A retained dormant or regional row is not an active missing translation. Full emulator gameplay is not claimed.', 'summary': dict(Counter(record['decision'] for record in result)), 'flagged_summary': dict(Counter(record['decision'] for record in result if record['reported_verdict'] in ['ERROR', 'NEEDS_ATTENTION'])), 'untransplanted_summary': dict(Counter(record['decision'] for record in result if record['reported_verdict'] == 'UNTRANSPLANTED')), 'records': result}
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
