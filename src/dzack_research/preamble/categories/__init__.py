r"""Categories for the preamble method surface.

Objects are routed by :func:`dzack_research.preamble.refine.refine` (category
methods before concrete class methods) via post-init hooks on Sage classes.
Categories do not ``setattr`` API methods and do not replace constructors.

EXAMPLES::

    sage: from dzack_research.preamble.categories import IntegralLattices
    sage: IntegralLattices()._repr_object_names()
    'integral lattices'
"""

from __future__ import annotations

from dzack_research.preamble.refine import refine

from .discriminant_groups import (
    DiscriminantQuadraticModules,
    FinitelyPresentedGroups,
    install as _install_discriminant,
)
from .hyperbolic_lattices import HyperbolicLattices
from .integral_lattices import IntegralLattices, install as _install_integral
from .lattice_homomorphisms import LatticeHomomorphisms
from .lattice_isometries import LatticeIsometries

__all__ = [
    "DiscriminantQuadraticModules",
    "FinitelyPresentedGroups",
    "HyperbolicLattices",
    "IntegralLattices",
    "LatticeHomomorphisms",
    "LatticeIsometries",
    "install",
    "refine",
]


def install() -> None:
    """Register post-init hooks for all preamble categories."""
    _install_integral()
    _install_discriminant()


# Hooks are registered by ``preamble.install()`` or an explicit ``categories.install()``.
# Do not auto-hook on import: building the catalogue under live hooks must be deliberate.
