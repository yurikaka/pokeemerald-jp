#include "bulk.h"
#ifndef REMOTE_BULK_MASTER_ONLY
void RemoteBulkSlaveInit(struct RemoteBulkSlave *s, struct RemoteSaveBackend backend)
{
    s->backend = backend;
    s->valid = 0;
}
int RemoteBulkSlaveReceive(struct RemoteBulkSlave *s, uint16_t word, uint16_t *out, int *completed)
{
    unsigned i;
    *completed = 0;
    if ((word & 0xffe0u) == BULK_READ) {
        unsigned sector = word & 31u;
        s->valid = 0;
        if (s->backend.read && s->backend.read(s->backend.context,
                sector * REMOTE_SAVE_SECTOR_SIZE, s->data, REMOTE_SAVE_SECTOR_SIZE)) {
            s->crc = RemoteSaveCrc16(s->data, REMOTE_SAVE_SECTOR_SIZE);
            s->valid = 1;
        }
        *out = s->valid ? BULK_READY : BULK_ERROR;
        return 1;
    }
    if (word == BULK_STATUS) { *out = s->valid ? BULK_READY : BULK_ERROR; return 1; }
    if ((word & 0xf800u) == BULK_WORD) {
        i = (word & 0x07ffu) * 2u;
        *out = s->valid ? (uint16_t)(s->data[i] | ((uint16_t)s->data[i+1] << 8)) : BULK_ERROR;
        return 1;
    }
    if (word == BULK_CRC) { *out = s->valid ? s->crc : BULK_ERROR; return 1; }
    if (word == BULK_ACK) {
        *completed = s->valid;
        s->valid = 0;
        *out = REMOTE_LINK_READY;
        return 1;
    }
    return 0;
}
#endif
#ifndef REMOTE_BULK_SLAVE_ONLY
int RemoteBulkChoice(RemoteLinkTransfer transfer, void *context)
{
    uint16_t rx; unsigned i;
    if (!transfer) return -1;
    for (i=0;i<512;i++) {
        if (!transfer(context, BULK_CHOOSE, &rx)) return -1;
        if (rx == BULK_CHOICE_BASE || rx == BULK_CHOICE_BASE+1u) return rx-BULK_CHOICE_BASE;
        if (rx == BULK_CHOICE_ERROR) return -1;
    }
    return -1;
}
int RemoteBulkRead(RemoteLinkTransfer transfer, void *context, uint16_t sector, uint8_t *dest, unsigned polls)
{
    unsigned attempt, i, n;
    uint16_t rx, crc;
    if (!transfer || !dest || sector >= REMOTE_SAVE_FLASH_SIZE / REMOTE_SAVE_SECTOR_SIZE) return 0;
    for (attempt = 0; attempt < 3; ++attempt) {
        if (!transfer(context, (uint16_t)(BULK_READ | sector), &rx)) continue;
        for (n = 0; n < polls; ++n) {
            if (!transfer(context, BULK_STATUS, &rx)) break;
            if (rx == BULK_READY || rx == BULK_ERROR) break;
        }
        if (n == polls || rx != BULK_READY) continue;
        if (!transfer(context, BULK_WORD, &rx)) continue;
        for (i = 1; i < REMOTE_SAVE_SECTOR_SIZE / 2; ++i) {
            if (!transfer(context, (uint16_t)(BULK_WORD | i), &rx)) break;
            dest[2*i-2] = (uint8_t)rx; dest[2*i-1] = (uint8_t)(rx >> 8);
        }
        if (i != REMOTE_SAVE_SECTOR_SIZE / 2 || !transfer(context, BULK_CRC, &rx)) continue;
        dest[REMOTE_SAVE_SECTOR_SIZE-2] = (uint8_t)rx;
        dest[REMOTE_SAVE_SECTOR_SIZE-1] = (uint8_t)(rx >> 8);
        if (!transfer(context, BULK_STATUS, &crc)) continue;
        if (crc != RemoteSaveCrc16(dest, REMOTE_SAVE_SECTOR_SIZE)) continue;
        if (!transfer(context, BULK_ACK, &rx)) continue;
        return 1;
    }
    return 0;
}
#endif
