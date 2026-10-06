# Storage PC party-full message (hz4)

The screenshot shows the external PC menu error when Withdraw is selected with
six party Pokemon, not the similar error inside the storage interface.

Wokann `src/pokemon_storage_system.c::Task_PokemonStorageSystemPC` checks
`task->data[2] == 0 && CountPartyMons() == PARTY_SIZE` and passes
`gUnknown_85CB55C` to `AddTextPrinterParameterized2`. The compiled object's
`.text.Task_PokemonStorageSystemPC` section is fixed at `0x080C6AF4`; its
`R_ARM_ABS32` relocation at offset `0x1BC` references `gUnknown_85CB55C`.
The resulting ROM text-pointer field is `0x080C6CB0 -> 0x085CB55C`.

The complete original 40-byte text is explicitly defined in Wokann
`src/strings.c`. Its message is `てもちのポケモンは いっぱいです！`, followed by
padding and a blank second line. It means the party is full.

US `src/pokemon_storage_system.c` uses `gText_PartyFull` for this same condition.
The Chinese definition in US `src/strings.c` is `同行的宝可梦已经满了！`.
Batch448 already contains that exact Chinese resource and references it from
the separate storage message table at `0x0854CA8C`.

Add the missed external-menu pointer to batch448, sharing the existing
`Chs_ChecklistLiteral_448_gText_PartyFull` resource. Do not change the party-size
check, window layout, storage logic, original Japanese byte array, or the
existing in-storage message reference.
