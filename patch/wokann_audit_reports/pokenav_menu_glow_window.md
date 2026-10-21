# PokeNav menu highlight window initialization

Verified against `../pokeemerald_wokann_dev` branch `dev`,
`src/pokenav_menu_handler_gfx.c`, `SetupPokenavMenuScanlineEffects`.
Its `BUGFIX` branch explicitly documents partial/missing glow caused by
leftover window values and replaces `SetGpuRegBits(REG_OFFSET_WIN0V,
DISPLAY_HEIGHT)` with `SetGpuReg(REG_OFFSET_WIN0V, DISPLAY_HEIGHT)`.

The native function is at `081CA0D8` (local assembly name `sub_081CA0D8`).
Immediately before the BL at `081CA108`, r0 is `0x44` (WIN0V), and r1 is
`0xA0` (160). The original BL targets `08001200`, SetGpuRegBits. The patch
changes only that BL to target `08001144`, SetGpuReg.

The old write ORs 0x00A0 into existing state, retaining the previous top
boundary and some bottom-boundary bits. The new write establishes the full
visible vertical range [0,160), allowing the menu's existing per-scanline
horizontal window and brightness animation to affect the whole selected row.
No option graphics, palettes or animation timing are changed by this fix.

Validation: successful ROM build; decoded the installed Thumb BL and checked
its SetGpuReg destination and unchanged register/value setup. In-game
verification remains pending.
