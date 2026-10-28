#ifndef REMOTE_SAVE_JP_BINDINGS_H
#define REMOTE_SAVE_JP_BINDINGS_H
#include "multiboot.h"
#include "gba_link.h"
/* These bindings are for the unmodified JP Emerald revision with SHA-1
 * d7cf8f156ba9c455d164e1ea780a6bf1945465c2. */
struct RemoteBootOps RemoteJpMultiBootOps(void);
void RemoteJpLinkInit(struct RemoteLinkMaster *);
int RemoteJpBootStart(struct RemoteBoot *);
#endif
