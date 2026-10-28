#ifndef REMOTE_SAVE_GBA_FLASH_H
#define REMOTE_SAVE_GBA_FLASH_H
#include "flash.h"
/* The linked cartridge must be JP Emerald (BPEJ) with supported 1 Mbit Flash.
 * Must execute entirely from GBA RAM, not the cartridge. */
int RemoteGbaFlashOpen(struct RemoteFlash *);
#endif
