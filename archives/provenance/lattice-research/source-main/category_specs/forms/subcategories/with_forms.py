r"""Modules equipped with forms."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction, UniversalHomElementMethods
from ...modules import Modules

if TYPE_CHECKING:
    from ...types import (
        FormedModule,
        FormedModuleElement,
        FormedModuleMorphism,
        OrthogonalGroup,
        RModuleMorphism,
    )


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

        @abstractmethod
        def is_bilinear(self) -> bool: ...

        @abstractmethod
        def is_quadratic(self) -> bool: ...

        @abstractmethod
        def form(self) -> RModuleMorphism: ...

        @final
        def orthogonal_group(self) -> OrthogonalGroup:
            r"""Return ``Aut_C(M)`` for this formed-module category ``C``."""
            return self.category().AutCategory().Of(self)

    class SubcategoryMethods:
        @final
        def Bilinear(self) -> Category:
            r"""Introduced here: select the bilinear-formed subcategory."""
            return self._with_axiom("Bilinear")
        @final
        def Quadratic(self) -> Category:
            r"""Introduced here: select the quadratic-formed subcategory."""
            return self._with_axiom("Quadratic")
        @final
        def Symmetric(self) -> Category:
            r"""Introduced here: select the symmetric-bilinear subcategory."""
            return self._with_axiom("Symmetric")
        @final
        def Alternating(self) -> Category:
            r"""Introduced here: select the alternating-bilinear subcategory."""
            return self._with_axiom("Alternating")
        @final
        def Nondegenerate(self) -> Category:
            r"""Introduced here: select the nondegenerate-bilinear subcategory."""
            return self._with_axiom("Nondegenerate")
        @final
        def Integral(self) -> Category:
            r"""Introduced here: select the integral-bilinear subcategory."""
            return self._with_axiom("Integral")
        @final
        def Rational(self) -> Category:
            r"""Introduced here: select the rational-bilinear subcategory."""
            return self._with_axiom("Rational")

    class ElementMethods: ...

    class HomCategory(HomCategoryConstruction):
        class ElementMethods(UniversalHomElementMethods):
            @abstractmethod
            def kernel(self) -> FormedModule:
                r"""Return ``ker(f)`` with the restricted form."""
                ...

            @abstractmethod
            def image(self) -> FormedModule:
                r"""Return ``im(f)`` with the restricted form."""
                ...

            @abstractmethod
            def inverse_image(self, subobject: FormedModule) -> FormedModule:
                r"""Return ``f^{-1}(subobject)`` with the restricted form."""
                ...

            @abstractmethod
            def cokernel(self) -> FormedModule:
                r"""Return ``codomain(f) / image(f)`` with descended form data.

                The underlying quotient is formed in the finitely generated
                module category.  The form codomain also descends: first take
                the coefficient-module cokernel of the form-codomain map, then
                quotient further by the image of cross terms
                ``b(image(f), codomain(f))``.  Bilinear or quadratic form data
                is attached exactly when this produces a well-defined form on
                the quotient object.
                """
                ...

            @abstractmethod
            def lift(self, x: FormedModuleElement) -> FormedModuleElement:
                r"""Return a lift along this morphism when one exists."""
                ...

            @abstractmethod
            def projection(self) -> FormedModuleMorphism:
                r"""Return the quotient projection associated to ``cokernel()``."""
                ...

            def is_isometry(self) -> bool:
                r"""Return whether this form-preserving morphism is an isomorphism."""
                return self.is_isomorphism()

    Bilinear = LazyImport(
        "category_specs.forms.subcategories.bilinear", "BilinearModulesCategory"
    )
    Quadratic = LazyImport(
        "category_specs.forms.subcategories.quadratic", "QuadraticModulesCategory"
    )


class OverPIDFormedModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Modules over a PID equipped with a form.

    Canonical chain: ``Modules(R).OverPID().WithForms()``.
    """

    from ...modules.subcategories.over_pid import _OverPID

    _base_category_class_and_axiom = (_OverPID, "WithForms")
    _defining_predicates = ("has_form",)

    ParentMethods = FormedModulesCategory.ParentMethods

    SubcategoryMethods = FormedModulesCategory.SubcategoryMethods

    ElementMethods = FormedModulesCategory.ElementMethods

    class HomCategory(HomCategoryConstruction):
        class ElementMethods(FormedModulesCategory.HomCategory.ElementMethods): ...

    Bilinear = LazyImport(
        "category_specs.forms.subcategories.bilinear", "OverPIDBilinearModulesCategory"
    )
    Quadratic = LazyImport(
        "category_specs.forms.subcategories.quadratic",
        "OverPIDQuadraticModulesCategory",
    )


FormedModulesObject = FormedModulesCategory.ParentMethods
FormedModulesElement = FormedModulesCategory.ElementMethods
FormedModulesMorphism = FormedModulesCategory.HomCategory.ElementMethods
OverPIDFormedModulesObject = OverPIDFormedModulesCategory.ParentMethods
OverPIDFormedModulesElement = OverPIDFormedModulesCategory.ElementMethods
OverPIDFormedModulesMorphism = OverPIDFormedModulesCategory.HomCategory.ElementMethods
