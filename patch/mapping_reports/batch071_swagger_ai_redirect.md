# Batch 071: Swagger AI branch mistaken for a daycare text reference

## Original erroneous mapping

`071_route117.json` redirected the four-byte operand at 0x0828A74F
from 0x0828AAA5 to `Chs_Route117_Text_TakeGoodCareOfIt`.
There was exactly one reference write for this symbol in the batch;
this was not an extra duplicate alongside a correct daycare reference.
The write entered the wrong subsystem entirely.

`git blame` attributes the wrong reference to commit `acd59add`.
The original generated mapping/audit reports remain as historical evidence.
In particular, `071_route117.json`'s mapping report already distinguishes
the erroneous expected-only reference from the correct mapped-only one.
The Wokann audit's `verified_source_definition` only established that the
daycare text symbol exists; it did not prove this operand was a text reference.

## Wokann cross-check and crash evidence

Wokann `data/battle_ai_scripts.s` has
`if_effect EFFECT_SWAGGER, AI_CBM_Confuse`. The macro in
`asm/macros/battle_ai_script.inc` emits opcode 0x37, one effect byte,
and a four-byte destination. `EFFECT_SWAGGER` is 118 (0x76).
At 0x0828A74D the original ROM has `37 76 A5 AA 28 08`.
The operand at +2 is the AI branch to 0x0828AAA5, not dialogue.

`AI_CBM_Confuse` checks confusion, Own Tempo, and Safeguard before
returning the move score. `BattleAICmd_if_effect` follows the destination
when the move's effect matches. `BattleAI_DoAIProcessing` dispatches
the next byte through `sBattleAICmdTable` without a bounds check.

User-provided VBA-M version-10 snapshots `07.sgm` and `08.sgm`
were inspected locally and are not included in the commit:

- The decoded EWRAM block begins at file offset 0x85DF.
- In 07, gUnknown_203A804 (0x0203A804, current AI script pointer) is zero.
- In 08, it is 0x0901DA88, the current build's Chinese daycare payload.
- The AI structure is at 0x02000448, movesetIndex is 3, and moveConsidered
  is 207 (Swagger). Mightyena's moves are 44, 316, 46, 207, with PP
  25, 40, 20, 15. The trainer's AI flags enable CheckBadMove.
- LR is 0x08131021, following the AI dispatch call at 0x0813101C.
  The payload begins with 0xFC. Dispatching index 0xFC reads
  0x14011045 from 0x0858FA3C, outside the valid AI command table,
  and attempts to execute a non-code destination. The later saved
  PC has run into invalid address space.

This establishes an AI bytecode misdirection, not a renderer, Intimidate,
or Combusken nickname fault. The first-turn choice prompt is visible
while the opponent AI performs its move scoring.

## Correct mapping and minimal fix

Wokann `data/scripts/day_care.inc`,
`Route117_EventScript_DaycareReceiveEgg`, uses
`msgbox Route117_Text_TakeGoodCareOfIt, MSGBOX_DEFAULT`.
The text label is explicitly at 0x08257BC6. Its `loadword 0` operand
is at 0x08257772; the original bytes are
`0F 00 C6 7B 25 08 09 04 25` including the following standard-script call.

Replace the erroneous batch entry with that verified daycare operand.
Keep the Chinese definition unchanged. This restores the original AI
branch and ensures the actual daycare dialogue is localized rather than
merely dropping the translation.

## Regression checks

`verify_battle_ai_scripts.py` verifies:

- All bytes in the battle AI script entry table and script region
  0x0828A480..0x0828C8D6 match the original ROM.
- The six-byte Swagger conditional retains its original destination.
- No batch text reference overlaps or targets this AI script region.
- The daycare text has one batch reference, to 0x08257772, with the
  correct original pointer, expected emitted payload, and source evidence.

Build and ROM checks can establish the repaired operand; a fresh emulator
run is still needed to confirm the full battle proceeds. Resume from 07
or an earlier state, not 08, which already contains the invalid AI pointer
and program counter.
