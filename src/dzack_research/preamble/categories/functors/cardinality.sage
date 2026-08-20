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
    from dzack_research.preamble.categories.abstract_categories.products import (
        CoproductOfSets,
    )
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Core,
    )
    from dzack_research.preamble.categories.sets.sets import PowerSetParent


class CardinalityFunctor(Functor):
    r"""Send a set to its cardinal and an isomorphism to its order arrow."""

    def __init__(self) -> None:
        Functor.__init__(self, Sets().core(), Cardinalities())

    if TYPE_CHECKING:
        def domain(self) -> Core: ...
        def codomain(self) -> Cardinalities: ...

    def _apply_functor(self, source: "lexicon.Set") -> Cardinal:
        cardinal_number = source.cardinality()
        assert isinstance(cardinal_number, Cardinal), (
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

    def cartesian_product_comparison(
        self,
        product: "Sets.CartesianProducts.ParentMethods",
    ) -> CardinalityMorphism:
        r"""Return the equality arrow ``#(prod X_i) -> prod #X_i``."""
        source = self._apply_functor(product)
        target = self.codomain().product(
            *(self._apply_functor(factor) for factor in product.factors())
        )
        assert source == target, "#(prod X_i) equals prod #X_i"
        return self.codomain().hom(source, target).identity()

    def coproduct_comparison(
        self,
        coproduct: "CoproductOfSets",
    ) -> CardinalityMorphism:
        r"""Return the equality arrow ``#(coprod X_i) -> sum #X_i``."""
        source = self._apply_functor(coproduct)
        target = self.codomain().sum(
            *(self._apply_functor(cofactor) for cofactor in coproduct.cofactors())
        )
        assert source == target, "#(coprod X_i) equals sum #X_i"
        return self.codomain().hom(source, target).identity()

    def power_set_comparison(
        self,
        power_set: "PowerSetParent",
    ) -> CardinalityMorphism:
        r"""Return the equality arrow ``#P(X) -> 2 ^ #X``."""
        source = self._apply_functor(power_set)
        target = self.codomain().power(
            2,
            self._apply_functor(power_set.base_set()),
        )
        assert source == target, "#P(X) equals 2 ^ #X"
        return self.codomain().hom(source, target).identity()

    def _repr_(self) -> str:
        return "The cardinality functor # : core(Sets) -> Cardinalities"


@cached_function
def cardinality_functor() -> CardinalityFunctor:
    r"""Return the cardinality functor."""
    return CardinalityFunctor()
