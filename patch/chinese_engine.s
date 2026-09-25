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
.equ JP_ADD_TEXT_PRINTER,       0x0800449D
.equ JP_FILL_WINDOW_PIXEL_BUFFER, 0x08003B19
.equ JP_LOAD_PALETTE,           0x080A1201
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
.global ChsBattleMoveNamePlaceholderHook
.type ChsBattleMoveNamePlaceholderHook, %function
.thumb_func
ChsBattleMoveNamePlaceholderHook:
    ldr r0, =Chs_sText_AttackerUsedX + 18
    cmp r0, r9
    bne .Lbattle_move_name_raw
    ldr r0, =0x0203A874
    ldr r0, [r0]
    ldrh r0, [r0]
    ldr r1, =0x0162
    cmp r0, r1
    bhi .Lbattle_move_name_raw
    lsls r0, r0, #4
    ldr r1, =ChsMoveNames
    adds r4, r0, r1
    b .Lbattle_move_name_copy
.Lbattle_move_name_raw:
    ldr r1, =0x02022C1C
    ldrb r0, [r1]
    cmp r0, #0xFD
    bne .Lbattle_move_name_copy_raw
    ldr r4, =0x02021C54
    adds r0, r1, #0
    adds r1, r4, #0
    ldr r3, =0x0814F665
    bl .Lbattle_move_name_expand
    b .Lbattle_move_name_copy
.Lbattle_move_name_copy_raw:
    adds r4, r1, #0
.Lbattle_move_name_copy:
    ldr r0, =0x0814F5DD
    bx r0
.Lbattle_move_name_expand:
    bx r3

.align 2
.global ChsBattleExpNamePlaceholderHook
.type ChsBattleExpNamePlaceholderHook, %function
.thumb_func
ChsBattleExpNamePlaceholderHook:
    ldr r0, =Chs_sText_PkmnGainedEXP + 4
    cmp r0, r9
    beq .Lbattle_exp_name_from_buffer
    adds r0, #1
    cmp r0, r9
    bne .Lbattle_exp_name_original
.Lbattle_exp_name_from_buffer:
    ldr r1, =0x02022C0C
    ldrb r0, [r1]
    cmp r0, #0xFD
    beq .Lbattle_exp_name_expand_trim
.Lbattle_exp_name_copy_raw:
    ldr r1, =0x02022C0C
    adds r4, r1, #0
    b .Lbattle_exp_name_copy
.Lbattle_exp_name_original:
    ldr r1, =0x02022C0C
    ldrb r0, [r1]
    cmp r0, #0xFD
    beq .Lbattle_exp_name_expand
    b .Lbattle_exp_name_copy_raw
.Lbattle_exp_name_expand_trim:
    movs r0, #0xFF
    strb r0, [r1, #4]
    b .Lbattle_exp_name_expand
.Lbattle_exp_name_expand:
    ldr r4, =0x02021C40
    adds r0, r1, #0
    adds r1, r4, #0
    ldr r3, =0x0814F665
    bl .Lbattle_exp_name_expand_raw
    b .Lbattle_exp_name_copy
.Lbattle_exp_name_copy:
    ldr r0, =0x0814F5DD
    bx r0
.Lbattle_exp_name_expand_raw:
    bx r3

.ltorg

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
.global ChsGetBerryNameByType
.type ChsGetBerryNameByType, %function
.thumb_func
ChsGetBerryNameByType:
    push {r4, lr}
    adds r4, r1, #0
    lsls r0, r0, #24
    lsrs r0, r0, #24
    adds r0, #0x84
    bl ChsItemIdGetName
    adds r1, r0, #0
    adds r0, r4, #0
    ldr r3, =0x080088B9
    bl .Lberry_name_copy
    pop {r4}
    pop {r1}
    bx r1
.Lberry_name_copy:
    bx r3

.align 2
.global ChsTrainerNameFromId
.type ChsTrainerNameFromId, %function
.thumb_func
ChsTrainerNameFromId:
    push {lr}
    lsls r0, r0, #16
    lsrs r0, r0, #16
    ldr r1, =0x356
    cmp r0, r1
    bls .Ltrainer_name_valid
    movs r0, #0
.Ltrainer_name_valid:
    lsls r0, r0, #2
    ldr r1, =ChsTrainerNames
    ldr r0, [r1, r0]
    pop {r1}
    bx r1

.align 2
.global ChsTrainerClassNameFromId
.type ChsTrainerClassNameFromId, %function
.thumb_func
ChsTrainerClassNameFromId:
    push {lr}
    lsls r0, r0, #16
    lsrs r0, r0, #16
    ldr r1, =0x356
    cmp r0, r1
    bls .Ltrainer_class_id_valid
    movs r0, #0
.Ltrainer_class_id_valid:
    lsls r0, r0, #5
    ldr r1, =0x082E383C
    adds r0, r0, r1
    ldrb r0, [r0, #1]
    lsls r0, r0, #2
    ldr r1, =ChsTrainerClassNames
    ldr r0, [r1, r0]
    pop {r1}
    bx r1

.align 2
.global ChsBattleTrainerClassNameHook
.type ChsBattleTrainerClassNameHook, %function
.thumb_func
ChsBattleTrainerClassNameHook:
    cmp r0, #11
    bne .Lbattle_trainer_class_from_r0
    adds r0, r1, #0
.Lbattle_trainer_class_from_r0:
    lsls r0, r0, #24
    lsrs r0, r0, #24
    cmp r0, #65
    bls .Lbattle_trainer_class_valid
    movs r0, #0
.Lbattle_trainer_class_valid:
    lsls r0, r0, #2
    ldr r1, =ChsTrainerClassNames
    ldr r4, [r1, r0]
    ldr r0, =0x0814F5DD
    bx r0

.align 2
.global ChsBattleTrainerNameHook
.type ChsBattleTrainerNameHook, %function
.thumb_func
ChsBattleTrainerNameHook:
    bl ChsTrainerNameFromId
    adds r4, r0, #0
    ldr r0, =0x0814F5DD
    bx r0

.align 2
.global ChsBerryFirmness
ChsBerryFirmness:
    .4byte ChsBerryFirmnessVerySoft
    .4byte ChsBerryFirmnessSoft
    .4byte ChsBerryFirmnessHard
    .4byte ChsBerryFirmnessVeryHard
    .4byte ChsBerryFirmnessSuperHard

.ltorg

.align 2
.global ChsPrintAllBerryData
.type ChsPrintAllBerryData, %function
.thumb_func
ChsPrintAllBerryData:
    push {r4, lr}
    ldr r4, =0x08177FE9
    bl .Lberry_tag_call_r4
    ldr r4, =0x0817804D
    bl .Lberry_tag_call_r4
    ldr r4, =0x08178109
    bl .Lberry_tag_call_r4
    ldr r4, =0x08178189
    bl .Lberry_tag_call_r4
    ldr r4, =0x081781BD
    bl .Lberry_tag_call_r4
    bl ChsPrintBerryFlavorLabels
    pop {r4}
    pop {r0}
    bx r0

.align 2
.Lberry_tag_call_r4:
    bx r4

.align 2
.type ChsPrintBerryFlavorLabels, %function
.thumb_func
ChsPrintBerryFlavorLabels:
    push {r4, r5, lr}
    sub sp, #12
    movs r5, #4
    str r5, [sp]
    movs r5, #0
    str r5, [sp, #4]
    str r5, [sp, #8]
    ldr r0, =ChsBerryTagFlavorPalette
    movs r1, #0xE0
    movs r2, #32
    ldr r4, =JP_LOAD_PALETTE
    bl .Lberry_tag_call_r4
    movs r0, #4
    movs r1, #0
    ldr r4, =JP_FILL_WINDOW_PIXEL_BUFFER
    bl .Lberry_tag_call_r4
    ldr r4, =JP_ADD_TEXT_PRINTER

    movs r0, #4
    movs r1, #0
    ldr r2, =ChsBerryFlavorSpicy
    movs r3, #23
    bl .Lberry_tag_call_r4

    movs r0, #4
    movs r1, #0
    ldr r2, =ChsBerryFlavorDry
    movs r3, #55
    bl .Lberry_tag_call_r4

    movs r0, #4
    movs r1, #0
    ldr r2, =ChsBerryFlavorSweet
    movs r3, #87
    bl .Lberry_tag_call_r4

    movs r0, #4
    movs r1, #0
    ldr r2, =ChsBerryFlavorBitter
    movs r3, #119
    bl .Lberry_tag_call_r4

    movs r0, #4
    movs r1, #0
    ldr r2, =ChsBerryFlavorSour
    movs r3, #151
    bl .Lberry_tag_call_r4

    add sp, #12
    pop {r4, r5}
    pop {r0}
    bx r0

.ltorg

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
    push {r4-r7, lr}
    sub sp, #4
    adds r4, r0, #0
    adds r5, r1, #0
    ldr r0, =0x02021C7C
    cmp r4, r0
    bne .Lbag_pocket_direct

    ldrb r6, [r4]
    ldrb r7, [r4, #8]
    lsls r0, r6, #8
    orrs r0, r7
    ldr r1, =0x0203CB20
    ldr r1, [r1]
    ldr r2, =0x00000C44
    adds r1, r1, r2
    ldr r2, [r1]
    cmp r0, r2
    beq .Lbag_pocket_copy_cached
    str r0, [r1]
    adds r0, r6, #0
    movs r1, #0
    bl ChsBagCachePocketName
    adds r0, r7, #0
    movs r1, #8
    bl ChsBagCachePocketName
    b .Lbag_pocket_copy_cached

.Lbag_pocket_direct:
    adds r4, r4, r5
    ldrb r0, [r4]
    bl ChsBagDrawPocketName
    b .Lbag_pocket_return

.Lbag_pocket_copy_cached:
    cmp r5, #8
    bls .Lbag_pocket_offset_ok
    movs r5, #8
.Lbag_pocket_offset_ok:
    movs r0, #2
    movs r1, #7
    ldr r3, =0x0800401D
    bl .Lbag_pocket_call_r3
    adds r6, r0, #0
    ldr r4, =0x0203CB20
    ldr r4, [r4]
    ldr r0, =0x00000844
    adds r4, r4, r0
    lsls r5, r5, #5
    adds r4, r4, r5
    adds r0, r4, #0
    adds r1, r6, #0
    bl ChsBagCopyPocketTiles
    ldr r0, =0x00000200
    adds r4, r4, r0
    movs r0, #0x80
    lsls r0, r0, #1
    adds r6, r6, r0
    adds r0, r4, #0
    adds r1, r6, #0
    bl ChsBagCopyPocketTiles
    movs r0, #2
    movs r1, #2
    ldr r3, =0x08003529
    bl .Lbag_pocket_call_r3

.Lbag_pocket_return:
    add sp, #4
    pop {r4-r7}
    pop {r0}
    bx r0
.Lbag_pocket_call_r3:
    bx r3
.Lbag_pocket_call_r4:
    bx r4

.align 2
.type ChsBagDrawPocketName, %function
.thumb_func
ChsBagDrawPocketName:
    push {r4, lr}
    subs r0, #0xF0
    cmp r0, #4
    bhi .Lbag_draw_return
    adds r4, r0, #0
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
.Lbag_draw_return:
    pop {r4}
    pop {r0}
    bx r0

.align 2
.type ChsBagCachePocketName, %function
.thumb_func
ChsBagCachePocketName:
    push {r4-r7, lr}
    sub sp, #4
    adds r5, r1, #0
    bl ChsBagDrawPocketName
    movs r0, #2
    movs r1, #7
    ldr r3, =0x0800401D
    bl .Lbag_pocket_call_r3
    adds r4, r0, #0
    ldr r6, =0x0203CB20
    ldr r6, [r6]
    ldr r0, =0x00000844
    adds r6, r6, r0
    lsls r5, r5, #5
    adds r6, r6, r5
    adds r0, r4, #0
    adds r1, r6, #0
    bl ChsBagCopyPocketTiles
    ldr r0, =0x00000100
    adds r4, r4, r0
    ldr r0, =0x00000200
    adds r6, r6, r0
    adds r0, r4, #0
    adds r1, r6, #0
    bl ChsBagCopyPocketTiles
    add sp, #4
    pop {r4-r7}
    pop {r0}
    bx r0

.align 2
.type ChsBagCopyPocketTiles, %function
.thumb_func
ChsBagCopyPocketTiles:
    push {r4-r7}
    movs r2, #16
.Lbag_copy_tiles_loop:
    ldmia r0!, {r3-r6}
    stmia r1!, {r3-r6}
    subs r2, #1
    bne .Lbag_copy_tiles_loop
    pop {r4-r7}
    bx lr

.align 2
.global ChsSaveInfoFormat
.type ChsSaveInfoFormat, %function
.thumb_func
ChsSaveInfoFormat:
    push {r4, r5, r6, r7, lr}
    lsls r0, r0, #0x18
    lsrs r3, r0, #0x18
    lsls r2, r2, #0x18
    lsrs r2, r2, #0x18
    adds r5, r1, #0
    movs r1, #0xFC
    strb r1, [r5]
    adds r5, #1
    movs r0, #1
    strb r0, [r5]
    adds r5, #1
    strb r2, [r5]
    adds r5, #1
    strb r1, [r5]
    adds r5, #1
    movs r0, #3
    strb r0, [r5]
    adds r5, #1
    adds r2, #1
    strb r2, [r5]
    adds r5, #1
    cmp r3, #4
    bhi .Lsave_info_return
    lsls r0, r3, #2
    ldr r1, =.Lsave_info_jump_table
    adds r0, r0, r1
    ldr r0, [r0]
    mov pc, r0

.align 2
.Lsave_info_jump_table:
    .4byte .Lsave_info_player_name
    .4byte .Lsave_info_pokedex
    .4byte .Lsave_info_time
    .4byte .Lsave_info_region_name
    .4byte .Lsave_info_badges

.Lsave_info_player_name:
    ldr r0, =0x03005AF0
    ldr r1, [r0]
    adds r0, r5, #0
    ldr r3, =0x080088B9
    bl .Lsave_info_call_r3
    b .Lsave_info_return

.Lsave_info_pokedex:
    ldr r3, =0x0809CD05
    bl .Lsave_info_call_r3
    cmp r0, #0
    beq .Lsave_info_hoenn_dex
    movs r0, #1
    ldr r3, =0x080BFD4D
    bl .Lsave_info_call_r3
    b .Lsave_info_dex_count
.Lsave_info_hoenn_dex:
    movs r0, #1
    ldr r3, =0x080BFD9D
    bl .Lsave_info_call_r3
.Lsave_info_dex_count:
    adds r1, r0, #0
    lsls r1, r1, #0x10
    lsrs r1, r1, #0x10
    adds r0, r5, #0
    movs r2, #0
    movs r3, #3
    ldr r4, =0x080089D9
    bl .Lsave_info_call_r4
    adds r5, r0, #0
    movs r0, #0xFC
    strb r0, [r5]
    movs r0, #0x16
    strb r0, [r5, #1]
    movs r0, #0x6F
    strb r0, [r5, #2]
    movs r0, #0x8C
    strb r0, [r5, #3]
    movs r0, #0xFF
    strb r0, [r5, #4]
    b .Lsave_info_return

.Lsave_info_time:
    ldr r4, =0x03005AF0
    ldr r0, [r4]
    ldrh r1, [r0, #0x0E]
    adds r0, r5, #0
    movs r2, #0
    movs r3, #3
    ldr r6, =0x080089D9
    bl .Lsave_info_call_r6
    adds r5, r0, #0
    movs r0, #0xF0
    strb r0, [r5]
    adds r5, #1
    ldr r0, [r4]
    ldrb r1, [r0, #0x10]
    adds r0, r5, #0
    movs r2, #2
    movs r3, #2
    ldr r6, =0x080089D9
    bl .Lsave_info_call_r6
    b .Lsave_info_return

.Lsave_info_region_name:
    ldr r0, =0x02036FB8
    ldrb r1, [r0, #0x14]
    adds r0, r5, #0
    ldr r3, =0x081245E9
    bl .Lsave_info_call_r3
    b .Lsave_info_return

.Lsave_info_badges:
    ldr r4, =0x00000867
    movs r6, #0
    adds r7, r5, #1
.Lsave_info_badge_loop:
    lsls r0, r4, #0x10
    lsrs r0, r0, #0x10
    ldr r3, =0x0809D069
    bl .Lsave_info_call_r3
    lsls r0, r0, #0x18
    cmp r0, #0
    beq .Lsave_info_badge_next
    adds r6, #1
.Lsave_info_badge_next:
    adds r4, #1
    ldr r0, =0x0000086E
    cmp r4, r0
    ble .Lsave_info_badge_loop
    adds r0, r6, #0
    subs r0, #0x5F
    strb r0, [r5]
    adds r5, r7, #0
    movs r0, #0xFC
    strb r0, [r5]
    movs r0, #0x16
    strb r0, [r5, #1]
    movs r0, #0x63
    strb r0, [r5, #2]
    movs r0, #0x60
    strb r0, [r5, #3]
    movs r0, #0xFF
    strb r0, [r5, #4]

.Lsave_info_return:
    pop {r4, r5, r6, r7}
    pop {r0}
    bx r0
.Lsave_info_call_r3:
    bx r3
.Lsave_info_call_r4:
    bx r4
.Lsave_info_call_r6:
    bx r6

.ltorg

.global ChsPokedexPrintCategory
.type ChsPokedexPrintCategory, %function
.thumb_func
ChsPokedexPrintCategory:
    @ Replaces sub_080C0150 (0x080C0150). When r1 points into the relocated
    @ ChsPokedexEntries table, prints the Chinese category followed by the
    @ 宝可梦 suffix left-aligned at (x, y); otherwise replays the original
    @ kana renderer. The original "     ポケモン" string printed behind the
    @ category is blanked by a code patch at 0x085C8FC0.
    push {r4, r5, r6, r7, lr}
    push {r1}
    movs r4, r0
    movs r5, r2
    movs r6, r3
    ldr r0, =ChsPokedexEntries
    subs r0, r1, r0
    blo .Lpokedex_category_fallback
    ldr r1, =(387 * 28)
    cmp r0, r1
    bhs .Lpokedex_category_fallback
    movs r1, #28
    swi 0x06
    cmp r1, #0
    bne .Lpokedex_category_fallback
    add sp, #4
    lsls r0, r0, #2
    ldr r1, =ChsPokedexEntriesCategoryTable
    ldr r1, [r1, r0]
    sub sp, #24
    mov r2, sp
.Lpokedex_category_copy:
    ldrb r3, [r1]
    cmp r3, #0xFF
    beq .Lpokedex_category_suffix
    strb r3, [r2]
    adds r1, #1
    adds r2, #1
    b .Lpokedex_category_copy
.Lpokedex_category_suffix:
    ldr r1, =ChsPokedexEntriesCategorySuffix
    adds r1, #2
.Lpokedex_category_suffix_copy:
    ldrb r3, [r1]
    strb r3, [r2]
    cmp r3, #0xFF
    beq .Lpokedex_category_print
    adds r1, #1
    adds r2, #1
    b .Lpokedex_category_suffix_copy
.Lpokedex_category_print:
    lsls r0, r4, #0x18
    lsrs r0, r0, #0x18
    mov r1, sp
    movs r2, r5
    movs r3, r6
    ldr r4, =0x080BFFE1
    bl .Lpokedex_category_call_r4
    add sp, #24
    pop {r4, r5, r6, r7}
    pop {r0}
    bx r0

.Lpokedex_category_fallback:
    pop {r1}
    sub sp, #8
    movs r3, r6
    movs r0, r4
    lsls r0, r0, #0x18
    lsrs r6, r0, #0x18
    movs r4, r1
    movs r2, r5
    lsls r2, r2, #0x18
    lsrs r2, r2, #0x18
    mov ip, r2
    ldr r0, =0x080C0161
    bx r0
.Lpokedex_category_call_r4:
    bx r4

.ltorg

.global ChsStarterPokemonLabel
.type ChsStarterPokemonLabel, %function
.thumb_func
ChsStarterPokemonLabel:
    @ Replaces CreateStarterPokemonLabel (0x08134480) wholesale.
    @ Identical to the original except the category line is the Chinese
    @ category + 宝可梦 suffix (longer than the original 5-kana field, so
    @ the stack layout is widened) instead of inline kana + ポケモン.
    @ Stack frame: sp+0x0C category (20), sp+0x20 name (12),
    @              sp+0x2C window template (8), sp+0x34 template pointer.
    push {r4, r5, r6, r7, lr}
    mov r7, sl
    mov r6, sb
    mov r5, r8
    push {r5, r6, r7}
    sub sp, #0x38
    lsls r0, r0, #0x18
    lsrs r6, r0, #0x18
    movs r0, r6
    ldr r1, =0x08133E95
    bl .Lstarter_call_r1
    lsls r0, r0, #0x10
    lsrs r7, r0, #0x10
    movs r0, r7
    ldr r1, =0x0806CF69
    bl .Lstarter_call_r1
    lsls r0, r0, #0x10
    lsrs r0, r0, #0x10
    lsls r0, r0, #2
    ldr r1, =ChsPokedexEntriesCategoryTable
    ldr r2, [r1, r0]
    movs r5, #0
    add r1, sp, #0x20
    mov sl, r1
    mov r1, sp
    adds r1, #0x2C
    str r1, [sp, #0x34]
.Lstarter_category_copy:
    ldrb r0, [r2]
    cmp r0, #0xFF
    beq .Lstarter_category_suffix
    mov r1, sp
    adds r1, r1, r5
    adds r1, #0x0C
    strb r0, [r1]
    adds r2, #1
    adds r5, #1
    b .Lstarter_category_copy
.Lstarter_category_suffix:
    ldr r2, =ChsPokedexEntriesCategorySuffix
    adds r2, #2
.Lstarter_suffix_copy:
    ldrb r0, [r2]
    cmp r0, #0xFF
    beq .Lstarter_category_done
    mov r1, sp
    adds r1, r1, r5
    adds r1, #0x0C
    strb r0, [r1]
    adds r2, #1
    adds r5, #1
    b .Lstarter_suffix_copy
.Lstarter_category_done:
    mov r1, sp
    adds r1, r1, r5
    adds r1, #0x0C
    movs r0, #0xFF
    strb r0, [r1]
    movs r3, #0
    movs r5, #0
    lsls r4, r7, #1
    ldr r0, =0x082EA31C
    mov r8, r0
    lsls r6, r6, #1
    mov ip, r6
    adds r0, r4, r7
    lsls r0, r0, #1
    add r0, r8
    ldrb r0, [r0]
    cmp r0, #0xFF
    beq .Lstarter_name_done
.Lstarter_name_loop:
    mov r1, sl
    adds r2, r1, r5
    adds r1, r4, r7
    lsls r1, r1, #1
    adds r0, r3, r1
    add r0, r8
    ldrb r0, [r0]
    strb r0, [r2]
    adds r0, r3, #1
    lsls r0, r0, #0x18
    lsrs r3, r0, #0x18
    adds r0, r5, #1
    lsls r0, r0, #0x18
    lsrs r5, r0, #0x18
    adds r1, r3, r1
    add r1, r8
    ldrb r0, [r1]
    cmp r0, #0xFF
    beq .Lstarter_name_done
    cmp r3, #9
    bls .Lstarter_name_loop
.Lstarter_name_done:
    mov r2, sl
    adds r1, r2, r5
    movs r0, #0xFF
    strb r0, [r1]
    ldr r2, =0x08590BF4
    ldr r0, [r2]
    ldr r1, [r2, #4]
    str r0, [sp, #0x2C]
    str r1, [sp, #0x30]
    ldr r0, =0x08590C02
    add r0, ip
    mov sb, r0
    ldrb r0, [r0]
    lsls r0, r0, #8
    ldr r1, =0xFFFF00FF
    ldr r2, [sp, #0x2C]
    ands r2, r1
    orrs r2, r0
    str r2, [sp, #0x2C]
    ldr r1, =0x08590C03
    add r1, ip
    mov r8, r1
    ldrb r1, [r1]
    lsls r1, r1, #0x10
    ldr r0, =0xFF00FFFF
    ands r0, r2
    orrs r0, r1
    str r0, [sp, #0x2C]
    ldr r0, [sp, #0x34]
    ldr r1, =0x08003251
    bl .Lstarter_call_r1
    ldr r4, =0x030011F8
    strh r0, [r4]
    lsls r0, r0, #0x18
    lsrs r0, r0, #0x18
    movs r1, #0
    ldr r2, =0x08003B19
    bl .Lstarter_call_r2
    ldrb r0, [r4]
    ldr r6, =0x08590C1C
    str r6, [sp]
    movs r5, #0
    str r5, [sp, #4]
    add r1, sp, #0x0C
    str r1, [sp, #8]
    movs r1, #1
    movs r2, #0
    movs r3, #2
    ldr r7, =0x08199AFD
    bl .Lstarter_call_r7
    ldrb r0, [r4]
    str r6, [sp]
    str r5, [sp, #4]
    mov r2, sl
    str r2, [sp, #8]
    movs r1, #1
    movs r2, #0
    movs r3, #0x12
    ldr r7, =0x08199AFD
    bl .Lstarter_call_r7
    ldrb r0, [r4]
    ldr r1, =0x0800365D
    bl .Lstarter_call_r1
    movs r0, #0
    ldr r1, =0x08199655
    bl .Lstarter_call_r1
    mov r0, sb
    ldrb r1, [r0]
    lsls r0, r1, #0x1B
    movs r2, #0xFC
    lsls r2, r2, #0x18
    adds r0, r0, r2
    adds r1, #9
    lsls r1, r1, #3
    adds r1, #4
    lsls r1, r1, #0x18
    mov r2, r8
    ldrb r4, [r2]
    lsls r5, r4, #0x1B
    lsrs r5, r5, #0x18
    adds r4, #4
    lsls r4, r4, #0x1B
    lsrs r4, r4, #0x18
    lsrs r1, r1, #8
    orrs r1, r0
    lsrs r1, r1, #0x10
    movs r0, #0x40
    ldr r2, =0x08001145
    bl .Lstarter_call_r2
    lsls r5, r5, #8
    orrs r5, r4
    movs r0, #0x44
    movs r1, r5
    ldr r2, =0x08001145
    bl .Lstarter_call_r2
    add sp, #0x38
    pop {r3, r4, r5}
    mov r8, r3
    mov sb, r4
    mov sl, r5
    pop {r4, r5, r6, r7}
    pop {r0}
    bx r0
.Lstarter_call_r1:
    bx r1
.Lstarter_call_r2:
    bx r2
.Lstarter_call_r7:
    bx r7

.ltorg

@ r0 = dest, r1 = category string; copies category + 宝可梦 suffix,
@ FF-terminated. Clobbers r2, r3.
ChsAppendCategorySuffix:
.Lcategory_append_copy:
    ldrb r2, [r1]
    cmp r2, #0xFF
    beq .Lcategory_append_suffix
    strb r2, [r0]
    adds r0, #1
    adds r1, #1
    b .Lcategory_append_copy
.Lcategory_append_suffix:
    ldr r1, =ChsPokedexEntriesCategorySuffix
    adds r1, #2
.Lcategory_append_suffix_copy:
    ldrb r2, [r1]
    strb r2, [r0]
    cmp r2, #0xFF
    beq .Lcategory_append_done
    adds r0, #1
    adds r1, #1
    b .Lcategory_append_suffix_copy
.Lcategory_append_done:
    bx lr

.global ChsFactorySelectPrintMonCategory
.type ChsFactorySelectPrintMonCategory, %function
.thumb_func
ChsFactorySelectPrintMonCategory:
    @ Replaces Select_PrintMonCategory (0x0819B99C). Prints the Chinese
    @ category + 宝可梦 left-aligned instead of the right-aligned kana.
    push {r4, r5, lr}
    sub sp, #0x20
    ldr r5, =0x03001278
    ldr r0, [r5]
    ldrb r4, [r0, #3]
    cmp r4, #5
    bhi .Lselect_category_done
    movs r0, #5
    ldr r1, =0x0800365D
    bl .Lselect_category_call_r1
    movs r0, #5
    movs r1, #0
    ldr r2, =0x08003B19
    bl .Lselect_category_call_r2
    movs r0, #0x6C
    muls r0, r4, r0
    ldr r1, [r5]
    adds r0, r0, r1
    adds r0, #0x14
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A059
    bl .Lselect_category_call_r3
    lsls r0, r0, #0x10
    lsrs r0, r0, #0x10
    ldr r1, =0x0806CF69
    bl .Lselect_category_call_r1
    lsls r0, r0, #0x10
    lsrs r0, r0, #0x10
    lsls r0, r0, #2
    ldr r1, =ChsPokedexEntriesCategoryTable
    ldr r1, [r1, r0]
    add r0, sp, #0x0C
    bl ChsAppendCategorySuffix
    movs r0, #2
    str r0, [sp]
    movs r0, #0
    str r0, [sp, #4]
    str r0, [sp, #8]
    movs r0, #5
    movs r1, #1
    add r2, sp, #0x0C
    movs r3, #0
    ldr r4, =0x0800449D
    bl .Lselect_category_call_r4
    movs r0, #5
    movs r1, #2
    ldr r2, =0x08003529
    bl .Lselect_category_call_r2
.Lselect_category_done:
    add sp, #0x20
    pop {r4, r5}
    pop {r0}
    bx r0
.Lselect_category_call_r1:
    bx r1
.Lselect_category_call_r2:
    bx r2
.Lselect_category_call_r3:
    bx r3
.Lselect_category_call_r4:
    bx r4

.ltorg

.global ChsFactorySwapPrintMonCategory
.type ChsFactorySwapPrintMonCategory, %function
.thumb_func
ChsFactorySwapPrintMonCategory:
    @ Replaces Swap_PrintMonCategory (0x0819EE50). Prints the Chinese
    @ category + 宝可梦 left-aligned instead of the right-aligned kana.
    push {r4, r5, r6, lr}
    sub sp, #0x20
    ldr r6, =0x03001280
    ldr r0, [r6]
    ldrb r4, [r0, #3]
    movs r5, r4
    movs r0, #8
    movs r1, #0
    ldr r2, =0x08003B19
    bl .Lswap_category_call_r2
    cmp r4, #2
    bls .Lswap_category_have_mon
    movs r0, #8
    movs r1, #2
    ldr r2, =0x08003529
    bl .Lswap_category_call_r2
    b .Lswap_category_done
.Lswap_category_have_mon:
    movs r0, #8
    ldr r1, =0x0800365D
    bl .Lswap_category_call_r1
    ldr r0, [r6]
    ldrb r0, [r0, #0x14]
    cmp r0, #0
    bne .Lswap_category_rented
    movs r0, #0x64
    muls r0, r4, r0
    ldr r1, =0x02024190
    b .Lswap_category_get_species
.Lswap_category_rented:
    movs r0, #0x64
    muls r0, r5, r0
    ldr r1, =0x020243E8
.Lswap_category_get_species:
    adds r0, r0, r1
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A059
    bl .Lswap_category_call_r3
    lsls r0, r0, #0x10
    lsrs r0, r0, #0x10
    ldr r1, =0x0806CF69
    bl .Lswap_category_call_r1
    lsls r0, r0, #0x10
    lsrs r0, r0, #0x10
    lsls r0, r0, #2
    ldr r1, =ChsPokedexEntriesCategoryTable
    ldr r1, [r1, r0]
    add r0, sp, #0x0C
    bl ChsAppendCategorySuffix
    movs r0, #2
    str r0, [sp]
    movs r0, #0
    str r0, [sp, #4]
    str r0, [sp, #8]
    movs r0, #8
    movs r1, #1
    add r2, sp, #0x0C
    movs r3, #0
    ldr r4, =0x0800449D
    bl .Lswap_category_call_r4
    movs r0, #8
    movs r1, #2
    ldr r2, =0x08003529
    bl .Lswap_category_call_r2
.Lswap_category_done:
    add sp, #0x20
    pop {r4, r5, r6}
    pop {r0}
    bx r0
.Lswap_category_call_r1:
    bx r1
.Lswap_category_call_r2:
    bx r2
.Lswap_category_call_r3:
    bx r3
.Lswap_category_call_r4:
    bx r4

.ltorg

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
.global ChsSearchPrintHook
.type ChsSearchPrintHook, %function
.thumb_func
ChsSearchPrintHook:
    @ Replaces the Pokedex search-menu window print wrapper (0x080C07CC).
    @ Identical to the original except the search-option value prints
    @ (call sites 0x080C1790-0x080C1816) are drawn 1 pixel higher.
    push {r4, r5, lr}
    sub sp, #24
    ldr r4, [sp, #32]
    adds r5, r1, #0
    adds r3, r2, #0
    lsls r3, r3, #24
    add r1, sp, #20
    movs r2, #0
    strb r2, [r1]
    movs r2, #15
    strb r2, [r1, #1]
    movs r2, #2
    strb r2, [r1, #2]
    adds r2, r1, #0
    movs r1, #0
    str r1, [sp]
    str r1, [sp, #4]
    str r2, [sp, #8]
    subs r1, #1
    str r1, [sp, #12]
    str r0, [sp, #16]
    lsls r5, r5, #27
    lsrs r5, r5, #24
    lsrs r3, r3, #21
    movs r2, #2
    ldr r1, =0x080C1795
    cmp r4, r1
    blo .Lsearch_y_ready
    ldr r1, =0x080C181D
    cmp r4, r1
    bhi .Lsearch_y_ready
    movs r2, #1
.Lsearch_y_ready:
    adds r3, r3, r2
    lsls r3, r3, #24
    lsrs r3, r3, #24
    movs r0, #0
    movs r1, #1
    adds r2, r5, #0
    ldr r4, =JP_ADD_TEXT_PRINTER_4
    bl .Lsearch_call_r4
    add sp, #24
    pop {r4, r5}
    pop {r0}
    bx r0
.align 2
.Lsearch_call_r4:
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
.global ChsMenuInfoIcons
ChsMenuInfoIcons:
    .byte 12, 12, 0x00, 0
    .byte 32, 12, 0x20, 0
    .byte 32, 12, 0x64, 0
    .byte 32, 12, 0x60, 0
    .byte 32, 12, 0x80, 0
    .byte 32, 12, 0x48, 0
    .byte 32, 12, 0x44, 0
    .byte 32, 12, 0x6C, 0
    .byte 32, 12, 0x68, 0
    .byte 32, 12, 0x88, 0
    .byte 32, 12, 0xA4, 0
    .byte 32, 12, 0x24, 0
    .byte 32, 12, 0x28, 0
    .byte 32, 12, 0x2C, 0
    .byte 32, 12, 0x40, 0
    .byte 32, 12, 0x84, 0
    .byte 32, 12, 0x4C, 0
    .byte 32, 12, 0xA0, 0
    .byte 32, 12, 0x8C, 0
    .byte 42, 12, 0xA8, 0
    .byte 42, 12, 0xC0, 0
    .byte 42, 12, 0xC8, 0
    .byte 42, 12, 0xE0, 0
    .byte 42, 12, 0xE8, 0
    .byte 8, 8, 0xAE, 0
    .byte 8, 8, 0xAF, 0

.align 2
.global ChsMenuInfoTilesGfx
ChsMenuInfoTilesGfx:
    .incbin "patch/gfx/menu_info_tiles.4bpp"

.align 2
.global ChsPokedexAreaUnknownGfx
ChsPokedexAreaUnknownGfx:
    .incbin "build/patch/pokedex_area_unknown.lz"

.align 2
.global ChsPokedexInfoTilesGfx
ChsPokedexInfoTilesGfx:
    .incbin "build/patch/pokedex_info_tiles.lz"

.align 2
.global ChsPokedexInfoTilemap
ChsPokedexInfoTilemap:
    .incbin "build/patch/pokedex_info_tilemap.lz"

.align 2
.global ChsPokedexInterfaceGfx
ChsPokedexInterfaceGfx:
    .incbin "build/patch/pokedex_interface.lz"

.align 2
.global ChsPokedexInterfacePal
ChsPokedexInterfacePal:
    .2byte 0x020F, 0x7FFF, 0x1098, 0x5EF7, 0x5294, 0x398C, 0x20E5, 0x34E5
    .2byte 0x1400, 0x7FFF, 0x1FDD, 0x5C1F, 0x2746, 0x1203, 0x2E77, 0x0000

.align 2
.global ChsTrainerCardGfx
ChsTrainerCardGfx:
    .incbin "build/patch/trainer_card_tiles.lz"

.align 2
.global ChsPokedexSearchGfx
ChsPokedexSearchGfx:
    .incbin "build/patch/pokedex_search_tiles.lz"

.align 2
.global ChsStatusIconsGfx
ChsStatusIconsGfx:
    .incbin "build/patch/status_icons.lz"

.align 2
.global ChsShopMoneyGfx
ChsShopMoneyGfx:
    .incbin "build/patch/shop_money.lz"

.align 2
.global ChsEasyChatButtonWindowGfx
ChsEasyChatButtonWindowGfx:
    .incbin "build/patch/easy_chat_button_window.lz"

.align 2
.global ChsEasyChatModeGfx
ChsEasyChatModeGfx:
    .incbin "build/patch/easy_chat_mode.lz"

.align 2
.global ChsEasyChatModePal
ChsEasyChatModePal:
    .2byte 0x7FFF, 0x6F5B, 0x5AF6, 0x39CE
    .2byte 0x0000, 0x0000, 0x0000, 0x0000
    .2byte 0x0000, 0x0000, 0x0000, 0x0000
    .2byte 0x0000, 0x0000, 0x0000, 0x0000

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
.global ChsBerryTagWindowTemplates
ChsBerryTagWindowTemplates:
    .byte 0x01, 0x0B, 0x04, 0x0A, 0x02, 0x0F, 0xF3, 0x00
    .byte 0x01, 0x0B, 0x07, 0x0F, 0x04, 0x0F, 0x53, 0x00
    .incbin "baserom_jp.gba", 0x5CD0B0, 16
    .byte 0x01, 0x04, 0x0B, 0x16, 0x03, 0x0E, 0x07, 0x01
    .incbin "baserom_jp.gba", 0x5CD0C0, 8

.align 2
ChsBerryTagFlavorPalette:
    .2byte 0x73BB
    .2byte 0x73BB
    .incbin "baserom_jp.gba", 0x5CD07C, 28

.align 2
.global ChsBerryTagTiles
ChsBerryTagTiles:
    .incbin "build/patch/berry_tag_tiles.lz"

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
