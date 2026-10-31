.syntax unified
.cpu arm7tdmi
.thumb
.section .battle_nickname, "ax", %progbits
.align 2
.equ JP_SPECIES_NAMES, 0x082EA31C
.global ChsBattleGetMonNickname
.type ChsBattleGetMonNickname, %function
.thumb_func
ChsBattleGetMonNickname:
    adds r1, r2, #0
    push {r4-r6, lr}
    sub sp, #0x0C
    adds r4, r0, #0
    adds r5, r1, #0
    movs r1, #2
    mov r2, sp
    ldr r3, =0x0806A059
    bl .Lbattlenick_call_r3
    mov r0, sp
    ldr r3, =0x0800885D
    bl .Lbattlenick_call_r3
    @ Only display helpers: keep egg creation and storage nickname getters JP.
    adds r0, r4, #0
    movs r1, #0x2D
    movs r2, #0
    ldr r3, =0x0806A059
    bl .Lbattlenick_call_r3
    cmp r0, #0
    beq .Lbattlenick_species_display
    mov r0, sp
    ldr r1, =0x085C8C62
    ldr r3, =0x0800895D
    bl .Lbattlenick_call_r3
    cmp r0, #0
    bne .Lbattlenick_copy_original
    adds r0, r5, #0
    ldr r1, =Chs_ChecklistLiteral_gText_EggNickname
    ldr r3, =0x080088B9
    bl .Lbattlenick_call_r3
    b .Lbattlenick_done
.Lbattlenick_species_display:
    adds r0, r4, #0
    movs r1, #0x0B
    movs r2, #0
    ldr r3, =0x0806A059
    bl .Lbattlenick_call_r3
    lsls r6, r0, #0x10
    lsrs r6, r6, #0x10
    ldr r1, =(412)
    cmp r6, r1
    bhs .Lbattlenick_copy_original
    lsls r0, r6, #1
    adds r0, r0, r6
    lsls r0, r0, #1
    ldr r1, =JP_SPECIES_NAMES
    adds r1, r1, r0
    mov r0, sp
    ldr r3, =0x0800895D
    bl .Lbattlenick_call_r3
    cmp r0, #0
    bne .Lbattlenick_copy_original
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
    b .Lbattlenick_done
.Lbattlenick_copy_original:
    adds r0, r5, #0
    mov r1, sp
    ldr r3, =0x080088B9
    bl .Lbattlenick_call_r3
.Lbattlenick_done:
    add sp, #0x0C
    pop {r4-r6}
    pop {r1}
    bx r1
.Lbattlenick_call_r3:
    bx r3

.ltorg

.align 2
.global ChsGetBoxMonNicknameFromData
.type ChsGetBoxMonNicknameFromData, %function
.thumb_func
ChsGetBoxMonNicknameFromData:
    adds r1, r2, #0
    ldr r3, =ChsCopyBoxMonNickname + 1
    bx r3
.ltorg
