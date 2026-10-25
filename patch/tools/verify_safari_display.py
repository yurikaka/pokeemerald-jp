"""Render Safari healthbox/menu via native entry points; emulate BIOS copies and temporary-window allocation."""
import sys,struct
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'patch/tools'))
from verify_remaining_display_port import Machine
from build_berry_tag_gfx import lzdec
from unicorn import UC_HOOK_CODE
from unicorn.arm_const import UC_ARM_REG_R0,UC_ARM_REG_R1,UC_ARM_REG_R2,UC_ARM_REG_R3,UC_ARM_REG_SP,UC_ARM_REG_LR,UC_ARM_REG_PC
m=Machine({'Fonts':0x080061A4,'Title':0x080741E0,'Count':0x08074320,'Menu':0x0814FA04});c=m.cpu
buf=0x02028000;menu_buf=0x0202A000;base_tile=32;vram=0x06010000+base_tile*32
source=(ROOT.parent / 'pokeemerald_wokann_dev/graphics/battle_interface/healthbox_safari.png.4bpp.lz').read_bytes();gfx=lzdec(source,0x08000000)
def hook(c,a,size,u):
 if a in (0x082959B8,0x082959BC):
  src=c.reg_read(UC_ARM_REG_R0);dst=c.reg_read(UC_ARM_REG_R1);control=c.reg_read(UC_ARM_REG_R2)
  unit=4 if a==0x082959B8 or control&(1<<26) else 2
  length=(control&0x1FFFFF)*unit
  if control&(1<<24):data=bytes(c.mem_read(src,unit))*(length//unit)
  else:data=bytes(c.mem_read(src,length))
  c.mem_write(dst,data);c.reg_write(UC_ARM_REG_PC,c.reg_read(UC_ARM_REG_LR))
 elif a==0x08003250:
  template=c.reg_read(UC_ARM_REG_R0)
  assert template % 4 == 0, 'Native AddWindow requires a word-aligned template'
  fields=bytes(c.mem_read(template,8))
  assert fields == bytes((0,0,0,7,2,0,0,0))
  c.mem_write(0x02020004+24*12,fields+struct.pack('<I',buf))
  c.reg_write(UC_ARM_REG_R0,24);c.reg_write(UC_ARM_REG_PC,c.reg_read(UC_ARM_REG_LR))
 elif a in (0x08003444,0x0800365C,0x080035A8):c.reg_write(UC_ARM_REG_PC,c.reg_read(UC_ARM_REG_LR))
c.hook_add(UC_HOOK_CODE,hook);m.call('Fonts')
c.mem_write(0x020205AC+4,struct.pack('<H',base_tile))
def reset():c.mem_write(vram,gfx)
def draw(n):c.mem_write(0x02039D18,bytes((n,)));m.call('Count',(0,));return bytes(c.mem_read(vram,4096))
reset();m.call('Title',(0,));initial=bytes(c.mem_read(vram,4096));frames={}
assert initial != gfx, 'Title did not render'
for n in (30,29,10,9,1,0):
 frames[n]=draw(n)
 c.mem_write(vram,initial);fresh=draw(n);assert frames[n]==fresh,n
assert len(set(frames.values())) == 6, 'Distinct ball counts did not render'
# Updates must stay in the 56x13 count rectangle; frame pixels remain intact.
def px(b,x,y):
 t=(x//64)*64+(y//8)*8+(x%64)//8;o=t*32+(y%8)*4+(x%8)//2
 return b[o]>>(4*(x%2))&15
for y in range(64):
 for x in range(128):
  if not(24<=x<80 and 4<=y<17 or 32<=x<88 and 19<=y<32):assert px(frames[0],x,y)==px(gfx,x,y),(x,y)
pal=[(0,0,0),(50,50,50),(248,248,216),(128,128,128)]+[(160,200,200)]*12
out=Image.new('RGB',(128*4,40*4*3))
for row,n in enumerate((30,9,0)):
 im=Image.new('RGB',(128,40))
 for y in range(40):
  for x in range(128):im.putpixel((x,y),pal[px(frames[n],x,y)])
 out.paste(im.resize((512,160)),(0,row*160))
out.save('/tmp/safari-panel-fixed.png')
# Execute the same native menu printer used by SafariHandleChooseAction.
c.mem_write(0x02020004+2*12,bytes((0,17,35,12,4,5,0x90,1))+struct.pack('<I',menu_buf))
ptr=m.word(0x08159A28)
menu=m.string(ptr)
assert menu.count(b'\xfc\x0d\x30') == 2, 'Menu columns are not at 48px'
assert b'\x73\xf1\x67\xa7\x6a\x14' in menu, 'Safari Ball label missing'
assert b'\x60\x63\x66\xd7\x62\xc0\x67\x00' in menu, 'Full Pokeblock label missing'
m.call('Menu',(ptr,2))
b=bytes(c.mem_read(menu_buf,12*4*32));im=Image.new('RGB',(96,32));p=[(240,240,224)]*16;p[13]=(32,32,32);p[14]=(240,240,224);p[15]=(128,128,128)
for y in range(32):
 for x in range(96):
  o=((y//8)*12+x//8)*32+(y%8)*4+x%8//2
  im.putpixel((x,y),p[b[o]>>(4*(x%2))&15])
im.resize((768,256)).save('/tmp/safari-menu-fixed.png')
print('PASS: native entry points render; six counts match fresh renders; frame pixels preserved; native 96px menu rendered.')

# Verify the actual layout veneers, including the case used after closing the
# Pokeblock case. Substitute allocation/transfers and inspect their arguments.
map_buffer = 0x02030000
map_data = lzdec((ROOT / 'baserom_jp.gba').read_bytes(), 0x08C00530)
captured_templates = []

def layout_hook(cpu, address, size, unused):
    if address == 0x08003090:
        assert cpu.reg_read(UC_ARM_REG_R0) % 4 == 0
        captured_templates.append(bytes(cpu.mem_read(cpu.reg_read(UC_ARM_REG_R0), 200)))
        cpu.reg_write(UC_ARM_REG_R0, 1)
    elif address == 0x080021CC:
        assert cpu.reg_read(UC_ARM_REG_R1) == 0x08C00530
        cpu.mem_write(map_buffer, map_data)
    elif address == 0x08002194:
        cpu.reg_write(UC_ARM_REG_R0, map_buffer)
    elif address == 0x080023B4:
        stack = cpu.reg_read(UC_ARM_REG_SP)
        x, y = cpu.reg_read(UC_ARM_REG_R2), cpu.reg_read(UC_ARM_REG_R3)
        width, height, palette = struct.unpack('<III', cpu.mem_read(stack, 12))
        assert (width, height, palette) == (1, 2, 17)
        src = cpu.reg_read(UC_ARM_REG_R1)
        for dy in range(2):
            tile = struct.unpack('<H', cpu.mem_read(src + dy * 2, 2))[0]
            cpu.mem_write(map_buffer + ((y + dy) * 32 + x) * 2, struct.pack('<H', (tile & 0xFFF) | 0x1000))
    elif address != 0x08002248:
        return
    cpu.reg_write(UC_ARM_REG_PC, cpu.reg_read(UC_ARM_REG_LR))

c.hook_add(UC_HOOK_CODE, layout_hook)
m.names.update({'InitLayout':0x08035510, 'InitialFrame':0x0803590C,
                'ReturnFrame':0x08036270, 'ShowCursor':0x080598C8, 'HideCursor':0x08059910})
for safari in (False, True):
    c.mem_write(0x02022C90, struct.pack('<I', 0x80 if safari else 0))
    m.call('InitLayout', (0x082EB870,), (0x08035518,))
    templates = captured_templates[-1]
    original = bytes(c.mem_read(0x082EB870, 200))
    if safari:
        assert (templates[11], templates[14], templates[15], templates[17], templates[19]) == (13, 0xC0, 1, 17, 12)
        regions = [(struct.unpack_from('<H', templates, i * 8 + 6)[0], templates[i * 8 + 3] * templates[i * 8 + 4]) for i in (0, 1, 2)]
        for i, (start, length) in enumerate(regions):
            for other, other_length in regions[i+1:]:
                assert start + length <= other or other + other_length <= start
    else:
        assert templates == original
    for entry, stop in (('InitialFrame',0x08035918), ('ReturnFrame',0x0803627C)):
        m.call(entry, (), (stop,))
        expected = bytearray(map_data)
        if safari:
            struct.pack_into('<H', expected, (33*32+15)*2, 0x1000)
            struct.pack_into('<H', expected, (33*32+17)*2, 0)
            for y in range(34,40):
                edge = struct.unpack_from('<H',map_data,(y*32+17)*2)[0]
                inside = struct.unpack_from('<H',map_data,(y*32+18)*2)[0]
                for x in range(15,29):struct.pack_into('<H',expected,(y*32+x)*2,edge if x==15 else inside)
        assert bytes(c.mem_read(map_buffer,4096)) == expected
        for position in range(4):
            x=(16 if safari else 18)+(position&1)*6; y=35+(position&2)
            m.call('ShowCursor',(position,))
            assert m.word(map_buffer+(y*32+x)*2)&0xFFFF == 0x1001
            m.call('HideCursor',(position,))
            assert m.word(map_buffer+(y*32+x)*2)&0xFFFF == 0x1016
print('PASS: Safari-only templates, nonoverlapping VRAM tiles, both frame reloads, and all four cursors; ordinary battle layout preserved.')
