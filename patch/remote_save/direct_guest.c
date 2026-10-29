/* Standalone, read-only GBA cartridge ROM for testing the multiplayer link. */
#include <stdint.h>
#include "connection_display.h"
#define IO16(a) (*(volatile uint16_t *)(a))
#define SIOCNT IO16(0x04000128u)
#define SEND IO16(0x0400012au)
#define MULTI0 IO16(0x04000120u)
#define RCNT IO16(0x04000134u)
#define IF IO16(0x04000202u)
#define IE IO16(0x04000200u)
#define IME IO16(0x04000208u)
void __attribute__((noreturn)) DirectGuestMain(void)
{
    unsigned phase=0;
    IME=0;IE=0;
    RemoteDebugShow("GUEST WAIT PROBE");
    RCNT=0;SIOCNT=0x6003u;SEND=LINK_READY;IF=0xffffu;
    for (;;) {
        uint16_t word;
        while (!(IF&0x80u)) {}
        IF=0x80u;word=MULTI0;
        if (phase==0 && word==LINK_PROBE) {
            phase=1;RemoteDebugShow("GUEST GOT PROBE");SEND=LINK_ACK;
        } else if (phase==1 && word==LINK_CONFIRM) {
            phase=2;RemoteDebugShow("GUEST LINK OK");SEND=LINK_DONE;
        }
    }
}
