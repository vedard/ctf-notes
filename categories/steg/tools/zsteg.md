# zsteg

https://github.com/zed-0xff/zsteg

Detect steganography in PNG and BMP files (LSB, bit planes, alpha, textual chunks).

```bash
zsteg image.png
zsteg -a image.png          # all tests, slower
zsteg image.png -b 2        # check specific bitplane
```

Notes:
- Output is noisy — grep for `file:`, `text:`, `hex:` hits.
- PNG only; use `steghide` for JPEG/WAV/AU.
