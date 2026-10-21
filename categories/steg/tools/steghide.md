# steghide

https://steghide.sourceforge.net/

Hide/extract data in WAV, BMP, JPEG, AU files. Classic LSB-ish stego with a passphrase.

```bash
steghide extract -sf image.jpg          # prompts for passphrase
steghide extract -sf image.jpg -p pass
steghide info image.jpg                 # embedded size, no passphrase needed
steghide embed -cf cover.jpg -ef secret.txt -p pass   # creating challenges
```

Empty passphrase is common in CTFs — just press enter. Related: `zsteg` (PNG/BMP), `outguess`, `stegsolve`.
