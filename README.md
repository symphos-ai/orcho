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

This package is the recommended installer for the public Orcho command set. It
installs the core CLI by default and can include optional control surfaces with
Python extras.

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
pipx install "orcho[mcp]"
```

This installs the core commands plus the MCP server:

```bash
orcho --help
orcho-run --help
orcho-cross --help
orcho-mcp --help
```

Core commands only:

```bash
pipx install orcho
```

All optional public surfaces:

```bash
pipx install "orcho[all]"
```

Use quotes around extras in shells such as `zsh`.

### Alternative: project-managed environment

Use `pip` when you intentionally want Orcho inside the active virtual
environment, CI image, devcontainer, or Docker image.

```bash
python -m pip install "orcho[mcp]"
```

## Commands

```bash
orcho --help
orcho-run --help
orcho-cross --help
orcho-mcp --help
```

`orcho-mcp` requires `orcho[mcp]` or `orcho[all]`.

## Package Layout

- `orcho-core` provides the core engine and CLI.
- `orcho-mcp` provides the MCP server.

This package only coordinates installation and command dispatch.
