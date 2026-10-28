ENTRY(receiver_start)
SECTIONS {
 . = 0x02000000;
 .header : { KEEP(*(.header)) }
 .text : { *(.text.start) *(.text*) *(.rodata*) }
 .data : { *(.data*) }
 . = ALIGN(4);
 __bss_start = .;
 .bss (NOLOAD) : { *(.bss*) *(COMMON) }
 . = ALIGN(4);
 __bss_end = .;
 /DISCARD/ : { *(.ARM.attributes) *(.comment) *(.note*) *(.eh_frame*) }
}
ASSERT(__bss_end <= 0x02040000, "receiver exceeds GBA EWRAM")
