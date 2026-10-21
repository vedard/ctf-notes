# ROPgadget

https://github.com/JonathanSalwan/ROPgadget

Search ROP/JOP gadgets in binaries.

```bash
ROPgadget --binary chal --only "pop|ret" | grep rdi
ROPgadget --binary chal --only "syscall" | grep syscall
ROPgadget --binary chal --string "/bin/sh"
```

Useful options:
- `--only "pop|ret"` — filter gadget types (combine with `grep`)
- `--string "..."` — find a string in the binary (note its address)
- `--depth N` — max gadget length

Missing `/bin/sh` in the binary? Write it yourself via `gets(bss)` before the execve ROP chain.
