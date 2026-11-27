r"""Consolidated rational-lattice category adapters over Sage implementations."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final

from category_specs.cat import Category_over_base_ring, CategoryWithAxiom_over_base_ring
from category_specs.forms.subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory,
)
from category_specs.modules import Modules
from category_specs.utils import refine_category
from sage.categories.category import Category
from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
from sage.groups.additive_abelian.additive_abelian_wrapper import AdditiveAbelianGroupWrapper
from sage.matrix.constructor import matrix
from sage.misc.lazy_import import LazyImport
from sage.modules.free_quadratic_module import QuadraticSpace
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from src.sage_patches import module_operations

module_operations.install()

if TYPE_CHECKING:
    from category_specs.types import Matrix, Ring, RingElement, RModuleElement

_POSITIVE_DEFINITE_ALGORITHMS = {
    "LLL",
    "BKZ",
    "approximate_closest_vector",
    "basis_of_short_vectors",
    "enumerate_short_vectors",
    "minimum",
    "short_vectors",
    "short_vectors_up_to_sign",
    "short_vector_list_up_to_length",
    "shortest_vector",
    "closest_vector",
    "voronoi_cell",
}

_RAW_MODULE_METHODS_NOT_PROMOTED = {
    "dense_module",
    "free_resolution",
    "graded_free_resolution",
    "pseudoHom",
    "pseudohom",
    "quotient_abstract",
    "sparse_module",
    "subspaces",
}

_FINITE_CONTEXT_METHODS_NOT_PROMOTED_ON_LATTICES = {
    "all_submodules",
    "list",
    "orthogonal_submodule_to",
    "primary_part",
    "random_element",
}


def _wrap_lattice(result: Any) -> Any:
    r"""Wrap Sage quadratic-module parents and leave other Sage values untouched."""
    if hasattr(result, "gram_matrix") and hasattr(result, "inner_product_matrix"):
        return ConsolidatedLattice(result)
    return result


def _wrap_span_with_form(result: Any, ambient_gram: Matrix) -> ConsolidatedLattice:
    r"""Wrap a Sage module span with the induced ambient quadratic form."""
    wrapped = _wrap_lattice(result)
    if isinstance(wrapped, ConsolidatedLattice):
        return wrapped
    assert hasattr(result, "basis_matrix")
    basis = result.basis_matrix()
    return ConsolidatedLattice(_quadratic_space_from_gram(basis * ambient_gram * basis.transpose()))


def _sage_object(obj: object) -> object:
    r"""Return the wrapped Sage object when ``obj`` is one of this module's adapters."""
    if hasattr(obj, "sage_object"):
        return obj.sage_object()
    return obj


def _apply_lattice_isometry(g: object, v: object) -> object:
    r"""Apply a supplied lattice isometry represented as a morphism, callable, or matrix."""
    if callable(g):
        return g(v)
    if hasattr(g, "matrix"):
        return g.matrix() * v
    return g * v


def _bilinear_value(lattice: object, x: object, y: object) -> object:
    r"""Evaluate the bilinear form using Sage's native operation when exposed."""
    lattice_object = _sage_object(lattice)
    if hasattr(lattice_object, "inner_product"):
        return lattice_object.inner_product(x, y)
    return x * y


def _signature_pair_from_gram(gram: Matrix) -> tuple[int, int]:
    r"""Return the real signature pair of a symmetric rational Gram matrix."""
    eigenvalues = gram.change_ring(QQ).eigenvalues()
    positive = sum(1 for value in eigenvalues if value > 0)
    negative = sum(1 for value in eigenvalues if value < 0)
    return (positive, negative)


def _quadratic_space_from_gram(gram: Matrix) -> Any:
    r"""Return a Sage rational quadratic space with the supplied Gram matrix."""
    return QuadraticSpace(QQ, gram.nrows(), gram)


def _assert_requested_lattice_properties(
    lattice: object,
    *,
    check_integral: bool | None = None,
    check_even: bool | None = None,
) -> None:
    r"""Fail loudly when a requested lattice-category property is not satisfied."""
    if check_integral is True:
        assert hasattr(lattice, "is_integral")
        if not lattice.is_integral():
            raise ValueError("generated lattice is not integral")
    if check_even is True:
        assert hasattr(lattice, "is_even")
        if not lattice.is_even():
            raise ValueError("generated lattice is not even")


def _elementary_divisors_from_invariants(invariants: Sequence[object]) -> tuple[object, ...]:
    r"""Return prime-power elementary divisors determined by invariant factors."""
    divisors = []
    for invariant in invariants:
        if invariant == 0:
            divisors.append(invariant)
            continue
        if invariant == 1:
            continue
        for prime, exponent in ZZ(invariant).factor():
            divisors.append(prime**exponent)
    divisors.sort()
    return tuple(divisors)


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
            Modules(self.base_ring(), dispatch=False).Free().FiniteRank().WithForms().Bilinear().Symmetric().Rational(),
        ]

    @final
    def __contains__(self, obj: object) -> bool:
        return isinstance(obj, ConsolidatedLattice) and obj.category().is_subcategory(self)

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


RationalLatticesCategory.Symmetric = LazyImport(__name__, "_SymmetricRationalLattices")
RationalLatticesCategory.Nondegenerate = LazyImport(__name__, "_NondegenerateRationalLattices")
RationalLatticesCategory.Integral = LazyImport(__name__, "_IntegralRationalLattices")
RationalLatticesCategory.Even = LazyImport(__name__, "_EvenRationalLattices")
RationalLatticesCategory.Unimodular = LazyImport(__name__, "_UnimodularRationalLattices")
RationalLatticesCategory.Definite = LazyImport(__name__, "_DefiniteRationalLattices")
RationalLatticesCategory.Indefinite = LazyImport(__name__, "_IndefiniteRationalLattices")
RationalLatticesCategory.PositiveDefinite = LazyImport(__name__, "_PositiveDefiniteRationalLattices")
RationalLatticesCategory.NegativeDefinite = LazyImport(__name__, "_NegativeDefiniteRationalLattices")


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


DiscriminantGroupsCategory.FiniteBilinearForms = LazyImport(__name__, "_FiniteBilinearDiscriminantGroups")
DiscriminantGroupsCategory.FiniteQuadraticForms = LazyImport(__name__, "_FiniteQuadraticDiscriminantGroups")
DiscriminantGroupsCategory.Even = LazyImport(__name__, "_EvenDiscriminantGroups")
DiscriminantGroupsCategory.WithSourceLattice = LazyImport(__name__, "_WithSourceLatticeDiscriminantGroups")


class LatticeMorphismAdapter:
    r"""Form-preserving lattice morphism backed by Sage's module-hom machinery."""

    @final
    def __init__(
        self,
        sage_morphism: object,
        domain: ConsolidatedLattice,
        codomain: ConsolidatedLattice,
    ) -> None:
        self._sage_morphism = sage_morphism
        self._domain = domain
        self._codomain = codomain

    @final
    def sage_object(self) -> object:
        return self._sage_morphism

    @final
    def __getattr__(self, name: str) -> object:
        return getattr(self._sage_morphism, name)

    @final
    def __call__(self, x: object) -> object:
        return self._sage_morphism(x)

    @final
    def domain(self) -> ConsolidatedLattice:
        return self._domain

    @final
    def codomain(self) -> ConsolidatedLattice:
        return self._codomain

    @final
    def matrix(self) -> Matrix:
        return self._sage_morphism.matrix()

    @final
    def kernel(self) -> object:
        return _wrap_lattice(self._sage_morphism.kernel())

    @final
    def image(self) -> object:
        return _wrap_lattice(self._sage_morphism.image())

    @final
    def lift(self, x: object) -> object:
        return self._sage_morphism.lift(x)

    @final
    def im_gens(self) -> object:
        return self._sage_morphism.im_gens()

    @final
    def restriction_to_sublattice(self, sublattice: ConsolidatedLattice) -> LatticeMorphismAdapter:
        assert hasattr(self._sage_morphism, "restrict_domain")
        restricted_domain = _wrap_lattice(_sage_object(sublattice))
        assert isinstance(restricted_domain, ConsolidatedLattice)
        restricted = self._sage_morphism.restrict_domain(restricted_domain.sage_object())
        return LatticeMorphismAdapter(restricted, restricted_domain, self.codomain())

    @final
    def induced_map_on_quotient(
        self,
        domain_relation: ConsolidatedLattice,
        codomain_relation: ConsolidatedLattice,
    ) -> object:
        domain_quotient = self.domain().quotient_by_sublattice(domain_relation)
        codomain_quotient = self.codomain().quotient_by_sublattice(codomain_relation)
        images = [codomain_quotient.sage_object()(self._sage_morphism(generator.lift())) for generator in domain_quotient.sage_object().gens()]
        return domain_quotient.sage_object().hom(
            images,
            codomain=codomain_quotient.sage_object(),
        )

    @final
    def induced_map_on_discriminant_group(self) -> object:
        domain_group = self.domain().discriminant_group()
        codomain_group = self.codomain().discriminant_group()

        def induced(x: object) -> object:
            return codomain_group.project_from_dual(self._sage_morphism(domain_group.lift_to_dual(x)))

        return induced

    @final
    def kernel_on_discriminant_group(self) -> object:
        domain_group = self.domain().discriminant_group()
        induced = self.induced_map_on_discriminant_group()
        zero = self.codomain().discriminant_group().zero()
        return domain_group.subgroup([x for x in domain_group if induced(x) == zero])


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
        return LatticeMorphismAdapter(morphism, self.domain(), self.codomain())

    @final
    def identity(self) -> object:
        return LatticeMorphismAdapter(
            self._sage_homset.identity(),
            self.domain(),
            self.codomain(),
        )

    @final
    def _preserves_form(self, morphism: object) -> bool:
        matrix_data = morphism.matrix()
        domain_gram = self.domain().gram_matrix()
        codomain_gram = self.codomain().gram_matrix()
        return matrix_data.transpose() * codomain_gram * matrix_data == domain_gram


class TransportedFiniteForm:
    r"""Finite bilinear/quadratic form transported along a supplied morphism."""

    @final
    def __init__(self, source: object, phi: object, *, direction: str) -> None:
        assert direction in {"pullback", "pushforward"}
        self._source = source
        self._phi = phi
        self._direction = direction

    @final
    def _pull(self, x: object) -> object:
        if self._direction == "pullback":
            return self._phi(x)
        return self._phi.lift(x)

    @final
    def b(self, x: object, y: object) -> object:
        return self._source.b(self._pull(x), self._pull(y))

    @final
    def q(self, x: object) -> object:
        return self._source.q(self._pull(x))


class LatticeQuotientAdapter:
    r"""Source-aware adapter over Sage FGP quotient modules from lattice quotients."""

    @final
    def __init__(
        self,
        sage_parent: object,
        cover_lattice: ConsolidatedLattice,
        relation_lattice: ConsolidatedLattice,
    ) -> None:
        self._sage_parent = sage_parent
        self._cover_lattice = cover_lattice
        self._relation_lattice = relation_lattice

    @final
    def sage_object(self) -> object:
        return self._sage_parent

    @final
    def __getattr__(self, name: str) -> object:
        if name in _RAW_MODULE_METHODS_NOT_PROMOTED:
            raise AttributeError(f"{name} is a raw Sage module method, not a promoted lattice quotient operation; use underlying_quotient_module() explicitly")
        return getattr(self._sage_parent, name)

    @final
    def __repr__(self) -> str:
        return repr(self._sage_parent)

    @final
    def __iter__(self) -> object:
        return iter(self._sage_parent)

    @final
    def __contains__(self, element: object) -> bool:
        return element in self._sage_parent

    @final
    def __call__(self, data: object) -> object:
        return self._sage_parent(data)

    @final
    def cover_lattice(self) -> ConsolidatedLattice:
        return self._cover_lattice

    @final
    def relation_lattice(self) -> ConsolidatedLattice:
        return self._relation_lattice

    @final
    def cover(self) -> ConsolidatedLattice:
        return self.cover_lattice()

    @final
    def relations(self) -> ConsolidatedLattice:
        return self.relation_lattice()

    @final
    def quotient_map(self) -> object:
        return self._sage_parent.quotient_map()

    @final
    def invariant_factors(self) -> tuple[object, ...]:
        return tuple(self._sage_parent.invariants())

    @final
    def elementary_divisors(self) -> tuple[object, ...]:
        return _elementary_divisors_from_invariants(self.invariant_factors())

    @final
    def smith_generators(self) -> tuple[object, ...]:
        return tuple(self._sage_parent.smith_form_gens())

    @final
    def coordinates_in_smith_basis(self, x: object) -> object:
        if hasattr(self._sage_parent, "coordinate_vector"):
            return self._sage_parent.coordinate_vector(x)
        return self._sage_parent.gens_vector(x)

    @final
    def coordinates_in_generators(self, x: object, *, reduce: bool = True) -> object:
        return self._sage_parent.gens_vector(x, reduce=reduce)

    @final
    def generator_relations(self) -> object:
        return self._sage_parent.W()

    @final
    def lift(self, x: object) -> object:
        return self._sage_parent.lift(x)

    @final
    def form_descends(self) -> bool:
        cover_basis = self.cover_lattice().basis()
        relation_basis = self.relation_lattice().basis()
        return all(_bilinear_value(self.cover_lattice(), relation_vector, cover_vector) in ZZ for relation_vector in relation_basis for cover_vector in cover_basis) and all(
            _bilinear_value(self.cover_lattice(), relation_vector, relation_vector) / 2 in ZZ for relation_vector in relation_basis
        )

    @final
    def b(self, x: object, y: object) -> object:
        assert self.form_descends()
        return _bilinear_value(self.cover_lattice(), self.lift(x), self.lift(y))

    @final
    def q(self, x: object) -> object:
        assert self.form_descends()
        lift = self.lift(x)
        return _bilinear_value(self.cover_lattice(), lift, lift) / 2

    @final
    def discriminant_form_when_descends(self) -> LatticeQuotientAdapter:
        if not self.form_descends():
            raise ValueError("the lattice form does not descend to this quotient")
        return self

    @final
    def underlying_quotient_module(self) -> object:
        return self._sage_parent


class DiscriminantGroupAdapter:
    r"""Source-aware adapter over Sage ``TorsionQuadraticModule`` objects."""

    @final
    def __init__(
        self,
        sage_parent: object,
        source_lattice: ConsolidatedLattice,
    ) -> None:
        self._sage_parent = sage_parent
        self._source_lattice = source_lattice

    @final
    def sage_object(self) -> object:
        return self._sage_parent

    @final
    def __getattr__(self, name: str) -> object:
        if name in _RAW_MODULE_METHODS_NOT_PROMOTED:
            raise AttributeError(f"{name} is a raw Sage module method, not a promoted lattice operation; use underlying_module() or underlying_quadratic_module() explicitly")
        if name in _POSITIVE_DEFINITE_ALGORITHMS:
            raise AttributeError(f"{name} is a positive-definite lattice algorithm, not a discriminant-group operation")
        return getattr(self._sage_parent, name)

    @final
    def __repr__(self) -> str:
        return repr(self._sage_parent)

    @final
    def __iter__(self) -> object:
        return iter(self._sage_parent)

    @final
    def __contains__(self, element: object) -> bool:
        return element in self._sage_parent

    @final
    def __call__(self, data: object) -> object:
        return self._sage_parent(data)

    @final
    def source_lattice(self) -> ConsolidatedLattice:
        return self._source_lattice

    @final
    def relation_lattice(self) -> ConsolidatedLattice:
        return self.source_lattice()

    @final
    def metric_dual(self) -> ConsolidatedLattice:
        return self.source_lattice().dual()

    @final
    def dual_lattice(self) -> ConsolidatedLattice:
        return self.metric_dual()

    @final
    def cover_lattice(self) -> ConsolidatedLattice:
        return self.metric_dual()

    @final
    def order(self) -> object:
        return self.cardinality()

    @final
    def is_trivial(self) -> bool:
        return bool(self.order() == 1)

    @final
    def exponent(self) -> object:
        exponent = ZZ.one()
        for invariant in self.invariants():
            if invariant:
                exponent = exponent.lcm(invariant)
        return exponent

    @final
    def is_cyclic(self) -> bool:
        return sum(1 for invariant in self.invariants() if invariant not in (0, 1)) <= 1

    @final
    def short_name(self) -> str:
        invariants = tuple(invariant for invariant in self.invariants() if invariant not in (0, 1))
        if not invariants:
            return "0"
        return " x ".join(f"C{invariant}" for invariant in invariants)

    @final
    def zero(self) -> object:
        if hasattr(self._sage_parent, "zero"):
            return self._sage_parent.zero()
        return self._sage_parent(0)

    @final
    def identity(self) -> object:
        return self.zero()

    @final
    def invariant_factors(self) -> tuple[object, ...]:
        return tuple(self.invariants())

    @final
    def elementary_divisors(self) -> tuple[object, ...]:
        return _elementary_divisors_from_invariants(self.invariant_factors())

    @final
    def generator_orders(self) -> tuple[object, ...]:
        return tuple(generator.additive_order() for generator in self.gens())

    @final
    def rank_p(self, p: object) -> int:
        return sum(1 for invariant in self.invariants() if invariant % p == 0)

    @final
    def length_p(self, p: object) -> int:
        return len(self.primary_part(p).invariants())

    @final
    def smith_generators(self) -> tuple[object, ...]:
        return tuple(self.smith_form_gens())

    @final
    def coordinates(
        self,
        x: object,
        gens: Sequence[object] | None = None,
        *,
        reduce: bool = True,
    ) -> object:
        if gens is None:
            return self._sage_parent.gens_vector(x, reduce=reduce)
        return AdditiveAbelianGroupWrapper.from_generators(gens, universe=self._sage_parent).discrete_log(x)

    @final
    def discrete_log(
        self,
        x: object,
        gens: Sequence[object] | None = None,
    ) -> object:
        return self.coordinates(x, gens=gens)

    @final
    def discrete_exp(
        self,
        v: Sequence[object],
        gens: Sequence[object] | None = None,
    ) -> object:
        if gens is None:
            return self._sage_parent.linear_combination_of_smith_form_gens(v)
        return AdditiveAbelianGroupWrapper.from_generators(gens, universe=self._sage_parent).discrete_exp(v)

    @final
    def as_additive_abelian_group(self) -> object:
        return AdditiveAbelianGroupWrapper.from_generators(self.gens(), universe=self._sage_parent)

    @final
    def underlying_abelian_group(self) -> object:
        return self.as_additive_abelian_group()

    @final
    def underlying_quotient_module(self) -> object:
        return self._sage_parent

    @final
    def relations_among(self, gens: Sequence[object]) -> object:
        return AdditiveAbelianGroupWrapper.from_generators(gens, universe=self._sage_parent).W()

    @final
    def basis_from_generators(self, gens: Sequence[object]) -> object:
        return AdditiveAbelianGroupWrapper.from_generators(gens, universe=self._sage_parent).gens()

    @final
    def from_generators(self, gens: Sequence[object]) -> object:
        return self.subgroup(gens)

    @final
    def subgroup(self, gens: Sequence[object]) -> object:
        return self._sage_parent.submodule_with_gens(gens)

    @final
    def subgroup_generated_by(self, gens: Sequence[object]) -> object:
        return self.subgroup(gens)

    @final
    def subgroups(self) -> object:
        return self._sage_parent.all_submodules()

    @final
    def all_subgroups(self) -> object:
        return self.subgroups()

    @final
    def contains_subgroup(self, H: object) -> bool:
        return bool(_sage_object(H).is_submodule(self._sage_parent))

    @final
    def quotient_group(self, H: object) -> object:
        return self._sage_parent.quotient(_sage_object(H))

    @final
    def quotient(self, H: object) -> object:
        return self.quotient_group(H)

    @final
    def quotient_map(self, H: object) -> object:
        quotient = self.quotient_group(H)
        if hasattr(quotient, "quotient_map"):
            return quotient.quotient_map()
        raise NotImplementedError("Sage quotient did not expose a quotient_map")

    @final
    def cosets(self, H: object) -> object:
        quotient = self.quotient_group(H)
        if hasattr(quotient, "list"):
            return quotient.list()
        return list(quotient)

    @final
    def primary_decomposition(self) -> tuple[object, ...]:
        return tuple(self.primary_part(p) for p, _ in self.exponent().factor())

    @final
    def primary_parts(self) -> tuple[object, ...]:
        return self.primary_decomposition()

    @final
    def p_torsion(self, p: object, *, k: int = 1) -> object:
        return self.subgroup([x for x in self._sage_parent if (p**k) * x == self.zero()])

    @final
    def p_primary_part(self, p: object) -> object:
        return self.primary_part(p)

    @final
    def torsion_subgroup(self) -> DiscriminantGroupAdapter:
        return self

    @final
    def automorphism_group(self) -> object:
        return AbelianGroupGap([invariant for invariant in self.invariants() if invariant != 1]).automorphism_group()

    @final
    def q(self, x: object) -> object:
        return x.q()

    @final
    def b(self, x: object, y: object) -> object:
        return x * y

    @final
    def is_isotropic_element(self, x: object) -> bool:
        return bool(self.q(x) == 0)

    @final
    def isotropic_elements(self) -> tuple[object, ...]:
        return tuple(x for x in self._sage_parent if self.is_isotropic_element(x))

    @final
    def is_isotropic_subgroup(self, H: object) -> bool:
        return all(self.is_isotropic_element(x) for x in _sage_object(H))

    @final
    def is_totally_isotropic(self, H: object) -> bool:
        return self.is_isotropic_subgroup(H)

    @final
    def orthogonal(self, H: object) -> object:
        return self._sage_parent.orthogonal_submodule_to(_sage_object(H))

    @final
    def orthogonal_complement(self, H: object) -> object:
        return self.orthogonal(H)

    @final
    def isotropic_subgroups(self) -> tuple[object, ...]:
        return tuple(H for H in self.subgroups() if self.is_isotropic_subgroup(H))

    @final
    def is_lagrangian(self, H: object) -> bool:
        return bool(self.orthogonal(H) == _sage_object(H))

    @final
    def lagrangian_subgroups(self) -> tuple[object, ...]:
        return tuple(H for H in self.isotropic_subgroups() if self.is_lagrangian(H))

    @final
    def metabolizers(self) -> tuple[object, ...]:
        return self.lagrangian_subgroups()

    @final
    def is_metabolic(self) -> bool:
        return bool(self.lagrangian_subgroups())

    @final
    def is_anisotropic(self) -> bool:
        return all(x == self.zero() for x in self.isotropic_elements())

    @final
    def is_maximal_isotropic(self, H: object) -> bool:
        H0 = _sage_object(H)
        return self.is_isotropic_subgroup(H0) and not any(H0 != K and H0.is_submodule(K) for K in self.isotropic_subgroups())

    @final
    def maximal_isotropic_subgroups(self) -> tuple[object, ...]:
        return tuple(H for H in self.isotropic_subgroups() if self.is_maximal_isotropic(H))

    @final
    def orthogonal_quotient(self, H: object) -> object:
        return self.orthogonal(H).quotient(_sage_object(H))

    @final
    def restricted_form(self, H: object) -> object:
        return _sage_object(H)

    @final
    def pushforward_form(self, phi: object) -> object:
        assert hasattr(phi, "lift")
        return TransportedFiniteForm(self, phi, direction="pushforward")

    @final
    def pullback_form(self, phi: object) -> object:
        assert callable(phi)
        return TransportedFiniteForm(self, phi, direction="pullback")

    @final
    def subquotient_form(self, H: object, K: object) -> object:
        return _sage_object(K).quotient(_sage_object(H))

    @final
    def bilinear_orthogonal_group(self) -> object:
        return self._sage_parent.orthogonal_group(kind="bilinear")

    @final
    def quadratic_orthogonal_group(self) -> object:
        return self._sage_parent.orthogonal_group(kind="quadratic")

    @final
    def isometry_group(self) -> object:
        return self.quadratic_orthogonal_group()

    @final
    def isometry_to(self, other: object, *, kind: str = "quadratic") -> object:
        raise NotImplementedError("Sage does not expose a direct torsion-quadratic isometry_to constructor")

    @final
    def is_isomorphic_to(self, other: object, *, kind: str = "quadratic") -> bool:
        other_obj = _sage_object(other)
        if kind == "group":
            return self.invariant_factors() == tuple(other_obj.invariants())
        if kind == "bilinear":
            raise NotImplementedError("Sage does not expose bilinear finite-form isomorphism here")
        if kind != "quadratic":
            raise ValueError("is_isomorphic_to kind must be 'group', 'bilinear', or 'quadratic'")
        if hasattr(self._sage_parent, "normal_form") and hasattr(other_obj, "normal_form"):
            return bool(self._sage_parent.normal_form() == other_obj.normal_form())
        return bool(self._sage_parent == other_obj)

    @final
    def normal_form(self, *, partial: bool = False, return_isometry: bool = False) -> object:
        if return_isometry:
            raise NotImplementedError("Sage normal_form does not return an isometry on this adapter path")
        return self._sage_parent.normal_form(partial=partial)

    @final
    def character_group(self) -> object:
        return AbelianGroupGap([invariant for invariant in self.invariants() if invariant != 1])

    @final
    def pontryagin_dual(self) -> object:
        return self.character_group()

    @final
    def pairing_character(self, x: object) -> object:
        return lambda y: self.b(x, y)

    @final
    def pairing_isomorphism_to_dual(self) -> object:
        if not self.is_nondegenerate():
            raise ValueError("the pairing map is an isomorphism only for nondegenerate pairings")
        return self.pairing_character

    @final
    def annihilator_subgroup(self, H: object) -> object:
        return self.orthogonal(H)

    @final
    def radical(self) -> object:
        return self.left_kernel()

    @final
    def left_kernel(self) -> object:
        return self.subgroup([x for x in self._sage_parent if all(self.b(x, y) == 0 for y in self._sage_parent)])

    @final
    def right_kernel(self) -> object:
        return self.subgroup([y for y in self._sage_parent if all(self.b(x, y) == 0 for x in self._sage_parent)])

    @final
    def is_nondegenerate(self) -> bool:
        return bool(self.left_kernel().cardinality() == 1 and self.right_kernel().cardinality() == 1)

    @final
    def lift_to_dual(self, x: object) -> object:
        return x.lift()

    @final
    def project_from_dual(self, v: object) -> object:
        return self._sage_parent(v)

    @final
    def coset_representative(self, x: object) -> object:
        return self.lift_to_dual(x)

    @final
    def preimage_lattice(self, H: object) -> ConsolidatedLattice:
        return self.source_lattice().overlattice([self.lift_to_dual(x) for x in _sage_object(H)])

    @final
    def overlattice_from_isotropic_subgroup(self, H: object) -> ConsolidatedLattice:
        if not self.is_isotropic_subgroup(H):
            raise ValueError("overlattice subgroups must be isotropic")
        return self.preimage_lattice(H)

    @final
    def discriminant_form_of_overlattice(self, H: object) -> object:
        return self.overlattice_from_isotropic_subgroup(H).discriminant_group()

    @final
    def action_of_lattice_isometry(self, g: object) -> object:
        def action(x: object) -> object:
            return self.project_from_dual(_apply_lattice_isometry(g, self.lift_to_dual(x)))

        return action

    @final
    def action_of_lattice_group(self, G: object) -> object:
        if hasattr(G, "gens"):
            return self._sage_parent.orthogonal_group(G.gens())
        return self._sage_parent.orthogonal_group(G)

    @final
    def image_of_lattice_group(self, G: object) -> object:
        return self.action_of_lattice_group(G)

    @final
    def _orbit_from_generators(self, x: object, gens: Sequence[object]) -> tuple[object, ...]:
        orbit = [x]
        frontier = [x]
        while frontier:
            current = frontier.pop()
            for generator in gens:
                action = self.action_of_lattice_isometry(generator)
                image = action(current)
                if all(image != known for known in orbit):
                    orbit.append(image)
                    frontier.append(image)
        return tuple(orbit)

    @final
    def _subgroup_orbit_from_generators(self, H: object, gens: Sequence[object]) -> tuple[object, ...]:
        orbit = [H]
        frontier = [H]
        while frontier:
            current = frontier.pop()
            for generator in gens:
                action = self.action_of_lattice_isometry(generator)
                image = self.subgroup([action(x) for x in _sage_object(current)])
                if all(image != known for known in orbit):
                    orbit.append(image)
                    frontier.append(image)
        return tuple(orbit)

    @staticmethod
    def _partition_by_orbit(objects: Sequence[object], orbit_function: object) -> tuple[tuple[object, ...], ...]:
        remaining = list(objects)
        orbits = []
        while remaining:
            orbit = tuple(orbit_function(remaining[0]))
            orbits.append(orbit)
            remaining = [x for x in remaining if all(x != y for y in orbit)]
        return tuple(orbits)

    @final
    def kernel_of_lattice_group_action(self, G: object) -> object:
        action = self.action_of_lattice_group(G)
        if hasattr(action, "kernel"):
            return action.kernel()
        if hasattr(G, "__iter__") and hasattr(G, "subgroup"):
            kernel_elements = [g for g in G if all(self.action_of_lattice_isometry(g)(x) == x for x in self)]
            return G.subgroup(kernel_elements)
        raise NotImplementedError("kernel computation requires a finite iterable group with subgroup construction")

    @final
    def orbit(self, x: object, G: object | None = None) -> object:
        group = self.quadratic_orthogonal_group() if G is None else G
        if hasattr(group, "orbit"):
            return group.orbit(x)
        if hasattr(group, "gens"):
            return self._orbit_from_generators(x, tuple(group.gens()))
        raise NotImplementedError("the supplied group object does not expose orbit computation")

    @final
    def orbits(self, G: object | None = None) -> object:
        group = self.quadratic_orthogonal_group() if G is None else G
        if hasattr(group, "orbits"):
            return group.orbits()
        if hasattr(group, "gens"):
            gens = tuple(group.gens())
            return self._partition_by_orbit(
                tuple(self._sage_parent),
                lambda x: self._orbit_from_generators(x, gens),
            )
        raise NotImplementedError("the supplied group object does not expose orbit computation")

    @final
    def orbits_on_subgroups(self, G: object | None = None) -> object:
        group = self.quadratic_orthogonal_group() if G is None else G
        if hasattr(group, "orbits"):
            return group.orbits(self.subgroups())
        if hasattr(group, "gens"):
            gens = tuple(group.gens())
            return self._partition_by_orbit(
                tuple(self.subgroups()),
                lambda H: self._subgroup_orbit_from_generators(H, gens),
            )
        raise NotImplementedError("the supplied group object does not expose subgroup orbit computation")

    @final
    def orbits_on_isotropic_subgroups(self, G: object | None = None) -> object:
        group = self.quadratic_orthogonal_group() if G is None else G
        if hasattr(group, "orbits"):
            return group.orbits(self.isotropic_subgroups())
        if hasattr(group, "gens"):
            gens = tuple(group.gens())
            return self._partition_by_orbit(
                tuple(self.isotropic_subgroups()),
                lambda H: self._subgroup_orbit_from_generators(H, gens),
            )
        raise NotImplementedError("the supplied group object does not expose isotropic-subgroup orbit computation")


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
    def __getattribute__(self, name: str) -> object:
        if name in _RAW_MODULE_METHODS_NOT_PROMOTED:
            raise AttributeError(f"{name} is a raw Sage module method, not a promoted lattice operation; use underlying_module() or underlying_quadratic_module() explicitly")
        if name in _FINITE_CONTEXT_METHODS_NOT_PROMOTED_ON_LATTICES:
            raise AttributeError(f"{name} is a finite quotient/discriminant-group operation, not a generic lattice operation")
        if name in _POSITIVE_DEFINITE_ALGORITHMS:
            is_positive_definite = object.__getattribute__(self, "is_positive_definite")
            if not is_positive_definite():
                raise AttributeError(f"{name} is only exposed on positive-definite lattice wrappers; use underlying_quadratic_module() for raw Sage access")
        return object.__getattribute__(self, name)

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
        rank = self.gram_matrix().nrows()
        if positive + negative == rank and (positive == 0 or negative == 0):
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
    def ambient_quadratic_space(self) -> object:
        return ConsolidatedLattice(_quadratic_space_from_gram(self.inner_product_matrix()))

    @final
    def rational_span(self) -> ConsolidatedLattice:
        return ConsolidatedLattice(_quadratic_space_from_gram(self.gram_matrix()))

    @final
    def basis_matrix(self, ring: Ring | None = None, *, kind: str = "user") -> Matrix:
        if kind == "user":
            if ring is None:
                return self._sage_parent.basis_matrix()
            return self._sage_parent.basis_matrix(ring)
        if kind == "echelon":
            if hasattr(self._sage_parent, "echelonized_basis_matrix"):
                return self._sage_parent.echelonized_basis_matrix()
            echelonized = self._sage_parent.echelonized_basis()
            return matrix(echelonized)
        raise ValueError("basis kind must be 'user' or 'echelon'")

    @final
    def coordinates(self, x: RModuleElement, *, basis: str = "user") -> object:
        if basis == "user":
            return self._sage_parent.coordinate_vector(x)
        if basis == "echelon":
            if hasattr(self._sage_parent, "echelon_coordinate_vector"):
                return self._sage_parent.echelon_coordinate_vector(x)
            return self._sage_parent.echelon_coordinates(x)
        raise ValueError("basis must be 'user' or 'echelon'")

    @final
    def ambient_coordinates(self, x: RModuleElement) -> object:
        return self._sage_parent.ambient_vector_space()(x)

    @final
    def change_base_ring(self, ring: Ring) -> ConsolidatedLattice:
        return self.change_ring(ring)

    @final
    def bilinear_form(self) -> object:
        return self.inner_product_matrix()

    @final
    def gram_matrix(self, *, basis: str = "user") -> Matrix:
        if basis == "user":
            return self._sage_parent.gram_matrix()
        if basis == "echelon":
            basis_matrix = self.basis_matrix(kind="echelon")
            return basis_matrix * self.ambient_gram_matrix() * basis_matrix.transpose()
        raise ValueError("basis must be 'user' or 'echelon'")

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
    def determinant(self) -> RingElement:
        return self._sage_parent.determinant()

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
    def is_positive_definite(self) -> bool:
        positive, negative = self.signature_pair()
        return bool(positive == self.gram_matrix().nrows() and negative == 0)

    @final
    def is_negative_definite(self) -> bool:
        positive, negative = self.signature_pair()
        return bool(positive == 0 and negative == self.gram_matrix().nrows())

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
    def ambient_gram_matrix(self) -> Matrix:
        return self.inner_product_matrix()

    @final
    def signed_discriminant(self) -> RingElement:
        if hasattr(self._sage_parent, "discriminant"):
            return self._sage_parent.discriminant()
        return self.determinant()

    @final
    def absolute_discriminant(self) -> RingElement:
        return abs(self.determinant())

    @final
    def is_degenerate(self) -> bool:
        return not self.is_nondegenerate()

    @final
    def radical(self) -> ConsolidatedLattice:
        if hasattr(self._sage_parent, "radical"):
            return _wrap_span_with_form(
                self._sage_parent.radical(),
                self.ambient_gram_matrix(),
            )
        kernel = self.gram_matrix().kernel()
        return _wrap_span_with_form(
            self._sage_parent.span(kernel.basis()),
            self.ambient_gram_matrix(),
        )

    @final
    def dual(self, *, value_ring: Ring | None = None) -> ConsolidatedLattice:
        if value_ring not in (None, ZZ):
            raise NotImplementedError("Sage metric duals are implemented here for ZZ-valued pairings")
        if hasattr(self._sage_parent, "dual_lattice"):
            return ConsolidatedLattice(self._sage_parent.dual_lattice())
        dual_basis = self.gram_matrix().inverse() * self.basis_matrix()
        return _wrap_span_with_form(
            self._sage_parent.span(dual_basis),
            self.ambient_gram_matrix(),
        )

    @final
    def dual_lattice(self, *, value_ring: Ring | None = None) -> ConsolidatedLattice:
        return self.dual(value_ring=value_ring)

    @final
    def codual(self, *, value_ring: Ring | None = None) -> ConsolidatedLattice:
        return self.dual(value_ring=value_ring)

    @final
    def dual_pairing_lattice(self) -> ConsolidatedLattice:
        return self.dual()

    @final
    def is_self_dual(self, *, value_ring: Ring | None = None) -> bool:
        return bool(self == self.dual(value_ring=value_ring))

    @final
    def change_ring(self, ring: Ring) -> ConsolidatedLattice:
        return _wrap_lattice(self._sage_parent.change_ring(ring))

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
        *,
        require_subset: bool = True,
        require_integral: bool = True,
    ) -> ConsolidatedLattice:
        if not require_integral:
            return self.fractional_sublattice(gens)
        if require_subset is False:
            lattice = _wrap_span_with_form(
                self._sage_parent.span(gens),
                self.ambient_gram_matrix(),
            )
            _assert_requested_lattice_properties(lattice, check_integral=True)
            return lattice
        lattice = ConsolidatedLattice(self._sage_parent.sublattice(gens))
        _assert_requested_lattice_properties(lattice, check_integral=True)
        return lattice

    @final
    def fractional_sublattice(self, gens: Sequence[RModuleElement]) -> ConsolidatedLattice:
        return _wrap_span_with_form(self._sage_parent.span(gens), self.ambient_gram_matrix())

    @final
    def overlattice(
        self,
        gens: Sequence[RModuleElement],
        check_integral: bool = True,
    ) -> ConsolidatedLattice:
        lattice = ConsolidatedLattice(self._sage_parent.overlattice(gens))
        _assert_requested_lattice_properties(lattice, check_integral=True if check_integral else None)
        return lattice

    @final
    def span(
        self,
        gens: Sequence[RModuleElement],
        *,
        base_ring: Ring | None = None,
        check_integral: bool | None = None,
        check_even: bool | None = None,
        **kwds: object,
    ) -> Any:
        target_ring = self.base_ring() if base_ring is None else base_ring
        if target_ring == QQ:
            assert hasattr(self._sage_parent, "vector_space_span")
            lattice = _wrap_span_with_form(
                self._sage_parent.vector_space_span(gens),
                self.ambient_gram_matrix(),
            )
        elif target_ring == self.base_ring():
            lattice = _wrap_span_with_form(
                self._sage_parent.span(gens, **kwds),
                self.ambient_gram_matrix(),
            )
        else:
            lattice = _wrap_span_with_form(
                self._sage_parent.change_ring(target_ring).span(gens, **kwds),
                self.ambient_gram_matrix(),
            )
        _assert_requested_lattice_properties(lattice, check_integral=check_integral, check_even=check_even)
        return lattice

    @final
    def span_of_basis(
        self,
        basis: Sequence[RModuleElement],
        *,
        base_ring: Ring | None = None,
        check_integral: bool | None = None,
        check_even: bool | None = None,
        **kwds: object,
    ) -> Any:
        target_ring = self.base_ring() if base_ring is None else base_ring
        if target_ring == QQ:
            assert hasattr(self._sage_parent, "vector_space_span_of_basis")
            lattice = _wrap_span_with_form(
                self._sage_parent.vector_space_span_of_basis(basis),
                self.ambient_gram_matrix(),
            )
        elif target_ring == self.base_ring():
            lattice = _wrap_span_with_form(
                self._sage_parent.span_of_basis(basis, **kwds),
                self.ambient_gram_matrix(),
            )
        else:
            lattice = _wrap_span_with_form(
                self._sage_parent.change_ring(target_ring).span_of_basis(basis, **kwds),
                self.ambient_gram_matrix(),
            )
        _assert_requested_lattice_properties(lattice, check_integral=check_integral, check_even=check_even)
        return lattice

    @final
    def zero_lattice(self) -> ConsolidatedLattice:
        if hasattr(self._sage_parent, "zero_submodule"):
            return _wrap_span_with_form(
                self._sage_parent.zero_submodule(),
                self.ambient_gram_matrix(),
            )
        return _wrap_span_with_form(self._sage_parent.span([]), self.ambient_gram_matrix())

    @final
    def intersection(self, other: ConsolidatedLattice) -> Any:
        return _wrap_span_with_form(
            self._sage_parent.intersection(_sage_object(other)),
            self.ambient_gram_matrix(),
        )

    @final
    def sum(self, other: ConsolidatedLattice) -> Any:
        return _wrap_span_with_form(
            self._sage_parent + _sage_object(other),
            self.ambient_gram_matrix(),
        )

    @final
    def primitive_closure(self, *, in_ambient: ConsolidatedLattice | None = None) -> Any:
        if in_ambient is None:
            return self.saturation()
        assert hasattr(self._sage_parent, "vector_space_span_of_basis")
        raw_rational_span = self._sage_parent.vector_space_span_of_basis(self._sage_parent.basis())
        return _wrap_span_with_form(
            _sage_object(in_ambient).intersection(raw_rational_span),
            in_ambient.ambient_gram_matrix(),
        )

    @final
    def saturation(self, *, in_ambient: ConsolidatedLattice | None = None) -> Any:
        if in_ambient is not None:
            return self.primitive_closure(in_ambient=in_ambient)
        return _wrap_span_with_form(
            self._sage_parent.saturation(),
            self.ambient_gram_matrix(),
        )

    @final
    def integral_saturation(self) -> Any:
        return _wrap_span_with_form(
            self._sage_parent.saturation(),
            self.ambient_gram_matrix(),
        )

    @final
    def index_in(self, other: ConsolidatedLattice) -> RingElement:
        return self._sage_parent.index_in(_sage_object(other))

    @final
    def relative_index(self, other: ConsolidatedLattice) -> RingElement:
        return self.index_in(other)

    @final
    def denominator(self) -> RingElement:
        return self._sage_parent.denominator()

    @final
    def clear_denominators(self) -> ConsolidatedLattice:
        return self.scale_basis(self.denominator())

    @final
    def direct_sum(self, other: ConsolidatedLattice, **kwds: object) -> Any:
        return _wrap_lattice(self._sage_parent.direct_sum(_sage_object(other), **kwds))

    @final
    def _require_positive_definite_algorithm(self, name: str) -> None:
        if not self.is_positive_definite():
            raise AttributeError(f"{name} is only exposed on positive-definite lattice wrappers; use underlying_quadratic_module() for raw Sage access")

    @final
    def LLL(self, *args: object, **kwds: object) -> Any:
        self._require_positive_definite_algorithm("LLL")
        return _wrap_lattice(self._sage_parent.LLL(*args, **kwds))

    @final
    def BKZ(self, *args: object, **kwds: object) -> Any:
        self._require_positive_definite_algorithm("BKZ")
        return _wrap_lattice(self._sage_parent.BKZ(*args, **kwds))

    @final
    def minimum(self, *args: object, **kwds: object) -> object:
        self._require_positive_definite_algorithm("minimum")
        return self._sage_parent.minimum(*args, **kwds)

    @final
    def short_vectors(self, *args: object, **kwds: object) -> object:
        self._require_positive_definite_algorithm("short_vectors")
        return self._sage_parent.short_vectors(*args, **kwds)

    @final
    def short_vectors_up_to_sign(self, *args: object, **kwds: object) -> object:
        self._require_positive_definite_algorithm("short_vectors_up_to_sign")
        kwds.setdefault("up_to_sign_flag", True)
        return self._sage_parent.short_vectors(*args, **kwds)

    @final
    def enumerate_short_vectors(self, *args: object, **kwds: object) -> object:
        self._require_positive_definite_algorithm("enumerate_short_vectors")
        return self._sage_parent.enumerate_short_vectors(*args, **kwds)

    @final
    def shortest_vector(self, *args: object, **kwds: object) -> object:
        self._require_positive_definite_algorithm("shortest_vector")
        return self._sage_parent.shortest_vector(*args, **kwds)

    @final
    def closest_vector(self, *args: object, **kwds: object) -> object:
        self._require_positive_definite_algorithm("closest_vector")
        return self._sage_parent.closest_vector(*args, **kwds)

    @final
    def voronoi_cell(self, *args: object, **kwds: object) -> object:
        self._require_positive_definite_algorithm("voronoi_cell")
        return self._sage_parent.voronoi_cell(*args, **kwds)

    @final
    def hom(self, codomain: ConsolidatedLattice) -> LatticeHomset:
        return LatticeHomset(self, codomain)

    @final
    def module_hom(self, images: object, *, codomain: object | None = None) -> object:
        if codomain is None:
            return self._sage_parent.hom(images)
        return self._sage_parent.hom(images, codomain=_sage_object(codomain))

    @final
    def lattice_hom(
        self,
        matrix_or_images: object,
        *,
        codomain: ConsolidatedLattice,
    ) -> object:
        return self.hom(codomain)(matrix_or_images)

    @final
    def isometry(
        self,
        matrix_or_images: object,
        *,
        codomain: ConsolidatedLattice | None = None,
    ) -> object:
        return self.hom(self if codomain is None else codomain)(matrix_or_images)

    @final
    def similarity(
        self,
        matrix_or_images: object,
        multiplier: RingElement,
        *,
        codomain: ConsolidatedLattice | None = None,
    ) -> object:
        target = self if codomain is None else codomain
        morphism = self.sage_object().Hom(target.sage_object())(matrix_or_images)
        matrix_data = morphism.matrix()
        if matrix_data.transpose() * target.gram_matrix() * matrix_data != multiplier * self.gram_matrix():
            raise ValueError("lattice similarities must satisfy F^T G_M F = multiplier * G_L")
        return LatticeMorphismAdapter(morphism, self, target)

    @final
    def embedding(
        self,
        matrix_or_images: object,
        *,
        codomain: ConsolidatedLattice,
        primitive: bool = False,
    ) -> object:
        morphism = self.lattice_hom(matrix_or_images, codomain=codomain)
        if primitive:
            image = morphism.image()
            assert hasattr(image, "is_primitive")
            if not image.is_primitive():
                raise ValueError("embedding image is not primitive")
        return morphism

    @final
    def quotient_by_sublattice(self, sublattice: ConsolidatedLattice) -> object:
        quotient = self._sage_parent.quotient_module(_sage_object(sublattice))
        return LatticeQuotientAdapter(quotient, self, _wrap_lattice(_sage_object(sublattice)))

    @final
    def finite_quotient(self, other: ConsolidatedLattice) -> object:
        self_object = self.sage_object()
        other_object = _sage_object(other)
        assert hasattr(self_object, "is_submodule")
        assert hasattr(other_object, "is_submodule")
        if other_object.is_submodule(self_object):
            quotient = self.quotient_by_sublattice(other)
        elif self_object.is_submodule(other_object):
            quotient = LatticeQuotientAdapter(
                other_object.quotient_module(self_object),
                _wrap_lattice(other_object),
                self,
            )
        else:
            raise ValueError("finite lattice quotients require comparable lattices")
        quotient_object = quotient.sage_object()
        assert hasattr(quotient_object, "is_finite")
        if not quotient_object.is_finite():
            raise ValueError("quotient is not finite")
        return quotient

    @final
    def quotient_map_to(self, quotient: object) -> object:
        if isinstance(quotient, LatticeQuotientAdapter):
            return quotient.quotient_map()
        if isinstance(quotient, ConsolidatedLattice):
            return self.finite_quotient(quotient).quotient_map()
        if hasattr(quotient, "quotient_map"):
            return quotient.quotient_map()
        raise NotImplementedError("the supplied quotient object does not expose quotient_map")

    @final
    def discriminant_group(self, primary: int = 0) -> object:
        discriminant_group = refine_category(
            self._sage_parent.discriminant_group(primary),
            DiscriminantGroups(ZZ),
            test=False,
        )
        return DiscriminantGroupAdapter(discriminant_group, self)

    @final
    def underlying_module(self) -> object:
        return self._sage_parent

    @final
    def underlying_quadratic_module(self) -> object:
        return self._sage_parent

    @final
    def underlying_quotient_module(self) -> object:
        return self._sage_parent


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
        quadratic_space = _quadratic_space_from_gram(gram)
        if basis is None:
            return ConsolidatedLattice(quadratic_space)
        return _wrap_span_with_form(quadratic_space.span(basis), gram)
    raise ValueError("nonintegral ZZ lattices must be built from an existing Sage parent")
