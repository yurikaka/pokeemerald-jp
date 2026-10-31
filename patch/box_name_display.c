/* Wokann dev pokemon_storage_system.c: boxNames at +0x8344, stride 9.
 * Only explicit display entries translate default box labels. */
typedef unsigned char u8;
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

u8 *ChsBoxNameOriginal(unsigned raw_box)
{
    unsigned box = raw_box & 255;
    if (box >= 14) return 0;
    return *(u8 **)0x03005AF4 + 0x8344 + box * 9;
}

const u8 *ChsBoxNameForDisplay(unsigned raw_box)
{
    unsigned box = raw_box & 255;
    const u8 *name = ChsBoxNameOriginal(raw_box);
    if (!name) return 0;
    return is_default_name(name, box) ? box_labels[box] : name;
}

/* StringLength counts bytes, so omit the mode prefix only for centering. */
const u8 *ChsBoxNameForWidth(unsigned raw_box)
{
    unsigned box = raw_box & 255;
    const u8 *name = ChsBoxNameOriginal(raw_box);
    if (!name) return 0;
    return is_default_name(name, box) ? box_labels[box] + 2 : name;
}
