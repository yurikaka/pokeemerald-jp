# Japanese Easy Chat mode labels (wj3)

The mode sprite uses `PALTAG_MISC_UI`, backed by
`gEasyChatButtonWindow_Pal`, not the background `gEasyChatMode_Pal`.
The imported US graphics used indices 1..3 for their neutral frame;
these are green in the Japanese object palette. Restoring the background
palette did not fix this independent object-palette mismatch.

Cross-check Wokann `src/easy_chat.c`: `sCompressedSpriteSheets` loads
`gEasyChatMode_Gfx` (0x1000 bytes), and `sSpriteTemplate_ModeWindow`
uses a 64x32 sprite with `PALTAG_MISC_UI`. Animation frame offsets are
0, 32, 64 and 96 tiles. The first frame is the Japanese syllabary mode
(`あいうえお モード`), not the US alphabet mode. The second is group
mode (`グループ モード`). The manifest's existing pointer at 0x0857442C
redirects the sheet originally at 0x085737F4.

Generate the replacement from the verified Japanese compressed resource.
Change only the two label rectangles to `假名` and `分组`, using the
existing Chinese small font and Japanese object-palette indices 12, 14,
15. Preserve every frame pixel outside those rectangles, including the
transition and hidden animation frames. No palette, mode selection,
word library, or input handling is changed.

`verify_easy_chat_palette.py` checks the built graphics against the
generator and verifies that all frame/background pixels outside the
label rectangles remain identical to the original Japanese resource.
