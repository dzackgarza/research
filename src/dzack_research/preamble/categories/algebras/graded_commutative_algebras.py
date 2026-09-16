r"""Graded-commutative algebras: the ``Supercommutative`` axiom and its strict form.

``GradedCommutativeAlgebras(R, M, parity)`` is the axiom category
``GradedAlgebras(R, M, parity).Supercommutative()`` under its standard plural
name; the Koszul sign is read through the parity stated with the grading.

Strict graded commutativity additionally imposes ``x^2 = 0`` in odd degree,
which is essential over rings with 2-torsion.  Bourbaki, Algebra III §4.9,
calls such an algebra *alternating*; Sage's ``commutative_dga`` calls the
differential graded case *strictly commutative*.  With no single name in the
field, the strict form is a subcategory under its descriptive name rather
than an axiom.
"""

from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.refine import refine

GradedCommutativeAlgebras = GradedAlgebras.Supercommutative


class StrictlyGradedCommutativeAlgebras(OwnedCategoryOverBaseRing):
    r"""Supercommutative graded algebras whose odd homogeneous elements square to zero."""

    def an_object(self):
        r"""The identity-degree rank-one algebra, where odd-square conditions are vacuous."""
        algebra = self._graded_algebras.Supercommutative().an_object()
        refine(algebra, self)
        return algebra

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None, parity=None):
        graded_algebras = GradedAlgebras(base_ring, grading_monoid, parity)
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, graded_algebras.base_ring(), graded_algebras
        )

    def __init__(self, base_ring, graded_algebras) -> None:
        self._graded_algebras = graded_algebras
        super().__init__(base_ring)

    def grading_monoid(self):
        return self._graded_algebras.grading_monoid()

    def parity_homomorphism(self):
        r"""Return the ``M -> ZZ/2`` this category's Koszul sign is read through."""
        return self._graded_algebras.parity_homomorphism()

    @classmethod
    def _repr_object_names(cls):
        return "strictly graded-commutative algebras"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self._graded_algebras)

    def super_categories(self):
        return [self._graded_algebras.Supercommutative()]


__all__ = [
    "GradedCommutativeAlgebras",
    "StrictlyGradedCommutativeAlgebras",
]
