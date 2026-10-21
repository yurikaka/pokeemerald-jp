# Default Enigma Berry name

Verified against `../pokeemerald_wokann_dev` branch `dev`:
`src/item.c`, `CopyItemName` at `080D5EC8`, handles item `00AF` separately.
It copies `GetBerryInfo(43)->name`, then appends the Japanese suffix at
`085C9440`. Unlike `ItemId_GetName`, this path does not return the Chinese
item table's encoding marker. The translated Berry Info names contain only
the compact glyph bytes; they are unsuitable for this unmarked string path.

`src/berry.c`, `GetBerryInfo` and `IsEnigmaBerryValid`, distinguish the ROM
default from valid external berry data in the save. `ChsCopyItemName` uses
the complete Chinese item name for the default Enigma Berry. For a valid
external berry it preserves the native GetBerryInfo/copy/append behavior.
Other items use the existing Chinese ItemId_GetName path.

Validation: successful ROM build; checked the installed hook and the complete
encoded `谜芝果` item name. The current local save's external berry record is
empty. No save file was modified and no in-game emulator check was performed.
