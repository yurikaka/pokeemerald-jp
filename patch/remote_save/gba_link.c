#include "gba_link.h"
#define IO16(a) (*(volatile uint16_t *)(a))
#define REG_SIOMULTI1 IO16(0x04000122u)
#define REG_SIOCNT IO16(0x04000128u)
#define REG_SIOMLT_SEND IO16(0x0400012au)
#define REG_RCNT IO16(0x04000134u)
void RemoteGbaLinkMasterInit(void)
{
    REG_RCNT &= (uint16_t)~0x8000u;
    REG_SIOCNT = 0x2003u;
    REG_SIOMLT_SEND = 0;
}
int RemoteGbaLinkTransfer(void *unused, uint16_t tx, uint16_t *rx)
{
    volatile uint32_t delay;
    uint32_t timeout;
    (void)unused;
    if (!rx) return 0;
    /* Give the receiver time to load its next response word. */
    for (delay = 0; delay < 2000u; ++delay) {}
    for (timeout = 0; timeout < 100000u; ++timeout)
        if ((REG_SIOCNT & 0x000cu) == 0x0008u) break; /* ready, master */
    if (timeout == 100000u) return 0;
    REG_SIOMLT_SEND = tx;
    REG_SIOCNT |= 0x0080u;
    for (timeout = 0; timeout < 100000u; ++timeout)
        if (!(REG_SIOCNT & 0x0080u)) break;
    if (timeout == 100000u || (REG_SIOCNT & 0x0040u)) return 0;
    *rx = REG_SIOMULTI1;
    return *rx != 0xffffu;
}
