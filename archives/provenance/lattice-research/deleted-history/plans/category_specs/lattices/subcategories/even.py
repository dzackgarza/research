r"""Even lattices."""

from __future__ import annotations

from typing import final, override

from ...cat import CategoryWithAxiom_over_base_ring
from ..chain import LatticesCategory


class _EvenLattices(CategoryWithAxiom_over_base_ring):
    r"""Integral lattices whose self-products are even.

    Canonical chain: ``Lattices(R).Even()``.
    """

    _base_category_class_and_axiom = (LatticesCategory, "Even")
    _defining_predicates = ("is_even",)

    class ParentMethods:
        @override
        @final
        def is_even(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
