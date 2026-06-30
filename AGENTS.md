# orcho Instructions

## Scope

This file applies to `orcho/`.

`orcho` is the Apache-2.0 public convenience distribution for installing the
Orcho command set. Runtime implementation lives in sibling public packages such
as `orcho-core` and `orcho-mcp`; this package should stay small and only own
packaging metadata plus console-script dispatch.

Also obey the workspace-level `../AGENTS.md`.

## Workspace Development Pipeline

When working on this repo inside the Orcho workspace, follow
`../DEVELOPMENT_PIPELINE.md`. That manual pipeline governs direct source
development only; it is separate from Orcho-managed worktree runs.

## Package Boundary

- Keep `orcho-core` as the required dependency.
- Keep MCP as an optional extra.
- Do not copy implementation code from sibling packages into this package.
- Wrapper scripts may import sibling packages at command runtime and should
  print a concise install hint when an optional extra is missing.
