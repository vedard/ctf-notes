# AWS CLI

https://aws.amazon.com/cli/

Query and manage AWS resources. In cloud CTF challenges, first figure out what identity you hold and what it can reach.

```bash
aws sts get-caller-identity                      # who am I?
aws sts get-caller-identity --profile ctf
aws s3 ls                                        # list buckets
aws s3 cp s3://bucket/flag.txt -                 # read object
aws iam list-attached-user-policies --user-name u
aws ec2 describe-instances --query "Reservations[].Instances[].PublicIpAddress"
```

Credentials come from env vars (`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`), `~/.aws/credentials` profiles (`--profile`), or an instance/task metadata service at `http://169.254.169.254/` (IMDSv2 needs a token header first).
