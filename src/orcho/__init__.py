"""Convenience installer package for the public Orcho command set."""
from importlib.metadata import PackageNotFoundError, version

__all__ = ["__version__"]

try:
    __version__ = version("orcho")
except PackageNotFoundError:
    __version__ = "0+unknown"
