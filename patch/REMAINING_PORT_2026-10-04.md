# Remaining display ports — 2026-10-04

## Current state

The seven identified active untranslated structured/display groups are now
implemented. This means implementation and automated verification are complete,
not that every game scene has passed a GBA playthrough. No new commits or pushes
are made by this work. The ROM remains `pokeemerald_jp_chs.gba`.

| Group | Implementation | Provenance and validation |
| --- | --- | --- |
| Pokéblock names | Batch 491: 14 names and list formatter | US strings; all colors and levels 0/1/99/255 executed, 24-byte list/save canaries preserved |
| Decoration names | 121 compact resources in relocated 28-byte records | US decoration header; all nontext fields and 11 interior name pointers checked |
| Link-card colors | Batch 492: four colors, unchanged five-byte stride | US strings; star indices 1–4 and original data checked |
| Blender local NPC names | Batch 493: six names, printer/results/ranking display hooks | US berry_blender.c; local player/link excluded, original records untouched |
| Mail signature | Batch 494: display-only prefix replacement | US From text; maximum seven-character JP sender, stack, colors, original buffer checked |
| Berry Fix Program | Six localized graphics/map/palette sets | US berry_fix_program.c; compressed ROM exactly matches previews, all pixels outside text regions unchanged |
| Contest NPC names | Batch 495: 96 nickname/trainer pairs, live and saved caption display consumers | JP original strings verified against ROM; exact species/name/trainer matching, record canaries and unmatched-name fallback checked |

## Fixed-layout implementation

`F5 F1 index` selects a full display string from a resource pointer table without
expanding the fixed-length field. The renderer uses only safe TextPrinter bytes
0x17, 0x18 and 0x1A, retains the original currentChar continuation, and resets
language mode at resource termination. All 139 resources, ASCII continuation,
Japanese continuation and adjacent-printer canaries pass ARM execution tests.

Pokéblock list labels use the existing small font and retain the original
nine-byte name area. Decoration records retain their original strides and data
fields. The Berry Fix loader/state machine is not rewritten. Its generated
palettes preserve every originally referenced palette bank, including the third
bank used by the Ruby/Sapphire boot-screen illustration.

Contest names remain Japanese in the original opponent records, gContestMons,
link packets and saved ContestWinner structures. Dedicated UI/script/caption
copies resolve exact original NPC name pairs to Chinese only for display.
The existing nickname conversion still handles unchanged default species names.
Unmatched custom player/link names are retained. Two old inline calls inside
newly replaced contest script functions were removed to avoid overlapping hooks.

## Checklist and historical reports

The 3326-row report previously called rows completed even when their execution
status was blocked. This work updates all 21 blocked rows, the mail-layout
rejection, and three graphics-only Berry Fix title rows with implementations
and evidence. Historical classifications are retained for comparison.

The older PORT_PROGRESS and FE570A7E5_QUEUE dashboards are explicitly historical;
they must not be used to restart completed map/text work. Report 430 now records
the structured-display implementations rather than claiming they are unresolved.

Intentional exclusions remain: Easy Chat words/keyboard, NPC trade OT and other
persistent exchanged names, and dormant Magma Hideout landmark text with no JP
consumer. They are not patched speculatively. Gen-3 description-source research
was deferred by the user and is not part of this work.

## Reproducible validation

With devkitARM on PATH:

```sh
make clean
make chs -j4
make compare
python3 patch/tools/build_berry_fix_gfx.py
python3 patch/tools/verify_berry_fix_gfx.py
/tmp/chs-port-verify-env/bin/python patch/tools/verify_remaining_display_port.py
```

The temporary verifier environment contains Unicorn 2.1.4. Other environments
can use any Python environment with Unicorn installed; graphics tools require
Pillow. Output reports are under build/patch. Address provenance and test results
are also recorded in mapping_reports/remaining_display_port_2026-10-04.json.

Clean Chinese build and vanilla ROM SHA-1 comparison pass. ARM helper tests and
graphics round-trip checks pass. These are not a full GBA emulator simulation:
interrupts, VRAM timing, link exchanges and complete state transitions are not
covered. Gameplay checks still needed are decoration purchase/listing, Pokéblock
list and blender results, mail display, link-card colors, contest results and
paintings, and Berry Fix menu/transfer screens.
