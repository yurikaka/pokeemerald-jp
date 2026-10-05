# Easy Chat footer and selected-word tile overlap (wj2.png)

The footer generator added Chinese labels immediately after the 43
original tiles, assigning new tiles 0x2B through 0x80. The Japanese
selected-word window on BG3 starts at tile 0x30. Rendering selected
words therefore overwrote most Chinese footer graphics, making buttons
show fragments of the selected words instead of their labels.

Wokann `src/easy_chat.c`, `sub_0811DB10`, constructs this dynamic window
with baseBlock 0x30; local `asm/easy_chat.s` confirms the same layout.
The nine `sPhraseFrameDimensions` entries at 0x08574358 specify at most
28 by 6 tiles, so its largest occupied range ends at tile 0xD8 exclusive.
BG3 uses character block 2, while BG1 uses the following block 3.

Keep the original 43 tiles intact and reserve padding up to tile 0x100
before adding footer glyphs. The 86 footer tiles then occupy 0x100..0x155,
outside all selected-word windows and below the next character block
at tile 0x200. No function, cursor coordinates, word IDs, or save data
change. The padding is loaded before the selected-word window is drawn.

The resource verifier checks every generated footer tile against the
selected-word range and the next BG character block boundary, in
addition to checking the actual built ROM resources and original palette.
Gameplay appearance remains subject to emulator testing.
