# Gobuster

https://github.com/OJ/gobuster

Fast directory / vhost / DNS brute-force tool written in Go.

## Directory brute-force

```bash
gobuster dir -u http://target.com -w /usr/share/seclists/Discovery/Web-Content/common.txt
gobuster dir -u http://target.com -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt
```

Common options:
- `-x php,html,txt` — also try these extensions
- `-b 404,403` — exclude status codes
- `-k` — skip TLS certificate validation
- `-r` — follow redirects

## Vhost brute-force

```bash
gobuster vhost -u http://target.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -t 50 --append-domain
```

- `--append-domain` — append target domain to each wordlist entry (`admin.target.com`)

