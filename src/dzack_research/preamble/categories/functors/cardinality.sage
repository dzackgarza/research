r"""The cardinality functor ``# : core(Sets) -> Cardinalities``."""

from typing import TYPE_CHECKING

from dzack_research.preamble.categories.abstract_categories.functors import Functor
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.sets.cardinals import (
    Cardinal,
    Cardinalities,
    CardinalityMorphism,
)
from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    from dzack_research.preamble import lexicon
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Core,
    )


class CardinalityFunctor(Functor):
    r"""Send a set to its cardinal and an isomorphism to its order arrow."""

    def __init__(self) -> None:
        Functor.__init__(self, Sets().core(), Cardinalities())

    if TYPE_CHECKING:
        def domain(self) -> Core: ...
        def codomain(self) -> Cardinalities: ...

    def _apply_functor(self, source: "lexicon.Set") -> Cardinal:
        cardinal_number = source.cardinality()
        assert cardinal_number in Cardinalities(), (
            "an object of the owned Sets category has an exact cardinal object"
        )
        return cardinal_number

    def _apply_functor_to_morphism(
        self,
        morphism: Morphism,
    ) -> CardinalityMorphism:
        isomorphism = self.domain().arrow(morphism)
        source = self._apply_functor(isomorphism.domain())
        target = self._apply_functor(isomorphism.codomain())
        assert source == target, "isomorphic sets have equal cardinality"
        return self.codomain().hom(source, target).unique_morphism()

    def _repr_(self) -> str:
        return "The cardinality functor # : core(Sets) -> Cardinalities"


@cached_function
def cardinality_functor() -> CardinalityFunctor:
    r"""Return the cardinality functor."""
    return CardinalityFunctor()
