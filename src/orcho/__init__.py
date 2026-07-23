"""Convenience installer package for the public Orcho command set."""
from importlib.metadata import version

__all__ = ["__version__"]

__version__ = version("orcho")
