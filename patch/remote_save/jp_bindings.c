#include "jp_bindings.h"
extern const uint8_t RemoteReceiverImageStart[], RemoteReceiverImageEnd[];
struct RemoteBootOps RemoteJpMultiBootOps(void)
{
    struct RemoteBootOps ops;
    ops.init = (void (*)(struct RemoteMultiBootParam *))0x081ba36du;
    ops.step = (int (*)(struct RemoteMultiBootParam *))0x081ba3a9u;
    ops.start = (void (*)(struct RemoteMultiBootParam *, const uint8_t *, int, uint8_t, int8_t))0x081ba809u;
    ops.complete = (int (*)(struct RemoteMultiBootParam *))0x081ba8cdu;
    return ops;
}
void RemoteJpLinkInit(struct RemoteLinkMaster *master)
{
    RemoteGbaLinkMasterInit();
    master->context = 0;
    master->transfer = RemoteGbaLinkTransfer;
    /* Allow time for Flash erase, but bound a missing or unresponsive peer. */
    master->poll_limit = 6000u;
}
int RemoteJpBootStart(struct RemoteBoot *boot)
{
    uint32_t size = (uint32_t)(RemoteReceiverImageEnd - RemoteReceiverImageStart);
    return RemoteBootStart(boot, RemoteJpMultiBootOps(), RemoteReceiverImageStart, size);
}
