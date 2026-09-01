r"""Finite free lattices whose bilinear form takes values in ``Frac(R)``."""

from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FinitelyGeneratedFreeFormModules,
    SymmetricBilinearFormModules,
)
from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
)
from dzack_research.preamble.refine import refine


class RationalLattices(OwnedCategoryOverBaseRing):
    r"""Nondegenerate finite free ``R``-modules with ``Frac(R)``-valued form."""

    @classmethod
    def _repr_object_names(cls):
        return "rational lattices"

    def super_categories(self):
        return [
            FinitelyGeneratedFreeFormModules(self.base_ring()),
            SymmetricBilinearFormModules(self.base_ring()),
        ]

    class ParentMethods:
        def fraction_field(self):
            return self.base_ring().fraction_field()

        def is_nondegenerate(self) -> bool:
            return True


def refine_rational_lattice(lattice):
    r"""Adopt a finite free ``Frac(R)``-valued nondegenerate form as a rational lattice."""
    base_ring = lattice.base_ring()
    fraction_field = base_ring.fraction_field()
    if engine_ring(lattice.value_module()) is not engine_ring(fraction_field):
        raise TypeError(
            f"a rational lattice over {base_ring} has values in {fraction_field}"
        )
    if lattice.gram_tensor().det() == 0:
        raise ValueError("a rational lattice has a nondegenerate form")
    return refine(lattice, RationalLattices(base_ring))


__all__ = ["RationalLattices", "refine_rational_lattice"]
