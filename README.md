# CTF Notes

Personal knowledge base for CTF competitions. Cross-category material lives at the top level; category-specific material under [`categories/`](categories/). Conventions documented in [AGENTS.md](AGENTS.md).

## Cross-Category
[references](references.md)

### Snippets
- [Reverse Shell Stabilization](snippets/shells.md)

### Tools

- [cchef](tools/cchef.md) CyberChef on the command line
- [CyberChef](tools/cyberchef.md) web app for encoding, decoding, hashing, and data analysis
- [NetExec](tools/netexec.md) network service exploitation tool (CrackMapExec successor) for Windows/AD enumeration, auth, and lateral movement
- [strings](tools/strings.md) print printable strings from any binary

## Cloud

### Tools

- [AWS CLI](categories/cloud/tools/aws-cli.md) query and manage AWS resources
- [Azure CLI](categories/cloud/tools/az.md) query and manage Azure resources (`az`)
- [gcloud](categories/cloud/tools/gcloud.md) Google Cloud CLI

## Crypto

[references](categories/crypto/references.md)

### Tools

- [John the Ripper](categories/crypto/tools/john.md) offline password cracker

## Forensic

### Tools

- [chainsaw](categories/forensic/tools/chainsaw.md) Windows Event Log and Sysmon triage
- [exiftool](categories/forensic/tools/exiftool.md) file metadata reader
- [Hindsight](categories/forensic/tools/hindsight.md) Chrome and Firefox browser artifact parser
- [rtptools](categories/forensic/tools/rtptools.md) replay RTP streams and rebuild media from pcaps
- [Volatility 3](categories/forensic/tools/volatility3.md) memory dump forensics
- [Wireshark](categories/forensic/tools/wireshark.md) packet capture analysis

## OSINT

### Tools

- [Sherlock](categories/osint/tools/sherlock.md) find a username across hundreds of sites

## Pwn

### Techniques

- [ret2libc (32-bit, libc-base brute-force)](categories/pwn/techniques/ret2libc-32-bruteforce.md) ret2libc without a leak by brute-forcing the libc base
- [ret2syscall](categories/pwn/techniques/ret2syscall.md) ROP chain calling syscalls directly, bypassing libc

### Tools

- [checksec](categories/pwn/tools/checksec.md) show binary hardening (RELRO, canary, NX, PIE)
- [pwndbg](categories/pwn/tools/pwndbg.md) gdb plugin for exploit development
- [pwntools](categories/pwn/tools/pwntools.md) Python library for exploit development
- [ROPgadget](categories/pwn/tools/ropgadget.md) search ROP and JOP gadgets in binaries

### Templates

- [solve.py](categories/pwn/templates/solve.py) pwntools exploit skeleton

## Rev

### Tools

- [dnSpy](categories/rev/tools/dnspy.md) decompile and debug .NET assemblies
- [Ghidra](categories/rev/tools/ghidra.md) RE suite for native binaries
- [JADX](categories/rev/tools/jadx.md) decompile Android APKs
- [pycdc (Decompyle++)](categories/rev/tools/pycdc.md) decompile Python `.pyc` files
- [unluac](categories/rev/tools/unluac.md) decompile Lua bytecode
- [unrpa / unrpyc](categories/rev/tools/unrpa.md) unpack Ren'Py archives and decompile scripts

## Steg

### Tools

- [binwalk](categories/steg/tools/binwalk.md) find and extract embedded files in a blob
- [foremost](categories/steg/tools/foremost.md) carve embedded files by signature
- [steghide](categories/steg/tools/steghide.md) hide/extract data in WAV, BMP, JPEG, AU files
- [zsteg](categories/steg/tools/zsteg.md) detect steganography in PNG and BMP files

## Web

[references](categories/web/references.md)

### Techniques

- [Dynamic LINQ injection (.NET)](categories/web/techniques/dynamic-linq-injection.md) injection into `System.Linq.Dynamic.Core` query strings

### Tools

- [Burp Suite](categories/web/tools/burp.md) intercepting proxy and manual web testing suite
- [Gobuster](categories/web/tools/gobuster.md) directory, vhost, and DNS brute-force
- [HTTPie](categories/web/tools/httpie.md) user-friendly HTTP client
- [sqlmap](categories/web/tools/sqlmap.md) automatic SQL injection detection and exploitation

