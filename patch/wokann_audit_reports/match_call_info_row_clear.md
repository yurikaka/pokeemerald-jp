# Match Call information row clearing

Switching between trainer information pages could leave the previous trainer's
text after a shorter Chinese string. The JP renderer calls
`StringCopyPadded(..., 15)`, which counts bytes rather than display width. Chinese
characters and their language control codes exhaust that count before the
120-pixel row has been covered.

Cross-reference: `../pokeemerald_wokann_dev`, branch `dev`,
`src/pokenav_list.c`, `PrintMatchCallFlavorText`, and `src/string_util.c`,
`StringCopyPadded`. `src/pokenav_match_call_gfx.c` sets a 15-tile list width and
reprints the information without clearing the entire page when changing contact.

The native JP function is at `0x081C85FC`. A veneer at `0x081C8648` clears the
current 16-pixel row to palette index 1, using the actual window width times
eight. It preserves the list pointer, row index, text buffer and return address,
replays the displaced printer setup, and resumes at `0x081C8650`. The original
eight bytes are `39 01 02 22 11 43 00 91`. Text, colors and row positions retain
the native behavior. Rows without a flavor-text pointer retain the native path.

Validation: `patch/tools/verify_match_call_info_rows.py` executes the real ROM
copy, clear and text-printing functions in Unicorn, substituting only the contact
lookup and VRAM transfer. With the original instructions restored, a long-to-short
replacement reproduces the stale pixels. With the installed hook, all four text
fields pass at circular-row bases 0, 7 and 15. Each complete pixel buffer matches
the result of drawing the short string onto a fresh background.

Run with Python's `unicorn` package installed:

```sh
python3 patch/tools/verify_match_call_info_rows.py
```

This is a rendering regression check, not an emulator or hardware play test.
