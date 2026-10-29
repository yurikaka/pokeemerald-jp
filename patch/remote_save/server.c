#include "server.h"

/* The receiver overrides this to recheck its cartridge before each operation. */
__attribute__((weak)) int RemoteSaveValidatePeer(void) { return 1; }
static int equal_bytes(const uint8_t *a, const uint8_t *b, size_t n)
{
    size_t i;
    for (i = 0; i < n; ++i) if (a[i] != b[i]) return 0;
    return 1;
}
static void copy_bytes(uint8_t *d, const uint8_t *s, size_t n)
{
    size_t i;
    for (i = 0; i < n; ++i) d[i] = s[i];
}
void RemoteSaveServerInit(struct RemoteSaveServer *s, struct RemoteSaveBackend b)
{
    s->backend = b; s->has_last = 0; s->last_request_length = 0; s->last_response_length = 0;
}
size_t RemoteSaveServerHandle(struct RemoteSaveServer *s, const uint8_t *wire, size_t len,
                              uint8_t *out, size_t cap)
{
    struct RemoteSaveFrame req, reply;
    uint16_t count;
    size_t n;
    int status = REMOTE_STATUS_BAD_REQUEST;
    if (!s || !out || cap < REMOTE_SAVE_MAX_FRAME || !RemoteSaveDecode(&req, wire, len) ||
        (req.command & 0x80u)) return 0;
    /* A restarted or replacement receiver must never accept an old session's
     * first read or mutation. Only a fresh sequence-zero HELLO opens it. */
    if (!s->has_last && (req.command != REMOTE_SAVE_HELLO || req.sequence != 0 ||
                         req.length != 4 || req.offset != 0)) {
        reply.command = req.command | 0x80u; reply.sequence = req.sequence;
        reply.offset = req.offset; reply.length = 1;
        reply.payload[0] = REMOTE_STATUS_SEQUENCE_CONFLICT;
        return RemoteSaveEncode(out, cap, &reply);
    }
    if (s->has_last && req.sequence == s->last_sequence) {
        if (len == s->last_request_length && equal_bytes(wire, s->last_request, len)) {
            copy_bytes(out, s->last_response, s->last_response_length);
            return s->last_response_length;
        }
        reply.command = req.command | 0x80u; reply.sequence = req.sequence;
        reply.offset = req.offset; reply.length = 1;
        reply.payload[0] = REMOTE_STATUS_SEQUENCE_CONFLICT;
        return RemoteSaveEncode(out, cap, &reply);
    }
    if (s->has_last && req.sequence != (uint16_t)(s->last_sequence + 1u)) {
        reply.command = req.command | 0x80u; reply.sequence = req.sequence;
        reply.offset = req.offset; reply.length = 1;
        reply.payload[0] = REMOTE_STATUS_SEQUENCE_CONFLICT;
        return RemoteSaveEncode(out, cap, &reply);
    }
    reply.command = req.command | 0x80u; reply.sequence = req.sequence;
    reply.offset = req.offset; reply.length = 1;
    switch (req.command) {
    case REMOTE_SAVE_HELLO:
        if (req.length == 4 && req.offset == 0) {
            s->session = (uint32_t)req.payload[0] | ((uint32_t)req.payload[1] << 8) |
                ((uint32_t)req.payload[2] << 16) | ((uint32_t)req.payload[3] << 24);
            status = REMOTE_STATUS_OK;
        }
        break;
    case REMOTE_SAVE_STATUS:
        if (req.length == 0 && req.offset == 0 && RemoteSaveValidatePeer()) {
            status = REMOTE_STATUS_OK; reply.length = 5;
            reply.payload[1] = (uint8_t)s->session;
            reply.payload[2] = (uint8_t)(s->session >> 8);
            reply.payload[3] = (uint8_t)(s->session >> 16);
            reply.payload[4] = (uint8_t)(s->session >> 24);
        }
        else if (req.length == 0 && req.offset == 0) status = REMOTE_STATUS_IO_ERROR;
        break;
    case REMOTE_SAVE_DISCONNECT:
        if (req.length == 0 && req.offset == 0) status = REMOTE_STATUS_OK;
        break;
    case REMOTE_SAVE_READ:
        if (req.length != 2) break;
        count = (uint16_t)(req.payload[0] | ((uint16_t)req.payload[1] << 8));
        /* One response byte is reserved for status. */
        if (!count || count > REMOTE_SAVE_MAX_PAYLOAD - 1 || req.offset >= REMOTE_SAVE_FLASH_SIZE ||
            count > REMOTE_SAVE_FLASH_SIZE - req.offset) break;
        status = s->backend.read && s->backend.read(s->backend.context, req.offset, reply.payload + 1, count)
                 ? REMOTE_STATUS_OK : REMOTE_STATUS_IO_ERROR;
        if (status == REMOTE_STATUS_OK) reply.length = (uint16_t)(count + 1);
        break;
    case REMOTE_SAVE_PROGRAM:
        if (!req.length || req.offset >= REMOTE_SAVE_FLASH_SIZE ||
            req.length > REMOTE_SAVE_FLASH_SIZE - req.offset ||
            req.length > REMOTE_SAVE_SECTOR_SIZE - (req.offset % REMOTE_SAVE_SECTOR_SIZE)) break;
        status = RemoteSaveValidatePeer() && s->backend.program && s->backend.program(s->backend.context, req.offset, req.payload, req.length)
                 ? REMOTE_STATUS_OK : REMOTE_STATUS_IO_ERROR;
        break;
    case REMOTE_SAVE_ERASE_SECTOR:
        if (req.length || req.offset >= REMOTE_SAVE_FLASH_SIZE || req.offset % REMOTE_SAVE_SECTOR_SIZE) break;
        status = RemoteSaveValidatePeer() && s->backend.erase && s->backend.erase(s->backend.context, req.offset)
                 ? REMOTE_STATUS_OK : REMOTE_STATUS_IO_ERROR;
        break;
    default: break;
    }
    reply.payload[0] = (uint8_t)status;
    n = RemoteSaveEncode(out, cap, &reply);
    if (!n) return 0;
    copy_bytes(s->last_request, wire, len); s->last_request_length = len;
    copy_bytes(s->last_response, out, n); s->last_response_length = n;
    s->last_sequence = req.sequence; s->has_last = 1;
    return n;
}
