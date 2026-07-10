r"""Public compatibility API for the owned synthetic lattice spike.

The implementation is organized by concept:

- ``categories``: Sage category declarations and axioms.
- ``parents`` and ``elements``: owned synthetic lattice parents/elements.
- ``homsets``: owned form-preserving homsets and morphisms.
- ``discriminant``: owned finite discriminant quotients.
- ``constructors``: thin public construction helpers.
"""

from .forms.discriminant import (
    SyntheticDiscriminantAction,
    SyntheticDiscriminantGroupElement,
    SyntheticDiscriminantSubgroup,
    SyntheticGenus,
    SyntheticOrthogonalGroup,
    TorsionQuadraticForm,
)
from .forms.discriminant_forms import (
    SyntheticBilinearDiscriminantForm,
    SyntheticQuadraticDiscriminantForm,
    SyntheticSourcedDiscriminantForm,
)
from .morphisms.homsets import LatticeHomset, LatticeMorphism, LatticeSimilarity
from .morphisms.isometry_groups import SyntheticIsometryGroup, SyntheticIsometrySubgroup
from .objects.categories import DiscriminantForms, Genera, Lattices
from .objects.constructors import IntegralLatticeGluing, Lattice, SyntheticLatticeFromGram
from .objects.elements import SyntheticLatticeElement
from .objects.parents import SyntheticLattice

__all__ = [
    "DiscriminantForms",
    "Genera",
    "IntegralLatticeGluing",
    "Lattice",
    "LatticeHomset",
    "LatticeMorphism",
    "LatticeSimilarity",
    "Lattices",
    "SyntheticDiscriminantAction",
    "SyntheticBilinearDiscriminantForm",
    "SyntheticQuadraticDiscriminantForm",
    "SyntheticSourcedDiscriminantForm",
    "SyntheticGenus",
    "SyntheticDiscriminantGroupElement",
    "SyntheticDiscriminantSubgroup",
    "SyntheticOrthogonalGroup",
    "SyntheticIsometryGroup",
    "SyntheticIsometrySubgroup",
    "SyntheticLattice",
    "SyntheticLatticeElement",
    "SyntheticLatticeFromGram",
    "TorsionQuadraticForm",
]
