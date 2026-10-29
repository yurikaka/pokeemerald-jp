#include <stdint.h>
#define RESULT (*(volatile uint32_t *)0x0203fff0u)
#define BEGIN ((int (*)(void))(REMOTE_BEGIN | 1u))
#define TICK ((int (*)(volatile int16_t *))(REMOTE_TICK | 1u))
#define READ ((int (*)(uint16_t,uint32_t,uint8_t *,uint32_t))(REMOTE_READ | 1u))
#define INIT_HEAP ((void (*)(void *,uint32_t))0x08000badu)
#define PROGRAM (*(uint16_t (**)(uint16_t,const uint8_t *))0x030075ecu)
static uint8_t data[4096],verify[4096];
void TestMain(void){volatile int16_t phase=0;unsigned i,k;const uint16_t sectors[2]={2,16};RESULT=1;while(!TICK(&phase)){} RESULT=2;if(!BEGIN()){RESULT=3;for(;;){}}
 *(volatile uint32_t *)0x03007ff0u=0x03006120u;
 *(volatile uint32_t *)0x03006120u=0x68736d53u;
 INIT_HEAP((void *)0x02000000u,0x1c000u);
 *(volatile uint16_t *)0x06017600u=0x789a;
 *(volatile uint16_t *)0x050003e2u=0x4321;
 *(volatile uint16_t *)0x070001e0u=0x4321;
 *(volatile uint16_t *)0x04000000u=0x1040;
 for(k=0;k<2;k++){
  for(i=0;i<4096;i++)data[i]=(uint8_t)(i*37u+(i>>8)+k*17u);
  data[0xff4]=(uint8_t)k;data[0xff5]=0;
  data[0xff8]=0x25;data[0xff9]=0x20;data[0xffa]=0x01;data[0xffb]=0x08;
  if(PROGRAM(sectors[k],data)){RESULT=0x100+k;for(;;){}}
  if(*(volatile uint32_t *)0x03006120u!=0x68736d53u){RESULT=0x500+k;for(;;){}}
  if(*(volatile uint16_t *)0x06017600u!=0x789a || *(volatile uint16_t *)0x050003e2u!=0x4321 ||
     *(volatile uint16_t *)0x070001e0u!=0x4321 || *(volatile uint16_t *)0x04000000u!=0x1040){RESULT=0x400+k;for(;;){}}
  if(!READ(sectors[k],0,verify,4096)){RESULT=0x200+k;for(;;){}}
  for(i=0;i<4096;i++)if(data[i]!=verify[i]){RESULT=0x300+k;for(;;){}}
 }
 if(!PROGRAM(28,data)){RESULT=4;for(;;){}}
 RESULT=0x600d;for(;;){}
}
