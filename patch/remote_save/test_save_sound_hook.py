from unicorn import Uc,UC_ARCH_ARM,UC_MODE_THUMB,UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_PC,UC_ARM_REG_SP,UC_ARM_REG_LR,UC_ARM_REG_R0
from pathlib import Path
import struct
import subprocess
import sys
rom=Path(sys.argv[1]).read_bytes()
prefix=sys.argv[2]
syms={p[2]:int(p[0],16) for l in subprocess.check_output([prefix+'nm','build/patch/payload.elf'],text=True).splitlines() if len(p:=l.split())==3}
for active,flash,damaged in [(1,1,0),(1,1,1),(1,0,0),(0,1,0)]:
 u=Uc(UC_ARCH_ARM,UC_MODE_THUMB);u.mem_map(0x08000000,0x2000000);u.mem_write(0x08000000,rom);u.mem_map(0x03000000,0x8000);u.mem_map(0x04000000,0x10000)
 def w(a,v):u.mem_write(a,struct.pack('<I',v))
 w(0x03007ff0,0x03006120);w(0x03006120,0x68736d53);w(0x030075e4,0xa75d0000 if active else 0);w(0x03005ae8,flash);w(0x03005f3c,damaged)
 u.mem_write(0x04000080,struct.pack('<HH',0xff77,0xbb0f));u.reg_write(UC_ARM_REG_SP,0x03007e40);u.reg_write(UC_ARM_REG_LR,0x08000101);u.reg_write(UC_ARM_REG_R0,0);events=[]
 def hook(u,a,size,z):
  if a in (0x0828ecec,0x0828ed68):
   v=struct.unpack('<I',u.mem_read(0x03006120,4))[0];events.append('off' if a==0x0828ecec else 'on');w(0x03006120,v+(10 if a==0x0828ecec else -10));u.reg_write(UC_ARM_REG_PC,u.reg_read(UC_ARM_REG_LR))
  elif a in (syms['RemoteJpSaveCheck'],syms['RemoteJpSaveCommit']):
   u.reg_write(UC_ARM_REG_R0,1);u.reg_write(UC_ARM_REG_PC,u.reg_read(UC_ARM_REG_LR))
  elif a==0x08153154:
   l,h=struct.unpack('<HH',u.mem_read(0x04000080,4));assert (l,h)==((0x0077,0x880f) if active else (0xff77,0xbb0f)),(hex(l),hex(h));events.append('save');u.reg_write(UC_ARM_REG_PC,u.reg_read(UC_ARM_REG_LR))
  elif a==0x08178e48: events.append('failure');u.reg_write(UC_ARM_REG_PC,u.reg_read(UC_ARM_REG_LR))
  elif a==0x08000100:u.emu_stop()
 u.hook_add(UC_HOOK_CODE,hook);u.emu_start(0x08153275,0,count=10000)
 expected=(['off'] if active else [])+(['save'] if flash else [])+(['failure'] if flash and damaged else [])+(['on'] if active else [])
 assert events==expected,(events,expected)
 assert u.reg_read(UC_ARM_REG_R0)==(1 if flash and not damaged else 255)
 assert struct.unpack('<HH',u.mem_read(0x04000080,4))==(0xff77,0xbb0f)
 assert u.reg_read(UC_ARM_REG_SP)==0x03007e40
 print(active,flash,damaged,events)
