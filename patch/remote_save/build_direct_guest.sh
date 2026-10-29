#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
prefix="${REMOTE_ARM_PREFIX:-arm-none-eabi-}"
out=build/remote_save
mkdir -p "$out"
"${prefix}gcc" -mcpu=arm7tdmi -c patch/remote_save/direct_guest_start.s -o "$out/direct_guest_start.o"
"${prefix}gcc" -mcpu=arm7tdmi -mthumb -Os -ffreestanding -fno-builtin -fno-unwind-tables -fno-asynchronous-unwind-tables -Wall -Wextra -Werror -c patch/remote_save/direct_guest.c -o "$out/direct_guest.o"
"${prefix}gcc" -mcpu=arm7tdmi -mthumb -nostdlib -Wl,-T,patch/remote_save/direct_guest.ld -Wl,-Map,"$out/direct_guest.map" -o "$out/direct_guest.elf" "$out/direct_guest_start.o" "$out/direct_guest.o" -lgcc
"${prefix}objcopy" -O binary "$out/direct_guest.elf" "$out/direct-guest.gba"
python3 - "$out/direct-guest.gba" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1]);b=bytearray(p.read_bytes());b[0xa0:0xac]=b'LINKTEST    ';b[0xac:0xb0]=b'LNKJ';b[0xb0:0xb2]=b'01';b[0xbc]=0;b[0xbd]=(-sum(b[0xa0:0xbd])-0x19)&255
b+=bytes([0xff])*(max(0x20000,len(b))-len(b));p.write_bytes(b)
PY
