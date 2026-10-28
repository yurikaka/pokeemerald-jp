#include "multiboot.h"
#include <assert.h>
#include <stdio.h>
static unsigned calls, started, finished, disconnect, protocol_error;
static const uint8_t *source;
static void init(struct RemoteMultiBootParam *p) { p->probe_count=0; p->client_bit=0; }
static int step(struct RemoteMultiBootParam *p) { ++calls; p->client_bit=disconnect ? 0 : 2; p->response_bit=2; return protocol_error ? 0x70 : 0; }
static void start(struct RemoteMultiBootParam *p, const uint8_t *data, int n, uint8_t color, int8_t speed)
{ assert(data == source + 0xc0 && n == 0x100 && color == 4 && speed == 1); p->probe_count=0xd0; ++started; }
static int complete(struct RemoteMultiBootParam *p) { (void)p; return finished; }
int main(void)
{
 static uint8_t image[0x1c0]; struct RemoteBoot b;
 struct RemoteBootOps ops={init,step,start,complete}; unsigned i;
 source=image; assert(!RemoteBootStart(&b,ops,image,0x1bf));
 assert(RemoteBootStart(&b,ops,image,sizeof(image)));
 assert(RemoteBootTick(&b)==REMOTE_BOOT_WAITING);
 for(i=0;i<180;++i) assert(RemoteBootTick(&b)==REMOTE_BOOT_WAITING);
 assert(RemoteBootTick(&b)==REMOTE_BOOT_SENDING && started==1);
 finished=1; assert(RemoteBootTick(&b)==REMOTE_BOOT_COMPLETE);
 assert(RemoteBootTick(&b)==REMOTE_BOOT_COMPLETE);
 assert(RemoteBootStart(&b,ops,image,sizeof(image)));
 b.elapsed_frames = 899;
 assert(RemoteBootTick(&b)==REMOTE_BOOT_ERROR);
 assert(b.error_reason == REMOTE_BOOT_ERROR_TIMEOUT);
 assert(RemoteBootStart(&b,ops,image,sizeof(image)));
 b.status = REMOTE_BOOT_SENDING; disconnect = 1; finished = 0;
 assert(RemoteBootTick(&b)==REMOTE_BOOT_ERROR && b.error_reason == REMOTE_BOOT_ERROR_LOST);
 assert(RemoteBootStart(&b,ops,image,sizeof(image)));
 b.status = REMOTE_BOOT_SENDING; protocol_error = 1;
 assert(RemoteBootTick(&b)==REMOTE_BOOT_ERROR && b.error_reason == REMOTE_BOOT_ERROR_PROTOCOL);
 puts("remote multiboot controller tests passed"); return 0;
}
