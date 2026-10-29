#include "game.h"
#include "link.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
struct Harness { struct RemoteLinkSlave link; uint8_t flash[REMOTE_SAVE_FLASH_SIZE]; int corrupt_once; };
static int read_data(void *p, uint32_t off, uint8_t *dst, uint16_t len)
{ struct Harness *h=p; memcpy(dst,h->flash+off,len); return 1; }
static int transfer(void *p, uint16_t tx, uint16_t *rx)
{
    struct Harness *h=p;
    *rx=h->link.output;
    if (h->corrupt_once && *rx==0x0352u && h->link.server->last_request[2]==REMOTE_SAVE_READ) {
        *rx=0x0301u; h->corrupt_once=0;
    }
    (void)RemoteLinkSlaveReceive(&h->link,tx); return 1;
}
int main(void)
{
    static struct Harness h;
    static struct RemoteSaveServer server;
    struct RemoteSaveBackend backend={&h,read_data,0,0};
    struct RemoteLinkMaster master={&h,transfer,1000};
    struct RemoteSaveClient client;
    uint8_t sector[REMOTE_SAVE_SECTOR_SIZE];
    unsigned i, id;
    for(i=0;i<sizeof(h.flash);i++) h.flash[i]=(uint8_t)((i*13u)^(i>>8));
    RemoteSaveServerInit(&server,backend);RemoteLinkSlaveInit(&h.link,&server);
    RemoteSaveClientInit(&client,&master,RemoteLinkExchange,3);client.session=0x12345678;
    assert(RemoteSaveClientHello(&client));assert(RemoteSaveClientStatus(&client));
    h.corrupt_once=1;
    for(id=0;id<32;id++) {
        assert(RemoteGameRead(&client,(uint16_t)id,0,sector,sizeof(sector)));
        assert(memcmp(sector,h.flash+id*4096u,sizeof(sector))==0);
    }
    assert(!h.corrupt_once); /* read recovered from a deliberately corrupt frame */
    assert(!RemoteSaveClientErase(&client,0));
    for(i=0;i<sizeof(h.flash);i++) assert(h.flash[i]==(uint8_t)((i*13u)^(i>>8)));
    puts("read-only transfer across both Flash banks passed");return 0;
}
