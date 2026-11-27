r"""Submodules."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, cast, final

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import (
        Cardinality,
        QuotientModule,
        RModMorphism,
        RModule,
        SubModule,
    )


class _Subobjects(SubobjectsCategory):
    r"""Submodule category.

    Canonical chain: ``Modules(R).Subobjects()``.
    """

    @abstractmethod
    def as_subobject_of_self(self, M: RModule) -> SubModule:
        r"""Regard M as a submodule of itself via the identity."""
        ...

    class ParentMethods:
        @abstractmethod
        def ambient_module(self) -> RModule:
            r"""The ambient R-module of which ``self`` is a submodule."""
            ...

        @final
        def ambient(self) -> RModule:
            r"""Return the ambient module of this submodule."""
            return self.ambient_module()

        @final
        def ambient_vector_space(self) -> RModule:
            r"""Return the ambient vector space when the base category is over a
            field.
            """
            return self.ambient_module()

        @abstractmethod
        def inclusion(self) -> RModMorphism: ...

        @abstractmethod
        def intersect(self, N: SubModule) -> SubModule: ...

        @final
        def __and__(self, N: SubModule) -> SubModule:
            return self.intersect(N)

        @final
        def index(self) -> Cardinality:
            return cast(Cardinality, getattr(self.inclusion(), "index")())

        @final
        def is_primitive(self) -> bool:
            return bool(getattr(self.inclusion(), "is_primitive")())

        @abstractmethod
        def saturation(self) -> SubModule: ...

        @abstractmethod
        def complement(self) -> RModule: ...

        @abstractmethod
        def is_subspace(self, other: RModule) -> bool: ...

        @final
        def is_submodule_of(self, other: RModule | None = None) -> bool:
            r"""Return whether this submodule is contained in ``other`` or its
            ambient.
            """
            return bool(self <= (self.ambient_module() if other is None else other))

        @abstractmethod
        def __le__(self, other: RModule) -> bool: ...

        @final
        def quotient_module(self) -> QuotientModule:
            return cast(QuotientModule, getattr(self.inclusion(), "cokernel")())

    class ElementMethods: ...
