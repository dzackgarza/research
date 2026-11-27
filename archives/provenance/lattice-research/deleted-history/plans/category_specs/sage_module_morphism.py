r"""Spec for the homset/morphism layer over ``Modules(R)``.

Defines:
    RModuleHomsets             -- the category of R-module homsets Hom_R(M, N)
    RModuleHomsets.Forms       -- forms Hom_R(T_R(M)[p,q], S) (linear,
                                  bilinear, quadratic, symmetric, ...)
    RModuleHomsets.Endset      -- End_R(M) as an R-algebra
    RModuleHomsets.Endset.Autset
                               -- Aut_R(M) as the group of units of End_R(M)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.groups import Groups
from sage.categories.homsets import HomsetsCategory
from sage.categories.magmatic_algebras import MagmaticAlgebras
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    from typing import Self

    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer

    Cardinality = Integer | InfinityElement
    RingElement = Any
    RModule = Any
    RModuleElement = Any
    RModuleMorphism = Any
    RModHomset = Any
    SubModule = Any
    QuotientModule = Any
    BilinearForm = Any
    BilinearFormsModule = Any
    QuadraticForm = Any
    QuadraticFormsModule = Any
    RModAutSet = Any
    RModuleEndomorphism = Any
    RModuleHomsetElement = Any


# ---------------------------------------------------------------------------
# Forms-axiom helpers (wired into RModuleHomsets.Forms below)
# ---------------------------------------------------------------------------

class _Bilinear(CategoryWithAxiom_over_base_ring):
    class ParentMethods:
        @abstract_method
        def associated_quadratic_forms(self) -> QuadraticFormsModule: ...

    class ElementMethods:
        @abstract_method
        def associated_quadratic_form(self) -> QuadraticForm: ...

        def b(
            self, v: RModuleElement, w: RModuleElement
        ) -> RModuleElement:
            return self.evaluate(v.tensor(w))


class _Quadratic(CategoryWithAxiom_over_base_ring):
    class ParentMethods:
        @abstract_method
        def associated_bilinear_forms(self) -> BilinearFormsModule: ...

    class ElementMethods:
        @abstract_method
        def associated_bilinear_form(self) -> BilinearForm: ...

        def q(self, v: RModuleElement) -> RModuleElement:
            return self.evaluate(v)


# ---------------------------------------------------------------------------
# Homset-level (parent) methods
# ---------------------------------------------------------------------------

class _RModHomsetObjects:
    @abstract_method
    def domain(self) -> RModule: ...

    @abstract_method
    def codomain(self) -> RModule: ...

    @abstract_method
    def __call__(self, *args, **kwds) -> RModuleMorphism: ...

    @abstract_method
    def __contains__(self, obj: Any) -> bool: ...

    @cached_method
    def zero(self):
        from sage.misc.constant_function import ConstantFunction
        return self(ConstantFunction(self.codomain().zero()))

    @abstract_method
    def natural_morphism(self) -> RModuleHomsetElement:
        r"""The morphism in Hom_R(M, N) sending e_i -> f_i for all
        generators e_i of M and f_i of N.  As a matrix this is ``[Id | 0]``
        or ``[Id | 0]^t``: rectangular with 1s along the diagonal.
        """
        ...


# ---------------------------------------------------------------------------
# Morphism (element) methods
# ---------------------------------------------------------------------------

class _RModMorphisms:
    # ``parent`` is a Sage ``Element`` intrinsic and is not restated here.

    def domain(self) -> RModule:
        return self.parent().domain()

    def codomain(self) -> RModule:
        return self.parent().codomain()

    @abstract_method
    def kernel(self) -> SubModule: ...

    @abstract_method
    def cokernel(self) -> QuotientModule: ...

    @abstract_method
    def image(self) -> SubModule: ...

    @abstract_method
    def coimage(self) -> SubModule: ...

    @abstract_method
    def evaluate(self, m: RModuleElement) -> RModuleElement: ...

    @abstract_method
    def __call__(
        self, m: RModuleElement | SubModule
    ) -> RModuleElement | SubModule:
        r"""``f(m)`` is f applied to m; ``f(M)`` is the image submodule of f."""
        ...

    @abstract_method
    def compose(self, f: Self) -> Self: ...

    @abstract_method
    def is_identity(self) -> bool: ...

    @abstract_method
    def is_isomorphism(self) -> bool: ...

    @abstract_method
    def is_injective(self) -> bool: ...

    @abstract_method
    def is_surjective(self) -> bool: ...

    @abstract_method
    def is_bijective(self) -> bool: ...

    @abstract_method
    def is_endomorphism(self) -> bool: ...

    @abstract_method
    def is_automorphism(self) -> bool: ...

    @abstract_method
    def index(self) -> Cardinality: ...

    @abstract_method
    def direct_sum(self, f: Self) -> Self: ...

    @abstract_method
    def __add__(self, f: Self) -> Self:
        r"""``(f + g)(m) := f(m) + g(m)``, pointwise addition in Hom_R(M, N)."""
        ...

    @abstract_method
    def tensor(self, f: Self) -> Self: ...

    @abstract_method
    def scale(self, r: RingElement) -> Self:
        r"""``(r*f)(m) := r * f(m) = f(r.m)``."""
        ...

    @abstract_method
    def _mul_(self, data: RingElement | Self) -> Self:
        r"""Concrete impls dispatch on ``RingElement`` (-> ``scale``)
        vs another ``RModMorphism`` (-> ``tensor``).
        """
        ...

    def is_primitive(self) -> bool:
        r"""``f: M -> N`` is primitive iff coker(f) is torsionfree."""
        return self.cokernel().is_torsionfree()

    @abstract_method
    def lift(self, m: RModuleElement) -> RModuleElement:
        r"""Return any element ``m'`` such that ``f(m') = m``."""
        ...

    @abstract_method
    def dual(self) -> Self:
        r"""Given f in Hom_R(A, B), return f^* in Hom_R(B^*, A^*) where
        f^*(\phi) := \phi \circ f.  (Also called the adjoint or transpose.)
        Satisfies ``<f(m), \phi>_{nat,N} = <m, f^*(\phi)>_{nat,M}``.
        """
        ...

    def saturation(self) -> Self:
        r"""Given f in Hom_R(A, B), find the inclusion ``g`` of im(f) into
        Sat_B(im(f)) and return ``h := g \circ f`` in Hom_R(A, B) so that
        im(h) is saturated.
        """
        return self.image().saturation().inclusion().compose(self)


# ---------------------------------------------------------------------------
# Endomorphism element methods
# ---------------------------------------------------------------------------

class _RModEndomorphisms:
    @abstract_method
    def order(self) -> Cardinality:
        r"""The minimal n such that f^n = id, or infinity if none exists.
        Equivalently the cardinality of {f^n | n in NN}.
        """
        ...

    @abstract_method
    def is_automorphism(self) -> bool: ...

    @abstract_method
    def is_invertible(self) -> bool: ...

    @abstract_method
    def inverse(self) -> Self:
        r"""Asserts ``self.is_automorphism()`` first."""
        ...

    @abstract_method
    def __pow__(self, n: int) -> Self: ...


# ---------------------------------------------------------------------------
# Automorphism element methods
# ---------------------------------------------------------------------------

class _RModAutomorphisms:
    def is_automorphism(self) -> bool:
        return True

    def is_injective(self) -> bool:
        return True

    def is_surjective(self) -> bool:
        return True

    def is_bijective(self) -> bool:
        return True

    def is_invertible(self) -> bool:
        return True

    def is_isomorphism(self) -> bool:
        return True

    def image(self) -> SubModule:
        return self.codomain()

    @abstract_method
    def inverse(self) -> Self: ...

    @abstract_method
    def __pow__(self, n: int) -> Self: ...


# ---------------------------------------------------------------------------
# Endset and Autset subcategories
# ---------------------------------------------------------------------------

class _Endsets(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        r"""End_R(M) is an R-algebra."""
        # Deferred to avoid circular import with sage_modules.
        from .sage_modules import Modules
        R = self.base_ring()
        return [MagmaticAlgebras(R), Modules(R)]

    class ParentMethods:
        @abstract_method
        def base_module(self) -> RModule:
            r"""If this is End_R(M), return M."""
            ...

        @abstract_method
        def Aut(self) -> RModAutSet: ...

        @abstract_method
        def unit_group(self) -> RModAutSet: ...

        @abstract_method
        def identity(self) -> RModuleEndomorphism: ...
        # Do not define ``as_automorphism`` -- promotion of invertible
        # objects should happen automatically.

    ElementMethods = _RModEndomorphisms


class _Autsets(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        r"""Aut_R(M) := End_R(M)^* is the group of units of End_R(M)."""
        return [self.base_category().Endset(), Groups()]

    class ParentMethods:
        def is_aut_set(self) -> bool:
            return True

    ElementMethods = _RModAutomorphisms


_Endsets.Autset = _Autsets


# ---------------------------------------------------------------------------
# Forms axiom subcategory
# ---------------------------------------------------------------------------

class _Forms(CategoryWithAxiom_over_base_ring):
    r"""R-modules of the form ``Hom_R(T_R(M)[p,q], S)`` where ``T_R(M)[p,q]``
    is the (p, q) part of the bitensor R-algebra of M and ``S`` is an
    R-submodule of ``K := Frac(R)``.
    """

    class ParentMethods:
        @abstract_method
        def form_degree(self) -> tuple[int, int]:
            r"""Return ``(p, q)``."""
            ...

        @abstract_method
        def is_integral(self) -> bool: ...

        @abstract_method
        def is_rational(self) -> bool:
            r"""True if it takes a non-integral value."""
            ...

        @abstract_method
        def base_module(self) -> RModule:
            r"""If this is ``Hom_R(T_R(M)[p,q], S)``, return ``M``."""
            ...

    class SubcategoryMethods:
        @cached_method
        def Rational(self):
            r"""``S = K``: ``Hom_R(M, K)``."""
            return self._with_axiom("Rational")

        @cached_method
        def Integral(self):
            r"""``S = R``: ``Hom_R(M, R)``."""
            return self._with_axiom("Integral")

        @cached_method
        def Linear(self):
            r"""(1, 0)-forms: ``Hom_R(M, S)``."""
            return self._with_axiom("Linear")

        @cached_method
        def Bilinear(self):
            r"""(1, 1)-forms: ``Hom_R(M \otimes_R M^*, S)``."""
            return self._with_axiom("Bilinear")

        @cached_method
        def Quadratic(self):
            r"""Twisted (1, 0)-forms: ``Hom_R(M, S^\sigma)``."""
            return self._with_axiom("Quadratic")

        @cached_method
        def NonDegenerate(self):
            r"""Forms with trivial kernels."""
            return self._with_axiom("NonDegenerate")

        @cached_method
        def Symmetric(self):
            r"""Symmetric (n, 0)-forms: ``Hom_R(Sym^n_R(M), S)``."""
            return self._with_axiom("Symmetric")

        @cached_method
        def Alternating(self):
            r"""Alternating (n, 0)-forms: ``Hom_R(\Lambda^n_R(M), S)``."""
            return self._with_axiom("Alternating")

    Bilinear = _Bilinear
    Quadratic = _Quadratic


# ---------------------------------------------------------------------------
# RModuleHomsets: the homset category proper
# ---------------------------------------------------------------------------

class RModuleHomsets(HomsetsCategory):
    r"""The category of R-module homsets ``Hom_R(M, N)``.

    Objects are homsets; elements are R-module morphisms.
    """

    def extra_super_categories(self):
        r"""``Hom_R(M, N)`` is again an R-module for any M, N."""
        return [self.base_category()]

    class SubcategoryMethods:
        @cached_method
        def Endset(self):
            return self._with_axiom("Endset")

        @cached_method
        def Autset(self):
            return self._with_axiom("Autset")

        @cached_method
        def Forms(self):
            return self._with_axiom("Forms")

    ParentMethods = _RModHomsetObjects
    ElementMethods = _RModMorphisms

    Endset = _Endsets
    Autset = _Autsets
    Forms = _Forms
