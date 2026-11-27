r"""Spec for the hom/morphism layer over ``Modules(R)``.

Defines:
    RModuleHomCategory         -- the category of R-module homs Hom_R(M, N)
    RModuleHomCategory.Forms   -- hom-layer interpretation of tensor-component
                                  duals as Hom_R(T_R(M)[p,q], S).
    Modules(R).EndCategory()   -- category whose objects are End_R(M)
    Modules(R).AutCategory()   -- category whose objects are Aut_R(M)

For a form-bearing module category ``C`` such as
``Modules(R).WithForms().Bilinear()``, the object ``C.AutCategory().Of(M)`` is the
orthogonal group of the formed module ``M``. This is categorical ownership, not a
generic Sage group wrapper.
"""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TypeVar, cast, final, override, TypeAlias

from sage.categories.magmatic_algebras import MagmaticAlgebras as SageMagmaticAlgebras
from sage.misc.lazy_import import LazyImport

from ..cat import Category, CategoryWithAxiom
from ..homsets import (
    GenericAutCategory,
    GenericEndCategory,
    HomCategoryOf,
    UniversalAutElementMethods,
    UniversalAutObjectMethods,
    UniversalEndElementMethods,
    UniversalEndObjectMethods,
    UniversalHomElementMethods,
    UniversalHomObjectMethods,
)
from ..types import Ring, RModMorphism, RModuleElement

if TYPE_CHECKING:
    from typing import Self

    from ..types import (
        BilinearForm,
        BilinearFormsModule,
        Cardinality,
        Integer,
        QuadraticForm,
        QuadraticFormsModule,
        QuotientModule,
        RingElement,
        RingMorphism,
        RModAut,
        RModule,
        SubModule,
    )

_F = TypeVar("_F", bound=Callable[..., object])


# ---------------------------------------------------------------------------
# Hom-level parent methods
# ---------------------------------------------------------------------------


class _RModHomCategoryObjectMethods(UniversalHomObjectMethods):
    @final
    def base_ring(self) -> Ring:
        r"""Return the scalar ring of this module Hom object."""
        domain: Any = self.domain()
        return cast(Ring, domain.base_ring())

    @abstractmethod
    def __call__(
        self,
        data: RModMorphism | Callable[[RModuleElement], RModuleElement],
    ) -> RModMorphism:
        r"""Coerce module-morphism data into this hom object."""
        ...

    @final
    def zero(self) -> RModMorphism:
        from sage.misc.constant_function import ConstantFunction

        codomain: Any = self.codomain()
        zero_function: Callable[[RModuleElement], RModuleElement] = ConstantFunction(cast(RModuleElement, codomain.zero()))
        return self(zero_function)

    @abstractmethod
    def natural_morphism(self) -> RModMorphism:
        r"""The morphism in Hom_R(M, N) sending e_i -> f_i for all
        generators e_i of M and f_i of N.  As a matrix this is ``[Id | 0]``
        or ``[Id | 0]^t``: rectangular with 1s along the diagonal.
        """
        ...


# ---------------------------------------------------------------------------
# Morphism (element) methods
# ---------------------------------------------------------------------------


class _RModMorphisms(UniversalHomElementMethods):
    r"""ElementMethods introduced by ``Modules(R).HomCategory()`` for R-linear maps."""

    # ``parent`` is a Sage ``Element`` intrinsic and is not restated here.

    @abstractmethod
    def kernel(self) -> SubModule: ...

    @abstractmethod
    def image(self, subobject: SubModule | None = None) -> SubModule:
        r"""Return ``im(f)`` or the direct image ``f(subobject)``."""
        ...

    @abstractmethod
    def direct_image(self, subobject: SubModule) -> SubModule:
        r"""Return the direct-image submodule ``f(subobject)``."""
        ...

    @abstractmethod
    def cokernel(self) -> QuotientModule: ...

    @abstractmethod
    def coimage(self) -> SubModule: ...

    @abstractmethod
    def inverse_image(self, subobject: SubModule) -> SubModule:
        r"""Return the inverse-image submodule ``f^{-1}(subobject)``."""
        ...

    @abstractmethod
    def restrict_domain(self, subobject: SubModule) -> RModMorphism:
        r"""Return the induced morphism from ``subobject`` to the codomain."""
        ...

    @abstractmethod
    def restrict_codomain(self, subobject: SubModule) -> RModMorphism:
        r"""Return the induced morphism into ``subobject`` when ``im(f) <= subobject``."""
        ...

    @abstractmethod
    def restrict(self, subobject: SubModule) -> RModMorphism:
        r"""Return the endomorphism of ``subobject`` induced by an invariant map."""
        ...

    @abstractmethod
    def is_injective(self) -> bool: ...

    @abstractmethod
    def is_surjective(self) -> bool: ...

    @abstractmethod
    def is_bijective(self) -> bool: ...

    @abstractmethod
    def inverse(self) -> RModMorphism:
        r"""Return the inverse morphism when this morphism is an isomorphism."""
        ...

    @abstractmethod
    def is_zero(self) -> bool:
        r"""Return whether this morphism is the zero morphism."""
        ...

    @abstractmethod
    def evaluate(self, m: RModuleElement) -> RModuleElement: ...

    @abstractmethod
    def index(self) -> Cardinality: ...

    @abstractmethod
    def direct_sum(self, f: Self) -> Self: ...

    @abstractmethod
    def tensor(self, f: Self) -> Self: ...

    @abstractmethod
    def base_change(self, morphism: RingMorphism) -> RModMorphism:
        r"""Return the scalar extension of this morphism along ``morphism``."""
        ...

    @abstractmethod
    def scale(self, r: RingElement) -> Self:
        r"""``(r*f)(m) := r * f(m) = f(r.m)``."""
        ...

    @abstractmethod
    def _mul_(self, data: RingElement | Self) -> Self:
        r"""Concrete impls dispatch on ``RingElement`` (-> ``scale``)
        vs another ``RModMorphism`` (-> ``tensor``).
        """
        ...

    @final
    def is_primitive(self) -> bool:
        r"""``f: M -> N`` is primitive iff coker(f) is torsionfree."""
        return bool(self.cokernel().is_torsionfree())

    @abstractmethod
    def lift(self, m: RModuleElement) -> RModuleElement:
        r"""Return any element ``m'`` such that ``f(m') = m``."""
        ...

    @abstractmethod
    def preimage_representative(self, m: RModuleElement) -> RModuleElement:
        r"""Return one representative of a preimage of ``m`` when it exists."""
        ...

    @abstractmethod
    def dual(self) -> Self:
        r"""Given f in Hom_R(A, B), return f^* in Hom_R(B^*, A^*) where
        f^*(\phi) := \phi \circ f.  (Also called the adjoint or transpose.)
        Satisfies ``<f(m), \phi>_{nat,N} = <m, f^*(\phi)>_{nat,M}``.
        """
        ...

    @final
    def saturation(self) -> Self:
        r"""Given f in Hom_R(A, B), find the inclusion ``g`` of im(f) into
        Sat_B(im(f)) and return ``h := g \circ f`` in Hom_R(A, B) so that
        im(h) is saturated.
        """
        im: Any = self.image()
        sat: Any = im.saturation()
        incl: Any = sat.inclusion()
        return cast(Self, incl.pre_compose(self))


# ---------------------------------------------------------------------------
# Endomorphism element methods
# ---------------------------------------------------------------------------


class _RModEndomorphisms(UniversalEndElementMethods):
    @abstractmethod
    def __pow__(self, n: Integer) -> Self: ...


# ---------------------------------------------------------------------------
# Automorphism element methods
# ---------------------------------------------------------------------------


class _RModAutomorphisms(UniversalAutElementMethods):
    r"""Module-specific automorphism methods; generic aut-category methods are
    inherited.
    """


# ---------------------------------------------------------------------------
# RModuleHomCategory: the hom category proper
# ---------------------------------------------------------------------------


class RModuleHomCategory(HomCategoryOf):
    r"""The category of R-module homs ``Hom_R(M, N)``.

    Canonical chain: ``Modules(R).HomCategory()``.

    Objects are hom parents; elements are R-module morphisms.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""``Hom_R(M, N)`` is again an R-module for any M, N."""
        return [HomCategoryOf(self.base_category()), self.base_category()]

    class SubcategoryMethods:
        @final
        def Forms(self) -> Category:
            self_any: Any = self
            return cast(Category, self_any._with_axiom("Forms"))

    ParentMethods : TypeAlias = _RModHomCategoryObjectMethods
    ElementMethods : TypeAlias = _RModMorphisms

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "RModuleEndCategory")
    Forms = LazyImport(__name__, "_Forms")


# ---------------------------------------------------------------------------
# Forms axiom subcategories
# ---------------------------------------------------------------------------


class _Forms(CategoryWithAxiom):
    r"""R-modules of the form ``Hom_R(T_R(M)[p,q], S)`` where ``T_R(M)[p,q]``

    Canonical chain: ``Modules(R).HomCategory().Forms()``.
    is the standard tensor-type ``(p,q)`` component and ``S`` is an R-submodule
    of ``K := Frac(R)``.

    The owning category for integral forms is
    ``TensorAlgebraComponents(R).DualObjects()``.  This hom category records the
    evaluation interpretation of those dual tensor components.
    """

    _base_category_class_and_axiom = (RModuleHomCategory, "Forms")

    class ParentMethods:
        @abstractmethod
        def is_integral(self) -> bool: ...

        @abstractmethod
        def is_rational(self) -> bool:
            r"""True if it takes a non-integral value."""
            ...

    class SubcategoryMethods:
        @final
        def Rational(self) -> Category:
            r"""Forms with target ``S = K`` in ``Hom_R(T_R(M)[p,q], S)``."""
            self_any: Any = self
            return cast(Category, self_any._with_axiom("Rational"))

        @final
        def Integral(self) -> Category:
            r"""Forms with target ``S = R`` in ``Hom_R(T_R(M)[p,q], S)``."""
            self_any: Any = self
            return cast(Category, self_any._with_axiom("Integral"))

        @final
        def Linear(self) -> Category:
            r"""Linear forms: domain ``T_R(M)[1,0]=M``, represented type ``(0,1)``."""
            self_any: Any = self
            return cast(Category, self_any._with_axiom("Linear"))

        @final
        def Bilinear(self) -> Category:
            r"""Bilinear forms: domain ``T_R(M)[2,0]``, represented type ``(0,2)``."""
            self_any: Any = self
            return cast(Category, self_any._with_axiom("Bilinear"))

        @final
        def Quadratic(self) -> Category:
            r"""Quadratic forms on ``M``."""
            self_any: Any = self
            return cast(Category, self_any._with_axiom("Quadratic"))

        @final
        def NonDegenerate(self) -> Category:
            r"""Forms with trivial kernels."""
            self_any: Any = self
            return cast(Category, self_any._with_axiom("NonDegenerate"))

        @final
        def Symmetric(self) -> Category:
            r"""Symmetric forms: represented type ``(0,n)``."""
            self_any: Any = self
            return cast(Category, self_any._with_axiom("Symmetric"))

        @final
        def Alternating(self) -> Category:
            r"""Alternating forms: represented type ``(0,n)``."""
            self_any: Any = self
            return cast(Category, self_any._with_axiom("Alternating"))

    Bilinear = LazyImport(__name__, "_Bilinear")
    Quadratic = LazyImport(__name__, "_Quadratic")

    class ElementMethods: ...


class _Bilinear(CategoryWithAxiom):
    r"""Canonical chain: ``Modules(R).HomCategory().Forms().Bilinear()``."""

    _base_category_class_and_axiom = (_Forms, "Bilinear")

    class ParentMethods:
        @abstractmethod
        def associated_quadratic_forms(self) -> QuadraticFormsModule: ...

    class ElementMethods:
        @abstractmethod
        def evaluate(self, m: RModuleElement) -> RModuleElement: ...

        @abstractmethod
        def associated_quadratic_form(self) -> QuadraticForm: ...

        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            v_any: Any = v
            return self.evaluate(v_any.tensor(w))


class _Quadratic(CategoryWithAxiom):
    r"""Canonical chain: ``Modules(R).HomCategory().Forms().Quadratic()``."""

    _base_category_class_and_axiom = (_Forms, "Quadratic")

    class ParentMethods:
        @abstractmethod
        def associated_bilinear_forms(self) -> BilinearFormsModule: ...

    class ElementMethods:
        @abstractmethod
        def evaluate(self, m: RModuleElement) -> RModuleElement: ...

        @abstractmethod
        def associated_bilinear_form(self) -> BilinearForm: ...

        @final
        def q(self, v: RModuleElement) -> RModuleElement:
            return self.evaluate(v)


# ---------------------------------------------------------------------------
# End and aut subcategories
# ---------------------------------------------------------------------------


class _RModEndObjectMethods(_RModHomCategoryObjectMethods, UniversalEndObjectMethods):
    r"""Module End parent methods; ``End_R(M)`` is ``Hom_R(M, M)``."""

    @abstractmethod
    def base_module(self) -> RModule:
        r"""If this is End_R(M), return M."""
        ...

    @abstractmethod
    def unit_group(self) -> RModAut: ...

    # Do not define ``as_automorphism`` -- promotion of invertible
    # objects should happen automatically.


class _RModAutObjectMethods(_RModEndObjectMethods, UniversalAutObjectMethods):
    r"""Module-specific aut parent methods; generic aut methods are inherited."""


class RModuleEndCategory(GenericEndCategory):
    r"""Canonical chain: ``Modules(R).EndCategory()``."""

    _base_category_class_and_axiom = (RModuleHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "RModuleAutCategory")

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""End_R(M) is an R-algebra."""
        from ..algebras import Algebras
        from . import Modules

        R = self.base_category().base_category().base_ring()
        return [
            *super().extra_super_categories(),
            Algebras(R),
            SageMagmaticAlgebras(R),
            Modules(R),
        ]

    ParentMethods : TypeAlias = _RModEndObjectMethods
    ElementMethods : TypeAlias = _RModEndomorphisms


class RModuleAutCategory(GenericAutCategory):
    r"""Category of module automorphism groups.

    Canonical chain: ``Modules(R).AutCategory()``.

    When the base category is a category of modules with forms, objects of this
    aut category are orthogonal groups: automorphisms of the underlying module
    that preserve the form because they are automorphisms in that formed-module
    category.
    """

    _base_category_class_and_axiom = (RModuleEndCategory, "Autset")

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Aut_R(M) := End_R(M)^* is the group of units of End_R(M)."""
        return super().extra_super_categories()

    ParentMethods : TypeAlias = _RModAutObjectMethods
    ElementMethods : TypeAlias = _RModAutomorphisms
