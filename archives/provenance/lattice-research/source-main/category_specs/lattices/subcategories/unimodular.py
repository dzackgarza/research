r"""Unimodular lattices."""

from __future__ import annotations

from typing import final

from ...cat import CategoryWithAxiom_over_base_ring
from ..chain import LatticesCategory


class _UnimodularLattices(CategoryWithAxiom_over_base_ring):
    r"""Integral lattices whose discriminant group is trivial.

    Canonical chain: ``Lattices(R).Unimodular()``.
    """

    _base_category_class_and_axiom = (LatticesCategory, "Unimodular")
    _defining_predicates = ("is_unimodular",)

    class ParentMethods:
        @final
        def is_unimodular(self) -> bool:
            return True

    class ElementMethods: ...
