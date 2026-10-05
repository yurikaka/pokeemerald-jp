# Questionnaire background and footer palette corruption (wj.png)

Commit `0498e0a` redirected the palette load at `0x0811D868` from the
original `0x08573E64` to a four-shade grayscale palette whose remaining
12 entries were zero. Despite its resource name, this load supplies the
entire background palette bank 0, not the mode-window sprite palette.

Wokann `src/easy_chat.c`, `LoadEasyChatPalettes`, confirms this palette
is loaded at index 0 with size 0x20. `src/graphics.c` identifies the
original as `graphics/easy_chat/mode.png.gbapal`. The localized footer
uses entries 12, 14 and 15, which the replacement zeroed out. Original
background artwork also uses colors outside the replacement's range.

Wokann's `sSpriteTemplate_ModeWindow` instead uses `PALTAG_MISC_UI`,
backed by `gEasyChatButtonWindow_Pal` in `sSpritePalettes`. Thus changing
the background bank was not necessary for the localized mode sprites.

Remove only the background palette pointer override and its unused
payload. Retain the Chinese footer, button and mode graphics, original
tilemaps, cursor layout, and questionnaire word IDs and save behavior.

`verify_easy_chat_palette.py` checks the Wokann palette declaration,
the restored ROM pointer, all original palette bytes, footer colors,
and the built localized footer resources. Emulator appearance still
requires gameplay verification.
