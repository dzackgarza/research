r"""Functors and natural transformations as arrows in the Cat type tower."""

from typing import TYPE_CHECKING

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from sage.categories.category import Category
    from sage.categories.morphism import Morphism
    from sage.structure.parent import Parent

    from dzack_research.preamble.categories.abstract_categories.hom_categories import (
        HomCategoryOf,
    )


class Functor(Cat().ArrowType):
    r"""A functor, as an object of \(\operatorname{Hom}_{\mathbf{Cat}}(C,D)\)."""

    def __init__(
        self,
        domain: "Category",
        codomain: "Category",
        hom_category: "Category | None" = None,
    ) -> None:
        parent = Cat().Hom(domain, codomain) if hom_category is None else hom_category
        assert parent.domain() is domain
        assert parent.codomain() is codomain
        super().__init__(hom_category=parent)


class IdentityFunctor(Functor):
    r"""The identity arrow of a category in \(\mathbf{Cat}\)."""

    _faithful = True

    def __init__(
        self,
        category: "Category",
        hom_category: "Category | None" = None,
    ) -> None:
        parent = Cat().Hom(category, category) if hom_category is None else hom_category
        Functor.__init__(self, category, category, hom_category=parent)

    def _apply_functor(
        self,
        obj: "Parent | Category",
    ) -> "Parent | Category":
        return obj

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        return morphism

    def factors(self) -> tuple[Functor, ...]:
        return ()

    def _repr_(self) -> str:
        return f"Identity functor of {self.domain()}"


def compose_functors(
    second: Functor,
    first: Functor,
    hom_category: "Category | None" = None,
) -> Functor:
    r"""Return the flattened composite ``second`` after ``first``."""
    assert first.codomain() is second.domain(), (
        "functors compose only when their middle category agrees"
    )
    factors = first.factors() + second.factors()
    if not factors:
        return IdentityFunctor(first.domain(), hom_category=hom_category)
    if len(factors) == 1:
        return factors[0]
    return ComposedFunctor(factors, hom_category=hom_category)


class ComposedFunctor(Functor):
    r"""A flattened nonempty sequence of composable functors."""

    def __init__(
        self,
        factors: tuple[Functor, ...],
        hom_category: "Category | None" = None,
    ) -> None:
        assert factors
        for early, late in zip(factors, factors[1:]):
            assert early.codomain() is late.domain(), (
                "functors compose only when their middle category agrees"
            )
        self._factors = factors
        Functor.__init__(
            self,
            factors[0].domain(),
            factors[-1].codomain(),
            hom_category=hom_category,
        )

    def factors(self) -> tuple[Functor, ...]:
        return self._factors

    def is_faithful(self) -> bool:
        return all(factor.is_faithful() for factor in self._factors)

    def _apply_functor(
        self,
        obj: "Parent | Category",
    ) -> "Parent | Category":
        result = obj
        for factor in self._factors:
            result = factor(result)
        return result

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        result = morphism
        for factor in self._factors:
            result = factor(result)
        return result

    def _repr_(self) -> str:
        return " . ".join(str(factor) for factor in reversed(self._factors))


def NaturalTransformations(source: Functor, target: Functor) -> "Category":
    r"""Return the Hom category of natural transformations \(F\Rightarrow G\)."""
    assert source.parent() is target.parent(), (
        "natural transformations require parallel functors"
    )
    return source.parent().Hom(source, target)


def NaturalTransformation(
    source: Functor,
    target: Functor,
    components: "Callable",
) -> "HomCategoryOf.ElementMethods":
    r"""Construct a natural transformation from its declared components."""
    return NaturalTransformations(source, target)(components)


def NaturalIsomorphism(
    source: Functor,
    target: Functor,
    components: "Callable",
    inverse_components: "Callable",
) -> "HomCategoryOf.ElementMethods":
    r"""Construct a natural isomorphism from mutually inverse components."""
    forward = NaturalTransformation(source, target, components)
    backward = NaturalTransformation(target, source, inverse_components)
    return Isomorphism(forward, backward)
