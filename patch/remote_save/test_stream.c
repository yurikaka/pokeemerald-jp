#include "stream.h"
#include <assert.h>
#include <stdio.h>
int main(void)
{
 struct RemoteSaveStream s; struct RemoteSaveFrame q = {0}, r;
 uint8_t data[REMOTE_SAVE_MAX_FRAME]; size_t n, i;
 RemoteSaveStreamInit(&s); assert(RemoteSaveStreamPush(&s, 0xff, &r) == 0);
 q.command = REMOTE_SAVE_PROGRAM; q.sequence = 42; q.offset = 0x10001; q.length = 256;
 for (i = 0; i < 256; ++i) q.payload[i] = (uint8_t)i;
 n = RemoteSaveEncode(data, sizeof(data), &q); assert(n == sizeof(data));
 for (i = 0; i < n - 1; ++i) assert(RemoteSaveStreamPush(&s, data[i], &r) == 0);
 assert(RemoteSaveStreamPush(&s, data[n-1], &r) == 1 && r.sequence == 42 && r.payload[255] == 255);
 data[20] ^= 1;
 for (i = 0; i < n - 1; ++i) assert(RemoteSaveStreamPush(&s, data[i], &r) == 0);
 assert(RemoteSaveStreamPush(&s, data[n-1], &r) == -1);
 data[20] ^= 1;
 for (i = 0; i < n - 1; ++i) assert(RemoteSaveStreamPush(&s, data[i], &r) == 0);
 assert(RemoteSaveStreamPush(&s, data[n-1], &r) == 1);
 puts("remote save stream tests passed"); return 0;
}
