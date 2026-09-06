"""Owned Lie-algebra categories."""

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _proper_restriction_base_ring,
)
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
        ring = self.base_ring()
        if ring not in OwnedRings().Commutative():
            raise TypeError("a Lie algebra here is over a commutative base ring")

        # A Lie algebra over R is one over any ring R restricts to, exactly as
        # an associative algebra is, so the two towers have the same shape.
        base = _proper_restriction_base_ring(ring)
        if base is not None:
            return [Modules(ring), LieAlgebras(base)]
        return [Modules(ring)]

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
    ring, and ``AssociativeAlgebras`` states it once for all of them.  This
    category does not name the associative algebras in turn: knowing that a
    bracket is a commutator does not hand back the product it came from, since
    many associative products share one commutator.  The passage in that
    direction is the functor, not an edge.
    """

    @classmethod
    def _repr_object_names(cls):
        return "commutator Lie algebras"

    def super_categories(self):
        ring = self.base_ring()
        base = _proper_restriction_base_ring(ring)
        if base is not None:
            return [LieAlgebras(ring), CommutatorLieAlgebras(base)]
        return [LieAlgebras(ring)]


__all__ = ["CommutatorLieAlgebras", "LieAlgebras"]
