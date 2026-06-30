# Orcho

[![PyPI](https://img.shields.io/pypi/v/orcho.svg)](https://pypi.org/project/orcho/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://pypi.org/project/orcho/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![DCO](https://github.com/symphos-ai/orcho/actions/workflows/dco.yml/badge.svg)](https://github.com/symphos-ai/orcho/actions/workflows/dco.yml)

Local-first control plane for cross-agent AI software delivery.

This package is the recommended installer for the public Orcho command set. It
installs the core CLI by default and can include optional control surfaces with
Python extras.

## Install

Core CLI:

```bash
pipx install orcho
```

Core CLI plus MCP server:

```bash
pipx install 'orcho[mcp]'
```

Everything:

```bash
pipx install 'orcho[all]'
```

Use quotes around extras in shells such as `zsh`.

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
