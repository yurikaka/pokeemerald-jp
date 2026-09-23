# Japanese Chinese patch

This directory contains a source-only patch for the Japanese `BPEJ` ROM. It
does not contain a ROM.

The first porting batch covers:

- the main menu and continue-summary labels;
- Professor Birch's new-game introduction and gender menu;
- the options menu.

US `CLEAR_TO` (`FC 13`) is a no-op in the Japanese engine. During conversion
it is remapped to `SHIFT_TEXT` (`FC 0D`), which the Japanese engine
implements with the same set-cursor-column semantics, restoring two-column
layouts such as the battle action menu.

Later text ports are stored as independently auditable files under
`patch/batches`. Each batch records the corresponding US localization commit,
the original US text symbol, the exact Japanese pointer locations and their
expected original values. US Chinese text bytes are converted to the Japanese
patch encoding during the build. Placeholders containing Japanese save data,
such as the player name, explicitly switch back to the Japanese renderer.

`make chs` first produces the exact 16 MiB Japanese build, expands a copy to
32 MiB, injects the Chinese renderer/fonts/text pool at `0x09000000`, and
redirects only the audited references in `manifest.json`. The input ROM SHA-1
must be `d7cf8f156ba9c455d164e1ea780a6bf1945465c2`.

The injected text uses `EXT_CTRL_CODE_ENG` to enter Chinese mode and
`EXT_CTRL_CODE_JPN` around player names copied from the save file. This keeps
unported Japanese strings and saved names in their original single-byte
encoding.

The Japanese ROM's original 22-tile dialogue windows are left unchanged.
During the build, `build_texts.py` finds dialogue pages wider than 168 pixels
and reflows them automatically, regenerating newline and scroll controls while
preserving explicit page breaks. This applies to every map-dialogue batch and
to Professor Birch's introduction.

Tool paths can be supplied without installing anything system-wide:

```sh
make chs \
  PATCH_ARM_PREFIX=/path/to/arm-none-eabi- \
  GBAGFX=/path/to/gbagfx
```
