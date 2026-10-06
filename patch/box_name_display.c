/* Wokann dev pokemon_storage_system.c: boxNames at +0x8344, stride 9.
 * GetBoxNamePtr remains a writable JP save pointer except at verified display
 * callers. No save fields or markers are added; renamed boxes stay unchanged.
 */
typedef unsigned char u8;
typedef unsigned int u32;
#define LABEL1(n) {0xFC,0x16,0xBC,0xC9,0xD2,0x00,0xA1+(n),0xFF}
#define LABEL2(n) {0xFC,0x16,0xBC,0xC9,0xD2,0x00,0xA2,0xA1+(n),0xFF}
static const u8 box_labels[14][9] = {
    LABEL1(1), LABEL1(2), LABEL1(3), LABEL1(4), LABEL1(5),
    LABEL1(6), LABEL1(7), LABEL1(8), LABEL1(9),
    LABEL2(0), LABEL2(1), LABEL2(2), LABEL2(3), LABEL2(4),
};

static int is_default_name(const u8 *name, unsigned box)
{
    const u8 *prefix = (const u8 *)0x085CB584; /* original ボックス */
    unsigned i = 0;
    while (prefix[i] != 255) {
        if (name[i] != prefix[i]) return 0;
        i++;
    }
    unsigned number = box + 1;
    if (number >= 10 && name[i++] != 0xA2) return 0;
    return name[i] == 0xA1 + (number >= 10 ? number - 10 : number)
        && name[i + 1] == 255;
}

const u8 *ChsBoxNameForDisplay(unsigned raw_box)
{
    unsigned box = raw_box & 255; /* original getter explicitly narrows r0 */
    if (box >= 14) return 0;
    u8 *name = *(u8 **)0x03005AF4 + 0x8344 + box * 9;
    u32 caller = (u32)__builtin_return_address(0);
    switch (caller) {
    /* battle_script_commands.c Cmd_givecaughtmon, scrcmd.c bufferboxname */
    case 0x08056309: case 0x08056355: case 0x08056381: case 0x0809ABC7:
    /* Storage box selector and title drawing. */
    case 0x080C74C7: case 0x080CC4A9: case 0x080CC63F:
    /* naming_screen.c DisplaySentToPCMessage, NOT the name editor. */
    case 0x080E2A99: case 0x080E2AD9: case 0x080E2AFF:
    /* pokenav_conditions.c, menu_specialized.c condition location labels */
    case 0x081CD051: case 0x081D2567:
        return is_default_name(name, box) ? box_labels[box] : name;
    /* StringLength counts bytes: omit FC16 only for title centering. */
    case 0x080CC4DF: case 0x080CC68B:
        return is_default_name(name, box) ? box_labels[box] + 2 : name;
    default:
        /* ResetPokemonStorageSystem 080C703F and name editor 080C97A1
         * receive the actual writable storage field, even for defaults. */
        return name;
    }
}
