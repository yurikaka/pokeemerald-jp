# `fe570a7e5` execution queue

**Historical queue:** do not resume from the old `NEXT` rows below. The later
3326-row review superseded this queue. See `REMAINING_PORT_2026-10-04.md` for
the final structured-display implementations and outstanding gameplay tests.

This file is the **resume point** for this US commit. Work only the first
`NEXT` row. Move it to `DONE` or `PARKED` with evidence before starting the
following row. `PARKED` means a direct ROM patch is unsafe; it is not work
silently considered complete.

## Batch membership

The following **368** batch JSON files have `source_commit: fe570a7e5`.
Ranges mean every number in that range; numbers not listed do not belong to
this US commit: `001–104`, `106–170`, `177–179`, `185–197`, `199–208`,
`210–241`, `243–251`, `253–257`, `259–260`, `269`, `271–273`, `275–285`,
`287–290`, `292–293`, `295–309`, `312–330`, `332–345`, `354–370`, `372`,
`374–376`, `381–389`, `391–395`, `397–398`, `408–425`, and `427`.

`428` and `429` also belong to this work but are manifest `code_patches`
(fixed trainer-name fields), not batch JSON files. `399–407` are explicitly
outside this commit and must not be worked before this queue is complete.

## Main map dialogue

| Area | Batches | Applied | Source/ROM state | Remaining work |
| --- | --- | ---: | --- | --- |
| Main story towns/routes through Shoal Cave | `001–167` (except `105`) | 3,455 texts / 3,680 pointers | **DONE** — all 3,680 pointers match Wokann after correcting batch 047's `Submersible` typo | Game-test story progression and NPC dialogue |
| Battle Frontier maps | `199–231` (except `209`) | 202 additional source/ROM-verified static texts / 225 pointers | Static direct coverage complete | 231 dynamic placeholders require per-buffer language tracing; 63 original texts have no ROM pointer |
| Remaining towns, dungeons, League, ship, and routes | `232–337` (listed ranges in Batch membership) | 5 additional source/ROM-verified static texts / 5 pointers | Static direct coverage complete | 19 dynamic placeholders require per-buffer language tracing; 49 no-pointer and 64 no-label entries are parked |

The source order for unfinished **map dynamic text** is `215`, then `216`, and
so on. Batch `199` is complete: player names remain Japanese-mode save data;
Arena opponent names come from the compact-Chinese fixed trainer-name table;
and the eligibility messages assemble Japanese species names and grammar.
Batch `200` is complete: player and round buffers remain Japanese-mode, while
Dome trainer fields already use compact Chinese. Batches `202–207` are
complete: `202` contains only the Japanese-mode saved player name, and
`203–207` contain no unresolved dynamic placeholders. Batches `208`, `210`,
and `214` are complete: each uses the same Japanese-mode banned-species
eligibility buffer verified for `199` and `201`. Batch `201` is complete:
eligibility data remains Japanese-mode, while item and fixed trainer names are
compact Chinese. Its three no-pointer/object-mismatch texts remain parked. The
three no-pointer texts in batch `199` are unused and remain parked in its
mapping report.

| Order | State | Exact scope | Resume from | Completion evidence |
| --- | --- | --- | --- | --- |
| 1 | DONE | Source/ROM-verifiable static **map** dialogue in batches `199–337` | `port_map_dialogue.py` with Wokann `event_scripts.o` text symbols | Each new target matches Wokann bytes at `0x081DABAC + object symbol`, and every patched pointer matches the original JP target |
| 2 | DONE | Battle Frontier **dynamic** map dialogue in batches `215–231` | `217`, `219`, `223`, `224`, and `231` reports record each runtime buffer source; 12 original no-pointer texts remain parked | Each placeholder is traced to Japanese- or compact-Chinese-mode data; no saved/link/player data is rewritten |
| 3 | DONE | Remaining town/dungeon/route dynamic map dialogue in batches `232–337` | `259`, `272`, `282`, `283`, `326`, `328`, and `329` trace every live runtime buffer; all remaining entries are source-level no-pointer/no-label records | Same as row 2; no saved/link/player data is rewritten |
| 4 | DONE | Shared script text in batches `338–398` | Consolidated dynamic sources: `343` (Match Call), `383` (Apprentice), `386` (TV), and `392` (Mauville Man); duplicate reports retain no additional ROM pointers | Dynamic values have a traced language source; no saved/link/player data is rewritten |
| 5 | DONE | `src/strings.c`: classify and port unresolved direct strings | All executable dynamic fields are mapped; remaining entries are preexisting coverage, non-unique Japanese byte strings, unsupported fixed-width layouts, or Wokann symbol differences and retain their source-level report reasons | Every dynamic entry is mapped; non-direct entries remain explicitly classified rather than guessed |
| 6 | DONE | `src/battle_message.c`, Union Room, and trade | `414`, `419`, `420`, and `425` map all live dynamic controls; `424` has no live dynamic field | All battle/link values are locally mode-wrapped without changing saved, link, or trade data |
| 7 | DONE | Four non-pointer designs | `patch/mapping_reports/430_fe570a7e5_structured_data_audit.json` | Contest display, decoration display, Berry Program graphics, and Magma Hideout landmark retain their separate audited designs |
| 8 | DONE | Build verification | `make chs` and `make compare` after every dynamic batch | Chinese ROM builds successfully and the vanilla Japanese ROM still compares exactly |

## Already source/ROM audited; awaiting game tests

- Battle Frontier trainer names: report `428_battle_frontier_trainer_names.json`.
- Battle Tent trainer names: report `429_battle_tent_trainer_names.json`.
- Pyramid map popup: report `408_pyramid_map_popup.json`.
- Mystery Event and Mystery Gift static messages: reports `409_mystery_event_messages.json` and `410_mystery_gift_cancel.json`.

## Audit-tool exceptions

`patch/wokann_audit_reports/` reports some static C tables as `needs_review`
because it cannot reconstruct their linker-emitted pointer tables. Do not use
that label as a task state. Reports 408–410 and 412–429 contain the manual
Wokann/ROM evidence for their respective static tables.
