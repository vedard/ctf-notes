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

## Hunting with sigma + jq

```bash
# Sigma hunt over a whole winevt directory (run from chainsaw's mappings/ parent)
chainsaw hunt /mnt/C/Windows/System32/winevt/logs/ \
  -s sigma --mapping mappings/sigma-event-logs-all.yml

# Filter to one EventID (space before '=' matters), output JSON, extract fields
chainsaw search --tau='Event.System.EventID: =4688' /mnt/C/Windows/System32/winevt/logs -j \
  | jq -r '.[].Event.EventData | [.NewProcessName, .ParentProcessName] | @tsv'
```

Common EventIDs: `1` (Sysmon process create), `4104` (Script Block Logging), `4624` (logon), `4688` (process create).
