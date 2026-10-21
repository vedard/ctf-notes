# pwndbg

https://pwndbg.re/

gdb plugin for exploit dev — find crash offsets, inspect registers/stack/heap, trace exploitation. Replaces the gdb CLI experience (install once: `git clone https://github.com/pwndbg/pwndbg && cd pwndbg && ./gdbinit.sh`).

```bash
gdb ./chal
```

Essential commands:
```text
break main        # b main / b *0x4011a3
breakrva
info functions
run / r           # start program
continue / c      # next break
next / n          # step over, step / s step into
info registers    # regs, x/10gx $rsp  examine memory
x/s $rdi          # print string at rdi
disas main        # disassemble
backtrace / bt    # call stack
p var             # print value
```

pwndbg extras:
```text
telescope $rsp    # stack dump with dereferences
cyclic 100        # pattern; cyclic_find <value> → offset
vmmap             # memory mappings
heap / vis_heap_chunks
checksec          # protections
payload           # show current ROP payload
```