#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
prefix="${REMOTE_ARM_PREFIX:-../toolchains/arm-gnu-toolchain-13.3.rel1-darwin-x86_64-arm-none-eabi/bin/arm-none-eabi-}"
rom="${1:?pass the path to a freshly built patched ROM}"
tmp="$(mktemp -d "${TMPDIR:-/tmp}/remote-cpu-test.XXXXXX")"
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
begin=$("${prefix}nm" build/patch/payload.elf | awk '$3 == "RemoteJpSaveBegin" { print $1 }')
test -n "$begin"
"${prefix}as" -mcpu=arm7tdmi patch/remote_save/test_guest_start.s -o "$tmp/start.o"
"${prefix}gcc" -mcpu=arm7tdmi -mthumb -Os -ffreestanding -DREMOTE_BEGIN="0x$begin" -c patch/remote_save/test_guest.c -o "$tmp/test.o"
"${prefix}ld" -Ttext=0x02001000 -o "$tmp/test.elf" "$tmp/start.o" "$tmp/test.o"
"${prefix}objcopy" -O binary "$tmp/test.elf" "$tmp/test.bin"
python3 patch/remote_save/test_dual_cpu.py "$rom" "$tmp/test.bin"
