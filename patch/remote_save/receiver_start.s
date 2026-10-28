.syntax unified
.cpu arm7tdmi
.section .header,"ax",%progbits
.arm
b receiver_start
.incbin "baserom_jp.gba", 4, 188
.section .text.start,"ax",%progbits
.arm
.global receiver_start
receiver_start:
    b receiver_boot
    .space 28
receiver_boot:
    ldr sp, =0x03007f00
    ldr r0, =__bss_start
    ldr r1, =__bss_end
    mov r2, #0
1:  cmp r0, r1
    strlo r2, [r0], #4
    blo 1b
    ldr r0, =RemoteReceiverMain + 1
    bx r0
2:  b 2b
