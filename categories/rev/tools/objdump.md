# objdump

https://sourceware.org/binutils/docs/binutils/objdump.html

Disassembler and object-file inspector from binutils. First stop before opening Ghidra, and the quickest way to read a symbol table or PLT stub.

```bash
objdump -d chal                 # disassemble .text
objdump -d -M intel chal       # Intel syntax (default is AT&T)
objdump -d -j .plt chal        # PLT stubs
objdump -t chal                # symbol table
objdump -R chal                # dynamic relocations (GOT entries)
objdump -s -j .rodata chal    # dump a section's bytes
objdump -h chal                # section headers
objdump -f chal                # file header (arch, endianness)
objdump -x chal                # all headers
```

Useful options:
- `-M intel` — Intel syntax; much easier to read than AT&T (`mov rax, rdi` vs `mov %rdi,%rax`)
- `-C` — demangle C++ symbols
- `-d` — disassemble
- `-s` — dump full contents of sections
- `-j <section>` — restrict to one section
- `-r` / `-R` — relocations / dynamic relocations

CTF notes:
- Read `.plt` first: it shows which libc functions the binary imports, which hints at the vulnerability (e.g. `printf` → format string, `gets` → stack overflow, `mprotect` → shellcode).
- `objdump -R` on a PIE binary shows the GOT slots — useful for planning a GOT overwrite or leak.
- Combine with `checksec` to know whether addresses you see are stable (no PIE) or relocated.
