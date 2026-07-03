# Orcho

[![PyPI](https://img.shields.io/pypi/v/orcho.svg)](https://pypi.org/project/orcho/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://pypi.org/project/orcho/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![CI](https://github.com/symphos-ai/orcho/actions/workflows/ci.yml/badge.svg)](https://github.com/symphos-ai/orcho/actions/workflows/ci.yml)
[![DCO](https://github.com/symphos-ai/orcho/actions/workflows/dco.yml/badge.svg)](https://github.com/symphos-ai/orcho/actions/workflows/dco.yml)
[![Release](https://github.com/symphos-ai/orcho/actions/workflows/release.yml/badge.svg)](https://github.com/symphos-ai/orcho/actions/workflows/release.yml)
[![codecov](https://codecov.io/gh/symphos-ai/orcho/branch/main/graph/badge.svg)](https://codecov.io/gh/symphos-ai/orcho)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/symphos-ai/orcho/badge)](https://scorecard.dev/viewer/?uri=github.com/symphos-ai/orcho)

Local-first control plane for cross-agent AI software delivery.

📖 **Documentation:** [docs.orcho.dev](https://docs.orcho.dev)

![One orcho run end to end, sped up: the opening envelope, the pipeline map, the plan contract, plan validation, implement subtasks with attestations, review, final acceptance, the delivery commit, and the closing rollup](https://raw.githubusercontent.com/symphos-ai/orcho-core/main/docs/assets/orcho-run-demo.gif)

<sub>One `orcho run` end to end (mock pipeline, sped up). Interactive version
with pause and scrub: [docs.orcho.dev](https://docs.orcho.dev).</sub>

This package is the recommended installer for the public Orcho command set. It
installs the full set by default — the core CLI and the MCP server. For a
minimal engine-only install, depend on `orcho-core` directly.

## Install

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
