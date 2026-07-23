# Orcho in Docker

Run Orcho fully isolated in a container instead of installing it with
`pipx`. Your project is mounted into the container, the agent CLIs run
inside it, and only the resulting changes land back in your working
tree.

```bash
docker pull ghcr.io/symphos-ai/orcho
```

## Quick start

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -v ~/.orcho-auth:/agent-auth:ro \
  ghcr.io/symphos-ai/orcho \
  orcho run --project /workspace --task "<task>"
```

Make it feel like a native CLI:

```bash
alias orcho='docker run --rm -it \
  -v "$PWD":/workspace \
  -v ~/.orcho-auth:/agent-auth:ro \
  ghcr.io/symphos-ai/orcho orcho'

orcho run --project /workspace --task "Add input validation to the login endpoint."
orcho status
```

Run state and evidence land in the container-internal Orcho workspace
(`ORCHO_WORKSPACE=/orcho-workspace`), never inside your mounted project.
Add `-v ~/.orcho-workspace:/orcho-workspace` to keep run history across
containers; without it, history disappears with the container.

## One-time credential setup

The agent CLIs inside the image start logged out. Put credentials in a
directory (e.g. `~/.orcho-auth`) and mount it at `/agent-auth`; the
entrypoint installs them before your command runs.

| File in `/agent-auth` | Installed to | Source on your machine |
| --- | --- | --- |
| `claude-credentials.json` | `~/.claude/.credentials.json` | see below |
| `codex-auth.json` | `~/.codex/auth.json` | `~/.codex/auth.json` |
| `gitconfig` | `~/.gitconfig` | your `~/.gitconfig` |

```bash
mkdir -p ~/.orcho-auth && chmod 700 ~/.orcho-auth

# claude — macOS stores subscription credentials in the keychain:
security find-generic-password -s "Claude Code-credentials" -w \
  > ~/.orcho-auth/claude-credentials.json
# claude — Linux stores them in a file instead:
cp ~/.claude/.credentials.json ~/.orcho-auth/claude-credentials.json

# codex — subscription tokens live in a file on every platform:
cp ~/.codex/auth.json ~/.orcho-auth/codex-auth.json

# git identity for delivery commits:
cp ~/.gitconfig ~/.orcho-auth/gitconfig
```

API keys work as environment variables instead of files:

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -e ANTHROPIC_API_KEY \
  -e OPENAI_API_KEY \
  -e GEMINI_API_KEY \
  ghcr.io/symphos-ai/orcho \
  orcho run <task>
```

`OPENAI_API_KEY` is written to `~/.codex/auth.json` inside the
container when no `codex-auth.json` file is provided; the other keys
are read directly by their CLIs.

Pushing from inside the container additionally needs an SSH key or
token (`-v ~/.ssh:/root/.ssh:ro`, or a `GITHUB_TOKEN`-style env var
your remote accepts). Local-only delivery (the default) needs none.

## MCP server

The image also carries the MCP server, so an MCP client can drive a
containerized Orcho over stdio. Mount the workspace parent directory and bind
the server to the workspace inside the container:

```json
{
  "mcpServers": {
    "orcho": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-v", "/path/to/my-workspace:/workspace",
        "-v", "/home/you/.orcho-auth:/agent-auth:ro",
        "-e", "ORCHO_WORKSPACE=/workspace/workspace-orchestrator",
        "ghcr.io/symphos-ai/orcho", "orcho-mcp"
      ]
    }
  }
}
```

Inside that server, projects live under `/workspace/<project-name>`.

## Project toolchain

Verification phases run your project's own tests inside the container.
The base image ships Python and Node toolchains; for anything else,
extend it:

```dockerfile
FROM ghcr.io/symphos-ai/orcho
RUN apt-get update && apt-get install -y --no-install-recommends \
    <your build deps> && rm -rf /var/lib/apt/lists/*
```

Teams with an existing devcontainer can instead install Orcho and the
agent CLIs into that image; this Dockerfile is a working reference for
the required pieces.

## Security scanning

Scanners such as `docker scout` report CVEs inherited from the Debian
base and from `git`'s dependency chain (notably `perl`); most carry
"Fixed version: not fixed" upstream and appear in virtually every
Debian-based image, including the official `python` and `node` bases.
The weekly rebuild picks up Debian, npm, and pip security updates as
they are released, and `npm`/`pip` are upgraded at build time so
fixable advisories in the tooling do not linger. Pull `:latest` (or
rebuild from this Dockerfile) to pick up the current state.

## Notes

- The container runs as root with `IS_SANDBOX=1` (required by the
  claude CLI for non-interactive root operation). On Linux hosts,
  files created in the mounted workspace are root-owned; `chown` them
  afterwards or run with a matching `--user` and adjust `HOME`
  handling accordingly.
- On macOS, bind-mount file I/O is slower than native disk. For
  worktree-heavy runs the native `pipx` install remains the faster
  option; the container trades speed for isolation.
- Non-interactive runs (`--no-interactive`, CI) must pass an explicit
  `--profile` (e.g. `--profile task`); interactive runs prompt for one.
- Delivery commits are authored as `Orcho Container
  <orcho@container.local>` unless you provide a `gitconfig` in
  `/agent-auth` or set `GIT_AUTHOR_*`/`GIT_COMMITTER_*` variables —
  supply your identity for commits you intend to keep.
- Version tags mirror the `orcho` package (`:0.1.1`, `:latest`). The
  image is also rebuilt on a weekly schedule so the bundled agent CLIs
  stay current.
