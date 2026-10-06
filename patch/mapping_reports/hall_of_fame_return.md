# Hall of Fame display return-address repair

## Confirmed defect

Wokann dev `src/hall_of_fame.c::HallOfFame_PrintMonInfo` calls
`GetStringWidth` at `0x08174996` (egg) and `0x081749D8` (normal species).
The Chinese patch routes these two calls through `ChsGetMonNickname` and
`ChsNicknameDisplayRouter` to `.Lnickname_hof_width_found`.

That adapter saved r0-r2 but not LR before calling
`ChsConvertNicknameForSpecies`. Its BL replaced LR with the adapter's own
post-call address. Tail-jumping to the original `GetStringWidth` therefore
passed the wrong return address: when width calculation returned, execution
reentered the adapter's register-pop sequence and consumed unrelated stack
data. This defect affects nickname conversion attempts whether or not the
nickname matches the Japanese species name.

## Repair and data boundary

Preserve LR across conversion and width calculation. The display adapter saves
r4-r6 and LR and returns through the saved LR. Custom Japanese nicknames retain
the native `GetStringWidth` path. No species tables, saved records or helper
comparison semantics change.

Wokann's routine uses a 0x1c-byte stack frame and copies the displayed nickname
to sp+0xc. The adapter converts that temporary text, not the Hall of Fame
record pointed to by r7. The Chinese species token is five bytes including EOS
and fits this temporary buffer. `Task_Hof_InitMonData` still reads the original
nickname using `GetMonData3` and writes ten bytes to the saved record.

## Verification limits

`verify_hall_of_fame_return.py` checks compiled save/restore instructions,
both original and patched call destinations,
and byte-identical native record initialization at `0x08173500..0x0817369F`.
This is a static binary check, not an emulator playthrough. Runtime testing
should cover registering a champion team and viewing that record from a PC,
including both unchanged Japanese nicknames and custom nicknames.

## Five-character display follow-up (mrt1)

The native width function does not measure the Chinese compact species token
as the name it renders. The nickname therefore starts too far right and
overlaps the following slash/species text. The adapter now measures resolved
Chinese name glyphs (12 pixels per Chinese glyph, 8 per single-byte glyph).
For five-character species names it materializes the existing narrow-font
form in the temporary nickname buffer and returns its 40-pixel width.
Shorter names retain their normal font. Custom Japanese nicknames retain the
native width function and their original text.

An eight-byte veneer at `0x08174AC4` intercepts only the species-line printer
argument setup. Wokann's original instructions there are `add r0, sp, #0xc`,
`str r0, [sp, #8]`, `movs r0, #0`, `movs r1, #1`. The wrapper prints five-character
species names with the existing narrow font, preserving slash, gender and
original coordinates, then resumes at `0x08174AD4`. It uses a separate temporary
stack buffer because slash + font switches + five glyphs + gender + EOS needs
17 bytes, exceeding the original 16-byte text area. The wrapper has 44 bytes
of local stack storage, and its text occupies offsets 15 through 31 inclusive.
The nickname's narrow form needs only 15 bytes and fits the original area.
No saved Hall of Fame nickname or party nickname is changed.
