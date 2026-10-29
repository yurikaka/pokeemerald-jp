#include <assert.h>
#include <string.h>
#include <stdio.h>
#include "bulk.h"
static unsigned reads, completed, corrupt;
static uint8_t memory[REMOTE_SAVE_FLASH_SIZE];
static int readflash(void *c, uint32_t off, uint8_t *dst, uint16_t n) { (void)c; ++reads; memcpy(dst,memory+off,n); return 1; }
struct wire { struct RemoteBulkSlave slave; uint16_t output; };
static int exchange(void *c, uint16_t tx, uint16_t *rx) {
 struct wire *w=c; int done; uint16_t next; *rx=w->output;
 if (corrupt && tx==(BULK_WORD|25)) { *rx^=1; corrupt=0; }
 assert(RemoteBulkSlaveReceive(&w->slave,tx,&next,&done)); w->output=next; completed+=(unsigned)done; return 1;
}
int main(void) {
 struct wire w; struct RemoteSaveBackend b={0,readflash,0,0}; uint8_t out[4096]; unsigned i;
 for(i=0;i<sizeof(memory);i++) memory[i]=(uint8_t)(i*37u+(i>>16));
 memory[16*4096+50]=255; memory[16*4096+51]=255;
 RemoteBulkSlaveInit(&w.slave,b); w.output=REMOTE_LINK_READY;
 assert(RemoteBulkRead(exchange,&w,0,out,20)); assert(!memcmp(out,memory,4096));
 corrupt=1; assert(RemoteBulkRead(exchange,&w,16,out,20)); assert(!memcmp(out,memory+16*4096,4096));
 assert(reads==3 && completed==2); assert(!RemoteBulkRead(exchange,&w,32,out,20));
 puts("bulk: both banks, FFFF, CRC retry and bounds passed");
}
