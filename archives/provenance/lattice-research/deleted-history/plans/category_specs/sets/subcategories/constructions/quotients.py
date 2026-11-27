r"""Quotient construction category for sets."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method

from ....cat import QuotientsCategory

if TYPE_CHECKING:
    from ....types import QuotientSet, Set, SetElement, SetMorphism


class _Quotients(QuotientsCategory):
    r"""Quotient sets as equivalence-class objects.

    Canonical chain: ``Sets().Quotients()``.

    This remains an attachable Sage construction category: ``Sets().Quotients()``
    and ``C.Quotients()`` for a set subcategory ``C`` are built with
    ``category_of`` rather than as singleton categories.
    """

    class ParentMethods:
        @abstract_method
        def ambient_set(self) -> Set:
            r"""Return the set being quotiented."""
            ...

        @abstract_method
        def projection(self) -> SetMorphism:
            r"""Return the quotient projection from the ambient set."""
            ...

        @abstract_method
        def equivalence_class(self, x: SetElement) -> QuotientSet:
            r"""Return the equivalence class of ``x``."""
            ...

    class ElementMethods:
        @abstract_method
        def representative(self) -> SetElement:
            r"""Return a representative of this equivalence class."""
            ...

    class MorphismMethods: ...
