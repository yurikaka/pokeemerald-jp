ENTRY(BoxDebugMain)
SECTIONS {
 . = 0x0201b200;
 .text : { *(.text*) *(.rodata*) }
 .data : { *(.data*) }
 . = ALIGN(4);
 __box_bss_start = .;
 .bss (NOLOAD) : { *(.bss*) *(COMMON) }
 . = ALIGN(4);
 __box_bss_end = .;
 /DISCARD/ : { *(.ARM.attributes) *(.comment) *(.note*) *(.eh_frame*) }
}
ASSERT(__box_bss_end <= 0x0203f000, "box guest exceeds safe EWRAM")
