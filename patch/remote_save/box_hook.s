.syntax unified
.cpu arm7tdmi
.thumb
.section .text
.align 2
.global BoxWaitForScreen
.type BoxWaitForScreen, %function
.thumb_func
BoxWaitForScreen:
    /* Reproduce the two replaced Box loop instructions. The loop ends in
       VBlankIntrWait, so 180 iterations leave the original screen visible. */
    ldr r0, [r4]
    adds r0, #1
    cmp r0, #180
    bhs 1f
    bx lr
1:
    bl BoxDebugMain
    b 1b
