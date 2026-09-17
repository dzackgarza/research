"""Divisor groups as framed free modules."""

from sage.misc.cachefunc import cached_method
from sage.misc.latex import latex

from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.modules.pure.modules import (
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


def _integers():
    from sage.rings.integer_ring import ZZ as SageZZ

    return _own_ring(SageZZ)


def _module_in_role(module, category, **construction_data):
    r"""The object of ``category`` built on the presentation of ``module``.

    The role's object is constructed on the presentation ``module`` carries,
    through the module constructor that built ``module``; the levels
    ``category`` adds consume ``construction_data`` in their cooperative
    constructors.  The result is framed by ``module.module_generating_set()``,
    so :func:`_framing_identity` relates the two.
    """
    ring = module.base_ring()
    assert (
        module in FramedFreeModules(ring).FinitelyGenerated()
        or module in ModulesWithChosenFinitePresentation(ring)
    ), (
        f"{category} is stated on a module with a finitely framed free or a chosen "
        f"finite presentation, which {module} does not carry"
    )
    return module._same_presentation_module(
        module.module_generating_set(),
        _extra_categories=(category,),
        _extra_construction_data=construction_data,
    )


def _framing_identity(source, role):
    r"""The isomorphism ``source -> role`` sending each framing generator to its namesake.

    ``role`` was built on the presentation of ``source`` by
    :func:`_module_in_role`, so the two share one framing and this is the
    identity in those coordinates.
    """
    return source.module_category().Mor(source, role)(
        {label: role.module_generator(label) for label in source.module_generating_set()}
    )


class DivisorGroups(Category):
    r"""Free abelian groups on specified prime divisors.

    An object is the free \(\mathbb{Z}\)-module on a chosen set of prime
    divisors, framed by that set.
    """

    def an_object(self):
        r"""The free abelian group on one prime divisor."""
        return self(_integers().free_module(finite_ordered_set(("D",))))

    @classmethod
    def _repr_object_names(cls):
        return "divisor groups"

    def super_categories(self):
        return [FramedFreeModules(_integers())]

    def _call_(self, module):
        assert module in FramedFreeModules(_integers()), (
            "a divisor group is a free abelian group on specified prime divisors"
        )
        return _module_in_role(module, self)


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
        r"""The formal divisor \(\sum_P a_P\,P\) of the finitely supported ``terms``.

        ``terms`` is the finitely supported coefficient function
        \(P \mapsto a_P\), given as a mapping from prime divisors to
        coefficients.
        """
        ring = self.base_ring()
        prime_divisors = finite_ordered_set(tuple(terms))
        group = self(tuple(prime_divisors))
        return group.linear_combination(
            {prime_divisor: ring(terms[prime_divisor]) for prime_divisor in prime_divisors}
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
