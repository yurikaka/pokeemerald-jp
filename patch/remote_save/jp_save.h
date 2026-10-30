#ifndef REMOTE_SAVE_JP_SAVE_H
#define REMOTE_SAVE_JP_SAVE_H
#include "game.h"
int RemoteJpSaveBegin(void);
int RemoteJpSaveCheck(void);
int RemoteJpSaveCommit(void);
int RemoteJpSaveActive(void);
int RemoteJpSaveFailed(void);
int RemoteJpSaveRestoreLocal(uint32_t original_flash_present);
int RemoteJpRead(uint16_t sector, uint32_t offset, uint8_t *dest, uint32_t length);
uint16_t RemoteJpErase(uint16_t sector);
uint16_t RemoteJpEraseChip(void);
uint16_t RemoteJpProgramByte(uint16_t sector, uint32_t offset, uint8_t data);
uint16_t RemoteJpProgramSector(uint16_t sector, const uint8_t *data);
#endif
