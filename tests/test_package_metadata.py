from __future__ import annotations

import tomllib
from importlib.metadata import version
from pathlib import Path

import orcho


def test_package_version_matches_installed_distribution() -> None:
    assert orcho.__version__ == version("orcho")


def test_distribution_does_not_publish_unresolved_tui_extra() -> None:
    pyproject = tomllib.loads(
        (Path(__file__).parents[1] / "pyproject.toml").read_text(encoding="utf-8")
    )

    assert "tui" not in pyproject["project"]["optional-dependencies"]
