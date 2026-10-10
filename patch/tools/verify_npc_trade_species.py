"""Execute NPC trade species producers and render their Chinese display tokens."""
import argparse
import json
import struct
from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_R3, UC_ARM_REG_R4, UC_ARM_REG_R6
from verify_remaining_display_port import Machine, symbols, ROOT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names.update(TradeSpecies=0x0807E174, TradeNames=0x0807E1C4,
                   SetMonData=0x0806A774, Expand=0x08008BCC)
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    # Wokann dev trade.c: 60-byte records, received species +12, requested +56.
    table, stride = 0x0830D114, 60
    assert rom[0x30D114:0x30D204] == base[0x30D114:0x30D204]
    for start, end, literal in ((0x7E174, 0x7E1C4, 0x7E1BC),
                                (0x7E1C4, 0x7E228, 0x7E224)):
        assert m.word(0x08000000 + literal) == m.names['ChsSpeciesNameTokens']
        restored = bytearray(rom[start:end])
        restored[literal - start:literal - start + 4] = base[literal:literal + 4]
        # Existing nickname-display hook is independent of these two literals.
        if start == 0x7E1C4:
            restored[0x7E1E6 - start:0x7E1EA - start] = base[0x7E1E6:0x7E1EA]
        assert restored == base[start:end]

    batches = [json.loads(p.read_text()) for p in (ROOT / 'patch/batches').glob('*.json')]
    prompts = ('RustboroCity_House1_Text_IllTradeIfYouWant',
               'FortreeCity_House1_Text_YouWillTradeWontYou',
               'PacifidlogTown_House3_Text_WillingToTradeIt',
               'BattleFrontier_Lounge6_Text_WouldYouLikeToTrade')
    prompt_symbols = {}
    for batch in batches:
        for text in batch.get('texts', []):
            if text.get('source_symbol') in prompts:
                prompt_symbols[text['source_symbol']] = text['name']
    assert set(prompt_symbols) == set(prompts)
    mon, value, output, printer, token_addr = 0x02024190, 0x02022000, 0x02023000, 0x02024000, 0x02025000
    saved, saved_size = 0x02028000, 0x8000
    m.cpu.mem_write(saved, b'\xa5' * saved_size)
    def token(species):
        return b'\xf5\xf2' + struct.pack('<H', species) + b'\xff'
    def set_data(field, data):
        m.cpu.mem_write(value, data + bytes(16))
        m.call('SetMonData', (mon, field, value))
    rendered = set()
    for index, prompt in enumerate(prompts):
        received = struct.unpack_from('<H', base, table - 0x08000000 + index * stride + 12)[0]
        requested = struct.unpack_from('<H', base, table - 0x08000000 + index * stride + 56)[0]
        m.cpu.mem_write(0x02037280, struct.pack('<HH', index, 0))
        m.cpu.mem_write(0x02021C40, b'\xa5' * 40)
        assert m.call('TradeSpecies') == requested
        assert m.string(0x02021C40) == token(requested)
        assert m.string(0x02021C54) == token(received)
        assert bytes(m.cpu.mem_read(0x02021C45, 15)) == b'\xa5' * 15
        assert bytes(m.cpu.mem_read(0x02021C59, 15)) == b'\xa5' * 15
        m.call('Expand', (output, m.names[prompt_symbols[prompt]]))
        assert token(requested)[:-1] in m.string(output)
        assert token(received)[:-1] in m.string(output)
        default_nickname = m.string(0x082EA31C + requested * 6)
        for nickname in (default_nickname, b'\x01\x02\x03\xff'):
            m.cpu.mem_write(mon, bytes(100))
            set_data(11, struct.pack('<H', requested))
            set_data(2, nickname)
            before = bytes(m.cpu.mem_read(mon, 100))
            m.call('TradeNames')
            assert m.string(0x02021C40) == (token(requested) if nickname == default_nickname else nickname)
            assert m.string(0x02021C54) == token(received)
            assert bytes(m.cpu.mem_read(mon, 100)) == before
        for species in (requested, received):
            if species in rendered:
                continue
            # The renderer must resolve tokens even inside a JP-mode placeholder.
            m.cpu.mem_write(token_addr, token(species))
            m.cpu.mem_write(printer, bytes(32))
            m.cpu.mem_write(printer, struct.pack('<I', token_addr))
            glyphs = 0
            for _ in range(20):
                m.cpu.reg_write(UC_ARM_REG_R4, printer + 0x14)
                m.cpu.reg_write(UC_ARM_REG_R6, printer)
                m.call('ChineseRenderHook', (0,), (0x080059B2, 0x08005B32, 0x0800582C))
                end = m.cpu.reg_read(UC_ARM_REG_PC)
                if end == 0x08005B32:
                    glyphs += 1
                elif end == 0x0800582C:
                    assert m.cpu.reg_read(UC_ARM_REG_R3) == 255
                    break
            else:
                raise AssertionError('Species token did not reach EOS')
            assert glyphs >= 2
            rendered.add(species)
    assert bytes(m.cpu.mem_read(saved, saved_size)) == b'\xa5' * saved_size
    print('PASS: all four NPC trade offers and animation species; Chinese glyph rendering; '
          'requested species IDs, custom nicknames, Pokemon/save bytes and original trade records preserved')


if __name__ == '__main__':
    main()
