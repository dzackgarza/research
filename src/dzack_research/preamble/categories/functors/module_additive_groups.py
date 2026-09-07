r"""The forgetful functor from left modules to abelian groups."""

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.magmas import AdditiveGroups


class UnderlyingAdditiveGroupFunctor(Functor):
    r"""Forget the scalar action and retain the chosen underlying additive group."""

    _faithful = True

    def __init__(self, modules) -> None:
        super().__init__(modules, AdditiveGroups().AdditiveCommutative())

    def _apply_object(self, module):
        return module.underlying_additive_group()

    def _apply_morphism(self, morphism):
        source = morphism.domain()
        target = morphism.codomain()
        hom = self.codomain().Mor(self(source), self(target))
        return hom.elementwise(
            lambda element: target._underlying_additive_element(morphism(source(element)))
        )
