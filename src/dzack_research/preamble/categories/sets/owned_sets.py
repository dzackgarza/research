"""The owned category of sets and its canonical finite/countable indexing objects."""

from sage.categories.category import Category
from sage.categories.homset import Hom
from sage.categories.sets_cat import Sets as SageSets
from sage.categories.sets_with_partial_maps import SetsWithPartialMaps
from sage.rings.integer_ring import ZZ
from sage.rings.semirings.non_negative_integer_semiring import NN
from sage.misc.cachefunc import cached_function


@cached_function
def _finite_delta(dimension):
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

    return finite_ordered_set(ZZ.range(ZZ(dimension) + 1))


class _Delta:
    r"""The standard finite ordinals \(\Delta[n]=\{0,\ldots,n\}\), and \(\Delta[\aleph_0]=\mathbb N\)."""

    def __getitem__(self, dimension):
        from dzack_research.preamble.categories.sets.cardinals import aleph0, cardinal
        if dimension == -1:
            return _finite_delta(-1)
        size = cardinal(dimension)
        if size == aleph0:
            return NN
        if not size.is_finite():
            raise ValueError("the represented simplex index is finite or countably infinite")
        return _finite_delta(size.finite_value())

    def __repr__(self) -> str:
        return "Δ"


class _Aleph:
    def __getitem__(self, index):
        from dzack_research.preamble.categories.sets.cardinals import aleph

        return aleph(index)

    def __repr__(self) -> str:
        return "ℵ"


class Sets(Category):
    r"""The owned category of sets.

    All Sage set objects are admitted.  The category owns the mathematical
    constructions the preamble adds; Sage remains the implementation of
    ordinary set maps.

    Every owned object is realised as a Sage ``Parent``, and Sage's coercion
    layer states one thing about every parent it converts into: it is an
    object of ``SetsWithPartialMaps``, the category of sets whose maps may be
    partial.  That is the single crossing between the owned graph and Sage's,
    declared once here at the root; no owned category below it names a Sage
    category.
    """

    Δ = _Delta()
    ℵ = _Aleph()
    א = ℵ

    def super_categories(self):
        return [SetsWithPartialMaps()]

    def __contains__(self, candidate) -> bool:
        try:
            if candidate.category().is_subcategory(self):
                return True
        except AttributeError:
            pass
        try:
            return candidate in SageSets()
        except (TypeError, ValueError):
            return False

    def hom(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a set morphism requires two set objects")
        return Hom(domain, codomain, self)

    Hom = hom
    homset = hom

    class SubcategoryMethods:
        def Homsets(self):
            r"""A Hom object of any owned category is a set."""
            return Homsets()

        def Endsets(self):
            r"""An endomorphism object of any owned category is a monoid under composition."""
            return Endsets()

    def identity(self, set_object):
        return self.hom(set_object, set_object).identity()

    def Countable(self):
        return CountableSets()

    def CountablyInfinite(self):
        return CountablyInfiniteSets()

    def Uncountable(self):
        return UncountableSets()

    def PartiallyOrdered(self):
        return PartiallyOrderedSets()

    def TotallyOrdered(self):
        return TotallyOrderedSets()

    class ParentMethods:
        def power_set(self):
            from dzack_research.preamble.categories.sets.sets import PowerSet

            return PowerSet(self)

        def exponential(self, exponent):
            from dzack_research.preamble.categories.sets.sets import ExponentialOfSets

            return ExponentialOfSets(self, exponent)

        def subsets_of_size(self, size):
            from dzack_research.preamble.categories.sets.sets import SubsetsOfSize

            return SubsetsOfSize(self, size)

        def finite_subsets(self):
            from dzack_research.preamble.categories.sets.sets import FiniteSubsets

            return FiniteSubsets(self)


__all__ = ["Sets"]


class Homsets(Category):
    r"""Hom objects \(\operatorname{Hom}(X,Y)\), which are sets."""

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def is_endomorphism_set(self) -> bool:
            return self.domain() is self.codomain()


class Endsets(Category):
    r"""Endomorphism objects \(\operatorname{End}(X)\), monoids under composition."""

    def super_categories(self):
        from dzack_research.preamble.categories.group.magmas import Monoids

        return [Homsets(), Monoids()]

    class ParentMethods:
        def is_endomorphism_set(self) -> bool:
            return True


class FiniteSets(Category):
    r"""Sets whose cardinality is finite."""

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        if candidate not in Sets():
            return False
        try:
            return candidate in SageSets().Finite()
        except (TypeError, ValueError):
            return False


class InfiniteSets(Category):
    r"""Sets whose cardinality is infinite."""

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        if candidate not in Sets():
            return False
        try:
            return candidate in SageSets().Infinite()
        except (TypeError, ValueError):
            return False


class CountableSets(Category):
    r"""Sets equipped with a countable enumeration."""

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        if candidate not in Sets():
            return False
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        try:
            return cardinal(candidate.cardinality()).is_countable()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return False


class CountablyInfiniteSets(Category):
    r"""Countably infinite sets."""

    def super_categories(self):
        return [CountableSets(), InfiniteSets()]

    def __contains__(self, candidate) -> bool:
        if candidate not in Sets():
            return False
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        try:
            return cardinal(candidate.cardinality()).is_countably_infinite()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return False


class UncountableSets(Category):
    r"""Sets whose represented cardinal is provably uncountable."""

    def super_categories(self):
        return [InfiniteSets()]

    def __contains__(self, candidate) -> bool:
        if candidate not in Sets():
            return False
        from dzack_research.preamble.categories.sets.cardinals import cardinal

        try:
            return cardinal(candidate.cardinality()).is_uncountable()
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return False


class PartiallyOrderedSets(Category):
    r"""Sets equipped with a partial order."""

    def super_categories(self):
        return [Sets()]


class TotallyOrderedSets(Category):
    r"""Sets equipped with a total order."""

    def super_categories(self):
        return [PartiallyOrderedSets()]


class FinitelySupportedFunctionSets(Category):
    r"""Function sets whose elements have finite support."""

    def super_categories(self):
        return [Sets()]



def placement_of(parent):
    r"""Return the strongest represented owned Set cardinality category for ``parent``."""
    if parent in FiniteSets():
        return FiniteSets()
    if parent in CountablyInfiniteSets():
        return CountablyInfiniteSets()
    if parent in UncountableSets():
        return UncountableSets()
    if parent in InfiniteSets():
        return InfiniteSets()
    if parent in CountableSets():
        return CountableSets()
    return Sets()


def register_set_axioms() -> None:
    r"""Compatibility entry point: the live owned categories need no Sage-global mutation."""
    return None


class SetSubcategoryMethods:
    r"""Compatibility name for the owned Set category-navigation surface."""


__all__ = [
    "CountableSets",
    "CountablyInfiniteSets",
    "FiniteSets",
    "FinitelySupportedFunctionSets",
    "InfiniteSets",
    "PartiallyOrderedSets",
    "SetSubcategoryMethods",
    "Sets",
    "TotallyOrderedSets",
    "UncountableSets",
    "placement_of",
    "register_set_axioms",
]
