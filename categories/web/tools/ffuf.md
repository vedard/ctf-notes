# ffuf

https://github.com/ffuf/ffuf

Fast web fuzzer written in Go. Replaces gobuster/wfuzz for path, vhost, parameter, and value fuzzing. The keyword `FUZZ` marks the injection point.

## Directory / file fuzzing

```bash
ffuf -u http://target/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
ffuf -u http://target/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -e .php,.txt,.bak
ffuf -u http://target/FUZZ -w wordlist.txt -mc 200,204,301,302,307,401,403
ffuf -u http://target/FUZZ -w wordlist.txt -fc 404 -fs 0
```

- `-mc` — match status codes, `-fc` — filter status codes
- `-fs` — filter by response size (drops wildcard/soft-404 noise)
- `-e` — extensions to append
- `-recursion -recursion-depth 2` — recurse into found directories
- `-k` — ignore TLS errors, `-H 'Cookie: ...'` — headers

## Vhost / subdomain fuzzing

```bash
ffuf -u http://target -H 'Host: FUZZ.target.com' -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -fs 4242
```

Filter on the baseline response size (`-fs`) or the default vhost gets reported for every word.

## Parameter and value fuzzing

```bash
ffuf -u 'http://target/index.php?FUZZ=1' -w params.txt -fs 4242
ffuf -u 'http://target/index.php?id=FUZZ' -w <(seq 1 1000) -fs 4242
ffuf -u http://target/login -X POST -d 'user=admin&pass=FUZZ' -w passwords.txt -fc 401
```

## Number ranges with `seq`

ffuf has no built-in range generator; feed it a wordlist from stdin (`-w -`) or process substitution.

```bash
# IDs 1..1000
seq 1 1000 | ffuf -u 'http://target/item?id=FUZZ' -w - -mc all -fs 0

# Zero-padded, e.g. 0001..5000 (useful for filenames / PINs)
seq -f '%04g' 1 5000 | ffuf -u 'http://target/uploads/FUZZ.jpg' -w -

# Custom step / format
seq 0 2 1000 | ffuf -u 'http://target/page/FUZZ' -w - -mc 200

# Multiple ranges without a file (process substitution works in bash/zsh)
ffuf -u 'http://target/user/FUZZ' -w <(seq 1 9999) -mc 200
```

- `-w -` reads the wordlist from stdin, one candidate per line.
- `seq START END` / `seq START STEP END` / `seq -f FORMAT START END` control the values and padding.
- Add `-o out.json -of json` to keep results, and `-c` for colored output on a TTY.

## Useful options

- `-t 100` — concurrency (default 40)
- `-rate 100` — requests per second cap
- `-ac` — auto-calibrate filters against a random baseline
- `-ic` — ignore comments in the wordlist
- `-s` — silent (only results)
- `-v` — full URL in output
- `-of csv|json|html|md` with `-o file` — structured output
