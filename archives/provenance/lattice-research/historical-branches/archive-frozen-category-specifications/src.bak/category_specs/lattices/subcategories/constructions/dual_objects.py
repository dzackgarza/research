r"""Dual-object construction category for lattices."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, TypeAlias

from ....cat import DualObjectsCategory
from ...homsets import LatticeHomCategory

if TYPE_CHECKING:
    from ... import LatticesCategory


class LatticeDualObjectsCategory(DualObjectsCategory):
    r"""Hom-dual lattice objects with evaluation-bearing elements.

    Canonical chain: ``Lattices(R).DualObjects()``.

    This construction is reserved for category-theoretic dual objects: parents
    represented as ``Hom_R(N, R)`` for some object ``N`` and therefore carrying
    hom-object and evaluation behavior.  The metric-dual lattice
    ``L^\# = {v in L_K | b(v, L) subset R}`` is constructed by
    ``dual_lattice()`` or the lattice-specific metric-dual construction surface.

    Diagnostics: when the global category diagnostic flag is enabled, implementations
    should emit a category diagnostic if a compatibility path or adjacent Sage spelling
    could make this Hom-dual construction look like the metric-dual construction.
    """

    @final
    def extra_super_categories(self) -> list[LatticesCategory]:
        return [self.base_category().Rational()]

    class ParentMethods: ...

    class ElementMethods: ...



LatticeDualObjectsObject : TypeAlias = LatticeDualObjectsCategory.ParentMethods
LatticeDualObjectsElement : TypeAlias = LatticeDualObjectsCategory.ElementMethods
LatticeDualObjectsMorphism : TypeAlias = LatticeHomCategory.ElementMethods
