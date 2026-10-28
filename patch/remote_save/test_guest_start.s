.syntax unified
.cpu arm7tdmi
.arm
.global _start
.section .text.start
_start:
 ldr sp, =0x03007f00
 ldr r0, =TestMain + 1
 bx r0
