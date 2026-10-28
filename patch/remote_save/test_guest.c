#include <stdint.h>
#define RESULT (*(volatile uint32_t *)0x0203fff0u)
#define BEGIN ((int (*)(void))(REMOTE_BEGIN | 1u))
#define READ ((void (*)(uint16_t,uint32_t,uint8_t *,uint32_t))0x0829005du)
#define ERASE (*(uint16_t (**)(uint16_t))0x03007600u)
#define WRITE (*(uint16_t (**)(uint16_t,uint32_t,uint8_t))0x030075f4u)
void TestMain(void)
{
 uint8_t data[256]; unsigned i;
 RESULT=1;
 if (!BEGIN()) { RESULT=2; for(;;){} }
 if (ERASE(31)) { RESULT=3; for(;;){} }
 if (WRITE(31, 15, 0x42)) { RESULT=4; for(;;){} }
 READ(31, 15, data, sizeof(data));
 if (data[0] != 0x42) { RESULT=6; for(;;){} }
 for (i=1; i<sizeof(data); ++i) if (data[i] != 0xff) { RESULT=7; for(;;){} }
 RESULT = 0x600d;
 for(;;){}
}
