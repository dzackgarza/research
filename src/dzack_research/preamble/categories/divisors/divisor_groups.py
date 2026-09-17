r"""Divisor groups as framed free modules.

A divisor group is built once, by the free-module construction of its
underlying abelian group with the divisor category joined to it.  Each divisor
category level stores only the datum it adds and threads the rest to the module
levels through ``super().__init__``.
"""

from sage.misc.cachefunc import cached_method
from sage.misc.latex import latex
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


def _integers():
    return _own_ring(SageZZ)


def _cokernel_in_category(presentation, category, **data):
    r"""\(\operatorname{coker}(\rho)\) for the morphism ``presentation`` \(\rho\colon F \to G\), built once in ``category``.

    The cokernel is framed by the generators of \(G\), and its
    ``cokernel_projection()`` is the quotient map \(G \to \operatorname{coker}\rho\).
    The levels of ``category`` consume ``data`` in their constructors.
    """
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _presented_module_from_morphism,
    )

    return _presented_module_from_morphism(
        presentation,
        _cokernel_morphism=presentation,
        _extra_categories=(category,),
        _extra_construction_data=data,
    )


def _zero_presentation():
    r"""The zero morphism \(0 \to 0\) of abelian groups, whose cokernel is the zero group."""
    zero = _integers().free_module(finite_ordered_set(()))
    return zero.module_category().Mor(zero, zero)({})


def _free_presentation(generators):
    r"""The zero morphism \(0 \to \mathbb{Z}^{(S)}\), presenting the free abelian group on ``generators``."""
    integers = _integers()
    zero = integers.free_module(finite_ordered_set(()))
    free = integers.free_module(generators)
    return zero.module_category().Mor(zero, free)({})


def _affine_line_over_integers():
    r"""\(\mathbb{A}^1_{\mathbb{Z}} = \operatorname{Spec} \mathbb{Z}[x]\), the witness scheme of the divisor categories."""
    integers = _integers()
    return integers.polynomial_ring(("x",)).affine_spectrum(base_ring=integers)


class DivisorGroups(Category):
    r"""Free abelian groups on specified prime divisors.

    An object is the free \(\mathbb{Z}\)-module \(\bigoplus_{P \in S} \mathbb{Z}P\)
    on a set \(S\) of prime divisors, framed by \(S\).  The set \(S\) is the
    defining datum and the free-module level consumes it; this level adds no
    datum of its own.
    """

    def an_object(self):
        r"""The free abelian group on one prime divisor."""
        return self(finite_ordered_set(("D",)))

    @classmethod
    def _repr_object_names(cls):
        return "divisor groups"

    def super_categories(self):
        return [FramedFreeModules(_own_ring(SageZZ))]

    def _call_(self, prime_divisors):
        r"""The free abelian group on the set ``prime_divisors`` of prime divisors."""
        return _integers()._fresh_free_module_on(
            prime_divisors,
            _extra_categories=(self,),
        )


class FormalDivisorGroups(OwnedCategoryOverBaseRing):
    r"""Formal divisors with coefficients in a specified ring."""

    def an_object(self):
        r"""The free ``R``-module on two prime divisors."""
        return self(("P", "Q"))

    @cached_method(key=lambda self, prime_divisors: tuple(prime_divisors))
    def _call_(self, prime_divisors):
        r"""Return the free formal-divisor group on the stated prime divisors."""
        return self.base_ring()._fresh_free_module_on(
            finite_ordered_set(prime_divisors),
            _extra_categories=(self,),
        )

    def from_terms(self, terms):
        r"""The formal divisor \(\sum_i a_i P_i\) of a finite family of terms \((a_i, P_i)\).

        A prime divisor occurring in several terms receives the sum of their
        coefficients, so the result is the finitely supported coefficient
        function \(P \mapsto \sum_{P_i = P} a_i\).
        """
        ring = self.base_ring()
        terms = tuple(terms)
        prime_divisors = finite_ordered_set(
            tuple(prime_divisor for _, prime_divisor in terms)
        )
        group = self(tuple(prime_divisors))
        return group.linear_combination(
            {
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
        )

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
