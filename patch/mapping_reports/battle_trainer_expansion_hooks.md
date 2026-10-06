# Battle trainer expansion hook repair

## Reported reproduction

The Victory Road pair starts a two-opponent double battle and resets after the
trainer portraits slide, before any battle text. Talking to either trainer to
start a single battle works. VBA-M states 09/10 capture battle entry and reset.
This reproduction has not been run in an emulator in this environment.

## Source-backed defects

Reference: Wokann dev `src/battle_message.c`, naked
`BattleStringExpandPlaceholders` assembly.

1. Original trainer-class branches at `0x0814F172` and `0x0814F4CE` target
   `0x0814F5BE`, two bytes into the 16-byte function trampoline installed at
   `0x0814F5BC`. They skip its first `push {r0}`. The trampoline still performs
   a two-word pop, consuming an existing caller-stack word and leaving SP four
   bytes too high. Both normal trainer-class expansion paths are affected;
   the report does not establish that this defect is exclusive to double battles.
2. The 16-byte trainer-name trampoline at `0x0814F514` overwrites the literal
   `0x0203886C` at `0x0814F51C` with `0x0000BD01`. The original second-trainer
   entry at `0x0814F510` reads this literal before loading the trainer ID.
   Consequently it reads the ID from the wrong address. The trampoline also
   overwrites the unused original name-table literal at `0x0814F520`.
3. The class trampoline overwrites the Frontier trainer-ID literal
   `0x0203886E` at `0x0814F5C8` and part of the class-table literal at
   `0x0814F5CC`. Those original literals must remain valid for shared entries.

## Minimal repair

- Use the existing eight-byte, stack-neutral `ldr r3; bx r3; .word target`
  veneer at `0x0814F514` and `0x0814F5BC`.
- Retarget the two class branches from `0x0814F5BE` to `0x0814F5BC`.
- Keep all original literals from `0x0814F51C` and `0x0814F5C8` intact.
- Keep the Chinese helper bodies, trainer records, battle scripts, graphics,
  species names and move-name changes unchanged.

The veneer may clobber r3: the original shared copy continuation at
`0x0814F5DC` assigns r3 from sb before using it. Trainer-name lookup already
clobbers r1 through its existing helper; no additional calling convention
change is introduced.

## Verification

`patch/tools/verify_battle_trainer_hooks.py` checks the Wokann source entries,
original bytes, veneer targets, both branch destinations and preservation of
the surrounding literals and shared instructions. Runtime acceptance requires
retesting the two-opponent battle, both single battles and a Frontier battle.

State 09's PC inside LZ77 decompression does not by itself prove a bad graphics
pointer: BIOS decompression advances source/destination registers. The native
cave background table and compressed entry resources match the built ROM.
State 10's low main-loop PC alone also does not locate the original failure.
