#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "slot_select.h"
static uint8_t slots[2][14*4096];
static void put16(uint8_t*p,uint16_t x){p[0]=x;p[1]=x>>8;}
static void put32(uint8_t*p,uint32_t x){put16(p,(uint16_t)x);put16(p+2,(uint16_t)(x>>16));}
static void make_slot(unsigned slot,uint32_t count){unsigned i;for(i=0;i<14;i++){uint8_t*p=slots[slot]+i*4096;memset(p,0,4096);put16(p+0xff4,i);put32(p+0xff8,0x08012025);put32(p+0xffc,count);}}
int main(void){uint32_t a=0,b=0;make_slot(0,124);make_slot(1,123);assert(RemoteSlotValidate(slots[0],0,&a));assert(RemoteSlotValidate(slots[1],1,&b));assert(RemoteSlotChoose(1,a,1,b)==0);assert(RemoteSlotChoose(0,a,1,b)==1);assert(RemoteSlotChoose(1,0xffffffffu,1,0)==1);slots[0][0]^=1;assert(!RemoteSlotValidate(slots[0],0,&a));slots[1][0xff4]=20;assert(!RemoteSlotValidate(slots[1],1,&b));assert(RemoteSlotChoose(0,0,0,0)==-1);puts("slot validation, newest, fallback and wraparound passed");}
