#ifndef REMOTE_SAVE_LINK_H
#define REMOTE_SAVE_LINK_H
#include "client.h"
#include "stream.h"
#define REMOTE_LINK_READY 0x0200u
#define REMOTE_LINK_SYNC 0x0400u
#define REMOTE_LINK_POLL 0x0500u
#define REMOTE_LINK_BYTE 0x0100u
#define REMOTE_LINK_RESPONSE 0x0300u
struct RemoteLinkSlave {
    struct RemoteSaveServer *server;
    struct RemoteSaveStream stream;
    struct RemoteSaveFrame frame;
    uint8_t response[REMOTE_SAVE_MAX_FRAME];
    size_t response_length, response_pos;
    uint16_t output;
};
void RemoteLinkSlaveInit(struct RemoteLinkSlave *, struct RemoteSaveServer *);
/* Called after a complete transfer; its result is preloaded for the next one. */
uint16_t RemoteLinkSlaveReceive(struct RemoteLinkSlave *, uint16_t);
typedef int (*RemoteLinkTransfer)(void *, uint16_t, uint16_t *);
struct RemoteLinkMaster { void *context; RemoteLinkTransfer transfer; uint32_t poll_limit; };
size_t RemoteLinkExchange(void *, const uint8_t *, size_t, uint8_t *, size_t);
#endif
