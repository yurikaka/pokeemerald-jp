ENTRY(direct_start)
SECTIONS {
 . = 0x08000000;
 .header : { KEEP(*(.header)) }
 .text : { *(.text.start) *(.text*) *(.rodata*) }
 .data : { *(.data*) }
 /DISCARD/ : { *(.ARM.attributes) *(.comment) *(.note*) *(.eh_frame*) }
}
