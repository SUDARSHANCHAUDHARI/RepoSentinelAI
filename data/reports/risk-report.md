# RepoSentinel AI Risk Report

- Findings: 4
- Risk score: 100/100
- Risk level: high

## Priority Queue

### 1. File contains credential-like material.

- Severity: `critical`
- Type: `secret.aws_access_key`
- Path: `app.py`
- Evidence: `{"line": 1, "path": "app.py", "preview": "AWS_ACCESS_KEY_ID = \"[REDACTED]\""}`
- Suggested fix: Remove the secret from git history, rotate it, and load it from a secret manager or environment variable.

### 2. Python dependency is not pinned.

- Severity: `medium`
- Type: `dependency.unpinned_python`
- Path: `requirements.txt`
- Evidence: `{"dependency": "fastapi", "line": 1, "path": "requirements.txt"}`
- Suggested fix: Pin the dependency to a reviewed version and enable dependency scanning.

### 3. Dockerfile uses a latest base image tag.

- Severity: `medium`
- Type: `docker.latest_base`
- Path: `Dockerfile`
- Evidence: `{"path": "Dockerfile"}`
- Suggested fix: Use a pinned base image and run the container as a non-root user.

### 4. Dockerfile does not set a non-root USER.

- Severity: `medium`
- Type: `docker.root_user`
- Path: `Dockerfile`
- Evidence: `{"path": "Dockerfile"}`
- Suggested fix: Use a pinned base image and run the container as a non-root user.
