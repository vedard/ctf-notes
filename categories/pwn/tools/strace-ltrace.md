# strace / ltrace

https://github.com/strace/strace · https://github.com/ltrace/ltrace

Trace what a program does. `strace` shows syscalls (kernel side), `ltrace` shows library calls (libc side). Run on challenge binaries to see the secret being read, the flag file opened, or the comparison that gates the win.

```bash
strace ./chal                    # every syscall
strace -f ./chal                 # follow forked children
strace ./chal 2> trace.txt       # strace writes to stderr
strace -o trace.txt ./chal       # or to a file
strace -e trace=openat,read,write ./chal
strace -e trace=%file ./chal     # file-related syscalls only
strace -e trace=network ./chal
strace -c ./chal                 # summary counts by syscall
strace -p <pid>                  # attach to a running process

ltrace ./chal                    # library calls
ltrace -e 'printf+puts' ./chal
ltrace -S ./chal                 # also show the return value
```

Useful options:
- `-f` — follow forks (needed when the binary re-execs or spawns a shell)
- `-e trace=<syscalls>` — filter which syscalls are logged
- `-o <file>` — write the log to a file
- `-c` — summary instead of a full log
- `-p <pid>` — attach to an existing process
- `-S` (ltrace) — print return values

CTF notes:
- `strace -f -e trace=openat ./chal` is the fastest way to spot a flag file path being opened.
- `ltrace` on a decrypted-output binary reveals the real comparison (e.g. `strcmp("s3cr3t", input)`).
- Output is unreadable at full verbosity — narrow with `-e` before grepping.
- If the binary is statically linked, `ltrace` shows nothing useful; `strace` still works.
