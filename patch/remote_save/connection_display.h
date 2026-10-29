#ifndef REMOTE_CONNECTION_DISPLAY_H
#define REMOTE_CONNECTION_DISPLAY_H
#include <stdint.h>
#define LINK_PROBE 0x6a51u
#define LINK_CONFIRM 0x6a52u
#define LINK_READY 0xa501u
#define LINK_ACK 0xa502u
#define LINK_DONE 0xa503u
static inline void RemoteDebugShow(const char *text)
{
    static const uint8_t font[26][7] = {
        {14,17,17,31,17,17,17},{30,17,17,30,17,17,30},{14,17,16,16,16,17,14},
        {30,17,17,17,17,17,30},{31,16,16,30,16,16,31},{31,16,16,30,16,16,16},
        {14,17,16,23,17,17,15},{17,17,17,31,17,17,17},{14,4,4,4,4,4,14},
        {7,2,2,2,18,18,12},{17,18,20,24,20,18,17},{16,16,16,16,16,16,31},
        {17,27,21,21,17,17,17},{17,25,21,19,17,17,17},{14,17,17,17,17,17,14},
        {30,17,17,30,16,16,16},{14,17,17,17,21,18,13},{30,17,17,30,20,18,17},
        {15,16,16,14,1,1,30},{31,4,4,4,4,4,4},{17,17,17,17,17,17,14},
        {17,17,17,17,17,10,4},{17,17,17,21,21,21,10},{17,17,10,4,10,17,17},
        {17,17,10,4,4,4,4},{31,1,2,4,8,16,31}
    };
    static const uint8_t digits[10][7] = {
        {14,17,19,21,25,17,14},{4,12,4,4,4,4,14},{14,17,1,2,4,8,31},
        {30,1,1,14,1,1,30},{2,6,10,18,31,2,2},{31,16,16,30,1,1,30},
        {14,16,16,30,17,17,14},{31,1,2,4,8,8,8},{14,17,17,14,17,17,14},
        {14,17,17,15,1,1,14}
    };
    /* 19 glyph sprites and 42 transparent progress sprites. The tile/OAM
     * reservation is temporary; the game redraws them when the menu resumes. */
    volatile uint16_t *tiles=(volatile uint16_t *)0x06017600u;
    volatile uint16_t *oam=(volatile uint16_t *)0x07000000u;
    volatile uint16_t *palette=(volatile uint16_t *)0x050003e0u;
    volatile uint16_t *io=(volatile uint16_t *)0x04000000u;
    unsigned i,y,x, wait;
    /* OAM is writable in VBlank. A bounded wait also prevents a hang if the
     * display is stopped by an emulator or debugger. */
    for(wait=0;wait<200000u && (io[3]<160u || io[3]>215u);wait++) {}
    palette[1]=0x0000u; /* Opaque black; palette index zero remains transparent. */
    for(i=0;i<61u*16u;i++) tiles[i]=0;
    for(i=0;i<61u;i++) {
        unsigned obj=60u+i;
        oam[obj*4u]=0x0200u;
        oam[obj*4u+1]=0;
        oam[obj*4u+2]=(uint16_t)(0xf000u | (0x3b0u+i));
    }
    for(i=0;i<19u && text[i];i++) {
        unsigned c=(unsigned char)text[i]; const uint8_t *glyph=0;
        if(c>='A'&&c<='Z') glyph=font[c-'A'];
        else if(c>='0'&&c<='9') glyph=digits[c-'0'];
        if(!glyph) continue;
        for(y=0;y<7;y++) {
            uint32_t row=0;
            for(x=0;x<5;x++) if(glyph[y]&(1u<<(4u-x))) row|=1u<<(x*4u);
            tiles[i*16u+y*2u]=(uint16_t)row;
            tiles[i*16u+y*2u+1u]=(uint16_t)(row>>16);
        }
        oam[(60u+i)*4u]=142u;
        oam[(60u+i)*4u+1u]=(uint16_t)(8u+i*8u);
    }
    for(i=0;i<42u;i++) {
        unsigned obj=79u+i;
        oam[obj*4u]=151u;
        oam[obj*4u+1u]=(uint16_t)(8u+i*5u);
    }
    io[0] = (uint16_t)((io[0] | 0x1000u) & ~0x0080u); /* OBJ on, display unblanked; keep BG mode. */
}
/* Progress uses already configured sprites, so no OAM writes are needed
 * while serial transfers are in flight. */
static inline void RemoteDebugSectorProgress(unsigned count)
{
    volatile uint16_t *tile=(volatile uint16_t *)0x06017600u;
    unsigned y;
    if(count>=42u) return;
    tile+=(19u+count)*16u;
    for(y=0;y<4;y++) { tile[y*2u]=0x1111u; tile[y*2u+1u]=0; }
}
static inline void RemoteDebugMark(unsigned stage)
{
    RemoteDebugSectorProgress(stage);
}
#endif
