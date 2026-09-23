SECTIONS
{
    . = 0x09000000;

    .text : { *(.text*) }
    .rodata : { *(.rodata*) }

    /DISCARD/ : { *(.ARM.attributes) *(.comment) *(.note*) }
}
