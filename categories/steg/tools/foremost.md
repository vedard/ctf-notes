# foremost

https://en.wikipedia.org/wiki/Foremost

Carve embedded files out of a blob by file signature. Sibling of binwalk; try both — one finds what the other misses.

```bash
foremost -i file.bin -o output/
foremost -t all -i file.bin -o output/   # all built-in types
```

Useful options:
- `-o` — output dir (must not already exist or be non-empty)
- `-t png,jpg,pdf` — restrict to given types
- `-T` — time stamp output dirs
