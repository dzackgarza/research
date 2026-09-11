r"""The cardinality functor ``# : core(Set) -> Card``."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.abstract_categories.arrow_categories import Core
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
    cardinal,
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

    def cartesian_product_comparison(self, product):
        r"""Return ``prod_i #X_i -> #(prod_i X_i)`` for a represented set product."""
        try:
            index_set = product.index_set()
            expected = self.codomain().indexed_product(
                index_set, lambda index: self(product.factor(index))
            )
        except AttributeError as error:
            raise TypeError("the comparison requires a represented Cartesian product of sets") from error
        actual = self(product)
        if expected != actual:
            raise ArithmeticError(
                "the represented Cartesian product cardinality disagrees with the product of factor cardinals"
            )
        return self.codomain().Mor(expected, actual).unique_morphism()

    def coproduct_comparison(self, coproduct):
        r"""Return ``sum_i #X_i -> #(coprod_i X_i)`` for a represented set coproduct."""
        try:
            index_set = coproduct.index_set()
            expected = self.codomain().indexed_sum(
                index_set, lambda index: self(coproduct.cofactor(index))
            )
        except AttributeError as error:
            raise TypeError("the comparison requires a represented coproduct of sets") from error
        actual = self(coproduct)
        if expected != actual:
            raise ArithmeticError(
                "the represented coproduct cardinality disagrees with the sum of cofactor cardinals"
            )
        return self.codomain().Mor(expected, actual).unique_morphism()

    def power_set_comparison(self, power_set):
        r"""Return ``2^(#X) -> #P(X)`` for a represented power set."""
        try:
            base_set = power_set.base_set()
        except AttributeError as error:
            raise TypeError("the comparison requires a represented power set") from error
        expected = self.codomain().power(cardinal(2), self(base_set))
        actual = self(power_set)
        if expected != actual:
            raise ArithmeticError(
                "the represented power-set cardinality disagrees with two to the base-set cardinal"
            )
        return self.codomain().Mor(expected, actual).unique_morphism()

    def _repr_(self):
        return "Cardinality functor # : core(Set) -> Card"


@cached_function
def cardinality_functor() -> CardinalityFunctor:
    return CardinalityFunctor()


__all__ = ["CardinalityFunctor", "cardinality_functor"]
