/* Wokann dev battle_interface.c: the JP safari healthbox is two 64x64
 * objects with the right object's tiles at +64. Render through the existing
 * Chinese font printer instead of the single-byte RenderTextFont9 path.
 */
typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;

static unsigned is_safari(void)
{
    return *(const u32 *)0x02022C90 & 0x80;
}

/* data_b2.s: 25 eight-byte entries, including the terminator. The action
 * window grows left by two tiles; its extra tiles must not alias the prompt.
 */
void ChsSafariInitWindows(const u8 *templates)
{
    if (!is_safari()) {
        ((void (*)(const u8 *))0x08003091)(templates);
        return;
    }
    u8 copy[25 * 8] __attribute__((aligned(4)));
    for (unsigned i = 0; i < sizeof(copy); i++)
        ((volatile u8 *)copy)[i] = templates[i];
    copy[8 + 3] = 13;                 /* prompt width: 104px */
    copy[8 + 6] = 0xC0;              /* prompt base block: 0x1C0 */
    copy[16 + 1] = 17;               /* menu x: 136px */
    copy[16 + 3] = 12;               /* menu width: 96px */
    ((void (*)(const u8 *))0x08003091)(copy);
}

/* Both initial loading and returning from the Pokeblock case load this map. */
void ChsSafariLoadTextboxMap(void)
{
    ((void (*)(unsigned, const void *, unsigned, unsigned))0x080021CD)
        (0, (const void *)0x08C00530, 0, 0);
    if (is_safari()) {
        u16 *map = ((u16 *(*)(unsigned))0x08002195)(0);
        map[33 * 32 + 15] = map[33 * 32 + 17];
        map[33 * 32 + 17] = 0;
        for (unsigned y = 34; y <= 39; y++) {
            u16 edge = map[y * 32 + 17], inside = map[y * 32 + 18];
            for (unsigned x = 15; x < 29; x++)
                map[y * 32 + x] = x == 15 ? edge : inside;
        }
    }
    ((void (*)(unsigned))0x08002249)(0);
}

static void action_cursor(unsigned position, unsigned show)
{
    u16 tiles[2];
    tiles[0] = show ? 1 : 0x1016;
    tiles[1] = show ? 2 : 0x1016;
    ((void (*)(unsigned, const u16 *, unsigned, unsigned, unsigned, unsigned, unsigned))0x080023B5)
        (0, tiles, (is_safari() ? 16 : 18) + (position & 1) * 6,
         35 + (position & 2), 1, 2, 17);
    ((void (*)(unsigned))0x08002249)(0);
}

void ChsSafariShowActionCursor(unsigned position)
{
    action_cursor(position & 255, 1);
}

void ChsSafariHideActionCursor(unsigned position)
{
    action_cursor(position & 255, 0);
}

#define ADD_WINDOW ((unsigned (*)(const u8 *))0x08003251)
#define REMOVE_WINDOW ((void (*)(unsigned))0x08003445)
#define FILL_WINDOW ((void (*)(unsigned, unsigned))0x08003B19)
#define WINDOW_ATTRIBUTE ((u32 (*)(unsigned, unsigned))0x0800401D)
#define PRINT ((void (*)(unsigned, unsigned, unsigned, unsigned, unsigned, unsigned, const u8 *, int, const u8 *))0x08199B85)

/* Native AddWindow copies two words with LDR: ARM7 rotates unaligned loads. */
static const u8 window_template[] __attribute__((aligned(4))) = {0, 0, 0, 7, 2, 0, 0, 0};
static const u8 colors[] = {2, 1, 3};
static const u8 title[] = {0xFC,0x16,0x73,0xF1,0x67,0xA7,0x6A,0x14,0xFF};

static void draw(unsigned sprite, const u8 *text, unsigned left, unsigned top)
{
    unsigned window = ADD_WINDOW(window_template);
    if (window == 0xFF) return;
    FILL_WINDOW(window, 0x22);
    PRINT(window, 0, 0, 0, 0, 0, colors, -1, text);
    const u8 *pixels = (const u8 *)WINDOW_ATTRIBUTE(window, 7);
    const u8 *object = (const u8 *)0x020205AC + (sprite & 255) * 68;
    unsigned base_tile = *(const u16 *)(object + 4) & 1023;
    for (unsigned y = 0; y < 13; y++) {
        for (unsigned x = 0; x < 56; x++) {
            unsigned source = ((y >> 3) * 7 + (x >> 3)) * 32
                            + (y & 7) * 4 + (x & 7) / 2;
            unsigned color = (pixels[source] >> ((x & 1) * 4)) & 15;
            unsigned dx = left + x, dy = top + y;
            unsigned tile = base_tile + (dx >> 6) * 64
                          + (dy >> 3) * 8 + ((dx & 63) >> 3);
            /* GBA VRAM requires halfword writes, including single pixels. */
            volatile u16 *dest = (volatile u16 *)(0x06010000 + tile * 32
                               + (dy & 7) * 4 + (dx & 7) / 4 * 2);
            unsigned shift = (dx & 3) * 4;
            *dest = (*dest & ~(15u << shift)) | (color << shift);
        }
    }
    REMOVE_WINDOW(window);
}

void ChsSafariHealthboxTitle(unsigned sprite)
{
    draw(sprite, title, 24, 4);
}

void ChsSafariHealthboxCount(unsigned sprite)
{
    unsigned count = *(const u8 *)0x02039D18;
    static const u8 format[] = {0xFC,0x16,0x6A,0xDF,0x6E,0x8E,0,0,0x63,0x60,0xFF};
    u8 text[sizeof(format)];
    for (unsigned i = 0; i < sizeof(format); i++)
        ((volatile u8 *)text)[i] = format[i];
    unsigned tens = 0;
    while (count >= 10) { count -= 10; tens++; }
    text[6] = tens ? 0xA1 + tens : 0;
    text[7] = 0xA1 + count;
    draw(sprite, text, 32, 19);
}
