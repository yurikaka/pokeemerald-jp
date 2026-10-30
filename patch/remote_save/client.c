#include "client.h"

void RemoteSaveClientInit(struct RemoteSaveClient *c, void *ctx, RemoteSaveExchange exchange, uint8_t retries)
{ c->context = ctx; c->exchange = exchange; c->sequence = 0; c->session = 0; c->retries = retries; c->failed = 0; }
static int request(struct RemoteSaveClient *c, struct RemoteSaveFrame *q, struct RemoteSaveFrame *r)
{
    uint8_t tx[REMOTE_SAVE_MAX_FRAME], rx[REMOTE_SAVE_MAX_FRAME];
    size_t n, received;
    unsigned attempt;
    if (!c || !c->exchange || c->failed) return 0;
    q->sequence = c->sequence;
    n = RemoteSaveEncode(tx, sizeof(tx), q);
    if (!n) return 0;
    for (attempt = 0; attempt <= c->retries; ++attempt) {
        received = c->exchange(c->context, tx, n, rx, sizeof(rx));
        if (received && RemoteSaveDecode(r, rx, received) && r->command == (uint8_t)(q->command | 0x80u) &&
            r->sequence == q->sequence && r->offset == q->offset && r->length >= 1) {
            ++c->sequence;
            if (r->payload[0] == REMOTE_STATUS_OK) return 1;
            c->failed = 1;
            return 0;
        }
    }
    /* Once a reply is lost, the remote write outcome is unknown. Do not continue. */
    c->failed = 1;
    return 0;
}
int RemoteSaveClientHello(struct RemoteSaveClient *c)
{
    struct RemoteSaveFrame q, r;
    q.command = REMOTE_SAVE_HELLO; q.offset = 0; q.length = 4;
    q.payload[0] = (uint8_t)c->session; q.payload[1] = (uint8_t)(c->session >> 8);
    q.payload[2] = (uint8_t)(c->session >> 16); q.payload[3] = (uint8_t)(c->session >> 24);
    return request(c, &q, &r) && r.length == 1;
}
int RemoteSaveClientStatus(struct RemoteSaveClient *c)
{
    struct RemoteSaveFrame q, r;
    int ok;
    q.command = REMOTE_SAVE_STATUS; q.offset = 0; q.length = 0;
    ok = request(c, &q, &r) && r.length == 5 &&
        r.payload[1] == (uint8_t)c->session && r.payload[2] == (uint8_t)(c->session >> 8) &&
        r.payload[3] == (uint8_t)(c->session >> 16) && r.payload[4] == (uint8_t)(c->session >> 24);
    if (!ok && c) c->failed = 1;
    return ok;
}
int RemoteSaveClientRead(struct RemoteSaveClient *c, uint32_t off, uint8_t *out, uint32_t len)
{
    struct RemoteSaveFrame q, r;
    uint32_t i;
    if (!out || off > REMOTE_SAVE_FLASH_SIZE || len > REMOTE_SAVE_FLASH_SIZE - off) return 0;
    while (len) {
        uint16_t n = (uint16_t)(len > 255 ? 255 : len);
        q.command = REMOTE_SAVE_READ; q.offset = off; q.length = 2;
        q.payload[0] = (uint8_t)n; q.payload[1] = (uint8_t)(n >> 8);
        if (!request(c, &q, &r) || r.length != n + 1u) { c->failed = 1; return 0; }
        for (i = 0; i < n; ++i) out[i] = r.payload[i + 1];
        out += n; off += n; len -= n;
    }
    return 1;
}
int RemoteSaveClientProgram(struct RemoteSaveClient *c, uint32_t off, const uint8_t *data, uint32_t len)
{
    struct RemoteSaveFrame q, r;
    uint32_t i;
    if (!data || off > REMOTE_SAVE_FLASH_SIZE || len > REMOTE_SAVE_FLASH_SIZE - off) return 0;
    while (len) {
        uint32_t room = REMOTE_SAVE_SECTOR_SIZE - off % REMOTE_SAVE_SECTOR_SIZE;
        uint16_t n = (uint16_t)(len > REMOTE_SAVE_MAX_PAYLOAD ? REMOTE_SAVE_MAX_PAYLOAD : len);
        if (n > room) n = (uint16_t)room;
        q.command = REMOTE_SAVE_PROGRAM; q.offset = off; q.length = n;
        for (i = 0; i < n; ++i) q.payload[i] = data[i];
        if (!request(c, &q, &r) || r.length != 1) { c->failed = 1; return 0; }
        data += n; off += n; len -= n;
    }
    return 1;
}
int RemoteSaveClientErase(struct RemoteSaveClient *c, uint32_t off)
{
    struct RemoteSaveFrame q, r;
    if (off >= REMOTE_SAVE_FLASH_SIZE || off % REMOTE_SAVE_SECTOR_SIZE) return 0;
    q.command = REMOTE_SAVE_ERASE_SECTOR; q.offset = off; q.length = 0;
    if (!request(c, &q, &r) || r.length != 1) { c->failed = 1; return 0; }
    return 1;
}
int RemoteSaveClientCommit(struct RemoteSaveClient *c)
{
    struct RemoteSaveFrame q, r;
    q.command=REMOTE_SAVE_COMMIT; q.offset=0; q.length=0;
    return request(c,&q,&r) && r.length==1;
}
