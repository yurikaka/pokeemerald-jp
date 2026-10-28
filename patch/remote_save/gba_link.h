#ifndef REMOTE_SAVE_GBA_LINK_H
#define REMOTE_SAVE_GBA_LINK_H
#include "link.h"
/* Initialise multiplayer mode after Multiboot has completed. */
void RemoteGbaLinkMasterInit(void);
int RemoteGbaLinkTransfer(void *, uint16_t, uint16_t *);
#endif
