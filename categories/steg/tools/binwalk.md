# binwalk

https://github.com/ReFirmLabs/binwalk

Find embedded files and data inside another file. Standard first step on unknown blobs.

```bash
binwalk file.bin
binwalk -e file.bin          # extract found files (uses --dd by default)
binwalk -E file.bin          # entropy plot (spikes = encrypted/compressed regions)
```

Useful options:
- `-e` — extract files to `./_file.bin.extracted/`
- `-D ext:outdir` — extract only a given type, e.g. `-D png:out`
- `-A` — search for common opcodes (architecture guess)
- `--dd='.*'` — carve everything, useful when signatures fail
