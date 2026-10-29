.syntax unified
.cpu arm7tdmi
.section .header,"ax",%progbits
.arm
b direct_start
.incbin "baserom_jp.gba", 4, 188
.section .text.start,"ax",%progbits
.arm
.global direct_start
direct_start:
    mov r0, #0x1f
    msr cpsr_c, r0
    ldr sp, =0x03007f00
    ldr r0, =DirectGuestMain + 1
    bx r0
