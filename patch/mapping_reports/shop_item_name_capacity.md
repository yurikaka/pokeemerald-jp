# Shop item-name buffer capacity (kt2)

Verified against Wokann dev `src/shop.c::BuyMenuBuildListMenuTemplate`
and `BuyMenuSetListEntry`, plus `src/item.c::CopyItemName`.

The regular shop allocates `(itemCount + 1) * 11` bytes for copied display
names. It also multiplies item indices and the exit-entry index by 11.
Chinese names returned by the patched ItemId_GetName may require up to
16 bytes, including their compact-mode prefix and terminator. CopyItemName
uses StringCopy without truncation, so a long name overwrites the next
entry; filling that entry then overwrites the previous name's terminator.
This explains why kt2 shows the short first item correctly but subsequent
names run into one another.

Change only these immediate constants from 11 to 16:

- `0x080DF490`: allocation multiplier (`movs r1`).
- `0x080DF4B0`: item-entry stride (`movs r2`).
- `0x080DF4CC`: exit-entry stride (`movs r0`).

The list's name pointers, IDs, prices, item descriptions, purchasing logic
and save data remain unchanged. The correction applies to the shared
ordinary-shop list, not just the Frontier location. Decoration shops use
the same allocation; their fixed names remain comfortably within 16 bytes.

Run `python3 patch/tools/verify_shop_name_capacity.py` after building to
verify all Chinese item names fit, the three ROM instructions agree, and
adjacent-slot copying preserves terminators and a trailing canary.
