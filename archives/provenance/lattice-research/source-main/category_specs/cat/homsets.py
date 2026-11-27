r"""Hom categories internal to ``Cat()``.

Morphisms in ``Cat()`` are functors between categories.  Sage already has a
substantial functor and construction-functor implementation; this file only
declares the category-spec surface that will wrap that machinery.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, final, override

from sage.categories.functor import Functor
from sage.categories.pushout import ConstructionFunctor
from sage.misc.lazy_import import LazyImport

from ..homsets import (
    HomCategoryOf,
    UniversalHomElementMethods,
    UniversalHomObjectMethods,
)
from .base_category_types import Category


class _CatHomCategoryObjectMethods(UniversalHomObjectMethods):
    @abstractmethod
    def __call__(self, functor: Functor) -> Functor:
        r"""Coerce a Sage functor into this ``Cat()`` hom object."""
        del functor
        ...

    @abstractmethod
    def __contains__(self, functor: Any) -> bool:
        r"""Return whether ``functor`` is an element of this functor hom object."""
        ...


class _CatFunctorMethods(UniversalHomElementMethods):
    @abstractmethod
    def __call__(self, category: Category) -> Category:
        r"""Evaluate this functor on an object of its domain category."""
        ...

    @abstractmethod
    def _coerce_into_domain(self, category: Category) -> Category: ...

    @abstractmethod
    def _apply_functor(self, category: Category) -> Category: ...

    @abstractmethod
    def _apply_functor_to_morphism(self, functor: Functor) -> Functor:
        ...


class _CatConstructionFunctorMethods(_CatFunctorMethods):
    r"""Sage ``ConstructionFunctor`` surface for actual functors.

    These methods come from ``sage.categories.pushout.ConstructionFunctor``.
    They are not methods on Sage ``FunctorialConstructionCategory`` objects
    such as ``C.Subobjects()``; those are category objects, not callable
    functors between category objects.
    """

    coercion_reversed: bool = False

    @abstractmethod
    def pushout(self, other: ConstructionFunctor) -> ConstructionFunctor:
        r"""Return the pushout construction functor with ``other`` in ``Cat()``."""
        ...

    @abstractmethod
    def merge(self, other: ConstructionFunctor) -> ConstructionFunctor | None:
        r"""Return the merged construction functor with ``other`` in ``Cat()``."""
        ...

    @abstractmethod
    def commutes(self, other: ConstructionFunctor) -> bool:
        r"""Return whether this construction functor commutes with ``other``."""
        ...

    @abstractmethod
    def expand(self) -> list[ConstructionFunctor]:
        r"""Return the component construction functors represented by this functor."""
        ...

    @abstractmethod
    def common_base(
        self,
        other_functor: ConstructionFunctor,
        self_bases: tuple[Category, ...],
        other_bases: tuple[Category, ...],
    ) -> Category:
        r"""Return the common base data for this construction and
        ``other_functor``.
        """
        ...


class CatHomCategory(HomCategoryOf):
    r"""Hom category of functors between categories.

    Canonical chain: ``Cat().HomCategory()``.
    """

    @final
    def __init__(self, base_category: Category) -> None:
        super().__init__(base_category)

    @override
    @classmethod
    @final
    def category_of(cls, base_category: Category) -> CatHomCategory:
        r"""Return the functor hom category internal to ``base_category``."""
        return cls(base_category)

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"functor hom categories internal to {self.base_category()}"

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Return Sage's supercategories refined by Cat functor semantics."""
        return [HomCategoryOf(self.base_category())]

    ParentMethods = _CatHomCategoryObjectMethods
    ElementMethods = _CatFunctorMethods


    ConstructionFunctorMethods = _CatConstructionFunctorMethods
    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport("category_specs.cat.endsets", "CatEndCategory")
