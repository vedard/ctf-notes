# unluac

https://github.com/HansWessels/unluac

Decompile Lua bytecode (Lua 5.1) back to source. Java-based, runs from a single JAR.

```bash
java -jar unluac.jar myfile.luac > myfile.lua
```

- Requires the chunk's debug info (standard `luac` output keeps it); chunks compiled with `-s` (stripped) won't decompile cleanly.
- Alternatives: `luadec` (C, handles more Lua versions), and rust `unluac-rs` for LuaJIT/Luau.
- After decompiling, the recovered source usually reveals XOR/subtract keys or credential tables directly.
