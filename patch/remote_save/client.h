#ifndef REMOTE_SAVE_CLIENT_H
#define REMOTE_SAVE_CLIENT_H
#include "server.h"

/* Transport returns zero on timeout or error, otherwise response frame length. */
typedef size_t (*RemoteSaveExchange)(void *, const uint8_t *, size_t, uint8_t *, size_t);
struct RemoteSaveClient {
    void *context;
    RemoteSaveExchange exchange;
    uint16_t sequence;
    uint32_t session;
    uint8_t retries;
    uint8_t failed;
};
void RemoteSaveClientInit(struct RemoteSaveClient *, void *, RemoteSaveExchange, uint8_t);
int RemoteSaveClientHello(struct RemoteSaveClient *);
int RemoteSaveClientStatus(struct RemoteSaveClient *);
int RemoteSaveClientRead(struct RemoteSaveClient *, uint32_t, uint8_t *, uint32_t);
int RemoteSaveClientProgram(struct RemoteSaveClient *, uint32_t, const uint8_t *, uint32_t);
int RemoteSaveClientErase(struct RemoteSaveClient *, uint32_t);
#endif
