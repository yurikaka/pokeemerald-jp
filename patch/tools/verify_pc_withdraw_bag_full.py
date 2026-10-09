"""Exercise native PC withdrawal branches with bag/graphics endpoints stubbed."""
import argparse
import struct
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_LR, UC_ARM_REG_PC, UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_SP
from verify_remaining_display_port import Machine, symbols, ROOT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nm', default='arm-none-eabi-nm')
    args = parser.parse_args()
    m = Machine(symbols(args.nm))
    m.names.update(NativeResponse=0x0816C070, NativeWithdraw=0x0816C70C)
    expected = m.names['Chs_ChecklistLiteral_448_gText_BagIsFull2']
    assert m.word(0x0816C0E0) == expected
    assert m.call('NativeResponse', (0xFFFA,)) == expected
    for code, symbol in ((0xFFFE, 'Chs_ChecklistLiteral_476_gText_WithdrawHowManyItems'),
                         (0xFFFD, 'Chs_ChecklistLiteral_476_gText_WithdrawXItems')):
        assert m.call('NativeResponse', (code,)) == m.names[symbol]
    rom = (ROOT / 'pokeemerald_jp_chs.gba').read_bytes()
    base = (ROOT / 'baserom_jp.gba').read_bytes()
    # Only a response literal changed. Item manipulation, task state, quantity,
    # successful branch and failed branch remain original machine instructions.
    assert rom[0x16C70C:0x16C7C8] == base[0x16C70C:0x16C7C8]
    for start, end in ((0x16C070, 0x16C0B8), (0x16C0DC, 0x16C0E0),
                       (0x16C102, 0x16C148)):
        assert rom[start:end] == base[start:end]
    saved, saved_size = 0x02028000, 0x10000
    task_data = m.word(0x0816C780)
    captured, bag_calls = [], []
    bag_success = False

    def stub(cpu, address, size, unused):
        if address == 0x080D6140:
            bag_calls.append((cpu.reg_read(UC_ARM_REG_R0), cpu.reg_read(UC_ARM_REG_R1)))
            cpu.reg_write(UC_ARM_REG_R0, int(bag_success))
        elif address == 0x0816C108:
            pointer = cpu.reg_read(UC_ARM_REG_R0)
            captured.append((pointer, m.string(pointer)))
        else:
            return
        cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

    m.cpu.hook_add(UC_HOOK_CODE, stub)
    for bag_success in (False, True):
        m.cpu.mem_write(saved, b'\xa5' * saved_size)
        m.cpu.mem_write(m.word(0x0816C788), struct.pack('<I', saved))
        m.cpu.mem_write(saved + 0x498, struct.pack('<HH', 13, 10))
        m.cpu.mem_write(m.word(0x0816C784), bytes(4))
        m.cpu.mem_write(task_data - 8, bytes(40))
        m.cpu.mem_write(task_data + 4, struct.pack('<H', 1))
        before = bytes(m.cpu.mem_read(saved, saved_size))
        m.call('NativeWithdraw', (0,))
        assert bag_calls[-1] == (13, 1)
        result_symbol = ('Chs_ChecklistLiteral_476_gText_WithdrawXItems' if bag_success
                         else 'Chs_ChecklistLiteral_448_gText_BagIsFull2')
        assert captured[-1][0] == m.names[result_symbol]
        assert captured[-1][1] == m.string(m.names[result_symbol])
        assert bytes(m.cpu.mem_read(saved, saved_size)) == before
        assert m.word(task_data - 8) == m.word(0x0816C798 if bag_success else 0x0816C7C4)
        quantity = struct.unpack('<H', m.cpu.mem_read(task_data + 4, 2))[0]
        assert quantity == int(bag_success)
        assert m.cpu.reg_read(UC_ARM_REG_SP) == 0x03007800
    # The PC response has no wait-control code; the task handles confirmation.
    assert b'\xfc\x09' not in m.string(expected)
    print('PASS: native PC withdrawal success/failure paths and response selection; Chinese bag-full text; unchanged item code, quantities, task callbacks, stack and save data (bag/graphics endpoints stubbed)')


if __name__ == '__main__':
    main()
