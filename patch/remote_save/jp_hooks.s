.syntax unified
.cpu arm7tdmi
.thumb
.section .text
.align 2
.global RemoteHookReadFlash
.type RemoteHookReadFlash, %function
.thumb_func
RemoteHookReadFlash:
    push {r4-r7, lr}
    movs r4, r0
    movs r5, r1
    movs r6, r2
    movs r7, r3
    bl RemoteJpSaveActive
    cmp r0, #0
    beq 1f
    movs r0, r4
    movs r1, r5
    movs r2, r6
    movs r3, r7
    bl RemoteJpRead
    pop {r4-r7, pc}
1:  movs r0, r4
    movs r1, r5
    movs r2, r6
    movs r3, r7
    pop {r4-r7}
    mov ip, r3
    pop {r3}
    mov lr, r3
    mov r3, ip
    b RemoteOriginalReadFlash

.thumb_func
RemoteOriginalReadFlash:
    push {r4-r7, lr}
    sub sp, #0x80
    adds r5, r1, #0
    adds r6, r2, #0
    adds r7, r3, #0
    lsls r3, r0, #16
    lsrs r4, r3, #16
    ldr r2, =0x04000204
    ldr r0, =0x0829006d
    bx r0

.align 2
.global RemoteHookProgramSectorAndVerify
.type RemoteHookProgramSectorAndVerify, %function
.thumb_func
RemoteHookProgramSectorAndVerify:
    push {r4-r7, lr}
    movs r4, r0
    movs r5, r1
    bl RemoteJpSaveActive
    cmp r0, #0
    beq 2f
    movs r0, r4
    movs r1, r5
    bl RemoteJpProgramSector
    pop {r4-r7, pc}
2:  movs r0, r4
    movs r1, r5
    pop {r4-r7}
    pop {r3}
    mov lr, r3
    b RemoteOriginalProgramSectorAndVerify

.thumb_func
RemoteOriginalProgramSectorAndVerify:
    push {r4-r6, lr}
    adds r5, r1, #0
    lsls r0, r0, #16
    lsrs r4, r0, #16
    @ Resume at the untouched movs r6 and branch. The retry loop at 0x264
    @ must also stay intact, so this function uses an 8-byte veneer.
    ldr r3, =0x08290261
    bx r3
.ltorg

.align 2
.global RemoteOriginalTrySavingData
.type RemoteOriginalTrySavingData, %function
.thumb_func
RemoteOriginalTrySavingData:
    push {r4, r5, lr}
    lsls r0, r0, #24
    lsrs r5, r0, #24
    ldr r0, =0x03005ae8
    ldr r4, [r0]
    cmp r4, #1
    bne 1f
    ldr r3, =0x08153285
    bx r3
1:  ldr r3, =0x08153297
    bx r3
.ltorg

.section .rodata.remote_receiver, "a", %progbits
.align 2
.global RemoteReceiverImageStart
RemoteReceiverImageStart:
    .incbin "build/remote_save/receiver.gba"
.global RemoteReceiverImageEnd
RemoteReceiverImageEnd:

.include "patch/remote_save/jp_official_sender.s"
