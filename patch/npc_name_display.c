/* Display-only adapters; no save/Pokemon/link-name localization writes.
 * Addresses: Wokann dev battle_tower.c, frontier_util.c and tv.c.
 */
typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;
struct NamePair { const u8 *jp; const u8 *chs; };
#include "npc_names.h"
extern const u8 *ChsTrainerNames[];
extern const u8 *ChsContestOpponentDisplayNames[][2];
extern void ChsOriginalFrontierName(u8 *, u16);
extern void ChsOriginalBrainName(u8 *);
extern void ChsOriginalDomeName(u8 *, u16);

static u8 *copy(u8 *dest, const u8 *src)
{
    while (*src != 255) *dest++ = *src++;
    *dest = 255;
    return dest;
}
static int equal(const u8 *a, const u8 *b)
{
    for (unsigned i = 0; i < 32; i++) {
        if (a[i] != b[i]) return 0;
        if (a[i] == 255) return 1;
    }
    return 0;
}
const u8 *ChsResolveTrainerDisplayName(const u8 *name)
{
    /* pokenav_match_call_list.c supplies raw gTrainers name pointers. */
    u32 offset = (u32)name - 0x082E3840;
    if (offset <= 854 * 32 && !(offset & 31)) return ChsTrainerNames[offset >> 5];
    return name;
}

static const u8 *lookup_identity(const u8 *name)
{
    for (unsigned i = 0; i < sizeof(npc_names) / sizeof(npc_names[0]); i++)
        if (name == npc_names[i].jp) return npc_names[i].chs;
    return 0;
}
static const u8 *lookup_brain(const u8 *name)
{
    /* Match the original getter's result: recorded battles need not use the
     * current facility variable. These seven identities have distinct names. */
    for (unsigned id = 805; id <= 811; id++) {
        const u8 *jp = (const u8 *)0x082E3840 + id * 32;
        if (equal(name, jp)) return lookup_identity(jp);
    }
    return 0;
}

void ChsFrontierNameDisplay(u8 *dest, u16 id)
{
    u32 caller = (u32)__builtin_return_address(0);
    ChsOriginalFrontierName(dest, id);
    /* Wokann-backed display callers only. Save writer 08164D03 and link
     * data producers 0803736F/7B deliberately remain Japanese. */
    switch (caller) {
    case 0x0806E6BF: case 0x0814F5DB: case 0x081647DB:
    case 0x0816484D: case 0x081A40E7: case 0x081A40FB:
    case 0x081A57DD: /* battle_arena.c BufferArenaOpponentName */
    case 0x081B999D: break;
    default: return;
    }
    const u8 *jp = 0;
    if (id == 0x3FE) {
        const u8 *chs = lookup_brain(dest);
        if (chs) copy(dest, chs);
        return;
    } else if (id == 0xC03) jp = (const u8 *)0x082E9CC0;
    else if (id < 300) jp = *(const u8 **)0x0203B954 + id * 52 + 4;
    const u8 *chs = lookup_identity(jp);
    if (chs) copy(dest, chs);
}
void ChsBrainNameDisplay(u8 *dest)
{
    u32 caller = (u32)__builtin_return_address(0);
    ChsOriginalBrainName(dest);
    if (caller == 0x0814F201) {
        const u8 *chs = lookup_brain(dest);
        if (chs) copy(dest, chs);
    }
}
void ChsDomeBrainNameDisplay(u8 *dest)
{
    copy(dest, lookup_identity((const u8 *)0x082E9D00));
}
void ChsDomeNameDisplay(u8 *dest, u16 id)
{
    ChsOriginalDomeName(dest, id);
    if (id < 300) {
        const u8 *chs = lookup_identity(*(const u8 **)0x0203B954 + id * 52 + 4);
        if (chs) copy(dest, chs);
    }
}

u8 *ChsVsNameCopy(u8 *dest, const u8 *src)
{
    u32 caller = (u32)__builtin_return_address(0);
    /* battle_bg.c InitLinkBattleVsScreen, only Tower's two simulated NPC
     * slots. Real players and all other StringCopy7 callers retain JP's
     * original five-byte limit. No link record is rewritten. */
    if (caller == 0x08035C1B && (*(u32 *)0x02022C90 & 0x00800000)) {
        unsigned opponent = src == (const u8 *)0x020226E0 ? 0 :
                            src == (const u8 *)0x020226FC ? 1 : 2;
        if (opponent < 2) {
            unsigned id = *(u16 *)(0x0203886A + opponent * 2);
            if (id < 300 && equal(src, npc_names[id].jp))
                return copy(dest, npc_compact_names[id]);
        }
    }
    unsigned i;
    for (i = 0; i < 5 && src[i] != 255; i++) dest[i] = src[i];
    dest[i] = 255;
    return dest + i;
}

/* TV has no NPC identity flag. User-selected policy: assume an NPC when
 * the show's existing fields uniquely match its scene's NPC mapping.
 * A same-name player may therefore display as that NPC; persistence is JP.
 */
u8 *ChsTvNameStringCopy(u8 *dest, const u8 *src)
{
    u32 caller = (u32)__builtin_return_address(0);
    const u8 *translated = 0;
    if ((caller >= 0x080F2164 && caller < 0x080F23EC)
        || (caller >= 0x080F31E8 && caller < 0x080F39D0)) {
        unsigned slot = *(u16 *)0x02037280;
        if (slot < 25) {
            const u8 *show = *(const u8 **)0x03005AEC + 0x27CC + slot * 36;
            if (caller < 0x080F23EC && show[0] == 7 && src == show + 12) {
                /* Tower NPC names are unique within its pool. Do not mix
                 * Tent names or other facility brains into this mapping. */
                for (unsigned i = 0; i < 398; i++) {
                    if (i >= 300 && npc_names[i].jp != (const u8 *)0x082E9CE0) continue;
                    if (!equal(src, npc_names[i].jp)) continue;
                    if (translated && !equal(translated, npc_names[i].chs)) return copy(dest, src);
                    translated = npc_names[i].chs;
                }
            } else if (caller >= 0x080F31E8 && show[0] == 8 && src == show + 4) {
                /* Contest winner at +20 is always a player: never replace.
                 * Losing name + species disambiguates the two マヤコ NPCs. */
                u16 species = *(const u16 *)(show + 2);
                for (unsigned i = 0; i < 96; i++) {
                    const u8 *record = (const u8 *)0x08561028 + i * 64;
                    if (*(const u16 *)record != species || !equal(src, record + 13)) continue;
                    const u8 *name = ChsContestOpponentDisplayNames[i][1];
                    if (translated && !equal(translated, name)) return copy(dest, src);
                    translated = name;
                }
            }
        }
    }
    return copy(dest, translated ? translated : src);
}
