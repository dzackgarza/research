r"""Public compatibility surface for the owned synthetic lattice spike.

The implementation is organized by concept:

- ``categories``: Sage category declarations and axioms.
- ``parents`` and ``elements``: owned synthetic lattice parents/elements.
- ``homsets``: owned form-preserving homsets and morphisms.
- ``discriminant``: owned finite discriminant quotients.
- ``constructors``: thin public construction helpers.
"""

from .categories import DiscriminantForms, Lattices
from .constructors import IntegralLatticeGluing, Lattice, RootLattice, SyntheticLatticeFromGram, U
from .discriminant import (
    SyntheticDiscriminantAction,
    SyntheticFiniteQuadraticForm,
    SyntheticGenus,
    SyntheticDiscriminantGroup,
    SyntheticDiscriminantGroupElement,
    SyntheticDiscriminantSubgroup,
    SyntheticOrthogonalGroup,
    TorsionQuadraticForm,
)
from .elements import SyntheticLatticeElement
from .homsets import LatticeHomset, LatticeMorphism, LatticeSimilarity
from .endomorphism_rings import ModuleEndomorphism, SyntheticEndomorphismRing
from .isometry_groups import SyntheticIsometryGroup, SyntheticIsometrySubgroup
from .parents import SyntheticLattice

__all__ = [
    "DiscriminantForms",
    "IntegralLatticeGluing",
    "Lattice",
    "LatticeHomset",
    "LatticeMorphism",
    "LatticeSimilarity",
    "Lattices",
    "SyntheticDiscriminantAction",
    "SyntheticFiniteQuadraticForm",
    "SyntheticGenus",
    "SyntheticDiscriminantGroup",
    "SyntheticDiscriminantGroupElement",
    "SyntheticDiscriminantSubgroup",
    "SyntheticOrthogonalGroup",
    "ModuleEndomorphism",
    "SyntheticEndomorphismRing",
    "SyntheticIsometryGroup",
    "SyntheticIsometrySubgroup",
    "SyntheticLattice",
    "SyntheticLatticeElement",
    "RootLattice",
    "SyntheticLatticeFromGram",
    "U",
    "TorsionQuadraticForm",
]
