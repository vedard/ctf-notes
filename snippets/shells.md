# Reverse Shell Stabilization

```bash
python3 -c "import pty; pty.spawn('/bin/bash')"
# `Ctrl+Z`, then locally:
stty raw -echo; fg
```
