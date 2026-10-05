# Direction-sign arrows (lp1)

Wokann `charmap.txt` encodes arrows as FC 0C 00/01/02/03, unlike the US
single-byte 79/7A/7B/7C codes. Wokann's text renderer handles
EXT_CTRL_CODE_ESCAPE by combining its operand with 0x100 and drawing the
corresponding extra-font glyph. Its Route 101 sign explicitly uses UP_ARROW.

The Japanese Chinese conversion previously copied US arrow bytes unchanged.
In Chinese mode, 79/7B/7C fall in Chinese leading-byte ranges and consume
the following byte of the place name. 7A instead falls through to Japanese
kana. This explains both broken arrow glyphs and subsequent name corruption.

Convert single-byte arrows in Chinese-mode US input to Japanese escape
controls. Chinese two-byte tokens are consumed before their low byte can
be mistaken for an arrow, and explicitly Japanese-mode bytes remain intact.
Support the same four named controls in literal Chinese strings. Count
escaped font glyphs as eight pixels during wrapping, rather than zero.

No ROM address overrides or renderer changes are required. Existing batch
source bytes remain as provenance; every applicable resource is converted
on build. Verify with `python3 patch/tools/verify_sign_arrows.py`.
