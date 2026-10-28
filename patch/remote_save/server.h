#ifndef REMOTE_SAVE_SERVER_H
#define REMOTE_SAVE_SERVER_H
#include "protocol.h"

#define REMOTE_SAVE_FLASH_SIZE 131072u
#define REMOTE_SAVE_SECTOR_SIZE 4096u

enum RemoteSaveStatus {
    REMOTE_STATUS_OK = 0,
    REMOTE_STATUS_BAD_REQUEST = 1,
    REMOTE_STATUS_IO_ERROR = 2,
    REMOTE_STATUS_SEQUENCE_CONFLICT = 3
};

struct RemoteSaveBackend {
    void *context;
    int (*read)(void *, uint32_t, uint8_t *, uint16_t);
    int (*program)(void *, uint32_t, const uint8_t *, uint16_t);
    int (*erase)(void *, uint32_t);
};

/* Cache the previous response so a lost reply never repeats a flash mutation. */
struct RemoteSaveServer {
    struct RemoteSaveBackend backend;
    uint8_t last_request[REMOTE_SAVE_MAX_FRAME];
    uint8_t last_response[REMOTE_SAVE_MAX_FRAME];
    size_t last_request_length, last_response_length;
    uint16_t last_sequence;
    uint32_t session;
    uint8_t has_last;
};

void RemoteSaveServerInit(struct RemoteSaveServer *, struct RemoteSaveBackend);
size_t RemoteSaveServerHandle(struct RemoteSaveServer *, const uint8_t *, size_t,
                              uint8_t *, size_t);
#endif
