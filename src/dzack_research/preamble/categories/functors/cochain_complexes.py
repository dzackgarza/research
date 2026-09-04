r"""Forgetful functor from represented cochain complexes to graded modules."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


class CochainUnderlyingGradedModuleFunctor(Functor):
    r"""Forget the differential while retaining the same graded carrier."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(CochainComplexes(self._base_ring), GradedModules(self._base_ring))

    def _apply_object(self, complex_):
        return complex_

    def _apply_morphism(self, morphism):
        return morphism


@cached_function
def cochain_underlying_graded_module_functor(base_ring):
    return CochainUnderlyingGradedModuleFunctor(base_ring)


__all__ = [
    "CochainUnderlyingGradedModuleFunctor",
    "cochain_underlying_graded_module_functor",
]
