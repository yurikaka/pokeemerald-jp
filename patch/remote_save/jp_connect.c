#include "jp_connect.h"
#include "jp_bindings.h"
#include "jp_save.h"
#define FLASH_PRESENT (*(volatile uint32_t *)0x03005ae8u)
#define SAVE_FILE_STATUS (*(volatile uint16_t *)0x03005f50u)
#define SIOCNT (*(volatile uint16_t *)0x04000128u)
#define SIOMLT_SEND (*(volatile uint16_t *)0x0400012au)
#define RCNT (*(volatile uint16_t *)0x04000134u)
#define SIOMULTI1 (*(volatile uint16_t *)0x04000122u)
#define JP_RESET_SAVE_COUNTERS ((void (*)(void))0x0815265du)
#define JP_LOAD_GAME_SAVE ((uint8_t (*)(uint8_t))0x0815340du)
int RemoteJpConnectStart(struct RemoteConnect *c)
{
    if (!c) return 0;
    c->error = RemoteJpSaveActive() ? REMOTE_ERROR_RESTORE : REMOTE_ERROR_START;
    if (RemoteJpSaveActive()) return 0;
    c->original_flash_present = FLASH_PRESENT;
    c->original_rcnt = RCNT; c->original_siocnt = SIOCNT; c->original_send = SIOMLT_SEND;
    c->ready_frames = 0; c->error = REMOTE_ERROR_START;
    c->started = RemoteJpBootStart(&c->boot) ? 1 : 0;
    return c->started;
}
int RemoteJpConnectCancel(struct RemoteConnect *c)
{
    if (!c || !c->started) return 0;
    c->started = 0;
    if (RemoteJpSaveActive()) {
        if (!RemoteJpSaveRestoreLocal(c->original_flash_present)) { c->error = REMOTE_ERROR_RESTORE; return 0; }
        JP_RESET_SAVE_COUNTERS();
        (void)JP_LOAD_GAME_SAVE(0);
    }
    SIOCNT = c->original_siocnt; SIOMLT_SEND = c->original_send; RCNT = c->original_rcnt;
    return 1;
}
enum RemoteConnectResult RemoteJpConnectTick(struct RemoteConnect *c)
{
    enum RemoteBootStatus boot_status, previous;
    if (!c || !c->started) return REMOTE_CONNECT_FAILED;
    previous = c->boot.status;
    boot_status = RemoteBootTick(&c->boot);
    if (boot_status == REMOTE_BOOT_WAITING || boot_status == REMOTE_BOOT_SENDING) return REMOTE_CONNECT_WAITING;
    if (boot_status != REMOTE_BOOT_COMPLETE) {
        if (previous == REMOTE_BOOT_SENDING) {
            if (c->boot.error_reason == REMOTE_BOOT_ERROR_TIMEOUT) c->error = REMOTE_ERROR_TRANSFER_TIMEOUT;
            else if (c->boot.error_reason == REMOTE_BOOT_ERROR_PROTOCOL) c->error = REMOTE_ERROR_TRANSFER_PROTOCOL;
            else c->error = REMOTE_ERROR_TRANSFER_LOST;
        }
        else if ((SIOCNT & 0x3000u) != 0x2000u) c->error = REMOTE_ERROR_SIO_MODE;
        else if ((SIOCNT & 0x000cu) == 0) c->error = REMOTE_ERROR_SIO_00;
        else if ((SIOCNT & 0x000cu) == 4) c->error = REMOTE_ERROR_SIO_04;
        else if ((SIOCNT & 0x000cu) == 12) c->error = REMOTE_ERROR_SIO_0C;
        else if (SIOMULTI1 == 0xffffu) c->error = REMOTE_ERROR_WAIT_NO_REPLY;
        else if ((c->boot.params.response_bit & 2u) && (c->boot.params.client_bit & 2u))
            c->error = REMOTE_ERROR_WAIT_UNSTABLE;
        else c->error = REMOTE_ERROR_WAIT_BAD_REPLY;
        (void)RemoteJpConnectCancel(c);
        return REMOTE_CONNECT_FAILED;
    }
    /* Give the remote image time to identify its Flash after BIOS transfer. */
    if (++c->ready_frames < 30) return REMOTE_CONNECT_WAITING;
    c->ready_frames = 0;
    if (!RemoteJpSaveBegin()) {
        c->error = REMOTE_ERROR_HANDSHAKE;
        (void)RemoteJpConnectCancel(c);
        return REMOTE_CONNECT_FAILED;
    }
    JP_RESET_SAVE_COUNTERS();
    (void)JP_LOAD_GAME_SAVE(0);
    if (RemoteJpSaveFailed() || SAVE_FILE_STATUS != 1) {
        c->error = RemoteJpSaveFailed() ? REMOTE_ERROR_READ : REMOTE_ERROR_INVALID_SAVE;
        (void)RemoteJpConnectCancel(c);
        return REMOTE_CONNECT_FAILED;
    }
    c->started = 0;
    return REMOTE_CONNECT_LOADED;
}
