#!/bin/sh
set -eu
cd "$(dirname "$0")"
tmp="$(mktemp -d "${TMPDIR:-/tmp}/remote-save-tests.XXXXXX")"
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
for test in protocol server stream client link flash multiboot; do
    cc -std=c99 -Wall -Wextra -Werror -pedantic \
        protocol.c server.c stream.c client.c game.c link.c flash.c multiboot.c \
        "test_${test}.c" -o "$tmp/$test"
    "$tmp/$test"
done
