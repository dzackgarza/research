r"""Cartier divisor groups."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.divisors.divisor_groups import (
    _affine_line_over_integers,
    _cokernel_in_category,
    _free_presentation,
)
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


class CartierDivisorGroups(Category):
    r"""Cartier divisor groups of a scheme, with a chosen presentation.

    An object is \(\operatorname{coker}(\rho)\) for a morphism
    \(\rho\colon F \to G\) of framed abelian groups presenting Cartier divisors
    of one scheme \(X\), framed by the generators of \(G\).  The presentation
    \(\rho\) is consumed by the presented-module level; this level adds \(X\).
    A group free on chosen Cartier divisors is presented by \(\rho = 0\).
    """

    def an_object(self):
        r"""Cartier divisors of \(\mathbb{A}^1_{\mathbb{Z}}\) framed by one divisor with no relation."""
        return self(_affine_line_over_integers(), _free_presentation(finite_ordered_set(("D",))))

    @classmethod
    def _repr_object_names(cls):
        return "Cartier divisor groups"

    def super_categories(self):
        return [FramedModules(_own_ring(SageZZ))]

    def _call_(self, scheme, presentation):
        r"""\(\operatorname{coker}(\rho)\) for the presentation ``presentation`` of Cartier divisors of ``scheme``."""
        return _cokernel_in_category(presentation, self, divisor_scheme=scheme)

    class ParentMethods:
        def __init__(self, divisor_scheme, **rest) -> None:
            self._divisor_scheme = divisor_scheme
            super().__init__(**rest)

        def divisor_scheme(self):
            r"""The scheme whose Cartier divisors this group presents."""
            return self._divisor_scheme


__all__ = ["CartierDivisorGroups"]
