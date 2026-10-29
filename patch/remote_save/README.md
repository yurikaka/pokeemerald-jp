# Japanese Emerald remote-cartridge experiment

The title-menu cartridge connection sends a locally extracted Japanese Pokémon
Box multiboot image with an appended receiver. The guest displays the Box
screen before identifying the BPEJ cartridge and its supported 128 KiB Flash.
It snapshots both ordinary save slots, checks their sector signatures and
checksums, and streams the newer valid slot to the host. The host uses a
56 KiB temporary heap buffer and the original game loader, then returns to the
main menu without resetting the CPU. Special sectors 28–31 are read from the
guest on demand; a working link is required to use them.

Normal saves use the original game save preparation and write one 4 KiB sector
at a time to the guest, followed by readback verification. Writes and erases are
restricted to ordinary save slots. The guest updates its snapshot on successful
writes, and both screens show write progress. The host silences the sound driver
and output for the save attempt. Guest startup, cartridge checking, Flash timing,
interrupt handling and link recovery are experimental. Back up the cartridge
before testing. No automatic reconnection or persistent special-sector cache is
implemented; losing the connection can make subsequent reads or writes fail.

## Building

The Japanese base ROM and extracted Box multiboot image are not included. Set
`BOX_IMAGE` if the image is not at `../pokemon-box-jp-analysis/agbbin.bin`.
Use the ARM toolchain prefix for both steps:

    REMOTE_ARM_PREFIX=<prefix> sh patch/remote_save/build_box_connection.sh
    make chs-receiver CHS_ROM=build/remote_save/direct-host.gba PATCH_ARM_PREFIX=<prefix>
    python3 patch/remote_save/build_box_test.py build/remote_save/direct-host.gba build/remote_save/box-connection-image.bin build/remote_save/box-remote.gba --nm <prefix>nm --elf build/patch/payload.elf

The default `make chs` target retains the older Box diagnostic build. The
standalone direct-link test program is retained for diagnostics but has no
main-menu entry.

## Tests

`sh patch/remote_save/test.sh` runs the portable protocol, link, Flash and
Multiboot tests. Additional focused tests cover slot selection, bulk transfers,
streaming, and preservation of the prior save slot on interrupted writes.
The Unicorn dual-CPU scripts exercise the actual host and receiver code with a
simulated Flash device; they require the ARM toolchain, Unicorn and local ROM
and save files. Neither simulation nor mGBA replaces real hardware testing.
