r"""Divisor groups as framed free \(\mathbb Z\)-modules."""

from sage.rings.integer_ring import ZZ as SageZZ
from sage.misc.latex import latex
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.categories.rings import Ring
    from sage.structure.element import Element, RingElement
    from dzack_research.preamble.lexicon import OrderedSet

from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.refine import refine
from dzack_research.preamble.owned_category_bases import Category
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.sets.sets import finite_ordered_set


def DivisorGroup(module: "Module") -> "Module":
    r"""Refine the declared free module of divisors."""
    assert module in FramedFreeModules(SageZZ), (
        "a divisor group is constructed from its actual set of prime divisors"
    )
    return refine(module, DivisorGroups())


class DivisorGroups(Category):
    r"""Free abelian groups on specified prime divisors."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "divisor groups"

    def super_categories(self) -> list:
        return [FramedFreeModules(SageZZ)]


class FormalDivisorGroups(OwnedCategoryOverBaseRing):
    r"""Divisor groups with coefficients in a specified ring."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "formal divisor groups"

    def super_categories(self) -> list:
        return [FramedFreeModules(self.base_ring())]

    class ElementMethods:
        def terms(self) -> tuple[tuple["RingElement", "Element"], ...]:
            r"""Return the nonzero coefficients and prime divisors."""
            return tuple(
                (coefficient, prime_divisor)
                for prime_divisor, coefficient in self.coefficients().items()
            )

        def components(self) -> tuple["Element", ...]:
            r"""Return the prime divisors in the support."""
            return tuple(
                prime_divisor for _, prime_divisor in self.terms()
            )

        def _repr_(self) -> str:
            return " + ".join(
                f"{coefficient}*{prime_divisor}"
                for coefficient, prime_divisor in self.terms()
            ).replace("+ -", "- ")

        def _latex_(self) -> str:
            return " + ".join(
                rf"{latex(coefficient)}\,{latex(prime_divisor)}"
                for coefficient, prime_divisor in self.terms()
            ).replace("+ -", "- ")


def FormalDivisor(
    coefficient_ring: "Ring",
    terms: "tuple[tuple[RingElement, Element], ...]",
) -> "Element":
    r"""Return a formal divisor in the free module on its prime support."""
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreeModuleOn,
    )

    prime_divisors: "OrderedSet" = finite_ordered_set(
        tuple(dict.fromkeys(prime_divisor for _, prime_divisor in terms))
    )
    divisor_group = refine(
        FreeModuleOn(coefficient_ring, prime_divisors),
        FormalDivisorGroups(coefficient_ring),
    )
    coefficients = {
        prime_divisor: sum(
            (
                coefficient
                for coefficient, component in terms
                if component == prime_divisor
            ),
            coefficient_ring.zero(),
        )
        for prime_divisor in prime_divisors
    }
    divisor: "Element" = divisor_group(coefficients)
    return divisor
