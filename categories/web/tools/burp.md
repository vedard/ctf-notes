# Burp Suite

https://portswigger.net/burp

Intercepting proxy and manual testing suite. Route browser traffic through it, then manipulate requests in Repeater and fuzz in Intruder.

## Features

- **Proxy → HTTP history** — filter by status/length/type; right-click → *Send to Repeater* (Ctrl+R) / *Send to Intruder* (Ctrl+I).
- **Repeater** — manual request tweaking; split/response view, Ctrl+Space autocomplete, pin tabs into groups for multi-step flows (login → exploit).
- **Intruder** — set attack positions on the request, load payloads, *Start attack*.
  - `Sniper` = one position at a time; `Pitchfork`/`Battering ram`/`Cluster bomb` for multiple positions.
  - Free edition throttles Intruder — attack small payload lists, or filter first with a custom filter.

## Useful tricks

- **Match & replace** (Proxy → Options) — strip/rewrite headers on the fly (drop `X-Forwarded-For`, inject auth headers, downgrade HTTPS→HTTP for header reflection tests).
- **Scope** (Target → Scope) — keep history clean; right-click host → *Add to scope* and turn on "drop items out of scope".
- **Copy as curl / paste as curl** — right-click a request to move traffic between Burp and the terminal.
- **Extensions (BApp Store)** — common picks: *Turbo Intruder* (fast/large fuzzing, HTTP/2), *Param Miner* (hidden parameter discovery), *Authz* (authz/IDOR checks), *Jython/JRuby* for legacy scan checks.

