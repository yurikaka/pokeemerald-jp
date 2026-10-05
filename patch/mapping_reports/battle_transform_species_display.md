# Transform species display

Verified against Wokann dev:

- `battle_script_commands.c::Cmd_transformdataexecution` prepares
  `gBattleTextBuff1` using `PREPARE_SPECIES_BUFFER` and the target's species.
  It does not read the target's nickname for the transformed-into name.
- `battle_message.c::ExpandBattleTextBuffPlaceholders`, species branch
  `0x0814F7EC`, decodes that species and calls `GetSpeciesName`.
- `pokemon.c::GetSpeciesName` at `0x0806B3DC` reads the original Japanese
  species table. It also has non-display callers, so it must remain unchanged.

Hook only the species display branch at `0x0814F7F4`. Reproduce the
original species-ID combine, then write the existing five-byte Chinese
species display token (F5 F2 low high FF) into the original destination.
Return to `0x0814F7FC`; the original source-buffer advance remains intact.
Species IDs 412 and above retain the original GetSpeciesName path.

This covers species placeholders in battle messages, including Transform.
It does not modify battle Pokemon, transformation state, party data,
nicknames, the original species table or save data. The acting Pokemon's
nickname still follows the existing default-name comparison display path.
