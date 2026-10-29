#include "boot_handshake.h"
#include <assert.h>
#include <stdio.h>
int main(void)
{
    struct RemoteGuestBootHandshake h={0,0x3130,0x0096};
    const uint16_t master[]={0,0x8000,0x0400,0x0020,1,0,0x3130,0x0096};
    const uint16_t want[]={0,0,0x8000,0x0400,0x0020,1,0x3130,0x0096};
    uint16_t response=0; unsigned i;
    for(i=0;i<8;i++) {
        int done; assert(response==want[i]);
        done=RemoteGuestBootStep(&h,master[i],&response);
        assert(done==(i==7));
    }
    h.state=3;response=0xffff;
    assert(!RemoteGuestBootStep(&h,0,&response) && h.state==1 && response==0);
    assert(!RemoteGuestBootStep(&h,0x7777,&response) && h.state==0 && response==0);
    puts("multiboot guest handshake sequence passed");
    return 0;
}
