# SecLists

https://github.com/danielmiessler/SecLists

The standard wordlist collection. Passwords, usernames, web paths, DNS names, and injection payloads, maintained for pentesting and CTFs.

```bash
# Kali/Debian package — already installed at /usr/share/seclists
ls /usr/share/seclists

# Otherwise clone it
git clone https://github.com/danielmiessler/SecLists.git
```

## Most used wordlists

### Passwords

| Wordlist | Path (under the SecLists root) | Size | Use |
|---|---|---|---|
| best1050 | `Passwords/Common-Credentials/best1050.txt` | 1 049 | default/most common — try this first |
| 10k most common | `Passwords/Common-Credentials/10k-most-common.txt` | 10 000 | still fast, covers more |
| xato top 100k | `Passwords/Common-Credentials/xato-net-10-million-passwords-100000.txt` | 100 000 | ranked list for `john`/`hashcat` |
| darkweb 2017 | `Passwords/Common-Credentials/darkweb2017_top-10000.txt` | 10 000 | leaked-password corpus |
| darkc0de | `Passwords/darkc0de.txt` | 1.4 M | generic bulk list |
| rockyou | `Passwords/Leaked-Databases/rockyou.txt` | 14 M | the classic (upstream ships `rockyou.txt.tar.gz`) |
| default credentials | `Passwords/Default-Credentials/` | — | routers, DBs, cameras, appliances |
| JWT secrets | `Passwords/scraped-JWT-secrets.txt` | 1.1 M | brute-forceable JWT HMAC keys (`hashcat -m 16500`) |

### Usernames

| Wordlist | Path | Size | Use |
|---|---|---|---|
| shortlist | `Usernames/top-usernames-shortlist.txt` | small | `hydra -L` when you need volume |
| names | `Usernames/Names/names.txt` | 10 735 | common first names |
| xato usernames | `Usernames/xato-net-10-million-usernames.txt` | 10 M | last resort |

### Web content

| Wordlist | Path | Size | Use |
|---|---|---|---|
| dirb common | `Discovery/Web-Content/common.txt` | 4 750 | fastest path brute-force |
| DirBuster medium | `Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt` | 220 k | good default for CTF |
| DirBuster big | `Discovery/Web-Content/DirBuster-2007_directory-list-2.3-big.txt` | ~2 M | thorough, slow |
| raft directories | `Discovery/Web-Content/raft-medium-directories.txt` | medium | alternative to DirBuster |
| quickhits | `Discovery/Web-Content/quickhits.txt` | — | admin/login panels |
| api endpoints | `Discovery/Web-Content/api/api-endpoints.txt` | — | REST paths |
| graphql | `Discovery/Web-Content/graphql.txt` | — | GraphQL routes |
| logins | `Discovery/Web-Content/Logins.fuzz.txt` | — | login page paths |
| per-language | `Discovery/Web-Content/Programming-Language-Specific/` | — | php, java, ruby, etc. paths |

### DNS

| Wordlist | Path | Size | Use |
|---|---|---|---|
| subdomains | `Discovery/DNS/subdomains-top1million-5000.txt` | 5 000 | subdomain brute-force |
| subdomains | `Discovery/DNS/subdomains-top1million-20000.txt` | 20 000 | larger sweep |
| hostnames | `Discovery/DNS/namelist.txt` | — | vhost / host header brute-force |

### Payload lists (for fuzzing, not guessing)

| Wordlist | Path | Use |
|---|---|---|
| unix attacks | `Fuzzing/UnixAttacks.fuzzdb.txt` | command injection payloads |
| commix | `Fuzzing/command-injection-commix.txt` | command injection payloads |
| LFI | `Fuzzing/LFI/LFI-Jhaddix.txt` | local/remote file inclusion |
| XSS | `Fuzzing/XSS/human-friendly/` | XSS payloads |
| format string | `Fuzzing/FormatString-Jhaddix.txt` | format string payloads |
| SQLi | `Fuzzing/Databases/SQLi/` | SQL injection payloads |

## Usage

```bash
# Directory / vhost brute-force
gobuster dir -u http://target -w /usr/share/seclists/Discovery/Web-Content/common.txt
gobuster vhost -u http://target -w /usr/share/seclists/Discovery/DNS/namelist.txt

# Online password brute-force
hydra -l admin -P /usr/share/seclists/Passwords/Common-Credentials/best1050.txt <target> ssh

# Offline hash cracking
john --wordlist=/usr/share/seclists/Passwords/Common-Credentials/xato-net-10-million-passwords-100000.txt hash

# Subdomain enumeration
dnsrecon -d target -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

Notes:
- Paths differ between a clone and the distro package: the clone is `SecLists/Discovery/...`, the package is `/usr/share/seclists/Discovery/...`. Kali also ships rockyou at `/usr/share/wordlists/rockyou.txt`.
- Unpack rockyou once: `tar -xzf Passwords/Leaked-Databases/rockyou.txt.tar.gz`.
- Start small. `best1050` and `common.txt` solve most CTF logins; escalate only when they fail.
- For online brute-force stay on a ranked small list — big lists cost lockouts and timeouts.
- Find what is not in this table: `find /usr/share/seclists -name '*.txt' -size +1M`.
