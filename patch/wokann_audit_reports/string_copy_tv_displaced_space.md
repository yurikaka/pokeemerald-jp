# Displaced StringCopy function

Japanese `StringCopy` occupies `0x080088B8–0x080088D7` (32 bytes,
including alignment); the next function starts at `0x080088D8`.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x080088B8–0x080088C7` | 16 | Original string-copy entry to `ChsStringCopyOriginal`. |
| `0x080088C8–0x080088CF` | 8 | Explicit Tower TV copy entry to `ChsTvTowerNameCopy`. |
| `0x080088D0–0x080088D7` | 8 | Explicit Contest TV copy entry to `ChsTvContestNameCopy`. |

All 32 bytes are occupied; there is no candidate space left in this function.
The TV helpers retain program-type and source-field checks because several
call sites in each program copy strings other than the NPC name.
