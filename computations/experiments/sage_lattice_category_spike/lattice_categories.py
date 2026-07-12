r"""Public API for the owned synthetic lattice spike.

The implementation is organized by concept:

- ``categories``: Sage category declarations and axioms.
- ``parents`` and ``elements``: owned synthetic lattice parents/elements.
- ``homsets``: owned form-preserving homsets and morphisms.
- ``discriminant``: owned finite discriminant quotients.
- ``constructors``: thin public construction helpers.
"""

from . import lexicon
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
from .objects.functors import LatticeBaseChangeFunctor
from .objects.parents import SyntheticLattice


def Hom(
    domain: lexicon.Lattice,
    codomain: lexicon.Lattice,
    category: lexicon.SageCategory | None = None,
) -> lexicon.LatticeHomset:
    r"""Construct a lattice Hom through the source category root.

    This is the category-aware public spelling for lattice arguments. It
    performs canonical transport before asking Sage to construct the resolved
    homset.
    """
    return Lattices(domain.base_ring()).Hom(domain, codomain, category=category)


__all__ = [
    "DiscriminantForms",
    "Genera",
    "Hom",
    "IntegralLatticeGluing",
    "Lattice",
    "LatticeBaseChangeFunctor",
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
