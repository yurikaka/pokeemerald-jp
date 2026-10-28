#include "client.h"
#include "game.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
struct Harness { struct RemoteSaveServer server; uint8_t flash[REMOTE_SAVE_FLASH_SIZE]; int writes, erases, drop, always_drop; };
static int read_cb(void *p, uint32_t a, uint8_t *d, uint16_t n)
{ struct Harness *h = p; memcpy(d, h->flash + a, n); return 1; }
static int program_cb(void *p, uint32_t a, const uint8_t *d, uint16_t n)
{ struct Harness *h = p; ++h->writes; memcpy(h->flash + a, d, n); return 1; }
static int erase_cb(void *p, uint32_t a)
{ struct Harness *h = p; ++h->erases; memset(h->flash + a, 255, REMOTE_SAVE_SECTOR_SIZE); return 1; }
static size_t exchange(void *p, const uint8_t *in, size_t n, uint8_t *out, size_t cap)
{
 struct Harness *h = p; size_t result = RemoteSaveServerHandle(&h->server, in, n, out, cap);
 if (h->drop) { h->drop = 0; return 0; }
 return h->always_drop ? 0 : result;
}
int main(void)
{
 static struct Harness h;
 struct RemoteSaveBackend b = {&h, read_cb, program_cb, erase_cb};
 struct RemoteSaveClient c;
 uint8_t source[600], dest[600]; unsigned i;
 static uint8_t sector_data[REMOTE_SAVE_SECTOR_SIZE], sector_read[REMOTE_SAVE_SECTOR_SIZE];
 memset(h.flash, 255, sizeof(h.flash)); RemoteSaveServerInit(&h.server, b);
 RemoteSaveClientInit(&c, &h, exchange, 2);
 assert(RemoteSaveClientHello(&c));
 assert(RemoteSaveClientStatus(&c));
 for (i = 0; i < sizeof(source); ++i) source[i] = (uint8_t)(i * 7u);
 h.drop = 1;
 assert(RemoteSaveClientProgram(&c, 0x1ff00, source, sizeof(source)) == 0); /* bounds */
 assert(h.writes == 0 && !c.failed);
 assert(RemoteSaveClientProgram(&c, 0x1eeff, source, sizeof(source)));
 assert(h.writes == 4); /* 1, 256, 256, 87; first response was lost */
 assert(RemoteSaveClientRead(&c, 0x1eeff, dest, sizeof(dest)));
 assert(memcmp(source, dest, sizeof(source)) == 0);
 h.drop = 1; assert(RemoteSaveClientErase(&c, 0x1e000)); assert(h.erases == 1);
 h.always_drop = 1; assert(!RemoteSaveClientErase(&c, 0x1f000));
 assert(c.failed && h.erases == 2);
 assert(!RemoteSaveClientErase(&c, 0x1d000) && h.erases == 2);
 h.always_drop = 0; RemoteSaveServerInit(&h.server, b);
 RemoteSaveClientInit(&c, &h, exchange, 2); assert(RemoteSaveClientHello(&c));
 for (i = 0; i < sizeof(sector_data); ++i) sector_data[i] = (uint8_t)(i * 13u);
 assert(RemoteGameProgramSector(&c, 31, sector_data));
 assert(RemoteGameRead(&c, 31, 0, sector_read, sizeof(sector_read)));
 assert(memcmp(sector_data, sector_read, sizeof(sector_data)) == 0);
 assert(RemoteGameErase(&c, 16));
 assert(RemoteGameProgramByte(&c, 16, 0xfff, 0x52));
 assert(RemoteGameRead(&c, 16, 0xfff, sector_read, 1) && sector_read[0] == 0x52);
 assert(!RemoteGameRead(&c, 32, 0, sector_read, 1));
 assert(!RemoteGameProgramByte(&c, 0, 0x1000, 0x52));
 assert(!RemoteGameRead(&c, 0, 0xfff, sector_read, 2));
 /* A different peer at the expected sequence must not pass identity check. */
 ++h.server.session;
 assert(!RemoteSaveClientStatus(&c));
 assert(c.failed);
 RemoteSaveServerInit(&h.server, b);
 c.failed = 0;
 assert(!RemoteSaveClientStatus(&c)); /* restarted peer has no HELLO */
 RemoteSaveClientInit(&c, &h, exchange, 0);
 assert(RemoteSaveClientHello(&c));
 { int before = h.erases; h.drop = 1;
   assert(!RemoteSaveClientErase(&c, 0x1c000));
   assert(h.erases == before + 1 && c.failed); }
 puts("remote save end-to-end protocol tests passed"); return 0;
}
