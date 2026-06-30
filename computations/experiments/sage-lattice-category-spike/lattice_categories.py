r"""Public compatibility surface for the owned synthetic lattice spike.

The implementation is organized by concept:

- ``categories``: Sage category declarations and axioms.
- ``parents`` and ``elements``: owned synthetic lattice parents/elements.
- ``homsets``: owned form-preserving homsets and morphisms.
- ``discriminant``: owned finite discriminant quotients.
- ``constructors``: thin public construction helpers.
"""

from categories import DiscriminantGroups, Lattices, QuadraticModules, RationalLattices
from constructors import IntegralLatticeGluing, Lattice, SyntheticLatticeFromGram
from discriminant import (
    SyntheticDiscriminantAction,
    SyntheticFiniteQuadraticForm,
    SyntheticGenus,
    SyntheticDiscriminantGroup,
    SyntheticDiscriminantGroupElement,
    SyntheticDiscriminantSubgroup,
    SyntheticOrthogonalGroup,
    TorsionQuadraticForm,
)
from elements import SyntheticLatticeElement
from homsets import LatticeHomset, LatticeMorphism, LatticeSimilarity
from parents import SyntheticLattice

__all__ = [
    "DiscriminantGroups",
    "IntegralLatticeGluing",
    "Lattice",
    "LatticeHomset",
    "LatticeMorphism",
    "LatticeSimilarity",
    "Lattices",
    "QuadraticModules",
    "RationalLattices",
    "SyntheticDiscriminantAction",
    "SyntheticFiniteQuadraticForm",
    "SyntheticGenus",
    "SyntheticDiscriminantGroup",
    "SyntheticDiscriminantGroupElement",
    "SyntheticDiscriminantSubgroup",
    "SyntheticOrthogonalGroup",
    "SyntheticLattice",
    "SyntheticLatticeElement",
    "SyntheticLatticeFromGram",
    "TorsionQuadraticForm",
]
