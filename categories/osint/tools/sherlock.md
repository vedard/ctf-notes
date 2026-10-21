# Sherlock

https://github.com/sherlock-project/sherlock

Hunt down a username across many sites. Given one handle, it checks hundreds of platforms and reports where an account exists.

```bash
sherlock GaspardGungusIII
sherlock --timeout 10 --print-found <username>
sherlock -o results.txt <username>
```

- Takes a username (repeat the arg or use `--site`/file input for many) and prints `[+] Site: URL` for each hit.
- Common pivot: pull a username from document metadata (`exiftool`) or a profile, then feed it here to find the person's other accounts.
- Some sites WAF-block the default User-Agent; pass a browser UA if results look empty.
