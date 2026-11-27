r"""Aut categories internal to ``Cat()``."""

from __future__ import annotations

from typing import final, override

from ..homsets import AutCategoryOf, UniversalAutElementMethods
from .endsets import CatEndCategory, _CatEndofunctorMethods


class _CatAutofunctorMethods(_CatEndofunctorMethods, UniversalAutElementMethods):
    @final
    def is_autofunctor(self) -> bool:
        r"""Return ``True`` because this element is an automorphism in ``Cat()``."""
        return True


class CatAutCategory(AutCategoryOf):
    r"""Autofunctor category of a category.

    Canonical chain: ``Cat().AutCategory()``.
    """

    _base_category_class_and_axiom = (CatEndCategory, "Autset")

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"autofunctor categories internal to {self.base_category()}"

    ElementMethods = _CatAutofunctorMethods

    class ParentMethods: ...
