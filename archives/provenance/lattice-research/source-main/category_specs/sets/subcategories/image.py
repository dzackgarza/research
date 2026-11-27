r"""One-object subcategories for images of sets under maps."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.sets.image_set import ImageSubobject as SageImageSubobject

if TYPE_CHECKING:
    from ...types import Cardinality, Set, SetElement, SympySet


from ...cat import Category
from .. import Sets


class ImageSubobject(SageImageSubobject):
    r"""Project wrapper for Sage image subobjects."""

    @override
    @final
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ImageSubobject):
            return NotImplemented
        return list(self) == list(other)

    @override
    @final
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, ImageSubobject):
            return NotImplemented
        return not self.__eq__(other)

    @override
    @final
    def __hash__(self) -> int:
        return hash(tuple(self))

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        domain_subset = getattr(self, "_domain_subset", None)
        if domain_subset is not None and domain_subset.is_finite():
            return any(y == x for y in self)
        try:
            self._element_constructor_(x)
        except (ValueError, TypeError):
            return False
        return True


class _ImageSets(Category_singleton):
    r"""Image subobjects ``{f(x) | x in X}`` under a set map.

    Constructor target:
    ``Sets().Constructors().ImageSubobject(f, domain_subset)`` refines here as
    a constructive set subobject/subquotient.  The ambient set is the codomain
    of ``f``; ``lift`` and ``retract`` express the Sage-backed subquotient
    representation of the image inside that ambient.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().Subobjects(), Sets().Subquotients()]

    class ParentMethods:
        @abstractmethod
        def __eq__(self, other: object) -> bool: ...

        @abstractmethod
        def __ne__(self, other: object) -> bool: ...

        @abstractmethod
        def __hash__(self) -> int: ...

        @override
        @abstractmethod
        def _element_constructor_(self, x: SetElement) -> SetElement: ...

        @override
        @abstractmethod
        def ambient(self) -> Set:
            r"""Return the codomain ambient set containing this image."""
            ...

        @override
        @abstractmethod
        def lift(self, x: SetElement) -> SetElement:
            r"""Lift an image element into ``ambient()``."""
            ...

        @override
        @abstractmethod
        def retract(self, x: SetElement) -> SetElement:
            r"""Retract an ambient element to this image when defined."""
            ...

        @override
        @abstractmethod
        def cardinality(self) -> Cardinality: ...

        @override
        @abstractmethod
        def __iter__(self) -> Iterator[SetElement]: ...

        @override
        @abstractmethod
        def __contains__(self, x: Any) -> bool: ...

        @override
        @abstractmethod
        def _an_element_(self) -> SetElement: ...

        @override
        @abstractmethod
        def _sympy_(self) -> SympySet: ...

    class ElementMethods: ...
