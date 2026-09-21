"""Owned Lie-algebra categories."""

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing


def LieAlgebraMorphism(parent, linear):
    r"""Read the bracket-preserving linear map through the root algebra equation."""
    category = Algebras(parent.domain().base_ring()).Lie()
    assert parent.mor_category().is_subcategory(category), "the supplied arrow parent is a Lie-algebra Mor"
    return parent(linear)


def LieAlgebraMor(domain, codomain):
    r"""The ordinary algebra Mor between the specified Lie algebras."""
    return Algebras(domain.base_ring()).Lie().Mor(domain, codomain)


LieAlgebras = Algebras.Lie


class CommutatorLieAlgebras(OwnedCategoryOverBaseRing):
    r"""Associative algebras read as Lie algebras under \([x,y]=xy-yx\).

    The bracket is stated by
    associative refinement ``Algebras(R).Associative()``,
    which owns the product it is built from; this category adds the Lie
    structure that product determines.  The passage is named by
    ``Algebras(R).Associative().commutator_lie_algebra()``.

    Membership is a fact about every associative algebra over a commutative
    ring, and the associative refinement states it once for all of them.  This
    category does not name the associative algebras in turn: knowing that a
    bracket is a commutator does not hand back the product it came from, since
    many associative products share one commutator.  The passage in that
    direction is the functor, not an edge.
    """

    def an_object(self):
        r"""``gl_2(R)``, the commutator Lie algebra of the two-by-two matrices."""
        return Algebras(self.base_ring()).Lie().an_object()

    @classmethod
    def _repr_object_names(cls):
        return "commutator Lie algebras"

    def super_categories(self):
        return [Algebras(self.base_ring()).Lie()]


__all__ = [
    "CommutatorLieAlgebras",
    "LieAlgebraMor",
    "LieAlgebraMorphism",
    "LieAlgebras",
]
