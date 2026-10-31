SECTIONS
{
    . = 0x08162D3C;
    .battle_nickname : { *(.battle_nickname) }
    ASSERT(SIZEOF(.battle_nickname) <= 0x154, "battle nickname helper exceeds displaced space")

    . = 0x09000000;

    .text : { *(.text*) }
    .rodata : { *(.rodata*) }

    /DISCARD/ : { *(.ARM.attributes) *(.comment) *(.note*) }
}
