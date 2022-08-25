from pwn import *

KEY_LEN = 50000
MAX_CHUNK = 50000

r = remote("mercury.picoctf.net", 58913)
r.recvuntil(b"This is the encrypted flag!\n")
flag = r.recvlineS(keepends = False)
bin_flag = unhex(flag)

chunk_size = min(MAX_CHUNK, KEY_LEN - len(bin_flag))
r.sendlineafter(b"What data would you like to encrypt? ", b"a" * chunk_size)

r.sendlineafter(b"What data would you like to encrypt? ", bin_flag)
r.recvlineS()
final_flag = unhex(r.recvlineS())
log.success("The flag: {}".format(final_flag))
r.close()
print('\npicoCTF{' + final_flag.decode() + '}')