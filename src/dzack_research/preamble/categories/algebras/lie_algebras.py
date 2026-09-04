"""Owned Lie-algebra categories."""

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedCommutativeRings,
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
        if self.base_ring() not in OwnedCommutativeRings():
            raise TypeError("a Lie algebra here is over a commutative base ring")

        return [Modules(self.base_ring())]

    class ParentMethods:
        def bracket(self, left, right):
            return self(left).bracket(self(right))


class CommutatorLieAlgebras(LieAlgebras):
    r"""Associative algebras with bracket ``[x,y]=xy-yx``."""

    @classmethod
    def _repr_object_names(cls):
        return "commutator Lie algebras"

    def super_categories(self):

        return [
            LieAlgebras(self.base_ring()),
            AssociativeAlgebras(self.base_ring()),
        ]

    class ElementMethods:
        def bracket(self, other):
            other = self.parent()(other)
            return self * other - other * self


__all__ = ["CommutatorLieAlgebras", "LieAlgebras"]
