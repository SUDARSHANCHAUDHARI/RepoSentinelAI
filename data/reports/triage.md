# RepoSentinel AI Triage

## Remediation Checklist

- [ ] `critical` secret.aws_access_key in `app.py`: Remove the secret from git history, rotate it, and load it from a secret manager or environment variable.
- [ ] `medium` dependency.unpinned_python in `requirements.txt`: Pin the dependency to a reviewed version and enable dependency scanning.
- [ ] `medium` docker.latest_base in `Dockerfile`: Use a pinned base image and run the container as a non-root user.
- [ ] `medium` docker.root_user in `Dockerfile`: Use a pinned base image and run the container as a non-root user.
