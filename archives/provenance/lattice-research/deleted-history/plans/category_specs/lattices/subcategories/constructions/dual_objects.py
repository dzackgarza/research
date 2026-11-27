r"""Dual-object construction category for lattices."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import DualObjectsCategory

if TYPE_CHECKING:
    from ....types import DiscriminantGroupElement, Lattice, LatticeMorphism


class LatticeDualObjectsCategory(DualObjectsCategory):
    r"""Dual lattices ``L^* = {v in L_K | b(v, L) subset R}``.

    Canonical chain: ``Lattices(R).DualObjects()``.
    """

    @final
    def extra_super_categories(self):
        return [self.base_category().Rational()]

    class ParentMethods:
        @abstract_method
        def primal_lattice(self) -> Lattice: ...

        @abstract_method
        def inclusion_morphism(self) -> LatticeMorphism: ...

    class ElementMethods:
        @abstract_method
        def discriminant_class(self) -> DiscriminantGroupElement:
            r"""Return the image of this dual-lattice element in ``L^*/L``."""
            ...
    class MorphismMethods: ...


LatticeDualObjectsObject = LatticeDualObjectsCategory.ParentMethods
LatticeDualObjectsElement = LatticeDualObjectsCategory.ElementMethods
LatticeDualObjectsMorphism = LatticeDualObjectsCategory.MorphismMethods
