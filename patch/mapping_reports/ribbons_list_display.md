# Ribbons list display repair (jz1)

## Native path and observed problems

Wokann dev `src/pokenav_ribbons_list.c::BufferRibbonMonInfoText` reads
party or boxed nickname, gender, level and ribbon count. The Japanese version
pads the nickname to five single-byte positions and formats a gender/level/count
template. Chinese names need different pixel widths; the screenshot shows the
five-character name overlapping gender and count text clipped at the right.
The Japanese count suffix is byte 0x0A in the native three gender templates.

The row callback field at `0x081CF9F0` originally contains `0x081CF9F9`.
Wokann's `pokenav_ribbons_list.o` .text relocation at offset 0x960 names
`BufferRibbonMonInfoText`; the section starts at `0x081CF090`. Redirect this
one function pointer to `ChsBufferRibbonMonInfoText + 1`, preserving Thumb mode.
No trainer, species or persistent nickname table is rewritten.

## Display-only replacement

- Use the existing party/boxed nickname display helpers. A nickname matching
  its Japanese species name becomes a Chinese species token; a custom nickname
  stays unchanged. The old single-byte nickname padding is bypassed.
- Five-character converted Chinese names use `ChsWriteNarrowSpeciesName`.
  Four-character names keep the normal 12-pixel font (48 pixels); five-character
  narrow names occupy 40 pixels. The nickname lives in temporary stack memory.
- Put gender at pixel 50 with the native male/female color controls, followed
  by the native slash and Lv extra symbol. Level 100 fits before pixel 100.
- Put ribbon count at pixel 100, right-aligned in two digits, and append `个`
  in the normal Chinese font as explicitly requested. This translates the native
  Japanese `こ` unit rather than following the US layout without a unit. Two
  digits and the 12-pixel unit fit exactly within the 128-pixel window.
- Clear recycled ribbon list rows as well as Match Call rows through the
  existing source-backed row hook. Other Pokenav formatters remain excluded.

## Memory and reference boundaries

The builder reads the same fields as the Wokann function: boxId, monId and
two-byte ribbon count from the list item, and nickname/gender/level from the
mon. It calls no setter. The destination is Pokenav's 64-byte itemTextBuffer,
consumed by the list text printer. The local nickname area is 28 bytes and
the complete narrow five-character row requires at most 43 bytes excluding
any custom-name peculiarities. Normal custom Japanese nicknames remain on
the original Japanese rendering path.

Party address and all native getter/formatting service addresses are checked
against the original JP assembly/ELF labels and Wokann's corresponding C
getter calls. Original gender templates remain untouched. The new callback
is limited to the ribbon list; ribbon summary, save writes and nickname
comparison behavior are unchanged.

## Validation

`verify_ribbons_list_display.py` verifies the typed Wokann relocation, original
callback pointer, new Thumb pointer, both display helpers, column/buffer bounds
and the row-clearing selection. Build and vanilla comparison are separate checks.
No emulator playthrough has been performed here. Test party and boxed entries,
five-character names, level 100, both genders/genderless, multi-digit counts,
scrolling, and selecting an entry to open its ribbon summary.
