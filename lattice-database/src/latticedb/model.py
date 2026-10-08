"""The schema of the record of one lattice.

A lattice here is a free module of finite rank over the integers with a
symmetric bilinear form `b` that takes rational values. The Gram tensor of
the lattice is `b`, a symmetric (0,2)-tensor; a record gives its components
`b(e_i, e_j)` in a basis. The form is not assumed positive definite,
integral, or nondegenerate.

A record is static. Enrichment may ask the research preamble for additional
mathematical values and serialize the returned results; reading a record checks
only schema shape and stored-field coherence. It does not infer whether a
mathematical hypothesis holds from other stored invariants.

Invariants that exist only under a hypothesis live in a block named for the
hypothesis (`integral`, `definite`, `indefinite`, `hyperbolic`).
"""

import re
from collections.abc import Iterator
from datetime import date
from fractions import Fraction
from typing import Annotated, Literal, Self

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    ValidationError,
    model_validator,
)
from pydantic_core import InitErrorDetails, PydanticCustomError

type Yaml = None | bool | int | float | str | date | list[Yaml] | dict[str, Yaml]
"""A value that a YAML document can hold."""

type Vector = tuple[int, ...]
"""Coordinates of a lattice element in the chosen basis."""

type GramTensor = tuple[tuple[Fraction, ...], ...]
"""Components ``b(e_i,e_j)`` of the selected rational-valued bilinear form."""

_RATIONAL = re.compile(r"-?\d+(/[1-9]\d*)?")


def rational(value: Yaml | Fraction) -> Fraction:
    """Read an integer, or a string `p/q`, as an exact rational. Floats are refused."""
    match value:
        case Fraction():
            return value
        case bool():
            raise PydanticCustomError(
                "rational_type",
                "a rational is an integer or a string 'p/q', not a boolean",
            )
        case int():
            return Fraction(value)
        case str() if _RATIONAL.fullmatch(value):
            return Fraction(value)
        case str():
            raise PydanticCustomError(
                "rational_parsing",
                "'{value}' is not of the form 'p/q'",
                {"value": value},
            )
        case _:
            raise PydanticCustomError("rational_type", "a rational is an integer or a string 'p/q'")


Rational = Annotated[Fraction, BeforeValidator(rational)]
Tag = Annotated[str, Field(pattern=r"^[0-9A-Z]{4}$")]
Slug = Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
Family = Annotated[str, Field(pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$")]
AdeType = Annotated[str, Field(pattern=r"^(A[1-9]\d*|D[4-9]|D[1-9]\d+|E[678])$")]
RootType = Annotated[str, Field(pattern=r"^(A[1-9]\d*|B[2-9]|B[1-9]\d+|C[3-9]|C[1-9]\d+|D[4-9]|D[1-9]\d+|E[678]|F4|G2)$")]
IntegerVector = Annotated[tuple[int, ...], Field(strict=False)]
VectorList = Annotated[tuple[IntegerVector, ...], Field(strict=False)]
Cardinality = Annotated[int, Field(gt=0)] | Literal["aleph0"] | None
Definiteness = Literal[
    "positive_definite",
    "negative_definite",
    "indefinite",
    "positive_semidefinite",
    "negative_semidefinite",
    "zero",
]


def _problem(
    kind: str,
    message: str,
    location: tuple[str, ...],
    context: dict[str, str | int] | None = None,
) -> InitErrorDetails:
    return InitErrorDetails(type=PydanticCustomError(kind, message, context), loc=location, input=None)


class Record(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        frozen=True,
        arbitrary_types_allowed=True,
    )


class Related(Record):
    tag: Tag = Field(description="Tag of another lattice in the catalogue.")
    relation: str = Field(description="One sentence that states how that lattice is related to this one.")


class Summand(Record):
    """A lattice $M(k)$: a record $M$ of the catalogue with its form scaled by a nonzero integer $k$.

    The summand names a lattice card and an additional scale used by this construction.
    The catalogue does not identify a lattice with its twists globally: $M$ and $M(k)$
    may both have cards.
    """

    tag: Tag = Field(description="Tag of the lattice $M$ in the catalogue.")
    scale: int = Field(description="The nonzero integer $k$: the summand is $M$ with the form $k b_M$.")

    @model_validator(mode="after")
    def _nonzero_scale(self) -> Self:
        if self.scale == 0:
            problem = _problem(
                "summand_scale_zero",
                "M(0) has the zero form and is not a summand of a root sublattice",
                ("scale",),
            )
            raise ValidationError.from_exception_data(type(self).__name__, [problem])
        return self


class Reference(Record):
    citation: str = Field(description="Bibliographic citation as plain text.")
    url: str | None = Field(default=None, description="Address of the source, when it has one.")


OrbitGroup = Literal["O", "O+", "SO", "SO+", "Otilde", "Otilde+", "SOtilde", "SOtilde+"]
"""A subgroup $\\Gamma$ of $O(L)$: $S$ is the kernel of the determinant, `+` the kernel of the real spinor norm, and `tilde` the kernel of the action on $A_L$."""


OrbitCounts = Annotated[tuple[Annotated[int, Field(ge=0)] | None, ...], Field(strict=False)]


class PrimitiveOrbitSeries(Record):
    """The series $F_{L,\\Gamma}(z, w) = c_\\Gamma(0) + \\sum_{n \\geq 1} c_\\Gamma(n) z^n + \\sum_{n \\geq 1} c_\\Gamma(-n) w^n$ in $\\mathbb{Z}[[z, w]]$.

    $c_\\Gamma(n)$ is the number of $\\Gamma$-orbits on the primitive vectors $v$ with $b(v, v) = n$. A coefficient that is not known is null.
    """

    constant: Annotated[int, Field(ge=0)] | None = Field(
        default=None,
        description="$c_\\Gamma(0)$, the number of orbits of primitive isotropic vectors.",
    )
    z: OrbitCounts = Field(
        default=(),
        description="$c_\\Gamma(1), c_\\Gamma(2), \\dots$: the coefficients of $z, z^2, \\dots$",
    )
    w: OrbitCounts = Field(
        default=(),
        description="$c_\\Gamma(-1), c_\\Gamma(-2), \\dots$: the coefficients of $w, w^2, \\dots$",
    )
    reference: Reference | None = Field(
        default=None,
        description="The source of the coefficients; absent when `latticedb certify` computes them.",
    )

    def coefficient(self, n: int) -> int | None:
        """$c_\\Gamma(n)$, or None when it is not stated."""
        if n == 0:
            return self.constant
        counts, index = (self.z, n - 1) if n > 0 else (self.w, -n - 1)
        return counts[index] if index < len(counts) else None

    @property
    def degrees(self) -> range:
        """The $n$ for which the series can state $c_\\Gamma(n)$."""
        return range(-len(self.w), len(self.z) + 1)


class StabilizedObject(Record):
    """The object a subgroup of $O(L)$ fixes, named by a card's slug."""

    kind: Literal["vector_orbit", "chamber", "geometric_object", "geometric_family", "embedding"]
    identifier: str = Field(min_length=1)


class ChamberData(Record):
    """A chamber in the real hyperbolic lattice: a fundamental domain of a reflection subgroup."""

    interior_vector: IntegerVector = Field(description="An interior point of the chamber, in the record basis.")
    wall_normals: tuple[IntegerVector, ...] = Field(
        strict=False,
        description="One inward normal for each wall of the chamber, in the record basis.",
    )


class OrbitRepresentatives(Record):
    """Orbit representatives of the primitive vectors of one norm: one vector per $\\Gamma$-orbit, in the record basis."""

    square: int = Field(description="The norm $n = b(v, v)$ of each representative in this group.")
    representatives: VectorList = Field(
        strict=False,
        description="One primitive vector of norm $n$ for each $\\Gamma$-orbit, in the record basis.",
    )


class GroupData(Record):
    """A subgroup $\\Gamma \\leq O(L)$: its structure, its relation to $O(L)$, and the primitive-vector orbits it defines. $O$, $SO$, $O^+$, $SO^+$, $\\widetilde{O}$, $\\widetilde{SO}$, $\\widetilde{O}^+$ and $\\widetilde{SO}^+$ carry their series
    in `integral.primitive_orbits`; a key here names either one of those, extending it with generators, relators or representatives, or a further
    named subgroup such as $\\Gamma_{\\mathrm{En},2}$.
    """

    cardinality: Cardinality = Field(
        default=None,
        description=(
            "The cardinality $|\\Gamma|$ of $\\Gamma$: a positive integer $n$ when $\\Gamma$ is finite, or `aleph0` when it is "
            "countably infinite. A subgroup of $\\mathrm{GL}_n(\\mathbb{Z})$ is countable, so its cardinality is $n$ or $\\aleph_0$. "
            "A lattice of signature $(2, n)$ has a countably infinite $O(L)$, by the Eichler transvections "
            "$t(c, a) = v \\mapsto v - (a, v) c$ for a primitive isotropic $c$; its subgroups of finite index are infinite too."
        ),
    )

    index_in_orthogonal_group: Annotated[int, Field(gt=0)] | None = Field(default=None, description="The index $[O(L) : \\Gamma]$.")
    parent: str | None = Field(
        default=None,
        description="The key of a containing subgroup of the same lattice.",
    )
    generator_morphisms: Annotated[tuple[str, ...], Field(strict=False)] | None = Field(
        default=None,
        description="Names of self-isometries in this lattice card's `morphisms` field that generate $\\Gamma$.",
    )
    defining_relators: tuple[Annotated[tuple[int, ...], Field(strict=False)], ...] | None = Field(
        default=None,
        strict=False,
        description="Words in the signed generators above, one generator index per entry, that present $\\Gamma$.",
    )
    abstract_structure: str | None = Field(default=None, description="The abstract group $\\Gamma$, as plain text.")
    stabilized: StabilizedObject | None = Field(
        default=None,
        description="A vector orbit, chamber, geometric object, family or embedding that $\\Gamma$ fixes.",
    )
    chamber: ChamberData | None = Field(
        default=None,
        description="A chamber of the real hyperbolic lattice that $\\Gamma$ reflects in, when $\\Gamma$ is a reflection subgroup.",
    )
    orbits: tuple[OrbitRepresentatives, ...] | None = Field(
        default=None,
        strict=False,
        description=(
            "Orbit representatives of the primitive vectors, grouped by the norm $n$: one vector for each $\\Gamma$-orbit, "
            "in the record basis. A group states a set of representatives, not necessarily all of them."
        ),
    )
    reference: Reference | None = Field(default=None, description="The source of the structure and the representatives.")


class DiscriminantSequenceData(Record):
    """A finite discriminant action, its kernel order, and its pointed coset quotient."""

    discriminant_factors: list[int]
    discriminant_basis_lifts: list[list[str]]
    discriminant_quadratic_gram: list[list[str]]
    discriminant_group_order: int = Field(gt=0)
    discriminant_generators: list[list[list[int]]]
    image_generators: list[list[list[int]]]
    image_order: int = Field(gt=0)
    kernel_order: Annotated[int, Field(gt=0)] | None = None
    coset_representatives: list[list[list[int]]]
    mm_trivial: bool
    image_normal: bool
    quotient_generator_cosets: list[int] | None = None
    quotient_multiplication: list[list[int]] | None = None
    quotient_invariant_factors: list[Annotated[int, Field(gt=1)]] | None = None
    mm_f2_dimension: Annotated[int, Field(ge=0)] | None = None

    @model_validator(mode="after")
    def _sequence(self) -> Self:
        size = len(self.discriminant_factors)
        matrices = [
            *self.discriminant_generators,
            *self.image_generators,
            *self.coset_representatives,
        ]
        if any(len(rows) != size or any(len(row) != size for row in rows) for rows in matrices):
            raise ValueError("discriminant isometry matrices must be square in the stated basis")
        if len(self.discriminant_basis_lifts) != size or len(self.discriminant_quadratic_gram) != size:
            raise ValueError("the discriminant basis and quadratic Gram matrix must match the invariant factors")
        if self.image_normal != (self.quotient_multiplication is not None and self.quotient_generator_cosets is not None):
            raise ValueError("quotient group data are present exactly when the image is normal")
        if self.quotient_multiplication is not None:
            count = len(self.coset_representatives)
            if len(self.quotient_multiplication) != count or any(len(row) != count for row in self.quotient_multiplication):
                raise ValueError("the quotient multiplication table must index the cosets")
            if any(value < 0 or value >= count for row in self.quotient_multiplication for value in row):
                raise ValueError("quotient products must index the stated cosets")
        if self.quotient_invariant_factors is not None and self.quotient_multiplication is None:
            raise ValueError("quotient invariant factors require stored quotient-group data")
        if self.mm_f2_dimension is not None and self.quotient_multiplication is None:
            raise ValueError("the F2 dimension requires stored quotient-group data")
        return self


class IntegralData(Record):
    """Stored invariants of an integer-valued lattice, when available."""

    parity: Literal["even", "odd"] = Field(description="`even` when $b(x, x)$ is even for every $x$, `odd` otherwise.")
    level: Annotated[int, Field(gt=0)] | None = Field(
        default=None,
        description="Least positive $k$ for which $k b(x,x)$ is even for every $x$ in the dual lattice. Requires nonzero determinant.",
    )
    modular_scale: Literal[False] | Annotated[int, Field(gt=0)] | None = Field(
        default=None,
        description="The $k > 0$ with $L\\cong L^*(k)$, or `false` when there is no such $k$; an explicit chosen isometry, when stored, belongs to this card's morphisms rather than a separate object.",
    )
    discriminant_group: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Invariant factors $d_1 \\mid d_2 \\mid \\dots$, each greater than 1, of the cokernel of the correlation $L \\to \\operatorname{Hom}(L, \\mathbb{Z})$. "
            "The empty list is the trivial group."
        ),
    )
    discriminant_sequence: DiscriminantSequenceData | None = Field(
        default=None,
        description=(
            "For a nondegenerate even lattice, generators of $O(A_L,q_L)$, the image of the discriminant action in the stated basis, "
            "and representatives of the pointed coset set; full generators of $O(L)$ are named self-isometry morphisms when available. "
            "$MM(L)=O(A_L,q_L)/\\operatorname{im}\\rho_L$. A multiplication table and generator cosets are present when the image is normal."
        ),
    )
    overlattice_count: int | None = Field(
        default=None,
        description=(
            "The number of integral lattices $M$ with $L \\subseteq M \\subseteq L^*$, with $M = L$ counted: the number of subgroups $H$ of the discriminant group "
            "$A_L = L^*/L$ with $b_{A_L}(H, H) = 0$, for the form $b_{A_L}(x + L, y + L) = b(x, y) + \\mathbb{Z}$ with values in $\\mathbb{Q}/\\mathbb{Z}$. "
            "Subgroups are counted, not their orbits under the isometries of $L$. An even $L$ can have odd lattices among the $M$. "
            "When certified, this exact invariant was computed by the certification phase."
        ),
    )
    delta: Literal[0, 1] | None = Field(
        default=None,
        description=(
            "Nikulin's invariant $\\delta$ of an even lattice with $2 A_L = 0$: "
            "0 when $b(x, x)$ is an integer for every $x$ in the dual lattice $L^*$, and 1 otherwise. "
            "With the rank $r$ and $A_L \\cong (\\mathbb{Z}/2)^a$ it gives $(r, a, \\delta)$. "
            "This field is meaningful for an even nondegenerate 2-elementary lattice."
        ),
    )
    bad_reduction_primes: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The primes that divide $2 \\det L$, in increasing order: the primes $p$ at which $Q(x) = b(x, x)$ is degenerate modulo $p$. "
            "Outside them and the primes that divide $n$, the scheme $Q(x) = n$ over $\\mathbb{Z}$ has good reduction."
        ),
    )
    quadratic_character: int | None = Field(
        default=None,
        description=(
            "For rank $2m$: the discriminant $d$ of the field $\\mathbb{Q}(\\sqrt{D})$ with $D = (-1)^m \\det L$, and 1 when $D$ is a square. "
            "For $p \\nmid 2 \\det L$ the Kronecker symbol $\\chi_D(p) = (d / p)$ is 1 exactly when $Q$ modulo $p$ is a sum of $m$ hyperbolic planes, "
            "and it determines the number of points of $Q(x) = n$ over $\\mathbb{F}_{p^k}$. "
            "This field is meaningful for even rank and nonzero determinant."
        ),
    )
    genus_symbol: str | None = Field(
        default=None,
        description=(
            "`I` (odd) or `II` (even) with the signature, such as `II_{1,9}`. When the determinant is not 1 or -1, the local symbol at each prime "
            "that divides twice the determinant follows in parentheses, in the notation that SageMath prints. Requires a nonzero determinant."
        ),
    )
    genus_class_count: int | None = Field(
        default=None,
        gt=0,
        description=(
            "The class number of the genus of $L$: the number of isometry classes of lattices in the genus, $L$ counted. "
            "Computed by CI from the preamble operation `L.genus_class_number()`. "
            "Requires a nonzero determinant; absent when it is not computed."
        ),
    )
    spinor_genus_count: int | None = Field(
        default=None,
        gt=0,
        description=(
            "The number of spinor genera in the genus of $L$, a power of 2 (Conway and Sloane, SPLAG, Chapter 15, Section 9.1): "
            "the order of the quotient of the spinor operators by the spinor kernel of Theorems 16 and 17 there, enlarged by the spinor operator of one improper "
            "isometry, so that a spinor genus is a union of isometry classes. "
            "Computed by CI from the preamble operation `L.spinor_genus_count()`. Requires a nonzero determinant and rank at least 3."
        ),
    )
    spinor_genera: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The number of isometry classes in each spinor genus of the genus of $L$: first in the spinor genus of $L$, then in the others in decreasing order. "
            "The first entry is the class number of the spinor genus of $L$, and the sum is the class number of the genus. "
            "Computed by CI from the preamble operation `L.spinor_genus_class_numbers()`. Requires a nonzero determinant and rank at least 3."
        ),
    )
    hyperbolic_index: int | None = Field(
        default=None,
        ge=0,
        description=(
            "The largest $n$ with $L \\cong U^n \\oplus L'$ for a lattice $L'$, where $U$ is the hyperbolic plane. "
            "For an integral $L$ this is the largest $n$ with an embedding $U^n \\hookrightarrow L$, because a unimodular sublattice $M$ of $L$ "
            "satisfies $L = M \\oplus M^{\\perp}$. "
            "Computed by `latticedb certify`: $L \\cong U^n \\oplus L'$ holds exactly when the genus of $L$ is the sum of the genus of $U^n$ and a genus of "
            "signature $(n_+ - n, n_- - n)$, since a lattice $U \\oplus L'$ of rank at least 3 is alone in its genus "
            "(Nikulin 1980, Theorem 1.13.1*). Requires a nonzero determinant; absent when it is not computed."
        ),
    )
    primitive_orbits: dict[OrbitGroup, PrimitiveOrbitSeries] | None = Field(
        default=None,
        description=(
            "For a group $\\Gamma \\subseteq O(L)$, the series $F_{L,\\Gamma}(z, w)$ whose coefficient $c_\\Gamma(n)$ is the number of $\\Gamma$-orbits of primitive "
            "vectors $v$ with $b(v, v) = n$. The keys are `O`, `SO`, `O+`, `SO+`, `Otilde`, `SOtilde`, `Otilde+` and `SOtilde+`: $S$ is the kernel of the determinant, "
            "$+$ the kernel of the real spinor norm, and $\\widetilde{O}(L)$ the kernel of $O(L) \\to O(A_L)$. "
            "Computed by `latticedb certify` through $z^4$ and $w^4$ for a definite lattice; stated with a reference otherwise. Requires a nonzero determinant."
        ),
    )
    discriminant_orbits: dict[OrbitGroup, PrimitiveOrbitSeries] | None = Field(
        default=None,
        description=(
            "For a group $\\Gamma \\subseteq O(L)$, the series whose coefficient $c_\\Gamma(n)$ is the number of $\\Gamma$-orbits on the elements $\\alpha \\in A_L$ with "
            "$q_L(\\alpha) = n / \\operatorname{ord}(\\alpha)^2$, keyed by the same eight groups. This is a function of the discriminant form $(A_L, q_L)$, not of $L$: it is "
            "computed by `latticedb certify` from $(A_L, q_L)$ for an even lattice of hyperbolic index at least 2. It equals $F_{L,\\Gamma}$ for an even "
            "$L$ containing two orthogonal hyperbolic planes (Eichler; theory/orbits.md), and it is defined for every nondegenerate $L$."
        ),
    )


class RootSystemComponent(Record):
    """An irreducible component of the root system $\\Phi(L)$ of a definite lattice, with a base."""

    type: RootType = Field(
        description=(
            "Type of the component: `A1`, `B2`, `C3`, `D4`, `E6`, `E7`, `E8`, `F4`, `G2`, and the higher ranks of `A` to `D`. "
            "`B_n` has $2n$ short roots, and `C_n` has $2n$ long roots."
        )
    )
    scale: Rational = Field(
        description=(
            "The $k \\neq 0$ with $b(r, r) = 2k$ for each short root $r$ of the component. "
            "The simple roots have $b(\\alpha_i, \\alpha_j) = k\\,(\\alpha_i, \\alpha_j)$, "
            "where $(\\alpha_i, \\alpha_j)$ is the entry of the symmetrized Cartan matrix of the type, normalized so that $(r, r) = 2$ for a short root $r$. "
            "$k$ is negative on a negative definite lattice."
        )
    )
    simple_roots: Annotated[tuple[IntegerVector, ...], Field(strict=False)] = Field(
        description=(
            "Row $i$ lists the coordinates of the simple root $\\alpha_i$ in the chosen basis $e_1, \\dots, e_n$. "
            "The simple roots are numbered as SageMath's `CartanMatrix` numbers them. "
            "The rows of all components are a basis of $\\mathbb{Z}\\Phi(L)$: "
            "they are the matrix of the embedding into $L$ of the orthogonal sum of the root lattices of the components."
        )
    )

    @property
    def rank(self) -> int:
        return int(self.type[1:])


class DefiniteData(Record):
    """Invariants of a definite lattice. They are stated for a positive definite form; on a negative definite lattice they are the invariants of $-b$."""

    minimum: Rational | None = Field(
        default=None,
        description="Optional cached least value of $b(x,x)$ over nonzero $x$.",
    )
    kissing_number: int | None = Field(
        default=None,
        description="Optional cached number of vectors attaining the minimum.",
    )
    automorphism_group_order: int | None = Field(
        default=None,
        description="Order of $O(L)$, computed by CI from the preamble operation `L.orthogonal_group()`.",
    )
    automorphism_group_generator_morphisms: Annotated[tuple[str, ...], Field(strict=False)] | None = Field(
        default=None,
        description="Names of self-isometries in this card's `morphisms` field that generate $O(L)$, computed by CI from the preamble operation `L.orthogonal_group()`.",
    )
    minimal_vectors: list[list[int]] | None = Field(
        default=None,
        description="A complete minimal shell in the record basis; its size equals `kissing_number`.",
    )
    perfect: bool | None = Field(
        default=None,
        description="Whether the rank-one tensors $v v^T$ of minimal vectors span $\\operatorname{Sym}^2(\\mathbb Q^n)$.",
    )
    regular: bool | Literal["true under GRH"] | None = Field(
        default=None,
        description=(
            "For an integral ternary form: every positive integer represented by its genus is represented by this lattice. "
            "`true under GRH` when it is proved under the generalized Riemann hypothesis; `references` names the proof."
        ),
    )
    spinor_regular: bool | Literal["true under GRH"] | None = Field(
        default=None,
        description=(
            "For an integral ternary form: every positive integer represented by its spinor genus is represented by this lattice. "
            "`true under GRH` when it is proved under the generalized Riemann hypothesis; `references` names the proof."
        ),
    )
    theta_series: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Entry $k$ is the number of $x$ with $b(x, x) = k$, for $k = 0, 1, 2, \\dots$. "
            "The entries run through $k = \\max(\\mu, N)$ at least, "
            "where $\\mu$ is the minimum and $N$ is 12, 8, 6 or 4 for rank at most 4, at most 8, at most 12, or greater."
        ),
    )
    root_system: Annotated[tuple[AdeType, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "ADE type of $\\Phi_{\\{2\\}}(L) = \\{r \\in L : b(r, r) = 2\\}$, as irreducible components in any order: `[E8]`, `[A1, A1]`, or `[]` "
            "when it is empty. "
            "By Witt's theorem (Conway and Sloane, *Sphere Packings, Lattices and Groups*, 3rd edition, Chapter 4, §3), "
            "$\\mathbb{Z}\\Phi_{\\{2\\}}(L)$ is the orthogonal sum of the root lattices of the components. "
            "Optional cached root-system data; when present it is a preamble-computed or source-stated value."
        ),
    )
    roots: Annotated[tuple[RootSystemComponent, ...], Field(strict=False)] | None = Field(
        default=None,
        description="Optional cached root system $\\Phi(L)$ as irreducible components, each with a base; `[]` when it is known to have no roots.",
    )


class IndefiniteData(Record):
    """Invariants of a lattice on which $b(x, x)$ takes both signs."""

    isotropic: bool = Field(description="Whether $b(x, x) = 0$ for some nonzero $x$.")


class HyperbolicData(Record):
    """Invariants of a nondegenerate lattice of rank at least 2 whose signature is $(1, n)$ or $(n, 1)$."""

    reflective: bool = Field(description="Whether the subgroup generated by reflections has finite index in the isometry group.")


class RootSpan(Record):
    """$\\mathbb{Z}\\Phi(L)$ for a lattice that is not definite. Present only when $b$ is not definite."""

    roots: Annotated[tuple[IntegerVector, ...], Field(strict=False)] = Field(
        description=(
            "Roots of $L$ that generate $\\mathbb{Z}\\Phi(L)$: each row lists the coordinates of one root in the chosen basis $e_1, \\dots, e_n$. "
            "`[]` when $L$ has no roots. "
            "When the rows generate $L$, that proves $L = \\mathbb{Z}\\Phi(L)$. "
            "When they do not, the notes of the record prove that each root of $L$ is in the sublattice that the rows generate."
        )
    )
    norms: Annotated[tuple[Rational, ...], Field(strict=False)] = Field(description="Entry $i$ is $b(r_i, r_i)$ for the root $r_i$ in row $i$ of `roots`.")
    summands: Annotated[tuple[Summand, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Lattices $M_1(k_1), M_2(k_2), \\dots$, each a record with a scale, "
            "with $\\mathbb{Z}\\Phi(L) \\cong M_1(k_1) \\oplus M_2(k_2) \\oplus \\cdots$, an orthogonal sum. "
            "Present exactly when `embedding` is present. Absent when $L = \\mathbb{Z}\\Phi(L)$."
        ),
    )
    embedding: Annotated[tuple[IntegerVector, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Matrix of an isometric embedding $M_1 \\oplus M_2 \\oplus \\cdots \\to L$ with image $\\mathbb{Z}\\Phi(L)$: "
            "the rows list the coordinates of the images of the chosen basis vectors of $M_1$, then of $M_2$, and so on."
        ),
    )


class RootSublattice(Record):
    """The root sublattice $R(L) = \\mathbb{Z}\\Phi(L)$ as a sublattice of $L$. Present when $L$ is definite or has a `root_span` block."""

    invariant_factors: Annotated[tuple[int, ...], Field(strict=False)] = Field(
        description=(
            "The invariant factors $d_1 \\mid d_2 \\mid \\dots$ of $R(L)$ in $L$. Their number is the rank of $R(L)$. "
            "With $M'$ the primitive sublattice $L \\cap (R(L) \\otimes \\mathbb{Q})$, "
            "$M' / R(L) \\cong \\mathbb{Z}/d_1 \\oplus \\mathbb{Z}/d_2 \\oplus \\cdots$."
        )
    )
    norms: Annotated[tuple[Rational, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "For a root lattice, a set $S$ with $L = \\mathbb{Z}\\Phi_S(L)$: among the sets of values $b(r, r)$ of generating roots, "
            "one with the fewest elements, and then the least absolute values. Present exactly when $L = R(L)$."
        ),
    )


class Morphism(Record):
    """A stored morphism whose domain is the lattice card that contains it."""

    target: Tag = Field(description="Tag of the codomain lattice $T$.")
    name: str = Field(description="Name as plain text; TeX between `$` signs is rendered.")
    description: str | None = Field(
        default=None,
        description="One or two sentences on the morphism, as plain text with TeX between `$` signs.",
    )
    matrix: Annotated[tuple[IntegerVector, ...], Field(strict=False, min_length=1)] = Field(
        description=(
            "Matrix with $\\operatorname{rank} T$ rows and $\\operatorname{rank} S$ columns: column $j$ lists the coordinates of $\\varphi(e_j)$ in the chosen basis of $T$."
        )
    )
    scale: int = Field(
        default=1,
        description="The nonzero integer $c$ with $b_T(\\varphi x, \\varphi y) = c b_S(x, y)$.",
    )
    row_subdivisions: IntegerVector = Field(default=())
    column_subdivisions: IntegerVector = Field(default=())

    @model_validator(mode="after")
    def _well_defined(self) -> Self:
        columns = len(self.matrix[0])
        problems: list[InitErrorDetails] = []
        if columns == 0 or any(len(row) != columns for row in self.matrix):
            problems.append(
                _problem(
                    "matrix_shape",
                    "the rows of the matrix are nonempty and have one length",
                    ("matrix",),
                )
            )
        if self.scale == 0:
            problems.append(
                _problem(
                    "scale_nonzero",
                    "the scale c of a morphism S(c) -> T is not zero",
                    ("scale",),
                )
            )
        problems.extend(_subdivision_problems(self.row_subdivisions, len(self.matrix), ("row_subdivisions",)))
        problems.extend(_subdivision_problems(self.column_subdivisions, columns, ("column_subdivisions",)))
        if problems:
            raise ValidationError.from_exception_data(type(self).__name__, problems)
        return self

    @property
    def images(self) -> tuple[Vector, ...]:
        """The columns of the matrix: the coordinates of the images of the source basis."""
        return tuple(zip(*self.matrix, strict=True))


class Lattice(Record):
    tag: Tag = Field(description="Permanent identifier: four characters from 0-9 and A-Z. The file name is the tag.")
    name: str = Field(description="Name as plain text, for search.")
    latex: str = Field(description="Name as TeX, without math delimiters.")
    aliases: Annotated[tuple[str, ...], Field(strict=False)] = Field(default=(), description="Other names, as plain text.")
    certifications: dict[str, str] = Field(
        default_factory=dict,
        description=(
            "Completed computations cited by computation name. Each value is the SHA-256 certificate hash of that computation on this card's Gram tensor and stored result."
        ),
    )
    rank: int | None = Field(
        default=None,
        ge=1,
        description="Rank of the underlying free module, when the source states it.",
    )
    gram_tensor: (
        Annotated[
            tuple[Annotated[tuple[Rational, ...], Field(strict=False)], ...],
            Field(strict=False),
        ]
        | None
    ) = Field(
        default=None,
        description=(
            "Components of the Gram tensor, the symmetric (0,2)-tensor $b$, in a basis $e_1, \\dots, e_n$: "
            "row $i$ lists $b(e_i, e_1), \\dots, b(e_i, e_n)$. Values are integers or strings `p/q`."
        ),
    )
    signature: Annotated[tuple[int, int], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "`[n_plus, n_minus]`: the numbers of $v$ with $b(v, v) > 0$ and with $b(v, v) < 0$ in a $b$-orthogonal basis of $L \\otimes \\mathbb{Q}$. "
            "They do not depend on the basis (Sylvester's law of inertia)."
        ),
    )
    determinant: Rational | None = Field(
        default=None,
        description="$\\det(b(e_i, e_j))$. It is the same for every basis of $L$.",
    )
    definiteness: Definiteness | None = Field(
        default=None,
        description=(
            "`positive_definite` or `negative_definite` when $b(x, x)$ has one sign on nonzero $x$; `indefinite` when it takes both signs; "
            "`positive_semidefinite` when $b(x, x) \\geq 0$ for all $x$, $b \\neq 0$ and the determinant is zero, "
            "and `negative_semidefinite` with $\\leq$; `zero` when $b = 0$."
        ),
    )
    dual_gram_tensor: (
        Annotated[
            tuple[Annotated[tuple[Rational, ...], Field(strict=False)], ...],
            Field(strict=False),
        ]
        | None
    ) = Field(
        default=None,
        description=(
            "Components of the inverse Gram tensor, the Gram tensor $b^*$ of the dual lattice $L^*$ in the basis dual to $e_1, \\dots, e_n$: "
            "row $i$ lists $b^*(e^i, e^1), \\dots, b^*(e^i, e^n)$. Values are integers or strings `p/q`. "
            "Computed by `latticedb enrich` from the Gram tensor; it requires a nonzero determinant."
        ),
    )
    families: Annotated[tuple[Family, ...], Field(strict=False)] = Field(default=(), description="Named families that contain the lattice.")
    related: Annotated[tuple[Related, ...], Field(strict=False)] = Field(default=(), description="Related lattices in the catalogue.")
    references: Annotated[tuple[Reference, ...], Field(strict=False)] = Field(default=(), description="Literature for the lattice.")
    integral: IntegralData | None = Field(default=None, description=IntegralData.__doc__)
    definite: DefiniteData | None = Field(default=None, description=DefiniteData.__doc__)
    indefinite: IndefiniteData | None = Field(default=None, description=IndefiniteData.__doc__)
    hyperbolic: HyperbolicData | None = Field(default=None, description=HyperbolicData.__doc__)
    root_span: RootSpan | None = Field(default=None, description=RootSpan.__doc__)
    root_sublattice: RootSublattice | None = Field(default=None, description=RootSublattice.__doc__)
    morphisms: Annotated[tuple[Morphism, ...], Field(strict=False)] = Field(
        default=(),
        description="Stored morphisms whose domain is this lattice card; each morphism names its codomain lattice by tag.",
    )
    orthogonal_group: Slug | None = Field(
        default=None,
        description="Arithmetic-group card for the canonical integral orthogonal group O(L), when that group has a stored card.",
    )
    arithmetic_groups: Annotated[tuple[Slug, ...], Field(strict=False)] = Field(
        default=(),
        description="Arithmetic-group cards attached to this lattice, including `orthogonal_group` when it is stored.",
    )

    @property
    def nullity(self) -> int | None:
        return None if self.rank is None or self.signature is None else self.rank - self.signature[0] - self.signature[1]

    @property
    def is_definite(self) -> bool:
        """Whether $b(x, x)$ has one sign on the nonzero vectors of $L$."""
        return self.definiteness in ("positive_definite", "negative_definite")

    @property
    def root_span_factors(self) -> tuple[int, ...] | None:
        """The invariant factors of $R(L)$ in $L$; `None` when $R(L)$ is not decided."""
        return None if self.root_sublattice is None else self.root_sublattice.invariant_factors

    @model_validator(mode="after")
    def _well_defined(self) -> Self:
        """Verify only structural and cross-field coherence of a parsed card."""
        problems = list(self._shape_problems())
        if not problems:
            problems = [
                *self._integral_problems(),
                *self._definite_problems(),
                *self._root_problems(),
                *self._dual_problems(),
            ]
        if problems:
            raise ValidationError.from_exception_data(type(self).__name__, problems)
        return self

    def _shape_problems(self) -> Iterator[InitErrorDetails]:
        if self.rank is None or self.gram_tensor is None or self.signature is None or self.determinant is None or self.definiteness is None:
            return
        if len(self.gram_tensor) != self.rank or any(len(row) != self.rank for row in self.gram_tensor):
            yield _problem(
                "gram_tensor_shape",
                "a (0,2)-tensor on a module of rank {rank} has {rank} rows of {rank} components",
                ("gram_tensor",),
                {"rank": self.rank},
            )
        if min(self.signature) < 0 or self.nullity < 0:
            yield _problem(
                "signature_shape",
                "n_plus and n_minus are nonnegative with n_plus + n_minus <= {rank}",
                ("signature",),
                {"rank": self.rank},
            )

    def _integral_problems(self) -> Iterator[InitErrorDetails]:
        if self.integral is None:
            return
        if self.integral.discriminant_sequence is not None:
            if tuple(self.integral.discriminant_sequence.discriminant_factors) != self.integral.discriminant_group:
                yield _problem(
                    "discriminant_sequence_factors",
                    "the discriminant sequence must use the stated invariant factors",
                    ("integral", "discriminant_sequence", "discriminant_factors"),
                )
        yield from self._spinor_problems()

    def _dual_problems(self) -> Iterator[InitErrorDetails]:
        """Structural conditions on a stored dual Gram tensor."""
        if self.dual_gram_tensor is None:
            return
        if self.gram_tensor is None or self.rank is None:
            yield _problem(
                "dual_gram_requires_gram",
                "the dual Gram tensor requires the Gram tensor",
                ("dual_gram_tensor",),
            )
            return
        dual = self.dual_gram_tensor
        if len(dual) != self.rank or any(len(row) != self.rank for row in dual):
            yield _problem(
                "dual_gram_shape",
                "a (0,2)-tensor on a module of rank {rank} has {rank} rows of {rank} components",
                ("dual_gram_tensor",),
                {"rank": self.rank},
            )
            return

    def _spinor_problems(self) -> Iterator[InitErrorDetails]:
        """Structural conditions on stored spinor-genus data."""
        assert self.integral is not None
        count, genera = self.integral.spinor_genus_count, self.integral.spinor_genera
        if count is None and genera is None:
            return
        if genera is None:
            return
        location = ("integral", "spinor_genera")
        if count is not None and len(genera) != count:
            yield _problem(
                "spinor_genera_count",
                "{listed} spinor genera are listed, and there are {count}",
                location,
                {"listed": len(genera), "count": count},
            )

    def _definite_problems(self) -> Iterator[InitErrorDetails]:
        if self.definite is None:
            return
        data = self.definite
        generator_names = data.automorphism_group_generator_morphisms
        if generator_names is not None:
            self_isometry_names = [morphism.name for morphism in self.morphisms if morphism.target == self.tag and morphism.scale == 1]
            if len(set(generator_names)) != len(generator_names) or any(self_isometry_names.count(name) != 1 for name in generator_names):
                yield _problem(
                    "automorphism_group_generators",
                    "each generator name occurs once in the generator list and names exactly one isometry L -> L (a morphism entry with scale 1) on this lattice card",
                    ("definite", "automorphism_group_generator_morphisms"),
                )
        if data.roots is not None and any(
            len(component.simple_roots) != component.rank or any(len(row) != self.rank for row in component.simple_roots) for component in data.roots
        ):
            yield _problem(
                "roots_shape",
                "a component of rank m has m simple roots, each with {rank} coordinates",
                ("definite", "roots"),
                {"rank": self.rank},
            )
        if data.minimal_vectors is not None:
            vectors = data.minimal_vectors
            if (
                data.kissing_number is None
                or data.minimum is None
                or len(vectors) != data.kissing_number
                or len({tuple(v) for v in vectors}) != len(vectors)
                or any(len(v) != self.rank for v in vectors)
            ):
                yield _problem(
                    "minimal_shell_shape",
                    "the complete minimal shell has distinct vectors of the lattice rank and the kissing number",
                    ("definite", "minimal_vectors"),
                )

    def _root_problems(self) -> Iterator[InitErrorDetails]:
        span = self.root_span
        if span is not None:
            if self.definite is not None:
                yield _problem(
                    "root_span_on_definite",
                    "`definite.roots` states the roots of a definite lattice, so the `root_span` block is an error there",
                    ("root_span",),
                )
            if any(len(row) != self.rank for row in (*span.roots, *(span.embedding or ()))):
                yield _problem(
                    "root_span_shape",
                    "each row lists {rank} coordinates",
                    ("root_span",),
                    {"rank": self.rank},
                )
            if len(span.norms) != len(span.roots):
                yield _problem(
                    "root_span_norms_shape",
                    "`norms` has one entry for each row of `roots`",
                    ("root_span", "norms"),
                )
            if (span.summands is None) != (span.embedding is None):
                yield _problem(
                    "root_span_representative_incomplete",
                    "`summands` and `embedding` are stated together",
                    ("root_span",),
                )
        sublattice = self.root_sublattice
        decided = (self.definite is not None and self.definite.roots is not None) or span is not None
        if sublattice is None:
            return
        if not decided:
            yield _problem(
                "root_sublattice_not_decided",
                "the `root_sublattice` block requires stored `definite.roots` or `root_span` data",
                ("root_sublattice",),
            )
            return
        factors = sublattice.invariant_factors
        if len(factors) > self.rank or any(d < 1 for d in factors) or any(second % first != 0 for first, second in zip(factors, factors[1:], strict=False)):
            message = "at most {rank} positive invariant factors, each dividing the next"
            yield _problem(
                "root_sublattice_factors_shape",
                message,
                ("root_sublattice", "invariant_factors"),
                {"rank": self.rank},
            )


def _subdivision_problems(lines: Vector, size: int, location: tuple[str, ...]) -> Iterator[InitErrorDetails]:
    if any(not 0 < line < size for line in lines) or any(first >= second for first, second in zip(lines, lines[1:], strict=False)):
        yield _problem(
            "subdivision_range",
            "the lines increase strictly and each lies strictly between 0 and {size}",
            location,
            {"size": size},
        )
