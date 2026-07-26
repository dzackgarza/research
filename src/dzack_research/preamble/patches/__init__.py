r"""Install optional methods on Sage classes.

EXAMPLES::

    sage: from dzack_research.preamble import patches
    sage: patches.install("lattice_methods")
    sage: "lattice_methods" in patches.installed()
    True
    sage: patches.uninstall("lattice_methods")
"""

from __future__ import annotations

from types import ModuleType

from . import lattice_methods, vinberg

_REGISTRY: dict[str, ModuleType] = {
    "lattice_methods": lattice_methods,
    "vinberg": vinberg,
}

_installed: set[str] = set()

__all__ = ["available", "install", "installed", "uninstall"]


def available() -> tuple[str, ...]:
    """Return the available patch names."""
    return tuple(sorted(_REGISTRY))


def installed() -> tuple[str, ...]:
    """Return the installed patch names."""
    return tuple(sorted(_installed))


def install(name: str) -> None:
    """Install one patch."""
    assert name in _REGISTRY, f"unknown patch {name!r}; available: {available()}"
    if name in _installed:
        return
    _REGISTRY[name].install()
    _installed.add(name)


def uninstall(name: str) -> None:
    """Uninstall one patch."""
    assert name in _REGISTRY, f"unknown patch {name!r}; available: {available()}"
    if name not in _installed:
        return
    _REGISTRY[name].uninstall()
    _installed.discard(name)
