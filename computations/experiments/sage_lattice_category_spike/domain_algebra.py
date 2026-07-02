r"""Domain algebra for the synthetic lattice category (V2 declaration layer).

This module IS the typed language of the spike: vocabulary (the nouns, as
real typed classes), grammar (the constructor family — the only entry into the
language), transitions (each operation declared on the narrowest class where
the mathematics defines it), and boundary codecs (the parsed primitives below,
the only places raw Sage data crosses a domain signature).

SINGLE-SOURCE DESIGN (probe-verified 2026-07-02): the lattice-side classes are
CARRIERS — at T1 each is installed as the ``ParentMethods`` of its category or
axiom class, so the runtime-injected surface and this typed language are ONE
artifact (no parallel mirror to drift). Sage copies (does not inherit) carrier
attributes into the dynamic parent class, hence narrowing below stays
assertion-shaped rather than isinstance. The morphism/group/discriminant/genus
classes are ordinary ABC-style bases the implementations INHERIT nominally.
Carrier inheritance in this file is static structure only; at runtime each
category injects exactly its own delta. Every body fails loud — a silent
``...`` body would inject as a None-returning method, a catastrophic fail-open.

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
  only through the parsed primitives and raw boundary aliases, and at runtime
  only at declared seams and ephemeral-engine sites.
- ``ValueModule`` stays a Protocol deliberately: it types an EXTERNAL object
  (Sage's QmodnZ) that we neither own nor subclass — the one legitimate
  structural-typing use.

This module contains no logic. Grammar functions raise ``NotImplementedError``
until the parity plan's T1 realizes them.
"""

from __future__ import annotations

from typing import Callable, Iterator, Literal, NewType, Protocol, Sequence, TypeAlias

__all__ = [
    # boundary codecs
    "RawGramMatrix",
    "RawMorphismMatrix",
    "GramMatrix",
    "MorphismMatrix",
    "ExactScalar",
    "BaseRing",
    "parse_base_ring",
    "parse_gram_matrix",
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
"""Untrusted matrix-like input to the grammar; parsed once, never circulated."""

RawMorphismMatrix: TypeAlias = object
"""Untrusted matrix-like input to homset/element constructors."""

GramMatrix = NewType("GramMatrix", object)
"""PARSED symmetric square exact matrix — produced only by parse_gram_matrix.
Distinct from RawGramMatrix and from MorphismMatrix by type."""

MorphismMatrix = NewType("MorphismMatrix", object)
"""PARSED exact matrix of a validated morphism — produced only by the homset."""

ExactScalar = NewType("ExactScalar", object)
"""An exact Sage scalar (Integer/Rational). Never a float."""

BaseRing = NewType("BaseRing", object)
"""ZZ or QQ, parsed by parse_base_ring."""

SignaturePair: TypeAlias = tuple[int, int]
"""Sylvester pair (p, n); p + n < rank exactly for degenerate lattices."""

FormKind: TypeAlias = Literal["group", "bilinear", "quadratic"]

CartanType: TypeAlias = tuple[Literal["A", "D", "E"], int]


class ValueModule(Protocol):
    """The form-value object K/(level*R): QQ/ZZ (bilinear) or QQ/2ZZ (even quadratic)."""

    def level(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __call__(self, value: ExactScalar) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


# ---------------------------------------------------------------------------
# Elements
# ---------------------------------------------------------------------------

class LatticeElement:
    def parent(self) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def coefficient_vector(self) -> Sequence[ExactScalar]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def b(self, other: "LatticeElement") -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def q(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class DiscriminantFormElement:
    def parent(self) -> "DiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def b(self, other: "DiscriminantFormElement") -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def q(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def lift(self) -> "LatticeElement":
        """Coset lift to the dual lattice; meaningful for sourced forms."""
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def coefficient_vector(self) -> Sequence[ExactScalar]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def order(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


# ---------------------------------------------------------------------------
# Lattices: the base vocabulary (defined for EVERY lattice, degenerate included)
# ---------------------------------------------------------------------------

class Lattice:
    """A based free R-module (R, G) with symmetric bilinear form; possibly degenerate."""

    # structural
    def rank(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gram_matrix(self) -> GramMatrix:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def base_ring(self) -> BaseRing:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def b(self, left: LatticeElement, right: LatticeElement) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def q(self, element: LatticeElement) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def bilinear_form(self) -> Callable[[LatticeElement, LatticeElement], ExactScalar]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def quadratic_form(self) -> Callable[[LatticeElement], ExactScalar]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def basis(self) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gens(self) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gen(self, i: int) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def ngens(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def zero(self) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def determinant(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def discriminant(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def absolute_discriminant(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def signature_pair(self) -> SignaturePair:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def signature(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def denominator(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def random_element(self) -> LatticeElement:
        """Contracted into the owned surface (user ruling): sensible utility;
        the leaner super-category no longer inherits it, so we own it."""
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def clear_denominators(self) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # predicates (total; used by the narrowing functions below)
    def is_integral(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_even(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_unimodular(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_self_dual(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_degenerate(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_nondegenerate(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_definite(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_positive_definite(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_negative_definite(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_indefinite(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_hyperbolic(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # radical theory (the functor that STAYS a lattice)
    def radical(self) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def radical_quotient(self) -> "NondegenerateLattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # constructions
    def twist(self, scalar: ExactScalar) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def scale(self, scalar: ExactScalar) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def direct_sum(self, other: "Lattice") -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def tensor_product(self, other: "Lattice") -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def rationalization(self) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def base_extend(self, ring: BaseRing) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # subobject algebra
    def sublattice(self, generators: Sequence[Sequence[ExactScalar]]) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def fractional_sublattice(self, generators: Sequence[Sequence[ExactScalar]]) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def span(self, generators: Sequence[Sequence[ExactScalar]]) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def span_of_basis(self, basis: Sequence[Sequence[ExactScalar]]) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def sum(self, other: "Lattice") -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def intersection(self, other: "Lattice") -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def saturation(self) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def primitive_closure(self, ambient: "Lattice") -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def index_in(self, other: "Lattice") -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def index_in_saturation(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_submodule(self, other: "Lattice") -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_primitive(self, sublattice: "Lattice") -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def overlattice(self, generators: Sequence[Sequence[ExactScalar]]) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def orthogonal_complement(self, other: "Lattice") -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def zero_lattice(self) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # quotients (the functor that LEAVES: plain finite abelian quotient, no form axioms)
    def finite_quotient(self, sublattice: "Lattice") -> "DiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # morphisms
    def Hom(self, codomain: "Lattice") -> "LatticeHomset":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def hom(self, matrix: RawMorphismMatrix, codomain: "Lattice") -> "LatticeMorphism":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def embedding(
        self, matrix: RawMorphismMatrix, codomain: "Lattice", primitive: bool = False
    ) -> "LatticeMorphism":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def similarity(
        self, matrix: RawMorphismMatrix, codomain: "Lattice", scalar: ExactScalar
    ) -> "LatticeSimilarity":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def reflection(self, vector: LatticeElement) -> "LatticeMorphism":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # groups and isometry
    def isometry_group(self) -> "IsometryGroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


    def is_isometric(self, other: "Lattice") -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


# ---------------------------------------------------------------------------
# Subcategory vocabularies (axis 1: definedness -> placement, as types)
# ---------------------------------------------------------------------------

class NondegenerateLattice(Lattice):
    def dual(self) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def dual_inclusion(self) -> "LatticeMorphism":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class IntegralNondegenerateLattice(NondegenerateLattice):
    def discriminant_group(self, primary: int = 0) -> "SourcedDiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def genus(self) -> "Genus":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def same_genus(self, other: "IntegralNondegenerateLattice") -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def glue(self, isotropic_subgroup: "DiscriminantSubgroup") -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def maximal_overlattice(self, p: int | None = None) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def local_modification(self, data: object, p: int) -> "Lattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def embeds_primitively_in_unimodular(
        self, signature_pair: SignaturePair, even: bool = True
    ) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def primitive_embedding_into_unimodular(
        self, signature_pair: SignaturePair, even: bool = True
    ) -> "LatticeMorphism":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class DefiniteLattice(Lattice):
    """Finite-enumeration vocabulary. Semantics for the negative-definite case
    are gap-ledger item 4 (ratified interactively), not fixed by this stub."""

    def minimum(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def maximum(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def shortest_vector(self) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def short_vectors(self, bound: int) -> Sequence[Sequence[LatticeElement]]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def enumerate_short_vectors(self, bound: int) -> Iterator[LatticeElement]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def vectors_of_square(self, square: ExactScalar) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def roots(self) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def volume(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class PositiveDefiniteLattice(DefiniteLattice):
    def LLL(self) -> "PositiveDefiniteLattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def reduced_basis(self) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def cryptographic(self) -> "CryptographicLattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class CryptographicLattice(PositiveDefiniteLattice):
    """Opt-in axiom (decision D1); never auto-attached."""

    def BKZ(self, block_size: int = 10) -> "CryptographicLattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def HKZ(self) -> "CryptographicLattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def babai(self, target: Sequence[ExactScalar]) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def approximate_closest_vector(self, target: Sequence[ExactScalar]) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def closest_vector(self, target: Sequence[ExactScalar]) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def enumerate_close_vectors(
        self, target: Sequence[ExactScalar], radius: ExactScalar
    ) -> Sequence[LatticeElement]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def voronoi_cell(self, radius: int | None = None) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def voronoi_relevant_vectors(self) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gaussian_heuristic(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def hadamard_ratio(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def update_reduced_basis(self, vector: LatticeElement) -> "CryptographicLattice":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class IndefiniteLattice(Lattice):
    def has_isotropic_vector(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def isotropic_vectors(self, bound: int) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def primitive_isotropic_vectors(self, bound: int) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class HyperbolicLattice(IndefiniteLattice):
    """Signature (1, rank-1). Names fixed now; engines are the Vinberg workstream."""

    def weyl_group(self) -> "IsometrySubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def fundamental_chamber(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_reflective(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def roots_up_to_height(self, height: ExactScalar) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def isotropic_rays(self) -> tuple[LatticeElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class RootGeneratedLattice(Lattice):
    """Attached ONLY by construction provenance (the certificate), never detected."""

    def cartan_type(self) -> CartanType:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def irreducible_root_components(self) -> tuple["RootGeneratedLattice", ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


# ---------------------------------------------------------------------------
# Morphisms
# ---------------------------------------------------------------------------

class LatticeMorphism:
    """Form-preserving by construction: A^T G_M A = G_L, enforced at creation."""

    def domain(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def codomain(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def matrix(self) -> MorphismMatrix:  # the matrix-space seam
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __call__(self, element: LatticeElement) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_isometry(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # ring-LIKE predicates (V0d amendment 2026-07-03): End_Lat(L) = Hom(L, L) is the
    # form-preserving composition MONOID (operations escaping into End_{ZZ-Mod}(L) are
    # not vocabulary), but the monoid sits inside a ring, so ring-like QUERIES remain
    # well-defined on endomorphisms and are shimmed in here, curated against what
    # module-endomorphism and ring-element implementations actually expose.
    def is_identity(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_nilpotent(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_idempotent(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_unipotent(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def order(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_injective(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_surjective(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def kernel(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def image(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def cokernel(self) -> "DiscriminantForm":
        """Finite-cokernel case only; the general case is a gap-ledger contract."""
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def induced_map_on_discriminant_group(self) -> "DiscriminantAction":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")
    """Per-element functor; defined when domain == codomain is integral nondegenerate."""


class LatticeSimilarity:
    def domain(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def codomain(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def matrix(self) -> MorphismMatrix:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def scalar(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __call__(self, element: LatticeElement) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class LatticeHomset:
    def domain(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def codomain(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def from_matrix(self, matrix: RawMorphismMatrix) -> LatticeMorphism:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


# ---------------------------------------------------------------------------
# Isometry groups (O(L) exists for EVERY lattice; enumeration is per-leaf)
# ---------------------------------------------------------------------------

class IsometryGroup:
    """O(L). Membership/construction/is_finite are total; gens/order/iteration
    are contracts implemented exactly where the group is finite."""

    def lattice(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __contains__(self, candidate: object) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def from_matrix(self, matrix: RawMorphismMatrix) -> LatticeMorphism:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def one(self) -> LatticeMorphism:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_finite(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gens(self) -> tuple[LatticeMorphism, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def order(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __iter__(self) -> Iterator[LatticeMorphism]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def subgroup(self, generators: Sequence[LatticeMorphism]) -> "IsometrySubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def discriminant_action(self, isometry: LatticeMorphism) -> "DiscriminantAction":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def discriminant_representation(self) -> "DiscriminantOrthogonalGroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def stable_kernel(self) -> "IsometrySubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    # seams (implemented exactly where finite with computed generators)
    def as_matrix_group(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def as_permutation_group(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class IsometrySubgroup:
    """<gens> <= O(L): the ONLY home for caller-supplied generators. Answers
    subgroup questions only — no membership test, no O(L)-level claims."""

    def lattice(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def ambient(self) -> IsometryGroup:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gens(self) -> tuple[LatticeMorphism, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def preserves(self, sublattice: Lattice) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def discriminant_image(self) -> "DiscriminantOrthogonalGroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def order(self) -> int:  # implemented only when the ambient is finite
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __iter__(self) -> Iterator[LatticeMorphism]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def as_matrix_group(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def as_permutation_group(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class DiscriminantOrthogonalGroup:
    """O(q) (or a subgroup of it): FINITE for every discriminant form, so the
    full group surface is total on this side."""

    def discriminant_form(self) -> "DiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gens(self) -> tuple["DiscriminantAction", ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def order(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __contains__(self, candidate: object) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __iter__(self) -> Iterator["DiscriminantAction"]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def as_matrix_group(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def as_permutation_group(self) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class DiscriminantAction:
    def discriminant_form(self) -> "DiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def matrix(self) -> MorphismMatrix:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __call__(self, element: DiscriminantFormElement) -> DiscriminantFormElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_identity(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def inverse(self) -> "DiscriminantAction":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def preserves_bilinear_form(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def preserves_quadratic_form(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


# ---------------------------------------------------------------------------
# Discriminant forms (one consolidated parent; axioms select the vocabulary)
# ---------------------------------------------------------------------------

class DiscriminantForm:
    """The finite-abelian-group surface (every finite quotient, form or not)."""

    def invariants(self) -> tuple[int, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def elementary_divisors(self) -> tuple[int, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def cardinality(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def order(self, element: DiscriminantFormElement | None = None) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def exponent(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_cyclic(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def short_name(self) -> str:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def generator_orders(self) -> tuple[int, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def annihilator(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gens(self) -> tuple[DiscriminantFormElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gen(self, i: int) -> DiscriminantFormElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def ngens(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def smith_form_gens(self) -> tuple[DiscriminantFormElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def zero(self) -> DiscriminantFormElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def elements(self) -> tuple[DiscriminantFormElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def discrete_exp(self, coefficients: Sequence[int]) -> DiscriminantFormElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def discrete_log(self, element: DiscriminantFormElement) -> tuple[int, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def subgroup_generated_by(
        self, generators: Sequence[DiscriminantFormElement]
    ) -> "DiscriminantSubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def quotient_group(self, subgroup: "DiscriminantSubgroup") -> "DiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def primary_part(self, p: int) -> "DiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def primary_decomposition(self) -> tuple["DiscriminantForm", ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def all_submodules(self) -> tuple["DiscriminantSubgroup", ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def automorphism_group(self) -> DiscriminantOrthogonalGroup:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def permutation_group(self) -> object:  # the GAP-backed group-theoretic seam
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_finite(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def list(self) -> tuple[DiscriminantFormElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def random_element(self) -> DiscriminantFormElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def coordinates(self, element: DiscriminantFormElement) -> tuple[int, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gens_vector(self, element: DiscriminantFormElement) -> tuple[int, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def smith_form_gen(self, i: int) -> DiscriminantFormElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gens_to_smith(self) -> MorphismMatrix:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def smith_to_gens(self) -> MorphismMatrix:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def linear_combination_of_smith_form_gens(self, coefficients: Sequence[int]) -> DiscriminantFormElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def torsion_subgroup(self) -> "DiscriminantSubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def p_torsion(self, p: int, k: int = 1) -> "DiscriminantSubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def relations_among(self, generators: Sequence[DiscriminantFormElement]) -> MorphismMatrix:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def basis_from_generators(self, generators: Sequence[DiscriminantFormElement]) -> tuple[DiscriminantFormElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def cosets(self, subgroup: "DiscriminantSubgroup") -> tuple[tuple[DiscriminantFormElement, ...], ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def contains_subgroup(self, subgroup: "DiscriminantSubgroup") -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def quotient_map(self, subgroup: "DiscriminantSubgroup") -> Callable[[DiscriminantFormElement], DiscriminantFormElement]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def hom(self, images: Sequence[DiscriminantFormElement]) -> "DiscriminantAction":
        """Endomorphism from generator images; cross-form homs typed at V1."""
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_isomorphic(self, other: "DiscriminantForm", kind: FormKind = "quadratic") -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class BilinearDiscriminantForm(DiscriminantForm):
    def b(
        self, left: DiscriminantFormElement, right: DiscriminantFormElement
    ) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gram_matrix_bilinear(self) -> GramMatrix:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def value_module(self) -> ValueModule:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def radical(self) -> "DiscriminantSubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_nondegenerate(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def orthogonal_submodule_to(self, subgroup: "DiscriminantSubgroup") -> "DiscriminantSubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def orthogonal(self, subgroup: "DiscriminantSubgroup") -> "DiscriminantSubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_isotropic_subgroup(self, subgroup: "DiscriminantSubgroup") -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def isotropic_subgroups(self) -> tuple["DiscriminantSubgroup", ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_lagrangian(self, subgroup: "DiscriminantSubgroup") -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def lagrangian_subgroups(self) -> tuple["DiscriminantSubgroup", ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def metabolizer(self) -> "DiscriminantSubgroup":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_metabolic(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_anisotropic(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def maximal_isotropic_subgroups(self) -> tuple["DiscriminantSubgroup", ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def orthogonal_quotient(self, subgroup: "DiscriminantSubgroup") -> "DiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def orthogonal_group(self) -> DiscriminantOrthogonalGroup:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class QuadraticDiscriminantForm(BilinearDiscriminantForm):
    def q(self, element: DiscriminantFormElement) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gram_matrix_quadratic(self) -> GramMatrix:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def value_module_qf(self) -> ValueModule:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def brown_invariant(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def normal_form(self) -> tuple[tuple[int, ...], GramMatrix]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_genus(self, signature_pair: SignaturePair, even: bool = True) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def genus(self, signature_pair: SignaturePair, even: bool = True) -> "Genus":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def twist(self, scalar: ExactScalar) -> "QuadraticDiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class SourcedDiscriminantForm(QuadraticDiscriminantForm):
    """WithSourceLattice: carries L^*/L provenance."""

    def source_lattice(self) -> IntegralNondegenerateLattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def cover(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def relations(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def cover_lattice(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def relation_lattice(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def lift(self, element: DiscriminantFormElement) -> LatticeElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def projection(self, element: LatticeElement) -> DiscriminantFormElement:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def preimage_lattice(self, subgroup: "DiscriminantSubgroup") -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def overlattice_from_isotropic_subgroup(
        self, subgroup: "DiscriminantSubgroup"
    ) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def discriminant_form_of_overlattice(
        self, subgroup: "DiscriminantSubgroup"
    ) -> "DiscriminantForm":
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def action_of_isometry(self, isometry: LatticeMorphism) -> DiscriminantAction:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def orbit(
        self, element: DiscriminantFormElement, group: DiscriminantOrthogonalGroup
    ) -> tuple[DiscriminantFormElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def orbits(
        self, group: DiscriminantOrthogonalGroup
    ) -> tuple[tuple[DiscriminantFormElement, ...], ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def orbits_on_isotropic_subgroups(
        self, group: DiscriminantOrthogonalGroup
    ) -> tuple[tuple["DiscriminantSubgroup", ...], ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


class DiscriminantSubgroup:
    def ambient(self) -> DiscriminantForm:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def gens(self) -> tuple[DiscriminantFormElement, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def cardinality(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def __contains__(self, element: object) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


# ---------------------------------------------------------------------------
# Genus objects
# ---------------------------------------------------------------------------

class Genus:
    def signature_pair(self) -> SignaturePair:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def signature(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def det(self) -> ExactScalar:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def dim(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_even(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def discriminant_form(self) -> QuadraticDiscriminantForm:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def local_symbol(self, p: int) -> object:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def local_symbols(self) -> tuple[object, ...]:  # the genus-machinery data seam
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def brown_invariant(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def representative(self) -> Lattice:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def representatives(self) -> tuple[Lattice, ...]:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def class_number(self) -> int:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")

    def is_unique_class(self) -> bool:
        raise NotImplementedError("declared contract; engine per the parity-plan triage")


# ---------------------------------------------------------------------------
# Grammar: the constructor family (the ONLY entry into the language).
# Conceptually functors on the category namespace; realized at T1.
# ---------------------------------------------------------------------------

def parse_base_ring(raw: object) -> BaseRing:
    """Codec: asserts raw is ZZ or QQ."""
    raise NotImplementedError("realized at parity-plan T1")


def parse_gram_matrix(raw: RawGramMatrix, ring: BaseRing) -> GramMatrix:
    """Codec: asserts square, symmetric, exact entries over Frac(ring); the
    single place raw matrix data becomes a domain value (ADDD assertions)."""
    raise NotImplementedError("realized at parity-plan T1")


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
