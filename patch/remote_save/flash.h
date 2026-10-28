#ifndef REMOTE_SAVE_FLASH_H
#define REMOTE_SAVE_FLASH_H
#include "server.h"

/* Bus callbacks must perform volatile 8-bit accesses to the Flash window.
 * All driver code and callbacks must execute from RAM on real hardware. */
struct RemoteFlashBus {
    void *context;
    uint8_t (*read)(void *, uint16_t);
    void (*write)(void *, uint16_t, uint8_t);
    void (*delay)(void *);
};
struct RemoteFlash {
    struct RemoteFlashBus bus;
    uint8_t identified;
    uint32_t poll_limit;
};
void RemoteFlashInit(struct RemoteFlash *, struct RemoteFlashBus, uint32_t);
int RemoteFlashIdentify(struct RemoteFlash *);
struct RemoteSaveBackend RemoteFlashBackend(struct RemoteFlash *);
#endif
