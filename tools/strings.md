# strings

https://man7.org/linux/man-pages/man1/strings.1.html

Print printable strings from any binary. The very first thing to run on a new file.

```bash
strings chal
strings -n 8 chal          # min length 8
strings chal | grep -i flag
```
