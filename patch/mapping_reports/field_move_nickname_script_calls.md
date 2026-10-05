# Field move interaction script nickname crash

The replacement `ChsScrCmdBufferPartyMonNick` introduced in commit
`498e807` called two incorrect absolute Thumb addresses:

- `0x0809A81D` instead of `ScriptReadHalfword` at `0x08098795`.
  The incorrect address is inside `ScrCmd_braillemessage`, not the script
  operand reader, and cannot be entered with this calling convention.
- `0x0806E569` instead of `VarGet` at `0x0809CF6D`.

Cross-checks:

- Wokann `src/scrcmd.c`, `ScrCmd_bufferpartymonnick`, reads a byte for
  the string variable, reads a halfword, resolves it through `VarGet`,
  then obtains the party member nickname.
- Wokann `src/script.c`, `ScriptReadHalfword`, advances the script pointer
  by two bytes; `src/event_data.c`, `VarGet`, resolves the operand.
- Local Japanese `asm/scrcmd.s` original handler calls exactly these
  two functions. `asm/script.s` and `asm/event_data.s` establish their
  Japanese entry addresses.
- Wokann `data/scripts/field_move_scripts.inc` calls `bufferpartymonnick`
  before the yes/no prompt for Cut, Rock Smash, Strength, Waterfall,
  Dive, and surfacing when a capable party member is found.

Change only the two call target literals, retaining the Thumb bit.
Nickname comparison, display conversion, script operands, move effects,
and persistent data are unchanged. Other scripts using this command
also benefit from correcting its call targets.

Build and vanilla comparison are checked locally. Actual field-move
interaction must still be verified in an emulator; no runtime crash
reproduction was available for this change.
