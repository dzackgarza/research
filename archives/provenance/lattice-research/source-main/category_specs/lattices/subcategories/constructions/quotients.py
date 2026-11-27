r"""Quotient construction category for lattices."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ....cat import QuotientsCategory

if TYPE_CHECKING:
    from ....types import Lattice, LatticeElement, LatticeMorphism, RingElement


class _Quotients(QuotientsCategory):
    r"""Lattice quotients for quotient objects that remain in the lattice category.

    Canonical chain: ``Lattices(R).Quotients()``.
    """

    class ParentMethods:
        @abstractmethod
        def projection(self) -> LatticeMorphism: ...

        @abstractmethod
        def lift(self, x: _Quotients.ElementMethods) -> LatticeElement: ...

        @abstractmethod
        def cover_lattice(self) -> Lattice:
            """Return the covering lattice in the quotient presentation."""
            ...

        @abstractmethod
        def relation_lattice(self) -> Lattice:
            """Return the relation lattice in the quotient presentation."""
            ...

        @final
        def cover(self) -> Lattice:
            """Return the covering lattice in quotient notation."""
            return self.cover_lattice()

        @final
        def relations(self) -> Lattice:
            """Return the relation lattice in quotient notation."""
            return self.relation_lattice()

        @abstractmethod
        def quotient_map(self) -> LatticeMorphism:
            """Return the lattice quotient map."""
            ...

        @abstractmethod
        def finite_quotient(self) -> object:
            """Return the finite abelian quotient when the quotient is finite."""
            ...

        @abstractmethod
        def form_descends(self) -> bool:
            """Return whether the lattice form is well-defined on quotient classes."""
            ...

        @abstractmethod
        def b(self, x: object, y: object) -> RingElement:
            """Evaluate the induced finite bilinear form on quotient classes."""
            ...

        @abstractmethod
        def q(self, x: object) -> RingElement:
            """Evaluate the induced finite quadratic refinement on quotient classes."""
            ...

        @abstractmethod
        def discriminant_form_when_descends(self) -> object:
            """Return the induced finite bilinear or quadratic form when the form descends."""
            ...
    class ElementMethods:
        @abstractmethod
        def parent(self) -> _Quotients.ParentMethods: ...

        @final
        def lift(self) -> LatticeElement:
            return self.parent().lift(self)
