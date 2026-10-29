#ifndef REMOTE_BOOT_HANDSHAKE_H
#define REMOTE_BOOT_HANDSHAKE_H
#include <stdint.h>
/* The response returned here is preloaded for the NEXT multiplayer transfer. */
struct RemoteGuestBootHandshake { unsigned state; uint16_t code0,code1; };
static inline int RemoteGuestBootStep(struct RemoteGuestBootHandshake *h, uint16_t word, uint16_t *next)
{
    static const uint16_t expected[6]={0,0x8000,0x0400,0x0020,0x0001,0};
    if (h->state < 6) {
        if (word != expected[h->state]) {
            h->state = word == 0 ? 1u : 0u;
            *next = 0;
            return 0;
        }
        ++h->state;
        *next = h->state == 6 ? h->code0 : word;
        return 0;
    }
    if (h->state == 6 && word == h->code0) {
        h->state = 7; *next = h->code1; return 0;
    }
    if (h->state == 7 && word == h->code1) {
        h->state = 8; *next = h->code1; return 1;
    }
    h->state = word == 0 ? 1u : 0u; *next = 0; return 0;
}
#endif
