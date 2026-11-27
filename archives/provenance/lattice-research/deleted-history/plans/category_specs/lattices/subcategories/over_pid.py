r"""Lattices over principal ideal domains."""

from __future__ import annotations

from typing import final

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .over_dedekind import _LatticesOverDedekindDomain


class _LatticesOverPID(CategoryWithAxiom_over_base_ring):
    r"""Lattices whose base ring is a principal ideal domain.

    Canonical chain: ``Lattices(R).OverDedekindDomain().OverPID()``.
    """

    _base_category_class_and_axiom = (_LatticesOverDedekindDomain, "OverPID")
    _defining_predicates = ("is_over_pid",)

    class ParentMethods:
        @final
        def is_over_pid(self) -> bool:
            return True

        @abstract_method
        def is_over_integers(self) -> bool: ...

    class ElementMethods: ...
    class MorphismMethods: ...
