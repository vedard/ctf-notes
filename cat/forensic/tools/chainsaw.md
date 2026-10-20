# chainsaw

https://github.com/WithSecureLabs/chainsaw

Search Windows Event Log (.evtx) files quickly (WithSecure). Great for Sysmon triage.

```bash
# All process-creation events (Sysmon Event ID 1), command lines via jq
chainsaw search -t 'Event.System.EventID: =1' Microsoft-Windows-Sysmon%4Operational.evtx --json \
  | jq -r '.[].Event.EventData.CommandLine'

# Free-text search
chainsaw search cmd.exe Microsoft-Windows-Sysmon%4Operational.evtx --json \
  | jq -r '.[].Event.EventData.CommandLine'
```

Useful fields for infection-chain reconstruction: `Image`, `ParentImage`, `ParentCommandLine`, `Hashes` (MD5), `UtcTime`.
