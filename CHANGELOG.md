# Changelog

## Unreleased

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
