#include "link.h"
#ifndef REMOTE_LINK_MASTER_ONLY
void RemoteLinkSlaveInit(struct RemoteLinkSlave *s, struct RemoteSaveServer *server)
{
    s->server = server; RemoteSaveStreamInit(&s->stream);
    s->response_length = 0; s->response_pos = 0; s->output = REMOTE_LINK_READY;
}
uint16_t RemoteLinkSlaveReceive(struct RemoteLinkSlave *s, uint16_t token)
{
    if (token == REMOTE_LINK_SYNC) {
        RemoteSaveStreamInit(&s->stream); s->response_length = 0; s->response_pos = 0;
        s->output = REMOTE_LINK_READY;
    } else if ((token & 0xff00u) == REMOTE_LINK_BYTE) {
        int state = RemoteSaveStreamPush(&s->stream, (uint8_t)token, &s->frame);
        s->output = REMOTE_LINK_READY;
        if (state == 1) {
            uint8_t request[REMOTE_SAVE_MAX_FRAME];
            size_t len = RemoteSaveEncode(request, sizeof(request), &s->frame);
            s->response_length = RemoteSaveServerHandle(s->server, request, len,
                                                         s->response, sizeof(s->response));
            s->response_pos = 0;
            if (s->response_length) s->output = REMOTE_LINK_RESPONSE | s->response[s->response_pos++];
        }
    } else if (token == REMOTE_LINK_POLL) {
        if (s->response_pos < s->response_length)
            s->output = REMOTE_LINK_RESPONSE | s->response[s->response_pos++];
        else s->output = REMOTE_LINK_READY;
    }
    return s->output;
}
#endif
size_t RemoteLinkExchange(void *context, const uint8_t *in, size_t n, uint8_t *out, size_t cap)
{
    struct RemoteLinkMaster *m = context;
    size_t i, used = 0, expected = 0;
    uint32_t tries;
    uint16_t rx;
    if (!m || !m->transfer || !in || !out || n > REMOTE_SAVE_MAX_FRAME || cap < REMOTE_SAVE_MAX_FRAME) return 0;
    if (!m->transfer(m->context, REMOTE_LINK_SYNC, &rx)) return 0;
    for (tries = 0; tries < m->poll_limit; ++tries) {
        if (!m->transfer(m->context, REMOTE_LINK_POLL, &rx)) return 0;
        if (rx == REMOTE_LINK_READY) break;
    }
    if (tries == m->poll_limit) return 0;
    for (i = 0; i < n; ++i)
        if (!m->transfer(m->context, REMOTE_LINK_BYTE | in[i], &rx)) return 0;
    for (tries = 0; tries < m->poll_limit; ++tries) {
        if (!m->transfer(m->context, REMOTE_LINK_POLL, &rx)) return 0;
        if ((rx & 0xff00u) != REMOTE_LINK_RESPONSE) continue;
        if (used >= cap) return 0;
        out[used++] = (uint8_t)rx;
        if (used == REMOTE_SAVE_HEADER_SIZE) {
            expected = REMOTE_SAVE_HEADER_SIZE + ((size_t)out[8] | ((size_t)out[9] << 8)) + 2;
            if (expected > cap) return 0;
        }
        if (expected && used == expected) return used;
    }
    return 0;
}
