# cchef

https://github.com/roberson-io/cchef

CyberChef on the command line. Every operation is a subcommand that reads stdin/args and writes stdout, so operations chain through pipes or run as a single recipe. Good when the web GUI is unavailable or the data shouldn't leave the terminal.

```bash
echo -n "hello" | cchef from-base32 | cchef xor --key "Sp00ky" --key-type latin1
cchef to-base64 "hello"
cchef sha256 -i 'Hello, World!'
cchef magic -i "41 42 43"                       # auto-detect encoding
cchef bake -e "To_Base64()To_Hex()" "hello"     # run a full recipe at once
cchef list                                      # all operations, by category
```