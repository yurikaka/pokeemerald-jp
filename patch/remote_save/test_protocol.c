#include "protocol.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    uint8_t wire[REMOTE_SAVE_MAX_FRAME], copy[REMOTE_SAVE_MAX_FRAME];
    struct RemoteSaveFrame sent = {0}, received = {0};
    size_t n, i;
    assert(RemoteSaveCrc16((const uint8_t *)"123456789", 9) == 0x29b1);
    sent.command = REMOTE_SAVE_PROGRAM; sent.sequence = 0x3412;
    sent.offset = 0x01ff80; sent.length = 256;
    for (i = 0; i < sent.length; ++i) sent.payload[i] = (uint8_t)i;
    n = RemoteSaveEncode(wire, sizeof(wire), &sent);
    assert(n == sizeof(wire));
    assert(wire[0] == 0x52 && wire[1] == 1 && wire[2] == 3);
    assert(wire[3] == 0x12 && wire[4] == 0x34 && wire[5] == 0x80 && wire[6] == 0xff && wire[7] == 1);
    assert(RemoteSaveDecode(&received, wire, n));
    assert(received.command == sent.command && received.sequence == sent.sequence && received.offset == sent.offset);
    assert(received.length == sent.length && memcmp(received.payload, sent.payload, sent.length) == 0);
    assert(!RemoteSaveDecode(&received, wire, n - 1));
    memcpy(copy, wire, n); copy[20] ^= 1; assert(!RemoteSaveDecode(&received, copy, n));
    memcpy(copy, wire, n); copy[1] = 2; assert(!RemoteSaveDecode(&received, copy, n));
    assert(!RemoteSaveEncode(wire, n - 1, &sent));
    sent.length = 257; assert(!RemoteSaveEncode(wire, sizeof(wire), &sent));
    sent.length = 0; sent.offset = 0x1000000;
    assert(!RemoteSaveEncode(wire, sizeof(wire), &sent));
    sent.offset = 0x01ff80;
    sent.length = 0; n = RemoteSaveEncode(wire, sizeof(wire), &sent);
    assert(n == 12 && RemoteSaveDecode(&received, wire, n));
    puts("remote save protocol tests passed");
    return 0;
}
