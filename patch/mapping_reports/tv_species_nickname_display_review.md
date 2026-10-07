# TV species and nickname display review

Scope: all 33 TV programme handlers (32 dispatched by DoTVShow, plus
DoTVShowInSearchOfTrainers) and their species/nickname helpers.
Each entry below was checked against the corresponding naked function in
`../pokeemerald_wokann_dev/src/tv.c`, not inferred from pointer matches.

Follow-up: Fan Club Letter is a separate programme used by the reporter when
the lead Pokemon has its default Japanese name. It stores species, not a
Pokemon nickname. Its playback function DoTVShowPokemonFanClubLetter reads
species at record +0x02, multiplies it by six, and copies gSpeciesNames into
gStringVar2. Literal 0x080F2E00 was missing from the display redirections;
it now points to ChsSpeciesNameTokens. All other states of this playback
function were checked: there are no further species-table literals. Record
creation, player-name copies, and Easy Chat responses remain unchanged.

## Complete nickname copies (existing conversion, verified)

| Programme | Original StringCopy10 call | Species in saved record | Source nickname |
| --- | --- | --- | --- |
| Bravo contest interview | 0x080F1FB4 | r4 + 0x02 | r4 + 0x10 |
| Fan Club Opinions | 0x080F30EA | r4 + 0x02 | r4 + 0x10 |
| Name Rater | 0x080F26D8 | r5 + 0x02 | r5 + 0x04 |
| Name Rater | 0x080F276C | r5 + 0x02 | r5 + 0x04 |
| Name Rater | 0x080F28D8 | r5 + 0x02 | r5 + 0x04 |
| Successful Capture | 0x080F2998 | r5 + 0x10 | r5 + 0x04 |
| Successful Capture | 0x080F2A2C | r5 + 0x10 | r5 + 0x04 |
| Successful Capture | 0x080F2AA0 | r5 + 0x10 | r5 + 0x04 |
| Successful Capture | 0x080F2AE6 | r5 + 0x10 | r5 + 0x04 |
| Successful Capture | 0x080F2B16 | r5 + 0x10 | r5 + 0x04 |

These calls already branch to the patched 0x081B1814 entry. Its existing
ChsNicknameDisplayRouter selects the appropriate saved species field and calls
ChsCopyStoredNicknameForSpecies. That helper copies the source nickname into
the destination display buffer, then compares that copy with the original
Japanese species name. Equality emits the Chinese display token; inequality
preserves the custom nickname. The saved record is never modified.

Name Rater also splits nicknames and calculates nickname-derived values using
TV_GetNicknameSubstring and TV_GetNicknameSumMod8. These are not complete-name
copies and remain unchanged; do not feed Chinese tokens into these calculations.

## Species-only copies (new pointer redirections)

Each literal below supplies gSpeciesNames to a six-byte-stride StringCopy into
a display string variable. Redirect it to the six-byte ChsSpeciesNameTokens
table; do not compare with the nickname.

| Programme | Verified literals |
| --- | --- |
| Fan Club Opinions | 0x080F3100, 0x080F3138 |
| Name Rater | 0x080F26F4, 0x080F2854, 0x080F28CC |
| Successful Capture | 0x080F29B4, 0x080F2A3C, 0x080F2A78, 0x080F2AC4, 0x080F2AF8, 0x080F2B28 |

## Persistence boundaries

InterviewAfter_PkmnFanClubOpinions reads MON_DATA_NICKNAME directly into the
record at +0x10 and MON_DATA_SPECIES into +0x02. The capture and Name Rater
record creation paths are untouched. Playback only copies out of the record.
Original Japanese nickname storage, species values, name-derived calculations,
and the interview nickname comparison remain unchanged.

## Validation

The patch builder checks every redirected literal against original value
0x082EA31C. Build and binary verification are performed after this change.
No emulator playback test has yet been performed; test default and custom
nicknames in all four stored-species nickname programmes before claiming in-game verification.

## Full playback audit

Manually reviewed the species-table load, species * 6 calculation, destination,
shared copy paths and subsequent use in Wokann dev src/tv.c. The following
77 literals are display-only. 12 were included in the preceding fixes; this
full audit adds the remaining 65. The shared seen-species helper returns the
original numeric species; only its output display string changes.

| Programme / helper | Verified species-table literals |
| --- | --- |
| Shared random seen species | 0x080F0510 |
| BravoTrainerPokemonProfile | 0x080F1FCC, 0x080F20E4, 0x080F2124, 0x080F2158 |
| BravoTrainerBattleTower | 0x080F221C, 0x080F22C8, 0x080F2300, 0x080F23E4 |
| TheNameRaterShow | 0x080F26F4, 0x080F2854, 0x080F28CC |
| PokemonTodaySuccessfulCapture | 0x080F29B4, 0x080F2A3C, 0x080F2A78, 0x080F2AC4, 0x080F2AF8, 0x080F2B28 |
| PokemonTodayFailedCapture | 0x080F2BE0, 0x080F2C28 |
| PokemonFanClubLetter | 0x080F2E00 |
| PokemonFanClubOpinions | 0x080F3100, 0x080F3138 |
| PokemonNewsMassOutbreak | 0x080F31DC |
| PokemonContestLiveUpdates | 0x080F3374, 0x080F33D8, 0x080F341C, 0x080F3440, 0x080F3500, 0x080F3598, 0x080F35B0, 0x080F35C8, 0x080F35F4, 0x080F3660, 0x080F3678, 0x080F3690, 0x080F36A8, 0x080F36C0, 0x080F36EC, 0x080F3758, 0x080F3770, 0x080F3788, 0x080F37A0, 0x080F37B8, 0x080F37D0, 0x080F37E8, 0x080F3818, 0x080F3870, 0x080F3910, 0x080F3934, 0x080F3968, 0x080F39C4 |
| PokemonBattleUpdate | 0x080F3ADC, 0x080F3B18, 0x080F3BA0, 0x080F3BF8 |
| InSearchOfTrainers | 0x080F3FF4, 0x080F408C |
| PokemonAngler | 0x080F4130, 0x080F4178 |
| TheWorldOfMasters | 0x080F420C, 0x080F4258 |
| BreakingNewsTV | 0x080F4954, 0x080F499C, 0x080F4A2C, 0x080F4A7C, 0x080F4AEC, 0x080F4B2C, 0x080F4B88 |
| SecretBaseVisit | 0x080F4DE0 |
| PokemonBattleSeminar | 0x080F4F40, 0x080F4F88, 0x080F4FC0 |
| PokemonNewsBattleFrontier | 0x080F5780, 0x080F57B0, 0x080F57F8, 0x080F5828 |

### Other programme handlers

| Handler (DoTVShow prefix omitted) | Name-display finding / decision |
| --- | --- |
| TodaysSmartShopper | Player, place, items and counts; no Pokemon name displayed. |
| RecentHappenings | Player and Easy Chat words; stored species is not displayed. |
| DummiedOut | Empty handler. |
| 3CheersForPokeblocks | Player/blender names, flavor and color; no Pokemon name. |
| TodaysRivalTrainer | Player, map and counts; no Pokemon name. |
| DewfordTrendWatcherNetwork | Player and Easy Chat words; do not convert word library. |
| HoennTreasureInvestigators | Player, items and map; no Pokemon name. |
| FindThatGamer | Player and casino/game strings; no Pokemon name. |
| PokemonLotteryWinnerFlashReport | Player, prize and counts; no Pokemon name. |
| TrainerFanClubSpecial | Player/idol names, scores and Easy Chat; no Pokemon name. |
| TrainerFanClub | Player/idol names, scores and Easy Chat; no Pokemon name. |
| WhatsNo1InHoennToday | Player names and ranking/counts; no Pokemon name. |
| SecretBaseSecrets | Player/base names, items and flags; no Pokemon name. |
| SafariFanClub | Player and caught counts; no Pokemon name displayed. |
| SpotTheCuties | Four nickname copies from record +0x04, but original Japanese record has no species. Preserve nickname. |
| PokemonContestLiveUpdates2 | Lilycove Contest Lady, not the live contest programme above. Nickname +0x0B has no saved species. Preserve nickname. |

SecretBaseSecrets helper sub_080F59A4 counts set bits in record +0x0C;
it does not retrieve a species or nickname. Its action-state helper likewise
only reads flags. Neither requires a name hook.

### Deliberately protected Japanese paths

- 0x080F03D8: interview default-name comparison; retain original Japanese table.
- 0x080F1F88: Bravo default/custom-name branch comparison; retain original table.
- 0x080F07BC: TV_GetNicknameSubstring uses original name length and kana bytes
  for wordplay and a small temporary buffer; not a full species-name display.
- TV_GetNicknameSumMod8: original nickname-derived values, unchanged.
- SpotTheCuties and Lilycove Contest Lady: no stored species. Do not infer
  species from arbitrary custom nickname strings or add save-record fields.

Thus complete species-backed names are covered, but the two species-less
nickname programmes and intentional nickname fragments can still show Japanese.
This is a data limitation, not permission to change recording/persistence.

### Validation boundary

Ten complete stored-nickname call sites across four programme families use the
existing display conversion. The 77 literals above use Chinese tokens directly.
Interview and record creation functions remain untouched by these new literals;
no storage field, species numeric value or Easy Chat library is changed.
Build and binary checks are recorded below. Emulator playback is not available
in this audit; default/custom nicknames and every programme still need in-game
regression testing before claiming runtime success.

## Completed build / binary checks

- `make chs`: successful; output remains `pokeemerald_jp_chs.gba`.
- ROM SHA-1: `c6950da15a0b114cd9e0df860da848dace07a6f3`.
- All 77 whitelisted literals matched original `0x082EA31C` in baserom and
  point to `ChsSpeciesNameTokens` (`0x090B6E54`) in the built ROM.
- All ten complete nickname BL instructions target `0x081B1814`.
- Protected literals `0x080F03D8`, `0x080F1F88`, `0x080F07BC` still point
  to original Japanese `gSpeciesNames` in the built ROM.
- `make compare`: original Japanese ROM SHA-1 check passed.
- `git diff --check`: passed. No emulator tests performed.
