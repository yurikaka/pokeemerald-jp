# Fly map name residual (dt5)

Verified against Wokann `src/region_map.c::sub_08124910` and Japanese ASM.
The one-line name branch at `0x081249EA` prints into window 0 without
clearing it when moving between ordinary destinations. Original padded
Japanese names masked this omission; shorter Chinese names leave pixels
from the previous destination. The two-line special-destination branch
likewise prints window 1 without first filling it.

Insert a white (0x11) full-window fill before the first name printer in
each branch, through veneers at `0x081249EC` and `0x08124974`. Reproduce
the displaced loads and outgoing stack arguments, preserving the original
second-line printer, frame switching, name positions and BG update logic.
No destination IDs, cursor behavior or fly warp logic changes.
