#ifndef REMOTE_SAVE_JP_CONNECT_H
#define REMOTE_SAVE_JP_CONNECT_H
#include "multiboot.h"
enum RemoteConnectResult { REMOTE_CONNECT_WAITING, REMOTE_CONNECT_LOADED, REMOTE_CONNECT_FAILED };
enum RemoteConnectError { REMOTE_ERROR_START, REMOTE_ERROR_WAIT, REMOTE_ERROR_TRANSFER,
    REMOTE_ERROR_HANDSHAKE, REMOTE_ERROR_READ, REMOTE_ERROR_INVALID_SAVE, REMOTE_ERROR_RESTORE,
    REMOTE_ERROR_WAIT_NOT_READY, REMOTE_ERROR_WAIT_NO_REPLY, REMOTE_ERROR_WAIT_BAD_REPLY,
    REMOTE_ERROR_WAIT_UNSTABLE, REMOTE_ERROR_SIO_00, REMOTE_ERROR_SIO_04,
    REMOTE_ERROR_SIO_0C, REMOTE_ERROR_SIO_MODE, REMOTE_ERROR_TRANSFER_TIMEOUT,
    REMOTE_ERROR_TRANSFER_LOST, REMOTE_ERROR_TRANSFER_PROTOCOL };
struct RemoteConnect {
    struct RemoteBoot boot;
    uint32_t original_flash_present;
    uint32_t original_callback, original_vblank;
    uint16_t original_rcnt, original_siocnt, original_send;
    uint16_t original_ie;
    uint16_t ready_frames;
    uint8_t error;
    uint8_t started;
};
int RemoteJpConnectStart(struct RemoteConnect *);
enum RemoteConnectResult RemoteJpConnectTick(struct RemoteConnect *);
int RemoteJpConnectCancel(struct RemoteConnect *);
#endif
