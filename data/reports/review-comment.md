# RepoSentinel AI Security Review

## File contains credential-like material.

- Severity: `critical`
- Type: `secret.aws_access_key`
- Path: `app.py`
- Suggestion: Remove the secret from git history, rotate it, and load it from a secret manager or environment variable.

## Python dependency is not pinned.

- Severity: `medium`
- Type: `dependency.unpinned_python`
- Path: `requirements.txt`
- Suggestion: Pin the dependency to a reviewed version and enable dependency scanning.

## Dockerfile uses a latest base image tag.

- Severity: `medium`
- Type: `docker.latest_base`
- Path: `Dockerfile`
- Suggestion: Use a pinned base image and run the container as a non-root user.

## Dockerfile does not set a non-root USER.

- Severity: `medium`
- Type: `docker.root_user`
- Path: `Dockerfile`
- Suggestion: Use a pinned base image and run the container as a non-root user.
