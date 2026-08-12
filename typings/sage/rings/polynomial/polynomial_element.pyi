# Repo-scoped stubs; see lexicon/README.md.
#
# The polynomial noun: every concrete Sage polynomial (flint, NTL, generic)
# derives from sage.rings.polynomial.polynomial_element.Polynomial, so the
# contract is stated once here.
from collections.abc import Sequence
from typing import Literal, overload

from sage.rings.integer import Integer
from sage.structure.element import CommutativeRingElement, Element, RingElement
from sage.structure.parent import Parent

class Polynomial(CommutativeRingElement):
    def degree(self) -> Integer: ...
    # Roots in `ring` (QQbar for the exact algebraic closure), as bare roots
    # or as (root, multiplicity) pairs.
    @overload
    def roots(
        self,
        ring: Parent[Element] | None = ...,
        multiplicities: Literal[True] = ...,
    ) -> Sequence[tuple[RingElement, Integer]]: ...
    @overload
    def roots(
        self,
        ring: Parent[Element] | None,
        multiplicities: Literal[False],
    ) -> Sequence[RingElement]: ...
    @overload
    def roots(
        self,
        *,
        ring: Parent[Element] | None = ...,
        multiplicities: Literal[False],
    ) -> Sequence[RingElement]: ...
