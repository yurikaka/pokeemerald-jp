#include <stdint.h>
#define RESULT (*(volatile uint32_t *)0x0203fff0u)
#define BEGIN ((int (*)(void))(REMOTE_BEGIN | 1u))
#define READ ((int (*)(uint16_t,uint32_t,uint8_t *,uint32_t))(REMOTE_READ | 1u))
#define TICK ((int (*)(volatile int16_t *))(REMOTE_TICK | 1u))
#define CHOOSE ((int (*)(void *,void *))(REMOTE_CHOOSE | 1u))
#define STREAM ((int (*)(void *,void *,uint8_t *,void *))(REMOTE_STREAM | 1u))
#define VALIDATE ((int (*)(const uint8_t *,unsigned,uint32_t *))(REMOTE_VALIDATE | 1u))
void TestMain(void) {
 volatile int16_t phase=0; int slot; uint32_t counter;
 RESULT=1; while(!TICK(&phase)){} RESULT=2;
 if(!BEGIN()){RESULT=3;for(;;){}}
 slot=CHOOSE((void *)(REMOTE_TRANSFER|1u),0);
 if(slot!=EXPECTED_SLOT){RESULT=0x100+(unsigned)(slot+1);for(;;){}}
 if(!STREAM((void *)(REMOTE_TRANSFER|1u),0,(uint8_t *)0x02000000u,0)){RESULT=6;for(;;){}}
 if(!VALIDATE((const uint8_t *)0x02000000u,(unsigned)slot,&counter)){RESULT=4;for(;;){}}
 RESULT=0x600d;for(;;){}
}
