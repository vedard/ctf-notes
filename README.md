# CTF Notes

Personal knowledge base for CTF competitions. Cross-category material lives at the top level; category-specific material under [`categories/`](categories/). Directory conventions are documented in [AGENTS.md](AGENTS.md).

## Cross-category

- [references.md](references.md) — useful links (CTFtime, HackTricks, PayloadsAllTheThings, GTFOBins, writeup blog)
- [snippets/shells.md](snippets/shells.md) — reverse shell stabilization
- [tools/cchef.md](tools/cchef.md) — cchef — CyberChef on the command line
- [tools/cyberchef.md](tools/cyberchef.md) — CyberChef — web app for encoding/decoding, hashing, data analysis

## Categories

### [crypto](categories/crypto/)

- [references.md](categories/crypto/references.md) — crypto links (dCode)
- [tools/john.md](categories/crypto/tools/john.md) — John the Ripper — offline password cracker

### [forensic](categories/forensic/)

- [tools/chainsaw.md](categories/forensic/tools/chainsaw.md) — chainsaw — Windows Event Log / Sysmon triage
- [tools/exiftool.md](categories/forensic/tools/exiftool.md) — exiftool — file metadata
- [tools/hindsight.md](categories/forensic/tools/hindsight.md) — Hindsight — Chrome/Firefox browser artifact parser
- [tools/rtptools.md](categories/forensic/tools/rtptools.md) — rtptools — replay RTP streams / rebuild media from pcaps
- [tools/volatility3.md](categories/forensic/tools/volatility3.md) — Volatility 3 — memory dump forensics
- [tools/wireshark.md](categories/forensic/tools/wireshark.md) — Wireshark — packet capture analysis

### [osint](categories/osint/)

- [tools/sherlock.md](categories/osint/tools/sherlock.md) — Sherlock — hunt a username across hundreds of sites

### [pwn](categories/pwn/)

- [notes/ret2libc-32-bruteforce.md](categories/pwn/notes/ret2libc-32-bruteforce.md) — ret2libc (32-bit, libc-base brute-force) — no leak needed
- [notes/ret2syscall.md](categories/pwn/notes/ret2syscall.md) — ret2syscall — ROP chain calling syscalls directly, bypassing libc
- [templates/solve.py](categories/pwn/templates/solve.py) — pwntools exploit skeleton
- [tools/pwndbg.md](categories/pwn/tools/pwndbg.md) — pwndbg — gdb plugin for exploit dev
- [tools/pwntools.md](categories/pwn/tools/pwntools.md) — pwntools — Python library for exploit development
- [tools/ropgadget.md](categories/pwn/tools/ropgadget.md) — ROPgadget — search ROP/JOP gadgets in binaries

### [rev](categories/rev/)

- [tools/dnspy.md](categories/rev/tools/dnspy.md) — dnSpy — decompile/debug .NET assemblies
- [tools/ghidra.md](categories/rev/tools/ghidra.md) — Ghidra — RE suite, decompile native binaries
- [tools/jadx.md](categories/rev/tools/jadx.md) — JADX — decompile Android APKs
- [tools/pycdc.md](categories/rev/tools/pycdc.md) — pycdc (Decompyle++) — decompile Python `.pyc` files
- [tools/unluac.md](categories/rev/tools/unluac.md) — unluac — decompile Lua bytecode
- [tools/unrpa.md](categories/rev/tools/unrpa.md) — unrpa / unrpyc — unpack Ren'Py archives, decompile scripts

### [web](categories/web/)

- [notes/dynamic-linq-injection.md](categories/web/notes/dynamic-linq-injection.md) — Dynamic LINQ injection (.NET)
- [references.md](categories/web/references.md) — web links (CSP bypass)
- [tools/gobuster.md](categories/web/tools/gobuster.md) — Gobuster — directory / vhost / DNS brute-force
- [tools/httpie.md](categories/web/tools/httpie.md) — HTTPie — user-friendly HTTP client
