r"""Lattices over principal ideal domains."""

from __future__ import annotations

from abc import abstractmethod
from typing import final

from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from .over_dedekind import _LatticesOverDedekindDomain


class _LatticesOverPID(CategoryWithAxiom_over_base_ring):
    r"""Lattices whose base ring is a principal ideal domain.

    Canonical chain: ``Lattices(R).OverDedekindDomain().OverPID()``.
    """

    _base_category_class_and_axiom = (_LatticesOverDedekindDomain, "OverPID")
    _defining_predicates = ("is_over_pid",)
    OverIntegers = LazyImport(
        "category_specs.lattices.subcategories.over_integers", "_LatticesOverIntegers"
    )

    class ParentMethods:
        @final
        def is_over_pid(self) -> bool:
            return True

        @abstractmethod
        def is_over_integers(self) -> bool: ...

    class ElementMethods: ...
