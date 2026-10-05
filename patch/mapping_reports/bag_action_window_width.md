# Bag action window width

Verified against Wokann dev `src/data/item_menu_data.c::gUnknown_85DFA64`
and the grid-printing routine in `src/item_menu.c`.

The two-column 2x2 and 2x3 window templates at `0x085DFA74` and
`0x085DFA7C` start at tile 17 and are 12 tiles wide. The grid uses an
8-pixel text inset and 48-pixel column spacing. A four-character Chinese
label is 48 pixels wide, so its second-column end is eight pixels beyond
the original 96-pixel window.

Move the left edge to tile 15 and widen to 14 tiles, retaining the right
edge at tile 29, heights, palette, base tile, font and column spacing.
The second-column label now occupies pixels 56 through 103 of a
112-pixel window. This covers berry-blending selection and the other
two-column bag actions without shortening any label or changing actions.
