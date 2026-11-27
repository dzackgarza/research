r"""Modules equipped with forms."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from ...modules import Modules

if TYPE_CHECKING:
    from ...types import OrthogonalGroup, RModuleMorphism


class FormedModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Non-full category of pairs ``(M, f)`` with a form on ``M``.

    Canonical chain: ``Modules(R).WithForms()``.
    """

    _base_category_class_and_axiom = (Modules, "WithForms")
    _defining_predicates = ("has_form",)

    class ParentMethods:
        @override
        @final
        def has_form(self) -> bool:
            return True

        @abstract_method
        def is_bilinear(self) -> bool: ...

        @abstract_method
        def is_quadratic(self) -> bool: ...

        @abstract_method
        def form(self) -> RModuleMorphism: ...

        @final
        def orthogonal_group(self) -> OrthogonalGroup:
            r"""Return ``Aut_C(M)`` for this formed-module category ``C``."""
            return self.category().AutCategory().Of(self)

    class SubcategoryMethods:
        @cached_method
        @final
        def Bilinear(self) -> Category:
            r"""Introduced here: select the bilinear-formed subcategory."""
            return self._with_axiom("Bilinear")

        @cached_method
        @final
        def Quadratic(self) -> Category:
            r"""Introduced here: select the quadratic-formed subcategory."""
            return self._with_axiom("Quadratic")

        @cached_method
        @final
        def Symmetric(self) -> Category:
            r"""Introduced here: select the symmetric-bilinear subcategory."""
            return self._with_axiom("Symmetric")

        @cached_method
        @final
        def Alternating(self) -> Category:
            r"""Introduced here: select the alternating-bilinear subcategory."""
            return self._with_axiom("Alternating")

        @cached_method
        @final
        def Nondegenerate(self) -> Category:
            r"""Introduced here: select the nondegenerate-bilinear subcategory."""
            return self._with_axiom("Nondegenerate")

        @cached_method
        @final
        def Integral(self) -> Category:
            r"""Introduced here: select the integral-bilinear subcategory."""
            return self._with_axiom("Integral")

        @cached_method
        @final
        def Rational(self) -> Category:
            r"""Introduced here: select the rational-bilinear subcategory."""
            return self._with_axiom("Rational")

    class ElementMethods: ...
    class MorphismMethods: ...

    Bilinear = LazyImport("category_specs.forms.subcategories.bilinear", "BilinearModulesCategory")
    Quadratic = LazyImport("category_specs.forms.subcategories.quadratic", "QuadraticModulesCategory")


FormedModulesObject = FormedModulesCategory.ParentMethods
FormedModulesElement = FormedModulesCategory.ElementMethods
FormedModulesMorphism = FormedModulesCategory.MorphismMethods
