#ifndef REMOTE_SAVE_GAME_H
#define REMOTE_SAVE_GAME_H
#include "client.h"
/* A sector is one 4 KiB Flash erase unit, not one logical save section. */
#define REMOTE_GAME_SECTORS 32u
int RemoteGameRead(struct RemoteSaveClient *, uint16_t, uint32_t, uint8_t *, uint32_t);
int RemoteGameErase(struct RemoteSaveClient *, uint16_t);
int RemoteGameProgramByte(struct RemoteSaveClient *, uint16_t, uint32_t, uint8_t);
int RemoteGameProgramSector(struct RemoteSaveClient *, uint16_t, const uint8_t *);
#endif
