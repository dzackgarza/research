r"""Graded-commutative algebra categories.

For the standard additive integer grading, graded commutativity is the Koszul
rule ``xy = (-1)^(pq) yx`` on homogeneous elements of degrees ``p`` and ``q``.
Strict graded commutativity additionally imposes ``x^2 = 0`` in odd degree;
this distinction is essential over rings with 2-torsion.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.graded_modules import (
    require_grading_monoid,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras


class GradedCommutativeAlgebras(OwnedCategoryOverBaseRing):
    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None):
        monoid = require_grading_monoid(grading_monoid)
        if monoid is not _own_ring(SageZZ):
            raise NotImplementedError(
                "Koszul graded commutativity is currently represented for the integer grading"
            )
        return OwnedCategoryOverBaseRing.__classcall__(cls, base_ring, monoid)

    def __init__(self, base_ring, grading_monoid) -> None:
        self._grading_monoid = grading_monoid
        super().__init__(base_ring)

    def grading_monoid(self):
        return self._grading_monoid

    @classmethod
    def _repr_object_names(cls):
        return "graded-commutative algebras"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_monoid())

    def super_categories(self):

        return [GradedAlgebras(self.base_ring(), self.grading_monoid())]


class StrictlyGradedCommutativeAlgebras(OwnedCategoryOverBaseRing):
    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None):
        monoid = require_grading_monoid(grading_monoid)
        if monoid is not _own_ring(SageZZ):
            raise NotImplementedError(
                "strict graded commutativity is currently represented for the integer grading"
            )
        return OwnedCategoryOverBaseRing.__classcall__(cls, base_ring, monoid)

    def __init__(self, base_ring, grading_monoid) -> None:
        self._grading_monoid = grading_monoid
        super().__init__(base_ring)

    def grading_monoid(self):
        return self._grading_monoid

    @classmethod
    def _repr_object_names(cls):
        return "strictly graded-commutative algebras"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_monoid())

    def super_categories(self):
        return [
            GradedCommutativeAlgebras(
                self.base_ring(),
                self.grading_monoid(),
            )
        ]


__all__ = [
    "GradedCommutativeAlgebras",
    "StrictlyGradedCommutativeAlgebras",
]
