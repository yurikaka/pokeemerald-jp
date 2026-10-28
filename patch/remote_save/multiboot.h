#ifndef REMOTE_SAVE_MULTIBOOT_H
#define REMOTE_SAVE_MULTIBOOT_H
#include <stdint.h>
/* Layout from the JP game's gba/multiboot.h; pointers are 32-bit on GBA. */
struct RemoteMultiBootParam {
 uint32_t system_work[5]; uint8_t handshake_data, padding; uint16_t handshake_timeout;
 uint8_t probe_count, client_data[3], palette_data, response_bit, client_bit, reserved1;
 const uint8_t *boot_srcp, *boot_endp, *masterp; uint8_t *reserved2[3];
 uint32_t system_work2[4]; uint8_t sendflag, probe_target_bit, check_wait, server_type;
};
struct RemoteBootOps {
 void (*init)(struct RemoteMultiBootParam *);
 int (*step)(struct RemoteMultiBootParam *);
 void (*start)(struct RemoteMultiBootParam *, const uint8_t *, int, uint8_t, int8_t);
 int (*complete)(struct RemoteMultiBootParam *);
};
enum RemoteBootStatus { REMOTE_BOOT_WAITING, REMOTE_BOOT_SENDING, REMOTE_BOOT_COMPLETE, REMOTE_BOOT_ERROR };
struct RemoteBoot {
 struct RemoteMultiBootParam params;
 struct RemoteBootOps ops;
 const uint8_t *image;
 uint32_t size;
 uint16_t stable_frames, elapsed_frames;
 enum RemoteBootStatus status;
 uint8_t error_reason;
};
enum RemoteBootError { REMOTE_BOOT_ERROR_NONE, REMOTE_BOOT_ERROR_TIMEOUT, REMOTE_BOOT_ERROR_LOST, REMOTE_BOOT_ERROR_PROTOCOL };
int RemoteBootStart(struct RemoteBoot *, struct RemoteBootOps, const uint8_t *, uint32_t);
enum RemoteBootStatus RemoteBootTick(struct RemoteBoot *);
#endif
