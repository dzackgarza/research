r"""Opt-in monkeypatches, each individually toggleable.

Kept deliberately apart from the lattice spike's ``sage_patches/`` subtree, which
is a different kind of thing: those are *corrections to Sage upstream defects*
and are applied at package import on purpose, because making a bugfix optional
means shipping known-broken behaviour. Everything here is *capability injection*
-- attaching new methods to Sage classes -- which must never happen as an import
side effect, because it changes the meaning of objects the caller did not ask
about.

Nothing in this package is installed by importing it. Ask explicitly::

    from dzack_research.preamble import patches
    patches.install("vinberg")
    patches.installed()          # ('vinberg',)
    patches.uninstall("vinberg")

Every patch module supplies ``install()`` and ``uninstall()``, so a patch that
cannot be removed cannot be registered.
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
    """Names that :func:`install` accepts."""
    return tuple(sorted(_REGISTRY))


def installed() -> tuple[str, ...]:
    """Names currently applied to the Sage surface."""
    return tuple(sorted(_installed))


def install(name: str) -> None:
    """Apply one patch. Idempotent; unknown names fail loudly."""
    assert name in _REGISTRY, f"unknown patch {name!r}; available: {available()}"
    if name in _installed:
        return
    _REGISTRY[name].install()
    _installed.add(name)


def uninstall(name: str) -> None:
    """Remove one patch, restoring the unpatched Sage surface."""
    assert name in _REGISTRY, f"unknown patch {name!r}; available: {available()}"
    if name not in _installed:
        return
    _REGISTRY[name].uninstall()
    _installed.discard(name)
