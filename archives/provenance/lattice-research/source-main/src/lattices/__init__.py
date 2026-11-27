"""Lattice implementation — ModulesWithForms concrete carriers.

Phase 2: Core category objects and thin element wrappers.
Phase 3: Morphisms, homsets, kernels, images, cokernels.
Phase 4: Duals, meets, discriminant descent.
Phase 5: Orthogonal groups, roots, Weyl, Eichler, Coxeter.
"""

from __future__ import annotations

from .category import (
    ConsolidatedLattice,
    DiscriminantGroupAdapter,
    DiscriminantGroups,
    DiscriminantGroupsCategory,
    Lattice,
    LatticeHomset,
    LatticeMorphismAdapter,
    LatticeQuotientAdapter,
    RationalLattices,
    RationalLatticesCategory,
    from_sage,
)

__all__ = [
    "ConsolidatedLattice",
    "DiscriminantGroupAdapter",
    "DiscriminantGroups",
    "DiscriminantGroupsCategory",
    "Lattice",
    "LatticeHomset",
    "LatticeMorphismAdapter",
    "LatticeQuotientAdapter",
    "RationalLattices",
    "RationalLatticesCategory",
    "from_sage",
]
