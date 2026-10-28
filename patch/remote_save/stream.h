#ifndef REMOTE_SAVE_STREAM_H
#define REMOTE_SAVE_STREAM_H
#include "protocol.h"
/* A bounded stream parser, for transports which deliver one byte at a time. */
struct RemoteSaveStream {
    uint8_t buffer[REMOTE_SAVE_MAX_FRAME];
    size_t used;
};
void RemoteSaveStreamInit(struct RemoteSaveStream *);
/* Returns 1 for a complete frame, 0 while waiting, -1 for a malformed frame. */
int RemoteSaveStreamPush(struct RemoteSaveStream *, uint8_t, struct RemoteSaveFrame *);
#endif
