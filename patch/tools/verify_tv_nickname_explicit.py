#!/usr/bin/env python3
"""Verify explicit StringCopy10 entries against native copy and TV conversion."""
import argparse, struct
from unicorn.arm_const import UC_ARM_REG_LR,UC_ARM_REG_PC,UC_ARM_REG_R0,UC_ARM_REG_R1,UC_ARM_REG_R2,UC_ARM_REG_R4,UC_ARM_REG_R5,UC_ARM_REG_SP
from verify_remaining_display_port import Machine, symbols, ROOT
from verify_battle_nickname_direct import bl_target

def main():
 p=argparse.ArgumentParser();p.add_argument('--nm',default='arm-none-eabi-nm');a=p.parse_args();m=Machine(symbols(a.nm));u=m.cpu
 base=(ROOT/'baserom_jp.gba').read_bytes();rom=(ROOT/'pokeemerald_jp_chs.gba').read_bytes()
 groups=[((0x080F1FB4,0x080F30EA),0x08008838,UC_ARM_REG_R4,2),((0x080F26D8,0x080F276C,0x080F28D8),0x08008840,UC_ARM_REG_R5,2),((0x080F2998,0x080F2A2C,0x080F2AA0,0x080F2AE6,0x080F2B16),0x08008848,UC_ARM_REG_R5,16)]
 for sites,target,reg,offset in groups:
  for site in sites:
   assert bl_target(base,site)==0x08008828 and bl_target(rom,site)==target
   for original in (True,False):
    species=25;jp=m.string(0x082EA31C+species*6);nickname=jp if original else b'\xa1\xa2\xff';src,dest,record=0x02010000,0x02011000,0x02012000
    u.mem_write(src,nickname+bytes(16));u.mem_write(dest,b'\xa5'*32);u.mem_write(record+offset,struct.pack('<H',species));m.stop_addresses={site+4};u.reg_write(UC_ARM_REG_SP,0x03007800);u.reg_write(UC_ARM_REG_LR,0x0203F001);u.reg_write(UC_ARM_REG_R0,dest);u.reg_write(UC_ARM_REG_R1,src);u.reg_write(reg,record);u.emu_start(site|1,0,count=200000)
    assert u.reg_read(UC_ARM_REG_PC)==site+4 and u.reg_read(UC_ARM_REG_SP)==0x03007800
    expected=b'\xf5\xf2\x19\x00\xff' if original else nickname
    assert m.string(dest)==expected,(hex(site),m.string(dest),expected)
    assert u.reg_read(UC_ARM_REG_R0)==dest
 for nickname in (b'\xff',b'\xa1\xa2\xff',b'\xa1\xa2\xa3\xa4\xa5\xa6\xff'):
  src,dest=0x02010000,0x02011000;u.mem_write(src,nickname);u.mem_write(dest,b'\xa5'*32);m.names['OriginalCopy10']=0x08008828
  got=m.call('OriginalCopy10',(dest,src));expected=nickname[:5].split(b'\xff')[0]+b'\xff';assert m.string(dest)==expected and got==dest+len(expected)-1
 print('PASS: 10 explicit TV call sites, 3 species sources, default/custom names and original StringCopy10 behavior')
if __name__=='__main__':main()
