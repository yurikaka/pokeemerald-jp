#include "gba_flash.h"
#define REG_WAITCNT (*(volatile uint16_t *)0x04000204u)
#define CART_ROM ((volatile const uint8_t *)0x08000000u)
#define CART_FLASH ((volatile uint8_t *)0x0e000000u)
static uint8_t gba_read(void *ctx, uint16_t address)
{ (void)ctx; return CART_FLASH[address]; }
static void gba_write(void *ctx, uint16_t address, uint8_t data)
{ (void)ctx; CART_FLASH[address] = data; }
static void gba_delay(void *ctx)
{ volatile uint32_t i; (void)ctx; for (i = 0; i < 20000; ++i) {} }
int RemoteGbaFlashOpen(struct RemoteFlash *flash)
{
    struct RemoteFlashBus b;
    if (!flash || CART_ROM[0xac] != 'B' || CART_ROM[0xad] != 'P' ||
        CART_ROM[0xae] != 'E' || CART_ROM[0xaf] != 'J') return 0;
    REG_WAITCNT = (uint16_t)((REG_WAITCNT & ~3u) | 3u);
    b.context = 0; b.read = gba_read; b.write = gba_write; b.delay = gba_delay;
    /* Upper bound in iterations, not a precise hardware-time guarantee. */
    RemoteFlashInit(flash, b, 4000000u);
    return RemoteFlashIdentify(flash);
}
