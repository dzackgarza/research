r"""Domain algebra for the synthetic lattice category (V2 declaration layer).

This module IS the typed language of the spike: vocabulary (the nouns, as
structural ``Protocol`` contracts), grammar (the constructor family — the only
entry into the language), transitions (each operation declared on the narrowest
protocol where the mathematics defines it), and boundary codecs (the opaque
aliases below, the only places raw Sage data crosses a domain signature).

Rules of the language (authoritative source: the declaration-layer plan record
``lattice-category-mathematical-vocabulary-and-subcategory-tree-declaration-layer``
in the agent-memory vault):

- Two-axis placement: a method appears on the protocol where it is DEFINED;
  a defined-but-unimplemented contract raises the standard abstract signal at
  runtime — absence and abstract-error are different, intentional signals.
- Parse, don't validate: constructors assert their domain contract (ADDD
  style: assert early, dump data, direct to the fix surface) and route the
  object into the correct subcategory; nothing downstream re-checks what
  construction proved.
- Dispatch is by declared type / category membership, never hasattr probing.
  The ONLY sanctioned static downcasts are the ``in_*`` narrowing functions at
  the bottom of this module, each assertion-shaped.
- No Sage import appears in this module; Sage types cross domain signatures
  only through the opaque boundary aliases, and at runtime only at declared
  seams and ephemeral-engine sites.

This module contains no logic. Grammar functions raise ``NotImplementedError``
until the parity plan's T1 realizes them.
"""

from __future__ import annotations

from typing import Iterator, Literal, Protocol, Sequence, TypeAlias

__all__ = [
    # boundary codecs
    "RawGramMatrix",
    "RawMorphismMatrix",
    "ExactScalar",
    "BaseRing",
    "SignaturePair",
    "FormKind",
    "CartanType",
    # value objects
    "ValueModule",
    # lattice vocabulary
    "Lattice",
    "NondegenerateLattice",
    "IntegralNondegenerateLattice",
    "DefiniteLattice",
    "PositiveDefiniteLattice",
    "CryptographicLattice",
    "IndefiniteLattice",
    "HyperbolicLattice",
    "RootGeneratedLattice",
    "LatticeElement",
    # morphisms
    "LatticeMorphism",
    "LatticeHomset",
    "LatticeSimilarity",
    # groups
    "IsometryGroup",
    "IsometrySubgroup",
    "DiscriminantOrthogonalGroup",
    # discriminant vocabulary
    "DiscriminantForm",
    "BilinearDiscriminantForm",
    "QuadraticDiscriminantForm",
    "SourcedDiscriminantForm",
    "DiscriminantFormElement",
    "DiscriminantSubgroup",
    "DiscriminantAction",
    # genus
    "Genus",
    # grammar
    "from_gram_matrix",
    "from_form_data",
    "U",
    "RootLattice",
    # narrowing
    "in_nondegenerate",
    "in_integral_nondegenerate",
    "in_definite",
    "in_positive_definite",
    "in_indefinite",
    "in_hyperbolic",
]


# ---------------------------------------------------------------------------
# Boundary codecs (opaque on purpose: raw Sage data enters the language only
# through the grammar, and leaves it only at declared seams)
# ---------------------------------------------------------------------------

RawGramMatrix: TypeAlias = object
"""A matrix-like accepted by ``from_gram_matrix``; squareness/symmetry are the
constructor's assertions, not this alias's promise."""

RawMorphismMatrix: TypeAlias = object
"""A matrix-like accepted by homset/element constructors."""

ExactScalar: TypeAlias = object
"""An exact Sage scalar (Integer/Rational). Never a float."""

BaseRing: TypeAlias = object
"""ZZ or QQ (the constructor asserts membership)."""

SignaturePair: TypeAlias = tuple[int, int]
"""Sylvester pair (p, n); p + n < rank exactly for degenerate lattices."""

FormKind: TypeAlias = Literal["group", "bilinear", "quadratic"]

CartanType: TypeAlias = tuple[Literal["A", "D", "E"], int]


class ValueModule(Protocol):
    """The form-value object K/(level*R): QQ/ZZ (bilinear) or QQ/2ZZ (even quadratic)."""

    def level(self) -> ExactScalar: ...

    def __call__(self, value: ExactScalar) -> ExactScalar: ...


# ---------------------------------------------------------------------------
# Elements
# ---------------------------------------------------------------------------

class LatticeElement(Protocol):
    def parent(self) -> "Lattice": ...

    def coefficient_vector(self) -> Sequence[ExactScalar]: ...

    def b(self, other: "LatticeElement") -> ExactScalar: ...

    def q(self) -> ExactScalar: ...


class DiscriminantFormElement(Protocol):
    def parent(self) -> "DiscriminantForm": ...

    def coefficient_vector(self) -> Sequence[ExactScalar]: ...

    def order(self) -> int: ...


# ---------------------------------------------------------------------------
# Lattices: the base vocabulary (defined for EVERY lattice, degenerate included)
# ---------------------------------------------------------------------------

class Lattice(Protocol):
    """A based free R-module (R, G) with symmetric bilinear form; possibly degenerate."""

    # structural
    def rank(self) -> int: ...

    def gram_matrix(self) -> RawGramMatrix: ...

    def base_ring(self) -> BaseRing: ...

    def b(self, left: LatticeElement, right: LatticeElement) -> ExactScalar: ...

    def q(self, element: LatticeElement) -> ExactScalar: ...

    def basis(self) -> tuple[LatticeElement, ...]: ...

    def gens(self) -> tuple[LatticeElement, ...]: ...

    def gen(self, i: int) -> LatticeElement: ...

    def ngens(self) -> int: ...

    def zero(self) -> LatticeElement: ...

    def determinant(self) -> ExactScalar: ...

    def discriminant(self) -> ExactScalar: ...

    def absolute_discriminant(self) -> ExactScalar: ...

    def signature_pair(self) -> SignaturePair: ...

    def signature(self) -> int: ...

    def denominator(self) -> ExactScalar: ...

    def clear_denominators(self) -> "Lattice": ...

    # predicates (total; used by the narrowing functions below)
    def is_integral(self) -> bool: ...

    def is_even(self) -> bool: ...

    def is_unimodular(self) -> bool: ...

    def is_self_dual(self) -> bool: ...

    def is_degenerate(self) -> bool: ...

    def is_nondegenerate(self) -> bool: ...

    def is_definite(self) -> bool: ...

    def is_positive_definite(self) -> bool: ...

    def is_negative_definite(self) -> bool: ...

    def is_indefinite(self) -> bool: ...

    def is_hyperbolic(self) -> bool: ...

    # radical theory (the functor that STAYS a lattice)
    def radical(self) -> "Lattice": ...

    def radical_quotient(self) -> "NondegenerateLattice": ...

    # constructions
    def twist(self, scalar: ExactScalar) -> "Lattice": ...

    def scale(self, scalar: ExactScalar) -> "Lattice": ...

    def direct_sum(self, other: "Lattice") -> "Lattice": ...

    def tensor_product(self, other: "Lattice") -> "Lattice": ...

    def rationalization(self) -> "Lattice": ...

    def base_extend(self, ring: BaseRing) -> "Lattice": ...

    # subobject algebra
    def sublattice(self, generators: Sequence[Sequence[ExactScalar]]) -> "Lattice": ...

    def fractional_sublattice(self, generators: Sequence[Sequence[ExactScalar]]) -> "Lattice": ...

    def span(self, generators: Sequence[Sequence[ExactScalar]]) -> "Lattice": ...

    def span_of_basis(self, basis: Sequence[Sequence[ExactScalar]]) -> "Lattice": ...

    def sum(self, other: "Lattice") -> "Lattice": ...

    def intersection(self, other: "Lattice") -> "Lattice": ...

    def saturation(self) -> "Lattice": ...

    def primitive_closure(self, ambient: "Lattice") -> "Lattice": ...

    def index_in(self, other: "Lattice") -> ExactScalar: ...

    def index_in_saturation(self) -> ExactScalar: ...

    def is_submodule(self, other: "Lattice") -> bool: ...

    def is_primitive(self, sublattice: "Lattice") -> bool: ...

    def overlattice(self, generators: Sequence[Sequence[ExactScalar]]) -> "Lattice": ...

    def orthogonal_complement(self, other: "Lattice") -> "Lattice": ...

    def zero_lattice(self) -> "Lattice": ...

    # quotients (the functor that LEAVES: plain finite abelian quotient, no form axioms)
    def finite_quotient(self, sublattice: "Lattice") -> "DiscriminantForm": ...

    # morphisms
    def Hom(self, codomain: "Lattice") -> "LatticeHomset": ...

    def hom(self, matrix: RawMorphismMatrix, codomain: "Lattice") -> "LatticeMorphism": ...

    def embedding(
        self, matrix: RawMorphismMatrix, codomain: "Lattice", primitive: bool = False
    ) -> "LatticeMorphism": ...

    def similarity(
        self, matrix: RawMorphismMatrix, codomain: "Lattice", scalar: ExactScalar
    ) -> "LatticeSimilarity": ...

    def reflection(self, vector: LatticeElement) -> "LatticeMorphism": ...

    # groups and isometry
    def isometry_group(self) -> "IsometryGroup": ...

    def is_isometric(self, other: "Lattice") -> bool: ...


# ---------------------------------------------------------------------------
# Subcategory vocabularies (axis 1: definedness -> placement, as types)
# ---------------------------------------------------------------------------

class NondegenerateLattice(Lattice, Protocol):
    def dual(self) -> "Lattice": ...

    def dual_inclusion(self) -> "LatticeMorphism": ...


class IntegralNondegenerateLattice(NondegenerateLattice, Protocol):
    def discriminant_group(self, primary: int = 0) -> "SourcedDiscriminantForm": ...

    def genus(self) -> "Genus": ...

    def same_genus(self, other: "IntegralNondegenerateLattice") -> bool: ...

    def glue(self, isotropic_subgroup: "DiscriminantSubgroup") -> "Lattice": ...

    def maximal_overlattice(self, p: int | None = None) -> "Lattice": ...

    def local_modification(self, data: object, p: int) -> "Lattice": ...

    def embeds_primitively_in_unimodular(
        self, signature_pair: SignaturePair, even: bool = True
    ) -> bool: ...

    def primitive_embedding_into_unimodular(
        self, signature_pair: SignaturePair, even: bool = True
    ) -> "LatticeMorphism": ...


class DefiniteLattice(Lattice, Protocol):
    """Finite-enumeration vocabulary. Semantics for the negative-definite case
    are gap-ledger item 4 (ratified interactively), not fixed by this stub."""

    def minimum(self) -> ExactScalar: ...

    def maximum(self) -> ExactScalar: ...

    def shortest_vector(self) -> LatticeElement: ...

    def short_vectors(self, bound: int) -> Sequence[Sequence[LatticeElement]]: ...

    def enumerate_short_vectors(self, bound: int) -> Iterator[LatticeElement]: ...

    def vectors_of_square(self, square: ExactScalar) -> tuple[LatticeElement, ...]: ...

    def roots(self) -> tuple[LatticeElement, ...]: ...

    def volume(self) -> ExactScalar: ...


class PositiveDefiniteLattice(DefiniteLattice, Protocol):
    def LLL(self) -> "PositiveDefiniteLattice": ...

    def reduced_basis(self) -> tuple[LatticeElement, ...]: ...

    def cryptographic(self) -> "CryptographicLattice": ...


class CryptographicLattice(PositiveDefiniteLattice, Protocol):
    """Opt-in axiom (decision D1); never auto-attached."""

    def BKZ(self, block_size: int = 10) -> "CryptographicLattice": ...

    def HKZ(self) -> "CryptographicLattice": ...

    def babai(self, target: Sequence[ExactScalar]) -> LatticeElement: ...

    def approximate_closest_vector(self, target: Sequence[ExactScalar]) -> LatticeElement: ...

    def closest_vector(self, target: Sequence[ExactScalar]) -> LatticeElement: ...

    def enumerate_close_vectors(
        self, target: Sequence[ExactScalar], radius: ExactScalar
    ) -> Sequence[LatticeElement]: ...

    def voronoi_cell(self, radius: int | None = None) -> object: ...

    def voronoi_relevant_vectors(self) -> tuple[LatticeElement, ...]: ...

    def gaussian_heuristic(self) -> object: ...

    def hadamard_ratio(self) -> object: ...

    def update_reduced_basis(self, vector: LatticeElement) -> "CryptographicLattice": ...


class IndefiniteLattice(Lattice, Protocol):
    def has_isotropic_vector(self) -> bool: ...

    def isotropic_vectors(self, bound: int) -> tuple[LatticeElement, ...]: ...

    def primitive_isotropic_vectors(self, bound: int) -> tuple[LatticeElement, ...]: ...


class HyperbolicLattice(IndefiniteLattice, Protocol):
    """Signature (1, rank-1). Names fixed now; engines are the Vinberg workstream."""

    def weyl_group(self) -> "IsometrySubgroup": ...

    def fundamental_chamber(self) -> object: ...

    def is_reflective(self) -> bool: ...

    def roots_up_to_height(self, height: ExactScalar) -> tuple[LatticeElement, ...]: ...

    def isotropic_rays(self) -> tuple[LatticeElement, ...]: ...


class RootGeneratedLattice(Lattice, Protocol):
    """Attached ONLY by construction provenance (the certificate), never detected."""

    def cartan_type(self) -> CartanType: ...

    def irreducible_root_components(self) -> tuple["RootGeneratedLattice", ...]: ...


# ---------------------------------------------------------------------------
# Morphisms
# ---------------------------------------------------------------------------

class LatticeMorphism(Protocol):
    """Form-preserving by construction: A^T G_M A = G_L, enforced at creation."""

    def domain(self) -> Lattice: ...

    def codomain(self) -> Lattice: ...

    def matrix(self) -> RawMorphismMatrix: ...  # the matrix-space seam

    def __call__(self, element: LatticeElement) -> LatticeElement: ...

    def is_isometry(self) -> bool: ...

    def is_injective(self) -> bool: ...

    def is_surjective(self) -> bool: ...

    def kernel(self) -> Lattice: ...

    def image(self) -> Lattice: ...

    def cokernel(self) -> "DiscriminantForm": ...
    """Finite-cokernel case only; the general case is a gap-ledger contract."""

    def induced_map_on_discriminant_group(self) -> "DiscriminantAction": ...
    """Per-element functor; defined when domain == codomain is integral nondegenerate."""


class LatticeSimilarity(Protocol):
    def domain(self) -> Lattice: ...

    def codomain(self) -> Lattice: ...

    def matrix(self) -> RawMorphismMatrix: ...

    def scalar(self) -> ExactScalar: ...

    def __call__(self, element: LatticeElement) -> LatticeElement: ...


class LatticeHomset(Protocol):
    def domain(self) -> Lattice: ...

    def codomain(self) -> Lattice: ...

    def from_matrix(self, matrix: RawMorphismMatrix) -> LatticeMorphism: ...


# ---------------------------------------------------------------------------
# Isometry groups (O(L) exists for EVERY lattice; enumeration is per-leaf)
# ---------------------------------------------------------------------------

class IsometryGroup(Protocol):
    """O(L). Membership/construction/is_finite are total; gens/order/iteration
    are contracts implemented exactly where the group is finite."""

    def lattice(self) -> Lattice: ...

    def __contains__(self, candidate: object) -> bool: ...

    def from_matrix(self, matrix: RawMorphismMatrix) -> LatticeMorphism: ...

    def one(self) -> LatticeMorphism: ...

    def is_finite(self) -> bool: ...

    def gens(self) -> tuple[LatticeMorphism, ...]: ...

    def order(self) -> int: ...

    def __iter__(self) -> Iterator[LatticeMorphism]: ...

    def subgroup(self, generators: Sequence[LatticeMorphism]) -> "IsometrySubgroup": ...

    def discriminant_action(self, isometry: LatticeMorphism) -> "DiscriminantAction": ...

    def discriminant_representation(self) -> "DiscriminantOrthogonalGroup": ...

    def stable_kernel(self) -> "IsometrySubgroup": ...

    # seams (implemented exactly where finite with computed generators)
    def as_matrix_group(self) -> object: ...

    def as_permutation_group(self) -> object: ...


class IsometrySubgroup(Protocol):
    """<gens> <= O(L): the ONLY home for caller-supplied generators. Answers
    subgroup questions only — no membership test, no O(L)-level claims."""

    def lattice(self) -> Lattice: ...

    def ambient(self) -> IsometryGroup: ...

    def gens(self) -> tuple[LatticeMorphism, ...]: ...

    def preserves(self, sublattice: Lattice) -> bool: ...

    def discriminant_image(self) -> "DiscriminantOrthogonalGroup": ...

    def order(self) -> int: ...  # implemented only when the ambient is finite

    def __iter__(self) -> Iterator[LatticeMorphism]: ...

    def as_matrix_group(self) -> object: ...

    def as_permutation_group(self) -> object: ...


class DiscriminantOrthogonalGroup(Protocol):
    """O(q) (or a subgroup of it): FINITE for every discriminant form, so the
    full group surface is total on this side."""

    def discriminant_form(self) -> "DiscriminantForm": ...

    def gens(self) -> tuple["DiscriminantAction", ...]: ...

    def order(self) -> int: ...

    def __contains__(self, candidate: object) -> bool: ...

    def __iter__(self) -> Iterator["DiscriminantAction"]: ...

    def as_matrix_group(self) -> object: ...

    def as_permutation_group(self) -> object: ...


class DiscriminantAction(Protocol):
    def discriminant_form(self) -> "DiscriminantForm": ...

    def matrix(self) -> RawMorphismMatrix: ...

    def __call__(self, element: DiscriminantFormElement) -> DiscriminantFormElement: ...

    def is_identity(self) -> bool: ...

    def inverse(self) -> "DiscriminantAction": ...

    def preserves_bilinear_form(self) -> bool: ...

    def preserves_quadratic_form(self) -> bool: ...


# ---------------------------------------------------------------------------
# Discriminant forms (one consolidated parent; axioms select the vocabulary)
# ---------------------------------------------------------------------------

class DiscriminantForm(Protocol):
    """The finite-abelian-group surface (every finite quotient, form or not)."""

    def invariants(self) -> tuple[int, ...]: ...

    def elementary_divisors(self) -> tuple[int, ...]: ...

    def cardinality(self) -> int: ...

    def order(self, element: DiscriminantFormElement | None = None) -> int: ...

    def exponent(self) -> int: ...

    def is_cyclic(self) -> bool: ...

    def short_name(self) -> str: ...

    def generator_orders(self) -> tuple[int, ...]: ...

    def annihilator(self) -> ExactScalar: ...

    def gens(self) -> tuple[DiscriminantFormElement, ...]: ...

    def gen(self, i: int) -> DiscriminantFormElement: ...

    def ngens(self) -> int: ...

    def smith_form_gens(self) -> tuple[DiscriminantFormElement, ...]: ...

    def zero(self) -> DiscriminantFormElement: ...

    def elements(self) -> tuple[DiscriminantFormElement, ...]: ...

    def discrete_exp(self, coefficients: Sequence[int]) -> DiscriminantFormElement: ...

    def discrete_log(self, element: DiscriminantFormElement) -> tuple[int, ...]: ...

    def subgroup_generated_by(
        self, generators: Sequence[DiscriminantFormElement]
    ) -> "DiscriminantSubgroup": ...

    def quotient_group(self, subgroup: "DiscriminantSubgroup") -> "DiscriminantForm": ...

    def primary_part(self, p: int) -> "DiscriminantForm": ...

    def primary_decomposition(self) -> tuple["DiscriminantForm", ...]: ...

    def all_submodules(self) -> tuple["DiscriminantSubgroup", ...]: ...

    def automorphism_group(self) -> DiscriminantOrthogonalGroup: ...

    def permutation_group(self) -> object: ...  # the GAP-backed group-theoretic seam

    def is_isomorphic(self, other: "DiscriminantForm", kind: FormKind = "quadratic") -> bool: ...


class BilinearDiscriminantForm(DiscriminantForm, Protocol):
    def b(
        self, left: DiscriminantFormElement, right: DiscriminantFormElement
    ) -> ExactScalar: ...

    def gram_matrix_bilinear(self) -> RawGramMatrix: ...

    def value_module(self) -> ValueModule: ...

    def radical(self) -> "DiscriminantSubgroup": ...

    def is_nondegenerate(self) -> bool: ...

    def orthogonal(self, subgroup: "DiscriminantSubgroup") -> "DiscriminantSubgroup": ...

    def is_isotropic_subgroup(self, subgroup: "DiscriminantSubgroup") -> bool: ...

    def isotropic_subgroups(self) -> tuple["DiscriminantSubgroup", ...]: ...

    def is_lagrangian(self, subgroup: "DiscriminantSubgroup") -> bool: ...

    def lagrangian_subgroups(self) -> tuple["DiscriminantSubgroup", ...]: ...

    def metabolizer(self) -> "DiscriminantSubgroup": ...

    def is_metabolic(self) -> bool: ...

    def is_anisotropic(self) -> bool: ...

    def maximal_isotropic_subgroups(self) -> tuple["DiscriminantSubgroup", ...]: ...

    def orthogonal_quotient(self, subgroup: "DiscriminantSubgroup") -> "DiscriminantForm": ...

    def orthogonal_group(self) -> DiscriminantOrthogonalGroup: ...


class QuadraticDiscriminantForm(BilinearDiscriminantForm, Protocol):
    def q(self, element: DiscriminantFormElement) -> ExactScalar: ...

    def gram_matrix_quadratic(self) -> RawGramMatrix: ...

    def value_module_qf(self) -> ValueModule: ...

    def brown_invariant(self) -> int: ...

    def normal_form(self) -> tuple[tuple[int, ...], RawGramMatrix]: ...

    def is_genus(self, signature_pair: SignaturePair, even: bool = True) -> bool: ...

    def genus(self, signature_pair: SignaturePair, even: bool = True) -> "Genus": ...

    def twist(self, scalar: ExactScalar) -> "QuadraticDiscriminantForm": ...


class SourcedDiscriminantForm(QuadraticDiscriminantForm, Protocol):
    """WithSourceLattice: carries L^*/L provenance."""

    def source_lattice(self) -> IntegralNondegenerateLattice: ...

    def cover_lattice(self) -> Lattice: ...

    def relation_lattice(self) -> Lattice: ...

    def lift(self, element: DiscriminantFormElement) -> LatticeElement: ...

    def projection(self, element: LatticeElement) -> DiscriminantFormElement: ...

    def preimage_lattice(self, subgroup: "DiscriminantSubgroup") -> Lattice: ...

    def overlattice_from_isotropic_subgroup(
        self, subgroup: "DiscriminantSubgroup"
    ) -> Lattice: ...

    def discriminant_form_of_overlattice(
        self, subgroup: "DiscriminantSubgroup"
    ) -> "DiscriminantForm": ...

    def action_of_isometry(self, isometry: LatticeMorphism) -> DiscriminantAction: ...

    def orbit(
        self, element: DiscriminantFormElement, group: DiscriminantOrthogonalGroup
    ) -> tuple[DiscriminantFormElement, ...]: ...

    def orbits(
        self, group: DiscriminantOrthogonalGroup
    ) -> tuple[tuple[DiscriminantFormElement, ...], ...]: ...

    def orbits_on_isotropic_subgroups(
        self, group: DiscriminantOrthogonalGroup
    ) -> tuple[tuple["DiscriminantSubgroup", ...], ...]: ...


class DiscriminantSubgroup(Protocol):
    def ambient(self) -> DiscriminantForm: ...

    def gens(self) -> tuple[DiscriminantFormElement, ...]: ...

    def cardinality(self) -> int: ...

    def __contains__(self, element: object) -> bool: ...


# ---------------------------------------------------------------------------
# Genus objects
# ---------------------------------------------------------------------------

class Genus(Protocol):
    def signature_pair(self) -> SignaturePair: ...

    def signature(self) -> int: ...

    def det(self) -> ExactScalar: ...

    def dim(self) -> int: ...

    def is_even(self) -> bool: ...

    def discriminant_form(self) -> QuadraticDiscriminantForm: ...

    def local_symbol(self, p: int) -> object: ...

    def local_symbols(self) -> tuple[object, ...]: ...  # the genus-machinery data seam

    def brown_invariant(self) -> int: ...

    def representative(self) -> Lattice: ...

    def representatives(self) -> tuple[Lattice, ...]: ...

    def class_number(self) -> int: ...

    def is_unique_class(self) -> bool: ...


# ---------------------------------------------------------------------------
# Grammar: the constructor family (the ONLY entry into the language).
# Conceptually functors on the category namespace; realized at T1.
# ---------------------------------------------------------------------------

def from_gram_matrix(
    gram: RawGramMatrix, base_ring: BaseRing | None = None, label: str = "L"
) -> Lattice:
    """Functor from square symmetric matrices over R into Lattices(R).

    Asserts its domain contract (square, symmetric, R in {ZZ, QQ}) ADDD-style
    and routes the object into the correct subcategory (nondegenerate/degenerate,
    integrality/parity/unimodularity, definiteness, hyperbolic). The
    skew-symmetric branch is a reserved future extension of the domain
    stratification, excluded today by the symmetry assertion.
    """
    raise NotImplementedError("realized at parity-plan T1")


def from_form_data(
    invariants: Sequence[int],
    bilinear: RawGramMatrix | None,
    quadratic: Sequence[ExactScalar] | None,
    level: int,
) -> DiscriminantForm:
    """Entry into DiscriminantForms; axioms assigned from the data (T3 model)."""
    raise NotImplementedError("realized at parity-plan T3")


def U(n: int = 1) -> HyperbolicLattice:
    """The hyperbolic plane U(n): Gram [[0, n], [n, 0]]."""
    raise NotImplementedError("realized at parity-plan T1")


def RootLattice(
    type_: Literal["A", "D", "E"], n: int, negative: bool = False
) -> RootGeneratedLattice:
    """ADE root lattice with construction-provenance RootGenerated axiom;
    ``negative=True`` is the K3-convention twist by -1."""
    raise NotImplementedError("realized at parity-plan T1")


# ---------------------------------------------------------------------------
# Narrowing: the ONLY sanctioned static downcasts, each assertion-shaped.
# Runtime truth is category membership; these lift it to the type level.
# ---------------------------------------------------------------------------

def in_nondegenerate(lattice: Lattice) -> NondegenerateLattice:
    assert lattice.is_nondegenerate(), (
        f"nondegenerate lattice required; gram={lattice.gram_matrix()!r}; "
        "pass through radical_quotient() or fix the construction site"
    )
    return lattice  # type: ignore[return-value]


def in_integral_nondegenerate(lattice: Lattice) -> IntegralNondegenerateLattice:
    assert lattice.is_integral() and lattice.is_nondegenerate(), (
        f"integral nondegenerate lattice required; gram={lattice.gram_matrix()!r}; "
        f"integral={lattice.is_integral()}, nondegenerate={lattice.is_nondegenerate()}; "
        "fix the construction site"
    )
    return lattice  # type: ignore[return-value]


def in_definite(lattice: Lattice) -> DefiniteLattice:
    assert lattice.is_definite(), (
        f"definite lattice required; signature_pair={lattice.signature_pair()}; "
        "an indefinite lattice has no finite enumeration vocabulary"
    )
    return lattice  # type: ignore[return-value]


def in_positive_definite(lattice: Lattice) -> PositiveDefiniteLattice:
    assert lattice.is_positive_definite(), (
        f"positive-definite lattice required; signature_pair={lattice.signature_pair()}"
    )
    return lattice  # type: ignore[return-value]


def in_indefinite(lattice: Lattice) -> IndefiniteLattice:
    assert lattice.is_indefinite(), (
        f"indefinite lattice required; signature_pair={lattice.signature_pair()}"
    )
    return lattice  # type: ignore[return-value]


def in_hyperbolic(lattice: Lattice) -> HyperbolicLattice:
    assert lattice.is_hyperbolic(), (
        f"hyperbolic lattice (signature (1, n-1)) required; "
        f"signature_pair={lattice.signature_pair()}"
    )
    return lattice  # type: ignore[return-value]
