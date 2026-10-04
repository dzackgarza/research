"""The schema of the record of one lattice.

A lattice here is a free module of finite rank over the integers with a
symmetric bilinear form `b` that takes rational values. The Gram tensor of
the lattice is `b`, a symmetric (0,2)-tensor; a record gives its components
`b(e_i, e_j)` in a basis. The form is not assumed positive definite,
integral, or nondegenerate.

A record is static. `records.derive` computes its values once, when the
record is written; reading a record checks only that its fields have the
shapes of the schema and that each block is present exactly when the stored
fields state its hypothesis.

Invariants that exist only under a hypothesis live in a block named for the
hypothesis (`integral`, `definite`, `indefinite`, `hyperbolic`).
"""

import math
import re
from collections.abc import Iterator
from datetime import date
from fractions import Fraction
from typing import Annotated, Literal, Self

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, ValidationError, model_validator
from pydantic_core import InitErrorDetails, PydanticCustomError

from dzack_research.preamble.categories.sets.cardinals import Cardinal, aleph0, cardinal

from latticedb import arithmetic, root_systems
from latticedb.arithmetic import Vector

type Yaml = None | bool | int | float | str | date | list[Yaml] | dict[str, Yaml]
"""A value that a YAML document can hold."""

_RATIONAL = re.compile(r"-?\d+(/[1-9]\d*)?")


def rational(value: Yaml | Fraction) -> Fraction:
    """Read an integer, or a string `p/q`, as an exact rational. Floats are refused."""
    match value:
        case Fraction():
            return value
        case bool():
            raise PydanticCustomError("rational_type", "a rational is an integer or a string 'p/q', not a boolean")
        case int():
            return Fraction(value)
        case str() if _RATIONAL.fullmatch(value):
            return Fraction(value)
        case str():
            raise PydanticCustomError("rational_parsing", "'{value}' is not of the form 'p/q'", {"value": value})
        case _:
            raise PydanticCustomError("rational_type", "a rational is an integer or a string 'p/q'")


Rational = Annotated[Fraction, BeforeValidator(rational)]
Tag = Annotated[str, Field(pattern=r"^[0-9A-Z]{4}$")]
Slug = Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
Family = Annotated[str, Field(pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$")]
AdeType = Annotated[str, Field(pattern=r"^(A[1-9]\d*|D[4-9]|D[1-9]\d+|E[678])$")]
RootType = Annotated[str, Field(pattern=root_systems.TYPE_PATTERN)]
IntegerVector = Annotated[tuple[int, ...], Field(strict=False)]

def group_cardinality(value: object) -> Cardinal:
    """Read a card's finite or countably infinite group cardinality."""
    if isinstance(value, Cardinal):
        return value
    match value:
        case "aleph0":
            return aleph0
        case bool():
            pass
        case int() if value > 0:
            return cardinal(value)
    raise PydanticCustomError(
        "cardinality_type",
        "a group cardinality is a positive integer or 'aleph0'",
    )


Cardinality = Annotated[Cardinal, BeforeValidator(group_cardinality)] | None
Definiteness = Literal[
    "positive_definite",
    "negative_definite",
    "indefinite",
    "positive_semidefinite",
    "negative_semidefinite",
    "zero",
]


def _problem(kind: str, message: str, location: tuple[str, ...], context: dict[str, str | int] | None = None) -> InitErrorDetails:
    return InitErrorDetails(type=PydanticCustomError(kind, message, context), loc=location, input=None)


class Record(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True, arbitrary_types_allowed=True)


class Related(Record):
    tag: Tag = Field(description="Tag of another lattice in the catalogue.")
    relation: str = Field(description="One sentence that states how that lattice is related to this one.")


class Summand(Record):
    """A lattice $M(k)$: a record $M$ of the catalogue with its form scaled by a nonzero integer $k$.

    The catalogue records no twist $M(k)$ with $|k| \\geq 2$ other than the 13 rows $a = r$ of Nikulin's Table 1, and no $M(-1)$ outside its sign convention,
    so a summand of a root sublattice such as $A_1 = \\langle 1 \\rangle(2)$ names the record and the scale.
    """

    tag: Tag = Field(description="Tag of the lattice $M$ in the catalogue.")
    scale: int = Field(description="The nonzero integer $k$: the summand is $M$ with the form $k b_M$.")

    @model_validator(mode="after")
    def _nonzero_scale(self) -> Self:
        if self.scale == 0:
            problem = _problem("summand_scale_zero", "M(0) has the zero form and is not a summand of a root sublattice", ("scale",))
            raise ValidationError.from_exception_data(type(self).__name__, [problem])
        return self


class Reference(Record):
    citation: str = Field(description="Bibliographic citation as plain text.")
    url: str | None = Field(default=None, description="Address of the source, when it has one.")


OrbitGroup = Literal["O", "O+", "SO", "SO+", "Otilde", "Otilde+", "SOtilde", "SOtilde+"]
"""A subgroup $\\Gamma$ of $O(L)$: $S$ is the kernel of the determinant, `+` the kernel of the real spinor norm, and `tilde` the kernel of the action on $A_L$."""

ORBIT_SUBGROUPS: dict[OrbitGroup, tuple[OrbitGroup, ...]] = {
    "O": ("SO", "O+", "Otilde"),
    "SO": ("SO+", "SOtilde"),
    "O+": ("SO+", "Otilde+"),
    "Otilde": ("SOtilde", "Otilde+"),
    "SO+": ("SOtilde+",),
    "SOtilde": ("SOtilde+",),
    "Otilde+": ("SOtilde+",),
}
"""Each group, with the groups among the eight that it contains as an intersection with one more kernel."""

ORBIT_IDENTITIES: dict[int, tuple[tuple[OrbitGroup, OrbitGroup], ...]] = {
    1: (("O+", "SO"), ("SO+", "SO"), ("Otilde+", "SOtilde"), ("SOtilde+", "SOtilde")),
    -1: (("O+", "O"), ("SO+", "SO"), ("Otilde+", "Otilde"), ("SOtilde+", "SOtilde")),
    0: (),
}
"""For the sign of a definite lattice (0 for another), pairs of keys that name one group.

The real spinor norm of the reflection in $w$ is $-b(w, w)/2$ modulo squares (Dawes 2022, (4)), and $O(L)$ is generated by reflections over $\\mathbb{R}$
(Cartan–Dieudonné). On a positive definite lattice every reflection has spinor norm $-1$ and determinant $-1$, so $O^+ = SO$; on a negative definite one every
reflection has spinor norm $1$, so $O^+ = O$.
"""

ORBIT_IDENTITIES_UNIMODULAR: tuple[tuple[OrbitGroup, OrbitGroup], ...] = (("Otilde", "O"), ("SOtilde", "SO"), ("Otilde+", "O+"), ("SOtilde+", "SO+"))
"""Pairs of keys that name one group when $A_L = 0$, so that $\\widetilde{O}(L) = O(L)$."""


def _is_squarefree(n: int) -> bool:
    """Whether $n \\geq 1$ has no square factor $k^2 > 1$: then every vector of norm $n$ is primitive, since $b(kv, kv) = k^2 b(v, v)$."""
    return n >= 1 and all(n % (k * k) != 0 for k in range(2, math.isqrt(n) + 1))


def _orbit_inclusion_problems(series: dict[OrbitGroup, PrimitiveOrbitSeries], group: OrbitGroup, subgroup: OrbitGroup) -> Iterator[InitErrorDetails]:
    """A subgroup $H \\subseteq G$ has at least as many orbits as $G$ on each set, and none exactly when $G$ has none."""
    if group not in series or subgroup not in series:
        return
    for n in set(series[group].degrees) & set(series[subgroup].degrees):
        large, small = series[group].coefficient(n), series[subgroup].coefficient(n)
        if large is not None and small is not None and (small < large or (small == 0) != (large == 0)):
            message = "c_{subgroup}({n}) is {small} and c_{group}({n}) is {large}, but {subgroup} is a subgroup of {group}"
            context: dict[str, str | int] = {"n": n, "group": group, "subgroup": subgroup, "small": small, "large": large}
            yield _problem("primitive_orbit_subgroup", message, ("integral", "primitive_orbits", subgroup), context)


def _orbit_equality_problems(first: PrimitiveOrbitSeries, second: PrimitiveOrbitSeries, first_name: OrbitGroup, second_name: OrbitGroup) -> Iterator[InitErrorDetails]:
    """Two keys that name one group state the same coefficients."""
    for n in set(first.degrees) & set(second.degrees):
        a, b = first.coefficient(n), second.coefficient(n)
        if a is not None and b is not None and a != b:
            message = "{first} and {second} are one group on this lattice, but c({n}) is {a} and {b}"
            context: dict[str, str | int] = {"first": first_name, "second": second_name, "n": n, "a": a, "b": b}
            yield _problem("primitive_orbit_same_group", message, ("integral", "primitive_orbits", first_name), context)


OrbitCounts = Annotated[tuple[Annotated[int, Field(ge=0)] | None, ...], Field(strict=False)]


class PrimitiveOrbitSeries(Record):
    """The series $F_{L,\\Gamma}(z, w) = c_\\Gamma(0) + \\sum_{n \\geq 1} c_\\Gamma(n) z^n + \\sum_{n \\geq 1} c_\\Gamma(-n) w^n$ in $\\mathbb{Z}[[z, w]]$.

    $c_\\Gamma(n)$ is the number of $\\Gamma$-orbits on the primitive vectors $v$ with $b(v, v) = n$. A coefficient that is not known is null.
    """

    constant: Annotated[int, Field(ge=0)] | None = Field(default=None, description="$c_\\Gamma(0)$, the number of orbits of primitive isotropic vectors.")
    z: OrbitCounts = Field(default=(), description="$c_\\Gamma(1), c_\\Gamma(2), \\dots$: the coefficients of $z, z^2, \\dots$")
    w: OrbitCounts = Field(default=(), description="$c_\\Gamma(-1), c_\\Gamma(-2), \\dots$: the coefficients of $w, w^2, \\dots$")
    reference: Reference | None = Field(default=None, description="The source of the coefficients; absent when `latticedb enrich --genus-data` computes them.")

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


class DiscriminantSequenceData(Record):
    """A finite discriminant action, its kernel order, and its pointed coset quotient."""

    discriminant_factors: list[int]
    discriminant_basis_lifts: list[list[str]]
    discriminant_quadratic_gram: list[list[str]]
    lattice_group_order: Annotated[int, Field(gt=0)] | None = None
    lattice_generator_morphisms: list[str] | None = None
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
        matrices = [*self.discriminant_generators, *self.image_generators, *self.coset_representatives]
        if any(len(rows) != size or any(len(row) != size for row in rows) for rows in matrices):
            raise ValueError("discriminant isometry matrices must be square in the stated basis")
        if len(self.discriminant_basis_lifts) != size or len(self.discriminant_quadratic_gram) != size:
            raise ValueError("the discriminant basis and quadratic Gram matrix must match the invariant factors")
        if self.lattice_generator_morphisms is not None and len(self.lattice_generator_morphisms) != len(self.image_generators):
            raise ValueError("each lattice generator must have one induced discriminant isometry")
        if (self.lattice_group_order is None) != (self.kernel_order is None):
            raise ValueError("the lattice and kernel orders are stated together")
        if self.lattice_group_order is not None and self.kernel_order is not None and self.lattice_group_order != self.kernel_order * self.image_order:
            raise ValueError("the lattice group order must equal the kernel order times the image order")
        if self.discriminant_group_order != self.image_order * len(self.coset_representatives):
            raise ValueError("the discriminant group order must equal the image order times the coset count")
        if self.mm_trivial != (len(self.coset_representatives) == 1):
            raise ValueError("MM-triviality means that the pointed coset set has one element")
        if self.image_normal != (self.quotient_multiplication is not None and self.quotient_generator_cosets is not None):
            raise ValueError("quotient group data are present exactly when the image is normal")
        if self.quotient_multiplication is not None:
            count = len(self.coset_representatives)
            if len(self.quotient_multiplication) != count or any(len(row) != count for row in self.quotient_multiplication):
                raise ValueError("the quotient multiplication table must index the cosets")
            if any(value < 0 or value >= count for row in self.quotient_multiplication for value in row):
                raise ValueError("quotient products must index the stated cosets")
            if any(self.quotient_multiplication[0][i] != i or self.quotient_multiplication[i][0] != i for i in range(count)):
                raise ValueError("the distinguished coset is the quotient identity")
        if self.quotient_invariant_factors is not None:
            factors = self.quotient_invariant_factors
            table = self.quotient_multiplication
            if table is None or math.prod(factors) != len(self.coset_representatives) or any(second % first for first, second in zip(factors, factors[1:], strict=False)) or any(table[i][j] != table[j][i] for i in range(len(table)) for j in range(i)):
                raise ValueError("quotient invariant factors require an abelian quotient group of the stated size")
        if self.mm_f2_dimension is not None:
            table = self.quotient_multiplication
            if table is None or 2**self.mm_f2_dimension != len(self.coset_representatives) or any(table[i][i] != 0 for i in range(len(table))):
                raise ValueError("the F2 dimension requires an elementary abelian quotient of the stated size")
        return self


class IntegralData(Record):
    """Invariants of a lattice whose form takes integer values. Required when every $b(e_i, e_j)$ is an integer."""

    parity: Literal["even", "odd"] = Field(description="`even` when $b(x, x)$ is even for every $x$, `odd` otherwise.")
    level: Annotated[int, Field(gt=0)] | None = Field(
        default=None,
        description="Least positive $k$ for which $k b(x,x)$ is even for every $x$ in the dual lattice. Requires nonzero determinant.",
    )
    modular_scale: Annotated[int, Field(gt=0)] | None = Field(
        default=None,
        description="The $k$ of an isometry $L\\cong L^*(k)$ recorded by a dual-isometry morphism.",
    )
    discriminant_group: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Invariant factors $d_1 \\mid d_2 \\mid \\dots$, each greater than 1, of the cokernel of the correlation $L \\to \\operatorname{Hom}(L, \\mathbb{Z})$. "
            "The empty list is the trivial group. Required when the determinant is not zero."
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
            f"Stated when the determinant is not zero and $A_L$ has at most {arithmetic.SUBGROUP_BOUND} subgroups; otherwise absent, and the count is not decided."
        ),
    )
    delta: Literal[0, 1] | None = Field(
        default=None,
        description=(
            "Nikulin's invariant $\\delta$ of an even lattice with $2 A_L = 0$: "
            "0 when $b(x, x)$ is an integer for every $x$ in the dual lattice $L^*$, and 1 otherwise. "
            "With the rank $r$ and $A_L \\cong (\\mathbb{Z}/2)^a$ it gives $(r, a, \\delta)$. "
            "Required for, and only for, an even lattice whose determinant is not zero and whose invariant factors all equal 2."
        ),
    )
    bad_reduction_primes: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The primes that divide $2 \\det L$, in increasing order: the primes $p$ at which $Q(x) = b(x, x)$ is degenerate modulo $p$. "
            "Outside them and the primes that divide $n$, the scheme $Q(x) = n$ over $\\mathbb{Z}$ has good reduction. Required for, and only for, a nonzero determinant."
        ),
    )
    quadratic_character: int | None = Field(
        default=None,
        description=(
            "For rank $2m$: the discriminant $d$ of the field $\\mathbb{Q}(\\sqrt{D})$ with $D = (-1)^m \\det L$, and 1 when $D$ is a square. "
            "For $p \\nmid 2 \\det L$ the Kronecker symbol $\\chi_D(p) = (d / p)$ is 1 exactly when $Q$ modulo $p$ is a sum of $m$ hyperbolic planes, "
            "and it determines the number of points of $Q(x) = n$ over $\\mathbb{F}_{p^k}$. "
            "Required for, and only for, an even rank and a nonzero determinant."
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
            "Computed by `latticedb enrich --genus-data` with `Genus(G).representatives()` of SageMath; for an indefinite binary form, the representatives counted up to equivalence. "
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
            "Computed by `latticedb enrich --genus-data` with `Genus(G).spinor_generators(proper=False)` of SageMath. Requires a nonzero determinant and rank at least 3."
        ),
    )
    spinor_genera: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The number of isometry classes in each spinor genus of the genus of $L$: first in the spinor genus of $L$, then in the others in decreasing order. "
            "The first entry is the class number of the spinor genus of $L$, and the sum is the class number of the genus. "
            "An indefinite $L$ has one class in each spinor genus (Eichler; SPLAG, Chapter 15, Theorem 14). For a definite $L$, `latticedb enrich --genus-data` iterates "
            "$p$-neighbours from one lattice of each spinor genus at a prime $p$ whose spinor operator is in the spinor kernel, so that each neighbour stays in its "
            "spinor genus (SPLAG, Chapter 15, Theorem 15), and stores the counts only when the masses $\\sum 1/|O(M)|$ of the classes found add up to the mass "
            "of the genus. Requires a nonzero determinant and rank at least 3."
        ),
    )
    hyperbolic_index: int | None = Field(
        default=None,
        ge=0,
        description=(
            "The largest $n$ with $L \\cong U^n \\oplus L'$ for a lattice $L'$, where $U$ is the hyperbolic plane. "
            "For an integral $L$ this is the largest $n$ with an embedding $U^n \\hookrightarrow L$, because a unimodular sublattice $M$ of $L$ "
            "satisfies $L = M \\oplus M^{\\perp}$. "
            "Computed by `latticedb enrich --genus-data`: $L \\cong U^n \\oplus L'$ holds exactly when the genus of $L$ is the sum of the genus of $U^n$ and a genus of "
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
            "Computed by `latticedb enrich --genus-data` through $z^4$ and $w^4$ for a definite lattice, and from $(A_L, q_L)$ for an even lattice of hyperbolic index at least 2 "
            "(Gritsenko, Hulek and Sankaran 2009, Proposition 3.3(i); Nikulin 1980, Theorem 1.14.2); stated with a reference otherwise. Requires a nonzero determinant."
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

    minimum: Rational = Field(description="Least value of $b(x, x)$ over nonzero $x$.")
    kissing_number: int = Field(description="Number of $x$ with $b(x, x)$ equal to the minimum; finite because $b$ is definite.")
    automorphism_group_order: int | None = Field(default=None, description="Order of $O(L)$, computed by `latticedb enrich --genus-data` with `qfauto` of PARI/GP.")
    minimal_vectors: list[list[int]] | None = Field(default=None, description="A complete minimal shell in the record basis; its size equals `kissing_number`.")
    perfect: bool | None = Field(default=None, description="Whether the rank-one tensors $v v^T$ of minimal vectors span $\\operatorname{Sym}^2(\\mathbb Q^n)$.")
    regular: bool | None = Field(default=None, description="For an integral ternary form: every positive integer represented by its genus is represented by this lattice.")
    spinor_regular: bool | None = Field(default=None, description="For an integral ternary form: every positive integer represented by its spinor genus is represented by this lattice.")
    theta_series: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Entry $k$ is the number of $x$ with $b(x, x) = k$, for $k = 0, 1, 2, \\dots$ Required for, and only for, integer values. "
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
            "Required for, and only for, integer values."
        ),
    )
    roots: Annotated[tuple[RootSystemComponent, ...], Field(strict=False)] = Field(
        description="The root system $\\Phi(L)$ as its irreducible components, each with a base; `[]` when $L$ has no roots.",
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


def definiteness(n_plus: int, n_minus: int, n_zero: int) -> Definiteness:
    match (n_plus > 0, n_minus > 0, n_zero > 0):
        case (True, True, _):
            return "indefinite"
        case (True, False, False):
            return "positive_definite"
        case (False, True, False):
            return "negative_definite"
        case (True, False, True):
            return "positive_semidefinite"
        case (False, True, True):
            return "negative_semidefinite"
        case _:
            return "zero"


def theta_bound(rank: int, minimum: Fraction) -> int:
    """The least norm through which the theta series of a record states its counts: past the minimum, and further for small ranks."""
    match rank:
        case _ if rank <= 4:
            default = 12
        case _ if rank <= 8:
            default = 8
        case _ if rank <= 12:
            default = 6
        case _:
            default = 4
    return max(int(minimum), default)


class Lattice(Record):
    tag: Tag = Field(description="Permanent identifier: four characters from 0-9 and A-Z. The file name is the tag.")
    name: str = Field(description="Name as plain text, for search.")
    latex: str = Field(description="Name as TeX, without math delimiters.")
    aliases: Annotated[tuple[str, ...], Field(strict=False)] = Field(default=(), description="Other names, as plain text.")
    rank: int | None = Field(default=None, ge=1, description="Rank of the underlying free module, when the source states it.")
    gram_tensor: Annotated[tuple[Annotated[tuple[Rational, ...], Field(strict=False)], ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Components of the Gram tensor, the symmetric (0,2)-tensor $b$, in a basis $e_1, \\dots, e_n$: "
            "row $i$ lists $b(e_i, e_1), \\dots, b(e_i, e_n)$. Values are integers or strings `p/q`."
        )
    )
    signature: Annotated[tuple[int, int], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "`[n_plus, n_minus]`: the numbers of $v$ with $b(v, v) > 0$ and with $b(v, v) < 0$ in a $b$-orthogonal basis of $L \\otimes \\mathbb{Q}$. "
            "They do not depend on the basis (Sylvester's law of inertia)."
        )
    )
    determinant: Rational | None = Field(default=None, description="$\\det(b(e_i, e_j))$. It is the same for every basis of $L$.")
    definiteness: Definiteness | None = Field(
        default=None,
        description=(
            "`positive_definite` or `negative_definite` when $b(x, x)$ has one sign on nonzero $x$; `indefinite` when it takes both signs; "
            "`positive_semidefinite` when $b(x, x) \\geq 0$ for all $x$, $b \\neq 0$ and the determinant is zero, "
            "and `negative_semidefinite` with $\\leq$; `zero` when $b = 0$."
        )
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

    @property
    def nullity(self) -> int | None:
        return None if self.rank is None or self.signature is None else self.rank - self.signature[0] - self.signature[1]

    @property
    def is_nondegenerate(self) -> bool:
        return self.nullity is not None and self.nullity == 0

    @property
    def is_definite(self) -> bool:
        return self.definiteness in ("positive_definite", "negative_definite")

    @property
    def is_unimodular(self) -> bool:
        return self.integral is not None and self.determinant is not None and abs(self.determinant) == 1

    @property
    def is_two_elementary_even(self) -> bool:
        """Whether $L$ is even and nondegenerate with $2 A_L = 0$: the lattices with Nikulin's invariants $(r, a, \\delta)$."""
        integral = self.integral
        if integral is None or integral.parity != "even" or integral.discriminant_group is None:
            return False
        return all(factor == 2 for factor in integral.discriminant_group)

    @property
    def is_hyperbolic(self) -> bool:
        return self.is_nondegenerate and self.rank is not None and self.rank >= 2 and self.signature is not None and min(self.signature) == 1

    @property
    def is_integer_valued(self) -> bool:
        return self.gram_tensor is not None and all(entry.denominator == 1 for row in self.gram_tensor for entry in row)

    @property
    def root_count(self) -> int:
        """$|\\Phi(L)|$ for a definite lattice: the sum of the numbers of roots of the types of its components."""
        assert self.definite is not None, "a lattice that is not definite can have infinitely many roots"
        return sum(root_systems.root_count(component.type) for component in self.definite.roots)

    @property
    def root_span_factors(self) -> tuple[int, ...] | None:
        """The invariant factors of $R(L)$ in $L$; `None` when $R(L)$ is not decided."""
        return None if self.root_sublattice is None else self.root_sublattice.invariant_factors

    @property
    def root_span_rank(self) -> int | None:
        """The rank of $R(L)$."""
        factors = self.root_span_factors
        return None if factors is None else len(factors)

    @property
    def root_span_index(self) -> int | None:
        """$[M' : R(L)]$ for the primitive sublattice $M' = L \\cap (R(L) \\otimes \\mathbb{Q})$. It is $[L : R(L)]$ when the ranks agree."""
        factors = self.root_span_factors
        return None if factors is None else math.prod(factors)

    @property
    def root_span_is_primitive(self) -> bool | None:
        """Whether $R(L)$ is primitive in $L$; `None` when $R(L)$ is not decided."""
        index = self.root_span_index
        return None if index is None else index == 1

    @property
    def is_root_lattice(self) -> bool | None:
        """Whether $L = R(L)$; `None` when $R(L)$ is not decided."""
        factors = self.root_span_factors
        return None if factors is None else factors == (1,) * self.rank

    @property
    def root_norms(self) -> tuple[Fraction, ...] | None:
        """A set $S$ with $L = \\mathbb{Z}\\Phi_S(L)$, for a root lattice; `None` for another lattice."""
        return None if self.root_sublattice is None else self.root_sublattice.norms

    def _well_defined(self) -> Self:
        """Verify the mathematical fields of a parsed card when the check workflow runs."""
        problems = list(self._shape_problems())
        if not problems:
            problems = [
                *self._integral_problems(),
                *self._definite_problems(),
                *self._indefinite_problems(),
                *self._root_problems(),
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
            yield _problem("signature_shape", "n_plus and n_minus are nonnegative with n_plus + n_minus <= {rank}", ("signature",), {"rank": self.rank})

    def _integral_problems(self) -> Iterator[InitErrorDetails]:
        if self.integral is None:
            return
        if not self.is_integer_valued:
            yield _problem("integral_requires_integer_values", "the `integral` block requires every b(e_i, e_j) to be an integer", ("integral",))
            return
        if self.determinant == 0:
            if self.integral.level is not None or self.integral.modular_scale is not None:
                yield _problem("dual_invariants_nondegenerate", "level and modularity require a nonzero determinant", ("integral",))
            if self.integral.discriminant_group is not None:
                message = "the discriminant group is finite only when the determinant is not zero"
                yield _problem("discriminant_group_requires_nondegenerate", message, ("integral", "discriminant_group"))
            if self.integral.genus_symbol is not None:
                yield _problem("genus_requires_nondegenerate", "the genus symbol requires a nonzero determinant", ("integral", "genus_symbol"))
            if self.integral.genus_class_count is not None:
                message = "the class number of the genus requires a nonzero determinant"
                yield _problem("genus_class_count_requires_nondegenerate", message, ("integral", "genus_class_count"))
            if self.integral.hyperbolic_index is not None:
                message = "the hyperbolic index requires a nonzero determinant"
                yield _problem("hyperbolic_index_requires_nondegenerate", message, ("integral", "hyperbolic_index"))
            if self.integral.overlattice_count is not None:
                message = "the number of overlattices is finite only when the determinant is not zero"
                yield _problem("overlattice_count_requires_nondegenerate", message, ("integral", "overlattice_count"))
            if self.integral.primitive_orbits is not None:
                message = "the series of orbits of primitive vectors requires a nonzero determinant"
                yield _problem("primitive_orbits_requires_nondegenerate", message, ("integral", "primitive_orbits"))
        elif self.integral.discriminant_group is None:
            yield _problem("discriminant_group_missing", "the determinant is not zero, so `discriminant_group` is required", ("integral", "discriminant_group"))
        if self.integral.level is not None and self.determinant != 0 and self.integral.level != arithmetic.level(self.gram_tensor):
            yield _problem("level_value", "the stated level does not equal the level of the dual quadratic form", ("integral", "level"))
        if self.integral.discriminant_sequence is not None:
            if self.determinant == 0 or self.integral.parity != "even":
                yield _problem("discriminant_sequence_hypothesis", "the discriminant sequence requires a nondegenerate even lattice", ("integral", "discriminant_sequence"))
            elif tuple(self.integral.discriminant_sequence.discriminant_factors) != self.integral.discriminant_group:
                yield _problem("discriminant_sequence_factors", "the discriminant sequence must use the stated invariant factors", ("integral", "discriminant_sequence", "discriminant_factors"))
        defined = self.is_two_elementary_even
        if defined and self.integral.delta is None:
            yield _problem("delta_missing", "the lattice is even with 2 A_L = 0, so `delta` is required", ("integral", "delta"))
        if not defined and self.integral.delta is not None:
            yield _problem("delta_requires_two_elementary_even", "`delta` requires an even lattice with 2 A_L = 0 and a nonzero determinant", ("integral", "delta"))
        if self.integral.primitive_orbits is not None and self.determinant != 0:
            yield from self._orbit_problems(self.integral.primitive_orbits)
        yield from self._spinor_problems()
        yield from self._reduction_problems()

    def _reduction_problems(self) -> Iterator[InitErrorDetails]:
        """The primes of bad reduction and the character of the discriminant are those of the determinant."""
        assert self.integral is not None
        determinant = int(self.determinant)
        primes = arithmetic.bad_reduction_primes(determinant) if determinant != 0 else None
        if self.integral.bad_reduction_primes != primes:
            context: dict[str, str | int] = {"stated": str(self.integral.bad_reduction_primes), "computed": str(primes)}
            yield _problem("bad_reduction_primes", "`bad_reduction_primes` is {stated}, and the determinant gives {computed}", ("integral", "bad_reduction_primes"), context)
        character = arithmetic.quadratic_character(self.rank, determinant) if determinant != 0 and self.rank % 2 == 0 else None
        if self.integral.quadratic_character != character:
            context = {"stated": str(self.integral.quadratic_character), "computed": str(character)}
            yield _problem("quadratic_character", "`quadratic_character` is {stated}, and rank and determinant give {computed}", ("integral", "quadratic_character"), context)

    def _spinor_problems(self) -> Iterator[InitErrorDetails]:
        """Spinor genera exist for a nondegenerate lattice of rank at least 3; their number is a power of 2, and their classes make up the genus."""
        assert self.integral is not None
        count, genera = self.integral.spinor_genus_count, self.integral.spinor_genera
        if count is None and genera is None:
            return
        if self.determinant == 0 or self.rank < 3:
            yield _problem("spinor_genera_require_rank_three", "spinor genera require a nonzero determinant and rank at least 3", ("integral", "spinor_genus_count"))
            return
        if count is not None and count & (count - 1):
            yield _problem("spinor_genus_count_power_of_two", "the number of spinor genera is {count}, not a power of 2", ("integral", "spinor_genus_count"), {"count": count})
        if genera is None:
            return
        location = ("integral", "spinor_genera")
        if not genera or min(genera) < 1 or list(genera[1:]) != sorted(genera[1:], reverse=True):
            yield _problem("spinor_genera_order", "the class numbers of the spinor genera are positive, and after the first in decreasing order", location)
        if count is not None and len(genera) != count:
            yield _problem("spinor_genera_count", "{listed} spinor genera are listed, and there are {count}", location, {"listed": len(genera), "count": count})
        total = self.integral.genus_class_count
        if total is not None and sum(genera) != total:
            yield _problem("spinor_genera_sum", "the spinor genera hold {sum} classes, and the genus holds {total}", location, {"sum": sum(genera), "total": total})
        if self.definite is None and set(genera) != {1}:
            yield _problem("spinor_genera_indefinite", "a spinor genus of an indefinite lattice of rank at least 3 holds one class", location)

    def _orbit_problems(self, series: dict[OrbitGroup, PrimitiveOrbitSeries]) -> Iterator[InitErrorDetails]:
        """The coefficients vanish where no primitive vector has norm n, grow from a group to a subgroup, and agree for two keys that name one group."""
        assert self.integral is not None
        even = self.integral.parity == "even"
        sign = {"positive_definite": 1, "negative_definite": -1}.get(self.definiteness, 0)
        theta = self.definite.theta_series if self.definite is not None else None
        for group, values in series.items():
            location = ("integral", "primitive_orbits", group)
            for n in values.degrees:
                count = values.coefficient(n)
                if count is None:
                    continue
                if count > 0 and ((even and n % 2 != 0) or (sign != 0 and n * sign <= 0)):
                    yield _problem("primitive_orbit_without_vectors", "c({n}) is {count}, but no vector of L has norm {n}", location, {"n": n, "count": count})
                if theta is not None and 0 < n * sign < len(theta) and (count > 0) != (theta[n * sign] > 0) and (count > 0 or _is_squarefree(n * sign)):
                    message = "c({n}) is {count}, and the theta series has {vectors} vectors of norm {n}"
                    yield _problem("primitive_orbit_theta_series", message, location, {"n": n, "count": count, "vectors": theta[n * sign]})
        for group, subgroups in ORBIT_SUBGROUPS.items():
            for subgroup in subgroups:
                yield from _orbit_inclusion_problems(series, group, subgroup)
        same = ORBIT_IDENTITIES[sign] + (ORBIT_IDENTITIES_UNIMODULAR if self.is_unimodular else ())
        for first, second in same:
            if first in series and second in series:
                yield from _orbit_equality_problems(series[first], series[second], first, second)

    def _definite_problems(self) -> Iterator[InitErrorDetails]:
        if self.definite is None:
            return
        if not self.is_definite:
            yield _problem("definite_requires_definite", "the `definite` block requires a positive definite or negative definite form", ("definite",))
            return
        data = self.definite
        integer_valued = self.is_integer_valued
        for name, value in (("theta_series", data.theta_series), ("root_system", data.root_system)):
            if integer_valued and value is None:
                yield _problem(f"{name}_missing", "every b(e_i, e_j) is an integer, so `{name}` is required", ("definite", name), {"name": name})
            if not integer_valued and value is not None:
                yield _problem(f"{name}_requires_integral", "`{name}` requires an integer-valued form", ("definite", name), {"name": name})
        if data.theta_series is not None and len(data.theta_series) <= theta_bound(self.rank, data.minimum):
            yield _problem(
                "theta_series_short",
                "the theta series of a lattice of rank {rank} and minimum {minimum} states the counts through norm {bound}",
                ("definite", "theta_series"),
                {"rank": self.rank, "minimum": str(data.minimum), "bound": theta_bound(self.rank, data.minimum)},
            )
        if any(len(component.simple_roots) != component.rank or any(len(row) != self.rank for row in component.simple_roots) for component in data.roots):
            yield _problem("roots_shape", "a component of rank m has m simple roots, each with {rank} coordinates", ("definite", "roots"), {"rank": self.rank})
        if data.minimal_vectors is not None:
            vectors = data.minimal_vectors
            if len(vectors) != data.kissing_number or len({tuple(v) for v in vectors}) != len(vectors) or any(len(v) != self.rank for v in vectors):
                yield _problem("minimal_shell_shape", "the complete minimal shell has distinct vectors of the lattice rank and the kissing number", ("definite", "minimal_vectors"))
            else:
                sign = 1 if self.definiteness == "positive_definite" else -1
                if any(sign * sum((v[i] * self.gram_tensor[i][j] * v[j] for i in range(self.rank) for j in range(self.rank)), Fraction()) != data.minimum for v in vectors):
                    yield _problem("minimal_shell_norm", "each minimal vector has the stated minimum norm", ("definite", "minimal_vectors"))
                if data.perfect is not None and data.perfect != arithmetic.is_perfect(self.rank, vectors):
                    yield _problem("perfectness_value", "minimal-vector tensors give a different perfectness value", ("definite", "perfect"))
        elif data.perfect is not None:
            yield _problem("perfectness_witness", "perfectness requires the complete minimal shell", ("definite", "perfect"))
        if (data.regular is not None or data.spinor_regular is not None) and (self.rank != 3 or self.integral is None):
            yield _problem("ternary_regularity", "regularity and spinor regularity require an integral ternary lattice", ("definite",))

    def _indefinite_problems(self) -> Iterator[InitErrorDetails]:
        indefinite = self.definiteness == "indefinite"
        if self.indefinite is not None and not indefinite:
            yield _problem("indefinite_requires_indefinite", "the `indefinite` block requires a form that takes both signs", ("indefinite",))
        if self.hyperbolic is not None and not self.is_hyperbolic:
            message = "the `hyperbolic` block requires a nondegenerate form of signature (1, n) or (n, 1) with n >= 1"
            yield _problem("hyperbolic_requires_hyperbolic", message, ("hyperbolic",))

    def _root_problems(self) -> Iterator[InitErrorDetails]:
        span = self.root_span
        if span is not None:
            if self.is_definite:
                yield _problem("root_span_on_definite", "`definite.roots` states the roots of a definite lattice, so the `root_span` block is an error there", ("root_span",))
            if any(len(row) != self.rank for row in (*span.roots, *(span.embedding or ()))):
                yield _problem("root_span_shape", "each row lists {rank} coordinates", ("root_span",), {"rank": self.rank})
            if len(span.norms) != len(span.roots):
                yield _problem("root_span_norms_shape", "`norms` has one entry for each row of `roots`", ("root_span", "norms"))
            if (span.summands is None) != (span.embedding is None):
                yield _problem("root_span_representative_incomplete", "`summands` and `embedding` are stated together", ("root_span",))
        sublattice = self.root_sublattice
        decided = self.definite is not None or span is not None
        if sublattice is None:
            if decided:
                yield _problem("root_sublattice_missing", "the roots of the lattice are stated, so the `root_sublattice` block is required", ("root_sublattice",))
            return
        if not decided:
            yield _problem("root_sublattice_not_decided", "the `root_sublattice` block requires `definite` or `root_span`", ("root_sublattice",))
            return
        factors = sublattice.invariant_factors
        if len(factors) > self.rank or any(d < 1 for d in factors) or any(second % first != 0 for first, second in zip(factors, factors[1:], strict=False)):
            message = "at most {rank} positive invariant factors, each dividing the next"
            yield _problem("root_sublattice_factors_shape", message, ("root_sublattice", "invariant_factors"), {"rank": self.rank})
        if (sublattice.norms is not None) != (factors == (1,) * self.rank):
            yield _problem("root_sublattice_norms", "`norms` is present exactly for a root lattice", ("root_sublattice", "norms"))


def _subdivision_problems(lines: Vector, size: int, location: tuple[str, ...]) -> Iterator[InitErrorDetails]:
    if any(not 0 < line < size for line in lines) or any(first >= second for first, second in zip(lines, lines[1:], strict=False)):
        yield _problem("subdivision_range", "the lines increase strictly and each lies strictly between 0 and {size}", location, {"size": size})


class Morphism(Record):
    """A morphism $\\varphi \\colon S(c) \\to T$ of lattices.

    A $\\mathbb{Z}$-linear map with $b_T(\\varphi x, \\varphi y) = c \\, b_S(x, y)$ for a nonzero integer $c$, 1 by default.

    Its matrix is in the chosen bases of $S$ and $T$, which list the orthogonal summands in the order of their names.
    """

    name: str = Field(description="Name as plain text; TeX between `$` signs is rendered.")
    description: str | None = Field(default=None, description="One or two sentences on the morphism, as plain text with TeX between `$` signs.")
    matrix: Annotated[tuple[IntegerVector, ...], Field(strict=False, min_length=1)] = Field(
        description=(
            "Matrix of $\\varphi$, with $\\operatorname{rank} T$ rows and $\\operatorname{rank} S$ columns: column $j$ lists the coordinates of $\\varphi(e_j)$ "
            "in the chosen basis of $T$, so that $M^{\\top} G_T M = c \\, G_S$ for the matrices $G_S = (b_S(e_i, e_j))$ and $G_T = (b_T(e_i, e_j))$. "
            "A SageMath morphism `phi` gives `phi.matrix().transpose()`, because SageMath lists the images in rows."
        )
    )
    scale: int = Field(
        default=1,
        description=(
            "The nonzero integer $c$ with $b_T(\\varphi x, \\varphi y) = c \\, b_S(x, y)$: the map is a morphism $S(c) \\to T$ from the twist of $S$ by $c$. "
            "Absent for $c = 1$. A lattice that a source names as a twist $M(c)$ of the record $M$ maps to $T$ with this scale."
        ),
    )
    row_subdivisions: IntegerVector = Field(
        default=(),
        description=(
            "Lines between the rows, as `M.subdivisions()` of SageMath states them: a line $k$ lies between rows $k$ and $k + 1$. "
            "The basis vectors of $T$ between two consecutive lines span an orthogonal summand of $T$."
        ),
    )
    column_subdivisions: IntegerVector = Field(
        default=(),
        description=(
            "Lines between the columns: a line $k$ lies between columns $k$ and $k + 1$. "
            "The basis vectors of $S$ between two consecutive lines span an orthogonal summand of $S$."
        ),
    )

    @model_validator(mode="after")
    def _well_defined(self) -> Self:
        columns = len(self.matrix[0])
        problems: list[InitErrorDetails] = []
        if columns == 0 or any(len(row) != columns for row in self.matrix):
            problems.append(_problem("matrix_shape", "the rows of the matrix are nonempty and have one length", ("matrix",)))
        if self.scale == 0:
            problems.append(_problem("scale_nonzero", "the scale c of a morphism S(c) -> T is not zero", ("scale",)))
        problems.extend(_subdivision_problems(self.row_subdivisions, len(self.matrix), ("row_subdivisions",)))
        problems.extend(_subdivision_problems(self.column_subdivisions, columns, ("column_subdivisions",)))
        if problems:
            raise ValidationError.from_exception_data(type(self).__name__, problems)
        return self

    @property
    def images(self) -> tuple[Vector, ...]:
        """The columns of the matrix: the coordinates of $\\varphi(e_1), \\varphi(e_2), \\dots$."""
        return tuple(zip(*self.matrix, strict=True))


class Morphisms(Record):
    """The front matter of `morphisms/<S>-<T>.md`: morphisms from the lattice $S$ to the lattice $T$ of the corpus."""

    source: Tag = Field(description="Tag of the source $S$.")
    target: Tag = Field(description="Tag of the target $T$.")
    morphisms: Annotated[tuple[Morphism, ...], Field(strict=False, min_length=1)] = Field(description="The morphisms $S \\to T$.")
