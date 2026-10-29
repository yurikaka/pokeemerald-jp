from unicorn import Uc, UC_ARCH_ARM, UC_MODE_ARM, UC_HOOK_MEM_READ, UC_HOOK_MEM_WRITE
from unicorn.arm_const import UC_ARM_REG_PC, UC_ARM_REG_CPSR, UC_ARM_REG_SP
from pathlib import Path
import struct
import sys
from collections import deque
trace=deque(maxlen=100)
root=Path(__file__).resolve().parents[2]
rom=Path(sys.argv[1]).read_bytes()
cart=(root/'baserom_jp.gba').read_bytes()
recv=(root/'build/remote_save/box-connection-image.bin').read_bytes()
host=Path(sys.argv[2]).read_bytes()
def w16(cpu, a, v): cpu.mem_write(a, struct.pack('<H',v&0xffff))
def w32(cpu, a, v): cpu.mem_write(a, struct.pack('<I',v&0xffffffff))
def r16(cpu,a): return struct.unpack('<H',cpu.mem_read(a,2))[0]
def setup():
 u=Uc(UC_ARCH_ARM,UC_MODE_ARM)
 for a,n in [(0,0x4000),(0x02000000,0x40000),(0x03000000,0x8000),(0x04000000,0x10000),(0x08000000,0x2000000),(0x0e000000,0x10000),(0x06000000,0x20000),(0x05000000,0x1000),(0x07000000,0x1000)]:u.mem_map(a,n)
 return u
h=setup();s=setup();h.mem_write(0x08000000,rom);s.mem_write(0x08000000,cart);s.mem_write(0x02000000,recv);h.mem_write(0x02020000,host)
h.reg_write(UC_ARM_REG_PC,0x02020000);s.reg_write(UC_ARM_REG_PC,int(sys.argv[3],16));s.reg_write(UC_ARM_REG_CPSR,0x3f);s.reg_write(UC_ARM_REG_SP,0x03007f00)
class State:
 mastercnt=0x200b; slavecnt=0x600b; slaveif=0; slaveout=0xffff; masterin=0xffff; slavein=0xffff; transfers=0
 flash=bytearray(b'\xff'*131072); mode=0; bank=0; ident=False
st=State()
def mmio_read(u,access,a,size,value,tag):
 if a==0x04000006: w16(u,a,160)
 elif a==0x04000128: w16(u,a, st.mastercnt if tag=='h' else st.slavecnt)
 elif a==0x04000202 and tag=='s': w16(u,a,st.slaveif)
 elif a==0x04000122 and tag=='h': w16(u,a,st.masterin)
 elif a==0x04000120 and tag=='s': w16(u,a,st.slavein)
 elif tag=='s' and 0x0e000000 <= a < 0x0e010000:
  k=a-0x0e000000
  v=({0:0x62,1:0x13}.get(k,0xff) if st.ident else st.flash[st.bank*65536+k]);u.mem_write(a,bytes([v]))
def mmio_write(u,access,a,size,v,tag):
 if tag=='s' and a==0x04000202: st.slaveif &= ~(v&0xffff)
 elif tag=='s' and a==0x0400012a: st.slaveout=v&0xffff
 elif a==0x04000128:
  if tag=='s': st.slavecnt=(v&~0x80)|8
  else:
   st.mastercnt=(v&~0x80)|8
   if v&0x80:
    st.slavein=r16(h,0x0400012a);st.masterin=st.slaveout;st.slaveif|=0x80;st.transfers+=1;trace.append((st.slavein,st.masterin))
 elif tag=='s' and 0x0e000000<=a<0x0e010000:
  a-=0x0e000000;v&=255
  if a==0x5555 and v==0xf0 and st.mode!=3:st.ident=False;st.mode=0;return
  if st.mode==0:st.mode=1 if a==0x5555 and v==0xaa else 0
  elif st.mode==1:st.mode=2 if a==0x2aaa and v==0x55 else 0
  elif st.mode==2:
   st.mode=0
   if a==0x5555:
    if v==0x90:st.ident=True
    elif v==0xb0:st.mode=4
    elif v==0xa0:st.mode=3
    elif v==0x80:st.mode=5
  elif st.mode==3:st.flash[st.bank*65536+a]&=v;st.mode=0
  elif st.mode==4:st.bank=v&1;st.mode=0
  elif st.mode==5:st.mode=6 if a==0x5555 and v==0xaa else 0
  elif st.mode==6:st.mode=7 if a==0x2aaa and v==0x55 else 0
  elif st.mode==7:
   if v==0x30:st.flash[st.bank*65536+a:st.bank*65536+a+4096]=b'\xff'*4096
   st.mode=0
for u,tag in [(h,'h'),(s,'s')]:
 u.hook_add(UC_HOOK_MEM_READ,mmio_read,tag,begin=0x04000000,end=0x0400ffff)
 u.hook_add(UC_HOOK_MEM_WRITE,mmio_write,tag,begin=0x04000000,end=0x0400ffff)
 if tag=='s':
  u.hook_add(UC_HOOK_MEM_READ,mmio_read,tag,begin=0x0e000000,end=0x0e00ffff)
  u.hook_add(UC_HOOK_MEM_WRITE,mmio_write,tag,begin=0x0e000000,end=0x0e00ffff)
def tick(u,insns):
 pc=u.reg_read(UC_ARM_REG_PC);thumb=u.reg_read(UC_ARM_REG_CPSR)&0x20
 u.emu_start(pc|bool(thumb),0,count=insns)

st.flash[:]= (root/'build/remote_save/baserom_jp.sav').read_bytes()[:131072]
expected=int(sys.argv[4])
if expected == 1:
 for i in range(14): struct.pack_into('<I',st.flash,i*4096+0xffc,122)
snapshot=bytes(st.flash)
for i in range(1000000):
 tick(s,1024); tick(h,1024)
 result=struct.unpack('<I',h.mem_read(0x0203fff0,4))[0]
 if result not in (0,1,2,4):
  print('result',hex(result),'round',i,'transfers',st.transfers,'guest',hex(s.reg_read(UC_ARM_REG_PC)))
  if result!=0x600d:
   print('trace', ' '.join('%04x:%04x'%v for v in trace));raise SystemExit(1)
  assert bytes(st.flash)==snapshot; assert bytes(h.mem_read(0x02000000,14*4096)) == snapshot[expected*14*4096:(expected+1)*14*4096]; assert r16(s,0x06017600+19*32)==0x1111, 'guest progress missing'
  break
else:raise SystemExit('timeout: result=%x transfers=%d host=%x guest=%x slaveout=%x'%(result,st.transfers,h.reg_read(UC_ARM_REG_PC),s.reg_read(UC_ARM_REG_PC),st.slaveout))
