from __future__ import annotations

import sys
import types

import pytest

from orcho import _scripts


def _module_with_main(return_value: int) -> types.ModuleType:
    module = types.ModuleType("test_module")

    def main() -> int:
        return return_value

    module.main = main  # type: ignore[attr-defined]
    return module


def test_orcho_main_dispatches_to_core_cli(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sys.modules, "cli", types.ModuleType("cli"))
    monkeypatch.setitem(sys.modules, "cli.orcho", _module_with_main(7))

    assert _scripts.orcho_main() == 7


def test_orcho_run_dispatches_to_project_orchestrator(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(sys.modules, "pipeline", types.ModuleType("pipeline"))
    monkeypatch.setitem(
        sys.modules,
        "pipeline.project_orchestrator",
        _module_with_main(3),
    )

    assert _scripts.orcho_run_main() == 3


def test_orcho_cross_dispatches_to_cross_project_cli(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(sys.modules, "pipeline", types.ModuleType("pipeline"))
    monkeypatch.setitem(sys.modules, "pipeline.cross_project", types.ModuleType("cross_project"))
    monkeypatch.setitem(
        sys.modules,
        "pipeline.cross_project.cli",
        _module_with_main(5),
    )

    assert _scripts.orcho_cross_main() == 5


def test_orcho_mcp_missing_extra_prints_install_hint(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(_scripts.importlib.util, "find_spec", lambda name: None)

    with pytest.raises(SystemExit) as excinfo:
        _scripts.orcho_mcp_main()

    assert excinfo.value.code == 1
    error = capsys.readouterr().err
    assert "pipx install 'orcho[mcp]'" in error
    assert "pipx inject orcho orcho-mcp" in error
