r"""The commutator functor \((-)^-\colon\mathbf{AssAlg}_R\to\mathbf{Lie}_R\).

An associative \(R\)-algebra over commutative \(R\) is a Lie algebra under
\([x,y]=xy-yx\).  The bracket is determined by the product -- nothing is
chosen -- so \(A^-\) is \(A\), one object placed in more categories, and this
functor names the passage rather than building a second model.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.lie_algebras import (
    CommutatorLieAlgebras,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.refine import refine


class CommutatorLieAlgebraFunctor(Functor):
    r"""\((-)^-\colon\mathbf{AssAlg}_R\to\mathbf{CommLie}_R\)."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            Algebras(self._base_ring).Associative(),
            CommutatorLieAlgebras(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, algebra):
        r"""Equip the same underlying module with the changed product ``xy-yx``."""
        multiplication = algebra.multiplication_morphism()
        tensor = multiplication.domain()
        commutator = tensor.from_bilinear(
            BilinearMap(
                algebra,
                algebra,
                algebra,
                lambda left, right: multiplication(
                    tensor.pure_tensor(
                        algebra.module_generator(left),
                        algebra.module_generator(right),
                    )
                )
                - multiplication(
                    tensor.pure_tensor(
                        algebra.module_generator(right),
                        algebra.module_generator(left),
                    )
                ),
            )
        )
        result = Algebras(self.base_ring()).Lie()(algebra, commutator)
        refine(result, CommutatorLieAlgebras(self.base_ring()))
        return result

    def _apply_morphism(self, morphism):
        r"""Return the underlying linear map between the changed multiplications.

        A morphism of associative algebras preserves the commutator, since
        \(f(xy-yx)=f(x)f(y)-f(y)f(x)\) follows from multiplicativity, and it
        is \(R\)-linear by the structure map.  Both are theorems, so the Lie
        level is told them rather than asked to decide them -- which is also
        what lets this answer for an algebra whose module framing is infinite,
        where the bracket condition has no decision procedure of its own.

        The image is the map itself; \(A^-\) is \(A\), so nothing is
        transported.  Every linear-map question about it -- matrix, kernel,
        cokernel -- is the module level's, and
        the algebra category's ``underlying_module()`` functor is where that map is asked for.
        """
        underlying = Algebras(self.base_ring()).underlying_module()(morphism)
        return Algebras(self.base_ring()).Lie().Mor(
            self(morphism.domain()),
            self(morphism.codomain()),
        )(underlying)

    def _repr_(self):
        return f"Commutator Lie-algebra functor on associative {self.base_ring()}-algebras"


@cached_function
def _commutator_lie_algebra_functor(base_ring) -> CommutatorLieAlgebraFunctor:
    return CommutatorLieAlgebraFunctor(base_ring)


__all__ = [
    "CommutatorLieAlgebraFunctor",
]
