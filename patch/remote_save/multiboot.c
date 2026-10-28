#include "multiboot.h"
#include <stddef.h>
#if UINTPTR_MAX == 0xffffffffu
typedef char CheckMultiBootMasterOffset[(offsetof(struct RemoteMultiBootParam, masterp) == 0x28) ? 1 : -1];
typedef char CheckMultiBootServerOffset[(offsetof(struct RemoteMultiBootParam, server_type) == 0x4b) ? 1 : -1];
#endif
int RemoteBootStart(struct RemoteBoot *b, struct RemoteBootOps ops, const uint8_t *image, uint32_t size)
{
 unsigned i; uint8_t *p;
 if (!b || !ops.init || !ops.step || !ops.start || !ops.complete || !image ||
     size < 0x1c0u || size > 0x400c0u || (size & 15u)) return 0;
 p = (uint8_t *)&b->params;
 for (i = 0; i < sizeof(b->params); ++i) p[i] = 0;
 b->ops = ops; b->image = image; b->size = size; b->stable_frames = 0;
 b->elapsed_frames = 0; b->status = REMOTE_BOOT_WAITING; b->error_reason = REMOTE_BOOT_ERROR_NONE;
 b->params.masterp = image; b->params.server_type = 0;
 b->ops.init(&b->params);
 return 1;
}
enum RemoteBootStatus RemoteBootTick(struct RemoteBoot *b)
{
 int step_result;
 if (!b) return REMOTE_BOOT_ERROR;
 if (b->status == REMOTE_BOOT_COMPLETE || b->status == REMOTE_BOOT_ERROR) return b->status;
 /* Avoid leaving the player on a static waiting screen indefinitely. */
 if (++b->elapsed_frames >= 900) { b->error_reason = REMOTE_BOOT_ERROR_TIMEOUT; b->status = REMOTE_BOOT_ERROR; return b->status; }
 if (b->status == REMOTE_BOOT_WAITING && b->params.probe_count == 0 &&
     (b->params.response_bit & 2u) && (b->params.client_bit & 2u)) {
     if (++b->stable_frames > 180) {
         b->ops.start(&b->params, b->image + 0xc0, (int)(b->size - 0xc0), 4, 1);
         b->status = REMOTE_BOOT_SENDING;
         return b->status;
     }
 } else if (b->status == REMOTE_BOOT_WAITING) b->stable_frames = 0;
 step_result = b->ops.step(&b->params);
 if (b->status == REMOTE_BOOT_SENDING) {
     if (b->ops.complete(&b->params)) b->status = REMOTE_BOOT_COMPLETE;
     else if (!(b->params.client_bit & 2u)) {
         b->error_reason = step_result ? REMOTE_BOOT_ERROR_PROTOCOL : REMOTE_BOOT_ERROR_LOST;
         b->status = REMOTE_BOOT_ERROR;
     }
 }
 return b->status;
}
