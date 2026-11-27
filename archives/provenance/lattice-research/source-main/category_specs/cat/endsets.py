r"""End categories internal to ``Cat()``."""

from __future__ import annotations

from typing import ClassVar, final, override

from sage.misc.lazy_import import LazyImport

from ..homsets import EndCategoryOf, HomCategoryOf, UniversalEndElementMethods
from .homsets import CatHomCategory, _CatFunctorMethods


class _CatEndofunctorMethods(_CatFunctorMethods, UniversalEndElementMethods):
    @final
    def is_endofunctor(self) -> bool:
        r"""Return whether this Cat morphism is an endofunctor."""
        return bool(self.domain() == self.codomain())


class CatEndCategory(EndCategoryOf):
    r"""Endofunctor category of a category.

    Canonical chain: ``Cat().EndCategory()``.
    """

    _base_category_class_and_axiom: ClassVar[tuple[type[HomCategoryOf], str]] = (
        CatHomCategory,
        "Endset",
    )

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"endofunctor categories internal to {self.base_category()}"

    ElementMethods = _CatEndofunctorMethods

    class ParentMethods: ...


    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport("category_specs.cat.autsets", "CatAutCategory")
