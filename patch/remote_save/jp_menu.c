#include "jp_save.h"
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
#define SET_VBLANK ((void (*)(void *))0x080006f1u)
#define STOP_SCANLINE ((void (*)(void))0x080b9711u)
#define RESET_TASKS ((void (*)(void))0x080a8819u)
#define CREATE_TASK ((uint8_t (*)(TaskFunc, uint8_t))0x080a8879u)
#define SET_CALLBACK ((void (*)(void (*)(void)))0x08000541u)
extern const uint8_t ChsRemoteMenuConnect[];
static void RemoteMenuInput(uint8_t);
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
        if (type >= 2 && !task->data[10]) {
            CHANGE_BG_Y(0, 0x2000, 1); CHANGE_BG_Y(1, 0x2000, 1);
            task->data[10] = 1;
        }
        ORIG_HIGHLIGHT((uint8_t)type, 0, task->data[14]);
        SET_GPU(0x44, type == 0 ? 0x415f : 0x819f);
    } else {
        if (task->data[10]) {
            CHANGE_BG_Y(0, 0x2000, 2); CHANGE_BG_Y(1, 0x2000, 2);
            task->data[10] = 0;
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
        /* Match the setup normally performed before berry_fix_main runs. */
        DISABLE_IRQ(0xffffu);
        ENABLE_IRQ(1);
        SOUND_OFF();
        SET_VBLANK(0);
        RESET_TASKS();
        STOP_SCANLINE();
        berry_id = CREATE_TASK(RemoteOfficialSenderCopy, 0);
        TASKS[berry_id].data[0] = 4;
        SET_CALLBACK((void (*)(void))0x081bf0b1u);
    } else if (ORIG_INPUT(id)) task->func = RemoteMenuHighlight;
}
