"""Owned Lie-algebra categories."""

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
)
from dzack_research.preamble.categories.algebras.algebras import AssociativeAlgebras
from dzack_research.preamble.categories.modules.pure.modules import Modules


class LieAlgebras(OwnedCategoryOverBaseRing):
    r"""Lie algebras over a commutative owned base ring."""

    def an_object(self):
        r"""``End_R(Free_R([2]))`` with the commutator bracket."""
        from dzack_research.preamble.categories.algebras.algebras import MatrixAlgebras

        return MatrixAlgebras(self.base_ring()).an_object()

    @classmethod
    def _repr_object_names(cls):
        return "Lie algebras"

    def super_categories(self):
        if self.base_ring() not in OwnedRings().Commutative():
            raise TypeError("a Lie algebra here is over a commutative base ring")

        return [Modules(self.base_ring())]

    class ParentMethods:
        def bracket(self, left, right):
            return self(left).bracket(self(right))


class CommutatorLieAlgebras(LieAlgebras):
    r"""Associative algebras read as Lie algebras under \([x,y]=xy-yx\).

    The bracket is stated by
    :class:`~dzack_research.preamble.categories.algebras.algebras.AssociativeAlgebras`,
    which owns the product it is built from; this category adds the Lie
    structure that product determines.  The passage is named by
    ``AssociativeAlgebras(R).commutator_lie_algebra()``.

    Membership is a fact about every associative algebra over a commutative
    ring, but a category that knows its objects are associative must declare
    this one for itself.  Saying it once on ``AssociativeAlgebras`` would put
    that category both above and below this one; saying it through the
    restriction-of-scalars edge instead puts the shared
    ``LieAlgebras.ParentMethods`` at two incompatible depths, which Sage
    refuses when it linearizes the parent class.
    """

    @classmethod
    def _repr_object_names(cls):
        return "commutator Lie algebras"

    def super_categories(self):

        return [
            LieAlgebras(self.base_ring()),
            AssociativeAlgebras(self.base_ring()),
        ]


__all__ = ["CommutatorLieAlgebras", "LieAlgebras"]
