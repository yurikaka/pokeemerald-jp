# Incoming Match Call crash after the ellipsis

## Cause

`PopulateTrainerName` at `0x08196644` has two paths:

- Six special multi-trainer entries copy the speaker's individual name, then
  branch to the shared epilogue at `0x0819668C`.
- Other trainers copy the trainer name from the normal trainer table. The
  Chinese display hook replaces this path starting at `0x08196680`.

The hook was declared as a 16-byte `function_hooks` entry even though it is
inside the function. It overwrote `0x08196680..0x0819668F`, including the
shared epilogue used by the special-name path. The latter jumped into the
hook's literal data and returned to an invalid address.

This occurs when a message populates a special trainer's name. Automatic
incoming calls select/build their message after completing the opening
ellipsis, matching the reported timing. Five of the six special trainer IDs
are in the normal 64-entry call-message trainer pool.

## Reference and fix

Cross-checked `../pokeemerald_wokann_dev` on `dev`:

- `src/match_call.c`: `PopulateTrainerName`, `sMultiTrainerMatchCallTexts`,
  `BuildMatchCallString`, and `MatchCall_PrintIntro`.
- `build/pokeemerald-jp/src/match_call.o`, `.text.PopulateTrainerName`: the
  special branch jumps from function offset `0x2A` to shared epilogue `0x48`.
  The ordinary name lookup starts at offset `0x3C`.
- JP `asm/match_call.s` supplies the corresponding linked addresses:
  hook `0x08196680`, shared epilogue `0x0819668C`.

Changed this one manifest entry to an eight-byte `veneer_hooks` entry. It
checks original bytes `610104480918281c`. The ordinary-name hook now only
looks up the Chinese name and sets the copy arguments, then resumes at the
native `StringCopy` call at `0x08196688` (Thumb target `0x08196689`). Both
paths use the same native epilogue at `0x0819668C`; the hook no longer
duplicates its register/stack restoration or the string-copy call wrapper.
The special path retains its native copy. The instructions from
`0x08196688` through `0x08196693` now match the JP base ROM.

No text, name-table data, call probabilities or save data were changed.

## Validation

`patch/tools/verify_match_call_incoming.py` uses Unicorn to execute native ROM
code and the installed Chinese name hooks:

- Reinstalling the old 16-byte trampoline reproduces an invalid instruction
  fetch for call-message trainer index 5 (trainer ID 687).
- All 64 trainer-name paths return normally, preserve callee-saved registers
  and stack balance, and copy exactly the expected name without overflowing
  the 32-byte destination allowance. Each executes the native shared epilogue
  exactly once.
- All six special table entries pass, including the entry outside the pool.
- All 64 incoming-call intro-to-message transitions select a same-route
  message, expand its placeholders and register the resulting nonempty text.

The transition test substitutes deterministic world state, the completed
intro printer, window clear and new printer registration. Message selection,
name/map variable population and placeholder expansion execute native code.
This is not a full emulator or hardware play test.

ROM CRC32 after rebuilding with the shared-return cleanup: `78498AE4`.
