"""Divisor groups as framed free modules."""

from collections.abc import Mapping

from sage.misc.cachefunc import cached_method
from sage.misc.latex import latex

from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules, FreshFreeModuleOn
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


def _module_in_role(module, category, message, *, construction_data=None):
    r"""Return a fresh represented module born in the stated divisor role."""
    constructor = getattr(module, "_same_presentation_module", None)
    if constructor is None:
        raise NotImplementedError(message)
    return constructor(
        module.module_generating_set(),
        _extra_categories=(category,),
        _extra_construction_data=construction_data,
    )


def _divisor_role_specimen(category):
    r"""Return a one-generator owned free abelian group in ``category``."""
    from sage.rings.integer_ring import ZZ as SageZZ

    integers = _own_ring(SageZZ)
    module = FreshFreeModuleOn(integers, finite_ordered_set(("D",)))
    return _module_in_role(
        module,
        category,
        "a divisor-role specimen requires a represented free-module presentation",
    )


class DivisorGroups(Category):
    r"""Free abelian groups on specified prime divisors."""

    def an_object(self):
        return _divisor_role_specimen(self)

    @classmethod
    def _repr_object_names(cls):
        return "divisor groups"

    def super_categories(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedFreeModules(_own_ring(SageZZ))]

    def _call_(self, module):
        from sage.rings.integer_ring import ZZ as SageZZ

        if module not in FramedFreeModules(_own_ring(SageZZ)):
            raise TypeError("a divisor group is a free abelian group on specified prime divisors")
        return _module_in_role(
            module,
            self,
            "a divisor group requires a represented free-module presentation",
        )


class FormalDivisorGroups(OwnedCategoryOverBaseRing):
    r"""Formal divisors with coefficients in a specified ring."""

    def an_object(self):
        r"""The free ``R``-module on two prime divisors."""
        return self(("P", "Q"))

    @cached_method(key=lambda self, prime_divisors: tuple(prime_divisors))
    def _call_(self, prime_divisors):
        r"""Return the free formal-divisor group on the stated prime divisors."""
        return FreshFreeModuleOn(
            self.base_ring(),
            finite_ordered_set(prime_divisors),
            _extra_categories=(self,),
        )

    def from_terms(self, terms):
        r"""Return the formal linear combination of the stated prime divisors."""
        ring = self.base_ring()
        terms = (
            tuple((coefficient, prime_divisor) for prime_divisor, coefficient in terms.items())
            if isinstance(terms, Mapping)
            else tuple(terms)
        )
        prime_divisors = finite_ordered_set(
            tuple(prime_divisor for _, prime_divisor in terms)
        )
        group = self(tuple(prime_divisors))
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

    @classmethod
    def _repr_object_names(cls):
        return "formal divisor groups"

    def super_categories(self):
        return [FramedFreeModules(self.base_ring())]

    class ParentMethods:
        # A formal divisor is an element of the free module's engine, so the
        # group, not the element, answers questions about its terms.
        def terms(self, divisor):
            return finite_ordered_set(
                tuple(
                    (coefficient, prime_divisor)
                    for prime_divisor, coefficient in self.framing_coefficients(divisor).items()
                )
            )

        def components(self, divisor):
            return tuple(prime_divisor for _, prime_divisor in self.terms(divisor))

        def divisor_repr(self, divisor) -> str:
            terms = self.terms(divisor)
            if not terms:
                return "0"
            return " + ".join(
                f"{coefficient}*{prime_divisor}" for coefficient, prime_divisor in terms
            ).replace("+ -", "- ")

        def divisor_latex(self, divisor) -> str:
            terms = self.terms(divisor)
            if not terms:
                return "0"
            return " + ".join(
                rf"{latex(coefficient)}\,{latex(prime_divisor)}" for coefficient, prime_divisor in terms
            ).replace("+ -", "- ")
