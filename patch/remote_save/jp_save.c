#include "jp_save.h"
#include "bulk.h"
#include "connection_display.h"
#include "jp_bindings.h"
/* PollFlashStatus is used only by the local Flash driver. While remote mode is
 * active all Flash paths must be redirected before this word can be repurposed.
 * The game Flash entry points are redirected before this word is repurposed. */
#define REMOTE_STATE (*(volatile uint32_t *)0x030075e4u)
#define STATE_ACTIVE 0xa75d0000u
#define STATE_FAILED 0xa75e0000u
#define STATE_MASK 0xffff0000u
#define PROGRAM_BYTE (*(volatile uint32_t *)0x030075f4u)
#define PROGRAM_SECTOR (*(volatile uint32_t *)0x030075ecu)
#define ERASE_SECTOR (*(volatile uint32_t *)0x03007600u)
#define SESSION_TOKEN (*(volatile uint32_t *)0x030075f8u)
#define ERASE_CHIP (*(volatile uint32_t *)0x030075fcu)
#define REG_IME (*(volatile uint16_t *)0x04000208u)
/* During initial read-only load, WaitForFlashWrite is unused because writes
 * are blocked. The menu temporarily borrows it as a progress counter. */
#define LOAD_PROGRESS (*(volatile uint32_t *)0x030075e8u)
#define LOAD_PROGRESS_MAGIC 0x52500000u
#define LOAD_CACHE_MAGIC 0x52600000u
/* JP gHeap is 0x1c000 bytes, exactly the two normal save slots.
 * Borrow its first 56 KiB only while loading: game code later uses it. */
#define LOAD_CACHE ((const uint8_t *)0x02000000u)
#define LOAD_CACHE_SECTORS 14u
#define FLASH_TYPE (*(volatile uint32_t *)0x030075f0u)
#define FLASH_PRESENT (*(volatile uint32_t *)0x03005ae8u)
static void prepare(struct RemoteSaveClient *client, struct RemoteLinkMaster *link)
{
    RemoteJpLinkInit(link);
    RemoteSaveClientInit(client, link, RemoteLinkExchange, 3);
    client->sequence = (uint16_t)REMOTE_STATE;
    client->session = SESSION_TOKEN;
    client->failed = (REMOTE_STATE & STATE_MASK) == STATE_FAILED;
}
static void finish(struct RemoteSaveClient *client, int ok)
{
    REMOTE_STATE = (ok && !client->failed ? STATE_ACTIVE : STATE_FAILED) | client->sequence;
}
int RemoteJpSaveActive(void)
{
    uint32_t state = REMOTE_STATE & STATE_MASK;
    return state == STATE_ACTIVE || state == STATE_FAILED;
}
int RemoteJpSaveFailed(void) { return (REMOTE_STATE & STATE_MASK) == STATE_FAILED; }
int RemoteJpSaveBegin(void)
{
    struct RemoteSaveClient client;
    struct RemoteLinkMaster link;
    uint16_t ime;
    RemoteJpLinkInit(&link);
    RemoteSaveClientInit(&client, &link, RemoteLinkExchange, 3);
    client.session = (*(volatile uint32_t *)0x03005ae0u ^
                      *(volatile uint32_t *)0x02024664u ^
                      *(volatile uint16_t *)0x04000006u ^ 0x524d5341u);
    if (!RemoteSaveClientHello(&client)) return 0;
    ime = REG_IME; REG_IME = 0;
    PROGRAM_BYTE = (uint32_t)(uintptr_t)&RemoteJpProgramByte;
    PROGRAM_SECTOR = (uint32_t)(uintptr_t)&RemoteJpProgramSector;
    ERASE_SECTOR = (uint32_t)(uintptr_t)&RemoteJpErase;
    ERASE_CHIP = (uint32_t)(uintptr_t)&RemoteJpEraseChip;
    SESSION_TOKEN = client.session;
    FLASH_PRESENT = 1;
    REMOTE_STATE = STATE_ACTIVE | client.sequence;
    REG_IME = ime;
    return 1;
}
int RemoteJpSaveRestoreLocal(uint32_t original_flash_present)
{
    const volatile uint32_t *setup;
    uint16_t ime;
    if (!RemoteJpSaveActive() || FLASH_TYPE < 0x08000018u || FLASH_TYPE >= 0x0a000000u) return 0;
    setup = (const volatile uint32_t *)(uintptr_t)(FLASH_TYPE - 0x18u);
    ime = REG_IME; REG_IME = 0;
    PROGRAM_BYTE = setup[0]; PROGRAM_SECTOR = setup[1]; ERASE_CHIP = setup[2]; ERASE_SECTOR = setup[3];
    REMOTE_STATE = 0; FLASH_PRESENT = original_flash_present;
    REG_IME = ime;
    return 1;
}
int RemoteJpRead(uint16_t sector, uint32_t offset, uint8_t *dest, uint32_t length)
{
    struct RemoteSaveClient client; struct RemoteLinkMaster link; int ok;
    if (!RemoteJpSaveActive()) return 0;
    if ((LOAD_PROGRESS & 0xffff0000u) == LOAD_CACHE_MAGIC && sector < 28u) {
        uint32_t i; unsigned slot=(unsigned)(LOAD_PROGRESS & 1u);
        if (!dest || offset > REMOTE_SAVE_SECTOR_SIZE || length > REMOTE_SAVE_SECTOR_SIZE - offset) return 0;
        for (i = 0; i < length; ++i)
            dest[i] = (sector >= LOAD_CACHE_SECTORS) == slot
                ? LOAD_CACHE[(uint32_t)(sector >= LOAD_CACHE_SECTORS ? sector - LOAD_CACHE_SECTORS : sector) * REMOTE_SAVE_SECTOR_SIZE + offset + i] : 0;
        return 1;
    }
    prepare(&client, &link); ok = RemoteSaveClientStatus(&client) &&
        (offset == 0 && length == REMOTE_SAVE_SECTOR_SIZE
         ? RemoteBulkRead(RemoteGbaLinkTransferRaw, 0, sector, dest, 512)
         : RemoteGameRead(&client, sector, offset, dest, length)); finish(&client, ok);
    if (ok && (LOAD_PROGRESS & 0xffff0000u) == LOAD_PROGRESS_MAGIC) {
        unsigned count=(unsigned)(LOAD_PROGRESS & 0xffffu);
        if (count < 42u) {
            RemoteDebugSectorProgress(count);
            LOAD_PROGRESS=LOAD_PROGRESS_MAGIC | (count+1u);
        }
    }
    /* The native loader indexes the sector ID before validating its signature.
     * A zero-filled failed read provides an in-range ID and invalid signature;
     * all-FF would make it index 0xffff and could crash before failure handling. */
    if (!ok && dest) { uint32_t i; for (i = 0; i < length; ++i) dest[i] = 0; }
    return ok;
}
/* Back up the OBJ resources touched by the temporary in-game overlay. */
struct OverlayHeapBlock {
    uint16_t used, magic;
    uint32_t size;
    struct OverlayHeapBlock *prev, *next;
};
static int SaveOverlayHeapHasRoom(uint32_t size)
{
    struct OverlayHeapBlock *head=*(struct OverlayHeapBlock **)0x03000004u, *p=head;
    unsigned n=0;
    if ((uintptr_t)head<0x02000000u || (uintptr_t)head>=0x0201c000u) return 0;
    do {
        if ((uintptr_t)p<0x02000000u || (uintptr_t)p>0x0201bff0u || p->magic!=0xa3a3u) return 0;
        if (!p->used && p->size>=size) return 1;
        p=p->next;
    } while (p!=head && ++n<1024u);
    return 0;
}
struct SaveOverlayBackup {
    uint16_t tiles[61u*16u];
    uint16_t oam[61u*3u];
    uint16_t color, display;
};
static struct SaveOverlayBackup *SaveOverlayBegin(unsigned completed)
{
    struct SaveOverlayBackup *b;
    volatile uint16_t *tiles=(volatile uint16_t *)0x06017600u;
    volatile uint16_t *oam=(volatile uint16_t *)0x07000000u;
    volatile uint16_t *io=(volatile uint16_t *)0x04000000u;
    unsigned i,j,wait;
    if (!SaveOverlayHeapHasRoom(sizeof(*b))) return 0;
    b=((void *(*)(uint32_t))0x08000bc9u)(sizeof(*b)); /* Alloc */
    if (!b) return 0;
    for(wait=0;wait<200000u && (io[3]<160u || io[3]>215u);wait++) {}
    for(i=0;i<61u*16u;i++) b->tiles[i]=tiles[i];
    for(i=0;i<61u;i++) for(j=0;j<3u;j++) b->oam[i*3u+j]=oam[(60u+i)*4u+j];
    b->color=*(volatile uint16_t *)0x050003e2u;
    b->display=io[0];
    RemoteDebugShow("HOST WRITE SAVE");
    *(volatile uint16_t *)0x050003e2u=0x001fu; /* Opaque red. */
    for(i=0;i<completed && i<14u;i++) RemoteDebugSectorProgress(i);
    return b;
}
static void SaveOverlayEnd(struct SaveOverlayBackup *b)
{
    volatile uint16_t *tiles=(volatile uint16_t *)0x06017600u;
    volatile uint16_t *oam=(volatile uint16_t *)0x07000000u;
    volatile uint16_t *io=(volatile uint16_t *)0x04000000u;
    unsigned i,j,wait;
    if (!b) return;
    for(wait=0;wait<200000u && (io[3]<160u || io[3]>215u);wait++) {}
    for(i=0;i<61u*16u;i++) tiles[i]=b->tiles[i];
    for(i=0;i<61u;i++) for(j=0;j<3u;j++) oam[(60u+i)*4u+j]=b->oam[i*3u+j];
    *(volatile uint16_t *)0x050003e2u=b->color;
    io[0]=(uint16_t)((io[0] & ~0x1080u) | (b->display & 0x1080u));
    ((void (*)(void *))0x08000bf1u)(b); /* Free */
}
extern int RemoteRecoveryActive(void);
/* Only whole sectors of the ordinary save slots may be written remotely. */
uint16_t RemoteJpErase(uint16_t sector)
{ (void)sector; return 0x80ffu; }
uint16_t RemoteJpEraseChip(void)
{ return 0x80ffu; }
uint16_t RemoteJpProgramByte(uint16_t sector, uint32_t offset, uint8_t data)
{ (void)sector; (void)offset; (void)data; return 0x80ffu; }
uint16_t RemoteJpProgramSector(uint16_t sector, const uint8_t *data)
{
    struct RemoteSaveClient client; struct RemoteLinkMaster link;
    uint16_t ime; int ok; unsigned id;
    struct SaveOverlayBackup *overlay=0;
    if (!RemoteJpSaveActive() || sector >= 28u || !data) return 0x80ffu;
    id=(unsigned)data[0xff4u] | ((unsigned)data[0xff5u]<<8);
    ime=REG_IME; REG_IME=0;
    if (id<14u && data[0xff8u]==0x25u && data[0xff9u]==0x20u &&
        data[0xffau]==0x01u && data[0xffbu]==0x08u)
        overlay=SaveOverlayBegin(id);
    prepare(&client,&link);
    link.poll_limit=65536u; /* Flash erase/program may take substantially longer than reads. */
    ok=RemoteSaveClientStatus(&client) && RemoteGameProgramSector(&client,sector,data);
    finish(&client,ok);
    if (overlay && ok) RemoteDebugSectorProgress(id);
    SaveOverlayEnd(overlay);
    /* In recovery, the full-screen status stays visible between sectors. */
    if (ok && id<14u && RemoteRecoveryActive()) RemoteDebugSectorProgress(id);
    REG_IME=ime;
    return ok ? 0 : 0x80ffu;
}

int RemoteJpSaveCheck(void)
{
    struct RemoteSaveClient client; struct RemoteLinkMaster link; int ok;
    if (!RemoteJpSaveActive()) return 0;
    prepare(&client,&link);
    ok=RemoteSaveClientStatus(&client);
    finish(&client,ok);
    return ok;
}
int RemoteJpSaveCommit(void)
{
    struct RemoteSaveClient client; struct RemoteLinkMaster link; int ok;
    prepare(&client,&link);
    ok=RemoteSaveClientCommit(&client);
    finish(&client,ok);
    return ok;
}
extern void RemoteScheduleSaveRecovery(void);
extern uint8_t RemoteOriginalTrySavingData(uint8_t);
uint8_t RemoteTrySavingData(uint8_t type)
{
    volatile uint32_t *sound=*(volatile uint32_t **)0x03007ff0u;
    uint16_t ime, sound_l=0, sound_h=0; int muted=0, routed=0; uint8_t result;
    /* Check before the original routine changes counters or writes any sector. */
    if (type==0 && RemoteJpSaveActive() && !RemoteJpSaveCheck()) {
        RemoteScheduleSaveRecovery();
        return 0xffu;
    }
    if (RemoteJpSaveActive()) {
        ime=REG_IME; REG_IME=0;
        sound_l=*(volatile uint16_t *)0x04000080u;
        sound_h=*(volatile uint16_t *)0x04000082u;
        *(volatile uint16_t *)0x04000080u=(uint16_t)(sound_l & 0x00ffu);
        *(volatile uint16_t *)0x04000082u=(uint16_t)(sound_h & ~0x3300u);
        REG_IME=ime; routed=1;
    }
    if (RemoteJpSaveActive() && (uintptr_t)sound>=0x02000000u &&
        (uintptr_t)sound<0x03008000u &&
        (sound[0]==0x68736d53u || sound[0]==0x68736d54u)) {
        ime=REG_IME; REG_IME=0;
        ((void (*)(void))0x0828ecedu)();
        REG_IME=ime; muted=1;
    }
    result=RemoteOriginalTrySavingData(type);
    if (type==0 && result==1 && RemoteJpSaveActive() && !RemoteJpSaveCommit()) result=0xffu;
    /* A peer may also disappear after the preflight, while saving. The
     * original routine restores counters before returning on failure. */
    if (type==0 && result!=1 && RemoteJpSaveFailed())
        RemoteScheduleSaveRecovery();
    if (muted) {
        ime=REG_IME; REG_IME=0;
        ((void (*)(void))0x0828ed69u)();
        REG_IME=ime;
    }
    if (routed) {
        ime=REG_IME; REG_IME=0;
        *(volatile uint16_t *)0x04000080u=sound_l;
        *(volatile uint16_t *)0x04000082u=sound_h;
        REG_IME=ime;
    }
    return result;
}
