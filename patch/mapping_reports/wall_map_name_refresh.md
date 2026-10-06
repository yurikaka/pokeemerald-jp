# Wall map name refresh and full region title (dt6)

Wokann `src/field_region_map.c::PrintRegionMapSecName` explicitly omits
`FillWindowPixelBuffer` in the branch that prints a named map section. Thus
the field/wall map has the same long-to-short redraw issue previously fixed
separately for the Fly and Pokenav maps.

The compiled `field_region_map.o` `.text` section corresponds to ROM base
`0x0816FF84`. `PrintRegionMapSecName` is section offset `0x290`, ROM address
`0x08170214`. Its handler literal at `0x08170240` is `0x0203B99C`.
The map-section type is at handler+10 and the name begins at handler+12.

The aligned veneer at `0x08170224` replaces exactly:

```
movs r0, #2
str r0, [sp]
movs r0, #0
str r0, [sp, #4]
```

`ChsWallMapNameFill` first clears window 0 to `0x11`, reloads the name pointer
after the fill's caller-saved register clobbers, replays the four instructions,
and resumes at `0x0817022C` (Thumb target `0x0817022D`). The existing text printer,
map input/state logic, and empty-name branch remain intact.

The title reference is `0x08170140 -> 0x085C611C`, already redirected to
`Chs_gText_Hoenn` by batch411. Wokann defines the original `ホウエンちほう`
in `src/field_region_map.c`. The US Chinese resource says only `丰缘`;
this intentional user-requested extension changes it to `丰缘地区`.

`sFieldRegionMapWindowTemplates[WIN_TITLE]` has width 7 tiles (56 pixels).
The existing normal Chinese renderer advances 12 pixels per glyph, so four
glyphs occupy 48 pixels and the centered origin is x=4. Patch only the
`movs r3, #0` at `0x08170114` to `movs r3, #4`; keep font, y, frame and window
dimensions unchanged. The title string has only this one batch reference.
