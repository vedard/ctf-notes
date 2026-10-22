# nmap

https://nmap.org/

Network scanner. First step on almost every challenge: find open ports, identify the service and version, then pivot to a category-specific tool.

```bash
nmap -sV -sC -p- <target>
nmap -sV -sC -p- -oN scan.txt <target>      # save output
nmap -sV -sC -p- --open <target>            # only open ports
nmap -Pn -p 80,443,8080 <target>            # skip ping, specific ports
nmap -sn 10.0.0.0/24                        # host discovery only
nmap -sU --top-ports 20 <target>            # UDP scan
nmap -A <target>                            # aggressive: -sV -sC -O + traceroute
```

Useful options:
- `-sV` — service/version detection
- `-sC` — run default NSE scripts
- `-p-` — all 65535 ports
- `-Pn` — treat host as up without pinging (CTF hosts often drop ICMP)
- `-n` — no DNS resolution (faster, keeps output numeric)
- `--script=vuln` / `--script http-enum` — NSE scripts
- `-T4` — faster timing
- `-oA out` — output in all formats

CTF notes:
- A filtered host still answers TCP scans — `-Pn` avoids the "host seems down" false negative.
- Version banners often leak the exact software (and therefore the matching exploit or CVE).
- `--script http-title,http-enum` is a cheap way to find hidden vhosts and paths; pair with `gobuster`.
