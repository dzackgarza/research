r"""Finite free lattices whose bilinear form takes values in ``Frac(R)``."""

from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FinitelyGeneratedFreeFormModules,
    SymmetricBilinearFormModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace


def _rational_lattice_determinant(lattice):
    r"""Return the Gram determinant in the selected fraction-field value module."""

    rank = int(lattice.module_generating_set().cardinality())
    gram = lattice.gram_tensor()
    return MatrixSpace(lattice.value_module(), rank).from_rows(
        (gram[row, column] for column in range(rank))
        for row in range(rank)
    ).determinant()


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

        def determinant(self):
            return _rational_lattice_determinant(self)

        def is_nondegenerate(self) -> bool:
            return True


def refine_rational_lattice(lattice):
    r"""Adopt a finite free ``Frac(R)``-valued nondegenerate form as a rational lattice."""
    base_ring = lattice.base_ring()
    fraction_field = base_ring.fraction_field()
    if _engine_ring(lattice.value_module()) is not _engine_ring(fraction_field):
        raise TypeError(
            f"a rational lattice over {base_ring} has values in {fraction_field}"
        )
    if _rational_lattice_determinant(lattice) == 0:
        raise ValueError("a rational lattice has a nondegenerate form")
    return refine(lattice, RationalLattices(base_ring))


__all__ = ["RationalLattices", "refine_rational_lattice"]
