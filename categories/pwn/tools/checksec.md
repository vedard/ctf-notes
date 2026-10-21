# checksec

https://github.com/slimm609/checksec

Show binary hardening: RELRO, canary, NX, PIE, fortify. Run before writing any pwn exploit.

```bash
checksec --file=chal
```

pwntools bundles it too:

```python
from pwn import *
print(ELF('chal').checksec())  # or just ELF('chal') in the repl
```

Reads:
- **NX enabled** — need ROP, not shellcode
- **Canary** — need a leak before buffer overflow
- **PIE** — addresses are randomized, need leak or partial overwrite
- **Full RELRO** — GOT is read-only, no GOT overwrite
