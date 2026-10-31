import struct,sys
from pathlib import Path
from unicorn import *
from unicorn.arm_const import *
root=Path('.');base=(root/'baserom_jp.gba').read_bytes();patched=(root/'pokeemerald_jp_chs.gba').read_bytes();stop=0x0203f000

def run(rom,font,data,spacing):
 u=Uc(UC_ARCH_ARM,UC_MODE_THUMB)
 for addr,size in [(0x08000000,0x2000000),(0x02000000,0x40000),(0x03000000,0x8000),(0x04000000,0x1000),(0x05000000,0x1000),(0x06000000,0x20000)]:u.mem_map(addr,size)
 u.mem_write(0x08000000,rom);u.mem_write(0x02001000,data);u.reg_write(UC_ARM_REG_SP,0x03007800);u.reg_write(UC_ARM_REG_LR,stop|1);u.reg_write(UC_ARM_REG_R0,font);u.reg_write(UC_ARM_REG_R1,0x02001000);u.reg_write(UC_ARM_REG_R2,spacing&0xffffffff)
 def hook(u,a,n,z):
  if a==stop:u.emu_stop()
 u.hook_add(UC_HOOK_CODE,hook);u.emu_start(0x08005dad,0,count=1000000);assert u.reg_read(UC_ARM_REG_PC)==stop,hex(u.reg_read(UC_ARM_REG_PC));assert u.reg_read(UC_ARM_REG_SP)==0x03007800
 return u.reg_read(UC_ARM_REG_R0)
for font in [0,1,2,3,4,5,6,7,8,9,10,255]:
 for data in [b'\xff',bytes.fromhex('bbbcbdff'),bytes.fromhex('a1a2a3a4ff'),bytes.fromhex('bbbcbdfebbcaff')]:
  for spacing in [-1,0,1,3]:
   a=run(base,font,data,spacing);b=run(patched,font,data,spacing);assert a==b,(font,data,spacing,a,b)
print('PASS: 192 native string-width comparisons; stack restored')
