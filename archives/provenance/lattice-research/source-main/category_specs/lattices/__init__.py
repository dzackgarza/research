r"""Lattice category.

``Lattices(R)`` is the named endpoint of the actual formed-module axiom chain

``Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral().Lattice()``.

The initializer owns the readable public index for the lattice subtree: the
root category class, constructor namespace, lattice-specific subcategories, and
standard type package aliases live here.  Detailed lattice methods stay
in the subcategory files.

Subcategory hierarchy::

    Lattices(R)
    |-- OverIntegralDomain()
    |   `-- OverDedekindDomain()
    |       `-- OverPID()
    |           `-- OverIntegers()
    |-- Even()
    |-- Unimodular()
    |-- Subobjects()
    |-- Quotients()
    |-- Subquotients()
    |-- ObjectsOver()
    |-- ObjectsUnder()
    |-- CartesianProducts()
    |-- DualObjects()
    |-- DualLattices()
    |-- Overlattices()
    |-- OrthogonalDirectSums()
    |-- DiscriminantGroups()
    `-- HomCategory()
        |-- EndCategory()
        `-- AutCategory()
"""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Literal, TypeVar, final, overload

from sage.categories.category import Category
from sage.misc.lazy_import import LazyImport

from ..cat import CategoryWithAxiom_over_base_ring
from ..forms.chain import (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
)
from ..modules import Modules
from ..utils import refine_category
from .homsets import (
    LatticeAutCategory,
    LatticeEndCategory,
    LatticeHomCategory,
    _LatticeMorphisms,
)
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import LatticeDualObjectsCategory
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    from ..spec_core import ConstructorRegistry
    from ..types import (
        DiscriminantGroup,
        DiscriminantGroupElement,
        Integer,
        Lattice,
        LatticeMorphism,
        Matrix,
        Ring,
        RingElement,
        RModuleElement,
    )

type LatticeBasisData = (
    Matrix | Sequence[RModuleElement] | Sequence[Sequence[RingElement]]
)
type CartanTypeData = str | Sequence[str | Integer | int]
type LatticeWithEmbeddings = tuple[Lattice, Sequence[LatticeMorphism]]


class LatticesCategory(CategoryWithAxiom_over_base_ring):
    r"""Lattices over ``R`` as the named endpoint of the lattice axiom chain.

    Canonical chain: ``Lattices(R)``.
    """

    _base_category_class_and_axiom = (
        IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
        "Lattice",
    )
    _defining_predicates = ("is_lattice",)

    @final
    def _repr_object_names(self) -> str:
        return f"lattices over {self.base_ring()}"

    class _Constructors:
        r"""Lattice constructor entry points over ``self.base_ring()``."""

        @final
        def __init__(self, category: LatticesCategory) -> None:
            self._category = category

        @final
        def __repr__(self) -> str:
            return f"lattice constructors over {self.base_ring()}"

        @final
        def provenance(self) -> ConstructorRegistry:
            r"""Return typed provenance records for lattice constructors."""
            from category_specs.spec_core import constructor_registry_for_category

            return constructor_registry_for_category(
                self.category(),
                owner_category=f"Lattices({self.base_ring()})",
                id_prefix="lattices",
            )

        @final
        def category(self) -> LatticesCategory:
            return self._category

        @final
        def base_ring(self) -> Ring:
            base_ring: Ring = self.category().base_ring()
            return base_ring

        @final
        def _assert_integral_constructor_base_ring(self) -> None:
            from sage.rings.integer_ring import ZZ

            assert self.base_ring() == ZZ

        @final
        def _refine_constructed_lattice(self, lattice: Lattice) -> Lattice:
            return refine_category(lattice, self.category(), test=False)

        @overload
        def IntegralLattice(
            self, *, gram_matrix: Matrix, basis: LatticeBasisData | None = None
        ) -> Lattice: ...

        @overload
        def IntegralLattice(
            self, *, rank: Integer | int, basis: LatticeBasisData | None = None
        ) -> Lattice: ...

        @overload
        def IntegralLattice(
            self, *, cartan_type: CartanTypeData, basis: LatticeBasisData | None = None
        ) -> Lattice: ...

        @overload
        def IntegralLattice(
            self,
            *,
            hyperbolic_plane: Literal["U", "H"],
            basis: LatticeBasisData | None = None,
        ) -> Lattice: ...

        @final
        def IntegralLattice(
            self,
            *,
            gram_matrix: Matrix | None = None,
            rank: Integer | int | None = None,
            cartan_type: CartanTypeData | None = None,
            hyperbolic_plane: Literal["U", "H"] | None = None,
            basis: LatticeBasisData | None = None,
        ) -> Lattice:
            r"""Construct a Sage integral lattice and refine it into this category."""
            from sage.modules.free_quadratic_module_integer_symmetric import (
                IntegralLattice,
            )

            self._assert_integral_constructor_base_ring()
            data = [
                gram_matrix,
                rank,
                cartan_type,
                hyperbolic_plane,
            ]
            supplied = [datum for datum in data if datum is not None]
            assert len(supplied) == 1
            return self._refine_constructed_lattice(
                IntegralLattice(supplied[0], basis=basis)
            )

        @overload
        def IntegralLatticeDirectSum(
            self,
            *,
            lattices: Sequence[Lattice],
            return_embeddings: Literal[False] = False,
        ) -> Lattice: ...

        @overload
        def IntegralLatticeDirectSum(
            self,
            *,
            lattices: Sequence[Lattice],
            return_embeddings: Literal[True],
        ) -> LatticeWithEmbeddings: ...

        @final
        def IntegralLatticeDirectSum(
            self,
            *,
            lattices: Sequence[Lattice],
            return_embeddings: bool = False,
        ) -> Lattice | LatticeWithEmbeddings:
            r"""Construct the orthogonal direct sum of integral lattices."""
            from sage.modules.free_quadratic_module_integer_symmetric import (
                IntegralLatticeDirectSum,
            )

            self._assert_integral_constructor_base_ring()
            result = IntegralLatticeDirectSum(
                list(lattices), return_embeddings=return_embeddings
            )
            if return_embeddings:
                lattice, embeddings = result
                return (self._refine_constructed_lattice(lattice), tuple(embeddings))
            return self._refine_constructed_lattice(result)

        @overload
        def IntegralLatticeGluing(
            self,
            *,
            lattices: Sequence[Lattice],
            glue: Sequence[Sequence[DiscriminantGroupElement]],
            return_embeddings: Literal[False] = False,
        ) -> Lattice: ...

        @overload
        def IntegralLatticeGluing(
            self,
            *,
            lattices: Sequence[Lattice],
            glue: Sequence[Sequence[DiscriminantGroupElement]],
            return_embeddings: Literal[True],
        ) -> LatticeWithEmbeddings: ...

        @final
        def IntegralLatticeGluing(
            self,
            *,
            lattices: Sequence[Lattice],
            glue: Sequence[Sequence[DiscriminantGroupElement]],
            return_embeddings: bool = False,
        ) -> Lattice | LatticeWithEmbeddings:
            r"""Construct the glued overlattice from discriminant-group glue data."""
            from sage.modules.free_quadratic_module_integer_symmetric import (
                IntegralLatticeGluing,
            )

            self._assert_integral_constructor_base_ring()
            result = IntegralLatticeGluing(
                list(lattices),
                [list(row) for row in glue],
                return_embeddings=return_embeddings,
            )
            if return_embeddings:
                lattice, embeddings = result
                return (self._refine_constructed_lattice(lattice), tuple(embeddings))
            return self._refine_constructed_lattice(result)

    @final
    def Constructors(self) -> LatticesCategory._Constructors:
        r"""Return the lattice constructor collector over ``self.base_ring()``."""
        return self.__class__._Constructors(self)

    class SubcategoryMethods:
        @final
        def OverIntegralDomain(self) -> Category:
            return self._with_axiom("OverIntegralDomain")
        @final
        def OverDedekindDomain(self) -> Category:
            return self._with_axiom("OverDedekindDomain")
        @final
        def OverPID(self) -> Category:
            return self.OverDedekindDomain().OverPID()
        @final
        def OverIntegers(self) -> Category:
            return self.OverPID().OverIntegers()
        @final
        def Even(self) -> Category:
            return self._with_axiom("Even")
        @final
        def Unimodular(self) -> Category:
            return self._with_axiom("Unimodular")
        @final
        def PositiveDefinite(self) -> Category:
            return self._with_axiom("PositiveDefinite")
        @final
        def DualObjects(self) -> Category:
            return LatticeDualObjectsCategory.category_of(self)
        @final
        def DualLattices(self) -> Category:
            r"""Return the metric-dual lattice construction category."""
            from .subcategories.constructions.dual_lattices import DualLatticesCategory

            return DualLatticesCategory(self.base_ring())
        @final
        def Overlattices(self) -> Category:
            from .subcategories.constructions.overlattices import OverlatticesCategory

            return OverlatticesCategory(self.base_ring())
        @final
        def OrthogonalDirectSums(self) -> Category:
            from .subcategories.constructions.orthogonal_direct_sums import (
                OrthogonalDirectSumsCategory,
            )

            return OrthogonalDirectSumsCategory(self.base_ring())
        @final
        def DiscriminantGroups(self) -> Category:
            from .subcategories.constructions.discriminant_groups import (
                LatticeDiscriminantGroupsCategory,
            )

            return LatticeDiscriminantGroupsCategory(self.base_ring())

    class ParentMethods:
        @final
        def is_lattice(self) -> bool:
            return True

        @abstractmethod
        def ambient_quadratic_space(self) -> object:
            """Return the ambient quadratic space carrying this lattice's form."""
            ...

        @abstractmethod
        def rational_span(self) -> object:
            """Return the category-aware rational quadratic span of this lattice."""
            ...

        @abstractmethod
        def basis_matrix(self, *, kind: str = "user") -> Matrix:
            """Return the user or echelon basis matrix without forgetting the lattice basis convention."""
            ...

        @abstractmethod
        def coordinates(self, x: RModuleElement, *, basis: str = "user") -> object:
            """Return coordinates of ``x`` in the requested lattice basis convention."""
            ...

        @abstractmethod
        def ambient_coordinates(self, x: RModuleElement) -> object:
            """Return ambient quadratic-space coordinates of ``x``."""
            ...

        @abstractmethod
        def change_base_ring(self, R: Ring) -> object:
            """Change the module base ring while preserving the ambient form metadata."""
            ...

        @abstractmethod
        def span(
            self,
            gens: Sequence[RModuleElement],
            *,
            base_ring: Ring | None = None,
            check_integral: bool | None = None,
            check_even: bool | None = None,
        ) -> object:
            """Return the category-aware lattice or rational quadratic span of ``gens``."""
            ...

        @abstractmethod
        def span_of_basis(
            self,
            basis: Sequence[RModuleElement],
            *,
            base_ring: Ring | None = None,
            check_integral: bool | None = None,
            check_even: bool | None = None,
        ) -> object:
            """Return the span generated by a declared basis, with lattice semantics preserved."""
            ...

        @abstractmethod
        def sublattice(
            self,
            gens: Sequence[RModuleElement],
            *,
            require_subset: bool = True,
            require_integral: bool = True,
        ) -> Lattice:
            """Return the integral sublattice generated by ``gens`` when its induced Gram matrix is integral."""
            ...

        @abstractmethod
        def fractional_sublattice(self, gens: Sequence[RModuleElement]) -> Lattice:
            """Return the fractional ZZ-lattice generated by rational ambient vectors."""
            ...

        @abstractmethod
        def overlattice(self, gens: Sequence[RModuleElement]) -> Lattice:
            """Return the overlattice generated inside the rational span or metric dual."""
            ...

        @abstractmethod
        def zero_lattice(self) -> Lattice:
            """Return the zero lattice in the same ambient quadratic space."""
            ...

        @abstractmethod
        def intersection(self, other: Lattice) -> Lattice:
            """Return the lattice-theoretic intersection inside a common ambient quadratic space."""
            ...

        @abstractmethod
        def sum(self, other: Lattice) -> Lattice:
            """Return the lattice sum inside a common ambient quadratic space."""
            ...

        @abstractmethod
        def primitive_closure(self, *, in_ambient: Lattice | None = None) -> Lattice:
            """Return the primitive closure in the specified ambient integral lattice."""
            ...

        @abstractmethod
        def saturation(self, *, in_ambient: Lattice | None = None) -> Lattice:
            """Return the requested lattice saturation, distinguishing primitive closure from module saturation."""
            ...

        @abstractmethod
        def integral_saturation(self) -> Lattice:
            """Return Sage's integral module saturation after clearing denominators."""
            ...

        @abstractmethod
        def index_in(self, other: Lattice) -> RingElement:
            """Return the finite index of this lattice in ``other`` when defined."""
            ...

        @abstractmethod
        def relative_index(self, other: Lattice) -> RingElement:
            """Return the lattice-theoretic relative index between comparable lattices."""
            ...

        @abstractmethod
        def denominator(self) -> RingElement:
            """Return the denominator of this fractional lattice in its ambient rational span."""
            ...

        @abstractmethod
        def clear_denominators(self) -> Lattice:
            """Return an integral representative obtained by clearing fractional denominators."""
            ...

        @abstractmethod
        def gram_matrix(self, *, basis: str = "user") -> Matrix:
            """Return the Gram matrix in the requested lattice basis convention."""
            ...

        @abstractmethod
        def ambient_gram_matrix(self) -> Matrix:
            """Return the Gram matrix of the ambient quadratic space."""
            ...

        @abstractmethod
        def determinant(self) -> RingElement:
            """Return the determinant of the Gram matrix, not a signed-discriminant convention."""
            ...

        @abstractmethod
        def signed_discriminant(self) -> RingElement:
            """Return Sage's signed discriminant convention for the quadratic module."""
            ...

        @abstractmethod
        def absolute_discriminant(self) -> RingElement:
            """Return the absolute Gram determinant, the expected order of the discriminant group when finite."""
            ...

        @abstractmethod
        def signature_pair(self) -> tuple[Integer, Integer]:
            """Return the positive and negative dimensions of the real quadratic space."""
            ...

        @abstractmethod
        def is_degenerate(self) -> bool:
            """Return whether the lattice form has nonzero radical."""
            ...

        @abstractmethod
        def radical(self) -> Lattice:
            """Return the radical as a category-aware lattice subobject."""
            ...

        @abstractmethod
        def dual(self, *, value_ring: Ring | None = None) -> Lattice:
            """Return the metric dual with respect to the chosen value ring."""
            ...

        @abstractmethod
        def codual(self, *, value_ring: Ring | None = None) -> Lattice:
            """Return the codual lattice determined by the chosen bilinear-value lattice."""
            ...

        @abstractmethod
        def dual_pairing_lattice(self) -> Lattice:
            """Return the lattice carrying the dual pairing data."""
            ...

        @abstractmethod
        def is_self_dual(self, *, value_ring: Ring | None = None) -> bool:
            """Return whether this lattice equals its metric dual for the chosen value ring."""
            ...

        @abstractmethod
        def is_unimodular(self) -> bool:
            """Return whether this lattice has trivial discriminant group."""
            ...

        @abstractmethod
        def quotient_by_sublattice(self, sublattice: Lattice) -> object:
            """Return the quotient by a sublattice, preserving finite quotient structure when present."""
            ...

        @abstractmethod
        def finite_quotient(self, sublattice: Lattice) -> object:
            """Return a finite quotient module or discriminant form when the induced form descends."""
            ...

        @abstractmethod
        def discriminant_group(self) -> DiscriminantGroup:
            """Return the quotient L^vee/L with its induced bilinear or quadratic form."""
            ...

        @abstractmethod
        def quotient_map_to(self, quotient: object) -> LatticeMorphism:
            """Return the quotient map from this lattice to the requested quotient object."""
            ...

        @abstractmethod
        def module_hom(self, images: object, *, codomain: object | None = None) -> object:
            """Return the underlying module homomorphism generated by the given images."""
            ...

        @abstractmethod
        def lattice_hom(self, matrix_or_images: object, *, codomain: Lattice) -> LatticeMorphism:
            """Return a lattice morphism with the specified matrix or generator images."""
            ...

        @abstractmethod
        def isometry(self, matrix_or_images: object, *, codomain: Lattice | None = None) -> LatticeMorphism:
            """Return a form-preserving lattice morphism satisfying F^T G_M F = G_L."""
            ...

        @abstractmethod
        def similarity(self, matrix_or_images: object, multiplier: RingElement, *, codomain: Lattice | None = None) -> LatticeMorphism:
            """Return a lattice similarity satisfying F^T G_M F = multiplier * G_L."""
            ...

        @abstractmethod
        def embedding(self, matrix_or_images: object, *, codomain: Lattice, primitive: bool = False) -> LatticeMorphism:
            """Return a lattice embedding, optionally requiring primitive image."""
            ...

        @abstractmethod
        def underlying_module(self) -> object:
            """Return the raw Sage module surface without promoting its methods to lattice operations."""
            ...

        @abstractmethod
        def underlying_quadratic_module(self) -> object:
            """Return the raw Sage quadratic-module surface when direct Sage access is required."""
            ...

        @abstractmethod
        def underlying_quotient_module(self) -> object:
            """Return the raw Sage quotient-module surface when direct quotient access is required."""
            ...
    class ElementMethods: ...

    HomCategory = LatticeHomCategory

    OverDedekindDomain = LazyImport(
        "category_specs.lattices.subcategories.over_dedekind",
        "_LatticesOverDedekindDomain",
    )
    OverIntegralDomain = LazyImport(
        "category_specs.lattices.subcategories.over_integral_domain",
        "_LatticesOverIntegralDomain",
    )
    OverPID = LazyImport(
        "category_specs.lattices.subcategories.over_pid", "_LatticesOverPID"
    )
    OverIntegers = LazyImport(
        "category_specs.lattices.subcategories.over_integers", "_LatticesOverIntegers"
    )
    Even = LazyImport("category_specs.lattices.subcategories.even", "_EvenLattices")
    Unimodular = LazyImport(
        "category_specs.lattices.subcategories.unimodular", "_UnimodularLattices"
    )
    PositiveDefinite = LazyImport(
        "category_specs.lattices.subcategories.positive_definite",
        "_PositiveDefiniteLattices",
    )

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    CartesianProducts = _CartesianProducts
    DualObjects = LatticeDualObjectsCategory
    DualLatticesCategoryClass = LazyImport(
        "category_specs.lattices.subcategories.constructions.dual_lattices",
        "DualLatticesCategory",
    )
    OverlatticesCategoryClass = LazyImport(
        "category_specs.lattices.subcategories.constructions.overlattices",
        "OverlatticesCategory",
    )
    OrthogonalDirectSumsCategoryClass = LazyImport(
        "category_specs.lattices.subcategories.constructions.orthogonal_direct_sums",
        "OrthogonalDirectSumsCategory",
    )
    DiscriminantGroupsCategoryClass = LazyImport(
        "category_specs.lattices.subcategories.constructions.discriminant_groups",
        "LatticeDiscriminantGroupsCategory",
    )


def _lattice_chain(base_ring: Ring) -> Category:
    r"""Return the immediate ambient category for ``Lattices(base_ring)``."""
    return (
        Modules(base_ring, dispatch=False)
        .Free()
        .FiniteRank()
        .WithForms()
        .Bilinear()
        .Symmetric()
        .Nondegenerate()
        .Integral()
    )


def lattice_category(base_ring: Ring) -> LatticesCategory:
    r"""Return ``Lattices(base_ring)`` as the named lattice axiom endpoint."""
    return _lattice_chain(base_ring).Lattice()


def Lattices(base_ring: Ring) -> LatticesCategory:
    r"""Return the named lattice axiom category over ``base_ring``."""
    return lattice_category(base_ring)


type LatticesObject = LatticesCategory.ParentMethods
type LatticesElement = LatticesCategory.ElementMethods
type LatticesMorphism = LatticeHomCategory.ElementMethods
LatticesHomCategory = LatticeHomCategory
LatticesEndCategory = LatticeEndCategory
LatticesAutCategory = LatticeAutCategory
LatticesHom = LatticeHomCategory.ParentMethods
LatticesEnd = LatticeEndCategory.ParentMethods
LatticesAut = LatticeAutCategory.ParentMethods
LatticesEndomorphism = LatticeEndCategory.ElementMethods
LatticesAutomorphism = LatticeAutCategory.ElementMethods
