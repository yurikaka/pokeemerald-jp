# Displaced Pokédex search print code

The Japanese `sub_080C07CC_jp` occupies `0x080C07CC–0x080C080F`
(68 bytes); the next function starts at `0x080C0810`. The current patch uses:

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x080C07CC–0x080C07DB` | 16 | Function-entry trampoline to `ChsSearchPrintOriginal`. |
| `0x080C07DC–0x080C07E3` | 8 | Veneer to `ChsSearchPrintRaised`, called by six search-option print sites. |
| `0x080C07E4–0x080C080F` | 44 | Displaced original instructions; candidate space, not yet reused. |

Normal calls enter one of the two trampolines and do not execute the remaining
original instructions. Before reusing any of the 44 bytes, verify direct branch
targets and other references against the Japanese ROM and Wokann `dev`, check
for overlap with all active patches, and validate Thumb alignment and branch
range. The displaced bytes have not been proven free of every external entry.
