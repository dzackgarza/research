r"""Subobject construction category for lattices."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Cardinality, Lattice, LatticeElement, LatticeMorphism


class _Subobjects(SubobjectsCategory):
    r"""Sublattices with the restricted bilinear form.

    Canonical chain: ``Lattices(R).Subobjects()``.
    """

    @abstract_method
    def as_subobject_of_self(self, L: Lattice) -> Lattice:
        r"""Regard ``L`` as a sublattice of itself via the identity."""
        ...

    class ParentMethods:
        @abstract_method
        def ambient_lattice(self) -> Lattice: ...

        @abstract_method
        def inclusion(self) -> LatticeMorphism: ...

        @abstract_method
        def intersect(self, M: Lattice) -> Lattice: ...

        @final
        def __and__(self, M: Lattice) -> Lattice:
            return self.intersect(M)

        @final
        def index(self) -> Cardinality:
            return self.inclusion().index()

        @final
        def lift(self, v: LatticeElement) -> LatticeElement:
            return self.inclusion()(v)

        @abstract_method
        def saturation(self) -> Lattice: ...

        @abstract_method
        def orthogonal_complement(self) -> Lattice: ...

    class ElementMethods: ...
    class MorphismMethods: ...
