#include "server.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
static uint8_t flash[REMOTE_SAVE_FLASH_SIZE];
static int writes, erases;
static int read_cb(void *ctx, uint32_t pos, uint8_t *out, uint16_t n)
{ (void)ctx; memcpy(out, flash + pos, n); return 1; }
static int write_cb(void *ctx, uint32_t pos, const uint8_t *in, uint16_t n)
{ (void)ctx; ++writes; memcpy(flash + pos, in, n); return 1; }
static int erase_cb(void *ctx, uint32_t pos)
{ (void)ctx; ++erases; memset(flash + pos, 0xff, REMOTE_SAVE_SECTOR_SIZE); return 1; }
static struct RemoteSaveServer server;
static struct RemoteSaveFrame req, reply;
static uint8_t in[REMOTE_SAVE_MAX_FRAME], out[REMOTE_SAVE_MAX_FRAME];
static void exchange(void)
{
 size_t n = RemoteSaveEncode(in, sizeof(in), &req);
 n = RemoteSaveServerHandle(&server, in, n, out, sizeof(out));
 assert(n && RemoteSaveDecode(&reply, out, n));
}
int main(void)
{
 struct RemoteSaveBackend b = {0, read_cb, write_cb, erase_cb};
 RemoteSaveServerInit(&server, b);
 req.command = REMOTE_SAVE_PROGRAM; req.sequence = 1; req.offset = 0x10001; req.length = 2;
 exchange(); assert(reply.payload[0] == REMOTE_STATUS_SEQUENCE_CONFLICT && writes == 0);
 req.command = REMOTE_SAVE_HELLO; req.sequence = 0; req.offset = 0; req.length = 4;
 exchange(); assert(reply.payload[0] == REMOTE_STATUS_OK);
 req.command = REMOTE_SAVE_PROGRAM; req.sequence = 1; req.offset = 0x10001; req.length = 2;
 req.payload[0] = 0x12; req.payload[1] = 0x34; exchange();
 assert(reply.payload[0] == REMOTE_STATUS_OK && writes == 1);
 exchange(); assert(reply.payload[0] == REMOTE_STATUS_OK && writes == 1);
 req.payload[0] = 0x99; exchange();
 assert(reply.payload[0] == REMOTE_STATUS_SEQUENCE_CONFLICT && writes == 1);
 req.command = REMOTE_SAVE_READ; req.sequence = 2; req.length = 2; req.payload[0] = 2; req.payload[1] = 0;
 exchange(); assert(reply.length == 3 && reply.payload[1] == 0x12 && reply.payload[2] == 0x34);
 req.sequence = 3; req.offset = REMOTE_SAVE_FLASH_SIZE - 1; exchange();
 assert(reply.payload[0] == REMOTE_STATUS_BAD_REQUEST);
 req.command = REMOTE_SAVE_ERASE_SECTOR; req.sequence = 4; req.offset = 0x10001; req.length = 0;
 exchange(); assert(reply.payload[0] == REMOTE_STATUS_BAD_REQUEST && erases == 0);
 req.sequence = 5; req.offset = 0x10000; exchange();
 assert(reply.payload[0] == REMOTE_STATUS_OK && erases == 1 && flash[0x10001] == 0xff);
 exchange(); assert(erases == 1);
 req.command = REMOTE_SAVE_PROGRAM; req.sequence = 6; req.offset = 0xfff; req.length = 2;
 exchange(); assert(reply.payload[0] == REMOTE_STATUS_BAD_REQUEST && writes == 1);
 req.command = REMOTE_SAVE_ERASE_SECTOR; req.sequence = 5; req.offset = 0x10000; req.length = 0;
 exchange(); assert(reply.payload[0] == REMOTE_STATUS_SEQUENCE_CONFLICT && erases == 1);
 puts("remote save server tests passed"); return 0;
}
