# Japanese Emerald remote-cartridge experiment

This branch is an experiment, not a complete remote-save implementation. The
main-menu entry initializes the game like the original Berry Program Update and
runs a copy of its Multiboot sender task. The copy sends the receiver embedded
in this directory and suppresses the original full-screen drawing calls. The
sender still uses the game's original Multiboot library. It does not currently
activate the remote-save backend or reload the main menu after sending.

`receiver.c` is a separate RAM program with the original sender's post-BIOS
startup handshake, a Japanese Emerald (`BPEJ`) cartridge check, and support for
Macronix C2/09 and Sanyo 62/13 128 KiB Flash. The client, server, serial and
Flash modules and the Japanese game hooks are experimental. The hooks include
session checking, but reconnection during gameplay, safe handling of interrupted
writes and real-hardware timing have not been validated. Do not use this branch
to write a valuable cartridge save without a backup.

## Pokémon Box sender test

`build_box_test.py` creates a diagnostic ROM that sends a locally extracted
Pokémon Box Japanese Multiboot program instead of the custom receiver. With
`--keep-screen`, it changes exactly one call in the Box image to avoid the
main-loop communication-timeout reset; the remaining original Box bytes are
untouched, apart from zero padding at the end to meet Multiboot alignment.
Pokémon Box normally expects a GameCube Joy Bus peer; showing its logo is not
evidence of a functioning remote-save connection.

On this branch `make chs` builds the verified Box diagnostic by default. It
requires the Japanese base ROM and the locally extracted Box image, neither of
which is included in the repository. Set `BOX_IMAGE` if the image is elsewhere.
For the local ARM toolchain, for example:

    make chs PATCH_ARM_PREFIX=../toolchains/arm-gnu-toolchain-13.3.rel1-darwin-x86_64-arm-none-eabi/bin/arm-none-eabi-

The build checks the SHA-256 before writing the output, so it cannot silently
produce a different ROM under the successful version's name:

    48af1f0554e69a5546801866f0af9466b2d02bd0669ab827340a27cdabde80c1

`make chs-receiver` builds the intermediate ROM that sends our custom receiver;
it is not the verified Box diagnostic.

## Tests

`sh patch/remote_save/test.sh` runs host protocol, server, link, Flash and
Multiboot-controller tests. `test_dual_cpu.sh ROM` optionally executes game
hooks and the receiver on two simulated ARM CPUs using Python Unicorn. These
tests do not verify a real link cable, the original BIOS Multiboot sender in two
emulators, or actual Flash timing.
