# pycdc (Decompyle++)

https://github.com/zrax/pycdc

Decompile Python `.pyc` files. Ships two binaries:

- `pycdc` — decompiler (often fails on 3.11+ bytecode)
- `pycdas` — disassembler; reliable fallback

```bash
pycdc check.pyc          # may error: "Error decompiling ..."
pycdas check.pyc         # [Disassembly] listing — read opcodes by hand
```