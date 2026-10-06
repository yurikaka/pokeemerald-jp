# Manual review findings

Anomaly log from manual review. Entries marked FIXED are resolved (verdicts
updated to `ok` with notes); entries without FIXED are open and pending a
user decision.

## Open items pending user decision

- `015_wallys_house.json[7]`: upstream 它 should be 他 (Wally). Fix in both repos.
- `022_dewford_town.json[4]`: upstream punctuation typo `别沮丧，！`.
- `110[14]`: upstream loose translation (details below).

| Batch | Index | Symbol | Issue |
|---|---|---|---|
| 015_wallys_house.json | 7 | PetalburgCity_WallysHouse_Text_YouMetWallyInEverGrandeCity | US汉化 source typo: 它 should be 他 (refers to Wally). Fix would need to land in both us_chs and this port. |
| 022_dewford_town.json | 4 | DewfordTown_Text_FishingAdvice | US汉化 upstream punctuation typo '别沮丧，！' |

## 061[7] ConcealedInPlanter wrong reference (FIXED)
- Override address was `0x0822C2CC`, which is the Battle Pyramid lobby fortune-teller script reference to `Text_HintDark` (`0x0822D000`, "あく タイプのポケモンたちが みえます").
- Chinese replacement was the Trick House "ConcealedInPlanter" text, so the fortune teller would have shown the wrong line.
- Fixed: 061 entry now targets the real planter script reference `0x0823CBE5 -> 0x0823D30C`.
- Batch 214 was missing `Text_HintDark` entirely (its reference had been stolen by the bad 061 mapping); added HintDark text + reference (`0x0822C2CC -> 0x0822D000`) using the US汉化 text.

## 061[7] → see above (fixed earlier)

## 107[0] GoingToMakeVolbeatStrong wrong Pokémon name (FIXED both repos)
- JP: バルビート (Volbeat). US汉化 mistakenly wrote 甜甜萤 (Illumise).
- The in-game trade gives the NPC Volbeat, so 电萤虫 is correct.
- Fixed: batch 107 us_encoded_hex re-encoded with 电萤虫; US汉化 scripts.inc updated too.

## 110[14] Route118_Text_DeandreDefeat upstream loose translation (not fixed)
- JP: ああ　だいじょうぶか！？　ボクのポケモン　1ごう　2ごう　3ごう！ (Are you OK? My Pokémon 1, 2, 3!)
- US汉化: 来吧，宝可梦！准备好了吗？宝可梦1、2、3？！ — reads like an intro; "are you okay" mistranslated as "准备好了吗".
- Faithful port of US汉化; candidate for upstream fix, pending user decision.

## 166[2] ShoalCave ExplainShellBell upstream typo — FIXED both repos
- US汉化 `data/text/shoal_cave.inc`: `原料每天都能采到原，` (stray 原) → `原料每天都能采到，`
- batch 166 us_encoded_hex updated to match corrected string (hex round-trip verified)
- Verdict: fix-text (upstream typo, fixed in both repos)


## 168[2][3] wallclock Confirm/Cancel CN texts swapped — FIXED
- wokann JP: gText_Cancel4="けってい"(confirm) @0x08591C15, gText_Confirm3="もどる　"(return) @0x08591C1A (symbol names inverted vs US)
- batch had けってい→返回 and もどる→确定 (swapped). Swapped hex so content matches: けってい→确定, もどる→返回
- Verdict: fix-text ×2


## 174[17] WonContestsWFriends upstream garbled — FIXED both repos
- us_chs strings.c: 赢得华丽大赛赢/个朋友 → 与朋友赢得华丽大赛
- batch 174 hex updated accordingly
- Verdict: fix-text


## 175[180-183] SEVII ISLE 6-9 left as raw English — FIXED
- us_chs has 七岛6号岛 etc.; batch now matches (pointer-table override, no length risk)
## 175[91] 海洋基地 vs upstream 海洋队基地 — noted, kept (display width)
## 175[112] MAPSEC_DYNAMIC -> empty matches upstream


## Sprite corruption: 5 batch reference_writes into compressed front sprites (FIXED)
- Root cause: batch generation searched the ROM for 4-byte pointer values and
  picked up coincidental matches inside compressed sprite LZ data, recording
  them as text references.
- Removed entries (each symbol still has its legitimate reference):
  - `201_battle_frontier_battle_dome_lobby.json` ref addr 0x08B8229E (inside Tropius anim_front)
  - `206_battle_frontier_battle_palace_battle_room.json` ref addr 0x08B77282 (inside Numel anim_front)
  - `229_battle_frontier_ranking_hall.json` ref addr 0x08B57D0C (inside Phanpy anim_front)
  - `260_littleroot_town_brendans_house_2_f.json` ref addr 0x08B8FFB1 (inside Registeel anim_front)
  - `419_union_room_0.json` ref addr 0x08B1A233 (inside Machamp anim_front)
- Symptom: front-sprite animation frames garbled for Machamp, Phanpy, Tropius
  (Numel and Registeel had latent corruption not yet noticed in-game).
- Verification: exact graphics-extent sweep (wokann incbin file sizes) over all
  batch override/reference_write addresses now reports 0 hits; rebuilt ROM has
  0 diff bytes in all 5 sprite regions. Manifest pointer_replacements (54)
  also swept: no graphics hits.

## Fishing_GotBite truncated Chinese text via 12-byte stack memcpy (FIXED)
- JP `Fishing_GotBite` (0x0808C4D6) copies `gText_OhABite` to a 12-byte stack
  buffer with `memcpy(sp+0xc, text, 0xC)` and prints from the stack. The JP
  string ひいてる　ひいてる！！ is exactly 12 bytes; the Chinese 啊！上钩了！
  with its FC16 prefix is 15 bytes, so the copy truncated it and printing read
  past the buffer into garbage (乱码).
- Fix (manifest code_patches): 0x0808C4F6 `add r2, sp, #0xC` (03aa) ->
  `ldr r2, [pc, #0x18]` (064a), loading the patched text pointer from the
  literal pool at 0x0808C510 directly. The memcpy remains but its result is
  unused; stack layout untouched.
- `Fishing_MonOnHook` (gText_PokemonOnHook) passes the pointer directly and
  was not affected.
