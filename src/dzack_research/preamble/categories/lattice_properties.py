r"""Mathematical property subcategories of the active lattice category."""

from sage.rings.infinity import Infinity

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.refine import refine


class FiniteRankLattices(OwnedCategoryOverBaseRing):
    r"""Lattices whose underlying free module has finite rank."""

    @classmethod
    def _repr_object_names(cls):
        return "finite-rank lattices"

    def super_categories(self):
        from dzack_research.preamble.categories.lattices import Lattices
        from dzack_research.preamble.categories.modules import FinitelyGeneratedFreeModules

        return [
            Lattices(self.base_ring()),
            FinitelyGeneratedFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        def is_finite_rank(self) -> bool:
            return True


class NondegenerateLattices(OwnedCategoryOverBaseRing):
    r"""Lattices whose correlation map has zero kernel."""

    @classmethod
    def _repr_object_names(cls):
        return "nondegenerate lattices"

    def super_categories(self):
        from dzack_research.preamble.categories.lattices import Lattices

        return [Lattices(self.base_ring())]


class EvenLattices(OwnedCategoryOverBaseRing):
    r"""Lattices satisfying ``b(x,x) in 2R`` for every lattice vector ``x``."""

    @classmethod
    def _repr_object_names(cls):
        return "even lattices"

    def super_categories(self):
        from dzack_research.preamble.categories.lattices import Lattices

        return [Lattices(self.base_ring())]


def refine_lattice_properties(lattice):
    r"""Attach the finite properties directly decidable from the form."""
    categories = []
    if lattice.rank() != Infinity:
        categories.append(FiniteRankLattices(lattice.base_ring()))
    if lattice.is_nondegenerate():
        categories.append(NondegenerateLattices(lattice.base_ring()))
    try:
        is_even = lattice.is_even()
    except NotImplementedError:
        is_even = False
    if is_even:
        categories.append(EvenLattices(lattice.base_ring()))
    if not categories:
        return lattice
    return refine(lattice, categories)


__all__ = [
    "EvenLattices",
    "FiniteRankLattices",
    "NondegenerateLattices",
    "refine_lattice_properties",
]
