.syntax unified
.cpu arm7tdmi
.thumb

.section .text
.align 2

.equ JP_DECOMPRESS_GLYPH_TILE, 0x080047C9
.equ JP_RENDER_TEXT_NORMAL,     0x0800582D
.equ JP_RENDER_TEXT_COPY,       0x08005B33
.equ JP_RENDER_TEXT_REPEAT,     0x080059B3
.equ JP_CURRENT_GLYPH,          0x03003030
.equ JP_ADD_TEXT_PRINTER_4,     0x08199B85
.equ SUMMARY_TEXT_COLORS,       0x085ED17C

.global ChineseRenderHook
.type ChineseRenderHook, %function
.thumb_func
ChineseRenderHook:
    @ Replay the four instructions replaced at 0x08005820.
    ldrb r0, [r6, #0x1D]
    strb r0, [r6, #0x1E]
    ldr r0, [r6]
    ldrb r3, [r0]
    adds r0, #1
    str r0, [r6]

    push {r2-r7, lr}

    @ A string's EOS byte always returns the printer to Japanese mode.
    @ Without this, an untranslated string printed after a Chinese one by
    @ the same printer (such as a species name in the party screen or the
    @ Pokédex) would inherit Chinese mode and have its 0x60-0x7D katakana
    @ misread as Chinese high bytes.  r2 and r5 are stack-saved here, so
    @ this stays transparent to the original render loop.
    cmp r3, #0xFF
    bne .Lnot_eos
    movs r2, #1
    adds r5, r6, #0
    adds r5, #0x21
    strb r2, [r5]
.Lnot_eos:
    cmp r3, #0xF5
    bne .Lnot_compact_chinese
    movs r2, #0
    adds r5, r6, #0
    adds r5, #0x21
    strb r2, [r5]
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0
.Lnot_compact_chinese:

    @ Chinese is active only after EXT_CTRL_CODE_ENG.  Original Japanese
    @ strings remain in Japanese mode and therefore keep their single-byte
    @ katakana interpretation.
    adds r2, r6, #0
    adds r2, #0x21
    ldrb r2, [r2]
    cmp r2, #0
    bne .Lnot_chinese

    @ 0x60-0x7D encode the translated Chinese high-byte ranges.  0x65 and
    @ 0x7A correspond to the two holes in the US Chinese encoding.
    cmp r3, #0x7F
    beq .Lpunctuation
    cmp r3, #0x60
    blo .Lnot_chinese
    cmp r3, #0x7D
    bhi .Lnot_chinese
    cmp r3, #0x65
    beq .Lnot_chinese
    cmp r3, #0x7A
    beq .Lnot_chinese

    ldrb r2, [r0]
    cmp r2, #0xF6
    bhi .Lnot_chinese
    adds r0, #1
    str r0, [r6]
    subs r3, #0x5F
    lsls r3, r3, #8
    orrs r3, r2
    b .Lload_glyph

.Lpunctuation:
    ldrb r2, [r0]
    cmp r2, #0xF6
    bhi .Lnot_chinese
    adds r0, #1
    str r0, [r6]
    lsls r3, r3, #8
    orrs r3, r2

.Lload_glyph:
    adds r0, r3, #0
    ldrb r1, [r4]
    bl DecompressChineseGlyph
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_COPY
    bx r0

.Lnot_chinese:
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_NORMAL
    bx r0

.align 2
.global SetJapaneseTextMode
.type SetJapaneseTextMode, %function
.thumb_func
SetJapaneseTextMode:
    movs r0, #1
    adds r1, r6, #0
    adds r1, #0x21
    strb r0, [r1]
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0

.align 2
.global SetChineseTextMode
.type SetChineseTextMode, %function
.thumb_func
SetChineseTextMode:
    movs r0, #0
    adds r1, r6, #0
    adds r1, #0x21
    strb r0, [r1]
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0

.align 2
.global ChsItemIdGetName
.type ChsItemIdGetName, %function
.thumb_func
ChsItemIdGetName:
    push {lr}
    lsls r0, r0, #16
    lsrs r0, r0, #16
    ldr r3, =0x080D6C75
    bl .Litem_name_call
    lsls r0, r0, #4
    ldr r1, =ChsItemNames
    adds r0, r0, r1
    pop {r1}
    bx r1
.Litem_name_call:
    bx r3

.align 2
.global ChsItemIdGetDescription
.type ChsItemIdGetDescription, %function
.thumb_func
ChsItemIdGetDescription:
    push {lr}
    lsls r0, r0, #16
    lsrs r0, r0, #16
    ldr r3, =0x080D6C75
    bl .Litem_description_call
    lsls r0, r0, #2
    ldr r1, =ChsItemDescriptions
    ldr r0, [r1, r0]
    pop {r1}
    bx r1
.Litem_description_call:
    bx r3

.align 2
.global ChsBagPrintPocketName
.type ChsBagPrintPocketName, %function
.thumb_func
ChsBagPrintPocketName:
    push {r4, lr}
    cmp r1, #0
    beq .Lprint_pocket_name
    cmp r1, #8
    beq .Lprint_pocket_name
    b .Lbag_pocket_return
.Lprint_pocket_name:
    adds r0, r0, r1
    ldrb r4, [r0]
    subs r4, #0xF0
    cmp r4, #4
    bhi .Lbag_pocket_return
    sub sp, #24
    movs r0, #2
    movs r1, #0
    ldr r3, =0x08003B19
    bl .Lbag_pocket_call_r3
    movs r0, #2
    str r0, [sp]
    movs r0, #0
    str r0, [sp, #4]
    str r0, [sp, #8]
    str r0, [sp, #12]
    movs r0, #1
    str r0, [sp, #16]
    ldr r0, =ChsPocketNameXOffsets
    ldrb r3, [r0, r4]
    lsls r0, r4, #2
    ldr r2, =ChsPocketNames
    adds r2, r2, r0
    ldr r2, [r2]
    movs r0, #2
    movs r1, #1
    ldr r4, =0x081ADD95
    bl .Lbag_pocket_call_r4
    add sp, #24
.Lbag_pocket_return:
    pop {r4}
    pop {r0}
    bx r0
.Lbag_pocket_call_r3:
    bx r3
.Lbag_pocket_call_r4:
    bx r4

.align 2
.global ChsPocketNameIds
ChsPocketNameIds:
    .byte 0xF0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF
    .byte 0xF1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF
    .byte 0xF2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF
    .byte 0xF3, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF
    .byte 0xF4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF

.align 2
ChsPocketNameXOffsets:
    .byte 12, 6, 2, 12, 8

.align 2
.global SummaryScreenPrintHook
.type SummaryScreenPrintHook, %function
.thumb_func
SummaryScreenPrintHook:
    @ Replaces SummaryScreen_PrintTextOnWindow (0x081C1ED8) wholesale.
    @ Identical to the original except the contest move page's Appeal/Jam
    @ labels use the 10 px small font to fit their 4-tile window.
    push {r4, r5, r6, lr}
    sub sp, #20
    ldr r4, [sp, #36]
    ldr r5, [sp, #40]
    lsls r0, r0, #24
    lsrs r0, r0, #24
    lsls r2, r2, #24
    lsrs r2, r2, #24
    lsls r3, r3, #24
    lsrs r3, r3, #24
    lsls r4, r4, #24
    lsrs r4, r4, #24
    lsls r5, r5, #24
    lsrs r5, r5, #24
    movs r6, #0
    str r6, [sp]
    str r4, [sp, #4]
    lsls r4, r5, #1
    adds r4, r4, r5
    ldr r5, =SUMMARY_TEXT_COLORS
    adds r4, r4, r5
    str r4, [sp, #8]
    str r6, [sp, #12]
    str r1, [sp, #16]
    movs r6, #1
    ldr r4, =Chs_gText_Appeal
    cmp r1, r4
    beq .Lssp_small_font
    ldr r4, =Chs_gText_Jam
    cmp r1, r4
    bne .Lssp_font_ready
.Lssp_small_font:
    movs r6, #0
.Lssp_font_ready:
    movs r1, r6
    ldr r4, =JP_ADD_TEXT_PRINTER_4
    bl .Lssp_call_r4
    add sp, #20
    pop {r4, r5, r6}
    pop {r0}
    bx r0
.align 2
.Lssp_call_r4:
    bx r4

.align 2
.type DecompressChineseGlyph, %function
.thumb_func
DecompressChineseGlyph:
    push {r4-r7, lr}
    adds r4, r0, #0
    ldr r5, =JP_CURRENT_GLYPH

    cmp r1, #0
    beq .Lsmall_font
    ldr r6, =ChineseNormalFont
    movs r0, #12
    movs r1, #15
    b .Lset_dimensions

.Lsmall_font:
    ldr r6, =ChineseSmallFont
    movs r0, #10
    movs r1, #13

.Lset_dimensions:
    adds r7, r5, #0
    adds r7, #0x80
    strb r0, [r7]
    strb r1, [r7, #1]

    lsrs r2, r4, #8
    cmp r2, #0x7F
    bne .Lchinese_index

    @ Punctuation is sourced from the matching Latin font by its US glyph ID.
    lsls r3, r4, #24
    lsrs r3, r3, #24
    ldr r6, =LatinNormalFont
    ldrb r0, [r7]
    cmp r0, #10
    bne .Lhave_index
    ldr r6, =LatinSmallFont
    b .Lhave_index

.Lchinese_index:
    lsls r3, r4, #24
    lsrs r3, r3, #24
    cmp r2, #0x1B
    bls .Lafter_gap_1b
    subs r2, #1
.Lafter_gap_1b:
    cmp r2, #6
    bls .Lafter_gap_06
    subs r2, #1
.Lafter_gap_06:
    subs r2, #1
    lsls r2, r2, #8
    adds r3, r3, r2

.Lhave_index:
    lsls r3, r3, #6
    adds r4, r6, r3

    adds r0, r4, #0
    adds r1, r5, #0
    bl .Lcall_decompress
    adds r0, r4, #0
    adds r0, #16
    adds r1, r5, #0
    adds r1, #32
    bl .Lcall_decompress
    adds r0, r4, #0
    adds r0, #32
    adds r1, r5, #0
    adds r1, #64
    bl .Lcall_decompress
    adds r0, r4, #0
    adds r0, #48
    adds r1, r5, #0
    adds r1, #96
    bl .Lcall_decompress

    pop {r4-r7}
    pop {r0}
    bx r0

.Lcall_decompress:
    ldr r3, =JP_DECOMPRESS_GLYPH_TILE
    bx r3

.ltorg

.section .rodata
.align 2
.include "build/patch/texts.inc"

.global ChsEmptyString
ChsEmptyString:
    .byte 0xFF

.align 2
.global ChsMoveTypesGfx
ChsMoveTypesGfx:
    .incbin "build/patch/move_types.lz"

.align 2
.global ChsPokedexAreaUnknownGfx
ChsPokedexAreaUnknownGfx:
    .incbin "build/patch/pokedex_area_unknown.lz"

.align 2
.global ChsStatusIconsGfx
ChsStatusIconsGfx:
    .incbin "build/patch/status_icons.lz"

.align 2
.global ChsShopMoneyGfx
ChsShopMoneyGfx:
    .incbin "build/patch/shop_money.lz"

.align 2
.global ChsSummaryTitleTilesGfx
ChsSummaryTitleTilesGfx:
    .incbin "build/patch/summary_titles.lz"

.align 2
.global ChsSummaryInfoTilemap
ChsSummaryInfoTilemap:
    .incbin "build/patch/summary_info.lz"

.align 2
.global ChsSummaryInfoEggTilemap
ChsSummaryInfoEggTilemap:
    .incbin "build/patch/summary_info_egg.lz"

.align 2
.global ChsSummarySkillsTilemap
ChsSummarySkillsTilemap:
    .incbin "build/patch/summary_skills.lz"

.align 2
.global ChsSummaryBattleTilemap
ChsSummaryBattleTilemap:
    .incbin "build/patch/summary_battle.lz"

.align 2
.global ChsSummaryContestTilemap
ChsSummaryContestTilemap:
    .incbin "build/patch/summary_contest.lz"

.align 2
.global ChsSummaryEffectBattleTilemap
ChsSummaryEffectBattleTilemap:
    .incbin "patch/gfx/summary_effect_battle.bin"

.align 2
.global ChsSummaryEffectContestTilemap
ChsSummaryEffectContestTilemap:
    .incbin "patch/gfx/summary_effect_contest.bin"

.align 2
ChineseNormalFont:
    .incbin "build/patch/chinese_normal.latfont"
.align 2
ChineseSmallFont:
    .incbin "build/patch/chinese_small.latfont"
.align 2
LatinNormalFont:
    .incbin "build/patch/latin_normal.latfont"
.align 2
LatinSmallFont:
    .incbin "build/patch/latin_small.latfont"
