# 🔓 Leaky Box — Container Security Review

**Scenario:** A developer handed over a container that "works fine." I reviewed it, found two security problems plus a leftover risk, fixed them, and proved the fixes worked.

## Findings

| # | Finding | Risk | Fix | Proof |
| --- | --- | --- | --- | --- |
| 1 | Container ran as **root** | An attacker who breaks into the app gets full control of the container and an easier path to the host | Added a non-root user (`useradd` + `USER appuser`) | `docker exec leaky whoami` → `appuser` |
| 2 | **Secret baked into the image** with `ENV` | Anyone with a copy of the image can read it with `docker history` or `docker inspect` — no hacking needed | Removed `ENV`; passed the secret at run time with `-e` | `docker history leaky-app` → no secret |
| 3 | **Old leaky image left behind** after the rebuild | The untagged old image still contained the secret | Deleted it with `docker image prune` | `docker images` → no `<none>` image |

## How I found the secret

The app never shows the secret on its webpage, but the image layers do:

```bash
docker history leaky-app
docker inspect leaky-app --format '{{.Config.Env}}'
```

## Files

- [`Dockerfile.bad`](Dockerfile.bad) — the original, insecure version
- [`Dockerfile`](Dockerfile) — the fixed version
- [`app.py`](app.py) — a Flask app that reports whether a secret was loaded, without revealing it

## Run the fixed version

```bash
docker build -t leaky-app .
docker run -d -p 8080:5000 --name leaky -e SECRET_CODE=your-value leaky-app
```

## What I learned

- **Fixing the Dockerfile doesn't erase old images.** Old copies keep the secret until they're deleted.
- **Once a real secret is baked into an image, assume it leaked and rotate it.**
- **Encrypting a secret inside the image doesn't help** — the decryption key would have to be in the image too.
- `-e` keeps secrets out of the image, but in production, secrets should come from a secrets manager.
