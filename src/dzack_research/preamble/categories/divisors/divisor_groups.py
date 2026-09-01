"""Divisor groups as framed free modules."""

from sage.categories.category import Category
from sage.misc.latex import latex

from dzack_research.preamble.categories.modules import FramedFreeModules, FreeModuleOn
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing, owned_ring_view
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class DivisorGroups(Category):
    r"""Free abelian groups on specified prime divisors."""

    @classmethod
    def _repr_object_names(cls):
        return "divisor groups"

    def super_categories(self):
        from dzack_research.preamble.categories.rings import own_ring
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedFreeModules(own_ring(SageZZ))]


def DivisorGroup(module):
    from dzack_research.preamble.categories.rings import own_ring
    from sage.rings.integer_ring import ZZ as SageZZ

    if module not in FramedFreeModules(own_ring(SageZZ)):
        raise TypeError("a divisor group is a free abelian group on specified prime divisors")
    return refine(module, DivisorGroups())


class FormalDivisorGroups(OwnedCategoryOverBaseRing):
    r"""Formal divisors with coefficients in a specified ring."""

    @classmethod
    def _repr_object_names(cls):
        return "formal divisor groups"

    def super_categories(self):
        return [FramedFreeModules(self.base_ring())]

    class ElementMethods:
        def terms(self):
            return tuple(
                (coefficient, prime_divisor)
                for prime_divisor, coefficient in module_coefficients(self).items()
            )

        def components(self):
            return tuple(prime_divisor for _, prime_divisor in self.terms())

        def _repr_(self):
            if not self.terms():
                return "0"
            return " + ".join(
                f"{coefficient}*{prime_divisor}"
                for coefficient, prime_divisor in self.terms()
            ).replace("+ -", "- ")

        def _latex_(self):
            if not self.terms():
                return "0"
            return " + ".join(
                rf"{latex(coefficient)}\,{latex(prime_divisor)}"
                for coefficient, prime_divisor in self.terms()
            ).replace("+ -", "- ")


def FormalDivisor(coefficient_ring, terms):
    r"""Return the formal linear combination of the stated prime divisors."""
    ring = owned_ring_view(coefficient_ring)
    terms = tuple(terms)
    prime_divisors = finite_ordered_set(
        prime_divisor
        for _, prime_divisor in terms
    )
    group = refine(
        FreeModuleOn(ring, prime_divisors),
        FormalDivisorGroups(ring),
    )
    coefficients = {
        prime_divisor: sum(
            (
                ring(coefficient)
                for coefficient, component in terms
                if component == prime_divisor
            ),
            ring.zero(),
        )
        for prime_divisor in prime_divisors
    }
    return group.linear_combination(coefficients)
