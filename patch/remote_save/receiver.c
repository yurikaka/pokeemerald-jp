/* Standalone Multiboot receiver. Its entire image is linked into EWRAM. */
#include "gba_flash.h"
#include "link.h"
#define IO16(a) (*(volatile uint16_t *)(a))
#define REG_SIOMULTI0 IO16(0x04000120u)
#define REG_SIOCNT IO16(0x04000128u)
#define REG_SIOMLT_SEND IO16(0x0400012au)
#define REG_RCNT IO16(0x04000134u)
#define REG_IE IO16(0x04000200u)
#define REG_IF IO16(0x04000202u)
#define REG_IME IO16(0x04000208u)
#define SERIAL_IRQ 0x0080u
static struct RemoteFlash flash;
static struct RemoteSaveServer server;
static struct RemoteLinkSlave link;
/* The JP game's Multiboot sender performs a post-BIOS startup handshake before
 * reporting completion. Each slave reply must be loaded before the next clock. */
static int startup_exchange(uint16_t *word)
{
    while (!(REG_SIOCNT & 0x0080u)) {}
    while (REG_SIOCNT & 0x0080u) {}
    if (REG_SIOCNT & 0x0040u) return 0;
    *word = REG_SIOMULTI0;
    return 1;
}
static void startup_handshake(void)
{
    uint16_t word, expected;
    volatile const uint16_t *code = (volatile const uint16_t *)0x020000acu;
    for (;;) {
        for (;;) {
            if (!startup_exchange(&word)) continue;
            REG_SIOMLT_SEND = 0;
            if (word == 0) break;
        }
        expected = 0x8000u;
        while (expected) {
            REG_SIOMLT_SEND = 0;
            if (!startup_exchange(&word) || word != expected) break;
            expected >>= 5;
        }
        if (expected) continue;
        REG_SIOMLT_SEND = 0;
        if (!startup_exchange(&word) || word != 0) continue;
        expected = code[0]; REG_SIOMLT_SEND = expected;
        if (!startup_exchange(&word) || word != expected) continue;
        expected = code[1]; REG_SIOMLT_SEND = expected;
        if (!startup_exchange(&word) || word != expected) continue;
        REG_SIOMLT_SEND = 0;
        return;
    }
}
int RemoteSaveValidatePeer(void)
{
    return RemoteGbaFlashOpen(&flash);
}
#ifdef REMOTE_RECEIVER_SELFTEST
volatile uint32_t gRemoteSelfTestResult;
__attribute__((noinline)) void RemoteGbaFlashTestDone(void) { __asm__ volatile("" ::: "memory"); }
#endif
void RemoteReceiverMain(void)
{
    struct RemoteSaveBackend backend;
    uint16_t in;
    REG_IME = 0; REG_IE = 0; REG_IF = 0xffffu;
    startup_handshake();
    if (!RemoteGbaFlashOpen(&flash)) {
        /* No Flash commands will be served when identification fails. */
        for (;;) {}
    }
    backend = RemoteFlashBackend(&flash);
#ifdef REMOTE_RECEIVER_SELFTEST
    {
        uint8_t expected[4] = {0x12, 0x34, 0x56, 0x78}, actual[4];
        gRemoteSelfTestResult = 1;
        if (!backend.erase(backend.context, 0x1f000u)) gRemoteSelfTestResult = 2;
        else if (!backend.program(backend.context, 0x1f001u, expected, 4)) gRemoteSelfTestResult = 3;
        else if (!backend.read(backend.context, 0x1f001u, actual, 4)) gRemoteSelfTestResult = 4;
        else if (actual[0] != expected[0] || actual[1] != expected[1] ||
                 actual[2] != expected[2] || actual[3] != expected[3]) gRemoteSelfTestResult = 5;
        else gRemoteSelfTestResult = 0;
        RemoteGbaFlashTestDone();
        for (;;) {}
    }
#endif
    RemoteSaveServerInit(&server, backend);
    RemoteLinkSlaveInit(&link, &server);
    REG_RCNT &= (uint16_t)~0x8000u;
    REG_SIOCNT = 0x6003u; /* Multiplayer, serial IRQ enabled, 115200 baud. */
    REG_SIOMLT_SEND = link.output;
    REG_IF = SERIAL_IRQ;
    for (;;) {
        while (!(REG_IF & SERIAL_IRQ)) {}
        REG_IF = SERIAL_IRQ;
        in = REG_SIOMULTI0;
        in = RemoteLinkSlaveReceive(&link, in);
        /* Discard clocks received while a long Flash operation was running;
         * their old output was READY, so they must not consume reply bytes. */
        REG_IF = SERIAL_IRQ;
        REG_SIOMLT_SEND = in;
    }
}
