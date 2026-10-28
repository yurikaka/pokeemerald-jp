#include "link.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
struct Test { struct RemoteLinkSlave slave; uint8_t flash[REMOTE_SAVE_FLASH_SIZE]; int writes, drop_response; };
static int rd(void *p, uint32_t a, uint8_t *d, uint16_t n) { struct Test *t = p; memcpy(d,t->flash+a,n); return 1; }
static int wr(void *p, uint32_t a, const uint8_t *d, uint16_t n) { struct Test *t = p; ++t->writes; memcpy(t->flash+a,d,n); return 1; }
static int er(void *p, uint32_t a) { struct Test *t = p; memset(t->flash+a,255,4096); return 1; }
static int transfer(void *p, uint16_t tx, uint16_t *rx)
{
 struct Test *t = p;
 *rx = t->slave.output;
 RemoteLinkSlaveReceive(&t->slave, tx);
 if (t->drop_response && (*rx & 0xff00u) == REMOTE_LINK_RESPONSE) { t->drop_response=0; return 0; }
 return 1;
}
int main(void)
{
 static struct Test t; struct RemoteSaveServer s; struct RemoteSaveClient c;
 struct RemoteSaveBackend b={&t,rd,wr,er}; struct RemoteLinkMaster m={&t,transfer,1000};
 uint8_t src[256], dst[256]; unsigned i;
 RemoteSaveServerInit(&s,b); RemoteLinkSlaveInit(&t.slave,&s);
 RemoteSaveClientInit(&c,&m,RemoteLinkExchange,2); assert(RemoteSaveClientHello(&c));
 for(i=0;i<256;++i) src[i]=(uint8_t)i;
 t.drop_response=1;
 assert(RemoteSaveClientProgram(&c,0x10000,src,256));
 assert(t.writes==1);
 assert(RemoteSaveClientRead(&c,0x10000,dst,256));
 assert(memcmp(src,dst,256)==0);
 puts("remote save serial-token tests passed"); return 0;
}
