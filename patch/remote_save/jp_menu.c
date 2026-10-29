#include "jp_save.h"
#include "gba_link.h"
#include "connection_display.h"
#include "slot_select.h"
#include "bulk.h"
#include "slot_stream.h"
#include <stddef.h>

typedef void (*TaskFunc)(uint8_t);
struct JpTask { TaskFunc func; uint8_t active, prev, next, priority; int16_t data[16]; };
struct JpWindow { uint8_t bg, left, top, width, height, palette; uint16_t base; };
#if UINTPTR_MAX == 0xffffffffu
typedef char CheckTaskSize[(sizeof(struct JpTask) == 40) ? 1 : -1];
#endif
#define TASKS ((volatile struct JpTask *)0x03005b60u)
#define KEYS (*(volatile uint16_t *)0x0300238eu)
#define ADD_WINDOW ((uint16_t (*)(const struct JpWindow *))0x08003251u)
#define FILL_WINDOW ((void (*)(uint8_t, uint8_t))0x08003b19u)
#define PUT_WINDOW ((void (*)(uint8_t))0x0800365du)
#define COPY_WINDOW ((void (*)(uint8_t, uint8_t))0x08003529u)
#define DRAW_BORDER ((void (*)(const struct JpWindow *, uint16_t))0x08031de5u)
#define PRINT_TEXT ((uint16_t (*)(uint8_t, uint8_t, uint8_t, uint8_t, const uint8_t *, int8_t, const uint8_t *))0x08199afdu)
#define CHANGE_BG_Y ((uint32_t (*)(uint8_t, int32_t, uint8_t))0x08001e95u)
#define SET_GPU ((void (*)(uint16_t, uint16_t))0x08001145u)
#define ORIG_HIGHLIGHT ((void (*)(uint8_t, uint8_t, int16_t))0x080303d9u)
#define ORIG_INPUT ((uint8_t (*)(uint8_t))0x0802fde1u)
#define PLAY_SE ((void (*)(uint16_t))0x080a306du)
#define HEADER_COLORS ((const uint8_t *)0x082d2970u)
extern void RemoteOfficialSenderCopy(uint8_t);
#define DISABLE_IRQ ((void (*)(uint16_t))0x080012a1u)
#define ENABLE_IRQ ((void (*)(uint16_t))0x08001275u)
#define SOUND_OFF ((void (*)(void))0x0828ecedu)
#define SOUND_ON ((void (*)(void))0x0828ed69u)
#define ENABLE_SOUND_VCOUNT ((void (*)(void))0x08000595u)
#define SET_VBLANK ((void (*)(void *))0x080006f1u)
#define STOP_SCANLINE ((void (*)(void))0x080b9711u)
#define RESET_TASKS ((void (*)(void))0x080a8819u)
#define CREATE_TASK ((uint8_t (*)(TaskFunc, uint8_t))0x080a8879u)
#define SET_CALLBACK ((void (*)(void (*)(void)))0x08000541u)
extern const uint8_t ChsRemoteMenuConnect[];
static void RemoteMenuInput(uint8_t);
int RemoteConnectionTick(volatile int16_t *phase);
static void print_window(uint8_t id, const uint8_t *text)
{
    FILL_WINDOW(id, 0xaa);
    (void)PRINT_TEXT(id, 1, 0, 2, HEADER_COLORS, -1, text);
    PUT_WINDOW(id); COPY_WINDOW(id, 3);
}
void RemoteMenuHighlight(uint8_t id)
{
    volatile struct JpTask *task = &TASKS[id];
    int16_t type = task->data[0], item = task->data[1];
    if (!RemoteJpSaveActive() && !task->data[11]) {
        struct JpWindow w;
        uint16_t window;
        w.bg = 0; w.left = 2; w.top = type == 0 ? 9 : (uint8_t)(5 + 4 * task->data[12]);
        w.width = 26; w.height = 2; w.palette = 15; w.base = 0x200;
        window = ADD_WINDOW(&w);
        if (window != 0xffu) {
            print_window((uint8_t)window, ChsRemoteMenuConnect);
            DRAW_BORDER(&w, 0x1d5);
            task->data[11] = (int16_t)(window + 1);
            ++task->data[12];
        }
    }
    if (task->data[11] && item == task->data[12] - 1) {
        int top = type == 0 ? 9 : 5 + 4 * item;
        int base_scroll = task->data[14] ? 4 : 0;
        int needed = top - base_scroll > 17 ? (top - base_scroll - 17 + 3) / 4 : 0;
        while (task->data[10] < needed) {
            CHANGE_BG_Y(0, 0x2000, 1); CHANGE_BG_Y(1, 0x2000, 1); ++task->data[10];
        }
        while (task->data[10] > needed) {
            CHANGE_BG_Y(0, 0x2000, 2); CHANGE_BG_Y(1, 0x2000, 2); --task->data[10];
        }
        top -= base_scroll + 4 * needed;
        ORIG_HIGHLIGHT((uint8_t)type, 0, task->data[14]);
        SET_GPU(0x44, (uint16_t)(((top * 8 - 7) << 8) | (top * 8 + 23)));
    } else {
        while (task->data[10] > 0) {
            CHANGE_BG_Y(0, 0x2000, 2); CHANGE_BG_Y(1, 0x2000, 2); --task->data[10];
        }
        ORIG_HIGHLIGHT((uint8_t)type, (uint8_t)item, task->data[14]);
    }
    task->func = RemoteMenuInput;
}
static void RemoteMenuInput(uint8_t id)
{
    volatile struct JpTask *task = &TASKS[id];
    if (task->data[11] && task->data[1] == task->data[12] - 1 && (KEYS & 1u)) {
        uint8_t berry_id;
        PLAY_SE(5);
        DISABLE_IRQ(0xffffu);
        ENABLE_IRQ(1);
        SOUND_OFF();
        SET_VBLANK(0);
        RESET_TASKS();
        STOP_SCANLINE();
        RemoteDebugShow("HOST START");
        berry_id = CREATE_TASK(RemoteOfficialSenderCopy, 0);
        TASKS[berry_id].data[0] = 4;
        SET_CALLBACK((void (*)(void))0x081bf0b1u);
    } else if (ORIG_INPUT(id)) task->func = RemoteMenuHighlight;
}

/* Poll a separate confirmation exchange after the official Multiboot handshake. */
int RemoteConnectionTick(volatile int16_t *phase)
{
    uint16_t rx;
    if (*phase == 0) { RemoteDebugShow("HOST WAIT PROBE"); RemoteGbaLinkMasterInit(); *phase = 1; return 0; }
    if (*phase == 1) {
        if (RemoteGbaLinkTransfer(0, LINK_PROBE, &rx) && (rx == LINK_READY || rx == LINK_ACK)) { *phase = 2; RemoteDebugShow("HOST WAIT CONFIRM"); }
    } else if (*phase == 2) {
        if (RemoteGbaLinkTransfer(0, LINK_CONFIRM, &rx) && rx == LINK_DONE) {
            RemoteDebugShow("HOST LINK OK");
            *phase = 3;
            return 1;
        }
    }
    return 0;
}

void RemoteDebugSending(void) { RemoteDebugShow("HOST SENDING"); }
void RemoteDebugBootComplete(void) { RemoteDebugShow("HOST BOOT OK"); }
void RemoteDebugBootFailed(const volatile int16_t *data)
{
    static const char hex[]="0123456789ABCDEF";
    uint32_t code=*(volatile uint32_t *)0x03006074u;
    unsigned phase=(uint16_t)data[2];
    volatile char text[17];
    const char *label="FAIL 00 PHASE 00";
    unsigned i;
    for (i=0;i<17;i++) text[i]=label[i];
    text[5]=hex[(code>>4)&15]; text[6]=hex[code&15];
    text[14]=hex[(phase>>4)&15]; text[15]=hex[phase&15];
    RemoteDebugShow((const char *)text);
}

int RemoteLoadTemporarySave(void)
{
    uint8_t status;
    int chosen;
    uint32_t counter;
    uint32_t oldWaitForFlashWrite;
    RemoteDebugShow("HOST READ SAVE");
    if (!RemoteJpSaveBegin()) { RemoteDebugShow("HOST LINK FAIL"); return 0; }
    ((void (*)(void))0x0815265du)(); /* Save_ResetSaveCounters */
    oldWaitForFlashWrite=*(volatile uint32_t *)0x030075e8u;
    *(volatile uint32_t *)0x030075e8u=0x52500000u;
    /* The guest validates both slots locally and retains a stable snapshot. */
    chosen=RemoteBulkChoice(RemoteGbaLinkTransferRaw, 0);
    if (chosen < 0) goto fail;
    if (!RemoteSlotStreamRead(RemoteGbaLinkTransferRaw, 0, (uint8_t *)0x02000000u,
                              RemoteDebugSectorProgress)) goto fail;
    /* Verify the whole received slot again before giving it to the game. */
    if (!RemoteSlotValidate((const uint8_t *)0x02000000u, (unsigned)chosen, &counter)) goto fail;
    *(volatile uint32_t *)0x030075e8u=0x52600000u | (unsigned)chosen;
    status=((uint8_t (*)(uint8_t))0x0815340du)(0); /* LoadGameSave(SAVE_NORMAL) */
    *(volatile uint32_t *)0x030075e8u=oldWaitForFlashWrite;
    ((void (*)(void *, uint32_t))0x08000badu)((void *)0x02000000u, 0x1c000u); /* InitHeap */
    if (RemoteJpSaveFailed() || status != 1) { RemoteDebugShow("HOST SAVE FAIL"); return 0; }
    RemoteDebugShow("HOST SAVE OK");
    ENABLE_SOUND_VCOUNT();
    SOUND_ON();
    RESET_TASKS();
    SET_CALLBACK((void (*)(void))0x0802f341u); /* CB2_InitMainMenu, no CPU reset */
    return 1;
fail:
    *(volatile uint32_t *)0x030075e8u=oldWaitForFlashWrite;
    ((void (*)(void *, uint32_t))0x08000badu)((void *)0x02000000u, 0x1c000u);
    RemoteDebugShow("HOST SAVE FAIL");
    return 0;
}
