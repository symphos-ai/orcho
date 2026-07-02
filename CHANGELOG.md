# Changelog

## Unreleased

## 0.1.1 - 2026-07-02

Full command set by default.

### Changed

- `pipx install orcho` now installs the full public command set: the MCP
  server package (`orcho-mcp`) moved from the `[mcp]`/`[all]` extras into the
  base dependencies.
- The `[mcp]` and `[all]` extras remain as no-op back-compat aliases for
  install commands already published in documentation.

### Known Notes

- For a minimal engine-only install, depend on `orcho-core` directly.

## 0.1.0 - 2026-07-01

Initial release baseline for `orcho`.

### Added

- Public convenience distribution for installing the Orcho command set.
- Default `orcho-core` dependency for the core CLI commands.
- Optional `mcp` and `all` extras for installing the MCP server package.
- Console-script dispatch for `orcho`, `orcho-run`, `orcho-cross`, and
  `orcho-mcp`.

### Known Notes

- `orcho-mcp` requires installing `orcho[mcp]` or `orcho[all]`.
