#include "flash.h"
#include "link.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
struct Fake { uint8_t data[REMOTE_SAVE_FLASH_SIZE]; unsigned state, bank, id, fail; uint8_t maker, device; };
static uint8_t fake_read(void *ctx, uint16_t a)
{
    struct Fake *f = ctx;
    if (f->id) return a == 0 ? f->maker : a == 1 ? f->device : 0xff;
    return f->fail ? 0x20 : f->data[f->bank * 65536u + a];
}
static void fake_write(void *ctx, uint16_t a, uint8_t v)
{
    struct Fake *f = ctx;
    if (v == 0xf0 && a == 0x5555 && f->state != 3) { f->id = 0; f->state = 0; return; }
    switch (f->state) {
    case 0: f->state = (a == 0x5555 && v == 0xaa) ? 1 : 0; break;
    case 1: f->state = (a == 0x2aaa && v == 0x55) ? 2 : 0; break;
    case 2:
        f->state = 0;
        if (a != 0x5555) break;
        if (v == 0x90) f->id = 1;
        else if (v == 0xb0) f->state = 4;
        else if (v == 0xa0) f->state = 3;
        else if (v == 0x80) f->state = 5;
        break;
    case 3: if (!f->fail) f->data[f->bank * 65536u + a] &= v; f->state = 0; break;
    case 4: f->bank = v & 1; f->state = 0; break;
    case 5: f->state = a == 0x5555 && v == 0xaa ? 6 : 0; break;
    case 6: f->state = a == 0x2aaa && v == 0x55 ? 7 : 0; break;
    case 7:
        if (v == 0x30 && !f->fail) memset(f->data + f->bank * 65536u + a, 0xff, REMOTE_SAVE_SECTOR_SIZE);
        f->state = 0; break;
    default: assert(0);
    }
}
static void delay(void *ctx) { (void)ctx; }
static int fake_transfer(void *ctx, uint16_t tx, uint16_t *rx)
{
    struct RemoteLinkSlave *s = ctx;
    *rx = s->output;
    RemoteLinkSlaveReceive(s, tx);
    return 1;
}
int main(void)
{
    struct Fake f;
    struct RemoteFlash flash;
    struct RemoteFlashBus bus;
    struct RemoteSaveBackend b;
    struct RemoteSaveServer server;
    struct RemoteLinkSlave slave;
    struct RemoteLinkMaster master;
    struct RemoteSaveClient client;
    uint8_t data[4] = {0x12, 0x34, 0x56, 0x78}, result[4];
    memset(&f, 0, sizeof(f)); memset(f.data, 0xff, sizeof(f.data));
    f.maker = 0xc2; f.device = 0x09;
    bus.context = &f; bus.read = fake_read; bus.write = fake_write; bus.delay = delay;
    RemoteFlashInit(&flash, bus, 100);
    b = RemoteFlashBackend(&flash);
    assert(!b.program(b.context, 0, data, 4));
    assert(RemoteFlashIdentify(&flash));
    f.maker = 0x62; f.device = 0x13; assert(RemoteFlashIdentify(&flash));
    f.device = 0x12; assert(!RemoteFlashIdentify(&flash));
    f.device = 0x13; assert(RemoteFlashIdentify(&flash));
    assert(b.program(b.context, 0x10001, data, 4));
    assert(b.read(b.context, 0x10001, result, 4));
    assert(memcmp(data, result, 4) == 0 && f.data[1] == 0xff);
    assert(b.erase(b.context, 0x10000));
    assert(b.read(b.context, 0x10001, result, 4) && result[0] == 0xff && result[3] == 0xff);
    assert(!b.program(b.context, 0xfff, data, 4));
    assert(!b.erase(b.context, 1));
    RemoteSaveServerInit(&server, b); RemoteLinkSlaveInit(&slave, &server);
    master.context = &slave; master.transfer = fake_transfer; master.poll_limit = 1000;
    RemoteSaveClientInit(&client, &master, RemoteLinkExchange, 2);
    assert(RemoteSaveClientHello(&client));
    assert(RemoteSaveClientProgram(&client, 0x10001, data, 4));
    assert(RemoteSaveClientRead(&client, 0x10001, result, 4));
    assert(memcmp(data, result, 4) == 0);
    assert(RemoteSaveClientErase(&client, 0x10000));
    assert(RemoteSaveClientRead(&client, 0x10001, result, 4));
    assert(result[0] == 0xff && result[3] == 0xff);
    f.fail = 1; assert(!b.program(b.context, 0, data, 1));
    puts("remote flash driver tests passed"); return 0;
}
