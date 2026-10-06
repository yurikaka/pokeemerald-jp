# NPC names: Japanese persistence, Chinese display

The original 855 `gTrainers` records and 390 Frontier/Tent trainer records
remain byte-for-byte Japanese. Contest and in-game trade records are likewise
unchanged. Easy Chat vocabulary and Frontier/Tent speech word IDs remain JP.

`build_npc_name_display.py` matches JP/US symbolic identities and checks the
original ROM name bytes. Steven and the seven brains additionally check JP
`constants/opponents.h` IDs 804–811. Display mappings are separate ROM data.

Reference: `../pokeemerald_wokann_dev`, branch `dev`, commit
`0ce6f19`; battle_tower.c, frontier_util.c, battle_arena.c, battle_tent.c,
battle_dome.c, battle_message.c, pokemon.c, tv.c, link.c, link.h, global.tv.h
and pokenav_match_call_list.c, battle_bg.c, battle_main.c, string_util.c.

## Display boundaries

- Normal battle names retain the existing `ChsTrainerNameFromId` pointer table.
- Match Call list names resolve original trainer pointers to the separate CHS
  table before appending, so restoring JP data does not garble that list.
- `GetFrontierTrainerName` at 08162D24 delegates to the original JP getter.
  Only verified display callers substitute CHS. Interview persistence caller
  08164D03 and link-name producers 0803736F/0803737B retain JP.
- Brain getter 081A4944 localizes battle-message caller 0814F201 only. It
  matches the native getter's result, including the recorded battle's facility.
- Dome name getters 08195498/08195538 serve the verified display buffers.
- Steven's partner-name display literal 0806E6B0 points at an independent CHS
  string; his raw trainer record is not changed.
- Linked Tower VS names localize only its two simulated NPC slots at display
  caller 08035C1B. Compact names fit the original 8-byte display buffer.
  The Japanese link records and real player names are unchanged; every other
  `StringCopy7` call retains JP's original five-byte copying limit.
- TV display assumes an NPC when existing fields uniquely match the scene.
  Tower opponent names match the 300 Frontier trainers and Anabel only.
  Contest losers match original Japanese name plus saved species against the
  96 NPC records. Contest winners are always players and are never replaced.
  Unmatched/conflicting entries retain the original name. A same-name player
  (and same-species player in Contest) deliberately follows the NPC mapping,
  per the user's selected policy. Other TV types/player fields are untouched.

No save fields, padding bytes, or identity markers are added or repurposed.
TV inference only changes display buffers, never the stored Japanese records.
For example サダハル maps to 贞治 in Frontier and 定春 in Slateport Tent;
direct displays select the original table identity, not just a name match.

Existing saves containing previously written Chinese names are not migrated.

Removed false text pointer 085BCA12 from batch 386: those four bytes are two
Slateport Tent Easy Chat word IDs, not a `TVSpotTheCuties` text reference.

## Verification

`verify_npc_name_display.py` executes the compiled Thumb hooks and native name
getters with Unicorn. It checks all 855 normal display pointers, 398 NPC
identity mappings, every verified Frontier display caller, save/link callers,
seven brains and differing recorded facilities, Dome/Steven, Tower TV,
winning/losing contest TV, player-name guards, EOS return pointers, invalid TV
slots and save/buffer canaries. Facility selection/VarGet are stubbed.

Also run `verify_remaining_display_port.py`, `verify_easy_chat_words.py` and
`verify_battle_trainer_hooks.py`. These are helper/static checks, not a full
in-game GBA playthrough.
