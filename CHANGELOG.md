# Changelog

## Unreleased

## 0.9.0 - 2026-08-29

A re-pin release: this package carries no code of its own, and the floors now
name the versions the set is actually tested against.

### Changed

- Requires `orcho-core>=0.9.0` and `orcho-mcp>=0.8.2`. The previous floors
  capped `orcho-core` below 0.9, so an install would have held users on an
  engine that cannot tell a working run from one that ceased to exist —
  the liveness predicate behind both the `stalled` verdict and
  `repair-state`'s orphan repair could never fire on a real run, because the
  reader rejected the timestamps the event writer emits.

  Those releases also carry: `orcho workspace init` as a decision surface
  instead of a scaffolder that wrote a `plugin.py` nothing reads, plus a new
  `orcho workspace mcp`; a verification gate that ran clean but cannot be
  proven no longer reported as a failing test suite; a paused gate that tells
  the operator what was rejected instead of an empty summary; `pre_run_dirty`
  intake that can seed an untracked directory; and, on Windows, a launched run
  that asks to break out of the launcher's job object.


## 0.8.6 - 2026-08-26

A version-identity release. The dependency ranges meant a new install always
received the current engine, so nothing was broken about what people ran — but
this package had stood at 0.8.0 since 20 August while `orcho-core` shipped four
releases, so `pip list` and this package's PyPI page both understated the
project by a month. Field reports arrived reading "orcho 0.8.0, orcho-core
0.8.4", which is confusing in exactly the situation where clarity matters most.

### Changed

- Requires `orcho-core>=0.8.6` and `orcho-mcp>=0.8.1`. The floors now name the
  versions this release is actually tested against, so the umbrella version is
  a statement about the set rather than a number that drifts away from it.
  Those releases carry: bounded service subprocesses and real process-tree
  ownership on Windows; a detached launch that no longer inherits the
  launcher's stdin; a run that cannot advance no longer reporting as active,
  and `repair-state` able to finalise it; the GLM adapter owning its own CLI
  configuration directory; and a profile-declared phase effort finally
  reaching the run.

## 0.8.0 - 2026-08-20

### Changed

- Requires the `orcho-core` and `orcho-mcp` 0.8.0 line, the Windows onboarding
  release: UTF-8 git output on non-UTF-8 consoles, a concurrent stderr drain
  that fixes a cross-platform child-process deadlock, sandbox passthrough for
  the GLM auth token, and a fail-fast guard for over-long Windows command
  lines. `claude-glm` setup moved into the runtime adapter; the packaged
  wrapper scripts and `orcho runtimes install` are gone.

## 0.7.0 - 2026-08-11

### Changed

- Depends on the `orcho-core` and `orcho-mcp` 0.7 line
  (`>=0.7.0,<0.8`), which adds typed verification-command timeouts,
  honest delivery decidability for stopped runs, and retention-aware
  workspace cleanup with a confirmed MCP reclaim surface.

## 0.6.0 - 2026-07-28

### Changed

- Depends on the `orcho-core` and `orcho-mcp` 0.6 line
  (`>=0.6.0,<0.7`).
- Release-path GitHub Actions use immutable pins and CodeQL covers protected
  release branches.

### Removed

- Removed the unresolved `[tui]` extra. The reserved `orcho tui` command no
  longer advertises an unpublished installation package.

## 0.5.0 - 2026-07-23

### Changed

- Depends on the `orcho-core` and `orcho-mcp` 0.5 line (`>=0.5.0,<0.6`).
- Reports the installed distribution version instead of a stale package
  constant.

## 0.4.0 - 2026-07-08

### Changed

- Depends on the `orcho-core` and `orcho-mcp` 0.4 line (`>=0.4.0,<0.5`).

## 0.3.0 - 2026-07-06

### Added

- Reserved the `orcho tui` command for a separately provided terminal
  interface.

### Changed

- Depends on the `orcho-core` and `orcho-mcp` 0.3 line (`>=0.3.0,<0.4`).

## 0.2.0 - 2026-07-05

### Changed

- Depends on the `orcho-core` and `orcho-mcp` 0.2 line (`>=0.2.0,<0.3`).

### Fixed

- Docker image CVE hygiene and a git-identity fallback for commits made inside
  the container.
- Docker workspace default and persistence behavior.

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
