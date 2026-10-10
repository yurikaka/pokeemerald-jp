# Gift transfer messages before meeting Lanette

Castform's party-full path calls `Common_EventScript_TransferredToPC` after
declining a nickname. Before FLAG_SYS_PC_LANETTE is set, the two script message
references and two naming-screen table references still pointed at Japanese
text. Batch 194 covered the battle table; batch 457 covered only Lanette's
script/naming variants. Batch 503 supplies the missing Someone's PC references
using the same existing templates and producer contract.

## Address evidence

Cross-checked against `../pokeemerald_wokann_dev`, branch `dev`:

- `data/scripts/pc_transfer.inc`: the common entry fills STR_VAR_1 with a box
  name and STR_VAR_2 with the received species. The full-box branches also
  fill STR_VAR_3. Someone/Lanette selection uses FLAG_SYS_PC_LANETTE.
- `data/text/pc_transfer.inc`: the original Someone templates occupy
  0x08243E08 and 0x08243E4C.
- `build/pokeemerald-jp/data/event_scripts.o`: nm and ABS32 relocations identify
  offsets 0x6964B / 0x6965D as references to those two text symbols. The section
  base 0x081DABAC is independently consistent with all four transfer text
  labels and the four message relocations. The resulting ROM references are
  0x082441F7 / 0x08244209; both are msgbox pointer operands (`0F 00` prefix).
- `src/naming_screen.c`, `DisplaySentToPCMessage`: the table at 0x08565858
  selects normal/full-box and Someone/Lanette variants by index 0/1/2/3, then
  expands STR_VAR_1..3. Base-ROM table words exactly match all four text labels;
  indices 0 and 2 at 0x08565858 / 0x08565860 were still Japanese.

No new text encoding, executable hook, or storage change is needed. Custom
nicknames and custom box names retain the original Japanese save encoding.

## Verification

`verify_gift_pc_transfer.py` checks all twelve original script/naming/battle
references, including the existing Lanette variants, and proves no old transfer
pointer remains. It runs native box/species buffering and placeholder expansion
for seven gift species, normal/full-box variants, all fourteen default box names
and custom names. It also executes the naming-screen message selection through
the expansion call for all four choices, with state-query endpoints stubbed.
Storage bytes and output guards are checked. This is ARM execution validation,
not an in-game scene test.
