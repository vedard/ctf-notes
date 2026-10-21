# gcloud

https://cloud.google.com/sdk

Google Cloud CLI.

```bash
gcloud auth list                             # active identities
gcloud config list
gcloud projects list
gcloud compute instances list
gcloud storage ls gs://bucket               # Cloud Storage (was gsutil)
gcloud secrets list
```

- Active config/credentials: `~/.config/gcloud/`
- Compute metadata: `http://metadata.google.internal/computeMetadata/v1/` (needs `Metadata-Flavor: Google` header); service-account tokens at `.../instance/service-accounts/default/token`.
