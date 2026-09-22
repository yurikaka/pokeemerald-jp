# Japanese Chinese patch

This directory contains a source-only patch for the Japanese `BPEJ` ROM. It
does not contain a ROM.

The first porting batch covers:

- the main menu and continue-summary labels;
- Professor Birch's new-game introduction and gender menu;
- the options menu.

`make chs` first produces the exact 16 MiB Japanese build, expands a copy to
32 MiB, injects the Chinese renderer/fonts/text pool at `0x09000000`, and
redirects only the audited references in `manifest.json`. The input ROM SHA-1
must be `d7cf8f156ba9c455d164e1ea780a6bf1945465c2`.

The injected text uses `EXT_CTRL_CODE_ENG` to enter Chinese mode and
`EXT_CTRL_CODE_JPN` around player names copied from the save file. This keeps
unported Japanese strings and saved names in their original single-byte
encoding.

Tool paths can be supplied without installing anything system-wide:

```sh
make chs \
  PATCH_ARM_PREFIX=/path/to/arm-none-eabi- \
  GBAGFX=/path/to/gbagfx
```

