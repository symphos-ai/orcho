from __future__ import annotations

from importlib.metadata import version

import orcho


def test_package_version_matches_installed_distribution() -> None:
    assert orcho.__version__ == version("orcho")
