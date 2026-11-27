r"""Torsion-free modules."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Ideal


class _Torsionfree(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).Torsionfree()``."""

    _base_category_class_and_axiom = (Modules, "Torsionfree")

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_torsionfree()

    class ParentMethods:
        @override
        @final
        def is_torsionfree(self) -> bool:
            return True

        @override
        @final
        def annihilator(self) -> Ideal:
            r"""Return ``Ann_R(M) = (0)``."""
            R = self.base_ring()
            zero_ideal: Ideal = R.ideal(R.zero())
            return zero_ideal

    class ElementMethods: ...
