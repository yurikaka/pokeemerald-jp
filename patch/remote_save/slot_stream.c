#include "slot_stream.h"
#include "protocol.h"
#ifndef SLOT_STREAM_MASTER_ONLY
void RemoteSlotStreamInit(struct RemoteSlotStream *s, const uint8_t *data)
{
    s->data=data; s->position=0; s->active=0;
    s->crc=data ? RemoteSaveCrc16(data,SLOT_BYTES) : 0;
}
int RemoteSlotStreamReceive(struct RemoteSlotStream *s, uint16_t word, uint16_t *out, unsigned *progress)
{
    *progress=0;
    if(word==SLOT_START) {
        s->active=1; s->position=0;
        *out=s->data ? SLOT_READY : SLOT_ERROR;
        return 1;
    }
    if(!s->active) return 0;
    if(word==SLOT_POLL) { *out=s->data ? SLOT_READY : SLOT_ERROR; return 1; }
    if(word==SLOT_NEXT) {
        if(!s->data || s->position>=SLOT_BYTES) { *out=SLOT_ERROR; return 1; }
        *out=(uint16_t)(s->data[s->position] | ((uint16_t)s->data[s->position+1]<<8));
        s->position+=2;
        if ((s->position & 4095u)==0) *progress=s->position/4096u;
        return 1;
    }
    if(word==SLOT_END) { *out=s->position==SLOT_BYTES ? s->crc : SLOT_ERROR; return 1; }
    if(word==SLOT_ACK) { s->active=0; *out=REMOTE_LINK_READY; return 1; }
    return 0;
}
#endif
int RemoteSlotStreamRead(RemoteLinkTransfer transfer, void *context, uint8_t *dest, void (*progress)(unsigned))
{
    unsigned attempt, n, i; uint16_t rx, crc;
    if (!transfer || !dest) return 0;
    for(attempt=0;attempt<3;attempt++) {
        if(!transfer(context,SLOT_START,&rx)) continue;
        for(n=0;n<512;n++) {
            if(!transfer(context,SLOT_POLL,&rx)) break;
            if(rx==SLOT_READY || rx==SLOT_ERROR) break;
        }
        if(n==512 || rx!=SLOT_READY) continue;
        if(!transfer(context,SLOT_NEXT,&rx)) continue;
        for(i=1;i<SLOT_BYTES/2;i++) {
            if(!transfer(context,SLOT_NEXT,&rx)) break;
            dest[2*i-2]=(uint8_t)rx; dest[2*i-1]=(uint8_t)(rx>>8);
            if(progress && (i & 2047u)==0) progress(i/2048u-1u);
        }
        if(i!=SLOT_BYTES/2 || !transfer(context,SLOT_END,&rx)) continue;
        dest[SLOT_BYTES-2]=(uint8_t)rx; dest[SLOT_BYTES-1]=(uint8_t)(rx>>8);
        if(progress) progress(13);
        if(!transfer(context,SLOT_POLL,&crc)) continue;
        if(crc!=RemoteSaveCrc16(dest,SLOT_BYTES)) continue;
        if(!transfer(context,SLOT_ACK,&rx)) continue;
        return 1;
    }
    return 0;
}
