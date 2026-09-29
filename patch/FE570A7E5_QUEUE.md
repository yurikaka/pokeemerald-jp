# `fe570a7e5` execution queue

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

The source order for unfinished **map dynamic text** is `199`, then `200`, and
so on. Resume at `patch/mapping_reports/199_battle_frontier_arena.json` →
`BattleFrontier_BattleArenaLobby_Text_NotEnoughValidMonsLvOpen` with
`STR_VAR_1`. The two Arena opponent-name messages are complete: Wokann's
`BufferArenaOpponentName` calls `GetFrontierTrainerName`, whose fixed source
field is already compact Chinese in report `428`; their placeholders must stay
in Chinese mode.

| Order | State | Exact scope | Resume from | Completion evidence |
| --- | --- | --- | --- | --- |
| 1 | DONE | Source/ROM-verifiable static **map** dialogue in batches `199–337` | `port_map_dialogue.py` with Wokann `event_scripts.o` text symbols | Each new target matches Wokann bytes at `0x081DABAC + object symbol`, and every patched pointer matches the original JP target |
| 2 | **NEXT** | Battle Frontier **dynamic** map dialogue in batches `199–231` | `patch/mapping_reports/199_battle_frontier_arena.json`, `BattleFrontier_BattleArenaLobby_Text_NotEnoughValidMonsLvOpen` | Each placeholder is traced to Japanese- or compact-Chinese-mode data; no saved/link/player data is rewritten |
| 3 | TODO | Remaining town/dungeon/route dynamic map dialogue in batches `232–337` | `patch/mapping_reports/259_lilycove_city_move_deleters_house.json`, `unresolved[0]` | Same as row 2; no-pointer/no-label entries retain a source-level parked reason |
| 4 | TODO | Shared script text: resolve candidates in batches `338–398` | `patch/mapping_reports/343_match_call.json`, then remaining files in numeric order | Dynamic values have a traced language source; no saved/link/player data is rewritten |
| 5 | TODO | `src/strings.c`: classify and port unresolved direct strings | `patch/mapping_reports/411_strings_c_direct.json`, `unresolved[0]` | Every entry is mapped, already covered, intentionally retained, or parked with a source-level reason |
| 6 | TODO | `src/battle_message.c`, Union Room, and trade | Reports `414`, `419`, `420`, `424`, `425` in numeric order | Wokann mapping proof and game tests for battle/link/trade behavior |
| 7 | TODO | Four non-pointer designs | `patch/mapping_reports/430_fe570a7e5_structured_data_audit.json` | Separate design and tests for contest display, decoration display, Berry Program graphics, and Magma Hideout landmark |
| 8 | TODO | Game verification | Newly built ROM and the batches/reports above | Normal dialogue, dynamic names, Frontier/Tent names, and link-sensitive paths tested |

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
