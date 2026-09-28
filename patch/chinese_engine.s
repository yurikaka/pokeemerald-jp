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
.equ JP_SPECIES_NAMES,          0x082EA31C
.equ JP_SPECIES_NAME_BYTES,     (412 * 6)
.equ JP_GET_MON_GENDER,         0x08069AF5
.equ JP_NATIONAL_DEX_TO_SPECIES, 0x0806CED1
.equ JP_POKEDEX_PRINT_TEXT,     0x080BFFE1
.equ JP_SUMMARY_PRINT_TEXT,     0x081C1ED9
.equ JP_GET_STRING_WIDTH,       0x08005DAD
.equ SUMMARY_TEXT_COLORS,       0x085ED17C
.equ JP_ADD_WINDOW,             0x08003251
.equ JP_REMOVE_WINDOW,          0x08003445
.equ JP_FILL_WINDOW_PIXEL_BUFFER, 0x08003B19
.equ JP_GET_WINDOW_ATTRIBUTE,   0x0800401D
.equ JP_ADD_TEXT_PRINTER_PARAM4, 0x08199B85
.equ JP_ADD_TEXT_PRINTER_PARAM3, 0x08199AFD
.equ JP_GET_BATTLER_SIDE,       0x080A62F9
.equ JP_IS_DOUBLE_BATTLE,       0x080A63E9
.equ JP_CPU_SET,                0x082959BD
.equ TEXT_MODE_OFFSET,         0x17
.equ TEXT_MODE_JAPANESE,       0
.equ TEXT_MODE_CHINESE,        1
.equ TEXT_MODE_COMPACT_SPECIES, 2
.equ TEXT_MODE_MUZAIPIXEL,     3
.equ TEXT_MODE_MUZAIPIXEL_JAPANESE, 4
.equ TEXT_SPECIES_ID_LO_OFFSET, 0x18
.equ TEXT_SPECIES_ID_HI_OFFSET, 0x19
.equ TEXT_SPECIES_CHAR_OFFSET,  0x1A

.align 2
.global ChsDisplayPartyPokemonBarDetail
.type ChsDisplayPartyPokemonBarDetail, %function
.thumb_func
ChsDisplayPartyPokemonBarDetail:
    push {r4-r7, lr}
    sub sp, #0x2C
    lsls r4, r0, #24
    lsrs r4, r4, #24
    adds r5, r1, #0
    lsls r6, r2, #24
    lsrs r6, r6, #24
    adds r7, r3, #0
    ldrb r0, [r5]
    cmp r0, #0xF5
    bne .Lparty_name_ready
    ldrb r0, [r5, #1]
    cmp r0, #0xF2
    bne .Lparty_name_ready
    ldrb r0, [r5, #2]
    ldrb r1, [r5, #3]
    lsls r1, r1, #8
    orrs r0, r1
    ldr r1, =412
    cmp r0, r1
    bhs .Lparty_name_ready
    add r1, sp, #0x0C
    movs r2, #5
    bl ChsWriteNarrowSpeciesName
    cmp r0, #0
    beq .Lparty_name_ready
    add r5, sp, #0x0C
.Lparty_name_ready:
    lsls r0, r6, #1
    adds r0, r0, r6
    ldr r1, =0x085E10B4
    adds r0, r0, r1
    str r0, [sp]
    movs r0, #0
    str r0, [sp, #4]
    str r5, [sp, #8]
    adds r0, r4, #0
    movs r1, #0
    ldrb r2, [r7]
    ldrb r3, [r7, #1]
    ldr r4, =JP_ADD_TEXT_PRINTER_PARAM3
    bl .Lparty_name_call_r4
    add sp, #0x2C
    pop {r4-r7}
    pop {r0}
    bx r0
.Lparty_name_call_r4:
    bx r4

.align 2
.global ChsPrintMonTrainerMemo
.type ChsPrintMonTrainerMemo, %function
.thumb_func
ChsPrintMonTrainerMemo:
    push {lr}
    bl ChsUseMuzaiIfLong
    pop {r0}
    push {r0}
    sub sp, #8
    ldr r0, =0x085ED114
    movs r1, #3
    ldr r3, =0x081C2621
    bl .Ltrainer_memo_call_r3
    lsls r0, r0, #24
    lsrs r0, r0, #24
    ldr r3, =0x081C2A5D
    bx r3
.Ltrainer_memo_call_r3:
    bx r3

.align 2
.type ChsUseMuzaiIfLong, %function
.thumb_func
ChsUseMuzaiIfLong:
    push {r4-r7, lr}
    ldr r4, =0x02021C7C
    adds r5, r4, #0
    movs r7, #0
.Lmemo_scan:
    ldrb r0, [r5]
    cmp r0, #0xFE
    beq .Lmemo_line_end
    cmp r0, #0xFF
    beq .Lmemo_line_end
    cmp r0, #0xFC
    beq .Lmemo_control
    cmp r0, #0xF5
    beq .Lmemo_skip_one
    cmp r0, #0xF7
    beq .Lmemo_skip_two
    cmp r0, #0xF8
    beq .Lmemo_skip_two
    cmp r0, #0xF9
    beq .Lmemo_symbol
    cmp r0, #0x7F
    beq .Lmemo_chinese_pair
    cmp r0, #0x60
    blo .Lmemo_single
    cmp r0, #0x7D
    bhi .Lmemo_single
    cmp r0, #0x65
    beq .Lmemo_single
    cmp r0, #0x7A
    beq .Lmemo_single
.Lmemo_chinese_pair:
    ldrb r0, [r5, #1]
    cmp r0, #0xF6
    bhi .Lmemo_single
    adds r5, #2
    adds r7, #12
    b .Lmemo_scan
.Lmemo_single:
    adds r5, #1
    adds r7, #8
    b .Lmemo_scan
.Lmemo_skip_one:
    adds r5, #1
    b .Lmemo_scan
.Lmemo_skip_two:
    adds r5, #2
    b .Lmemo_scan
.Lmemo_symbol:
    adds r5, #2
    adds r7, #8
    b .Lmemo_scan
.Lmemo_control:
    ldrb r0, [r5, #1]
    cmp r0, #4
    beq .Lmemo_control_three_args
    cmp r0, #1
    beq .Lmemo_control_one_arg
    cmp r0, #2
    beq .Lmemo_control_one_arg
    cmp r0, #3
    beq .Lmemo_control_one_arg
    cmp r0, #5
    beq .Lmemo_control_one_arg
    adds r5, #2
    b .Lmemo_scan
.Lmemo_control_one_arg:
    adds r5, #3
    b .Lmemo_scan
.Lmemo_control_three_args:
    adds r5, #5
    b .Lmemo_scan
.Lmemo_line_end:
    cmp r7, #156
    bls .Lmemo_done
    adds r6, r5, #0
.Lmemo_find_eos:
    ldrb r0, [r5]
    cmp r0, #0xFF
    beq .Lmemo_check_capacity
    adds r5, #1
    b .Lmemo_find_eos
.Lmemo_check_capacity:
    subs r0, r5, r4
    ldr r1, =0x3E3
    cmp r0, r1
    bhi .Lmemo_done
    adds r1, r5, #0
.Lmemo_shift_restore:
    ldrb r0, [r1]
    strb r0, [r1, #2]
    cmp r1, r6
    beq .Lmemo_write_restore
    subs r1, #1
    b .Lmemo_shift_restore
.Lmemo_write_restore:
    movs r0, #0xF5
    strb r0, [r6]
    movs r0, #0xF4
    strb r0, [r6, #1]
    adds r5, #2
    adds r1, r5, #0
.Lmemo_shift_start:
    ldrb r0, [r1]
    strb r0, [r1, #2]
    cmp r1, r4
    beq .Lmemo_write_start
    subs r1, #1
    b .Lmemo_shift_start
.Lmemo_write_start:
    movs r0, #0xF5
    strb r0, [r4]
    movs r0, #0xF3
    strb r0, [r4, #1]
.Lmemo_done:
    pop {r4-r7}
    pop {r0}
    bx r0

.global ChineseRenderHook
.type ChineseRenderHook, %function
.thumb_func
ChineseRenderHook:
    strb r0, [r6, #0x1E]
    ldrb r1, [r6, #TEXT_MODE_OFFSET]
    cmp r1, #TEXT_MODE_COMPACT_SPECIES
    bne .Lnot_compact_species_entry
    b .Lcompact_species_entry
.Lnot_compact_species_entry:
    ldr r0, [r6]
.Lredirect_direct_species_name:
    ldr r1, =JP_SPECIES_NAMES
    cmp r0, r1
    blo .Lread_current_character
    subs r2, r0, r1
    ldr r1, =JP_SPECIES_NAME_BYTES
    cmp r2, r1
    bhs .Lread_current_character
    movs r1, #0
.Lspecies_name_index:
    cmp r2, #6
    blo .Lspecies_name_aligned
    subs r2, #6
    adds r1, #1
    b .Lspecies_name_index
.Lspecies_name_aligned:
    cmp r2, #0
    bne .Lread_current_character
    lsls r1, r1, #2
    ldr r2, =ChsSpeciesNames
    ldr r0, [r2, r1]
    ldrb r2, [r6, #4]
    cmp r2, #0x13
    bne .Lread_current_character
    adds r2, r0, #1
    movs r1, #0
.Lsummary_species_glyph_count:
    ldrb r3, [r2]
    cmp r3, #0xFF
    beq .Lsummary_species_glyph_counted
    cmp r3, #0x7F
    beq .Lsummary_species_glyph_pair
    cmp r3, #0x60
    blo .Lsummary_species_glyph_single
    cmp r3, #0x7D
    bhi .Lsummary_species_glyph_single
    cmp r3, #0x65
    beq .Lsummary_species_glyph_single
    cmp r3, #0x7A
    beq .Lsummary_species_glyph_single
.Lsummary_species_glyph_pair:
    adds r2, #2
    b .Lsummary_species_glyph_next
.Lsummary_species_glyph_single:
    adds r2, #1
.Lsummary_species_glyph_next:
    adds r1, #1
    b .Lsummary_species_glyph_count
.Lsummary_species_glyph_counted:
    cmp r1, #4
    blo .Lread_current_character
    movs r2, #TEXT_MODE_MUZAIPIXEL_JAPANESE
    strb r2, [r6, #TEXT_MODE_OFFSET]
.Lread_current_character:
    ldrb r3, [r0]
    adds r0, #1
    str r0, [r6]

    push {r2-r7, lr}

    cmp r3, #0xFF
    bne .Lnot_eos
    movs r2, #TEXT_MODE_JAPANESE
    strb r2, [r6, #TEXT_MODE_OFFSET]
.Lnot_eos:
    cmp r3, #0xF5
    bne .Lnot_compact_chinese
    ldrb r2, [r0]
    cmp r2, #0xF3
    beq .Lset_muzaipixel_mode
    cmp r2, #0xF4
    beq .Lrestore_normal_chinese_mode
    cmp r2, #0xF2
    bne .Lset_compact_chinese_mode
    ldrb r2, [r0, #1]
    ldrb r4, [r0, #2]
    lsls r4, r4, #8
    orrs r2, r4
    ldr r4, =(412)
    cmp r2, r4
    bhs .Lset_compact_chinese_mode
    strb r2, [r6, #TEXT_SPECIES_ID_LO_OFFSET]
    lsrs r4, r2, #8
    strb r4, [r6, #TEXT_SPECIES_ID_HI_OFFSET]
    movs r4, #1
    strb r4, [r6, #TEXT_SPECIES_CHAR_OFFSET]
    adds r0, #3
    str r0, [r6]
    movs r2, #TEXT_MODE_COMPACT_SPECIES
    strb r2, [r6, #TEXT_MODE_OFFSET]
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0
.Lset_compact_chinese_mode:
    ldrb r2, [r6, #TEXT_MODE_OFFSET]
    cmp r2, #TEXT_MODE_MUZAIPIXEL_JAPANESE
    bne .Lset_normal_chinese_mode
    movs r2, #TEXT_MODE_MUZAIPIXEL
    b .Lstore_compact_chinese_mode
.Lset_normal_chinese_mode:
    movs r2, #TEXT_MODE_CHINESE
.Lstore_compact_chinese_mode:
    strb r2, [r6, #TEXT_MODE_OFFSET]
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0
.Lset_muzaipixel_mode:
    movs r2, #TEXT_MODE_MUZAIPIXEL
    b .Lset_muzaipixel_state
.Lrestore_normal_chinese_mode:
    movs r2, #TEXT_MODE_CHINESE
.Lset_muzaipixel_state:
    strb r2, [r6, #TEXT_MODE_OFFSET]
    adds r0, #1
    str r0, [r6]
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0
.Lnot_compact_chinese:
    ldrb r2, [r6, #TEXT_MODE_OFFSET]
    cmp r2, #TEXT_MODE_JAPANESE
    beq .Lnot_chinese
    cmp r2, #TEXT_MODE_MUZAIPIXEL_JAPANESE
    beq .Lnot_chinese

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
    ldrb r2, [r6, #TEXT_MODE_OFFSET]
    cmp r2, #TEXT_MODE_MUZAIPIXEL
    bne .Lload_selected_font
    movs r1, #0xFF
.Lload_selected_font:
    bl DecompressChineseGlyph
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_COPY
    bx r0

.Lnot_chinese:
    ldrb r1, [r6, #TEXT_MODE_OFFSET]
    cmp r1, #TEXT_MODE_MUZAIPIXEL
    bne .Lrender_original_glyph
    cmp r3, #0xF0
    bhs .Lrender_original_glyph
    movs r2, #0x7F
    lsls r2, r2, #8
    orrs r3, r2
    b .Lload_glyph
.Lrender_original_glyph:
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_NORMAL
    bx r0

.Lcompact_species_entry:
    push {r2-r7, lr}
.Lrender_compact_species:
    ldrb r2, [r6, #TEXT_SPECIES_ID_LO_OFFSET]
    ldrb r3, [r6, #TEXT_SPECIES_ID_HI_OFFSET]
    lsls r3, r3, #8
    orrs r2, r3
    lsls r2, r2, #2
    ldr r5, =ChsSpeciesNames
    ldr r5, [r5, r2]
    ldrb r2, [r6, #TEXT_SPECIES_CHAR_OFFSET]
    adds r5, r5, r2
    ldrb r3, [r5]
    cmp r3, #0xFF
    beq .Lcompact_species_done
    ldrb r2, [r5, #1]
    ldrb r5, [r6, #TEXT_SPECIES_CHAR_OFFSET]
    adds r5, #2
    strb r5, [r6, #TEXT_SPECIES_CHAR_OFFSET]
    cmp r3, #0x7F
    beq .Lcompact_species_punctuation
    subs r3, #0x5F
    lsls r3, r3, #8
    orrs r3, r2
    b .Lload_glyph
.Lcompact_species_punctuation:
    lsls r3, r3, #8
    orrs r3, r2
    b .Lload_glyph
.Lcompact_species_done:
    movs r2, #TEXT_MODE_JAPANESE
    strb r2, [r6, #TEXT_MODE_OFFSET]
    pop {r2-r7}
    pop {r1}
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0

.ltorg

.align 2
.global SetJapaneseTextMode
.type SetJapaneseTextMode, %function
.thumb_func
SetJapaneseTextMode:
    ldrb r0, [r6, #TEXT_MODE_OFFSET]
    cmp r0, #TEXT_MODE_MUZAIPIXEL
    beq .Lmuzaipixel_japanese
    cmp r0, #TEXT_MODE_MUZAIPIXEL_JAPANESE
    beq .Lmuzaipixel_japanese
    movs r0, #TEXT_MODE_JAPANESE
    strb r0, [r6, #TEXT_MODE_OFFSET]
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0
.Lmuzaipixel_japanese:
    movs r0, #TEXT_MODE_MUZAIPIXEL_JAPANESE
    strb r0, [r6, #TEXT_MODE_OFFSET]
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0

.align 2
.global SetChineseTextMode
.type SetChineseTextMode, %function
.thumb_func
SetChineseTextMode:
    ldrb r0, [r6, #TEXT_MODE_OFFSET]
    cmp r0, #TEXT_MODE_MUZAIPIXEL
    beq .Lmuzaipixel_chinese
    cmp r0, #TEXT_MODE_MUZAIPIXEL_JAPANESE
    beq .Lmuzaipixel_chinese
    movs r0, #TEXT_MODE_CHINESE
    strb r0, [r6, #TEXT_MODE_OFFSET]
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0
.Lmuzaipixel_chinese:
    movs r0, #TEXT_MODE_MUZAIPIXEL
    strb r0, [r6, #TEXT_MODE_OFFSET]
    ldr r0, =JP_RENDER_TEXT_REPEAT
    bx r0

.align 2
.global ChsNamingScreenSpeciesTitle
.type ChsNamingScreenSpeciesTitle, %function
.thumb_func
ChsNamingScreenSpeciesTitle:
    push {r4, r5, lr}
    sub sp, #0x2C
    ldr r5, =0x02039C34
    ldr r0, [r5]
    ldr r1, =0x00001E34
    adds r0, r0, r1
    ldrh r0, [r0]
    lsls r0, r0, #2
    ldr r1, =ChsSpeciesNames
    ldr r1, [r1, r0]
    add r4, sp, #0x0C
.Lnaming_copy_species:
    ldrb r2, [r1]
    cmp r2, #0xFF
    beq .Lnaming_append_suffix
    strb r2, [r4]
    adds r1, #1
    adds r4, #1
    b .Lnaming_copy_species
.Lnaming_append_suffix:
    movs r2, #0xFC
    strb r2, [r4]
    movs r2, #0x15
    strb r2, [r4, #1]
    adds r4, #2
    ldr r0, [r5]
    ldr r1, =0x00001E28
    adds r0, r0, r1
    ldr r1, [r0, #8]
    adds r0, r4, #0
    movs r2, #0x0F
    ldr r3, =0x080088F1
    bl .Lnaming_call_r3
    ldr r0, [r5]
    ldr r4, =0x00001E14
    adds r0, r0, r4
    ldrb r0, [r0]
    movs r1, #0x11
    ldr r3, =0x08003B19
    bl .Lnaming_call_r3
    ldr r0, [r5]
    adds r0, r0, r4
    ldrb r0, [r0]
    movs r1, #1
    str r1, [sp]
    movs r1, #0
    str r1, [sp, #4]
    str r1, [sp, #8]
    movs r1, #1
    add r2, sp, #0x0C
    movs r3, #9
    ldr r4, =JP_ADD_TEXT_PRINTER
    bl .Lnaming_call_r4
    ldr r0, [r5]
    ldr r1, =0x00001E14
    adds r0, r0, r1
    ldrb r0, [r0]
    ldr r3, =0x0800365D
    bl .Lnaming_call_r3
    add sp, #0x2C
    pop {r4, r5}
    pop {r0}
    bx r0
.Lnaming_call_r3:
    bx r3
.Lnaming_call_r4:
    bx r4

.ltorg

.align 2
.global ChsCopyMonNickname
.type ChsCopyMonNickname, %function
.thumb_func
ChsCopyMonNickname:
    push {r4-r6, lr}
    sub sp, #0x0C
    adds r4, r0, #0
    adds r5, r1, #0
    movs r1, #2
    mov r2, sp
    ldr r3, =0x0806A059
    bl .Lnick_call_r3
    mov r0, sp
    ldr r3, =0x0800885D
    bl .Lnick_call_r3
    adds r0, r4, #0
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A059
    bl .Lnick_call_r3
    lsls r6, r0, #0x10
    lsrs r6, r6, #0x10
    ldr r1, =(412)
    cmp r6, r1
    bhs .Lnick_copy_original
    lsls r0, r6, #1
    adds r0, r0, r6
    lsls r0, r0, #1
    ldr r1, =JP_SPECIES_NAMES
    adds r1, r1, r0
    mov r0, sp
    ldr r3, =0x0800895D
    bl .Lnick_call_r3
    cmp r0, #0
    bne .Lnick_copy_original
    movs r0, #0xF5
    strb r0, [r5]
    movs r0, #0xF2
    strb r0, [r5, #1]
    strb r6, [r5, #2]
    lsrs r0, r6, #8
    strb r0, [r5, #3]
    movs r0, #0xFF
    strb r0, [r5, #4]
    adds r0, r5, #4
    b .Lnick_done
.Lnick_copy_original:
    adds r0, r5, #0
    mov r1, sp
    ldr r3, =0x080088B9
    bl .Lnick_call_r3
.Lnick_done:
    add sp, #0x0C
    pop {r4-r6}
    pop {r1}
    bx r1
.Lnick_call_r3:
    bx r3

.align 2
.global ChsCopyBoxMonNickname
.type ChsCopyBoxMonNickname, %function
.thumb_func
ChsCopyBoxMonNickname:
    push {r4-r6, lr}
    sub sp, #0x0C
    adds r4, r0, #0
    adds r5, r1, #0
    movs r1, #2
    mov r2, sp
    ldr r3, =0x0806A1B5
    bl .Lbox_nick_call_r3
    mov r0, sp
    ldr r3, =0x0800885D
    bl .Lbox_nick_call_r3
    adds r0, r4, #0
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A1B5
    bl .Lbox_nick_call_r3
    lsls r6, r0, #0x10
    lsrs r6, r6, #0x10
    ldr r1, =(412)
    cmp r6, r1
    bhs .Lbox_nick_copy_original
    lsls r0, r6, #1
    adds r0, r0, r6
    lsls r0, r0, #1
    ldr r1, =JP_SPECIES_NAMES
    adds r1, r1, r0
    mov r0, sp
    ldr r3, =0x0800895D
    bl .Lbox_nick_call_r3
    cmp r0, #0
    bne .Lbox_nick_copy_original
    movs r0, #0xF5
    strb r0, [r5]
    movs r0, #0xF2
    strb r0, [r5, #1]
    strb r6, [r5, #2]
    lsrs r0, r6, #8
    strb r0, [r5, #3]
    movs r0, #0xFF
    strb r0, [r5, #4]
    adds r0, r5, #4
    b .Lbox_nick_done
.Lbox_nick_copy_original:
    adds r0, r5, #0
    mov r1, sp
    ldr r3, =0x080088B9
    bl .Lbox_nick_call_r3
.Lbox_nick_done:
    add sp, #0x0C
    pop {r4-r6}
    pop {r1}
    bx r1
.Lbox_nick_call_r3:
    bx r3

.align 2
.global ChsGetBoxMonNickname
.type ChsGetBoxMonNickname, %function
.thumb_func
ChsGetBoxMonNickname:
    b ChsTradeNicknameNearRouter
    nop

.align 2
.global ChsGetMonNicknameFromBox
.type ChsGetMonNicknameFromBox, %function
.thumb_func
ChsGetMonNicknameFromBox:
    ldr r3, .Lbox_nickname_router_target
    bx r3
    .space 24
.Lbox_nickname_router_target:
    .word ChsBoxNicknameDisplayRouter + 1

.align 2
.global ChsGetBoxMonNickAt
.type ChsGetBoxMonNickAt, %function
.thumb_func
ChsGetBoxMonNickAt:
    push {r4, r5, lr}
    adds r5, r2, #0
    lsls r0, r0, #0x18
    lsrs r3, r0, #0x18
    lsls r1, r1, #0x18
    lsrs r4, r1, #0x18
    cmp r3, #0x0D
    bhi .Lbox_nick_at_invalid
    cmp r4, #0x1D
    bhi .Lbox_nick_at_invalid
    ldr r2, =0x03005AF4
    lsls r0, r3, #2
    adds r0, r0, r3
    lsls r1, r0, #4
    subs r1, r1, r0
    lsls r1, r1, #5
    adds r1, #4
    ldr r0, [r2]
    adds r0, r0, r1
    lsls r1, r4, #2
    adds r1, r1, r4
    lsls r1, r1, #4
    adds r0, r0, r1
    adds r1, r5, #0
    bl ChsCopyBoxMonNickname
    b .Lbox_nick_at_done
.Lbox_nick_at_invalid:
    movs r0, #0xFF
    strb r0, [r5]
.Lbox_nick_at_done:
    pop {r4, r5}
    pop {r0}
    bx r0

.align 2
.global ChsGetMonNickname
.type ChsGetMonNickname, %function
.thumb_func
ChsGetMonNickname:
    ldr r3, .Lnickname_router_target
    bx r3
ChsTradeNicknameNearRouter:
    ldr r3, .Ltrade_router_target
    bx r3
    .space 80
.Lnickname_router_target:
    .word ChsNicknameDisplayRouter + 1
.Ltrade_router_target:
    .word ChsTradeNicknameRouter + 1

.align 2
.global ChsFaintFromFieldPoison
.type ChsFaintFromFieldPoison, %function
.thumb_func
ChsFaintFromFieldPoison:
    push {r4, r5, lr}
    sub sp, #4
    lsls r0, r0, #0x18
    lsrs r0, r0, #0x18
    movs r1, #0x64
    adds r4, r0, #0
    muls r4, r1, r4
    ldr r0, =0x02024190
    adds r4, r4, r0
    movs r0, #0
    str r0, [sp]
    adds r0, r4, #0
    movs r1, #7
    ldr r3, =0x0806D3CD
    bl .Lpoison_call_r3
    adds r0, r4, #0
    movs r1, #0x37
    mov r2, sp
    ldr r3, =0x0806A775
    bl .Lpoison_call_r3
    adds r0, r4, #0
    ldr r1, =0x02021C40
    bl ChsCopyFieldPoisonNickname
    add sp, #4
    pop {r4, r5}
    pop {r0}
    bx r0
.Lpoison_call_r3:
    bx r3

.align 2
.global ChsScrCmdBufferPartyMonNick
.type ChsScrCmdBufferPartyMonNick, %function
.thumb_func
ChsScrCmdBufferPartyMonNick:
    push {r4, r5, lr}
    ldr r1, [r0, #8]
    ldrb r4, [r1]
    adds r1, #1
    str r1, [r0, #8]
    ldr r3, =0x0809A81D
    bl .Lscript_nick_call_r3
    lsls r0, r0, #0x10
    lsrs r0, r0, #0x10
    ldr r3, =0x0806E569
    bl .Lscript_nick_call_r3
    lsls r0, r0, #0x10
    lsrs r0, r0, #0x10
    movs r1, #0x64
    muls r0, r1, r0
    ldr r1, =0x02024190
    adds r5, r0, r1
    ldr r1, =0x084E8918
    lsls r4, r4, #2
    adds r4, r4, r1
    ldr r1, [r4]
    adds r0, r5, #0
    bl ChsCopyMonNickname
    movs r0, #0
    pop {r4, r5}
    pop {r1}
    bx r1
.Lscript_nick_call_r3:
    bx r3

.align 2
.global ChsUpdateNickInHealthbox
.type ChsUpdateNickInHealthbox, %function
.thumb_func
ChsUpdateNickInHealthbox:
    push {r4-r7, lr}
    sub sp, #0x18
    lsls r0, r0, #0x18
    lsrs r4, r0, #0x18
    adds r5, r1, #0
    ldr r0, =0x02022AE0
    ldr r1, =0x085CC4EA
    ldr r3, =0x080088B9
    bl .Lhealthbox_call_r3
    adds r0, r5, #0
    mov r1, sp
    bl ChsCopyMonNickname
    ldr r0, =0x02022AE0
    mov r1, sp
    ldr r3, =0x080088D9
    bl .Lhealthbox_call_r3
    adds r6, r0, #0
    adds r0, r5, #0
    ldr r3, =JP_GET_MON_GENDER
    bl .Lhealthbox_call_r3
    lsls r7, r0, #0x18
    lsrs r7, r7, #0x18
    adds r0, r5, #0
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A059
    bl .Lhealthbox_call_r3
    cmp r0, #0x1D
    beq .Lhealthbox_nidoran
    cmp r0, #0x20
    bne .Lhealthbox_gender
.Lhealthbox_nidoran:
    mov r0, sp
    ldrb r0, [r0]
    cmp r0, #0xF5
    bne .Lhealthbox_gender
    movs r7, #100
.Lhealthbox_gender:
    cmp r7, #0
    beq .Lhealthbox_male
    cmp r7, #0xFE
    beq .Lhealthbox_female
    ldr r1, =0x085CC4FA
    b .Lhealthbox_append_gender
.Lhealthbox_male:
    ldr r1, =0x085CC4F0
    b .Lhealthbox_append_gender
.Lhealthbox_female:
    ldr r1, =0x085CC4F5
.Lhealthbox_append_gender:
    adds r0, r6, #0
    ldr r3, =0x080088B9
    bl .Lhealthbox_call_r3
    ldr r0, =.Lhealthbox_window_template
    ldr r3, =JP_ADD_WINDOW
    bl .Lhealthbox_call_r3
    lsls r6, r0, #0x18
    lsrs r6, r6, #0x18
    adds r0, r6, #0
    movs r1, #0x22
    ldr r3, =JP_FILL_WINDOW_PIXEL_BUFFER
    bl .Lhealthbox_call_r3
    add r1, sp, #0x14
    movs r0, #2
    strb r0, [r1]
    movs r0, #1
    strb r0, [r1, #1]
    movs r0, #3
    strb r0, [r1, #2]
    movs r0, #0
    str r0, [sp]
    str r0, [sp, #4]
    str r1, [sp, #8]
    mvns r0, r0
    str r0, [sp, #0xC]
    ldr r0, =0x02022AE0
    str r0, [sp, #0x10]
    adds r0, r6, #0
    movs r1, #1
    movs r2, #0
    ldr r3, =JP_ADD_TEXT_PRINTER_PARAM4
    mov r12, r3
    movs r3, #3
    bl .Lhealthbox_call_r12
    adds r0, r6, #0
    movs r1, #7
    ldr r3, =JP_GET_WINDOW_ATTRIBUTE
    bl .Lhealthbox_call_r3
    adds r5, r0, #0
    ldr r0, =0x020205AC
    lsls r1, r4, #4
    adds r1, r1, r4
    lsls r1, r1, #2
    adds r1, r1, r0
    ldrh r0, [r1, #4]
    lsls r0, r0, #0x16
    lsrs r7, r0, #0x11
    ldrh r0, [r1, #0x3A]
    lsls r0, r0, #0x18
    lsrs r0, r0, #0x18
    ldr r3, =JP_GET_BATTLER_SIDE
    bl .Lhealthbox_call_r3
    cmp r0, #0
    bne .Lhealthbox_enemy
    ldr r0, =0x06010040
    adds r0, r0, r7
    adds r1, r5, #0
    movs r2, #6
    bl ChsTextIntoHealthboxObject
    ldr r3, =JP_IS_DOUBLE_BATTLE
    bl .Lhealthbox_call_r3
    cmp r0, #0
    bne .Lhealthbox_player_double
    ldr r0, =0x06010800
    b .Lhealthbox_player_copy_tail
.Lhealthbox_player_double:
    ldr r0, =0x06010400
.Lhealthbox_player_copy_tail:
    adds r0, r0, r7
    adds r1, r5, #0
    adds r1, #0xC0
    movs r2, #1
    bl ChsTextIntoHealthboxObject
    b .Lhealthbox_remove_window
.Lhealthbox_enemy:
    ldr r0, =0x06010020
    adds r0, r0, r7
    adds r1, r5, #0
    movs r2, #7
    bl ChsTextIntoHealthboxObject
.Lhealthbox_remove_window:
    adds r0, r6, #0
    ldr r3, =JP_REMOVE_WINDOW
    bl .Lhealthbox_call_r3
    add sp, #0x18
    pop {r4-r7}
    pop {r0}
    bx r0
.Lhealthbox_call_r3:
    bx r3
.Lhealthbox_call_r12:
    bx r12

.align 2
.type ChsTextIntoHealthboxObject, %function
.thumb_func
ChsTextIntoHealthboxObject:
    push {r4-r6, lr}
    adds r4, r0, #0
    adds r5, r1, #0
    adds r6, r2, #0
    movs r0, #0x80
    lsls r0, r0, #1
    adds r0, r5, r0
    movs r1, #0x80
    lsls r1, r1, #1
    adds r1, r4, r1
    lsls r2, r6, #3
    ldr r3, =0x04000000
    orrs r2, r3
    ldr r3, =JP_CPU_SET
    bl .Lhealthbox_copy_call_r3
    cmp r6, #0
    beq .Lhealthbox_copy_done
.Lhealthbox_copy_column:
    adds r0, r5, #0
    adds r0, #0x14
    adds r1, r4, #0
    adds r1, #0x14
    ldr r2, =0x04000003
    ldr r3, =JP_CPU_SET
    bl .Lhealthbox_copy_call_r3
    adds r4, #0x20
    adds r5, #0x20
    subs r6, #1
    bne .Lhealthbox_copy_column
.Lhealthbox_copy_done:
    pop {r4-r6}
    pop {r0}
    bx r0
.Lhealthbox_copy_call_r3:
    bx r3

.align 2
.Lhealthbox_window_template:
    .byte 0, 0, 0, 8, 2, 0
    .hword 0

.ltorg

.align 2
.global ChsPokedexListName
.type ChsPokedexListName, %function
.thumb_func
ChsPokedexListName:
    push {r4-r7, lr}
    mov r7, r8
    push {r7}
    sub sp, #0x10
    lsls r0, r0, #0x10
    lsrs r5, r0, #0x10
    lsls r1, r1, #0x18
    lsrs r1, r1, #0x18
    mov r8, r1
    lsls r2, r2, #0x18
    lsrs r7, r2, #0x18
    adds r0, r5, #0
    ldr r3, =JP_NATIONAL_DEX_TO_SPECIES
    bl .Lpokedex_list_species_call
    cmp r0, #0
    beq .Lpokedex_list_unknown
    mov r2, sp
    adds r2, #4
    movs r3, #0xF5
    strb r3, [r2]
    movs r3, #0xF2
    strb r3, [r2, #1]
    strb r0, [r2, #2]
    lsrs r3, r0, #8
    strb r3, [r2, #3]
    movs r3, #0xFF
    strb r3, [r2, #4]
    movs r4, #4
    b .Lpokedex_list_print
.Lpokedex_list_unknown:
    movs r4, #0
    mov r2, sp
    adds r2, #4
    movs r3, #0xAE
.Lpokedex_list_blank:
    strb r3, [r2, r4]
    adds r4, #1
    cmp r4, #5
    blo .Lpokedex_list_blank
    movs r3, #0xFF
    strb r3, [r2, #5]
    movs r4, #0
.Lpokedex_list_print:
    str r7, [sp]
    movs r0, #0
    movs r1, #1
    add r2, sp, #4
    mov r3, r8
    ldr r5, =ChsPokedexPrintMonDexNumAndName + 1
    bl .Lpokedex_list_print_call
    adds r0, r4, #0
    add sp, #0x10
    pop {r3}
    mov r8, r3
    pop {r4-r7}
    pop {r1}
    bx r1
.Lpokedex_list_species_call:
    bx r3
.Lpokedex_list_print_call:
    bx r5

.align 2
.type ChsPokedexPrintMonDexNumAndName, %function
.thumb_func
ChsPokedexPrintMonDexNumAndName:
    push {r4, r5, r6, lr}
    mov r6, r8
    push {r6}
    sub sp, #0x18
    mov r8, r3
    ldr r3, [sp, #0x2C]
    lsls r0, r0, #0x18
    lsrs r0, r0, #0x18
    lsls r1, r1, #0x18
    lsrs r1, r1, #0x18
    lsls r3, r3, #0x18
    add r4, sp, #0x14
    movs r6, #0
    strb r6, [r4]
    adds r5, r4, #0
    movs r4, #0x0F
    strb r4, [r5, #1]
    movs r4, #3
    strb r4, [r5, #2]
    mov r4, r8
    lsls r4, r4, #0x1B
    lsrs r4, r4, #0x18
    subs r4, #6
    mov r8, r4
    lsrs r3, r3, #0x15
    adds r3, #2
    lsls r3, r3, #0x18
    lsrs r3, r3, #0x18
    str r6, [sp]
    str r6, [sp, #4]
    str r5, [sp, #8]
    movs r4, #1
    rsbs r4, r4, #0
    str r4, [sp, #0xC]
    str r2, [sp, #0x10]
    mov r2, r8
    ldr r4, =JP_ADD_TEXT_PRINTER_4
    bl .Lpokedex_list_add_text
    add sp, #0x18
    pop {r3}
    mov r8, r3
    pop {r4, r5, r6}
    pop {r0}
    bx r0
.Lpokedex_list_add_text:
    bx r4

.align 2
.global ChsPokedexName
.type ChsPokedexName, %function
.thumb_func
ChsPokedexName:
    push {r4-r7, lr}
    mov r4, r8
    mov r5, sb
    push {r4, r5}
    sub sp, #0xC
    adds r4, r0, #0
    adds r5, r1, #0
    adds r6, r2, #0
    adds r7, r3, #0
    adds r0, r5, #0
    ldr r3, =JP_NATIONAL_DEX_TO_SPECIES
    bl .Lpokedex_name_species_call
    cmp r0, #0
    beq .Lpokedex_name_unknown
    mov r1, sp
    movs r2, #0xF5
    strb r2, [r1]
    movs r2, #0xF2
    strb r2, [r1, #1]
    strb r0, [r1, #2]
    lsrs r2, r0, #8
    strb r2, [r1, #3]
    movs r2, #0xFF
    strb r2, [r1, #4]
    lsls r0, r0, #2
    ldr r1, =ChsSpeciesNames
    ldr r0, [r1, r0]
    adds r0, #1
    movs r5, #0
.Lpokedex_name_length:
    ldrb r1, [r0]
    cmp r1, #0xFF
    beq .Lpokedex_name_print
    adds r0, #2
    adds r5, #1
    b .Lpokedex_name_length
.Lpokedex_name_unknown:
    movs r5, #0
    mov r1, sp
    movs r2, #0xAE
.Lpokedex_name_dashes:
    strb r2, [r1, r5]
    adds r5, #1
    cmp r5, #5
    blo .Lpokedex_name_dashes
    movs r2, #0xFF
    strb r2, [r1, #5]
.Lpokedex_name_print:
    ldr r0, =JP_POKEDEX_PRINT_TEXT
    mov ip, r0
    adds r0, r4, #0
    mov r1, sp
    adds r2, r6, #0
    adds r3, r7, #0
    bl .Lpokedex_name_print_call
    adds r0, r5, #0
    add sp, #0xC
    pop {r3, r4}
    mov r8, r3
    mov sb, r4
    pop {r4-r7}
    pop {r1}
    bx r1
.Lpokedex_name_species_call:
    bx r3
.Lpokedex_name_print_call:
    bx ip

.align 2
.global ChsSummaryPrintGenderSymbol
.type ChsSummaryPrintGenderSymbol, %function
.thumb_func
ChsSummaryPrintGenderSymbol:
    push {r4, r5, lr}
    sub sp, #8
    adds r4, r0, #0
    lsls r5, r1, #0x10
    lsrs r5, r5, #0x10
    cmp r5, #0x20
    beq .Lsummary_gender_done
    cmp r5, #0x1D
    beq .Lsummary_gender_done
    adds r0, r4, #0
    ldr r3, =JP_GET_MON_GENDER
    bl .Lsummary_gender_call
    lsls r0, r0, #0x18
    lsrs r0, r0, #0x18
    cmp r0, #0
    beq .Lsummary_gender_male
    cmp r0, #0xFE
    bne .Lsummary_gender_done
    ldr r1, =0x085C940C
    movs r3, #4
    b .Lsummary_gender_print
.Lsummary_gender_male:
    ldr r1, =0x085C940A
    movs r3, #3
.Lsummary_gender_print:
    movs r0, #0
    str r0, [sp]
    str r3, [sp, #4]
    movs r2, #54
    movs r0, #0x13
    movs r3, #1
    ldr r4, =JP_SUMMARY_PRINT_TEXT
    bl .Lsummary_gender_print_call
.Lsummary_gender_done:
    add sp, #8
    pop {r4, r5}
    pop {r0}
    bx r0
.Lsummary_gender_call:
    bx r3
.Lsummary_gender_print_call:
    bx r4

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
    push {r0-r3}
    mov r0, lr
    ldr r1, =.Lbattle_nickname_callers
    movs r2, #28
.Lbattle_nickname_caller_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lbattle_nickname_caller_found
    adds r1, #4
    subs r2, #1
    bne .Lbattle_nickname_caller_loop
    pop {r0-r3}
    b .Lbattle_exp_name_original_entry
.Lbattle_nickname_caller_found:
    pop {r0-r3}
    adds r1, r2, #0
    b ChsCopyMonNickname
.Lbattle_exp_name_original_entry:
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

.align 2
.Lbattle_nickname_callers:
    .word 0x0814E965, 0x0814E999, 0x0814E9CD, 0x0814EA01
    .word 0x0814EA39, 0x0814EA79, 0x0814EAB9, 0x0814EAF9
    .word 0x0814EB81, 0x0814EBB7, 0x0814EC03, 0x0814EC3D
    .word 0x0814ECA7, 0x0814ECDB, 0x0814ED43, 0x0814ED77
    .word 0x0814EDDF, 0x0814EE13, 0x0814EE7B, 0x0814EEAF
    .word 0x0814EF17, 0x0814EF4B, 0x0814F3A7, 0x0814F3D9
    .word 0x0814F77F, 0x0814F7C1, 0x0814F81F, 0x0814F837

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
.type ChsTradeNicknameRouter, %function
.thumb_func
ChsTradeNicknameRouter:
    push {r0-r3}
    mov r0, lr
    ldr r1, =.Lparty_nickname_storage_callers
    movs r2, #2
.Lparty_nickname_storage_caller_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lparty_nickname_storage_found
    adds r1, #4
    subs r2, #1
    bne .Lparty_nickname_storage_caller_loop
    ldr r1, =.Ltrade_nickname_data_callers
    movs r2, #8
.Ltrade_nickname_caller_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Ltrade_nickname_caller_found
    adds r1, #4
    subs r2, #1
    bne .Ltrade_nickname_caller_loop
    pop {r0-r3}
    b .Lnickname_tail_copy_mon
.Ltrade_nickname_caller_found:
    pop {r0-r3}
    adds r1, r2, #0
    b .Lnickname_tail_copy_mon
.Lparty_nickname_storage_found:
    pop {r0-r3}
    b ChsCopyMonNicknameOriginal

.ltorg

.align 2
.type ChsBoxNicknameDisplayRouter, %function
.thumb_func
ChsBoxNicknameDisplayRouter:
    push {r0-r3}
    mov r0, lr
    ldr r1, =.Lbox_nickname_storage_caller
    ldr r1, [r1]
    cmp r0, r1
    beq .Lbox_nickname_storage_found
    ldr r1, =.Lbox_nickname_data_callers
    movs r2, #4
.Lbox_nickname_data_caller_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lbox_nickname_data_caller_found
    adds r1, #4
    subs r2, #1
    bne .Lbox_nickname_data_caller_loop
    pop {r0-r3}
    b .Lnickname_tail_copy_box
.Lbox_nickname_data_caller_found:
    pop {r0-r3}
    adds r1, r2, #0
    b .Lnickname_tail_copy_box
.Lbox_nickname_storage_found:
    pop {r0-r3}
    b ChsCopyBoxMonNicknameOriginal
.Lnickname_tail_copy_box:
    ldr r3, =ChsCopyBoxMonNickname + 1
    bx r3

.align 2
.type ChsNicknameDisplayRouter, %function
.thumb_func
ChsNicknameDisplayRouter:
    push {r0-r3}
    mov r0, lr
    ldr r1, =.Lnickname_tv_r4_species2_callers
    movs r2, #2
.Lnickname_tv_r4_species2_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lnickname_tv_r4_species2_found
    adds r1, #4
    subs r2, #1
    bne .Lnickname_tv_r4_species2_loop
    ldr r1, =.Lnickname_tv_r5_species2_callers
    movs r2, #3
.Lnickname_tv_r5_species2_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lnickname_tv_r5_species2_found
    adds r1, #4
    subs r2, #1
    bne .Lnickname_tv_r5_species2_loop
    ldr r1, =.Lnickname_tv_r5_species16_callers
    movs r2, #5
.Lnickname_tv_r5_species16_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lnickname_tv_r5_species16_found
    adds r1, #4
    subs r2, #1
    bne .Lnickname_tv_r5_species16_loop
    ldr r1, =.Lnickname_direct_data_callers
    movs r2, #1
.Lnickname_direct_data_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lnickname_direct_data_found
    adds r1, #4
    subs r2, #1
    bne .Lnickname_direct_data_loop
    ldr r1, =.Lnickname_partner_string_caller
    ldr r1, [r1]
    cmp r0, r1
    beq .Lnickname_partner_string_found
    ldr r1, =.Lnickname_condition_string_callers
    movs r2, #2
.Lnickname_condition_string_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lnickname_condition_string_found
    adds r1, #4
    subs r2, #1
    bne .Lnickname_condition_string_loop
    ldr r1, =.Lnickname_hof_width_callers
    movs r2, #2
.Lnickname_hof_width_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lnickname_hof_width_found
    adds r1, #4
    subs r2, #1
    bne .Lnickname_hof_width_loop
    ldr r1, =.Lmon_nickname_data_callers
    movs r2, #12
.Lnickname_original_caller_loop:
    ldr r3, [r1]
    cmp r0, r3
    beq .Lnickname_original_caller_found
    adds r1, #4
    subs r2, #1
    bne .Lnickname_original_caller_loop
    pop {r0-r3}
    b .Lnickname_tail_copy_mon
.Lnickname_original_caller_found:
    pop {r0-r3}
    adds r1, r2, #0
    b .Lnickname_tail_copy_mon
.Lnickname_tv_r4_species2_found:
    pop {r0-r3}
    ldrh r2, [r4, #2]
    b ChsCopyStoredNicknameForSpecies
.Lnickname_tv_r5_species2_found:
    pop {r0-r3}
    ldrh r2, [r5, #2]
    b ChsCopyStoredNicknameForSpecies
.Lnickname_tv_r5_species16_found:
    pop {r0-r3}
    ldrh r2, [r5, #0x10]
    b ChsCopyStoredNicknameForSpecies
.Lnickname_direct_data_found:
    pop {r0-r3}
    adds r1, r2, #0
    b .Lnickname_tail_copy_mon
.Lnickname_partner_string_found:
    pop {r0-r3}
    bl ChsTruncateNickname
    ldrh r0, [r7]
    adds r1, r4, #0
    b ChsConvertNicknameForSpecies
.Lnickname_condition_string_found:
    pop {r0-r3}
    bl ChsTruncateNickname
    adds r0, r4, #0
    adds r1, r6, #0
    bl ChsResolveBoxOrPartyMon
    adds r4, r0, #0
    cmp r2, #0
    beq .Lnickname_condition_party
    adds r0, r4, #0
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A1B5
    bl .Lnickname_router_call_r3
    b .Lnickname_condition_convert
.Lnickname_condition_party:
    adds r0, r4, #0
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A059
    bl .Lnickname_router_call_r3
.Lnickname_condition_convert:
    adds r1, r5, #0
    b ChsConvertNicknameForSpecies
.Lnickname_hof_width_found:
    pop {r0-r3}
    push {r0-r2}
    ldrh r0, [r7, #8]
    movs r3, #0x80
    lsls r3, r3, #2
    subs r3, #1
    ands r0, r3
    bl ChsConvertNicknameForSpecies
    pop {r0-r2}
    ldr r3, =0x08005DAD
    bx r3
.Lnickname_router_call_r3:
    bx r3
.Lnickname_tail_copy_mon:
    ldr r3, =ChsCopyMonNickname + 1
    bx r3

.align 2
.type ChsTruncateNickname, %function
.thumb_func
ChsTruncateNickname:
    movs r1, #0
.Ltruncate_nickname_loop:
    ldrb r2, [r0, r1]
    cmp r2, #0xFF
    beq .Ltruncate_nickname_done
    adds r1, #1
    cmp r1, #5
    blo .Ltruncate_nickname_loop
    movs r2, #0xFF
    strb r2, [r0, #5]
.Ltruncate_nickname_done:
    bx lr

.align 2
.type ChsResolveBoxOrPartyMon, %function
.thumb_func
ChsResolveBoxOrPartyMon:
    cmp r0, #14
    bne .Lresolve_box_mon
    movs r2, #0x64
    muls r1, r2, r1
    ldr r0, =0x02024190
    adds r0, r0, r1
    movs r2, #0
    bx lr
.Lresolve_box_mon:
    ldr r3, =0x080D1935
    push {lr}
    bl .Lresolve_box_call_r3
    movs r2, #1
    pop {r1}
    bx r1
.Lresolve_box_call_r3:
    bx r3

.align 2
.Lbox_nickname_data_callers:
    .word 0x080CE60B, 0x081CFA6B, 0x081CFE03, 0x081775F5
.Lparty_nickname_storage_callers:
    .word 0x0806F5E3, 0x08071765
.Lbox_nickname_storage_caller:
    .word 0x08070FBB
.Lmon_nickname_data_callers:
    .word 0x0813DC73, 0x0813E301, 0x0813EB3D, 0x0813F683
    .word 0x08161217, 0x080CE513, 0x081CFA39, 0x081CFDC9
    .word 0x081CEFDF, 0x081CF00F, 0x08166B77, 0x081775A7
.Ltrade_nickname_data_callers:
    .word 0x0807813D, 0x08078165, 0x080794A9, 0x080796DB
    .word 0x0807B55F, 0x0807B577, 0x0807B5D5, 0x0807E1EB
.Lnickname_direct_data_callers:
    .word 0x080F0A51
.Lnickname_partner_string_caller:
    .word 0x081B0A25
.Lnickname_condition_string_callers:
    .word 0x081CCDE3, 0x081D2347
.Lnickname_hof_width_callers:
    .word 0x0817499B, 0x081749DD
.Lnickname_tv_r4_species2_callers:
    .word 0x080F1FB9, 0x080F30EF
.Lnickname_tv_r5_species2_callers:
    .word 0x080F26DD, 0x080F2771, 0x080F28DD
.Lnickname_tv_r5_species16_callers:
    .word 0x080F299D, 0x080F2A31, 0x080F2AA5, 0x080F2AEB
    .word 0x080F2B1B
.align 2
.type ChsCopyStoredNicknameForSpecies, %function
.thumb_func
ChsCopyStoredNicknameForSpecies:
    push {r4-r6, lr}
    adds r4, r0, #0
    adds r5, r1, #0
    adds r6, r2, #0
    ldr r3, =0x08008829
    bl .Lcopy_stored_nickname_call_r3
    adds r0, r6, #0
    adds r1, r4, #0
    bl ChsConvertNicknameForSpecies
    adds r0, r4, #0
    pop {r4-r6}
    pop {r1}
    bx r1
.Lcopy_stored_nickname_call_r3:
    bx r3

.align 2
.type ChsCopyMonNicknameOriginal, %function
.thumb_func
ChsCopyMonNicknameOriginal:
    push {r4, lr}
    sub sp, #0x14
    adds r4, r1, #0
    movs r1, #2
    mov r2, sp
    ldr r3, =0x0806A059
    bl .Lcopy_original_nickname_call_r3
    adds r0, r4, #0
    mov r1, sp
    ldr r3, =0x08008829
    bl .Lcopy_original_nickname_call_r3
    add sp, #0x14
    pop {r4}
    pop {r1}
    bx r1

.align 2
.type ChsCopyBoxMonNicknameOriginal, %function
.thumb_func
ChsCopyBoxMonNicknameOriginal:
    push {r4, lr}
    sub sp, #0x14
    adds r4, r1, #0
    movs r1, #2
    mov r2, sp
    ldr r3, =0x0806A1B5
    bl .Lcopy_original_nickname_call_r3
    adds r0, r4, #0
    mov r1, sp
    ldr r3, =0x08008829
    bl .Lcopy_original_nickname_call_r3
    add sp, #0x14
    pop {r4}
    pop {r1}
    bx r1
.Lcopy_original_nickname_call_r3:
    bx r3

.align 2
.type ChsConvertNicknameForSpecies, %function
.thumb_func
ChsConvertNicknameForSpecies:
    push {r4-r6, lr}
    adds r4, r0, #0
    adds r5, r1, #0
    ldr r0, =(412)
    cmp r4, r0
    bhs .Lconvert_nickname_done
    lsls r0, r4, #1
    adds r0, r0, r4
    lsls r0, r0, #1
    ldr r6, =JP_SPECIES_NAMES
    adds r6, r6, r0
    movs r2, #0
.Lconvert_nickname_compare:
    ldrb r0, [r5, r2]
    ldrb r1, [r6, r2]
    cmp r0, r1
    bne .Lconvert_nickname_done
    cmp r0, #0xFF
    beq .Lconvert_nickname_write
    adds r2, #1
    cmp r2, #6
    blo .Lconvert_nickname_compare
    b .Lconvert_nickname_done
.Lconvert_nickname_write:
    movs r0, #0xF5
    strb r0, [r5]
    movs r0, #0xF2
    strb r0, [r5, #1]
    strb r4, [r5, #2]
    lsrs r0, r4, #8
    strb r0, [r5, #3]
    movs r0, #0xFF
    strb r0, [r5, #4]
.Lconvert_nickname_done:
    adds r0, r5, #0
    pop {r4-r6}
    pop {r1}
    bx r1

.align 2
.type ChsCopyFieldPoisonNickname, %function
.thumb_func
ChsCopyFieldPoisonNickname:
    push {r4-r6, lr}
    sub sp, #0x0C
    adds r4, r0, #0
    adds r5, r1, #0
    movs r1, #2
    mov r2, sp
    ldr r3, =0x0806A059
    bl .Lfield_nickname_call_r3
    mov r0, sp
    ldr r3, =0x0800885D
    bl .Lfield_nickname_call_r3
    adds r0, r5, #0
    mov r1, sp
    ldr r3, =0x080088B9
    bl .Lfield_nickname_call_r3
    adds r0, r4, #0
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A059
    bl .Lfield_nickname_call_r3
    adds r1, r5, #0
    bl ChsConvertNicknameForSpecies
    add sp, #0x0C
    pop {r4-r6}
    pop {r1}
    bx r1
.Lfield_nickname_call_r3:
    bx r3

.align 2
.global ChsCopyContestNicknameForDisplay
.type ChsCopyContestNicknameForDisplay, %function
.thumb_func
ChsCopyContestNicknameForDisplay:
    subs r3, r1, #2
    ldrh r2, [r3]
    b ChsCopyNicknameStringForSpecies

.align 2
.global ChsPrintContestantNicknameWithColor
.type ChsPrintContestantNicknameWithColor, %function
.thumb_func
ChsPrintContestantNicknameWithColor:
    push {r4, r5, lr}
    sub sp, #0x14
    lsls r0, r0, #0x18
    lsrs r4, r0, #0x18
    lsls r1, r1, #0x18
    lsrs r5, r1, #0x18
    lsls r1, r4, #6
    ldr r2, =0x02039AA2
    adds r1, r1, r2
    mov r0, sp
    bl ChsCopyContestNicknameForDisplay
    mov r0, sp
    adds r1, r5, #0
    ldr r3, =0x080DA665
    bl .Lcontest_nickname_call_r3
    ldr r0, =0x02039BC6
    adds r0, r4, r0
    ldrb r0, [r0]
    ldr r1, =0x02022AE0
    ldr r3, =0x080DE2D5
    bl .Lcontest_nickname_call_r3
    add sp, #0x14
    pop {r4, r5}
    pop {r1}
    bx r1

.align 2
.global ChsCopyContestWinnerNicknameForDisplay
.type ChsCopyContestWinnerNicknameForDisplay, %function
.thumb_func
ChsCopyContestWinnerNicknameForDisplay:
    subs r3, r1, #3
    ldrh r2, [r3]
    b ChsCopyNicknameStringForSpecies
.Lcontest_nickname_call_r3:
    bx r3

.align 2
.type ChsCopyNicknameStringForSpecies, %function
.thumb_func
ChsCopyNicknameStringForSpecies:
    push {r4-r6, lr}
    adds r4, r0, #0
    adds r5, r1, #0
    adds r6, r2, #0
    ldr r3, =0x080088B9
    bl .Lcontest_nickname_call_r3
    adds r0, r6, #0
    adds r1, r4, #0
    bl ChsConvertNicknameForSpecies
    adds r0, r4, #0
    pop {r4-r6}
    pop {r1}
    bx r1

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
    ldr r6, =0x0203CBE8
    ldr r6, [r6]
    adds r6, #0xA6
    cmp r1, r6
    bne .Lssp_ot_ready
    cmp r2, #4
    bne .Lssp_ot_ready
    push {r0-r3}
    bl ChsCopyOtSlashTail
    pop {r0-r3}
.Lssp_ot_ready:
    cmp r0, #0x12
    bne .Lssp_nickname_ready
    cmp r3, #2
    bne .Lssp_nickname_ready
    cmp r2, #0x18
    beq .Lssp_nickname_x_ready
    cmp r2, #0x20
    bne .Lssp_nickname_ready
.Lssp_nickname_x_ready:
    push {r0-r3}
    bl ChsPrepareSummaryNickname
    ldr r1, [sp, #4]
    ldr r2, [sp, #8]
    bl ChsSummaryNicknameX
    str r0, [sp, #8]
    pop {r0-r3}
.Lssp_nickname_ready:
    cmp r0, #0x13
    bne .Lssp_species_ready
    cmp r2, #4
    bne .Lssp_species_ready
    cmp r3, #1
    bne .Lssp_species_ready
    push {r0-r3}
    bl ChsSummarySpeciesNameX
    str r0, [sp, #8]
    pop {r0-r3}
.Lssp_species_ready:
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
.type ChsSummarySpeciesNameX, %function
.thumb_func
ChsSummarySpeciesNameX:
    push {r4-r7, lr}
    ldr r4, =0x0203CBE8
    ldr r4, [r4]
    adds r0, r4, #0
    adds r0, #0x70
    ldrh r5, [r0]
    ldr r0, =412
    cmp r5, r0
    bhs .Lsummary_species_x_zero
    lsls r0, r5, #2
    ldr r1, =ChsSpeciesNames
    ldr r1, [r1, r0]
    adds r1, #1
    movs r6, #0
    movs r7, #0
.Lsummary_species_width:
    ldrb r0, [r1]
    cmp r0, #0xFF
    beq .Lsummary_species_width_done
    cmp r0, #0x7F
    beq .Lsummary_species_width_pair
    cmp r0, #0x60
    blo .Lsummary_species_width_single
    cmp r0, #0x7D
    bhi .Lsummary_species_width_single
    cmp r0, #0x65
    beq .Lsummary_species_width_single
    cmp r0, #0x7A
    beq .Lsummary_species_width_single
.Lsummary_species_width_pair:
    adds r1, #2
    adds r6, #12
    b .Lsummary_species_width_next
.Lsummary_species_width_single:
    adds r1, #1
    adds r6, #8
.Lsummary_species_width_next:
    adds r7, #1
    b .Lsummary_species_width
.Lsummary_species_width_done:
    cmp r7, #4
    blo .Lsummary_species_check_gender
    lsls r6, r7, #3
.Lsummary_species_check_gender:
    movs r7, #62
    cmp r5, #0x20
    beq .Lsummary_species_align
    cmp r5, #0x1D
    beq .Lsummary_species_align
    adds r0, r4, #0
    adds r0, #0x0C
    ldr r3, =JP_GET_MON_GENDER
    bl .Lsummary_species_gender_call
    lsls r0, r0, #0x18
    lsrs r0, r0, #0x18
    cmp r0, #0
    beq .Lsummary_species_has_gender
    cmp r0, #0xFE
    bne .Lsummary_species_align
.Lsummary_species_has_gender:
    movs r7, #54
.Lsummary_species_align:
    cmp r6, r7
    bhi .Lsummary_species_x_zero
    subs r7, r7, r6
    adds r0, r7, #0
    b .Lsummary_species_x_done
.Lsummary_species_x_zero:
    movs r0, #0
.Lsummary_species_x_done:
    pop {r4-r7}
    pop {r1}
    bx r1
.Lsummary_species_gender_call:
    bx r3

.align 2
.type ChsSummaryNicknameX, %function
.thumb_func
ChsSummaryNicknameX:
    push {r4-r7, lr}
    adds r4, r1, #0
    adds r5, r2, #0
    ldrb r0, [r4]
    cmp r0, #0xF5
    bne .Lsummary_nickname_japanese_width
    ldrb r0, [r4, #1]
    cmp r0, #0xF2
    beq .Lsummary_nickname_species_width
    cmp r0, #0xF3
    beq .Lsummary_nickname_narrow_width
    b .Lsummary_nickname_japanese_width
.Lsummary_nickname_species_width:
    ldrb r0, [r4, #2]
    ldrb r1, [r4, #3]
    lsls r1, r1, #8
    orrs r0, r1
    ldr r1, =412
    cmp r0, r1
    bhs .Lsummary_nickname_x_original
    lsls r0, r0, #2
    ldr r1, =ChsSpeciesNames
    ldr r4, [r1, r0]
    adds r4, #1
    movs r7, #12
    b .Lsummary_nickname_measure
.Lsummary_nickname_narrow_width:
    adds r4, #2
    movs r7, #8
.Lsummary_nickname_measure:
    movs r6, #0
.Lsummary_nickname_measure_next:
    ldrb r0, [r4]
    cmp r0, #0xFF
    beq .Lsummary_nickname_x_from_width
    cmp r0, #0xF5
    beq .Lsummary_nickname_x_from_width
    cmp r0, #0x7F
    beq .Lsummary_nickname_measure_pair
    cmp r0, #0x60
    blo .Lsummary_nickname_measure_single
    cmp r0, #0x7D
    bhi .Lsummary_nickname_measure_single
    cmp r0, #0x65
    beq .Lsummary_nickname_measure_single
    cmp r0, #0x7A
    beq .Lsummary_nickname_measure_single
.Lsummary_nickname_measure_pair:
    adds r4, #2
    adds r6, r6, r7
    b .Lsummary_nickname_measure_next
.Lsummary_nickname_measure_single:
    adds r4, #1
    adds r6, #8
    b .Lsummary_nickname_measure_next
.Lsummary_nickname_japanese_width:
    movs r0, #1
    adds r1, r4, #0
    movs r2, #0
    subs r2, #1
    ldr r3, =JP_GET_STRING_WIDTH
    bl .Lsummary_nickname_width_call
    adds r6, r0, #0
    movs r7, #1
    b .Lsummary_nickname_x_from_width
.Lsummary_nickname_width_call:
    bx r3
.Lsummary_nickname_x_from_width:
    movs r0, #70
    cmp r6, r0
    bhs .Lsummary_nickname_x_original
    subs r0, r0, r6
    cmp r7, #1
    bne .Lsummary_nickname_x_done
    cmp r0, r5
    bhs .Lsummary_nickname_x_done
.Lsummary_nickname_x_original:
    adds r0, r5, #0
.Lsummary_nickname_x_done:
    pop {r4-r7}
    pop {r1}
    bx r1

.align 2
.type ChsPrepareSummaryNickname, %function
.thumb_func
ChsPrepareSummaryNickname:
    push {r4-r7, lr}
    adds r4, r1, #0
    ldrb r0, [r4]
    cmp r0, #0xF5
    bne .Lsummary_nickname_plain
    ldrb r0, [r4, #1]
    cmp r0, #0xF2
    bne .Lsummary_nickname_plain
    ldrb r0, [r4, #2]
    ldrb r1, [r4, #3]
    lsls r1, r1, #8
    orrs r0, r1
    ldr r1, =412
    cmp r0, r1
    bhs .Lsummary_nickname_done
    adds r1, r4, #0
    movs r2, #4
    bl ChsWriteNarrowSpeciesName
    b .Lsummary_nickname_done
.Lsummary_nickname_plain:
    adds r5, r4, #0
    movs r6, #0
    movs r7, #0
.Lsummary_nickname_plain_count:
    ldrb r0, [r5]
    cmp r0, #0xFF
    beq .Lsummary_nickname_plain_counted
    cmp r0, #0x60
    blo .Lsummary_nickname_done
    cmp r0, #0x7D
    bhi .Lsummary_nickname_done
    cmp r0, #0x65
    beq .Lsummary_nickname_done
    cmp r0, #0x7A
    beq .Lsummary_nickname_done
    ldrb r0, [r5, #1]
    cmp r0, #0xF6
    bhi .Lsummary_nickname_done
    adds r5, #2
    adds r6, #2
    adds r7, #1
    b .Lsummary_nickname_plain_count
.Lsummary_nickname_plain_counted:
    cmp r7, #4
    blo .Lsummary_nickname_done
    cmp r7, #5
    bhi .Lsummary_nickname_done
    adds r1, r6, #0
.Lsummary_nickname_shift:
    cmp r1, #0
    beq .Lsummary_nickname_shifted
    subs r1, #1
    ldrb r0, [r4, r1]
    adds r2, r1, #2
    strb r0, [r4, r2]
    b .Lsummary_nickname_shift
.Lsummary_nickname_shifted:
    movs r0, #0xF5
    strb r0, [r4]
    strb r0, [r5, #2]
    movs r0, #0xF3
    strb r0, [r4, #1]
    movs r0, #0xF4
    strb r0, [r5, #3]
    movs r0, #0xFF
    strb r0, [r5, #4]
.Lsummary_nickname_done:
    pop {r4-r7}
    pop {r0}
    bx r0

.align 2
.type ChsWriteNarrowSpeciesName, %function
.thumb_func
ChsWriteNarrowSpeciesName:
    push {r4-r7, lr}
    adds r4, r1, #0
    adds r7, r2, #0
    lsls r0, r0, #2
    ldr r1, =ChsSpeciesNames
    ldr r5, [r1, r0]
    adds r5, #1
    adds r6, r5, #0
    movs r2, #0
.Lsummary_species_count:
    ldrb r0, [r6]
    cmp r0, #0xFF
    beq .Lsummary_species_counted
    cmp r0, #0x7F
    beq .Lsummary_species_pair
    cmp r0, #0x60
    blo .Lsummary_species_single
    cmp r0, #0x7D
    bhi .Lsummary_species_single
    cmp r0, #0x65
    beq .Lsummary_species_single
    cmp r0, #0x7A
    beq .Lsummary_species_single
.Lsummary_species_pair:
    adds r6, #2
    b .Lsummary_species_next
.Lsummary_species_single:
    adds r6, #1
.Lsummary_species_next:
    adds r2, #1
    b .Lsummary_species_count
.Lsummary_species_counted:
    cmp r2, r7
    blo .Lsummary_species_skip
    movs r0, #0xF5
    strb r0, [r4]
    movs r0, #0xF3
    strb r0, [r4, #1]
    adds r4, #2
.Lsummary_species_copy:
    ldrb r0, [r5]
    cmp r0, #0xFF
    beq .Lsummary_species_copied
    strb r0, [r4]
    adds r4, #1
    adds r5, #1
    b .Lsummary_species_copy
.Lsummary_species_copied:
    movs r0, #0xF5
    strb r0, [r4]
    movs r0, #0xF4
    strb r0, [r4, #1]
    movs r0, #0xFF
    strb r0, [r4, #2]
    movs r0, #1
    b .Lsummary_species_done
.Lsummary_species_skip:
    movs r0, #0
.Lsummary_species_done:
    pop {r4-r7}
    pop {r1}
    bx r1

.align 2
.type ChsCopyOtSlashTail, %function
.thumb_func
ChsCopyOtSlashTail:
    push {r4, lr}
    adds r4, r0, #0
    movs r0, #7
    movs r1, #7
    ldr r3, =JP_GET_WINDOW_ATTRIBUTE
    bl .Lot_call_r3
    cmp r0, #0
    beq .Lot_done
    sub sp, #24
    adds r1, r0, #0
    adds r0, r4, #0
    movs r2, #48
    movs r3, #0
    movs r4, #56
    str r4, [sp]
    movs r4, #16
    str r4, [sp, #4]
    str r3, [sp, #8]
    str r3, [sp, #12]
    movs r4, #4
    str r4, [sp, #16]
    movs r4, #16
    str r4, [sp, #20]
    ldr r4, =0x080038AD
    bl .Lot_call_r4
    add sp, #24
.Lot_done:
    pop {r4}
    pop {r0}
    bx r0
.Lot_call_r3:
    bx r3
.Lot_call_r4:
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

    cmp r1, #0xFF
    beq .Lmuzaipixel_font
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
    b .Lset_dimensions

.Lmuzaipixel_font:
    ldr r6, =MuzaipixelChineseFont
    movs r0, #8
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
    cmp r0, #8
    bne .Lnot_muzaipixel_latin
    ldr r6, =MuzaipixelLatinFont
    ldr r0, =MuzaipixelLatinWidths
    ldrb r0, [r0, r3]
    strb r0, [r7]
    b .Lhave_index
.Lnot_muzaipixel_latin:
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

.align 2
.global ChsSpeciesNameTokens
ChsSpeciesNameTokens:
.set chs_species_token_index, 0
.rept 412
    .byte 0xF5, 0xF2, (chs_species_token_index & 0xFF), (chs_species_token_index >> 8), 0xFF, 0xFF
    .set chs_species_token_index, chs_species_token_index + 1
.endr

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
.global ChsBattleStatusGfx
ChsBattleStatusGfx:
    .incbin "patch/gfx/battle_status_tiles.4bpp"

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
.global ChsNamingScreenBackButtonGfx
ChsNamingScreenBackButtonGfx:
    .incbin "build/patch/naming_screen_back_button.4bpp"

.align 2
.global ChsNamingScreenOkButtonGfx
ChsNamingScreenOkButtonGfx:
    .incbin "build/patch/naming_screen_ok_button.4bpp"

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
MuzaipixelChineseFont:
    .incbin "build/patch/muzaipixel_chinese.latfont"
.align 2
MuzaipixelLatinFont:
    .incbin "build/patch/muzaipixel_latin.latfont"
.align 2
MuzaipixelLatinWidths:
    .incbin "patch/fonts/muzaipixel_latin_widths.bin"
.align 2
LatinNormalFont:
    .incbin "build/patch/latin_normal.latfont"
.align 2
LatinSmallFont:
    .incbin "build/patch/latin_small.latfont"
