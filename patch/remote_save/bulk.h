#ifndef REMOTE_SAVE_BULK_H
#define REMOTE_SAVE_BULK_H
#include "link.h"
#include "server.h"
#define BULK_READ 0xa600u
#define BULK_STATUS 0xa700u
#define BULK_CRC 0xa701u
#define BULK_ACK 0xa702u
#define BULK_READY 0xd17eu
#define BULK_ERROR 0xd1eeu
#define BULK_WORD 0x8000u
#define BULK_CHOOSE 0xa703u
#define BULK_CHOICE_BASE 0xd180u
#define BULK_CHOICE_ERROR 0xd18fu
struct RemoteBulkSlave {
    struct RemoteSaveBackend backend;
    uint8_t data[REMOTE_SAVE_SECTOR_SIZE];
    uint16_t crc;
    uint8_t valid;
};
void RemoteBulkSlaveInit(struct RemoteBulkSlave *, struct RemoteSaveBackend);
int RemoteBulkSlaveReceive(struct RemoteBulkSlave *, uint16_t, uint16_t *, int *);
int RemoteBulkChoice(RemoteLinkTransfer, void *);
int RemoteBulkRead(RemoteLinkTransfer, void *, uint16_t, uint8_t *, unsigned);
#endif
