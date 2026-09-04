r"""Functorial Set constructions: exponentials and finite/power subsets."""

from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from dzack_research.preamble.categories.sets.set_categories import Sets as _OwnedSets
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    MonomorphismArrowCategory,
    WideSubcategory,
)
from dzack_research.preamble.categories.abstract_categories.category_constructions import (
    OppositeCategory,
    ProductCategory,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.sets.set_categories import (
    ExponentialOfSets,
    FiniteSubsets,
    PowerSet,
    SubsetsOfSize,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


class ExponentialFunctor(Functor):
    r"""The internal-Hom functor ``Set^op x Set -> Set``."""

    def __init__(self) -> None:
        self._opposite_sets = OppositeCategory(Sets())
        self._product_category = ProductCategory(self._opposite_sets, Sets())
        super().__init__(self._product_category, Sets())

    def opposite_sets(self):
        return self._opposite_sets

    def pair(self, exponent, codomain):
        return self.domain()(self.opposite_sets()(exponent), codomain)

    def _apply_object(self, pair):
        return ExponentialOfSets(pair.second(), pair.first().underlying_object())

    def _apply_morphism(self, pair_morphism):
        source = self(pair_morphism.domain())
        target = self(pair_morphism.codomain())
        precompose = pair_morphism.first().underlying_arrow()
        postcompose = pair_morphism.second()
        return SetMorphism(
            _OwnedSets().hom(source, target),
            lambda function: target(
                lambda element: postcompose(function(precompose(element)))
            ),
        )

    def morphism(self, precompose, postcompose):
        r"""Return the product-category morphism induced by ``precompose`` and ``postcompose``."""
        source = self.pair(precompose.codomain(), postcompose.domain())
        target = self.pair(precompose.domain(), postcompose.codomain())
        opposite = self.opposite_sets().hom(source.first(), target.first())(precompose)
        return self.domain().hom(source, target)(opposite, postcompose)


class InverseImagePowerSetFunctor(Functor):
    r"""The contravariant power-set functor on the opposite of Set."""

    def __init__(self) -> None:
        self._opposite_sets = OppositeCategory(Sets())
        super().__init__(self._opposite_sets, Sets())

    def opposite_sets(self):
        return self._opposite_sets

    def _apply_object(self, opposite_set):
        return PowerSet(opposite_set.underlying_object())

    def _apply_morphism(self, opposite_morphism):
        source = self(opposite_morphism.domain())
        return source.inverse_image_morphism(opposite_morphism.underlying_arrow())

    def opposite_morphism(self, morphism):
        return self.domain().hom(
            self.domain()(morphism.codomain()),
            self.domain()(morphism.domain()),
        )(morphism)


class FinitePowerSetFunctor(Functor):
    r"""The covariant finite-power-set functor under direct image."""

    def __init__(self) -> None:
        super().__init__(Sets(), Sets())

    def _apply_object(self, source):
        return FiniteSubsets(source)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return SetMorphism(
            _OwnedSets().hom(source, target),
            lambda subset: target(tuple(morphism(member) for member in subset)),
        )


class FixedCardinalitySubsetFunctor(Functor):
    r"""Direct image on ``k``-element subsets, defined on injective set maps."""

    def __init__(self, subset_cardinality) -> None:
        from sage.rings.integer_ring import ZZ

        self._subset_cardinality = ZZ(subset_cardinality)
        if self._subset_cardinality < 0:
            raise ValueError("a subset cardinality is nonnegative")
        injections = MonomorphismArrowCategory(Sets())
        super().__init__(WideSubcategory(Sets(), injections), Sets())

    def subset_cardinality(self):
        return self._subset_cardinality

    def _apply_object(self, source):
        return SubsetsOfSize(source, self.subset_cardinality())

    def _apply_morphism(self, morphism):
        if not self.domain().admits(morphism):
            raise TypeError("fixed-cardinality direct image requires an injective set map")
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return SetMorphism(
            _OwnedSets().hom(source, target),
            lambda subset: target(tuple(morphism(member) for member in subset)),
        )


@cached_function
def exponential_functor() -> ExponentialFunctor:
    return ExponentialFunctor()


@cached_function
def inverse_image_power_set_functor() -> InverseImagePowerSetFunctor:
    return InverseImagePowerSetFunctor()


@cached_function
def finite_power_set_functor() -> FinitePowerSetFunctor:
    return FinitePowerSetFunctor()


@cached_function
def fixed_cardinality_subset_functor(subset_cardinality) -> FixedCardinalitySubsetFunctor:
    return FixedCardinalitySubsetFunctor(subset_cardinality)


__all__ = [
    "ExponentialFunctor",
    "FinitePowerSetFunctor",
    "FixedCardinalitySubsetFunctor",
    "InverseImagePowerSetFunctor",
    "exponential_functor",
    "finite_power_set_functor",
    "fixed_cardinality_subset_functor",
    "inverse_image_power_set_functor",
]
