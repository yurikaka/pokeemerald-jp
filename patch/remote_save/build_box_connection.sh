#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
prefix="${REMOTE_ARM_PREFIX:-arm-none-eabi-}"
image="${BOX_IMAGE:-../pokemon-box-jp-analysis/agbbin.bin}"
out=build/remote_save
mkdir -p "$out"
"${prefix}gcc" -mcpu=arm7tdmi -mthumb -Os -ffreestanding -fno-builtin -fno-unwind-tables -fno-asynchronous-unwind-tables -Wall -Wextra -Werror -c patch/remote_save/box_connection.c -o "$out/box_connection.o"
"${prefix}gcc" -mcpu=arm7tdmi -mthumb -c patch/remote_save/box_hook.s -o "$out/box_hook.o"
for name in protocol stream link bulk slot_select slot_stream flash gba_flash; do
    "${prefix}gcc" -mcpu=arm7tdmi -mthumb -Os -ffreestanding -fno-builtin -fno-unwind-tables -fno-asynchronous-unwind-tables -Wall -Wextra -Werror -c "patch/remote_save/$name.c" -o "$out/box_$name.o"
done
"${prefix}gcc" -mcpu=arm7tdmi -mthumb -nostdlib -Wl,-T,patch/remote_save/box_connection.ld -Wl,-Map,"$out/box_connection.map" -o "$out/box_connection.elf" "$out/box_connection.o" "$out/box_hook.o" "$out/box_protocol.o" "$out/box_server.o" "$out/box_stream.o" "$out/box_link.o" "$out/box_bulk.o" "$out/box_slot_select.o" "$out/box_slot_stream.o" "$out/box_flash.o" "$out/box_gba_flash.o" -lgcc
"${prefix}objcopy" -O binary "$out/box_connection.elf" "$out/box_connection.bin"
entry=$("${prefix}nm" "$out/box_connection.elf" | awk '$3 == "BoxWaitForScreen" {print $1}')
test -n "$entry"
printf "BoxWaitForScreen address: %s\n" "$entry"
python3 - "$image" "$out/box_connection.bin" "$out/box-connection-image.bin" "$entry" <<'PY'
import sys,struct
from pathlib import Path
src=bytearray(Path(sys.argv[1]).read_bytes()); payload=Path(sys.argv[2]).read_bytes()
assert len(src)==0x84f4 and src[0x3aa:0x3ae]==bytes.fromhex('02f04ff9')
assert src[0x3b2:0x3b6]==bytes.fromhex('20680130')
src[0x3aa:0x3ae]=bytes.fromhex('c046c046')
# Run Box for 180 display frames before entering the appended diagnostic.
addr=0x020003b2;target=int(sys.argv[4],16)&~1;delta=target-(addr+4)
assert delta%2==0 and -(1<<22)<=delta<(1<<22)
struct.pack_into('<HH',src,0x3b2,0xf000|((delta>>12)&0x7ff),0xf800|((delta>>1)&0x7ff))
src+=bytes(0x1b200-len(src));src+=payload
src+=bytes((-len(src))%16)
assert len(src)<0x3f000
Path(sys.argv[3]).write_bytes(src)
print('Box image + diagnostic:',len(src),'bytes, code at 0x0201b200')
PY
