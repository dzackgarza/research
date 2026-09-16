r"""Graded-commutative algebras: the ``Supercommutative`` axiom and its strict form.

``GradedCommutativeAlgebras(R, M)`` is the axiom category
``GradedAlgebras(R, M).Supercommutative()`` under its standard plural name.
The Koszul sign is read through the parity of the grading monoid, as
:func:`~dzack_research.preamble.categories.algebras.graded_algebras._koszul_parity`
states it.

Strict graded commutativity additionally imposes ``x^2 = 0`` in odd degree.
Bourbaki, Algebra III §4.9, calls such an algebra *alternating*; Sage's
``commutative_dga`` calls the differential graded case *strictly
commutative*.  The field has no single name, so the strict form stays a
subcategory under its descriptive name rather than an axiom.
"""

from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.modules.graded_modules import (
    _require_grading_monoid,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.refine import refine

GradedCommutativeAlgebras = GradedAlgebras.Supercommutative


class StrictlyGradedCommutativeAlgebras(OwnedCategoryOverBaseRing):
    r"""Supercommutative graded algebras whose odd homogeneous elements square to zero."""

    def an_object(self):
        r"""The identity-degree rank-one algebra, where odd-square conditions are vacuous."""
        algebra = GradedAlgebras(
            self.base_ring(),
            self.grading_monoid(),
        ).Supercommutative().an_object()
        refine(algebra, self)
        return algebra

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None):
        monoid = _require_grading_monoid(grading_monoid)
        return OwnedCategoryOverBaseRing.__classcall__(cls, base_ring, monoid)

    def __init__(self, base_ring, grading_monoid) -> None:
        self._grading_monoid = grading_monoid
        super().__init__(base_ring)

    def grading_monoid(self):
        return self._grading_monoid

    def parity_homomorphism(self):
        r"""Return the ``M -> ZZ/2`` this category's Koszul sign is read through."""
        return GradedAlgebras(self.base_ring(), self.grading_monoid()).Supercommutative().parity_homomorphism()

    @classmethod
    def _repr_object_names(cls):
        return "strictly graded-commutative algebras"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_monoid())

    def super_categories(self):
        return [GradedAlgebras(self.base_ring(), self.grading_monoid()).Supercommutative()]


__all__ = [
    "GradedCommutativeAlgebras",
    "StrictlyGradedCommutativeAlgebras",
]
