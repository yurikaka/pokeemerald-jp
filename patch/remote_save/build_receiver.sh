#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
prefix="${REMOTE_ARM_PREFIX:-../toolchains/arm-gnu-toolchain-13.3.rel1-darwin-x86_64-arm-none-eabi/bin/arm-none-eabi-}"
build="${REMOTE_BUILD_DIR:-build/remote_save}"
extra_flag=-UREMOTE_RECEIVER_SELFTEST
connection_flag=-UREMOTE_CONNECTION_TEST
if [[ "${REMOTE_CONNECTION_TEST:-1}" == 1 ]]; then connection_flag=-DREMOTE_CONNECTION_TEST; fi
if [[ "${REMOTE_SELFTEST:-0}" == 1 ]]; then extra_flag=-DREMOTE_RECEIVER_SELFTEST; connection_flag=-UREMOTE_CONNECTION_TEST; fi
mkdir -p "$build"
"${prefix}gcc" -mcpu=arm7tdmi -c patch/remote_save/receiver_start.s -o "$build/start.o"
for file in receiver protocol server stream link flash gba_flash; do
    "${prefix}gcc" -mcpu=arm7tdmi -mthumb -Os -ffreestanding -fno-builtin -fno-unwind-tables -fno-asynchronous-unwind-tables -std=c99 -Wall -Wextra -Werror "$extra_flag" "$connection_flag" -c "patch/remote_save/$file.c" -o "$build/$file.o"
done
"${prefix}gcc" -mcpu=arm7tdmi -mthumb -nostdlib -Wl,-T,patch/remote_save/receiver.ld -Wl,-Map,"$build/receiver.map" -o "$build/receiver.elf" "$build/start.o" "$build/receiver.o" "$build/protocol.o" "$build/server.o" "$build/stream.o" "$build/link.o" "$build/flash.o" "$build/gba_flash.o" -lgcc
"${prefix}objcopy" -O binary "$build/receiver.elf" "$build/receiver.gba"
# BIOS rounds multiboot payload length up to 16 bytes.
python3 - "$build/receiver.gba" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1]); data = p.read_bytes(); p.write_bytes(data + bytes((-len(data)) % 16))
PY
