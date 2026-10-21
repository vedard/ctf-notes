# John the Ripper

https://www.openwall.com/john/

Offline password cracker. Auto-detects hash format; use `--format` to force when detection fails.

```bash
# Crack with wordlist
john hash --wordlist=/usr/share/dict/rockyou.txt

# Show cracked passwords
john --show hash

# Force a format (list them all with --format=list)
john --format=raw-md5 hash --wordlist=/usr/share/dict/rockyou.txt
```