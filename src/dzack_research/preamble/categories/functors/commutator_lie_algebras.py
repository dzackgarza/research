r"""The commutator functor \((-)^-\colon\mathbf{AssAlg}_R\to\mathbf{Lie}_R\).

An associative \(R\)-algebra over commutative \(R\) is a Lie algebra under
\([x,y]=xy-yx\).  The bracket is determined by the product -- nothing is
chosen -- so \(A^-\) is \(A\), one object placed in more categories, and this
functor names the passage rather than building a second model.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import AssociativeAlgebras
from dzack_research.preamble.categories.algebras.lie_algebras import (
    CommutatorLieAlgebras,
)
from dzack_research.preamble.categories.functors.algebra_modules import (
    algebra_underlying_module_functor,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


class CommutatorLieAlgebraFunctor(Functor):
    r"""\((-)^-\colon\mathbf{AssAlg}_R\to\mathbf{CommLie}_R\)."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            AssociativeAlgebras(self._base_ring),
            CommutatorLieAlgebras(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, algebra):
        r"""Return the algebra, which already is its own commutator Lie algebra.

        The commutator is determined by the product, so the passage adds no
        structure and takes none away: an associative algebra over a
        commutative ring is placed in
        :class:`~dzack_research.preamble.categories.algebras.lie_algebras.CommutatorLieAlgebras`
        by its own category, and this functor is the identity on objects.
        It is therefore not what makes an algebra a Lie algebra -- the
        category graph says that -- and asking it is how a caller says which
        of the two structures it means to use next.
        """
        return algebra

    def _apply_morphism(self, morphism):
        r"""Return the underlying linear map of an algebra morphism.

        A morphism of associative algebras preserves the commutator, since
        \(f(xy-yx)=f(x)f(y)-f(y)f(x)\) follows from multiplicativity; that is
        a theorem, so the map is not tested here.  What the Lie level wants of
        it is the \(R\)-linear map, which is
        :func:`~dzack_research.preamble.categories.functors.algebra_modules.algebra_underlying_module_functor`
        applied to the same morphism.

        A Lie Hom is presently the module Hom of the two algebras:
        :class:`~dzack_research.preamble.categories.algebras.lie_algebras.LieAlgebras`
        declares no Hom of its own, so nothing yet cuts the bracket-preserving
        maps out of the linear ones.  Until it does, this is the parent the
        image arrives in.
        """
        return algebra_underlying_module_functor(self.base_ring())(morphism)

    def _repr_(self):
        return f"Commutator Lie-algebra functor on associative {self.base_ring()}-algebras"


@cached_function
def commutator_lie_algebra_functor(base_ring) -> CommutatorLieAlgebraFunctor:
    return CommutatorLieAlgebraFunctor(base_ring)


__all__ = [
    "CommutatorLieAlgebraFunctor",
    "commutator_lie_algebra_functor",
]
