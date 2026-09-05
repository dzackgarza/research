"""The owned operation spine below groups."""

from sage.categories.category import Category
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism

class Magmas(OwnedCategory):
    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

        return [Sets()]


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


class CommutativeAdditiveGroups(OwnedCategory):
    """Additive groups whose addition is commutative."""

    def super_categories(self):
        return [AdditiveGroups()]


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
