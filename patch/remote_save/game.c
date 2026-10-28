#include "game.h"
int RemoteGameRead(struct RemoteSaveClient *c, uint16_t sector, uint32_t offset, uint8_t *dest, uint32_t size)
{
    if (!c || !dest || sector >= REMOTE_GAME_SECTORS || offset > REMOTE_SAVE_SECTOR_SIZE ||
        size > REMOTE_SAVE_SECTOR_SIZE - offset) return 0;
    return RemoteSaveClientRead(c, (uint32_t)sector * REMOTE_SAVE_SECTOR_SIZE + offset, dest, size);
}
int RemoteGameErase(struct RemoteSaveClient *c, uint16_t sector)
{
    if (!c || sector >= REMOTE_GAME_SECTORS) return 0;
    return RemoteSaveClientErase(c, (uint32_t)sector * REMOTE_SAVE_SECTOR_SIZE);
}
int RemoteGameProgramByte(struct RemoteSaveClient *c, uint16_t sector, uint32_t offset, uint8_t data)
{
    if (!c || sector >= REMOTE_GAME_SECTORS || offset >= REMOTE_SAVE_SECTOR_SIZE) return 0;
    return RemoteSaveClientProgram(c, (uint32_t)sector * REMOTE_SAVE_SECTOR_SIZE + offset, &data, 1);
}
int RemoteGameProgramSector(struct RemoteSaveClient *c, uint16_t sector, const uint8_t *data)
{
    uint8_t verify[128];
    uint32_t offset, i;
    if (!c || !data || sector >= REMOTE_GAME_SECTORS) return 0;
    if (!RemoteGameErase(c, sector) ||
        !RemoteSaveClientProgram(c, (uint32_t)sector * REMOTE_SAVE_SECTOR_SIZE, data, REMOTE_SAVE_SECTOR_SIZE)) return 0;
    for (offset = 0; offset < REMOTE_SAVE_SECTOR_SIZE; offset += sizeof(verify)) {
        if (!RemoteGameRead(c, sector, offset, verify, sizeof(verify))) return 0;
        for (i = 0; i < sizeof(verify); ++i)
            if (verify[i] != data[offset + i]) { c->failed = 1; return 0; }
    }
    return 1;
}
