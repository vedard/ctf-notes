# ret2syscall

Build a ROP chain that performs a **syscall** directly, bypassing libc (no `system`, no leaked libc base needed).

## When to reach for it

- Stack overflow with a controllable return address.
- `system`/`execve` not available, or libc base unknown, but the binary has a `syscall` (or `int 0x80`) gadget.
- NX enabled (stack not executable) → return-oriented, not shellcode.

## How it works

Load syscall arguments into registers with `pop` gadgets, set `rax` to the syscall number, then hit `syscall`.

amd64 registers: `rax` = number, `rdi` `rsi` `rdx` `r10` `r8` `r9` = args.
Common numbers: `execve` = 59, `open` = 2, `read` = 0, `write` = 1.

## Minimal steps

1. Find gadgets: `pop rdi; ret`, `pop rsi; ret`, `pop rdx; ret`, `pop rax; ret`, `syscall; ret` (see `categories/pwn/tools/ropgadget.md`).
2. Need `"/bin/sh"` writable somewhere:
   - present as a string in the binary → use its address; or
   - write it to `.bss` with a prior `gets`/`read` call.
3. Build the chain: overflow offset + gadgets + `execve("/bin/sh", 0, 0)`.

```
offset
pop rdi; ret          -> addr of "/bin/sh"
pop rax; ret          -> 59
pop rsi; ret          -> 0
pop rdx; ret          -> 0
syscall
```

4. If writing to `.bss`, prepend: `pop rdi; ret -> bss` then `gets`, and send the string as a second input.

## Notes

- No syscall gadget but a usable libc? See `categories/pwn/notes/ret2libc-32-bruteforce.md`.
- `pop rdx; pop rbx; ret` and similar multi-pop gadgets are fine — pad the extra pops with junk.
- Missing `pop rsi`/`pop rdx`? Look for `pop rsi; pop r15; ret` or `mov`/`xchg`-based alternatives.
- 32-bit (`int 0x80`): args in `ebx` `ecx` `edx`; `execve` = 11.
