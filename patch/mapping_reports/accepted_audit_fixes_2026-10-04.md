# Accepted audit text fixes — 2026-10-04

Both Japanese-port batches and US Chinese source text receive the same eight
corrections below. Original imported audit reports remain unchanged.

| Symbol | Correction | Japanese-source evidence |
| --- | --- | --- |
| MauvilleCity_Text_UncleCanYouBattleWally | 能请你和来一场对战吗？ → 能请你和满充来一场对战吗？ | Wokann data/maps/MauvilleCity/scripts.inc:500 names ミツルくん as the opponent. |
| Route104_Text_RouteSignPetalburg | 1O4号道路 → 104号道路 | Wokann data/maps/Route104/scripts.inc:1057 explicitly uses 104. |
| MossdeepCity_SpaceCenter_2F_Text_Grunt7PostBattle | 输得比平常更惨！ → 比平常丢脸三倍！ | Wokann data/maps/MossdeepCity_SpaceCenter_2F/scripts.inc:417 says いつもの 3ばい かっこわるい. |
| SootopolisCity_House4_Text_AncientTreasuresWaitingInSea | 那里面一定有 → 那里面可能有 | Wokann data/maps/SootopolisCity_House4/scripts.inc:24 uses かも しれない, expressing possibility. |
| SootopolisCity_House6_Text_FirstGuestInWhileTakeDoll | 你好！你是我们 / 第一个客人， → 你好！好久没有 / 客人来了， | Wokann data/maps/SootopolisCity_House6/scripts.inc:36 says ひさしぶりの おきゃくさん. The slash here marks the retained line break. |
| gText_Var1CertainlyHowMany2 | 您要买几个{STR_VAR_1}？ → 您要买几个 / {STR_VAR_1}“{STR_VAR_2}”？ | Original JP text at 0x085C9903 includes both variables; Wokann src/shop.c prepares item name in gStringVar1 and move name in gStringVar2 at _080E0118 through _080E0168. |
| gArmaldoPokedexText | 住在地底下 → 住在陆地上 | Original Japanese description says ちじょうで くらす; original English says lives on land. |
| gMiloticPokedexText | 生活在广大的湖边 → 生活在大湖的底部 | Original Japanese description says おおきな みずうみの そこに; original English says at the bottom of large lakes. |

## Scope and safety

- Only text payloads change. Existing hook addresses, pointer-write targets,
  species names, saved data, and battle mechanics are unchanged.
- The ordinary purchase template gText_Var1CertainlyHowMany is unchanged.
  The restored second variable is a move name, not a quantity. The built JP ROM
  already points the shop producer's move-name literal at ChsMoveNames; it does
  not require a Japanese-mode wrapper for this translated name.
- Existing Japanese player-name wrappers in the Mauville dialogue are retained.
- Money-symbol placement, trainer-note line wrapping, battle placeholders,
  Frontier count-variable adaptation, and storage font controls are not reverted.
- The separately requested Encore correction is committed separately and is
  not counted among these eight fixes. Stockpile is unchanged.

## Validation

- Japanese make chs and vanilla make compare pass.
- US make passes.
- Six corrected dialogue/shop payloads match US source encoding and the built
  JP ROM; all six existing pointer writes resolve to their generated symbols.
- Both corrected Pokedex descriptions match US text and the built JP description
  pointers after the existing automatic wrapping. The JP Pokedex entry layout
  remains 28 bytes, with its description pointer at offset 12, matching Wokann
  include/pokedex.h.
- The ordinary purchase template remains byte-for-byte unchanged.
- No emulator gameplay test was performed. Fixes are committed by content;
  no push has been made for these fixes.

## Implementation commits

| Content | Japanese port | US Chinese |
| --- | --- | --- |
| Encore duration | 67a5276 | 6ffae39ea |
| Map dialogue | e405b84 | 0b86060f1 |
| TM purchase prompt | 3a31a63 | 085721d37 |
| Pokedex habitats | 39e1ca1 | b08e5a919 |
