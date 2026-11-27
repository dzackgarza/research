r"""Subquotient construction category for lattices."""

from __future__ import annotations

from abc import abstractmethod

from ....cat import SubquotientsCategory


class _Subquotients(SubquotientsCategory):
    r"""Lattice objects obtained as subobjects of quotients or quotients of subobjects.

    Canonical chain: ``Lattices(R).Subquotients()``.
    """

    class ParentMethods:
        @abstractmethod
        def cover_object(self) -> object:
            """Return the cover object K in a subquotient K/H."""
            ...

        @abstractmethod
        def relation_object(self) -> object:
            """Return the relation object H in a subquotient K/H."""
            ...

        @abstractmethod
        def projection(self) -> object:
            """Return the projection to the subquotient."""
            ...

        @abstractmethod
        def lift(self, x: object) -> object:
            """Lift a subquotient element to the cover when possible."""
            ...

        @abstractmethod
        def restricted_form(self) -> object:
            """Return the form restricted to the cover object."""
            ...

        @abstractmethod
        def orthogonal_complement(self) -> object:
            """Return the orthogonal complement relevant to this subquotient."""
            ...

        @abstractmethod
        def orthogonal_quotient(self) -> object:
            """Return the canonical gluing quotient H^perp/H when this is a form subquotient."""
            ...

        @abstractmethod
        def subquotient_form(self) -> object:
            """Return the induced form on this subquotient when defined."""
            ...

    class ElementMethods: ...
