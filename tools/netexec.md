# NetExec

https://www.netexec.wiki/

Network service exploitation tool (successor to CrackMapExec). Automates enumeration, authentication, command execution, and lateral movement across Windows/Active Directory environments (SMB, LDAP, WinRM, MSSQL, etc.).

### Supported Protocols & Capabilities

| Protocol | Default Ports | Authentication | Enumeration & Recon | File Operations | Remote Command Execution | Post-Exploitation / Notes |
|---|---|---|---|---|---|---|
| `smb` | 445, 139 | NTLM/Kerberos, hashes (-H), local/domain auth | Shares (`--shares`), users, groups, sessions, domain info | `--ls`, `--get-file`, `--put-file` | Yes (if admin) via `-x`/`-X` - marked as `(Pwn3d!)` on success | Best for lateral movement. Can dump SAM, LSA, NTDS, DPAPI, and LSASS (via modules like `lsassy`, `nanodump`, etc). |
| `ldap` | 389, 636 (LDAPS) | NTLM/Kerberos (-k, -d) | Users, groups, computers, trusts, DCs, password policy (`--pso`), delegations, ASREProast/kerberoast (`--asreproast`, `--kerberoasting`), BloodHound collection, LAPS/gMSA discovery | Limited | No direct shell | Great for domain mapping and finding attack paths. Can run custom queries with `--query`. |
| `winrm` | 5985, 5986 | NTLM/Kerberos | Auth validation, host info | Varies by setup | Yes (`-x`/`-X`) if admin/root equivalent | Very common for Windows RCE. Often returns `(Pwn3d!)` on successful admin auth. |
| `wmi` | 135 (+ RPC) | NTLM/Kerberos, local/domain | System info, processes, host enumeration | Limited | Yes (`-x`/`-X`) if admin | Functionally similar to SMB admin access. Has protocol-specific modules. |
| `mssql` | 1433 | SQL auth or Windows (domain/local) auth | Databases, instances, linked servers, server config | None natively | Yes via `xp_cmdshell`. Enable with `-M enable_cmdshell` then use `-x` | Can run arbitrary SQL with `--query`. Useful for lateral movement via linked servers (`enum_links` module). |
| `rdp` | 3389 | NTLM/Kerberos | Auth validation | N/A | Yes (added in recent versions) via `-x`/`-X` | Can test auth and take screenshots (`--screenshot`). Full RCE support depends on version. |
| `vnc` | 5900 | VNC authentication | Auth validation, connectivity | N/A | Very limited/native support varies | Primarily for checking VNC auth and visual access. |
| `ssh` | 22 | Password or key-based | Auth validation, host info | SFTP-like operations depending on modules | Yes (`-x`/`-X`) if the user has shell privileges (root shown explicitly) | Great for Linux/Unix targets. |
| `ftp` | 21 | Anonymous or credentials | Directory listing, file enumeration (`--ls`) | Upload/download (`--put`, `--get`) | No typical remote shell execution | File-focused. |
| `nfs` | 2049 | Host-based/exports (depends on config) | Share/export enumeration | Read/write if exports are misconfigured | No standard remote shell | Unix file share access focused. |

Notes:
- `(Pwn3d!)` indicates the authenticated account has code-execution/admin rights on the target (most common with SMB/WinRM/WMI/RDP).
- Use `nxc <protocol> -L` to list modules, `-M <module> --options` for module parameters.

## Examples

```bash
# Authenticate to SMB
nxc smb <target> -u <user> -p <pass>

# Pass-the-hash
nxc smb <target> -u <user> -H <ntlmhash>

# Enumerate shares
nxc smb <target> -u <user> -p <pass> --shares

# Check local admin access
nxc smb <target> -u <user> -p <pass> --local-auth

# Execute command (if admin)
nxc smb <target> -u <user> -p <pass> -x "whoami"

# Enumerate users via LDAP
nxc ldap <target> -u <user> -p <pass> --users
```
