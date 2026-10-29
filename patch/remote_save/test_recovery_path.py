from pathlib import Path
import subprocess,struct,sys
from unicorn import Uc,UC_ARCH_ARM,UC_MODE_THUMB,UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_PC,UC_ARM_REG_SP,UC_ARM_REG_LR,UC_ARM_REG_R0
prefix=sys.argv[2]; rom=Path(sys.argv[1]).read_bytes()
syms={p[2]:int(p[0],16) for l in subprocess.check_output([prefix+'nm','build/patch/payload.elf'],text=True).splitlines() if len(p:=l.split())==3}
def run(entry, interventions, initial=None):
 u=Uc(UC_ARCH_ARM,UC_MODE_THUMB)
 for a,n in [(0x08000000,0x2000000),(0x02000000,0x40000),(0x03000000,0x8000),(0x04000000,0x10000),(0x05000000,0x1000),(0x06000000,0x20000),(0x07000000,0x1000)]:u.mem_map(a,n)
 u.mem_write(0x08000000,rom);u.reg_write(UC_ARM_REG_SP,0x03007e40);u.reg_write(UC_ARM_REG_LR,0x08000101)
 u.mem_write(0x04000006,struct.pack("<H",160))
 if initial:initial(u)
 seen=[]
 def hook(u,a,size,_):
  if a==0x08000100:u.emu_stop();return
  if a in interventions:
   seen.append((a,u.reg_read(UC_ARM_REG_R0)))
   value=interventions[a](u) if callable(interventions[a]) else interventions[a]
   if value is not None:u.reg_write(UC_ARM_REG_R0,value)
   u.reg_write(UC_ARM_REG_PC,u.reg_read(UC_ARM_REG_LR))
 u.hook_add(UC_HOOK_CODE,hook);u.emu_start(entry|1,0,count=3000000)
 assert u.reg_read(UC_ARM_REG_PC)==0x08000100,(hex(u.reg_read(UC_ARM_REG_PC)),seen)
 return u,seen
w32=lambda u,a,x:u.mem_write(a,struct.pack('<I',x))
r32=lambda u,a:struct.unpack('<I',u.mem_read(a,4))[0]
callbacks=[]
def cb(u): callbacks.append(u.reg_read(UC_ARM_REG_R0));return 0
active=syms['RemoteJpSaveActive']; check=syms['RemoteJpSaveCheck']; orig=syms['RemoteOriginalTrySavingData']; begin=syms['RemoteJpSaveBegin']; schedule=syms['RemoteScheduleSaveRecovery']; recovery=syms['RemoteRecoveryStart']; finish=syms['RemoteRecoveryWriteSave']; setter=0x08000540
u,seen=run(syms['RemoteTrySavingData'],{active:1,check:0,setter:cb},lambda u:(w32(u,0x03007ff0,0),u.reg_write(UC_ARM_REG_R0,0)))
assert r32(u,0x030075e8)==0x52454356 and callbacks[-1]==(recovery|1)
assert u.reg_read(UC_ARM_REG_R0)==255 and orig not in [a for a,_ in seen]
callbacks.clear()
functions={0x080768b4:0,0x080012a0:0,0x08001274:0,0x0828ecec:0,0x080006f0:0,0x080b9710:0,0x0800668c:0,0x080a8818:0,0x08000bac:0,0x081baa20:0,0x080a8878:0,setter:cb}
def initial(u):w32(u,0x020246f0,0x98765432);w32(u,0x02000000,0x12345678)
u,seen=run(recovery,functions,initial)
assert r32(u,0x020246f0)==0x98765432 and r32(u,0x02000000)==0
assert (0x081baa20,5) in seen and callbacks[-1]==0x081bf0b1
callbacks.clear()
functions={begin:1,orig:1,syms['RemoteJpSaveFailed']:0,0x08000594:0,0x0828ed68:0,0x080a8818:0,setter:cb}
u,seen=run(finish,functions,lambda u:w32(u,0x030075e8,0x52454356))
assert r32(u,0x030075e8)==0 and callbacks[-1]==0x08085b99
assert u.reg_read(UC_ARM_REG_R0)==1
# Exercise the actual sender task's two preparation screens and write branch.
for phase,expected_state,expected_call in [(1,2,0x081baa20),(2,4,0x081baa20),(3,3,syms['RemoteRecoveryWriteSave'])]:
 def setup_task(u):
  w32(u,0x030075e8,0x52454356)
  u.mem_write(0x03005b68,struct.pack('<H',phase))
  u.mem_write(0x0300238e,struct.pack('<H',1))
  u.reg_write(UC_ARM_REG_R0,0)
 u,events=run(syms['RemoteOfficialSenderCopy'],{0x081baa20:0,syms['RemoteRecoveryWriteSave']:1},setup_task)
 assert (r32(u,0x03005b68)&0xffff)==expected_state
 assert expected_call in [a for a,_ in events],events
 if phase in (1,2):assert (expected_call,phase-1) in events
print('recovery: preflight failure, saved-state preservation, retry save and continue passed')
# Each stage paints exactly the number of completed phase marks; no marks are
# presented as byte progress while the BIOS transfer is executing.
for stage in range(7):
 def setup_stage(u,stage=stage):
  w32(u,0x030075e8,0x52454356);u.reg_write(UC_ARM_REG_R0,stage)
 u,_=run(syms['RemoteRecoveryStatus'],{},setup_stage)
 for i in range(7):
  pixel=struct.unpack('<H',u.mem_read(0x06017860+i*32,2))[0]
  assert pixel==(0x1111 if i<stage else 0),(stage,i,pixel)
print('recovery progress: seven stage counts passed')
