"""Divisor groups as framed free modules."""

from collections.abc import Mapping

from sage.categories.category import Category
from sage.misc.cachefunc import cached_function
from sage.misc.latex import latex

from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreshFreeModuleOn
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def _module_in_role(module, category, message):
    r"""Return a fresh represented module born in the stated divisor role."""
    constructor = getattr(module, "_same_presentation_module", None)
    if constructor is None:
        raise NotImplementedError(message)
    return constructor(
        module.module_generating_set(),
        _extra_categories=(category,),
    )


class DivisorGroups(Category):
    r"""Free abelian groups on specified prime divisors."""

    @classmethod
    def _repr_object_names(cls):
        return "divisor groups"

    def super_categories(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedFreeModules(_own_ring(SageZZ))]


def DivisorGroup(module):
    from sage.rings.integer_ring import ZZ as SageZZ

    if module not in FramedFreeModules(_own_ring(SageZZ)):
        raise TypeError("a divisor group is a free abelian group on specified prime divisors")
    return _module_in_role(
        module,
        DivisorGroups(),
        "a divisor group requires a represented free-module presentation",
    )


class FormalDivisorGroups(OwnedCategoryOverBaseRing):
    r"""Formal divisors with coefficients in a specified ring."""

    def an_object(self):
        r"""The free ``R``-module on two prime divisors."""
        return FormalDivisorGroup(self.base_ring(), ("P", "Q"))

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
                    for prime_divisor, coefficient in module_coefficients(
                        divisor, self
                    ).items()
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


@cached_function
def FormalDivisorGroup(coefficient_ring, prime_divisors):
    r"""Return the group of formal divisors on the stated prime divisors, one per ``(R, S)``."""
    ring = _owned_ring(coefficient_ring)
    return FreshFreeModuleOn(
        ring,
        finite_ordered_set(prime_divisors),
        _extra_categories=(FormalDivisorGroups(ring),),
    )


def FormalDivisor(coefficient_ring, terms):
    r"""Return the formal linear combination of the stated prime divisors.

    The divisor is an element of ``FormalDivisorGroup(R, S)`` for ``S`` the
    prime divisors in ``terms``, in order of first appearance; that group
    answers ``terms``, ``components`` and printing for it.
    """
    ring = _owned_ring(coefficient_ring)
    terms = (
        tuple((coefficient, prime_divisor) for prime_divisor, coefficient in terms.items())
        if isinstance(terms, Mapping)
        else tuple(terms)
    )
    prime_divisors = finite_ordered_set(
        tuple(prime_divisor for _, prime_divisor in terms)
    )
    group = FormalDivisorGroup(ring, tuple(prime_divisors))
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
