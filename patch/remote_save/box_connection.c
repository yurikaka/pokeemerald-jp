/* Box startup is retained; appended code implements a read-only Flash server. */
#include <stdint.h>
#include "connection_display.h"
#include "gba_flash.h"
#include "link.h"
#include "bulk.h"
#include "slot_select.h"
#include "slot_stream.h"
#define IO16(a) (*(volatile uint16_t *)(a))
#define SIOCNT IO16(0x04000128u)
#define SEND IO16(0x0400012au)
#define MULTI0 IO16(0x04000120u)
#define RCNT IO16(0x04000134u)
#define IF IO16(0x04000202u)
#define IME IO16(0x04000208u)
extern uint32_t __box_bss_start[], __box_bss_end[];
static struct RemoteFlash flash;
static struct RemoteSaveServer server;
static struct RemoteLinkSlave link;
static struct RemoteBulkSlave bulk;
static struct RemoteSlotStream slot_stream;
/* Snapshot both slots before choosing; subsequent sector reads use this copy. */
static uint8_t slots[2][14u * REMOTE_SAVE_SECTOR_SIZE];
static struct RemoteSaveBackend flash_backend;
static int selected_slot;
int RemoteSaveValidatePeer(void);
/* Normal save slots only. Update the snapshot only after real Flash succeeds. */
static int snapshot_program(void *context, uint32_t offset, const uint8_t *data, uint16_t length)
{
    uint32_t i; (void)context;
    if (offset >= sizeof(slots) || length > sizeof(slots)-offset ||
        !RemoteSaveValidatePeer() || !flash_backend.program ||
        !flash_backend.program(flash_backend.context,offset,data,length)) return 0;
    for (i=0;i<length;i++) ((uint8_t *)slots)[offset+i]=data[i];
    return 1;
}
static int snapshot_erase(void *context, uint32_t offset)
{
    uint32_t i; (void)context;
    if (offset >= sizeof(slots) || offset % REMOTE_SAVE_SECTOR_SIZE ||
        !RemoteSaveValidatePeer() || !flash_backend.erase ||
        !flash_backend.erase(flash_backend.context,offset)) return 0;
    for (i=0;i<REMOTE_SAVE_SECTOR_SIZE;i++) ((uint8_t *)slots)[offset+i]=0xffu;
    return 1;
}
static int snapshot_read(void *context, uint32_t offset, uint8_t *dest, uint16_t length)
{
    uint32_t i; (void)context;
    if (offset < sizeof(slots) && length <= sizeof(slots)-offset) {
        const uint8_t *src=(const uint8_t *)slots+offset;
        for (i=0;i<length;i++) dest[i]=src[i];
        return 1;
    }
    return flash_backend.read(flash_backend.context,offset,dest,length);
}
int RemoteSaveValidatePeer(void)
{
    volatile const uint8_t *cart=(volatile const uint8_t *)0x080000acu;
    return flash.identified && cart[0]=='B' && cart[1]=='P' && cart[2]=='E' && cart[3]=='J';
}
void __attribute__((noreturn)) BoxDebugMain(void)
{
    uint32_t *p;
    uint16_t word;
    struct RemoteSaveBackend backend;
    int phase=0, valid[2], writing=0;
    unsigned written_sectors=0;
    uint32_t counters[2]={0,0};
    unsigned completed_sectors=0;
    uint16_t last_progress_seq=0;
    int have_progress_seq=0;
    IME=0;
    for(p=__box_bss_start;p<__box_bss_end;p++) *p=0;
    RemoteDebugShow("GUEST CHECK FLASH");
    if(!RemoteGbaFlashOpen(&flash)) {
        RemoteDebugShow("GUEST FLASH FAIL");
        for(;;) {}
    }
    flash_backend=RemoteFlashBackend(&flash);
    RemoteDebugShow("GUEST CHECK SAVE");
    valid[0]=flash_backend.read(flash_backend.context,0,slots[0],sizeof(slots[0])) &&
             RemoteSlotValidate(slots[0],0,&counters[0]);
    valid[1]=flash_backend.read(flash_backend.context,sizeof(slots[0]),slots[1],sizeof(slots[1])) &&
             RemoteSlotValidate(slots[1],1,&counters[1]);
    selected_slot=RemoteSlotChoose(valid[0],counters[0],valid[1],counters[1]);
    backend=flash_backend;
    backend.read=snapshot_read;
    backend.program=snapshot_program; backend.erase=snapshot_erase;
    RemoteSaveServerInit(&server,backend);
    RemoteLinkSlaveInit(&link,&server);
    RemoteBulkSlaveInit(&bulk,backend);
    RemoteSlotStreamInit(&slot_stream,selected_slot < 0 ? 0 : slots[selected_slot]);
    RemoteDebugShow("GUEST WAIT PROBE");
    RCNT=0; SIOCNT=0x6003u; SEND=LINK_READY; IF=0x80u;
    for (;;) {
        while(!(IF&0x80u)){}
        IF=0x80u;word=MULTI0;
        if(phase==0 && word==LINK_PROBE) {phase=1;RemoteDebugShow("GUEST GOT PROBE");SEND=LINK_ACK;}
        else if(phase==1 && word==LINK_CONFIRM) {phase=2;RemoteDebugShow("GUEST LINK OK");SEND=LINK_DONE;}
        else if(phase>=2 && word==REMOTE_LINK_SYNC) {
            phase=3; SEND=RemoteLinkSlaveReceive(&link,word);
        }
        else if(phase==3) {
            int completed;
            uint16_t bulk_output;
            unsigned stream_progress;
            size_t before=link.response_pos;
            uint16_t previous_seq=server.last_sequence;
            int had_last=server.has_last;
            if (RemoteSlotStreamReceive(&slot_stream,word,&bulk_output,&stream_progress)) {
                if (word==SLOT_START) RemoteDebugShow("GUEST SEND SAVE");
                SEND=bulk_output;
                if(stream_progress) RemoteDebugSectorProgress(stream_progress-1u);
                continue;
            }
            if (word==BULK_CHOOSE) {
                SEND=selected_slot < 0 ? BULK_CHOICE_ERROR : (uint16_t)(BULK_CHOICE_BASE+selected_slot);
                continue;
            }
            if (RemoteBulkSlaveReceive(&bulk,word,&bulk_output,&completed)) {
                SEND=bulk_output;
                if (completed) RemoteDebugSectorProgress(completed_sectors++);
                continue;
            }
            uint16_t output=RemoteLinkSlaveReceive(&link,word);
            SEND=output;
            if (server.has_last && (!had_last || server.last_sequence!=previous_seq) &&
                link.response_length > REMOTE_SAVE_HEADER_SIZE &&
                (link.frame.command == REMOTE_SAVE_ERASE_SECTOR || link.frame.command == REMOTE_SAVE_PROGRAM)) {
                if (link.response[REMOTE_SAVE_HEADER_SIZE] != REMOTE_STATUS_OK) {
                    RemoteDebugShow("GUEST SAVE FAIL"); writing=0;
                } else if (link.frame.command == REMOTE_SAVE_ERASE_SECTOR && !writing) {
                    RemoteDebugShow("GUEST WRITE SAVE"); writing=1; written_sectors=0;
                } else if (link.frame.command == REMOTE_SAVE_PROGRAM && writing &&
                           (link.frame.offset & 4095u) == 3840u && link.frame.length == 256u) {
                    RemoteDebugSectorProgress(written_sectors++);
                    if (written_sectors==14u) writing=0;
                }
            }
            if (word==REMOTE_LINK_POLL && before < link.response_length &&
                link.response_pos == link.response_length &&
                link.frame.command == REMOTE_SAVE_READ && link.frame.length == 2 &&
                link.response_length > REMOTE_SAVE_HEADER_SIZE &&
                link.response[REMOTE_SAVE_HEADER_SIZE] == REMOTE_STATUS_OK &&
                (!have_progress_seq || link.frame.sequence != last_progress_seq)) {
                uint32_t count=(uint32_t)link.frame.payload[0] | ((uint32_t)link.frame.payload[1]<<8);
                if ((link.frame.offset % REMOTE_SAVE_SECTOR_SIZE) + count == REMOTE_SAVE_SECTOR_SIZE) {
                    RemoteDebugSectorProgress(completed_sectors++);
                    last_progress_seq=link.frame.sequence;
                    have_progress_seq=1;
                }
            }
        }
    }
}
