# Azure CLI

https://github.com/Azure/azure-cli

Query and manage Azure resources (`az`).

```bash
az login --identity                   # managed identity (common on compromised VMs)
az account list -o table
az role assignment list --assignee $(az ad signed-in-user show --query id -o tsv)
az storage account list -o table
az keyvault secret list --vault-name vlt --query "[].id" -o tsv
az vm list-ip-addresses -o table
```

- Config/credentials live under `~/.azure/`; a leaked `accessTokens.json` is a foothold.
- VM metadata endpoint: `http://169.254.169.254/metadata/instance?api-version=2021-02-01` (needs `Metadata: true` header).
