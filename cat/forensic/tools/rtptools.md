# rtptools

https://github.com/irtlab/rtptools

Contains `rtpplay`, which replays an RTP stream (rtpdump file) with its original timing, sending it to a UDP host/port. Pair it with `ffmpeg` listening on an SDP to rebuild a video/audio stream carved out of a packet capture.

Two-terminal workflow to reconstruct an RTSP/RTP stream (e.g. an H.264 camera feed) from a pcap:

1. In Wireshark, note the SDP from the `DESCRIBE` response (`a=rtpmap` codec, payload type), then `Telephony > RTP > RTP Streams` and export the stream as rtpdump (`.rtp`).
2. Write `stream.sdp` matching that stream:

```text
v=0
o=- 0 0 IN IP4 127.0.0.1
s=capture
c=IN IP4 127.0.0.1
t=0 0
m=video 5004 RTP/AVP 96
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1
```

3. Terminal 1 — start `ffmpeg` first so it is listening before the replay:

```bash
ffmpeg -protocol_whitelist file,udp,rtp -analyzeduration 20M -probesize 20M \
  -i stream.sdp -c:v libx264 -pix_fmt yuv420p -preset fast out.mp4
```

4. Terminal 2 — replay the capture:

```bash
rtpplay -T -f capture.rtp 127.0.0.1/5004
```

5. When `rtpplay` finishes, press `q` in the `ffmpeg` terminal to finalize `out.mp4`.

- `-T` — use the original timing from the dump (needed for continuous playback).
- Start `ffmpeg` before `rtpplay`, otherwise the early packets are lost.
- If the stream won't decode, check the SDP payload type / codec against the RTP packets and confirm `packetization-mode`.
