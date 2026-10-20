# Factory category label width

The select category window (template 5 at 085DBC64) is only 72px wide.
Four-character categories plus 宝可梦 total seven characters (84px in the
normal font). After ChsAppendCategorySuffix, ChsFactoryFitCategory switches
only labels of seven or more Chinese characters to the existing 8px narrow
font using F5 F3 / F5 F4. Shorter labels retain their original font. Apply
the same preparation to selection and swapping; no names are shortened.
Wokann battle_factory_screen.c Select_PrintMonCategory and
Swap_PrintMonCategory provide the corresponding native paths. The existing
category table contains Chinese-only labels, with at most seven characters
including the suffix; their prepared strings fit the 20-byte stack buffer.

Native execution rendered all 387 labels through both installed paths (774
cases), checking complete glyph counts, widths at most 72px, normal mode for
short labels and 8px narrow glyphs plus font restoration for long labels.
