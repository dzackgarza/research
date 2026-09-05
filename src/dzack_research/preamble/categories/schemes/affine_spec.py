"""The contravariant affine spectrum functor on commutative algebras."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras
from dzack_research.preamble.categories.abstract_categories.functors import ContravariantFunctor
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSchemes,
    Spec,
    affine_spec_morphism,
)


class AffineSpecFunctor(ContravariantFunctor):
    r"""The contravariant functor ``Spec_R: CAlg_R -> AffSch_R``."""

    def __init__(self, base_ring) -> None:
        base = _owned_ring(base_ring)
        self._base_ring = base
        ContravariantFunctor.__init__(
            self,
            CommutativeAlgebras(base),
            AffineSchemes(base),
        )

    def base_ring(self):
        return self._base_ring

    def _apply_contravariant_object(self, algebra):
        return Spec(algebra, base_ring=self.base_ring())

    def _apply_contravariant_morphism(self, morphism):
        return affine_spec_morphism(morphism)

    def _repr_(self) -> str:
        return f"Affine spectrum functor over {self.base_ring()}"


@cached_function
def affine_spec_functor(base_ring):
    return AffineSpecFunctor(base_ring)


SpecFunctor = affine_spec_functor

__all__ = ["AffineSpecFunctor", "SpecFunctor", "affine_spec_functor"]
