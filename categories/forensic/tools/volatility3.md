# Volatility 3

https://github.com/volatilityfoundation/volatility3

Framework for extracting artifacts from memory dumps (RAM). Successor to Volatility 2 (Volatility 2 is deprecated/archived).

```bash
vol -f memory.raw windows.info   # identify OS / confirm it parses
```

## Common plugins

- `windows.cmdline` / `windows.cmdscan` — process args + console command history
- `windows.pstree` — process parent/child tree
- `windows.netscan` — network connections (find C2 / exfil)
- `windows.malware.malfind` — injected / suspicious memory regions
- `windows.filescan` — open files (dropped payloads, persistence files)
- `windows.handles` — open handles
- `windows.registry.hivelist` / `.printkey` / `.userassist` — registry hives, run keys, executed programs
- `windows.envars` — environment variables
- `windows.strings` — strings from memory (slow; use external `strings memory.raw` instead)
