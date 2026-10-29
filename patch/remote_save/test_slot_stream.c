#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "slot_stream.h"
static uint8_t src[SLOT_BYTES],dst[SLOT_BYTES];
struct Wire {struct RemoteSlotStream slave; uint16_t output; unsigned starts, corrupt, count, last;};
static int transfer(void *c,uint16_t tx,uint16_t *rx){struct Wire*w=c;unsigned p;uint16_t next;*rx=w->output;if(tx==SLOT_START)w->starts++;if(w->corrupt && tx==SLOT_NEXT && ++w->count==1234){*rx^=1;w->corrupt=0;}assert(RemoteSlotStreamReceive(&w->slave,tx,&next,&p));w->output=next;if(p)w->last=p;return 1;}
int main(void){struct Wire w={0};unsigned i;for(i=0;i<SLOT_BYTES;i++)src[i]=(uint8_t)(i*11+(i>>8));src[400]=src[401]=0xff;RemoteSlotStreamInit(&w.slave,src);w.output=REMOTE_LINK_READY;w.corrupt=1;assert(RemoteSlotStreamRead(transfer,&w,dst,0));assert(w.starts==2 && w.last==14);assert(!memcmp(src,dst,SLOT_BYTES));puts("56 KiB streaming, 0xffff and CRC retry passed");return 0;}
