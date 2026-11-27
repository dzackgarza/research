r"""Subobject construction category for lattices."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Lattice, LatticeMorphism, RingElement


class _Subobjects(SubobjectsCategory):
    r"""Sublattices with the restricted bilinear form.

    Canonical chain: ``Lattices(R).Subobjects()``.
    """

    @abstractmethod
    def as_subobject_of_self(self, L: Lattice) -> Lattice:
        r"""Regard ``L`` as a sublattice of itself via the identity."""
        ...

    class ParentMethods:
        @abstractmethod
        def ambient(self) -> Lattice: ...

        @abstractmethod
        def inclusion(self) -> LatticeMorphism: ...

        @abstractmethod
        def intersect(self, M: Lattice) -> Lattice: ...

        @final
        def __and__(self, M: Lattice) -> Lattice:
            return self.intersect(M)

        @abstractmethod
        def saturation(self) -> Lattice: ...

        @abstractmethod
        def is_primitive(self) -> bool:
            r"""Return whether the ambient quotient by this sublattice is torsionfree."""
            ...

        @abstractmethod
        def orthogonal_complement(self) -> Lattice: ...

        @abstractmethod
        def sum(self, other: Lattice) -> Lattice:
            """Return the lattice sum in the common ambient object."""
            ...

        @abstractmethod
        def primitive_closure(self, *, in_ambient: Lattice | None = None) -> Lattice:
            """Return the primitive closure inside the chosen ambient integral lattice."""
            ...

        @abstractmethod
        def integral_saturation(self) -> Lattice:
            """Return Sage's module saturation after clearing denominators."""
            ...

        @abstractmethod
        def index_in(self, other: Lattice) -> RingElement:
            """Return the finite index in ``other`` when comparable."""
            ...

        @abstractmethod
        def relative_index(self, other: Lattice) -> RingElement:
            """Return the relative lattice index against ``other``."""
            ...

        @abstractmethod
        def denominator(self) -> RingElement:
            """Return the fractional denominator of this lattice subobject."""
            ...

        @abstractmethod
        def clear_denominators(self) -> Lattice:
            """Return an integral lattice obtained from this fractional subobject."""
            ...
    class ElementMethods: ...
