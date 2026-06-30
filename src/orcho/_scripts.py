"""Console-script dispatch for the Orcho convenience distribution."""

from __future__ import annotations

import importlib
import importlib.util
import sys
from collections.abc import Callable
from typing import NoReturn


def _load_callable(module_name: str, attr_name: str = "main") -> Callable[[], object]:
    module = importlib.import_module(module_name)
    target = getattr(module, attr_name)
    if not callable(target):
        msg = f"{module_name}:{attr_name} is not callable"
        raise TypeError(msg)
    return target


def _run(module_name: str, attr_name: str = "main") -> object:
    return _load_callable(module_name, attr_name)()


def _missing_optional(extra: str, command: str) -> NoReturn:
    package_name = f"orcho-{extra}"
    print(
        f"{command} requires the optional Orcho {extra} package.\n"
        f"Install it with:\n\n"
        f"  pipx install 'orcho[{extra}]'\n\n"
        f"For an existing pipx environment, inject the missing package:\n\n"
        f"  pipx inject orcho {package_name}\n",
        file=sys.stderr,
    )
    raise SystemExit(1)


def _ensure_optional_package(import_name: str, extra: str, command: str) -> None:
    if importlib.util.find_spec(import_name) is None:
        _missing_optional(extra, command)


def orcho_main() -> object:
    return _run("cli.orcho")


def orcho_run_main() -> object:
    return _run("pipeline.project_orchestrator")


def orcho_cross_main() -> object:
    return _run("pipeline.cross_project.cli")


def orcho_mcp_main() -> object:
    _ensure_optional_package("orcho_mcp", "mcp", "orcho-mcp")
    return _run("orcho_mcp.server")
