# tshark

https://www.wireshark.org/tshark.html

Command-line packet analyzer. Same dissectors as Wireshark, scriptable — the right tool for large pcaps, filtering, and bulk extraction.

```bash
tshark -r cap.pcap                                    # dump packets
tshark -r cap.pcap -Y "http.request"                  # display filter
tshark -r cap.pcap -Y "tcp.stream eq 0" -x            # hex dump one stream
tshark -r cap.pcap -T fields -e http.request.method -e http.request.uri
tshark -r cap.pcap -q -z conv,tcp                     # conversations
tshark -r cap.pcap -q -z io,stat,0                     # traffic volume per second
tshark -r cap.pcap -Y dns -T fields -e dns.qry.name   # DNS queries
tshark -r cap.pcap -Y "tcp.flags.syn==1 && tcp.flags.ack==0" -w syn.pcapng
tshark -r cap.pcap --export-objects http,outdir        # carve HTTP objects
```

Useful options:
- `-Y <filter>` — display filter (Wireshark syntax); `-R` is the old name
- `-T fields -e <field>` — print selected columns only
- `-x` — hex + ASCII dump of the packet
- `-q -z <stat>` — statistics (`conv,tcp`, `io,stat,0`, `http,tree`)
- `--export-objects <proto>,<dir>` — save transferred files (http, ftp, tftp, dcom)
- `-w <file>` — write the filtered capture to a new file
- `-c <count>` — stop after N packets

CTF notes:
- Start with `-z conv,tcp` to find the interesting stream, then pull it with `-Y "tcp.stream eq N" -x`.
- `--export-objects http,outdir` recovers uploaded and downloaded files straight from a pcap — the fastest route to an "uploaded a flag file" challenge.
- `-T fields -e ...` turns a pcap into grep-able text; combine with `sort -u` to list unique URLs, DNS names, or User-Agents.
- Extract objects from a stream instead of the whole capture: `-Y "http.request" --export-objects http,outdir`.
