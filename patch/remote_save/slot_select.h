#ifndef REMOTE_SAVE_SLOT_SELECT_H
#define REMOTE_SAVE_SLOT_SELECT_H
#include <stdint.h>
/* Returns whether all 14 sector IDs and native checksums are valid. */
int RemoteSlotValidate(const uint8_t *slot, unsigned slot_number, uint32_t *counter);
/* -1 if neither is valid; otherwise the number of the newest valid slot. */
int RemoteSlotChoose(int valid0, uint32_t counter0, int valid1, uint32_t counter1);
#endif
