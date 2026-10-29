#ifndef REMOTE_SLOT_STREAM_H
#define REMOTE_SLOT_STREAM_H
#include "link.h"
#define SLOT_BYTES (14u * 4096u)
#define SLOT_START 0xa710u
#define SLOT_NEXT 0xa711u
#define SLOT_END 0xa712u
#define SLOT_POLL 0xa713u
#define SLOT_ACK 0xa714u
#define SLOT_READY 0xd190u
#define SLOT_ERROR 0xd19fu
struct RemoteSlotStream {
    const uint8_t *data;
    uint32_t position;
    uint16_t crc;
    uint8_t active;
};
void RemoteSlotStreamInit(struct RemoteSlotStream *, const uint8_t *);
int RemoteSlotStreamReceive(struct RemoteSlotStream *, uint16_t, uint16_t *, unsigned *);
int RemoteSlotStreamRead(RemoteLinkTransfer, void *, uint8_t *, void (*)(unsigned));
#endif
