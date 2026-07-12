r"""First-class canonical functors between synthetic lattice categories."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from .. import lexicon

if TYPE_CHECKING:
    from .categories import Lattices


class LatticeBaseChangeFunctor(lexicon.LatticeBaseChangeFunctor, lexicon.SageFunctor):
    r"""Scalar extension along a canonical map of supported base rings.

    The source category owns the functor. Its object action enters the target
    category through ``from_base_change`` so the target classifies the result
    from its own data; its morphism action constructs through the target's
    homset root.
    """

    def __init__(self, domain: Lattices, codomain: Lattices) -> None:
        assert codomain.base_ring().coerce_map_from(domain.base_ring()) is not None, f"base change requires a canonical map {domain.base_ring()} -> {codomain.base_ring()}"
        lexicon.SageFunctor.__init__(self, domain, codomain)

    if TYPE_CHECKING:
        # The generic Sage functor surface returns Category.  This functor's
        # source and target are specifically lattice-category roots.
        def domain(self) -> Lattices: ...

        def codomain(self) -> Lattices: ...

    def source_base_ring(self) -> lexicon.BaseRing:
        return cast(lexicon.BaseRing, self.domain().base_ring())

    def target_base_ring(self) -> lexicon.BaseRing:
        return cast(lexicon.BaseRing, self.codomain().base_ring())

    def _coerce_into_domain(self, lattice: lexicon.Lattice) -> lexicon.Lattice:
        assert lattice in self.domain(), f"base-change source must belong to {self.domain()}; found={lattice.category()}"
        return lattice

    def _apply_functor(self, lattice: lexicon.Lattice) -> lexicon.Lattice:
        target = self.codomain()
        return target.from_base_change(lattice)

    def _apply_functor_to_morphism(self, morphism: lexicon.SageMorphism) -> lexicon.LatticeMorphism:
        assert isinstance(morphism, lexicon.LatticeMorphism), f"base change acts on lattice morphisms; found={type(morphism)}"
        target = self.codomain()
        domain = self._apply_functor(morphism.domain())
        codomain = self._apply_functor(morphism.codomain())
        return target.morphism(domain, morphism.matrix(), codomain=codomain)
