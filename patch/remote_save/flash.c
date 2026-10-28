#include "flash.h"

static void write_byte(struct RemoteFlash *f, uint16_t address, uint8_t value)
{ f->bus.write(f->bus.context, address, value); }
static uint8_t read_byte(struct RemoteFlash *f, uint16_t address)
{ return f->bus.read(f->bus.context, address); }
static void unlock(struct RemoteFlash *f)
{ write_byte(f, 0x5555, 0xaa); write_byte(f, 0x2aaa, 0x55); }
static void select_bank(struct RemoteFlash *f, uint32_t offset)
{ unlock(f); write_byte(f, 0x5555, 0xb0); write_byte(f, 0, (uint8_t)(offset >> 16)); }
static int poll(struct RemoteFlash *f, uint16_t address, uint8_t expected)
{
    uint32_t i;
    for (i = 0; i < f->poll_limit; ++i) {
        uint8_t value = read_byte(f, address);
        if (value == expected) return 1;
        if (value & 0x20u) {
            if (read_byte(f, address) == expected) return 1;
            break;
        }
    }
    write_byte(f, 0x5555, 0xf0);
    return 0;
}
void RemoteFlashInit(struct RemoteFlash *f, struct RemoteFlashBus bus, uint32_t limit)
{ f->bus = bus; f->identified = 0; f->poll_limit = limit; }
int RemoteFlashIdentify(struct RemoteFlash *f)
{
    uint8_t maker, device;
    if (!f || !f->bus.read || !f->bus.write || !f->bus.delay || !f->poll_limit) return 0;
    f->identified = 0;
    unlock(f); write_byte(f, 0x5555, 0x90); f->bus.delay(f->bus.context);
    maker = read_byte(f, 0); device = read_byte(f, 1);
    unlock(f); write_byte(f, 0x5555, 0xf0); write_byte(f, 0x5555, 0xf0); f->bus.delay(f->bus.context);
    /* JP Emerald selects the same routines for these two 128 KiB chips. */
    f->identified = (maker == 0xc2 && device == 0x09) ||
                    (maker == 0x62 && device == 0x13);
    return f->identified;
}
static int remote_read(void *context, uint32_t off, uint8_t *out, uint16_t n)
{
    struct RemoteFlash *f = context;
    uint32_t i, bank = 2;
    if (!f->identified || off >= REMOTE_SAVE_FLASH_SIZE || n > REMOTE_SAVE_FLASH_SIZE - off) return 0;
    for (i = 0; i < n; ++i) {
        uint32_t address = off + i;
        if ((address >> 16) != bank) { select_bank(f, address); bank = address >> 16; }
        out[i] = read_byte(f, (uint16_t)address);
    }
    return 1;
}
static int remote_program(void *context, uint32_t off, const uint8_t *data, uint16_t n)
{
    struct RemoteFlash *f = context;
    uint32_t i;
    if (!f->identified || !n || off >= REMOTE_SAVE_FLASH_SIZE || n > REMOTE_SAVE_FLASH_SIZE - off ||
        n > REMOTE_SAVE_SECTOR_SIZE - off % REMOTE_SAVE_SECTOR_SIZE) return 0;
    select_bank(f, off);
    for (i = 0; i < n; ++i) {
        uint16_t address = (uint16_t)(off + i);
        unlock(f); write_byte(f, 0x5555, 0xa0); write_byte(f, address, data[i]);
        if (!poll(f, address, data[i])) return 0;
    }
    for (i = 0; i < n; ++i) if (read_byte(f, (uint16_t)(off + i)) != data[i]) return 0;
    return 1;
}
static int remote_erase(void *context, uint32_t off)
{
    struct RemoteFlash *f = context;
    uint32_t i;
    uint16_t address;
    if (!f->identified || off >= REMOTE_SAVE_FLASH_SIZE || off % REMOTE_SAVE_SECTOR_SIZE) return 0;
    address = (uint16_t)off; select_bank(f, off);
    unlock(f); write_byte(f, 0x5555, 0x80); unlock(f); write_byte(f, address, 0x30);
    if (!poll(f, address, 0xff)) return 0;
    for (i = 0; i < REMOTE_SAVE_SECTOR_SIZE; ++i)
        if (read_byte(f, (uint16_t)(address + i)) != 0xff) return 0;
    return 1;
}
struct RemoteSaveBackend RemoteFlashBackend(struct RemoteFlash *f)
{
    struct RemoteSaveBackend b;
    b.context = f; b.read = remote_read; b.program = remote_program; b.erase = remote_erase;
    return b;
}
