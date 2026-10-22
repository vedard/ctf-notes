# Hydra

https://github.com/vanhauser-thc/th-hydra

Online brute-forcer. Same wordlists as `john`/`hashcat`, but attacks a live service instead of a local hash file.

```bash
# SSH with a single user
hydra -l admin -P /usr/share/wordlists/rockyou.txt <target> ssh

# SSH with a user list and one password
hydra -L users.txt -p admin <target> ssh

# HTTP form login
hydra -l admin -P rockyou.txt <target> http-post-form \
  "/login:user=^USER^&pass=^PASS^:F=Invalid"

# FTP
hydra -l anonymous -P rockyou.txt <target> ftp

# Pair list (user:pass) against a module
hydra -C creds.txt <target> ssh
```

Useful options:
- `-l` / `-L` — single username / username file
- `-p` / `-P` — single password / password file
- `-x user:pass` — explicit credential pairs
- `-sS` / `-sV` — SSL / verbose SSL
- `-t` — parallel tasks (default 16, lower it if the service rate-limits)
- `-f` — stop at first successful login
- `-F "string"` — failure string, needed for HTTP forms
- `-T 1` — delay between attempts (avoid lockouts)
- `-u` — UDP mode
- `-m` — force a specific module

CTF notes:
- For `http-post-form` the syntax is `path:user-field=^USER^&pass-field=^PASS^:F=failure-string`. The failure string is what tells Hydra the attempt failed; without it every attempt looks like a success.
- Hydra treats an HTTP 302 redirect as success. If the login page redirects on failure, pass `-F` with the error text instead.
- `-f` matters on CTFs: a valid login may disable the account after a few more attempts.
