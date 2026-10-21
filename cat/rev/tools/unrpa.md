# unrpa / unrpyc

https://github.com/lattyware/unrpa

Unpack Ren'Py game archives (`.rpa`). Ren'Py bundles scripts and assets into these archives, so a forensics/RE challenge on a Ren'Py game starts here.

- `unrpa` — extracts `.rpa` archives.
- `unrpyc` (https://github.com/CensoredUsername/unrpyc) — companion: decompiles the compiled scripts (`.rpyc`) back to `.rpy` once extracted.

```bash
unrpa -mp out -a game.rpa          # -m create dirs, -p prefix paths, -a all versions
unrpyc game/script.rpyc            # or: unrpyc -c -p out game/
```

- `.rpyc` files are compiled Ren'Py script — decompile with `unrpyc` to read game logic (keys, XOR seeds, embedded creds).
- Flags often hide in a second layer: an encrypted/encoded asset whose key sits in the decompiled script.
