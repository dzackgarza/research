"""Semirings and rngs, their Mor families, and the initial semiring.

The natural numbers are the initial owned semiring. Ring objects refine the
semiring Mor theory by their stronger ring Mor theory, while every unital ring
still receives the unique semiring morphism from the natural numbers.
"""

from sage.rings.integer_ring import ZZ as SageZZ
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    AdditiveMonoids,
    MonoidMorphism,
    Monoids,
    Semigroups,
)


class SemiringMorphism(MonoidMorphism):
    """A declared unital semiring morphism."""

    def __init__(self, parent, function) -> None:
        if not callable(function):
            raise TypeError(
                f"a semiring morphism {parent.domain()} -> {parent.codomain()} needs a map on elements, but "
                f"{function!r} is not callable"
            )
        self._function = function
        MonoidMorphism.__init__(self, parent, function)

    def _composition(self, right):
        if not (
            isinstance(right, SemiringMorphism)
            and right.codomain() is self.domain()
        ):
            return NotImplemented
        target = OwnedSemirings().Mor(right.domain(), self.codomain())
        return target(lambda element: self(right(element)))


class SemiringMor(CategoricalMor):
    """The fixed Mor object of unital semiring morphisms."""

    Element = SemiringMorphism

    def _element_constructor_(self, function):
        if isinstance(function, SemiringMorphism):
            if (
                function.domain() is not self.domain()
                or function.codomain() is not self.codomain()
            ):
                raise ValueError(
                    f"{function} is a semiring morphism {function.domain()} -> {function.codomain()}, not a "
                    f"morphism {self.domain()} -> {self.codomain()}"
                )
            if function.parent() is self:
                return function
            function = function.__call__
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"there is no identity morphism {self.domain()} -> {self.codomain()}: an identity exists only "
                "when the domain and codomain are the same semiring"
            )
        return self(lambda element: element)


class SemiringMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return SemiringMor


class RingMorCategoryConstruction(MorCategoryConstruction):
    r"""The owned family ``(A,B) |-> Hom_Ring(A,B)``."""

    def fixed_category_class(self):
        from dzack_research.preamble.categories.rings.ring_foundation import RingMor

        return RingMor


class RngMorCategoryConstruction(MorCategoryConstruction):
    r"""The owned family ``(A,B) |-> Hom_Rng(A,B)``."""

    def fixed_category_class(self):
        from dzack_research.preamble.categories.rings.ring_foundation import RngMor

        return RngMor


class OwnedSemirings(OwnedCategory):
    """Semirings on the owned operation spine."""

    _MorCategory = SemiringMorCategoryConstruction

    def an_object(self):
        r"""The integers, which are in particular a semiring."""
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)

    def super_categories(self):
        return [Monoids(), AdditiveMonoids()]

    def initial_object(self):
        """Return the natural numbers, initial among unital semirings."""
        from dzack_research.preamble.categories.sets.set_categories import NN

        return NN

    def initial_morphism(self, codomain):
        """Return the unique unital semiring morphism from NN to codomain."""
        if codomain not in self:
            raise TypeError(
                f"the initial semiring morphism needs a semiring codomain, but {codomain} lies in "
                f"{codomain.category()}"
            )
        source = self.initial_object()
        morphisms = self.Mor(source, codomain)
        if codomain is source:
            return morphisms.identity()

        def image(natural):
            count = int(natural)
            result = codomain.zero()
            summand = codomain.one()
            while count:
                if count % 2:
                    result = result + summand
                count //= 2
                if count:
                    summand = summand + summand
            return result

        return morphisms(image)


class OwnedRngs(OwnedCategory):
    """Rngs on the owned operation spine."""

    _MorCategory = RngMorCategoryConstruction

    def an_object(self):
        r"""The integers, which happen to be unital."""
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)

    def super_categories(self):
        return [Semigroups(), AdditiveGroups().AdditiveCommutative()]


__all__ = [
    "OwnedRngs",
    "OwnedSemirings",
    "RingMorCategoryConstruction",
    "SemiringMor",
    "SemiringMorCategoryConstruction",
    "SemiringMorphism",
]
