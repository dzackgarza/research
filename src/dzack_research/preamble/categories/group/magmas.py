"""The owned operation spine below groups."""

from sage.categories.category import Category
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)

class Magmas(OwnedCategory):
    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return [Sets()]

    class SubcategoryMethods:
        def Commutative(self):
            r"""Return this category with the axiom ``xy = yx``.

            Commutativity is a property of the operation, so it is stated once
            here, at the level that introduces the operation, and every
            subcategory reaches it.
            """
            return self._with_axiom("Commutative")


class Semigroups(OwnedCategory):
    def super_categories(self):
        return [Magmas()]


class Monoids(OwnedCategory):
    def super_categories(self):
        return [Semigroups()]

    class ElementMethods:
        def _pow_int(self, exponent):
            r"""Integer powers by repeated squaring, from the monoid law."""
            from sage.arith.power import generic_power

            return generic_power(self, exponent)

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a monoid Hom requires two monoids")
        return MonoidHomset(domain, codomain)



class AdditiveMagmas(OwnedCategory):
    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return [Sets()]

    class SubcategoryMethods:
        def AdditiveCommutative(self):
            r"""Return this category with the axiom ``x + y = y + x``."""
            return self._with_axiom("AdditiveCommutative")


class AdditiveSemigroups(OwnedCategory):
    def super_categories(self):
        return [AdditiveMagmas()]


class AdditiveMonoids(OwnedCategory):
    def super_categories(self):
        return [AdditiveSemigroups()]

    class ParentMethods:
        def monoidal_unit(self):
            return self.zero()


class AdditiveGroups(OwnedCategory):
    def super_categories(self):
        return [AdditiveMonoids()]

    class AdditiveCommutative(CategoryWithAxiom):
        """Additive groups whose addition is commutative."""

        class _HomCategory(HomCategoryConstruction):
            def fixed_category_class(self):
                from dzack_research.preamble.categories.group.additive_homsets import (
                    AdditiveHomset,
                )

                return AdditiveHomset

        @classmethod
        def _repr_object_names(cls):
            return "commutative additive groups"


class MonoidMorphism(Morphism):
    """A morphism in the owned category of monoids."""

    def __init__(self, parent, function) -> None:
        Morphism.__init__(self, parent)
        if not callable(function):
            raise TypeError("a monoid morphism requires an exact element map")
        self._function = function

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        return self.codomain()(self._function(self.domain()(element)))

    def __mul__(self, other):
        if not isinstance(other, MonoidMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        return MonoidHomset(other.domain(), self.codomain())(
            lambda element: self(other(element))
        )


class MonoidHomset(Homset):
    """The owned set ``Hom_Mon(A,B)``."""

    Element = MonoidMorphism

    def __init__(self, domain, codomain) -> None:
        from dzack_research.preamble.categories.sets.set_categories import Sets

        Homset.__init__(self, domain, codomain, category=Sets())

    def __call__(self, function):
        if isinstance(function, MonoidMorphism):
            if function.domain() is not self.domain() or function.codomain() is not self.codomain():
                raise ValueError("the monoid morphism has the wrong source or target")
            if function.parent() is self:
                return function
            function = function.__call__
        return self.element_class(self, function)

    _element_constructor_ = __call__

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on a monoid endomorphism Hom-set")
        return self(lambda element: element)
