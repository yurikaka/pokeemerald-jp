#ifndef REMOTE_SAVE_PROTOCOL_H
#define REMOTE_SAVE_PROTOCOL_H

#include <stddef.h>
#include <stdint.h>

/* Wire order is little-endian, independent of the host compiler. */
#define REMOTE_SAVE_VERSION 1u
#define REMOTE_SAVE_MAX_PAYLOAD 256u
#define REMOTE_SAVE_HEADER_SIZE 10u
#define REMOTE_SAVE_CRC_SIZE 2u
#define REMOTE_SAVE_MAX_FRAME (REMOTE_SAVE_HEADER_SIZE + REMOTE_SAVE_MAX_PAYLOAD + REMOTE_SAVE_CRC_SIZE)

/* Requests and responses use the same sequence. A response has bit 7 set. */
enum RemoteSaveCommand {
    REMOTE_SAVE_HELLO = 1,
    REMOTE_SAVE_READ = 2,
    REMOTE_SAVE_PROGRAM = 3,
    REMOTE_SAVE_ERASE_SECTOR = 4,
    REMOTE_SAVE_STATUS = 5,
    REMOTE_SAVE_DISCONNECT = 6,
    REMOTE_SAVE_COMMIT = 7
};

struct RemoteSaveFrame {
    uint8_t command;
    uint16_t sequence;
    uint32_t offset;
    uint16_t length;
    uint8_t payload[REMOTE_SAVE_MAX_PAYLOAD];
};

/* CRC-16/CCITT-FALSE: polynomial 0x1021, initial 0xffff. */
uint16_t RemoteSaveCrc16(const uint8_t *data, size_t length);
size_t RemoteSaveEncode(uint8_t *output, size_t capacity, const struct RemoteSaveFrame *frame);
/* Requires one complete frame, with no trailing bytes. Returns 1 on success. */
int RemoteSaveDecode(struct RemoteSaveFrame *frame, const uint8_t *input, size_t length);

#endif
