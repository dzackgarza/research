r"""The cardinality functor ``# : core(Set) -> Card``."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.abstract_categories.arrow_categories import Core
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


class CardinalityFunctor(Functor):
    r"""Send a set to its cardinal and a set isomorphism to the unique order arrow."""

    def __init__(self) -> None:
        super().__init__(Core(Sets()), Cardinalities())

    def _apply_object(self, set_object):
        return set_object.cardinality()

    def _apply_morphism(self, isomorphism):
        source = self(isomorphism.domain())
        target = self(isomorphism.codomain())
        if source != target:
            raise ValueError("isomorphic sets must have equal cardinality")
        return self.codomain().Mor(source, target).unique_morphism()

    def _repr_(self):
        return "Cardinality functor # : core(Set) -> Card"


@cached_function
def cardinality_functor() -> CardinalityFunctor:
    return CardinalityFunctor()


__all__ = ["CardinalityFunctor", "cardinality_functor"]
