#include "stream.h"
void RemoteSaveStreamInit(struct RemoteSaveStream *s) { s->used = 0; }
int RemoteSaveStreamPush(struct RemoteSaveStream *s, uint8_t byte, struct RemoteSaveFrame *frame)
{
    size_t payload, expected;
    int ok;
    if (!s || !frame) return -1;
    if (!s->used && byte != 0x52) return 0;
    if (s->used == 1 && byte != REMOTE_SAVE_VERSION) {
        s->used = byte == 0x52 ? 1 : 0;
        if (s->used) s->buffer[0] = byte;
        return -1;
    }
    if (s->used >= sizeof(s->buffer)) { s->used = 0; return -1; }
    s->buffer[s->used++] = byte;
    if (s->used < REMOTE_SAVE_HEADER_SIZE) return 0;
    payload = (size_t)s->buffer[8] | ((size_t)s->buffer[9] << 8);
    if (payload > REMOTE_SAVE_MAX_PAYLOAD) { s->used = 0; return -1; }
    expected = REMOTE_SAVE_HEADER_SIZE + payload + REMOTE_SAVE_CRC_SIZE;
    if (s->used < expected) return 0;
    ok = RemoteSaveDecode(frame, s->buffer, s->used);
    s->used = 0;
    return ok ? 1 : -1;
}
