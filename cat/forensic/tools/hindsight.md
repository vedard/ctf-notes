# Hindsight

https://github.com/RyanDFIR/hindsight

Chrome/Chromium (and Firefox via libyal) browser artifact parser: history, downloads, cookies, search terms, localStorage. Outputs JSON / CSV / Timeline / SQLite.

```bash
http -d https://github.com/RyanDFIR/hindsight/releases/download/v2026.06/hindsight-linux-x86_64
chmod +x ./hindsight-linux-x86_64

# Point it at a user home directory: it finds all browser profiles automatically
./hindsight-linux-x86_64 -i /mnt/C/Users/<user> -d -f jsonl
```