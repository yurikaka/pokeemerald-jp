#include "slot_select.h"
#define SLOT_SECTORS 14u
#define SECTOR_SIZE 4096u
static uint16_t read16(const uint8_t *p) { return (uint16_t)(p[0] | ((uint16_t)p[1] << 8)); }
static uint32_t read32(const uint8_t *p) { return (uint32_t)read16(p) | ((uint32_t)read16(p+2) << 16); }
int RemoteSlotValidate(const uint8_t *slot, unsigned slot_number, uint32_t *counter)
{
    static const uint16_t sizes[14] = {0xf2c,0xf80,0xf80,0xf80,0xf08,0xf80,0xf80,0xf80,0xf80,0xf80,0xf80,0xf80,0xf80,0x7d0};
    uint32_t flags=0, last=0; unsigned i,j;
    if (!slot || !counter || slot_number > 1) return 0;
    for (i=0;i<SLOT_SECTORS;i++) {
        const uint8_t *s=slot+i*SECTOR_SIZE;
        uint16_t id=read16(s+0xff4); uint32_t sum=0;
        if (read32(s+0xff8)!=0x08012025u || id>=14) return 0;
        for (j=0;j<sizes[id];j+=4) sum+=read32(s+j);
        if ((uint16_t)((sum>>16)+sum)!=read16(s+0xff6)) return 0;
        if (i && last!=read32(s+0xffc)) return 0;
        last=read32(s+0xffc);
        flags |= 1u<<id;
    }
    if (flags != 0x3fffu || (last & 1u)!=slot_number) return 0;
    *counter=last; return 1;
}
int RemoteSlotChoose(int valid0, uint32_t c0, int valid1, uint32_t c1)
{
    if (!valid0) return valid1 ? 1 : -1;
    if (!valid1) return 0;
    if ((c0==0xffffffffu && c1==0) || (c1==0xffffffffu && c0==0))
        return c0+1u < c1+1u ? 1 : 0;
    return c0<c1 ? 1 : 0;
}
