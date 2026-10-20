# AGENTS.md

Repository for personal CTF competition notes.

## Layout

```
.
├── AGENTS.md          # this file — structure + conventions (authoritative)
├── README.md          # short human overview, points here
├── references.md      # cross-category links
├── snippets/          # cross-category commands, copy-paste ready
├── tools/             # cross-category tool notes, setups
├── notes/             # cross-category exploit how-tos
└── cat/
    └── <category>/
        ├── snippets/  # category-specific commands
        ├── tools/     # category-specific tool notes
        ├── notes/     # category-specific exploit how-to
        ├── templates/ # starter files (payloads, scripts, skeletons)
        └── references.md  # category-specific links
```

Categories: `pwn`, `web`, `mobile`, `forensic`, `crypto`, `rev`, `misc`, `osint`.
Only categories with real content exist — create a directory when you add the first note.

## Conventions

- `snippets/` = frequently used commands: short, copy-paste ready, minimal explanation.
- `notes/` = **reusable technique notes**, not event writeups. Generalize one technique per file (what it is, when to reach for it, how it works, minimal steps). No challenge names, narratives, or "Full writeup" links — those live on the blog linked in `references.md`.
- `templates/` = reusable starting points: exploit skeletons, payload templates, config files. Per-category only.
- `tools/` = per-tool notes. Each tool note carries its own official link (homepage/repo) — never list a tool's link in `references.md`.
- `references.md` = links only, grouped by category, for material that is **not a tool** (blogs, writeups, docs, articles). Top level = cross-category; `cat/<category>/references.md` = category-specific. If a category has only tool links, do not create the file.
- Top-level folders hold cross-category material; anything category-specific goes under `cat/<category>/`.
- Use `.md` for notes, snippets, tools, and references.
- Do not commit empty directories or `.gitkeep` files — only real notes and their parent directories.
- No placeholder/stub files: a file is created only when it has real content.
