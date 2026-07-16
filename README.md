# Orcho

[![PyPI](https://img.shields.io/pypi/v/orcho.svg)](https://pypi.org/project/orcho/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://pypi.org/project/orcho/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![CI](https://github.com/symphos-ai/orcho/actions/workflows/ci.yml/badge.svg)](https://github.com/symphos-ai/orcho/actions/workflows/ci.yml)
[![DCO](https://github.com/symphos-ai/orcho/actions/workflows/dco.yml/badge.svg)](https://github.com/symphos-ai/orcho/actions/workflows/dco.yml)
[![Release](https://github.com/symphos-ai/orcho/actions/workflows/release.yml/badge.svg)](https://github.com/symphos-ai/orcho/actions/workflows/release.yml)
[![codecov](https://codecov.io/gh/symphos-ai/orcho/branch/main/graph/badge.svg)](https://codecov.io/gh/symphos-ai/orcho)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/symphos-ai/orcho/badge)](https://scorecard.dev/viewer/?uri=github.com/symphos-ai/orcho)

Orcho is a production harness and local-first control plane around AI coding
workers.

**Run one task. Watch Orcho plan, implement, reject false-ready work, repair
it, and prove what is ready to deliver.**

📖 **Documentation:** [docs.orcho.dev](https://docs.orcho.dev)

This package is the recommended installer for the public Orcho command set. It
installs the full set by default — the **core CLI** (`orcho-core`) and the
**MCP server** (`orcho-mcp`). For a minimal engine-only install, depend on
`orcho-core` directly.

Those are the two ways to drive Orcho, and both come with this package.

### Drive it yourself — the CLI

![One orcho run end to end, sped up: the opening envelope, the pipeline map, the plan contract, plan validation, implement subtasks with attestations, review, final acceptance, the delivery commit, and the closing rollup](https://raw.githubusercontent.com/symphos-ai/orcho-core/main/docs/assets/orcho-run-demo.gif)

<sub>`orcho run` end to end (mock pipeline, sped up): plan → validation →
implement → review → final acceptance → delivery, with a live phase stream and
an evidence rollup.</sub>

### Let your agent drive — MCP

![An AI client driving Orcho over MCP: it starts a mock run with orcho_run_start, watches it to a terminal state with orcho_run_watch, pulls the record with orcho_run_evidence and orcho_run_diff, and returns a short verdict](https://raw.githubusercontent.com/symphos-ai/orcho-mcp/main/docs/assets/orcho-mcp-demo.gif)

<sub>The same run, driven by an AI client (here Claude Code) through the MCP
server — `orcho_run_start` → `orcho_run_watch` → `orcho_run_evidence` → verdict,
all typed, no log scraping.</sub>

<sub>Both runs above are `mock=True`. Interactive, pausable versions:
[docs.orcho.dev](https://docs.orcho.dev).</sub>

## Install

Pick the install path by how isolated you want the run to be:

| Path | Use when | Command |
| --- | --- | --- |
| Native CLI with `pipx` | You trust the machine and want `orcho` on your shell `PATH`. | `pipx install orcho` |
| Docker | You want to try Orcho in a container, or keep agent CLIs and project tools isolated. | `docker pull ghcr.io/symphos-ai/orcho` |
| Project-managed `pip` | You intentionally want Orcho inside a virtualenv, CI image, devcontainer, or custom Docker image. | `python -m pip install orcho` |

If `pipx` is missing, install it first. On macOS with Homebrew:

```bash
brew install pipx
pipx ensurepath
exec zsh -l
```

For Linux or Windows, use the
[official pipx installation guide](https://pipx.pypa.io/stable/installation/).

### Recommended: isolated CLI install

Use `pipx` when you want Orcho commands available from your shell without
installing Orcho into the current project or Python environment.

```bash
pipx install orcho
```

This installs the core commands plus the MCP server:

```bash
orcho --help
orcho-run --help
orcho-cross --help
orcho-mcp --help
```

Engine and core CLI only, without the MCP server:

```bash
python -m pip install orcho-core
```

`orcho[mcp]` and `orcho[all]` remain as back-compat aliases; since 0.1.1 they
install the same set as plain `orcho`.

### Try without installing: Docker

Use Docker when you want to run Orcho in an isolated container while mounting
only the current project and an explicit credential directory.

```bash
docker pull ghcr.io/symphos-ai/orcho
alias orcho='docker run --rm -it \
  -v "$PWD":/workspace \
  -v ~/.orcho-auth:/agent-auth:ro \
  ghcr.io/symphos-ai/orcho orcho'

orcho run --project /workspace --task "Add input validation to the login endpoint."
orcho status
```

See [docker/README.md](docker/README.md) for the one-time credential bootstrap,
MCP stdio setup, and project-toolchain extension pattern.

### Alternative: project-managed environment

Use `pip` when you intentionally want Orcho inside the active virtual
environment, CI image, devcontainer, or Docker image.

```bash
python -m pip install orcho
```

## Commands

```bash
orcho --help
orcho-run --help
orcho-cross --help
orcho-mcp --help
```

## Package Layout

- `orcho-core` provides the core engine and CLI.
- `orcho-mcp` provides the MCP server.

This package only coordinates installation and command dispatch.
