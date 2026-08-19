r"""Consolidated rational-lattice category adapters over Sage implementations."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final

from sage.categories.category import Category
from sage.matrix.constructor import matrix
from sage.misc.lazy_import import LazyImport
from sage.modules.free_quadratic_module import QuadraticSpace
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from category_specs.cat import CategoryWithAxiom_over_base_ring, Category_over_base_ring
from category_specs.forms.subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory,
)
from category_specs.modules import Modules
from category_specs.utils import refine_category

if TYPE_CHECKING:
    from category_specs.types import Matrix, Ring, RingElement, RModuleElement


def _wrap_lattice(result: Any) -> Any:
    r"""Wrap Sage quadratic-module parents and leave other Sage values untouched."""
    if hasattr(result, "gram_matrix") and hasattr(result, "inner_product_matrix"):
        return ConsolidatedLattice(result)
    return result


def _signature_pair_from_gram(gram: Matrix) -> tuple[int, int]:
    r"""Return the real signature pair of a symmetric rational Gram matrix."""
    from sage.rings.real_double import RDF

    eigenvalues = gram.change_ring(RDF).eigenvalues()
    positive = sum(1 for value in eigenvalues if value > 0)
    negative = sum(1 for value in eigenvalues if value < 0)
    return (positive, negative)


class RationalLatticesCategory(Category_over_base_ring):
    r"""Finite-rank based modules in rational quadratic spaces.

    This category consolidates Sage's integral lattice, free quadratic module,
    and quadratic-space implementations without replacing their concrete
    parent, element, or morphism classes.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"rational lattices over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        return [
            Modules(self.base_ring(), dispatch=False)
            .Free()
            .FiniteRank()
            .WithForms()
            .Bilinear()
            .Symmetric()
            .Rational(),
        ]

    @final
    def __contains__(self, obj: object) -> bool:
        return isinstance(obj, ConsolidatedLattice) and obj.category().is_subcategory(
            self
        )

    class SubcategoryMethods:
        @final
        def Symmetric(self) -> Category:
            return self._with_axiom("Symmetric")

        @final
        def Nondegenerate(self) -> Category:
            return self._with_axiom("Nondegenerate")

        @final
        def Integral(self) -> Category:
            return self._with_axiom("Integral")

        @final
        def Even(self) -> Category:
            return self._with_axiom("Even")

        @final
        def Unimodular(self) -> Category:
            return self._with_axiom("Unimodular")

        @final
        def Definite(self) -> Category:
            return self._with_axiom("Definite")

        @final
        def Indefinite(self) -> Category:
            return self._with_axiom("Indefinite")

        @final
        def PositiveDefinite(self) -> Category:
            return self._with_axiom("PositiveDefinite")

        @final
        def NegativeDefinite(self) -> Category:
            return self._with_axiom("NegativeDefinite")


class _SymmetricRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "Symmetric")


class _NondegenerateRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "Nondegenerate")


class _IntegralRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "Integral")


class _EvenRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "Even")


class _UnimodularRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "Unimodular")


class _DefiniteRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "Definite")


class _IndefiniteRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "Indefinite")


class _PositiveDefiniteRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "PositiveDefinite")


class _NegativeDefiniteRationalLattices(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (RationalLatticesCategory, "NegativeDefinite")


RationalLatticesCategory.Symmetric = LazyImport(
    __name__, "_SymmetricRationalLattices"
)
RationalLatticesCategory.Nondegenerate = LazyImport(
    __name__, "_NondegenerateRationalLattices"
)
RationalLatticesCategory.Integral = LazyImport(__name__, "_IntegralRationalLattices")
RationalLatticesCategory.Even = LazyImport(__name__, "_EvenRationalLattices")
RationalLatticesCategory.Unimodular = LazyImport(
    __name__, "_UnimodularRationalLattices"
)
RationalLatticesCategory.Definite = LazyImport(__name__, "_DefiniteRationalLattices")
RationalLatticesCategory.Indefinite = LazyImport(
    __name__, "_IndefiniteRationalLattices"
)
RationalLatticesCategory.PositiveDefinite = LazyImport(
    __name__, "_PositiveDefiniteRationalLattices"
)
RationalLatticesCategory.NegativeDefinite = LazyImport(
    __name__, "_NegativeDefiniteRationalLattices"
)


class DiscriminantGroupsCategory(TorsionQuadraticModulesCategory):
    r"""Finite quadratic modules used as lattice discriminant groups."""

    @final
    def _repr_object_names(self) -> str:
        return f"discriminant groups over {self.base_ring()}"

    @final
    def __contains__(self, obj: object) -> bool:
        return all(hasattr(obj, name) for name in ("V", "W", "gram_matrix_quadratic"))

    class ParentMethods:
        @final
        def is_discriminant_group(self) -> bool:
            return True

    class SubcategoryMethods:
        @final
        def FiniteBilinearForms(self) -> Category:
            return self._with_axiom("FiniteBilinearForms")

        @final
        def FiniteQuadraticForms(self) -> Category:
            return self._with_axiom("FiniteQuadraticForms")

        @final
        def Even(self) -> Category:
            return self._with_axiom("Even")

        @final
        def WithSourceLattice(self) -> Category:
            return self._with_axiom("WithSourceLattice")


class _FiniteBilinearDiscriminantGroups(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (
        DiscriminantGroupsCategory,
        "FiniteBilinearForms",
    )


class _FiniteQuadraticDiscriminantGroups(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (
        DiscriminantGroupsCategory,
        "FiniteQuadraticForms",
    )


class _EvenDiscriminantGroups(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (DiscriminantGroupsCategory, "Even")


class _WithSourceLatticeDiscriminantGroups(CategoryWithAxiom_over_base_ring):
    _base_category_class_and_axiom = (
        DiscriminantGroupsCategory,
        "WithSourceLattice",
    )


DiscriminantGroupsCategory.FiniteBilinearForms = LazyImport(
    __name__, "_FiniteBilinearDiscriminantGroups"
)
DiscriminantGroupsCategory.FiniteQuadraticForms = LazyImport(
    __name__, "_FiniteQuadraticDiscriminantGroups"
)
DiscriminantGroupsCategory.Even = LazyImport(__name__, "_EvenDiscriminantGroups")
DiscriminantGroupsCategory.WithSourceLattice = LazyImport(
    __name__, "_WithSourceLatticeDiscriminantGroups"
)


class LatticeHomset:
    r"""Form-preserving maps built by Sage's ``FreeModuleHomspace``."""

    @final
    def __init__(
        self,
        domain: ConsolidatedLattice,
        codomain: ConsolidatedLattice,
    ) -> None:
        self._domain = domain
        self._codomain = codomain
        self._sage_homset = domain.sage_object().Hom(codomain.sage_object())

    @final
    def domain(self) -> ConsolidatedLattice:
        return self._domain

    @final
    def codomain(self) -> ConsolidatedLattice:
        return self._codomain

    @final
    def sage_homset(self) -> object:
        return self._sage_homset

    @final
    def __call__(self, data: object, **kwds: object) -> object:
        morphism = self._sage_homset(data, **kwds)
        if not self._preserves_form(morphism):
            raise ValueError("lattice morphisms must preserve the bilinear form")
        return morphism

    @final
    def identity(self) -> object:
        return self(self._sage_homset.identity())

    @final
    def _preserves_form(self, morphism: object) -> bool:
        matrix_data = morphism.matrix()
        domain_gram = self.domain().gram_matrix()
        codomain_gram = self.codomain().gram_matrix()
        return matrix_data * codomain_gram * matrix_data.transpose() == domain_gram


class ConsolidatedLattice:
    r"""Category-aware adapter over Sage quadratic-module parents."""

    @final
    def __init__(self, sage_parent: object) -> None:
        self._sage_parent = sage_parent

    @final
    def sage_object(self) -> object:
        return self._sage_parent

    @final
    def __getattr__(self, name: str) -> object:
        return getattr(self._sage_parent, name)

    @final
    def __repr__(self) -> str:
        return repr(self._sage_parent)

    @final
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ConsolidatedLattice):
            return False
        return bool(self.sage_object() == other.sage_object())

    @final
    def __contains__(self, element: object) -> bool:
        return element in self._sage_parent

    @final
    def __call__(self, data: object) -> object:
        return self._sage_parent(data)

    @final
    def category(self) -> Category:
        category = RationalLattices(self.base_ring()).Symmetric()
        if self.is_nondegenerate():
            category = category.Nondegenerate()
        if self.is_integral():
            category = category.Integral()
        if self.is_even():
            category = category.Even()
        if self.is_unimodular():
            category = category.Unimodular()
        positive, negative = self.signature_pair()
        if positive == 0 or negative == 0:
            category = category.Definite()
            if negative == 0:
                category = category.PositiveDefinite()
            if positive == 0:
                category = category.NegativeDefinite()
        else:
            category = category.Indefinite()
        return category

    @final
    def value_ring(self) -> Ring:
        return QQ

    @final
    def ambient_space(self) -> object:
        return self._sage_parent.ambient_vector_space()

    @final
    def rational_span(self) -> ConsolidatedLattice:
        return ConsolidatedLattice(self._sage_parent.vector_space())

    @final
    def bilinear_form(self) -> object:
        return self.inner_product_matrix()

    @final
    def is_rational_lattice(self) -> bool:
        return True

    @final
    def is_symmetric(self) -> bool:
        gram = self.gram_matrix()
        return bool(gram == gram.transpose())

    @final
    def is_nondegenerate(self) -> bool:
        return bool(self.determinant() != 0)

    @final
    def is_integral(self) -> bool:
        return bool(self.gram_matrix().denominator() == 1)

    @final
    def is_even(self) -> bool:
        if not self.is_integral():
            return False
        return all(entry in 2 * ZZ for entry in self.gram_matrix().diagonal())

    @final
    def is_unimodular(self) -> bool:
        return bool(self.is_integral() and abs(self.determinant()) == 1)

    @final
    def signature_pair(self) -> tuple[int, int]:
        if hasattr(self._sage_parent, "signature_pair"):
            return self._sage_parent.signature_pair()
        return _signature_pair_from_gram(self.gram_matrix())

    @final
    def signature(self) -> int:
        positive, negative = self.signature_pair()
        return positive - negative

    @final
    def dual(self) -> ConsolidatedLattice:
        dual_basis = self.gram_matrix().inverse() * self.basis_matrix()
        return ConsolidatedLattice(self._sage_parent.span(dual_basis))

    @final
    def change_ring(self, ring: Ring) -> ConsolidatedLattice:
        return ConsolidatedLattice(self._sage_parent.change_ring(ring))

    @final
    def scale_basis(self, scalar: RingElement) -> ConsolidatedLattice:
        return ConsolidatedLattice(scalar * self._sage_parent)

    @final
    def twist(self, scalar: RingElement) -> ConsolidatedLattice:
        return ConsolidatedLattice(self._sage_parent.twist(scalar))

    @final
    def sublattice(
        self,
        gens: Sequence[RModuleElement],
        check_integral: bool = True,
    ) -> ConsolidatedLattice:
        return ConsolidatedLattice(self._sage_parent.sublattice(gens))

    @final
    def overlattice(
        self,
        gens: Sequence[RModuleElement],
        check_integral: bool = True,
    ) -> ConsolidatedLattice:
        return ConsolidatedLattice(self._sage_parent.overlattice(gens))

    @final
    def span(self, gens: Sequence[RModuleElement], **kwds: object) -> Any:
        return _wrap_lattice(self._sage_parent.span(gens, **kwds))

    @final
    def span_of_basis(self, basis: Sequence[RModuleElement], **kwds: object) -> Any:
        return _wrap_lattice(self._sage_parent.span_of_basis(basis, **kwds))

    @final
    def intersection(self, other: ConsolidatedLattice) -> Any:
        return _wrap_lattice(self._sage_parent.intersection(other.sage_object()))

    @final
    def sum(self, other: ConsolidatedLattice) -> Any:
        return _wrap_lattice(self._sage_parent + other.sage_object())

    @final
    def direct_sum(self, other: ConsolidatedLattice, **kwds: object) -> Any:
        return _wrap_lattice(self._sage_parent.direct_sum(other.sage_object(), **kwds))

    @final
    def hom(self, codomain: ConsolidatedLattice) -> LatticeHomset:
        return LatticeHomset(self, codomain)

    @final
    def discriminant_group(self, primary: int = 0) -> object:
        return refine_category(
            self._sage_parent.discriminant_group(primary),
            DiscriminantGroups(ZZ),
            test=False,
        )


def RationalLattices(base_ring: Ring) -> RationalLatticesCategory:
    r"""Return consolidated rational lattices over ``base_ring``."""
    return RationalLatticesCategory(base_ring)


def DiscriminantGroups(base_ring: Ring = ZZ) -> DiscriminantGroupsCategory:
    r"""Return finite quadratic modules used as discriminant groups."""
    return DiscriminantGroupsCategory(base_ring)


def from_sage(sage_parent: object) -> ConsolidatedLattice:
    r"""Wrap an existing Sage quadratic-module parent as a consolidated lattice."""
    return ConsolidatedLattice(sage_parent)


def Lattice(
    data: object,
    *,
    base_ring: Ring = ZZ,
    integral: bool = True,
    basis: object | None = None,
) -> ConsolidatedLattice:
    r"""Construct a consolidated lattice using Sage's reference constructors."""
    if isinstance(data, ConsolidatedLattice):
        return data
    if hasattr(data, "gram_matrix") and hasattr(data, "inner_product_matrix"):
        return ConsolidatedLattice(data)
    if base_ring == ZZ and integral:
        return ConsolidatedLattice(IntegralLattice(data, basis=basis))
    if base_ring == QQ:
        gram = matrix(QQ, data)
        quadratic_space = QuadraticSpace(QQ, gram.nrows(), gram)
        if basis is None:
            return ConsolidatedLattice(quadratic_space)
        return ConsolidatedLattice(quadratic_space.span(basis))
    raise ValueError("nonintegral ZZ lattices must be built from an existing Sage parent")
