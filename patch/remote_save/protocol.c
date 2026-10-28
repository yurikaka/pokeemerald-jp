#include "protocol.h"

uint16_t RemoteSaveCrc16(const uint8_t *data, size_t length)
{
    uint16_t crc = 0xffffu;
    size_t i;
    unsigned bit;
    for (i = 0; i < length; ++i) {
        crc ^= (uint16_t)data[i] << 8;
        for (bit = 0; bit < 8; ++bit)
            crc = (uint16_t)((crc & 0x8000u) ? (((uint32_t)crc << 1) ^ 0x1021u) : ((uint32_t)crc << 1));
    }
    return crc;
}

size_t RemoteSaveEncode(uint8_t *out, size_t capacity, const struct RemoteSaveFrame *frame)
{
    size_t i, total;
    uint16_t crc;
    if (!out || !frame || frame->length > REMOTE_SAVE_MAX_PAYLOAD || frame->offset > 0xffffffu)
        return 0;
    total = REMOTE_SAVE_HEADER_SIZE + frame->length + REMOTE_SAVE_CRC_SIZE;
    if (capacity < total) return 0;
    out[0] = 0x52; out[1] = REMOTE_SAVE_VERSION; out[2] = frame->command;
    out[3] = (uint8_t)frame->sequence; out[4] = (uint8_t)(frame->sequence >> 8);
    out[5] = (uint8_t)frame->offset; out[6] = (uint8_t)(frame->offset >> 8);
    out[7] = (uint8_t)(frame->offset >> 16);
    out[8] = (uint8_t)frame->length; out[9] = (uint8_t)(frame->length >> 8);
    for (i = 0; i < frame->length; ++i) out[REMOTE_SAVE_HEADER_SIZE + i] = frame->payload[i];
    crc = RemoteSaveCrc16(out, total - 2);
    out[total - 2] = (uint8_t)crc; out[total - 1] = (uint8_t)(crc >> 8);
    return total;
}

int RemoteSaveDecode(struct RemoteSaveFrame *frame, const uint8_t *in, size_t length)
{
    size_t i, payload;
    uint16_t crc;
    if (!frame || !in || length < REMOTE_SAVE_HEADER_SIZE + REMOTE_SAVE_CRC_SIZE ||
        in[0] != 0x52 || in[1] != REMOTE_SAVE_VERSION) return 0;
    payload = (size_t)in[8] | ((size_t)in[9] << 8);
    if (payload > REMOTE_SAVE_MAX_PAYLOAD || length != REMOTE_SAVE_HEADER_SIZE + payload + 2) return 0;
    crc = RemoteSaveCrc16(in, length - 2);
    if (in[length - 2] != (uint8_t)crc || in[length - 1] != (uint8_t)(crc >> 8)) return 0;
    frame->command = in[2]; frame->sequence = (uint16_t)(in[3] | ((uint16_t)in[4] << 8));
    frame->offset = (uint32_t)in[5] | ((uint32_t)in[6] << 8) | ((uint32_t)in[7] << 16);
    frame->length = (uint16_t)payload;
    for (i = 0; i < payload; ++i) frame->payload[i] = in[REMOTE_SAVE_HEADER_SIZE + i];
    return 1;
}
