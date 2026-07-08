r"""Operations for the synthetic lattice category (V2 declaration layer).

This module owns the LATTICE-THEORY layer of the spike's typed language:
vocabulary (the nouns, as real typed classes), grammar (the constructor
family — the only entry into the language), transitions (each operation
declared on the narrowest class where the mathematics defines it), and raw
boundary payloads. The full type surface — general mathematical nouns,
scalar/matrix codecs, Sage interop — is the ``lexicon`` package
(``lexicon/INVENTORY.md`` is normative); this module's classes are
re-exported there, and downstream code imports from the lexicon.

SINGLE-SOURCE DESIGN (probe-verified 2026-07-02): the lattice-side classes are
the method-carrying base classes — at T1 each is installed as the ``ParentMethods`` of its category or
axiom class, so the runtime-injected API and this typed language are ONE
artifact (no parallel mirror to drift). Sage copies (does not inherit) these base classes'
attributes into the dynamic parent class, hence narrowing below stays
assertion-shaped rather than isinstance. The morphism/group/discriminant/genus
classes are ordinary ABC-style bases the implementations INHERIT nominally.
Base-class inheritance in this file is static structure only; at runtime each
category injects exactly its own delta. Every contract is a Sage
``abstract_method``: accessing an unimplemented one on a realized parent raises
the standard abstract-method error, so a leaf that fails to shadow a contract is
caught by ``TestSuite(L).run()`` (``_test_not_implemented_methods``) — never
injected as a silent None-returning method.

Rules of the language (authoritative source: the declaration-layer plan record
``lattice-category-mathematical-vocabulary-and-subcategory-tree-declaration-layer``
in the agent-memory vault):

- Two-axis placement: a method appears on the protocol where it is DEFINED;
  a defined-but-unimplemented contract raises the standard abstract signal at
  runtime — absence and abstract-error are different, intentional signals.
- Parse, don't validate: constructors assert their domain contract (ADDD
  style: assert early, dump data, direct to the fix site) and route the
  object into the correct subcategory; nothing downstream re-checks what
  construction proved.
- Dispatch is by declared type / category membership, never hasattr probing.
  The ONLY sanctioned static downcasts are the ``in_*`` narrowing functions at
  the bottom of this module, each assertion-shaped.
- No Sage *type* crosses a domain signature except through the parsed primitives
  and raw boundary aliases; the sole Sage runtime import is ``abstract_method``,
  the contract-declaration decorator (aliased to ``abc.abstractmethod`` under
  TYPE_CHECKING), exactly as in ``objects/categories.py``.
- ``ValueModule`` stays a Protocol deliberately: it types an EXTERNAL object
  (Sage's QmodnZ) that we neither own nor subclass — the one legitimate
  structural-typing use.

This module contains no logic. Contracts are declared with the framework
``abstract_method`` decorator (required — ``TestSuite`` sweeps any leaf that fails
to implement one); all hand-written checks (the ``in_*`` narrowing, constructor
domain contracts) stay ADDD ``assert``s, never a hand-rolled ``raise``. The
runtime realizations live in the concrete modules.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator, Sequence
from typing import TYPE_CHECKING, Any, Literal, Protocol, cast

if TYPE_CHECKING:
    # abstract_method ships untyped; use abc.abstractmethod for type-checking
    from abc import abstractmethod as abstract_method

    from sage.structure.richcmp import richcmp

    # Type-level nouns are drawn from the lexicon (the single type surface;
    # lexicon/INVENTORY.md). TYPE_CHECKING-only, so this module keeps its
    # no-runtime-Sage-import rule.
    from ..lexicon.algebra import (
        BaseRing,
        FreeModule,
        Matrix,
        MatrixGroup,
        PermutationGroup,
        Vector,
    )
    from ..lexicon.foundations import (
        CartanType,
        ExactScalar,
        GramMatrix,
        Integer,
        SignaturePair,
        SymbolicExpression,
    )
    from ..lexicon.geometry import Polyhedron
    from ..lexicon.interop import SageInfinity, SageLocalGenusSymbol
else:
    from sage.misc.abstract_method import abstract_method
    from sage.structure.richcmp import richcmp


__all__ = [
    # boundary codecs (scalar/matrix nouns and witnesses live in the lexicon)
    "RawGramMatrix",
    "RawMorphismMatrix",
    "RawVectors",
    "parse_base_ring",
    "parse_gram_matrix",
    "FormKind",
    # value objects
    "ValueModule",
    # lattice vocabulary
    "Lattice",
    "NondegenerateLattice",
    "IntegralNondegenerateLattice",
    "DefiniteLattice",
    "PositiveDefiniteLattice",
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
    "FiniteAbelianGroup",
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
# through the grammar, and leaves it only at declared Sage-call points)
# ---------------------------------------------------------------------------

type RawGramMatrix = Matrix | MatrixData
"""Untrusted matrix-shaped input to the grammar; parsed once, never circulated."""

type RawMorphismMatrix = Matrix | MatrixData
"""Untrusted matrix-shaped input to homset/element constructors."""

type RawVectors = Matrix | MatrixData | Sequence[Vector]
"""Untrusted family of vectors in given coordinates (rows of a matrix, nested
sequences, or actual vectors) — the input payload of the subobject algebra
(sublattice/span/overlattice generators)."""

type MatrixData = Sequence[Sequence[ExactScalar | int]]
"""Structured matrix-shaped input accepted by overloads that route through
`Matrix` (Python int literals are exact integers and enter freely)."""


type FormKind = Literal["group", "bilinear", "quadratic"]


class ValueModule(Protocol):
    """The form-value object K/(level*R): QQ/ZZ (bilinear) or QQ/2ZZ (even quadratic)."""

    @abstract_method
    def level(self) -> ExactScalar: ...

    @abstract_method
    def __call__(self, value: ExactScalar) -> ExactScalar: ...


# ---------------------------------------------------------------------------
# Elements
# ---------------------------------------------------------------------------


class LatticeElement:
    @abstract_method
    def parent(self) -> Lattice: ...

    @abstract_method
    def coefficient_vector(self) -> Vector:
        """The element's coordinates in the parent's distinguished basis — a
        genuine vector of the coefficient module (arithmetic flows through the
        module structure), never a bare sequence."""

    @abstract_method
    def b(self, other: LatticeElement) -> ExactScalar: ...

    @abstract_method
    def q(self) -> ExactScalar: ...

    def _richcmp_(self, other: LatticeElement, op: int) -> bool:
        r"""Compare as linear combinations of the generators: two elements agree
        iff they have equal coefficient tuples in the shared generating set.

        This is the sole comparison primitive lattice elements own. ``is_zero``
        and ``__bool__`` are inherited from the additive-group chain
        (``AdditiveMagmas.AdditiveUnital`` up through ``Element``) and delegate
        here, so zero-ness follows from the module's group structure rather than
        being hand-written. Sage calls ``_richcmp_`` only after coercing both
        operands into a common parent, so the parent match is the coercion
        framework's responsibility, not ours."""
        return richcmp(self.coefficient_vector(), other.coefficient_vector(), op)

    def __hash__(self) -> int:
        r"""Hash by generator coefficients (a hashable immutable vector).

        Sage's ``Element`` sets ``__hash__ = None`` -- rich comparison is defined
        at the C level and every element subclass must opt into hashing -- so
        without this, lattice elements are unusable in sets/dicts/caches. Keyed on
        the same coefficients ``_richcmp_`` compares, so equal elements hash
        equally."""
        return hash(self.coefficient_vector())

    def _repr_(self) -> str:
        r"""Render as the formal R-combination ``sum_i c_i e_i`` over the NONZERO
        coefficients, using the intrinsic generator symbols ``e_0, ..., e_{n-1}``
        -- the ordered symbol set ``S`` with ``L = R[S]`` -- never the raw
        coordinate vector.

        Each coefficient is rendered by the ring's OWN repr: ``-3`` in ``ZZ``
        renders as ``-3``. An arbitrary ring ``R`` has no absolute value and no
        sign to strip, so a term is just ``repr(c_i)`` next to ``repr(e_i)``. The
        empty combination (every coefficient zero) is ``0``."""
        terms = [f"{coefficient} e_{index}" for index, coefficient in enumerate(self.coefficient_vector()) if coefficient != 0]
        return " + ".join(terms) if terms else "0"


class DiscriminantFormElement:
    @abstract_method
    def parent(self) -> DiscriminantForm: ...

    @abstract_method
    def b(self, other: DiscriminantFormElement) -> ExactScalar: ...

    @abstract_method
    def q(self) -> ExactScalar: ...

    @abstract_method
    def lift(self) -> LatticeElement:
        """Coset lift to the dual lattice; meaningful for sourced forms."""

    @abstract_method
    def coefficient_vector(self) -> Vector:
        """Coordinates with respect to the group's distinguished generators
        (integer residues, exactly represented)."""

    @abstract_method
    def order(self) -> int: ...


# ---------------------------------------------------------------------------
# Lattices: the base vocabulary (defined for EVERY lattice, degenerate included)
# ---------------------------------------------------------------------------


class Lattice:
    """A based free R-module (R, G) with symmetric bilinear form; possibly degenerate."""

    # structural
    @abstract_method
    def rank(self) -> int: ...

    @abstract_method
    def gram_matrix(self) -> GramMatrix: ...

    @abstract_method
    def base_ring(self) -> BaseRing: ...

    @abstract_method
    def b(self, left: LatticeElement, right: LatticeElement) -> ExactScalar: ...

    @abstract_method
    def q(self, element: LatticeElement) -> ExactScalar: ...

    @abstract_method
    def bilinear_form(self) -> Callable[[LatticeElement, LatticeElement], ExactScalar]: ...

    @abstract_method
    def quadratic_form(self) -> Callable[[LatticeElement], ExactScalar]: ...

    @abstract_method
    def basis(self) -> tuple[LatticeElement, ...]: ...

    @abstract_method
    def gens(self) -> tuple[LatticeElement, ...]: ...

    @abstract_method
    def gen(self, i: int) -> LatticeElement: ...

    @abstract_method
    def ngens(self) -> int: ...

    @abstract_method
    def zero(self) -> LatticeElement: ...

    @abstract_method
    def determinant(self) -> ExactScalar: ...

    @abstract_method
    def discriminant(self) -> ExactScalar: ...

    @abstract_method
    def absolute_discriminant(self) -> ExactScalar: ...

    @abstract_method
    def signature_pair(self) -> SignaturePair: ...

    @abstract_method
    def signature(self) -> int: ...

    @abstract_method
    def denominator(self) -> ExactScalar: ...

    @abstract_method
    def random_element(self) -> LatticeElement:
        """Contracted into the owned public API (user ruling): sensible utility;
        the leaner super-category no longer inherits it, so we own it."""

    @abstract_method
    def clear_denominators(self) -> Lattice: ...

    # predicates (total; used by the narrowing functions below)
    @abstract_method
    def is_integral(self) -> bool: ...

    @abstract_method
    def is_even(self) -> bool: ...

    @abstract_method
    def is_unimodular(self) -> bool: ...

    @abstract_method
    def is_degenerate(self) -> bool: ...

    @abstract_method
    def is_nondegenerate(self) -> bool: ...

    @abstract_method
    def is_definite(self) -> bool: ...

    @abstract_method
    def is_positive_definite(self) -> bool: ...

    @abstract_method
    def is_negative_definite(self) -> bool: ...

    @abstract_method
    def is_indefinite(self) -> bool: ...

    @abstract_method
    def is_hyperbolic(self) -> bool: ...

    # radical theory (the functor that STAYS a lattice)
    @abstract_method
    def radical(self) -> Lattice: ...

    @abstract_method
    def radical_quotient(self) -> NondegenerateLattice: ...

    # constructions
    @abstract_method
    def twist(self, scalar: ExactScalar | int, label: str = "twist") -> Lattice: ...

    @abstract_method
    def scale(self, scalar: ExactScalar | int, label: str = "scale") -> Lattice: ...

    @abstract_method
    def direct_sum(self, other: Lattice, label: str = "direct_sum") -> Lattice: ...

    @abstract_method
    def tensor_product(self, other: Lattice) -> Lattice: ...

    @abstract_method
    def rationalization(self) -> Lattice: ...

    @abstract_method
    def base_extend(self, ring: BaseRing) -> Lattice: ...

    # subobject algebra (generator families enter as RawVectors payloads)
    @abstract_method
    def sublattice(self, generators: RawVectors) -> Lattice: ...

    @abstract_method
    def lattice_in_rationalization(self, generators: RawVectors) -> Lattice: ...

    @abstract_method
    def span(self, generators: RawVectors) -> Lattice: ...

    @abstract_method
    def span_of_basis(self, basis: RawVectors) -> Lattice: ...

    @abstract_method
    def sum(self, other: Lattice) -> Lattice: ...

    @abstract_method
    def intersection(self, other: Lattice) -> Lattice: ...

    @abstract_method
    def saturation(self) -> Lattice: ...

    @abstract_method
    def primitive_closure(self, ambient: Lattice) -> Lattice: ...

    @abstract_method
    def index_in(self, other: Lattice) -> ExactScalar: ...

    @abstract_method
    def index_in_saturation(self) -> ExactScalar: ...

    @abstract_method
    def is_submodule(self, other: Lattice) -> bool: ...

    @abstract_method
    def is_primitive(self, sublattice: Lattice) -> bool: ...

    @abstract_method
    def overlattice(
        self,
        generators: RawVectors,
        check_integral: bool = False,
        label: str = "overlattice",
    ) -> Lattice: ...

    @abstract_method
    def orthogonal_complement(self, other: Lattice) -> Lattice: ...

    @abstract_method
    def zero_lattice(self) -> Lattice: ...

    # quotients (the functor that LEAVES: plain finite abelian quotient, no form axioms)
    @abstract_method
    def finite_quotient(self, sublattice: Lattice) -> FiniteAbelianGroup: ...

    @abstract_method
    def _rationalization_module(self) -> FreeModule: ...

    @abstract_method
    def _underlying_module(self) -> FreeModule: ...

    # morphisms
    @abstract_method
    def Hom(self, codomain: Lattice) -> LatticeHomset: ...

    @abstract_method
    def hom(self, matrix: RawMorphismMatrix, codomain: Lattice) -> LatticeMorphism: ...

    @abstract_method
    def embedding(self, matrix: RawMorphismMatrix, codomain: Lattice) -> LatticeMorphism: ...

    @abstract_method
    def similarity(self, matrix: RawMorphismMatrix, codomain: Lattice, scalar: ExactScalar) -> LatticeSimilarity: ...

    @abstract_method
    def reflection(self, vector: LatticeElement) -> LatticeMorphism: ...

    # groups and isometry
    @abstract_method
    def isometry_group(self) -> IsometryGroup: ...

    @abstract_method
    def is_isometric(self, other: Lattice) -> bool: ...


# ---------------------------------------------------------------------------
# Subcategory vocabularies (axis 1: definedness -> placement, as types)
# ---------------------------------------------------------------------------


class NondegenerateLattice(Lattice):
    @abstract_method
    def dual(self) -> NondegenerateLattice:
        """The dual lattice (Gram ``G^{-1}`` in the dual basis) — itself
        nondegenerate, so the dual vocabulary is closed on this tier."""

    @abstract_method
    def dual_inclusion(self) -> LatticeMorphism: ...

    @abstract_method
    def is_self_dual(self) -> bool:
        """Defined through ``dual()``, so placed exactly where the dual exists
        (a degenerate lattice has no dual, hence no self-duality question)."""


class IntegralNondegenerateLattice(NondegenerateLattice):
    @abstract_method
    def discriminant_group(self, primary: int | Integer = 0) -> SourcedDiscriminantForm: ...

    @abstract_method
    def genus(self) -> Genus: ...

    @abstract_method
    def same_genus(self, other: IntegralNondegenerateLattice) -> bool: ...

    @abstract_method
    def glue(self, isotropic_subgroup: DiscriminantSubgroup) -> Lattice: ...

    @abstract_method
    def maximal_overlattice(self, p: int | None = None) -> Lattice: ...

    @abstract_method
    def local_modification(self, data: Matrix | DiscriminantSubgroup | Sequence[DiscriminantFormElement], p: int) -> Lattice: ...

    @abstract_method
    def embeds_primitively_in_unimodular(self, signature_pair: SignaturePair, even: bool = True) -> bool: ...

    @abstract_method
    def primitive_embedding_into_unimodular(self, signature_pair: SignaturePair, even: bool = True) -> LatticeMorphism: ...


class DefiniteLattice(Lattice):
    """Finite-enumeration vocabulary. Semantics for the negative-definite case
    are gap-ledger item 4 (ratified interactively), not fixed by this stub."""

    @abstract_method
    def minimum(self) -> ExactScalar | SageInfinity:
        """Least nonzero norm; ``+Infinity`` on the rank-0 lattice (an infimum
        over the empty set), so the codomain honestly includes infinity."""

    @abstract_method
    def maximum(self) -> ExactScalar | SageInfinity:
        """Supremum of the norm form over nonzero vectors — ``+-Infinity`` for
        every positive-rank definite lattice."""

    @abstract_method
    def shortest_vector(self) -> LatticeElement: ...

    @abstract_method
    def short_vectors(self, bound: int | Integer) -> Sequence[Sequence[LatticeElement]]: ...

    @abstract_method
    def enumerate_short_vectors(self, bound: int | Integer) -> Iterator[LatticeElement]: ...

    @abstract_method
    def vectors_of_square(self, square: ExactScalar | int) -> tuple[LatticeElement, ...]: ...

    @abstract_method
    def roots(self) -> tuple[LatticeElement, ...]: ...

    @abstract_method
    def volume(self) -> ExactScalar | SymbolicExpression:
        """Covolume ``sqrt(det G)`` — exact, but not rational in general, so the
        codomain includes exact symbolic values (never a float)."""


class PositiveDefiniteLattice(DefiniteLattice):
    """Home of the reduction/CVP/Voronoi suite (decision D1 revised 2026-07-04):
    Sage's own crypto lattice implementations presuppose exactly positive
    definiteness, so the suite is ordinary vocabulary here, never opt-in."""

    @abstract_method
    def LLL(self) -> PositiveDefiniteLattice: ...

    @abstract_method
    def reduced_basis(self) -> tuple[LatticeElement, ...]: ...

    @abstract_method
    def BKZ(self, block_size: int = 10) -> PositiveDefiniteLattice: ...

    @abstract_method
    def HKZ(self) -> PositiveDefiniteLattice: ...

    @abstract_method
    def babai(self, target: Sequence[ExactScalar] | Vector | LatticeElement) -> LatticeElement: ...

    @abstract_method
    def approximate_closest_vector(self, target: Sequence[ExactScalar] | Vector | LatticeElement) -> LatticeElement: ...

    @abstract_method
    def closest_vector(self, target: Sequence[ExactScalar] | Vector | LatticeElement) -> LatticeElement: ...

    @abstract_method
    def enumerate_close_vectors(self, target: Sequence[ExactScalar] | Vector | LatticeElement, radius: ExactScalar) -> Sequence[LatticeElement]: ...

    @abstract_method
    def voronoi_cell(self, radius: int | Integer | None = None) -> Polyhedron: ...

    @abstract_method
    def voronoi_relevant_vectors(self) -> tuple[LatticeElement, ...]: ...

    @abstract_method
    def gaussian_heuristic(self) -> SymbolicExpression:
        """Exact symbolic expected-shortest-length (Gamma/pi/e expressions);
        gap-ledger row 12 — the value is symbolic, never a float."""

    @abstract_method
    def hadamard_ratio(self) -> SymbolicExpression:
        """Exact symbolic ratio (n-th roots of square roots); never a float."""

    @abstract_method
    def update_reduced_basis(self, vector: LatticeElement) -> PositiveDefiniteLattice: ...


class IndefiniteLattice(Lattice):
    @abstract_method
    def has_isotropic_vector(self) -> bool: ...

    @abstract_method
    def isotropic_vectors(self, bound: int) -> tuple[LatticeElement, ...]: ...

    @abstract_method
    def primitive_isotropic_vectors(self, bound: int) -> tuple[LatticeElement, ...]: ...


class HyperbolicLattice(IndefiniteLattice):
    """Signature (1, rank-1). Names fixed now; the implementations are the Vinberg workstream."""

    @abstract_method
    def weyl_group(self) -> IsometrySubgroup: ...

    @abstract_method
    def fundamental_chamber(self) -> Polyhedron: ...

    @abstract_method
    def is_reflective(self) -> bool: ...

    @abstract_method
    def roots_up_to_height(self, height: ExactScalar) -> tuple[LatticeElement, ...]: ...

    @abstract_method
    def isotropic_rays(self) -> tuple[LatticeElement, ...]: ...


class RootGeneratedLattice(Lattice):
    """Attached ONLY by construction provenance (the certificate), never detected."""

    @abstract_method
    def cartan_type(self) -> CartanType: ...

    @abstract_method
    def irreducible_root_components(self) -> tuple[RootGeneratedLattice, ...]: ...


# ---------------------------------------------------------------------------
# Morphisms
# ---------------------------------------------------------------------------


class LatticeMorphism:
    """Form-preserving by construction: A^T G_M A = G_L, enforced at creation."""

    @abstract_method
    def domain(self) -> Lattice: ...

    @abstract_method
    def codomain(self) -> Lattice: ...

    @abstract_method
    def matrix(self) -> Matrix:  # where the morphism meets Sage matrix spaces
        ...

    @abstract_method
    def __call__(self, element: LatticeElement) -> LatticeElement: ...

    @abstract_method
    def is_isometry(self) -> bool: ...

    # ring-LIKE predicates (V0d amendment 2026-07-03): End_Lat(L) = Hom(L, L) is the
    # form-preserving composition MONOID (operations escaping into End_{ZZ-Mod}(L) are
    # not vocabulary), but the monoid sits inside a ring, so ring-like QUERIES remain
    # well-defined on endomorphisms and are shimmed in here, curated against what
    # module-endomorphism and ring-element implementations actually expose.
    @abstract_method
    def is_identity(self) -> bool: ...

    @abstract_method
    def is_nilpotent(self) -> bool: ...

    @abstract_method
    def is_idempotent(self) -> bool: ...

    @abstract_method
    def is_unipotent(self) -> bool: ...

    @abstract_method
    def order(self) -> int | SageInfinity:
        """Multiplicative order in N ∪ {+Infinity} (endomorphisms only)."""

    @abstract_method
    def is_injective(self) -> bool: ...

    @abstract_method
    def is_surjective(self) -> bool: ...

    @abstract_method
    def is_primitive_embedding(self) -> bool:
        """Injective with primitive (saturated) image in the codomain —
        equivalently, torsion-free module cokernel."""

    @abstract_method
    def kernel(self) -> Lattice: ...

    @abstract_method
    def image(self) -> Lattice: ...

    @abstract_method
    def cokernel(self) -> DiscriminantForm:
        """Finite-cokernel case only; the general case is a gap-ledger contract."""

    @abstract_method
    def induced_map_on_discriminant_group(self) -> DiscriminantAction: ...

    """Per-element functor; defined when domain == codomain is integral nondegenerate."""


class LatticeSimilarity:
    """A similitude: ``b(f x, f y) = scalar * b(x, y)`` for a fixed multiplier
    (O'Meara, Introduction to Quadratic Forms, §42; ``scalar = 1`` recovers
    isometry). Mostly a convenient generalization for discussing symmetric and
    skew-symmetric forms at once (ruling 2026-07-08); distinct from a
    homothety ``x -> scalar * x``, which multiplies the form by ``scalar**2``."""

    @abstract_method
    def domain(self) -> Lattice: ...

    @abstract_method
    def codomain(self) -> Lattice: ...

    @abstract_method
    def matrix(self) -> Matrix: ...

    @abstract_method
    def scalar(self) -> ExactScalar: ...

    @abstract_method
    def __call__(self, element: LatticeElement) -> LatticeElement: ...


class LatticeHomset:
    @abstract_method
    def domain(self) -> Lattice: ...

    @abstract_method
    def codomain(self) -> Lattice: ...

    @abstract_method
    def from_matrix(self, matrix: RawMorphismMatrix) -> LatticeMorphism: ...


# ---------------------------------------------------------------------------
# Isometry groups (O(L) exists for EVERY lattice; enumeration is per-leaf)
# ---------------------------------------------------------------------------


class IsometryGroup:
    """O(L). Membership/construction/is_finite are total; gens/order/iteration
    are contracts implemented exactly where the group is finite."""

    @abstract_method
    def lattice(self) -> Lattice: ...

    @abstract_method
    def __contains__(self, candidate: Any) -> bool: ...

    @abstract_method
    def from_matrix(self, matrix: RawMorphismMatrix) -> LatticeMorphism: ...

    @abstract_method
    def one(self) -> LatticeMorphism: ...

    @abstract_method
    def is_finite(self) -> bool: ...

    @abstract_method
    def gens(self) -> tuple[LatticeMorphism, ...]: ...

    @abstract_method
    def order(self) -> int: ...

    @abstract_method
    def __iter__(self) -> Iterator[LatticeMorphism]: ...

    @abstract_method
    def subgroup(self, generators: Sequence[LatticeMorphism]) -> IsometrySubgroup: ...

    @abstract_method
    def discriminant_action(self, isometry: LatticeMorphism) -> DiscriminantAction: ...

    @abstract_method
    def discriminant_representation(self) -> DiscriminantOrthogonalGroup: ...

    @abstract_method
    def stable_kernel(self) -> IsometrySubgroup: ...

    # structure vocabulary through the GAP seams (gap-ledger row 9e)
    @abstract_method
    def structure_description(self) -> str: ...

    @abstract_method
    def conjugacy_classes_representatives(self) -> tuple[LatticeMorphism, ...]: ...

    # points where Sage is called (implemented exactly where finite with computed generators)
    @abstract_method
    def as_matrix_group(self) -> MatrixGroup: ...

    @abstract_method
    def as_permutation_group(self) -> PermutationGroup: ...


class IsometrySubgroup:
    """<gens> <= O(L): the ONLY home for caller-supplied generators. Answers
    subgroup questions only — no membership test, no O(L)-level claims."""

    @abstract_method
    def lattice(self) -> Lattice: ...

    @abstract_method
    def ambient(self) -> IsometryGroup: ...

    @abstract_method
    def gens(self) -> tuple[LatticeMorphism, ...]: ...

    @abstract_method
    def preserves(self, sublattice: Lattice) -> bool: ...

    @abstract_method
    def discriminant_image(self) -> DiscriminantOrthogonalGroup: ...

    @abstract_method
    def order(self) -> int:  # implemented only when the ambient is finite
        ...

    @abstract_method
    def __iter__(self) -> Iterator[LatticeMorphism]: ...

    @abstract_method
    def as_matrix_group(self) -> MatrixGroup: ...

    @abstract_method
    def as_permutation_group(self) -> PermutationGroup: ...


class DiscriminantOrthogonalGroup:
    """O(q) (or a subgroup of it): FINITE for every discriminant form, so the
    full set of group operations is total on this side."""

    @abstract_method
    def discriminant_form(self) -> DiscriminantForm: ...

    @abstract_method
    def gens(self) -> tuple[DiscriminantAction, ...]: ...

    @abstract_method
    def order(self) -> int: ...

    @abstract_method
    def __contains__(self, candidate: Any) -> bool: ...

    @abstract_method
    def __iter__(self) -> Iterator[DiscriminantAction]: ...

    @abstract_method
    def as_matrix_group(self) -> MatrixGroup: ...

    @abstract_method
    def as_permutation_group(self) -> PermutationGroup: ...


class DiscriminantAction:
    @abstract_method
    def discriminant_form(self) -> DiscriminantForm: ...

    @abstract_method
    def matrix(self) -> Matrix: ...

    @abstract_method
    def __call__(self, element: DiscriminantFormElement) -> DiscriminantFormElement: ...

    @abstract_method
    def is_identity(self) -> bool: ...

    @abstract_method
    def inverse(self) -> DiscriminantAction: ...

    @abstract_method
    def preserves_bilinear_form(self) -> bool: ...

    @abstract_method
    def preserves_quadratic_form(self) -> bool: ...


# ---------------------------------------------------------------------------
# Discriminant forms (one consolidated parent; axioms select the vocabulary)
# ---------------------------------------------------------------------------


class FiniteAbelianGroup:
    """Finite abelian group with the full structure vocabulary (invariants,
    primary decomposition, subgroup lattice) — every finite quotient, form or
    not. This is the group layer of the discriminant tower; the form-carrying
    vocabulary starts at ``BilinearDiscriminantForm``."""

    @abstract_method
    def invariants(self) -> tuple[int, ...]: ...

    @abstract_method
    def elementary_divisors(self) -> tuple[int, ...]: ...

    @abstract_method
    def cardinality(self) -> int: ...

    @abstract_method
    def order(self, element: DiscriminantFormElement | None = None) -> int: ...

    @abstract_method
    def exponent(self) -> int: ...

    @abstract_method
    def is_cyclic(self) -> bool: ...

    @abstract_method
    def short_name(self) -> str: ...

    @abstract_method
    def generator_orders(self) -> tuple[int, ...]: ...

    @abstract_method
    def annihilator(self) -> ExactScalar: ...

    @abstract_method
    def gens(self) -> tuple[DiscriminantFormElement, ...]: ...

    @abstract_method
    def gen(self, i: int) -> DiscriminantFormElement: ...

    @abstract_method
    def ngens(self) -> int: ...

    @abstract_method
    def invariant_factor_gens(self) -> tuple[DiscriminantFormElement, ...]: ...

    @abstract_method
    def zero(self) -> DiscriminantFormElement: ...

    @abstract_method
    def elements(self) -> tuple[DiscriminantFormElement, ...]: ...

    @abstract_method
    def discrete_exp(self, coefficients: Sequence[int]) -> DiscriminantFormElement: ...

    @abstract_method
    def discrete_log(self, element: DiscriminantFormElement) -> tuple[int, ...]: ...

    @abstract_method
    def subgroup_generated_by(self, generators: Sequence[DiscriminantFormElement]) -> DiscriminantSubgroup: ...

    @abstract_method
    def quotient_group(self, subgroup: DiscriminantSubgroup) -> DiscriminantForm: ...

    @abstract_method
    def primary_part(self, p: int) -> DiscriminantForm: ...

    @abstract_method
    def primary_decomposition(self) -> tuple[DiscriminantForm, ...]: ...

    @abstract_method
    def all_submodules(self) -> tuple[DiscriminantSubgroup, ...]: ...

    @abstract_method
    def automorphism_group(self) -> DiscriminantOrthogonalGroup: ...

    @abstract_method
    def permutation_group(
        self,
    ) -> PermutationGroup:  # the GAP-backed permutation-group entry point
        ...

    @abstract_method
    def is_finite(self) -> bool: ...

    @abstract_method
    def list(self) -> tuple[DiscriminantFormElement, ...]: ...

    @abstract_method
    def random_element(self) -> DiscriminantFormElement: ...

    @abstract_method
    def coordinates(self, element: DiscriminantFormElement) -> tuple[int, ...]: ...

    @abstract_method
    def gens_vector(self, element: DiscriminantFormElement) -> tuple[int, ...]: ...

    @abstract_method
    def invariant_factor_gen(self, i: int) -> DiscriminantFormElement: ...

    @abstract_method
    def gens_to_invariant_factor_gens(self) -> Matrix: ...

    @abstract_method
    def invariant_factor_gens_to_gens(self) -> Matrix: ...

    @abstract_method
    def linear_combination_of_invariant_factor_gens(self, coefficients: Sequence[int]) -> DiscriminantFormElement: ...

    @abstract_method
    def torsion_subgroup(self) -> DiscriminantSubgroup: ...

    @abstract_method
    def p_torsion(self, p: int, k: int = 1) -> DiscriminantSubgroup: ...

    @abstract_method
    def relations_among(self, generators: Sequence[DiscriminantFormElement]) -> Matrix: ...

    @abstract_method
    def basis_from_generators(self, generators: Sequence[DiscriminantFormElement]) -> tuple[DiscriminantFormElement, ...]: ...

    @abstract_method
    def cosets(self, subgroup: DiscriminantSubgroup) -> tuple[tuple[DiscriminantFormElement, ...], ...]: ...

    @abstract_method
    def contains_subgroup(self, subgroup: DiscriminantSubgroup) -> bool: ...

    @abstract_method
    def quotient_map(self, subgroup: DiscriminantSubgroup) -> Callable[[DiscriminantFormElement], DiscriminantFormElement]: ...

    @abstract_method
    def hom(self, images: Sequence[DiscriminantFormElement]) -> DiscriminantAction:
        """Endomorphism from generator images; cross-form homs typed at V1."""

    @abstract_method
    def is_isomorphic(self, other: FiniteAbelianGroup) -> bool:
        """Group isomorphism — finite abelian groups are classified by their
        invariant factors, so this tier decides isomorphism in the category of
        torsion ZZ-modules. The form-carrying subcategories override with the
        finer ``kind`` selector (their objects live in categories of pairs)."""


DiscriminantForm = FiniteAbelianGroup
"""Transitional compatibility alias (M4, 2026-07-08) — the bare noun is
DEPRECATED in the lexicon because it conflates two ontologically different
objects: a torsion ZZ-module ``G`` (``FiniteAbelianGroup``) and a pair
``(G, b)`` or ``(G, q)`` (``BilinearDiscriminantForm`` /
``QuadraticDiscriminantForm``). Each annotation site must migrate to the
object it actually means; over ZZ the bilinear and quadratic theories are
qualitatively different and NOT interchangeable (Sterk, symmetric forms book
— ruling 2026-07-08), so the form-carrying sites must choose Bilinear vs
Quadratic deliberately, never a generic "form"."""


class BilinearDiscriminantForm(FiniteAbelianGroup):
    @abstract_method
    def q(self, element: DiscriminantFormElement) -> ExactScalar:
        """The induced diagonal quadratic form q(x) := b(x, x) (placement
        ruling 2026-07-03): every bilinear form induces a quadratic form along
        the diagonal — only polarization needs 2 invertible — so q is DEFINED
        on the Bilinear subcategory (values in the bilinear value module); the
        Quadratic subcategory refines it (finer value module)."""

    @abstract_method
    def b(self, left: DiscriminantFormElement, right: DiscriminantFormElement) -> ExactScalar: ...

    @abstract_method
    def gram_matrix_bilinear(self) -> GramMatrix: ...

    @abstract_method
    def value_module(self) -> ValueModule: ...

    @abstract_method
    def radical(self) -> DiscriminantSubgroup: ...

    @abstract_method
    def is_nondegenerate(self) -> bool: ...

    @abstract_method
    def orthogonal_submodule_to(self, subgroup: DiscriminantSubgroup) -> DiscriminantSubgroup: ...

    @abstract_method
    def orthogonal(self, subgroup: DiscriminantSubgroup) -> DiscriminantSubgroup: ...

    @abstract_method
    def is_isotropic_subgroup(self, subgroup: DiscriminantSubgroup) -> bool: ...

    @abstract_method
    def isotropic_subgroups(self) -> tuple[DiscriminantSubgroup, ...]: ...

    @abstract_method
    def is_lagrangian(self, subgroup: DiscriminantSubgroup) -> bool: ...

    @abstract_method
    def lagrangian_subgroups(self) -> tuple[DiscriminantSubgroup, ...]: ...

    @abstract_method
    def metabolizer(self) -> DiscriminantSubgroup: ...

    @abstract_method
    def is_metabolic(self) -> bool: ...

    @abstract_method
    def is_anisotropic(self) -> bool: ...

    @abstract_method
    def maximal_isotropic_subgroups(self) -> tuple[DiscriminantSubgroup, ...]: ...

    @abstract_method
    def orthogonal_quotient(self, subgroup: DiscriminantSubgroup) -> DiscriminantForm: ...

    @abstract_method
    def orthogonal_group(self) -> DiscriminantOrthogonalGroup: ...

    @abstract_method
    def is_isomorphic(self, other: FiniteAbelianGroup, kind: FormKind = "quadratic") -> bool:
        """Isomorphism in the selected category: the underlying group
        (``kind="group"``), the pair (G, b) (``"bilinear"``), or the pair
        (G, q) (``"quadratic"``); the theories are distinct over ZZ."""


class QuadraticDiscriminantForm(BilinearDiscriminantForm):
    @abstract_method
    def q(self, element: DiscriminantFormElement) -> ExactScalar: ...

    @abstract_method
    def gram_matrix_quadratic(self) -> GramMatrix: ...

    @abstract_method
    def value_module_qf(self) -> ValueModule: ...

    @abstract_method
    def brown_invariant(self) -> int: ...

    @abstract_method
    def miranda_morrison_normal_form(self) -> tuple[tuple[int, ...], GramMatrix]: ...

    @abstract_method
    def is_genus(self, signature_pair: SignaturePair, even: bool = True) -> bool: ...

    @abstract_method
    def genus(self, signature_pair: SignaturePair, even: bool = True) -> Genus: ...

    @abstract_method
    def twist(self, scalar: ExactScalar) -> QuadraticDiscriminantForm: ...


class SourcedDiscriminantForm(QuadraticDiscriminantForm):
    """WithSourceLattice: carries L^*/L provenance."""

    @abstract_method
    def source_lattice(self) -> IntegralNondegenerateLattice: ...

    @abstract_method
    def cover(self) -> Lattice: ...

    @abstract_method
    def relations(self) -> Lattice: ...

    @abstract_method
    def cover_lattice(self) -> Lattice: ...

    @abstract_method
    def relation_lattice(self) -> Lattice: ...

    @abstract_method
    def lift(self, element: DiscriminantFormElement) -> LatticeElement: ...

    @abstract_method
    def _coset_representative_in_source(self, element: DiscriminantFormElement) -> Sequence[ExactScalar]: ...

    @abstract_method
    def projection(self, element: LatticeElement) -> DiscriminantFormElement: ...

    @abstract_method
    def preimage_lattice(self, subgroup: DiscriminantSubgroup) -> Lattice: ...

    @abstract_method
    def overlattice_from_isotropic_subgroup(
        self,
        subgroup: DiscriminantSubgroup | Sequence[DiscriminantFormElement],
        label: str = "overlattice",
    ) -> IntegralNondegenerateLattice:
        """Gluing along an isotropic subgroup preserves rank and integrality
        and scales the determinant by the square of the index, so the result
        is again integral nondegenerate."""

    @abstract_method
    def discriminant_form_of_overlattice(self, subgroup: DiscriminantSubgroup) -> DiscriminantForm: ...

    @abstract_method
    def action_of_isometry(self, isometry: LatticeMorphism) -> DiscriminantAction: ...

    @abstract_method
    def orbit(self, element: DiscriminantFormElement, group: DiscriminantOrthogonalGroup) -> tuple[DiscriminantFormElement, ...]: ...

    @abstract_method
    def orbits(self, group: DiscriminantOrthogonalGroup) -> tuple[tuple[DiscriminantFormElement, ...], ...]: ...

    @abstract_method
    def orbits_on_isotropic_subgroups(self, group: DiscriminantOrthogonalGroup) -> tuple[tuple[DiscriminantSubgroup, ...], ...]: ...


class DiscriminantSubgroup:
    @abstract_method
    def ambient(self) -> DiscriminantForm: ...

    @abstract_method
    def gens(self) -> tuple[DiscriminantFormElement, ...]: ...

    @abstract_method
    def cardinality(self) -> int: ...

    @abstract_method
    def __contains__(self, element: Any) -> bool: ...

    @abstract_method
    def is_bilinear_isotropic(self) -> bool:
        """b restricts to zero on the subgroup."""

    @abstract_method
    def is_quadratic_isotropic(self) -> bool:
        """q restricts to zero on the subgroup (strictly stronger than
        bilinear isotropy over ZZ)."""


# ---------------------------------------------------------------------------
# Genus objects
# ---------------------------------------------------------------------------


class Genus:
    @abstract_method
    def signature_pair(self) -> SignaturePair: ...

    @abstract_method
    def signature(self) -> int: ...

    @abstract_method
    def det(self) -> ExactScalar: ...

    @abstract_method
    def dim(self) -> int: ...

    @abstract_method
    def is_even(self) -> bool: ...

    @abstract_method
    def discriminant_form(self) -> QuadraticDiscriminantForm: ...

    @abstract_method
    def local_symbol(self, p: int) -> SageLocalGenusSymbol: ...

    @abstract_method
    def local_symbols(
        self,
    ) -> tuple[SageLocalGenusSymbol, ...]:  # the data handed to Sage genus machinery
        ...

    # per-prime symbol extraction (gap-ledger G2): Conway-Sloane constituent
    # tuples and the local scalar data, enough to state Nikulin local conditions
    @abstract_method
    def local_symbol_tuples(self, p: int) -> tuple[tuple[int, ...], ...]: ...

    @abstract_method
    def local_determinant(self, p: int) -> ExactScalar: ...

    @abstract_method
    def local_rank(self, p: int) -> int: ...

    @abstract_method
    def local_excess(self, p: int) -> int: ...

    @abstract_method
    def local_level(self, p: int) -> int: ...

    @abstract_method
    def is_locally_even(self, p: int) -> bool: ...

    @abstract_method
    def brown_invariant(self) -> int: ...

    @abstract_method
    def representative(self) -> Lattice: ...

    @abstract_method
    def representatives(self) -> tuple[Lattice, ...]: ...

    @abstract_method
    def class_number(self) -> int: ...

    @abstract_method
    def is_unique_class(self) -> bool: ...


# ---------------------------------------------------------------------------
# Grammar: the constructor family (the ONLY entry into the language).
# Conceptually functors on the category namespace; realized at T1.
# ---------------------------------------------------------------------------


def parse_base_ring(raw: BaseRing) -> BaseRing:
    """Codec: asserts raw is ZZ or QQ."""
    assert False, "typed declaration only; the runtime entry is Lattices(R).from_gram_matrix / constructors.py (realized at T1)"


def parse_gram_matrix(raw: RawGramMatrix, ring: BaseRing) -> GramMatrix:
    """Codec: asserts square, symmetric, exact entries over Frac(ring); the
    single place raw matrix data becomes a domain value (ADDD assertions)."""
    assert False, "typed declaration only; the runtime entry is Lattices(R).from_gram_matrix / constructors.py (realized at T1)"


def from_gram_matrix(gram: RawGramMatrix, base_ring: BaseRing | None = None, label: str = "L") -> Lattice:
    """Functor from square symmetric matrices over R into Lattices(R).

    Asserts its domain contract (square, symmetric, R in {ZZ, QQ}) ADDD-style
    and routes the object into the correct subcategory (nondegenerate/degenerate,
    integrality/parity/unimodularity, definiteness, hyperbolic). The
    skew-symmetric branch is a reserved future extension of the domain
    stratification, excluded today by the symmetry assertion.
    """
    assert False, "typed declaration only; the runtime entry is Lattices(R).from_gram_matrix / constructors.py (realized at T1)"


def from_form_data(
    invariants: Sequence[int],
    bilinear: RawGramMatrix | None,
    quadratic: Sequence[ExactScalar] | None,
    level: int,
) -> DiscriminantForm:
    """Entry into DiscriminantForms; axioms assigned from the data (T3 model)."""
    assert False, "typed declaration only; the runtime entry is the discriminant_forms constructions (realized at T3)"


def U(n: int = 1) -> HyperbolicLattice:
    """The hyperbolic plane U(n): Gram [[0, n], [n, 0]]."""
    assert False, "typed declaration only; the runtime entry is Lattices(R).from_gram_matrix / constructors.py (realized at T1)"


def RootLattice(type_: Literal["A", "D", "E"], n: int, negative: bool = False) -> RootGeneratedLattice:
    """ADE root lattice with construction-provenance RootGenerated axiom;
    ``negative=True`` is the K3-convention twist by -1."""
    assert False, "typed declaration only; the runtime entry is Lattices(R).from_gram_matrix / constructors.py (realized at T1)"


# ---------------------------------------------------------------------------
# Narrowing: the ONLY sanctioned static downcasts, each assertion-shaped.
# Runtime truth is category membership; these lift it to the type level.
# ---------------------------------------------------------------------------


def in_nondegenerate(lattice: Lattice) -> NondegenerateLattice:
    assert lattice.is_nondegenerate(), f"nondegenerate lattice required; gram={lattice.gram_matrix()!r}; pass through radical_quotient() or fix the construction site"
    return cast(NondegenerateLattice, lattice)


def in_integral_nondegenerate(lattice: Lattice) -> IntegralNondegenerateLattice:
    assert lattice.is_integral() and lattice.is_nondegenerate(), (
        f"integral nondegenerate lattice required; gram={lattice.gram_matrix()!r}; "
        f"integral={lattice.is_integral()}, nondegenerate={lattice.is_nondegenerate()}; "
        "fix the construction site"
    )
    return cast(IntegralNondegenerateLattice, lattice)


def in_definite(lattice: Lattice) -> DefiniteLattice:
    assert lattice.is_definite(), f"definite lattice required; signature_pair={lattice.signature_pair()}; an indefinite lattice has no finite enumeration vocabulary"
    return cast(DefiniteLattice, lattice)


def in_positive_definite(lattice: Lattice) -> PositiveDefiniteLattice:
    assert lattice.is_positive_definite(), f"positive-definite lattice required; signature_pair={lattice.signature_pair()}"
    return cast(PositiveDefiniteLattice, lattice)


def in_indefinite(lattice: Lattice) -> IndefiniteLattice:
    assert lattice.is_indefinite(), f"indefinite lattice required; signature_pair={lattice.signature_pair()}"
    return cast(IndefiniteLattice, lattice)


def in_hyperbolic(lattice: Lattice) -> HyperbolicLattice:
    assert lattice.is_hyperbolic(), f"hyperbolic lattice (signature (1, n-1)) required; signature_pair={lattice.signature_pair()}"
    return cast(HyperbolicLattice, lattice)
