r"""Lattices over the integer ring."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ...cat import CategoryWithAxiom_over_base_ring
from .over_pid import _LatticesOverPID

if TYPE_CHECKING:
    from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring


class _LatticesOverIntegers(CategoryWithAxiom_over_base_ring):
    r"""Integral lattices over ``ZZ``.

    Canonical chain: ``Lattices(R).OverDedekindDomain().OverPID().OverIntegers()``.
    """

    _base_category_class_and_axiom = (_LatticesOverPID, "OverIntegers")
    _defining_predicates = ("is_over_integers",)

    class ParentMethods:
        @final
        def is_over_integers(self) -> bool:
            return True

        @abstractmethod
        def genus(self) -> GenusSymbol_global_ring: ...

    class ElementMethods: ...
