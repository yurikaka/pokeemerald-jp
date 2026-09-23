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
.global SummaryScreenPrintHook
.type SummaryScreenPrintHook, %function
.thumb_func
SummaryScreenPrintHook:
    @ Replaces SummaryScreen_PrintTextOnWindow (0x081C1ED8) wholesale.
    @ Identical to the original except the font id is chosen per string:
    @ the contest move page's Appeal/Jam labels only fit their 4-tile
    @ window in the 10 px small font (3 glyphs x 10 px <= 32 px).
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
