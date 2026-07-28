r"""Thin wrappers around lattice predicate methods.

Prefer calling the methods on a lattice refined into
:class:`~dzack_research.preamble.categories.IntegralLattices`::

    lattice.is_elliptic(), lattice.delta(), ...

These free functions remain for call sites that still pass the lattice as an
argument; they require the lattice to already carry the category methods
(via ``preamble.install()`` or ``refine``).

EXAMPLES::

    sage: from dzack_research.preamble import catalogue, install, predicates
    sage: install(vendor_paths=False)
    {...}
    sage: predicates.is_elliptic(catalogue.Lattices.E8)
    True
    sage: catalogue.Lattices.E8.delta()
    0
"""

from __future__ import annotations

from typing import Any

__all__ = [
    "delta",
    "is_coeven",
    "is_coodd",
    "is_elliptic",
    "is_parabolic",
]


def is_coeven(lattice: Any) -> bool:
    """Delegate to ``lattice.is_coeven()``."""
    return lattice.is_coeven()


def is_coodd(lattice: Any) -> bool:
    """Delegate to ``lattice.is_coodd()``."""
    return lattice.is_coodd()


def delta(lattice: Any) -> Any:
    """Delegate to ``lattice.delta()``."""
    return lattice.delta()


def is_elliptic(lattice: Any) -> bool:
    """Delegate to ``lattice.is_elliptic()``."""
    return lattice.is_elliptic()


def is_parabolic(lattice: Any) -> bool:
    """Delegate to ``lattice.is_parabolic()``."""
    return lattice.is_parabolic()
