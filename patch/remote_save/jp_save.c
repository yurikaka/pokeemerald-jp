#include "jp_save.h"
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
#define SESSION_TOKEN (*(volatile uint32_t *)0x030075fcu)
#define REG_IME (*(volatile uint16_t *)0x04000208u)
#define FLASH_TYPE (*(volatile uint32_t *)0x030075f0u)
#define FLASH_PRESENT (*(volatile uint32_t *)0x03005ae8u)
static void prepare(struct RemoteSaveClient *client, struct RemoteLinkMaster *link)
{
    RemoteJpLinkInit(link);
    RemoteSaveClientInit(client, link, RemoteLinkExchange, 0);
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
    RemoteSaveClientInit(&client, &link, RemoteLinkExchange, 0);
    client.session = (*(volatile uint32_t *)0x03005ae0u ^
                      *(volatile uint32_t *)0x02024664u ^
                      *(volatile uint16_t *)0x04000006u ^ 0x524d5341u);
    if (!RemoteSaveClientHello(&client)) return 0;
    ime = REG_IME; REG_IME = 0;
    PROGRAM_BYTE = (uint32_t)(uintptr_t)&RemoteJpProgramByte;
    PROGRAM_SECTOR = (uint32_t)(uintptr_t)&RemoteJpProgramSector;
    ERASE_SECTOR = (uint32_t)(uintptr_t)&RemoteJpErase;
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
    PROGRAM_BYTE = setup[0]; PROGRAM_SECTOR = setup[1]; SESSION_TOKEN = setup[2]; ERASE_SECTOR = setup[3];
    REMOTE_STATE = 0; FLASH_PRESENT = original_flash_present;
    REG_IME = ime;
    return 1;
}
int RemoteJpRead(uint16_t sector, uint32_t offset, uint8_t *dest, uint32_t length)
{
    struct RemoteSaveClient client; struct RemoteLinkMaster link; int ok;
    if (!RemoteJpSaveActive()) return 0;
    prepare(&client, &link); ok = RemoteSaveClientStatus(&client) && RemoteGameRead(&client, sector, offset, dest, length); finish(&client, ok);
    if (!ok && dest) { uint32_t i; for (i = 0; i < length; ++i) dest[i] = 0xff; }
    return ok;
}
uint16_t RemoteJpErase(uint16_t sector)
{
    struct RemoteSaveClient client; struct RemoteLinkMaster link; int ok;
    if (!RemoteJpSaveActive()) return 0x80ffu;
    prepare(&client, &link); ok = RemoteSaveClientStatus(&client) && RemoteGameErase(&client, sector); finish(&client, ok);
    return ok ? 0 : 0x80ffu;
}
uint16_t RemoteJpProgramByte(uint16_t sector, uint32_t offset, uint8_t data)
{
    struct RemoteSaveClient client; struct RemoteLinkMaster link; int ok;
    if (!RemoteJpSaveActive()) return 0x80ffu;
    prepare(&client, &link); ok = RemoteSaveClientStatus(&client) && RemoteGameProgramByte(&client, sector, offset, data); finish(&client, ok);
    return ok ? 0 : 0x80ffu;
}
uint16_t RemoteJpProgramSector(uint16_t sector, const uint8_t *data)
{
    struct RemoteSaveClient client; struct RemoteLinkMaster link; int ok;
    if (!RemoteJpSaveActive()) return 0x80ffu;
    prepare(&client, &link); ok = RemoteSaveClientStatus(&client) && RemoteGameProgramSector(&client, sector, data); finish(&client, ok);
    return ok ? 0 : 0x80ffu;
}
