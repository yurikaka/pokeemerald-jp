#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "game.h"
#include "slot_select.h"
struct Harness { uint8_t flash[131072]; int fail_sector; unsigned erase_count, program_count; struct RemoteSaveServer server; };
static int read_data(void*p,uint32_t off,uint8_t*d,uint16_t n){struct Harness*h=p;memcpy(d,h->flash+off,n);return 1;}
static int erase(void*p,uint32_t off){struct Harness*h=p;if((int)(off/4096)==h->fail_sector)return 0;memset(h->flash+off,255,4096);h->erase_count++;return 1;}
static int program(void*p,uint32_t off,const uint8_t*d,uint16_t n){struct Harness*h=p;unsigned i;for(i=0;i<n;i++)h->flash[off+i]&=d[i];h->program_count++;return 1;}
static size_t exchange(void*p,const uint8_t*q,size_t n,uint8_t*r,size_t cap){struct Harness*h=p;return RemoteSaveServerHandle(&h->server,q,n,r,cap);}
static void put16(uint8_t*p,uint16_t x){p[0]=(uint8_t)x;p[1]=(uint8_t)(x>>8);}
static void put32(uint8_t*p,uint32_t x){put16(p,(uint16_t)x);put16(p+2,(uint16_t)(x>>16));}
static void make_slot(uint8_t *p,uint32_t counter){unsigned i;memset(p,0,14*4096);for(i=0;i<14;i++){uint8_t*s=p+i*4096;put16(s+0xff4,(uint16_t)i);put32(s+0xff8,0x08012025);put32(s+0xffc,counter);}}
static void run(int fail){static struct Harness h;struct RemoteSaveClient c;struct RemoteSaveBackend b={&h,read_data,program,erase};uint8_t sector[4096];uint32_t count;unsigned i;memset(&h,0,sizeof(h));h.fail_sector=fail;make_slot(h.flash,124);make_slot(h.flash+14*4096,123);RemoteSaveServerInit(&h.server,b);RemoteSaveClientInit(&c,&h,exchange,3);c.session=0x12345678;assert(RemoteSaveClientHello(&c));assert(RemoteSaveClientStatus(&c));for(i=0;i<14;i++){memcpy(sector,h.flash+i*4096,4096);put32(sector+0xffc,125);if(!RemoteGameProgramSector(&c,(uint16_t)(i+14),sector))break;}assert(RemoteSlotValidate(h.flash,0,&count)&&count==124);if(fail<0){assert(i==14);assert(RemoteSlotValidate(h.flash+14*4096,1,&count)&&count==125);assert(h.erase_count==14 && h.program_count==14*16);}else{assert(i==(unsigned)(fail-14));assert(!RemoteSlotValidate(h.flash+14*4096,1,&count) || count==123);} }
int main(void){run(-1);run(20);puts("14-sector save and interrupted write preserve prior slot");}
