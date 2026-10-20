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
- `notes/` = full-detail writeups: context, vulnerability, step-by-step exploitation, lessons learned.
- `templates/` = reusable starting points: exploit skeletons, payload templates, config files. Per-category only.
- `references.md` = links only, grouped by category. Top level = cross-category links; `cat/<category>/references.md` = category-specific.
- Top-level folders hold cross-category material; anything category-specific goes under `cat/<category>/`.
- Use `.md` for notes, snippets, and references.
- Do not commit empty directories or `.gitkeep` files — only real notes and their parent directories.
- No placeholder/stub files: a file is created only when it has real content.
