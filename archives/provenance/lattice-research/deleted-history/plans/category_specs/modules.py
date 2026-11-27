"""Spec stub for the FGP module category used by the module redesign.

This category composes with Sage's existing ``Modules(R).FinitelyPresented()``
rather than replacing it.  It adds:

- a ``WithGenerators()`` axiom for modules with a canonical ordered generator
  tuple (distinct from ``WithBasis()``, which routes into
  ``CombinatorialFreeModule`` machinery and assumes a free structure),
- ``Free()``, ``Torsion()``, ``Ideals()``, ``Subobjects()``, and
  ``Quotients()`` subcategories, with ``SubObjects`` and
  ``QuotientObjects`` retained only as spelling aliases,
- construction methods on the category instance itself so that
  ``Modules(ZZ).free_module(n)`` etc. are the public API.

Sage's existing ``TensorProducts`` and ``CartesianProducts`` constructions are
inherited from ``Modules(R)``.  ``DualObjects`` extends Sage's dual-object
construction because these dual parents must also behave as homsets
``Hom_R(M, R)``.

The underlying implementation tracks the Smith Normal Form (SNF) diagonal
``[d_1, ..., d_k, 0, ..., 0]``.  An entry ``0`` contributes a free summand
``R``; a nonzero entry ``d_i`` contributes a torsion summand ``R/d_i``.
Construction methods auto-promote via ``_refine_category_`` when the
invariants indicate a purely free or purely torsion object.

Methods that return ideals (e.g. ``annihilator``) produce Sage
``Ideal_generic`` instances refined through the separate ring-ideal hierarchy
for the base ring and through ``Modules(R).Ideals()`` for the module-subobject
view.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator, Mapping, Sequence
from typing import TYPE_CHECKING, Any, final

import sage.categories.category_with_axiom as _cwa
from sage.categories.category import Category
from sage.categories.category_over_base_ring import Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.homset import Hom, Homset
from sage.categories.homsets import HomsetsCategory
from sage.categories.magmatic_algebras import MagmaticAlgebras
from sage.categories.modules import Modules as SageModules
from sage.categories.principal_ideal_domains import PrincipalIdealDomains
from sage.categories.quotients import QuotientsCategory
from sage.categories.subobjects import SubobjectsCategory
from sage.categories.tensor import TensorProductsCategory
from sage.misc.cachefunc import cached_method
from sage.rings.infinity import Infinity
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import InfinityElement, Matrix, Vector
from sage.structure.parent import Parent

from .homsets import (
    ModuleAutomorphism,
    RModAutset,
)

if TYPE_CHECKING:
    from .rings import ModuleBaseRingElement, ModuleBaseRingsCategoryObject
    from .types import (
        DualModule,
        DualModuleElement,
        FreeModule,
        Ideal,
        QuotientModule,
        RModEndset,
        RModEndsetElement,
        RModHomsetElement,
        RModule,
        RModuleElement,
        SubModule,
        TorsionModule,
    )

_cwa.all_axioms += ("WithGenerators", "Projective")

Cardinality = Integer | InfinityElement
ElementOrder = Integer | InfinityElement


class BaseChangeFunctor(ABC):
    r"""Functor that tensors an ``R``-module (or morphism) with a ring map ``R → S``."""

    @abstractmethod
    def apply_to_object(self, module: RModule) -> RModule:
        ...

    @abstractmethod
    def apply_to_morphism(self, morphism: RModHomsetElement) -> RModHomsetElement:
        ...


class Modules(Category_over_base_ring):
    r"""
    Category of finitely presented ``R``-modules with canonical generators,
    as a subcategory of ``SageModules(R).FinitelyPresented()``.

    The category instance is the main construction interface:

    - ``Modules(R).free_module(n)`` — free module ``R^n``
    - ``Modules(R).from_elements([d_1, ..., d_k])`` — torsion module ``R/d_1 ⊕ ... ⊕ R/d_k``
    - ``Modules(R).from_presentation_matrix(A)`` — from arbitrary matrix

    Purely free or purely torsion results are auto-promoted to
    ``Modules(R).Free()`` or ``Modules(R).Torsion()`` via ``_refine_category_``.
    """

    @staticmethod
    @final
    def __classcall_private__(cls, base_ring: Ring):
        if base_ring not in PrincipalIdealDomains():
            raise TypeError(f"Modules spec requires a commutative PID; got {base_ring!r}")
        return super().__classcall__(cls, base_ring)

    @final
    def super_categories(self) -> list[Category]:
        return [SageModules(self.base_ring()).FinitelyPresented()]

    @final
    def additional_structure(self):
        return None

    @final
    def _repr_object_names(self) -> str:
        return f"finitely presented modules over {self.base_ring()}"

    def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # Construction methods (called on the category instance)
    # ------------------------------------------------------------------

    @abstractmethod
    def free_module(self, n: Integer) -> FreeModule:
        r"""
        Return ``R^n``.

        Constructs the SNF module with ``n`` zero diagonal entries and
        auto-promotes to ``Modules(R).Free()``.
        """
        ...

    @abstractmethod
    def from_elements(self, elements: Sequence[ModuleBaseRingElement]) -> RModule:
        r"""
        Return ``R/d_1 ⊕ ... ⊕ R/d_k`` from the sequence ``[d_1, ..., d_k]``.

        Each ``d_i`` generates a torsion summand ``R/d_i`` directly.  To
        construct from SNF invariants (i.e. with automatic divisibility
        reduction), use
        ``Modules(R).from_presentation_matrix(diagonal_matrix(R, [d_1, ..., d_k]))``.
        """
        ...

    @abstractmethod
    def from_presentation_matrix(self, A: Matrix) -> RModule:
        r"""
        Construct from an arbitrary presentation matrix.

        Computes the SNF of ``A`` and delegates to ``from_elements`` with the
        resulting nonzero diagonal entries.
        """
        ...

    # ------------------------------------------------------------------
    # SubcategoryMethods
    # ------------------------------------------------------------------

    class SubcategoryMethods:

        @final
        @cached_method
        # @overload category base ring
        def base_ring(self) -> ModuleBaseRingsCategoryObject:
            return self._reduction[1][0]

        @final
        @cached_method
        def Free(self) -> Modules.Free:
            return self._with_axiom("Free")

        @final
        @cached_method
        def Torsion(self) -> Modules.Torsion:
            return self._with_axiom("Torsion")

        @final
        @cached_method
        def WithGenerators(self) -> Modules.WithGenerators:
            return self._with_axiom("WithGenerators")

        @final
        @cached_method
        def FinitelyPresented(self) -> Modules.FinitelyPresented:
            return self._with_axiom("FinitelyPresented")

        @final
        @cached_method
        def Projective(self) -> Modules.Projective:
            return self._with_axiom("Projective")

        @final
        @cached_method
        def Ideals(self) -> Modules.Ideals:
            return self._with_axiom("Ideals")

        @final
        @cached_method
        def Subobjects(self) -> Modules.Subobjects:
            return Modules.Subobjects.category_of(self)

        Submodules = Subobjects
        SubObjects = Subobjects

        @final
        @cached_method
        def Quotients(self) -> Modules.Quotients:
            return Modules.Quotients.category_of(self)

        QuotientObjects = Quotients

        @final
        @cached_method
        def DualObjects(self) -> Category:
            return self.TwistedForms().Linear()

        dual_objects = DualObjects

        @final
        @cached_method
        def TwistedForms(self) -> Category:
            from .twisted_forms import TwistedForms
            return TwistedForms(self.base_ring())

        @final
        @cached_method
        def WithForm(self) -> Modules.WithForm:
            return self._with_axiom("WithForm")

        @abstractmethod
        def zero_module(self) -> RModule: ...

        @abstractmethod
        def base_change(self, ring: ModuleBaseRingsCategoryObject) -> Modules: ...

        @abstractmethod
        def base_change_functor(self, ring: ModuleBaseRingsCategoryObject) -> BaseChangeFunctor: ...

        @abstractmethod
        def random_module(self) -> RModule: ...

        @abstractmethod
        def an_object(self) -> RModule: ...

    # ------------------------------------------------------------------
    # Subcategories
    # ------------------------------------------------------------------

    class WithGenerators(CategoryWithAxiom_over_base_ring):
        r"""Modules with a canonical ordered finite generator tuple."""

        @final
        def super_categories(self):
            return [Modules(self.base_ring())]

        @final
        def _repr_object_names(self) -> str:
            return "modules with canonical generators"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def module_generators(self) -> tuple[RModuleElement, ...]:
                """Distinguished finite generating tuple. NOT a basis."""
                ...

            @final
            def gens(self) -> tuple[RModuleElement, ...]:
                return self.module_generators()

            @final
            def gen(self, index: int) -> RModuleElement:
                return self.module_generators()[index]

            @final
            def ngens(self) -> Integer:
                return Integer(len(self.module_generators()))

            @abstractmethod
            def hom(self, im_gens, codomain=None, check=True):
                """Define a morphism by images of module_generators()."""
                ...

        class ElementMethods: ...
        class MorphismMethods: ...

    class FinitelyPresented(CategoryWithAxiom_over_base_ring):
        r"""Finitely presented modules -- implies WithGenerators over a PID."""

        def extra_super_categories(self):
            return [self.base_category().WithGenerators()]

        @final
        def _repr_object_names(self) -> str:
            return "finitely presented modules"

        def _latex_(self) -> str: ...

        class ParentMethods: ...
        class ElementMethods: ...
        class MorphismMethods: ...

    class Projective(CategoryWithAxiom_over_base_ring):
        r"""Projective modules -- have a Steinitz class but not necessarily a basis."""

        @final
        def super_categories(self):
            return [Modules(self.base_ring()).WithGenerators()]

        @final
        def _repr_object_names(self) -> str:
            return "projective modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def steinitz_class(self):
                """The Steinitz class in the ideal class group."""
                ...

        class ElementMethods: ...
        class MorphismMethods: ...

    class Free(CategoryWithAxiom_over_base_ring):
        r"""Free ``R``-modules; SNF diagonal is all zeros."""

        @final
        def super_categories(self):
            return [Modules(self.base_ring()).WithGenerators()]

        @final
        def _repr_object_names(self) -> str:
            return "free modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def rank(self) -> Integer: ...

            @final
            def free_rank(self) -> Integer:
                return self.rank()

            @abstractmethod
            def basis(self):
                """A basis for this free module."""
                ...

            @abstractmethod
            def tensor_module(
                self, contravariant_degree: int, covariant_degree: int
            ) -> FreeModule: ...

            @abstractmethod
            def tensor_algebra(self) -> Parent: ...

            @abstractmethod
            def exterior_algebra(self) -> Parent: ...

            @abstractmethod
            def symmetric_algebra(self) -> Parent: ...

            @abstractmethod
            def wedge_power(self, degree: int) -> FreeModule: ...

            @abstractmethod
            def determinant_module(self) -> FreeModule: ...

            @abstractmethod
            def linear_form(self, coefficients: Sequence[ModuleBaseRingElement]) -> RModHomsetElement:
                r"""
                Return the linear functional ``M → R`` whose value on
                generator ``g_i`` is ``coefficients[i]``.

                Concretely: given a free module ``M = R^n`` with generators
                ``e_1, ..., e_n``, returns the morphism
                ``Σ a_i e_i ↦ Σ coefficients[i] * a_i``.
                """
                ...

        class ElementMethods:
            @abstractmethod
            def __getitem__(self, index: int) -> ModuleBaseRingElement: ...

            @abstractmethod
            def divisibility(self) -> ModuleBaseRingElement: ...

            @abstractmethod
            def is_primitive(self) -> bool: ...

        class MorphismMethods: ...

    class Torsion(CategoryWithAxiom_over_base_ring):
        r"""Torsion ``R``-modules; SNF diagonal has no zero entries."""

        @final
        def super_categories(self):
            return [Modules(self.base_ring()).WithGenerators()]

        @final
        def _repr_object_names(self) -> str:
            return "torsion modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def invariant_factors(self) -> tuple[ModuleBaseRingElement, ...]:
                r"""The nonzero SNF diagonal entries ``(d_1, ..., d_k)``."""
                ...

            @abstractmethod
            def annihilator(self) -> Ideal:
                """The annihilator ideal of the torsion module."""
                ...

            @abstractmethod
            def p_part(self, p: ModuleBaseRingElement) -> TorsionModule: ...

            @abstractmethod
            def is_p_elementary(self, p: ModuleBaseRingElement) -> bool: ...

        class ElementMethods:
            @abstractmethod
            def order(self) -> ElementOrder: ...

        class MorphismMethods: ...

    class Ideals(CategoryWithAxiom_over_base_ring):
        r"""
        Subcategory of principal ``R``-ideals viewed as ``R``-subobjects.

        Objects are ``sage.rings.ideal.Ideal_generic`` instances whose
        categories have been refined into both ``ModuleBaseIdeals(R)`` and
        ``Modules(R).Ideals()``.

        ``ModuleBaseIdeals(R)`` supplies the ideal-side return-type overrides
        for ``Ideal_generic`` / ``Ideal_pid`` methods.  This module-facing
        category adds the fact that those ideals are subobjects of the
        ambient ``R``-module.
        """

        @final
        def super_categories(self):
            from .rings import ModuleBaseIdeals
            R = self.base_ring()
            return [Modules(R).Subobjects(), ModuleBaseIdeals(R)]

        @final
        def additional_structure(self):
            return None

        @final
        def _repr_object_names(self) -> str:
            return "principal ideal submodules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            ...

        class ElementMethods: ...
        class MorphismMethods: ...

    class Subobjects(SubobjectsCategory):
        r"""
        Subobjects of a finitely presented ``R``-module, equipped with
        a canonical inclusion morphism into an ambient module.
        """

        @final
        def super_categories(self):
            return [Modules(self.base_ring())]

        @final
        def _repr_object_names(self) -> str:
            return "subobjects of modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @final
            def ambient(self) -> RModule:
                return self.inclusion().codomain()

            @abstractmethod
            def inclusion(self) -> RModHomsetElement: ...

            @abstractmethod
            def intersect(self, other: SubModule) -> SubModule: ...

            @final
            def __and__(self, other: SubModule) -> SubModule:
                return self.intersect(other)

            @abstractmethod
            def index(self) -> Cardinality:
                r"""Cardinality of ``self.inclusion().codomain() / self``."""
                ...

        class ElementMethods: ...
        class MorphismMethods: ...

    SubObjects = Subobjects
    Submodules = Subobjects

    class Quotients(QuotientsCategory):
        r"""
        Quotient modules ``M/N``, equipped with a canonical projection
        morphism.  A quotient object is not inside an ambient module; its
        source module is ``projection().domain()``.
        """

        @final
        def super_categories(self):
            return [Modules(self.base_ring())]

        @final
        def _repr_object_names(self) -> str:
            return "quotient objects of modules"

        def _latex_(self) -> str: ...

        class ParentMethods:
            @abstractmethod
            def projection(self) -> RModHomsetElement: ...

        class ElementMethods: ...
        class MorphismMethods: ...

    class TensorProducts(TensorProductsCategory):
        class Homsets(HomsetsCategory):
            class ElementMethods:
                @abstractmethod
                def evaluate(self, *args: Any) -> RModuleElement:
                    r"""
                    Evaluate this tensor-hom morphism.
                    
                    Can be called with either a single tensor product element,
                    or a tuple of module elements representing a pure tensor.
                    """
                    ...

    QuotientObjects = Quotients

    class WithForm(CategoryWithAxiom_over_base_ring):
        r"""Refinement for modules equipped with form data."""

        @final
        def super_categories(self):
            return [self.base_category()]

        @final
        def additional_structure(self):
            return self.base_category().TwistedForms()

        @final
        def _repr_object_names(self) -> str:
            return "modules with forms"

        def _latex_(self) -> str: ...

        class ParentMethods:
            ...

        class ElementMethods:
            ...

    # ------------------------------------------------------------------
    # ParentMethods
    # ------------------------------------------------------------------

    class ParentMethods:

        @abstractmethod
        def invariants(self) -> tuple[ModuleBaseRingElement, ...]:
            r"""
            The full SNF diagonal ``(d_1, ..., d_k, 0, ..., 0)`` for every
            module in this category, where
            nonzero ``d_i`` are torsion invariants and zeros are free ranks.
            """
            ...

        @abstractmethod
        def __iter__(self) -> Iterator[RModuleElement]: ...

        @abstractmethod
        def zero(self) -> RModuleElement: ...

        # @overload module parent base ring
        @abstractmethod
        def base_ring(self) -> ModuleBaseRingsCategoryObject: ...

        @abstractmethod
        def free_part(self) -> FreeModule: ...

        @abstractmethod
        def torsion_part(self) -> TorsionModule: ...

        @abstractmethod
        def dual(self) -> DualModule:
            r"""
            The ``R``-dual ``Hom_R(M, R)`` as an object of
            ``Modules(R).DualObjects()``.
            """
            ...

        @abstractmethod
        def annihilator(
            self,
            value: RModuleElement | SubModule | None = None,
        ) -> Ideal:
            r"""
            Annihilator ideal.

            If ``value`` is a module element, return ``{r in R | r·value = 0}``.
            If ``value`` is a subobject, return the ideal annihilating every
            element of that subobject.  If ``value`` is ``None``, return the
            annihilator of the whole module ``self``.
            """
            ...

        @abstractmethod
        def is_free(self) -> bool: ...

        @abstractmethod
        def is_torsion(self) -> bool: ...

        @final
        def is_torsionfree(self) -> bool:
            r"""Over a PID, finitely presented torsion-free modules are free."""
            return self.is_free()

        @abstractmethod
        def free_rank(self) -> Integer: ...

        @abstractmethod
        def cardinality(self) -> Cardinality: ...

        @final
        def is_finite(self) -> bool:
            return self.cardinality() != Infinity

        @abstractmethod
        def is_isomorphic_to(self, other: RModule) -> bool: ...

        @final
        def Hom(self, other: RModule) -> Homset:
            return Hom(self, other, category=self.category())

        @final
        def End(self) -> RModEndset:
            return self.Hom(self)

        @final
        def Aut(self) -> RModAutset:
            return self.End().unit_group()

        @abstractmethod
        def direct_sum(self, *others: RModule) -> RModule: ...

        @abstractmethod
        def tensor(self, *others: RModule) -> RModule: ...

        @abstractmethod
        def span(
            self,
            elements: Iterable[RModuleElement] | ModuleBaseRingElement,
        ) -> SubModule: ...

        @abstractmethod
        def submodule(self, generators: Iterable[RModuleElement]) -> SubModule: ...

        @abstractmethod
        def submodules(self) -> Iterable[SubModule]: ...

        @abstractmethod
        def is_submodule_of(
            self,
            other: RModule,
            morphism: RModHomsetElement | None = None,
        ) -> bool: ...

        @abstractmethod
        def quotient(self, submodule: SubModule) -> QuotientModule: ...

        @final
        def __truediv__(self, submodule: SubModule) -> QuotientModule:
            return self.quotient(submodule)

        @abstractmethod
        def saturation(self) -> SubModule: ...

        @abstractmethod
        def is_primitive(self) -> bool: ...

        @final
        def __add__(self, other: RModule) -> RModule:
            return self.direct_sum(other)

        @abstractmethod
        def _mul_(self, other: ModuleBaseRingElement | RModule) -> RModule:
            r"""
            Dispatch multiplication by type.

            ``M * N`` is the tensor product of modules.  Scalar
            multiplication is only the Sage left action ``r * M`` and returns
            the subobject ``rM`` via ``_lmul_``.
            """
            ...

        @final
        def __mul__(self, other: ModuleBaseRingElement | RModule) -> RModule:
            return self._mul_(other)

        @abstractmethod
        def _lmul_(self, scalar: ModuleBaseRingElement) -> SubModule:
            r"""Return the submodule ``scalar · self = {scalar · m | m ∈ self}``."""
            ...

        @final
        def __rmul__(self, scalar: ModuleBaseRingElement) -> SubModule:
            return self._lmul_(scalar)

        @abstractmethod
        def __contains__(self, value: Any) -> bool: ...

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # ElementMethods
    # ------------------------------------------------------------------

    class ElementMethods:

        @abstractmethod
        def parent(self) -> RModule: ...

        @abstractmethod
        def order(self) -> ElementOrder:
            r"""Additive order in ``ZZ`` or ``Infinity``; never a ring element."""
            ...

        @abstractmethod
        def annihilator(self) -> Ideal:
            r"""Annihilator ideal ``{r ∈ R | r·self = 0}``."""
            ...

        @abstractmethod
        def to_vector(self) -> Vector:
            r"""Coordinates with respect to the ordered generator/basis tuple."""
            ...

        @abstractmethod
        def dual(self) -> DualModuleElement:
            r"""
            Return the corresponding element of ``self.parent().dual()``.
            """
            ...

        @final
        def span(self) -> SubModule:
            return self.parent().span([self])

        @abstractmethod
        def __add__(self, other: RModuleElement) -> RModuleElement: ...

        @abstractmethod
        def __neg__(self) -> RModuleElement: ...

        @abstractmethod
        def _lmul_(self, scalar: ModuleBaseRingElement) -> RModuleElement: ...

        @final
        def __rmul__(self, scalar: ModuleBaseRingElement) -> RModuleElement:
            return self._lmul_(scalar)

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # MorphismMethods
    # ------------------------------------------------------------------

    class MorphismMethods:

        # @override Morphism.domain
        @abstractmethod
        def domain(self) -> RModule: ...

        # @override Morphism.codomain
        @abstractmethod
        def codomain(self) -> RModule: ...

        @abstractmethod
        def __call__(self, value: RModuleElement) -> RModuleElement: ...

        @abstractmethod
        def to_matrix(self) -> Matrix: ...

        @final
        def to_tuple_of_images(self) -> tuple[RModuleElement, ...]:
            return tuple(self(g) for g in self.domain().gens())

        @final
        def to_list_of_images(self) -> list[RModuleElement]:
            return list(self.to_tuple_of_images())

        @final
        def to_dict(self) -> dict[RModuleElement, RModuleElement]:
            return dict(zip(self.domain().gens(), self.to_tuple_of_images(), strict=True))

        @abstractmethod
        def image(self) -> SubModule: ...

        @abstractmethod
        def kernel(self) -> SubModule: ...

        @abstractmethod
        def cokernel(self) -> QuotientModule: ...

        @abstractmethod
        def index(self) -> Cardinality:
            r"""Cardinality of ``self.codomain() / self.image()``."""
            ...

        @abstractmethod
        def lift(self, value: RModuleElement) -> RModuleElement: ...

        @abstractmethod
        def lift_generators(self) -> tuple[RModuleElement, ...]:
            r"""
            Lift the generators of ``codomain`` to elements of ``domain``
            along this morphism.
            """
            ...

        @abstractmethod
        def saturation(self) -> SubModule: ...

        @abstractmethod
        def invariant_submodule(self) -> SubModule:
            r"""
            Subobject of ``domain`` fixed by this endomorphism.

            Undefined unless ``self.is_endomorphism()``.
            """
            ...

        @abstractmethod
        def coinvariant_submodule(self) -> QuotientModule:
            r"""
            Quotient of ``domain`` by the image of ``(id - self)``.

            Undefined unless ``self.is_endomorphism()``.
            """
            ...

        @abstractmethod
        def is_injective(self) -> bool: ...

        @abstractmethod
        def is_surjective(self) -> bool: ...

        @final
        def is_bijective(self) -> bool:
            return self.is_injective() and self.is_surjective()

        @abstractmethod
        def is_endomorphism(self) -> bool: ...

        @abstractmethod
        def is_isomorphism(self) -> bool: ...

        @abstractmethod
        def is_identity(self) -> bool:
            r"""Whether this endomorphism is the identity on its domain."""
            ...

        @abstractmethod
        def is_primitive(self) -> bool: ...

        @abstractmethod
        def direct_sum(self, other: RModHomsetElement) -> RModHomsetElement: ...

        @abstractmethod
        def tensor(self, other: RModHomsetElement) -> RModHomsetElement: ...

        @abstractmethod
        def base_change(
            self, ring: ModuleBaseRingsCategoryObject
        ) -> RModHomsetElement: ...

        @abstractmethod
        def __mul__(self, other: RModHomsetElement) -> RModHomsetElement: ...

        @abstractmethod
        def _repr_(self) -> str: ...

        @abstractmethod
        def _latex_(self) -> str: ...

    # ------------------------------------------------------------------
    # Homsets
    # ------------------------------------------------------------------

    class Homsets(HomsetsCategory):

        @final
        def extra_super_categories(self):
            R = self.base_category().base_ring()
            return [Modules(R).FinitelyPresented()]

        # @overload homset category base ring
        @final
        def base_ring(self) -> ModuleBaseRingsCategoryObject:
            return self.base_category().base_ring()

        @final
        def _repr_object_names(self) -> str:
            return "homsets of modules"

        def _latex_(self) -> str: ...

        class ParentMethods:

            # @override Homset.domain
            @abstractmethod
            def domain(self) -> RModule: ...

            # @override Homset.codomain
            @abstractmethod
            def codomain(self) -> RModule: ...

            # @overload homset parent base ring
            @final
            @cached_method
            def base_ring(self) -> ModuleBaseRingsCategoryObject:
                return self.domain().base_ring()

            @abstractmethod
            def from_dict(
                self, mapping: Mapping[RModuleElement, RModuleElement]
            ) -> RModHomsetElement: ...

            @abstractmethod
            def from_images(
                self, images: Sequence[RModuleElement]
            ) -> RModHomsetElement: ...

            @final
            def from_tuple_of_images(
                self, images: tuple[RModuleElement, ...]
            ) -> RModHomsetElement:
                return self.from_images(images)

            @abstractmethod
            def from_matrix(self, matrix_data: Matrix) -> RModHomsetElement: ...

            @abstractmethod
            def natural_map(self) -> RModHomsetElement: ...

            @abstractmethod
            def __call__(self, data: Any) -> RModHomsetElement: ...

            @abstractmethod
            def __contains__(self, value: Any) -> bool: ...

            @abstractmethod
            def _repr_(self) -> str: ...

            @abstractmethod
            def _latex_(self) -> str: ...

        class ElementMethods: ...
        class MorphismMethods: ...

        class Endset(CategoryWithAxiom_over_base_ring):
            r"""
            Endomorphism algebras ``End_R(M)``.

            Sage's category join turns
            ``Modules(R).Homsets().Endset()`` into ``Algebras(R)``: homsets
            supply the ``R``-module structure, generic endsets supply the
            unital associative composition monoid, and ``MagmaticAlgebras(R)``
            supplies bilinearity of multiplication.
            """

            @final
            def extra_super_categories(self):
                return [MagmaticAlgebras(self.base_category().base_ring())]

            @final
            def _repr_object_names(self) -> str:
                return "endomorphism algebras of modules"

            def _latex_(self) -> str: ...

            class ParentMethods:

                @final
                def module(self) -> RModule:
                    return self.domain()

                @abstractmethod
                def identity(self) -> RModHomsetElement: ...

                @final
                def id(self) -> RModHomsetElement:
                    return self.identity()

                @final
                def one(self) -> RModHomsetElement:
                    return self.identity()

                @abstractmethod
                def zero(self) -> RModHomsetElement: ...

                @abstractmethod
                def matrix_algebra_quotient(self) -> Parent:
                    r"""
                    Present ``End_R(M)`` as a quotient of a matrix algebra.

                    For SNF invariants ``(d_1, ..., d_t, 0, ..., 0)``, the
                    presentation records the block equations forcing maps to
                    descend to ``M`` and the reductions modulo torsion
                    invariants.  If ``M`` is free of rank ``n``, this is the
                    literal matrix algebra ``Mat_n(R)``.
                    """
                    ...

                @abstractmethod
                def from_matrix(self, matrix_data: Matrix) -> RModEndsetElement: ...

                @abstractmethod
                def Aut(self) -> RModAutset: ...

                @final
                def unit_group(self) -> RModAutset:
                    return self.Aut()

            class ElementMethods:

                @abstractmethod
                def parent(self) -> RModEndset: ...

                @abstractmethod
                def is_unit(self) -> bool:
                    r"""Whether this endomorphism is an automorphism of its module."""
                    ...

                @abstractmethod
                def inverse(self) -> RModEndsetElement:
                    r"""Inverse in ``End_R(M)``; defined exactly for units."""
                    ...

                @final
                def __invert__(self) -> RModEndsetElement:
                    return self.inverse()

                @abstractmethod
                def as_automorphism(self) -> ModuleAutomorphism:
                    r"""Return this unit as an element of ``Aut_R(M)``."""
                    ...

            class MorphismMethods: ...


from .twisted_forms import TwistedForms

Modules.DualObjects = TwistedForms.Linear
TwistedForms.Linear._base_category_class = (Modules,)
