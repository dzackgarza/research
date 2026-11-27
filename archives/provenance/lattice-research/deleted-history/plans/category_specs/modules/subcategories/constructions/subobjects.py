r"""Submodules."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Cardinality, QuotientModule, RModMorphism, RModule, RModuleElement, SubModule


class _Subobjects(SubobjectsCategory):
    r"""Submodule category.

    Canonical chain: ``Modules(R).Subobjects()``.
    """

    @abstract_method
    def as_subobject_of_self(self, M: RModule) -> SubModule:
        r"""Regard M as a submodule of itself via the identity."""
        ...

    class ParentMethods:
        @abstract_method
        def ambient_module(self) -> RModule:
            r"""The ambient R-module of which ``self`` is a submodule."""
            ...

        @final
        def ambient(self) -> RModule:
            r"""Return the ambient module of this submodule."""
            return self.ambient_module()

        @final
        def ambient_vector_space(self) -> RModule:
            r"""Return the ambient vector space when the base category is over a field."""
            return self.ambient_module()

        @abstract_method
        def inclusion(self) -> RModMorphism: ...

        @abstract_method
        def intersect(self, N: SubModule) -> SubModule: ...

        @final
        def __and__(self, N: SubModule) -> SubModule:
            return self.intersect(N)

        @final
        def index(self) -> Cardinality:
            return self.inclusion().index()

        @final
        def is_primitive(self) -> bool:
            return self.inclusion().is_primitive()

        @final
        def lift(self, m: RModuleElement) -> RModuleElement:
            return self.inclusion()(m)

        @abstract_method
        def saturation(self) -> SubModule: ...

        @abstract_method
        def complement(self) -> RModule: ...

        @abstract_method
        def is_subspace(self, other: RModule) -> bool: ...

        @abstract_method
        def __le__(self, other: RModule) -> bool: ...

        @override
        @final
        def quotient_module(self) -> QuotientModule:
            return self.inclusion().cokernel()

    class ElementMethods: ...
    class MorphismMethods: ...
