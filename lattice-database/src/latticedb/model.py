"""The record of one lattice, with the checks that make the record well defined.

A lattice here is a free module of finite rank over the integers with a
symmetric bilinear form `b` that takes rational values. The Gram tensor of
the lattice is `b`, a symmetric (0,2)-tensor; a record gives its components
`b(e_i, e_j)` in a basis. The form is not assumed positive definite,
integral, or nondegenerate: each of those is declared, and each declaration
is checked against the Gram tensor.

Invariants that exist only under a hypothesis live in a block named for the
hypothesis (`integral`, `definite`, `indefinite`, `hyperbolic`). A block on a
lattice that does not satisfy its hypothesis is a validation error.
"""

import math
import re
from collections.abc import Iterator
from datetime import date
from fractions import Fraction
from functools import cached_property
from itertools import combinations
from typing import Annotated, Literal, Self

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, ValidationError, model_validator
from pydantic_core import InitErrorDetails, PydanticCustomError

from latticedb import arithmetic, root_systems
from latticedb.arithmetic import Vector

type Yaml = None | bool | int | float | str | date | list[Yaml] | dict[str, Yaml]
"""A value that a YAML document can hold."""

_RATIONAL = re.compile(r"-?\d+(/[1-9]\d*)?")


def _rational(value: Yaml | Fraction) -> Fraction:
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


Rational = Annotated[Fraction, BeforeValidator(_rational)]
Tag = Annotated[str, Field(pattern=r"^[0-9A-Z]{4}$")]
Family = Annotated[str, Field(pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$")]
AdeType = Annotated[str, Field(pattern=r"^(A[1-9]\d*|D[4-9]|D[1-9]\d+|E[678])$")]
RootType = Annotated[str, Field(pattern=root_systems.TYPE_PATTERN)]
IntegerVector = Annotated[tuple[int, ...], Field(strict=False)]
Definiteness = Literal[
    "positive_definite",
    "negative_definite",
    "indefinite",
    "positive_semidefinite",
    "negative_semidefinite",
    "zero",
]


class Record(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)


class Related(Record):
    tag: Tag = Field(description="Tag of another lattice in the catalogue.")
    relation: str = Field(description="How that lattice is related to this one, as a short phrase.")


class Reference(Record):
    citation: str = Field(description="Bibliographic citation as plain text.")
    url: str | None = Field(default=None, description="Address of the source, when it has one.")


class Provenance(Record):
    source: str = Field(description="Where the Gram tensor and the recorded invariants come from.")
    url: str | None = Field(default=None, description="Address of the source record, when it has one.")
    computed_with: str | None = Field(default=None, description="Software that computed the recorded invariants.")


class IntegralData(Record):
    """Invariants of a lattice whose form takes integer values. Required when every $b(e_i, e_j)$ is an integer."""

    parity: Literal["even", "odd"] = Field(description="`even` when $b(x, x)$ is even for every $x$, `odd` otherwise.")
    discriminant_group: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Invariant factors $d_1 \\mid d_2 \\mid \\dots$, each greater than 1, of the cokernel of the correlation $L \\to \\operatorname{Hom}(L, \\mathbb{Z})$. "
            "The empty list is the trivial group. Required when the determinant is not zero."
        ),
    )
    genus_symbol: str | None = Field(
        default=None,
        description=(
            "`I` (odd) or `II` (even) with the signature, such as `II_{1,9}`. When the determinant is not 1 or -1, the local symbol at each prime "
            "that divides twice the determinant follows in parentheses, in the notation that SageMath prints. Requires a nonzero determinant."
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
            "The $k \\neq 0$ such that a short root $r$ of the component has $b(r, r) = 2k$. "
            "The simple roots have $b(\\alpha_i, \\alpha_j) = k\\,(\\alpha_i, \\alpha_j)$, "
            "where $(\\alpha_i, \\alpha_j)$ is the entry of the symmetrized Cartan matrix of the type in which a short root has norm 2. "
            "$k$ is negative on a negative definite lattice."
        )
    )
    simple_roots: Annotated[tuple[IntegerVector, ...], Field(strict=False)] = Field(
        description=(
            "Row $i$ lists the coordinates of the simple root $\\alpha_i$ in the basis $e_1, \\dots, e_n$ of the record. "
            "The simple roots are numbered as SageMath's `CartanMatrix` numbers them. "
            "The rows of all components are a basis of $\\mathbb{Z}\\Phi(L)$: "
            "they are the matrix of the embedding into $L$ of the orthogonal sum of the root lattices of the components."
        )
    )


class DefiniteData(Record):
    """Invariants of a definite lattice. They are stated for a positive definite form; on a negative definite lattice they are the invariants of $-b$."""

    minimum: Rational = Field(description="Least value of $b(x, x)$ over nonzero $x$.")
    kissing_number: int | None = Field(
        default=None,
        description="Number of $x$ with $b(x, x)$ equal to the minimum. The number is finite because the form is definite.",
    )
    automorphism_group_order: int | None = Field(default=None, description="Order of the group of isometries of the lattice.")
    theta_series: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description="Entry $k$ is the number of $x$ with $b(x, x) = k$, for $k = 0, 1, 2, \\dots$ Requires integer values.",
    )
    root_system: Annotated[tuple[AdeType, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "ADE type of $\\Phi_{\\{2\\}}(L) = \\{r \\in L : b(r, r) = 2\\}$, as irreducible components in any order: `[E8]`, `[A1, A1]`, or `[]` when it is empty. "
            "$\\mathbb{Z}\\Phi_{\\{2\\}}(L)$ is the orthogonal sum of the root lattices of the components (Witt's theorem); it is not primitive in $L$ in general. "
            "The field `roots` states all of $\\Phi(L)$. Requires integer values."
        ),
    )
    roots: Annotated[tuple[RootSystemComponent, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "The root system $\\Phi(L)$ as its irreducible components, each with a base; `[]` when $L$ has no roots. "
            "The build lists the roots of $L$, and it rejects a declaration that is not $\\Phi(L)$. `just roots` writes the field."
        ),
    )


class IndefiniteData(Record):
    """Invariants of a lattice on which $b(x, x)$ takes both signs."""

    isotropic: bool = Field(description="Whether $b(x, x) = 0$ for some nonzero $x$.")


class HyperbolicData(Record):
    """Invariants of a nondegenerate lattice of rank at least 2 whose signature is $(1, n)$ or $(n, 1)$."""

    reflective: bool = Field(description="Whether the subgroup generated by reflections has finite index in the isometry group.")


class RootSpan(Record):
    """$\\mathbb{Z}\\Phi(L)$ for a lattice that is not definite. On a definite lattice the build lists $\\Phi(L)$, and this block is an error."""

    roots: Annotated[tuple[IntegerVector, ...], Field(strict=False)] = Field(
        description=(
            "Roots of $L$ that generate $\\mathbb{Z}\\Phi(L)$: each row lists the coordinates of one root in the basis $e_1, \\dots, e_n$ of the record. "
            "`[]` when $L$ has no roots. The build checks that each row is a root. "
            "When the rows generate $L$, that proves $L = \\mathbb{Z}\\Phi(L)$. "
            "When they do not, the notes of the record prove that each root of $L$ is in the sublattice that the rows generate."
        )
    )
    summands: Annotated[tuple[Tag, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Tags of lattices $M_1, M_2, \\dots$ with $\\mathbb{Z}\\Phi(L) \\cong M_1 \\oplus M_2 \\oplus \\cdots$, an orthogonal sum. "
            "Stated together with `embedding`. A root lattice does not state it: $\\mathbb{Z}\\Phi(L)$ is $L$."
        ),
    )
    embedding: Annotated[tuple[IntegerVector, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Matrix of an isometric embedding $M_1 \\oplus M_2 \\oplus \\cdots \\to L$ with image $\\mathbb{Z}\\Phi(L)$: "
            "the rows list the coordinates of the images of the basis vectors of the records of $M_1, M_2, \\dots$, in that order. "
            "The build checks that the rows have the Gram tensor of the orthogonal sum, and that they generate the sublattice that `roots` generates."
        ),
    )


def _definiteness(n_plus: int, n_minus: int, n_zero: int) -> Definiteness:
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


def _root_determinant(component: str) -> int:
    """Determinant of the root lattice of an irreducible simply laced root system.

    Conway and Sloane, Sphere Packings, Lattices and Groups, 3rd ed., Chapter 4, sections 6 to 8.
    """
    family, index = component[0], int(component[1:])
    match family:
        case "A":
            return index + 1
        case "D":
            return 4
        case _:
            return {6: 3, 7: 2, 8: 1}[index]


def _squared_root_sublattice_index(roots: tuple[str, ...], rank: int, determinant: Fraction) -> Fraction | None:
    """$[L : \\mathbb{Z}\\Phi_{\\{2\\}}(L)]^2 = \\det(\\mathbb{Z}\\Phi_{\\{2\\}}(L)) / \\det(L)$, when $\\mathbb{Z}\\Phi_{\\{2\\}}(L)$ has the rank of $L$."""
    if sum(int(component[1:]) for component in roots) != rank:
        return None
    return Fraction(math.prod(_root_determinant(component) for component in roots)) / abs(determinant)


def _problem(kind: str, message: str, location: tuple[str, ...], context: dict[str, str | int] | None = None) -> InitErrorDetails:
    return InitErrorDetails(type=PydanticCustomError(kind, message, context), loc=location, input=None)


class Lattice(Record):
    tag: Tag = Field(description="Permanent identifier: four characters from 0-9 and A-Z. The file name is the tag.")
    name: str = Field(description="Name as plain text, for search.")
    latex: str = Field(description="Name as TeX, without math delimiters.")
    aliases: Annotated[tuple[str, ...], Field(strict=False)] = Field(default=(), description="Other names, as plain text.")
    rank: int = Field(ge=1, description="Rank of the underlying free module.")
    gram_tensor: Annotated[tuple[Annotated[tuple[Rational, ...], Field(strict=False)], ...], Field(strict=False)] = Field(
        description=(
            "Components of the Gram tensor, the symmetric (0,2)-tensor $b$, in a basis $e_1, \\dots, e_n$: "
            "row $i$ lists $b(e_i, e_1), \\dots, b(e_i, e_n)$. Values are integers or strings `p/q`."
        )
    )
    signature: Annotated[tuple[int, int], Field(strict=False)] = Field(
        description=(
            "`[n_plus, n_minus]`: the numbers of $v$ with $b(v, v) > 0$ and with $b(v, v) < 0$ in a $b$-orthogonal basis of $L \\otimes \\mathbb{Q}$. "
            "They do not depend on the basis (Sylvester's law of inertia)."
        )
    )
    determinant: Rational = Field(description="$\\det(b(e_i, e_j))$. It is the same for every basis of $L$.")
    definiteness: Definiteness = Field(
        description=(
            "`positive_definite` or `negative_definite` when $b(x, x)$ has one sign on nonzero $x$; `indefinite` when it takes both signs; "
            "`positive_semidefinite` or `negative_semidefinite` when it has one sign and the determinant is zero; `zero` when $b = 0$."
        )
    )
    families: Annotated[tuple[Family, ...], Field(strict=False)] = Field(default=(), description="Named families that contain the lattice.")
    related: Annotated[tuple[Related, ...], Field(strict=False)] = Field(default=(), description="Related lattices in the catalogue.")
    references: Annotated[tuple[Reference, ...], Field(strict=False)] = Field(default=(), description="Literature for the lattice.")
    provenance: Provenance = Field(description="Origin of the record.")
    integral: IntegralData | None = Field(default=None, description=IntegralData.__doc__)
    definite: DefiniteData | None = Field(default=None, description=DefiniteData.__doc__)
    indefinite: IndefiniteData | None = Field(default=None, description=IndefiniteData.__doc__)
    hyperbolic: HyperbolicData | None = Field(default=None, description=HyperbolicData.__doc__)
    root_span: RootSpan | None = Field(default=None, description=RootSpan.__doc__)

    @property
    def nullity(self) -> int:
        return self.rank - self.signature[0] - self.signature[1]

    @property
    def is_nondegenerate(self) -> bool:
        return self.nullity == 0

    @property
    def is_definite(self) -> bool:
        return self.definiteness in ("positive_definite", "negative_definite")

    @property
    def is_unimodular(self) -> bool:
        return self.integral is not None and abs(self.determinant) == 1

    @property
    def is_hyperbolic(self) -> bool:
        return self.is_nondegenerate and self.rank >= 2 and min(self.signature) == 1

    @property
    def norm_two_span_rank(self) -> int | None:
        """The rank of $\\mathbb{Z}\\Phi_{\\{2\\}}(L)$, when the record states `root_system`."""
        if self.definite is None or self.definite.root_system is None:
            return None
        return sum(int(component[1:]) for component in self.definite.root_system)

    @property
    def norm_two_span_index(self) -> int | None:
        """$[L : \\mathbb{Z}\\Phi_{\\{2\\}}(L)]$, when the record states `root_system` and $\\mathbb{Z}\\Phi_{\\{2\\}}(L)$ has the rank of $L$."""
        if self.definite is None or self.definite.root_system is None:
            return None
        squared = _squared_root_sublattice_index(self.definite.root_system, self.rank, self.determinant)
        return None if squared is None else math.isqrt(squared.numerator)

    @cached_property
    def positive_roots(self) -> dict[Vector, Fraction]:
        """One of $r$, $-r$ for each root $r$ of a definite lattice, with $b(r, r)$."""
        assert self.is_definite, "the build lists the roots of a lattice only for a definite form"
        return arithmetic.definite_roots(self.gram_tensor)

    @cached_property
    def spanning_roots(self) -> dict[Vector, Fraction] | None:
        """Roots that generate $\\mathbb{Z}\\Phi(L)$, each with $b(r, r)$. `None` when the record does not decide $\\mathbb{Z}\\Phi(L)$.

        On a definite lattice they are all the roots. On another lattice they are the rows of `root_span.roots`.
        """
        if self.is_definite:
            return self.positive_roots
        if self.root_span is None:
            return None
        return {r: arithmetic.pairing(self.gram_tensor, r, r) for r in self.root_span.roots}

    @cached_property
    def root_span_factors(self) -> tuple[int, ...] | None:
        """The invariant factors $d_1 \\mid d_2 \\mid \\dots$ of $\\mathbb{Z}\\Phi(L)$ in $L$; `None` when $\\mathbb{Z}\\Phi(L)$ is not decided.

        Their number is the rank of $\\mathbb{Z}\\Phi(L)$. With $M'$ the primitive sublattice
        $L \\cap (\\mathbb{Z}\\Phi(L) \\otimes \\mathbb{Q})$, $M' / \\mathbb{Z}\\Phi(L) \\cong \\mathbb{Z}/d_1 \\oplus \\mathbb{Z}/d_2 \\oplus \\cdots$.
        """
        roots = self.spanning_roots
        return None if roots is None else arithmetic.invariant_factors(list(roots), self.rank)

    @property
    def root_span_rank(self) -> int | None:
        """The rank of $\\mathbb{Z}\\Phi(L)$."""
        factors = self.root_span_factors
        return None if factors is None else len(factors)

    @property
    def root_span_index(self) -> int | None:
        """$[M' : \\mathbb{Z}\\Phi(L)]$ for the primitive sublattice $M' = L \\cap (\\mathbb{Z}\\Phi(L) \\otimes \\mathbb{Q})$.

        It is $[L : \\mathbb{Z}\\Phi(L)]$ when the ranks agree.
        """
        factors = self.root_span_factors
        return None if factors is None else math.prod(factors)

    @property
    def root_span_is_primitive(self) -> bool | None:
        """Whether $\\mathbb{Z}\\Phi(L)$ is primitive in $L$: whether $P(L)$ has a maximum, which is then $R(L) = \\mathbb{Z}\\Phi(L)$."""
        index = self.root_span_index
        return None if index is None else index == 1

    @property
    def is_root_lattice(self) -> bool | None:
        """Whether $L = \\mathbb{Z}\\Phi(L)$; `None` when $\\mathbb{Z}\\Phi(L)$ is not decided."""
        factors = self.root_span_factors
        return None if factors is None else factors == (1,) * self.rank

    @cached_property
    def root_norms(self) -> tuple[Fraction, ...] | None:
        """A set $S$ with $L = \\mathbb{Z}\\Phi_S(L)$, for a root lattice; `None` for another lattice.

        $S$ has the fewest elements among the sets of values $b(r, r)$ of the roots of `spanning_roots`, and then the least absolute values.
        """
        roots = self.spanning_roots
        if roots is None or not self.is_root_lattice:
            return None
        return arithmetic.generating_norms(roots, self.rank)

    @model_validator(mode="after")
    def _well_defined(self) -> Self:
        problems = list(self._shape_problems())
        if not problems:
            problems = [
                *self._invariant_problems(),
                *self._integral_problems(),
                *self._definite_problems(),
                *self._indefinite_problems(),
                *self._hyperbolic_problems(),
            ]
        if not problems:
            problems = [*self._root_system_problems(), *self._root_span_problems()]
        if problems:
            raise ValidationError.from_exception_data(type(self).__name__, problems)
        return self

    def _shape_problems(self) -> Iterator[InitErrorDetails]:
        if len(self.gram_tensor) != self.rank or any(len(row) != self.rank for row in self.gram_tensor):
            yield _problem(
                "gram_tensor_shape",
                "a (0,2)-tensor on a module of rank {rank} has {rank} rows of {rank} components",
                ("gram_tensor",),
                {"rank": self.rank},
            )
            return
        if any(self.gram_tensor[i][j] != self.gram_tensor[j][i] for i in range(self.rank) for j in range(i)):
            yield _problem("gram_tensor_not_symmetric", "b(e_i, e_j) differs from b(e_j, e_i) for some i, j", ("gram_tensor",))

    def _invariant_problems(self) -> Iterator[InitErrorDetails]:
        determinant = arithmetic.determinant(self.gram_tensor)
        if self.determinant != determinant:
            yield _problem(
                "determinant_mismatch",
                "the Gram tensor has determinant {computed}, the record states {stated}",
                ("determinant",),
                {"computed": str(determinant), "stated": str(self.determinant)},
            )
        n_plus, n_minus, n_zero = arithmetic.inertia(self.gram_tensor)
        if self.signature != (n_plus, n_minus):
            yield _problem(
                "signature_mismatch",
                "the Gram tensor has signature ({n_plus}, {n_minus}), the record states ({stated_plus}, {stated_minus})",
                ("signature",),
                {"n_plus": n_plus, "n_minus": n_minus, "stated_plus": self.signature[0], "stated_minus": self.signature[1]},
            )
        definiteness = _definiteness(n_plus, n_minus, n_zero)
        if self.definiteness != definiteness:
            yield _problem(
                "definiteness_mismatch",
                "a form of signature ({n_plus}, {n_minus}) and nullity {n_zero} is {computed}, the record states {stated}",
                ("definiteness",),
                {"n_plus": n_plus, "n_minus": n_minus, "n_zero": n_zero, "computed": definiteness, "stated": self.definiteness},
            )

    def _integral_problems(self) -> Iterator[InitErrorDetails]:
        integer_valued = arithmetic.is_integer_valued(self.gram_tensor)
        if self.integral is None:
            if integer_valued:
                yield _problem("integral_block_missing", "every b(e_i, e_j) is an integer, so the `integral` block is required", ("integral",))
            return
        if not integer_valued:
            yield _problem("integral_requires_integer_values", "the `integral` block requires every b(e_i, e_j) to be an integer", ("integral",))
            return
        # b(x, x) = sum_i x_i^2 b(e_i, e_i) + 2 sum_{i<j} x_i x_j b(e_i, e_j), so b(x, x) is even for all x when each b(e_i, e_i) is.
        parity = "even" if all(self.gram_tensor[i][i] % 2 == 0 for i in range(self.rank)) else "odd"
        if self.integral.parity != parity:
            yield _problem(
                "parity_mismatch",
                "the lattice is {computed}, the record states {stated}",
                ("integral", "parity"),
                {"computed": parity, "stated": self.integral.parity},
            )
        nondegenerate = arithmetic.determinant(self.gram_tensor) != 0
        stated_group = self.integral.discriminant_group
        location = ("integral", "discriminant_group")
        if not nondegenerate:
            if stated_group is not None:
                yield _problem("discriminant_group_requires_nondegenerate", "the discriminant group is finite only when the determinant is not zero", location)
            if self.integral.genus_symbol is not None:
                yield _problem("genus_requires_nondegenerate", "the genus symbol requires a nonzero determinant", ("integral", "genus_symbol"))
            return
        if stated_group is None:
            yield _problem("discriminant_group_missing", "the determinant is not zero, so `discriminant_group` is required", location)
            return
        group = arithmetic.discriminant_invariants(self.gram_tensor)
        if stated_group != group:
            yield _problem(
                "discriminant_group_mismatch",
                "the discriminant group has invariant factors {computed}, the record states {stated}",
                location,
                {"computed": str(list(group)), "stated": str(list(stated_group))},
            )

    def _definite_problems(self) -> Iterator[InitErrorDetails]:
        if self.definite is None:
            return
        n_plus, n_minus, n_zero = arithmetic.inertia(self.gram_tensor)
        if n_zero > 0 or (n_plus > 0 and n_minus > 0):
            yield _problem("definite_requires_definite", "the `definite` block requires a positive definite or negative definite form", ("definite",))
            return
        data = self.definite
        rank = self.rank
        integer_valued = arithmetic.is_integer_valued(self.gram_tensor)
        even = integer_valued and all(self.gram_tensor[i][i] % 2 == 0 for i in range(rank))
        diagonal = [abs(self.gram_tensor[i][i]) for i in range(rank)]
        minimum = data.minimum
        if minimum <= 0:
            yield _problem("minimum_not_positive", "the minimum of a definite form is positive", ("definite", "minimum"))
            return
        if minimum > min(diagonal):
            yield _problem(
                "minimum_exceeds_diagonal",
                "a basis vector has |b(e, e)| = {least}, less than the stated minimum {stated}",
                ("definite", "minimum"),
                {"least": str(min(diagonal)), "stated": str(minimum)},
            )
        # Hermite's inequality: min^n <= (4/3)^(n(n-1)/2) * |det| for a definite form of rank n.
        exponent = rank * (rank - 1) // 2
        if minimum**rank * 3**exponent > 4**exponent * abs(arithmetic.determinant(self.gram_tensor)):
            yield _problem(
                "minimum_violates_hermite",
                "the stated minimum {stated} exceeds Hermite's bound for this rank and determinant",
                ("definite", "minimum"),
                {"stated": str(minimum)},
            )
        if integer_valued and minimum.denominator != 1:
            yield _problem("minimum_not_integer", "an integer-valued form has an integer minimum", ("definite", "minimum"))
        if even and minimum.denominator == 1 and minimum % 2 == 1:
            yield _problem("minimum_not_even", "an even lattice has an even minimum", ("definite", "minimum"))

        kissing = data.kissing_number
        if kissing is not None:
            if kissing <= 0 or kissing % 2 == 1:
                message = "minimal vectors come in pairs x, -x, so their number is even and positive"
                yield _problem("kissing_number_odd", message, ("definite", "kissing_number"))
            # Minimal vectors x, y with x != y, x != -y are distinct modulo 2L and none is in 2L:
            # otherwise (x + y)/2 or (x - y)/2, or x/2, is a shorter nonzero vector.
            if kissing > 2 * (2**rank - 1):
                yield _problem(
                    "kissing_number_exceeds_bound",
                    "a lattice of rank {rank} has at most {bound} minimal vectors",
                    ("definite", "kissing_number"),
                    {"rank": rank, "bound": 2 * (2**rank - 1)},
                )
            minimal_basis_vectors = sum(1 for entry in diagonal if entry == minimum)
            if kissing < 2 * minimal_basis_vectors:
                yield _problem(
                    "kissing_number_below_basis_count",
                    "{count} basis vectors attain the stated minimum, so there are at least {bound} minimal vectors",
                    ("definite", "kissing_number"),
                    {"count": minimal_basis_vectors, "bound": 2 * minimal_basis_vectors},
                )

        order = data.automorphism_group_order
        if order is not None and (order <= 0 or order % 2 == 1):
            yield _problem("automorphism_order_odd", "x -> -x is an isometry of order 2, so the order is even", ("definite", "automorphism_group_order"))

        theta = data.theta_series
        if theta is not None:
            location = ("definite", "theta_series")
            if not integer_valued:
                yield _problem("theta_requires_integral", "`theta_series` is indexed by integer values of b(x, x), so it requires an integer-valued form", location)
            else:
                if not theta or theta[0] != 1:
                    yield _problem("theta_constant_term", "only x = 0 has b(x, x) = 0, so the first entry is 1", location)
                if any(entry < 0 or entry % 2 == 1 for entry in theta[1:]):
                    yield _problem("theta_odd_coefficient", "nonzero vectors come in pairs x, -x, so each later entry is even and not negative", location)
                if any(entry != 0 for index, entry in enumerate(theta) if 0 < index < minimum):
                    yield _problem("theta_below_minimum", "there is no nonzero x with |b(x, x)| less than the minimum", location)
                if minimum.denominator == 1 and len(theta) > minimum and kissing is not None and theta[int(minimum)] != kissing:
                    yield _problem("theta_kissing_mismatch", "the entry at the minimum is the kissing number", location)
                if even and any(entry != 0 for entry in theta[1::2]):
                    yield _problem("theta_odd_norm_in_even_lattice", "an even lattice has no x with b(x, x) odd", location)

        roots = data.root_system
        if roots is not None:
            location = ("definite", "root_system")
            if not integer_valued:
                yield _problem("root_system_requires_integral", "`root_system` requires an integer-valued form", location)
                return
            if sum(int(component[1:]) for component in roots) > rank:
                yield _problem("root_system_rank", "the rank of the root system exceeds the rank of the lattice", location)
            count = sum(root_systems.root_count(component) for component in roots)
            if theta is not None and len(theta) > 2 and theta[2] != count:
                yield _problem(
                    "root_system_theta_mismatch",
                    "the root system has {count} roots, the theta series has {stated} vectors with |b(x, x)| = 2",
                    location,
                    {"count": count, "stated": theta[2]},
                )
            if minimum == 2 and kissing is not None and kissing != count:
                yield _problem(
                    "root_system_kissing_mismatch",
                    "the minimum is 2, so the {count} roots are the minimal vectors, but the kissing number is {stated}",
                    location,
                    {"count": count, "stated": kissing},
                )
            squared_index = _squared_root_sublattice_index(roots, rank, arithmetic.determinant(self.gram_tensor))
            if squared_index is not None and (squared_index.denominator != 1 or math.isqrt(squared_index.numerator) ** 2 != squared_index.numerator):
                yield _problem(
                    "root_system_index",
                    "the roots generate a sublattice of the rank of L, so its determinant is det(L) times the square of its index, but the quotient is {quotient}",
                    location,
                    {"quotient": str(squared_index)},
                )
            if minimum > 2 and roots:
                yield _problem("root_system_nonempty_above_norm_two", "the minimum is greater than 2, so there are no roots", location)

    def _indefinite_problems(self) -> Iterator[InitErrorDetails]:
        if self.indefinite is None:
            return
        n_plus, n_minus, n_zero = arithmetic.inertia(self.gram_tensor)
        if n_plus == 0 or n_minus == 0:
            yield _problem("indefinite_requires_indefinite", "the `indefinite` block requires a form that takes both signs", ("indefinite",))
            return
        location = ("indefinite", "isotropic")
        determinant = arithmetic.determinant(self.gram_tensor)
        witness = None
        if n_zero > 0:
            witness = "the radical of a degenerate form contains a nonzero x with b(x, x) = 0"
        elif any(self.gram_tensor[i][i] == 0 for i in range(self.rank)):
            witness = "a basis vector has b(e, e) = 0"
        elif self.rank >= 5:
            witness = "an indefinite rational form of rank at least 5 is isotropic (Meyer's theorem)"
        elif self.rank == 2 and arithmetic.is_rational_square(-determinant):
            witness = "a nondegenerate binary form is isotropic when minus its determinant is a square"
        if witness is not None and not self.indefinite.isotropic:
            yield _problem("isotropy_mismatch", "the record states anisotropic, but {reason}", location, {"reason": witness})
        if witness is None and self.rank == 2 and self.indefinite.isotropic:
            yield _problem("isotropy_mismatch", "a nondegenerate binary form is isotropic only when minus its determinant is a square", location)

    def _hyperbolic_problems(self) -> Iterator[InitErrorDetails]:
        if self.hyperbolic is None:
            return
        n_plus, n_minus, n_zero = arithmetic.inertia(self.gram_tensor)
        if n_zero > 0 or self.rank < 2 or min(n_plus, n_minus) != 1:
            message = "the `hyperbolic` block requires a nondegenerate form of signature (1, n) or (n, 1) with n >= 1"
            yield _problem("hyperbolic_requires_hyperbolic", message, ("hyperbolic",))

    def _root_system_problems(self) -> Iterator[InitErrorDetails]:
        """Whether `definite.roots` is $\\Phi(L)$, and whether `definite.root_system` has the number of roots $r$ with $|b(r, r)| = 2$.

        Let the declared simple roots $\\alpha_i$ of a component be roots of $L$ with
        $b(\\alpha_i, \\alpha_j) = k (\\alpha_i, \\alpha_j)$ for the symmetrized Cartan matrix of the
        declared type. Each $s_{\\alpha_i}$ is in $O(L)$, and $O(L)$ maps $\\Phi(L)$ to itself,
        so the orbit of the $\\alpha_i$ under the group $W$ that the $s_{\\alpha_i}$ generate is in
        $\\Phi(L)$. The form is definite, so that orbit is a root system with base $\\alpha_i$: it
        has the declared type, and `root_count(type)` elements. The orbits of orthogonal
        components are disjoint. The union is therefore $\\Phi(L)$ exactly when the sum of
        the `root_count(type)` is the number of roots of $L$.
        """
        if self.definite is None:
            return
        components = self.definite.roots
        if components is not None:
            location = ("definite", "roots")
            shapes = (len(component.simple_roots) == int(component.type[1:]) and all(len(row) == self.rank for row in component.simple_roots) for component in components)
            if not all(shapes):
                yield _problem("roots_shape", "a component of rank m has m simple roots, each with {rank} coordinates", location, {"rank": self.rank})
                return
            for component in components:
                for row in component.simple_roots:
                    if not arithmetic.is_root(self.gram_tensor, row):
                        yield _problem("simple_root_not_root", "{vector} is not a root of L", location, {"vector": str(list(row))})
                expected = root_systems.simple_root_gram(component.type)
                pairs = ((i, j) for i in range(len(expected)) for j in range(len(expected)))
                if any(arithmetic.pairing(self.gram_tensor, component.simple_roots[i], component.simple_roots[j]) != component.scale * expected[i][j] for i, j in pairs):
                    yield _problem(
                        "simple_roots_gram_mismatch",
                        "the simple roots of a component do not have the Gram matrix of type {type} with scale {scale}",
                        location,
                        {"type": component.type, "scale": str(component.scale)},
                    )
            for first, second in combinations(components, 2):
                if any(arithmetic.pairing(self.gram_tensor, r, s) != 0 for r in first.simple_roots for s in second.simple_roots):
                    yield _problem("root_components_not_orthogonal", "two components are not orthogonal", location)
            declared = sum(root_systems.root_count(component.type) for component in components)
            if declared != 2 * len(self.positive_roots):
                yield _problem(
                    "root_count_mismatch",
                    "the declared components have {declared} roots, the lattice has {listed}",
                    location,
                    {"declared": declared, "listed": 2 * len(self.positive_roots)},
                )
        if self.definite.root_system is not None:
            declared = sum(root_systems.root_count(component) for component in self.definite.root_system)
            listed = 2 * sum(1 for norm in self.positive_roots.values() if abs(norm) == 2)
            if declared != listed:
                yield _problem(
                    "root_system_count_mismatch",
                    "the declared root system has {declared} roots, the lattice has {listed} elements r with |b(r, r)| = 2",
                    ("definite", "root_system"),
                    {"declared": declared, "listed": listed},
                )

    def _root_span_problems(self) -> Iterator[InitErrorDetails]:
        span = self.root_span
        if span is None:
            return
        location = ("root_span",)
        if self.is_definite:
            yield _problem("root_span_on_definite", "the build lists the roots of a definite lattice, so the `root_span` block is an error there", location)
            return
        if any(len(row) != self.rank for row in (*span.roots, *(span.embedding or ()))):
            yield _problem("root_span_shape", "each row lists {rank} coordinates", location, {"rank": self.rank})
            return
        for row in span.roots:
            if not arithmetic.is_root(self.gram_tensor, row):
                yield _problem("root_span_not_root", "{vector} is not a root of L", ("root_span", "roots"), {"vector": str(list(row))})
        if (span.summands is None) != (span.embedding is None):
            yield _problem("root_span_representative_incomplete", "`summands` and `embedding` are stated together", location)
            return
        if span.embedding is not None:
            basis = arithmetic.span_basis(list(span.embedding))
            if len(basis) != len(span.embedding) or basis != arithmetic.span_basis(list(span.roots)):
                message = "the rows of `embedding` are not a basis of the sublattice that the rows of `roots` generate"
                yield _problem("root_span_embedding_mismatch", message, ("root_span", "embedding"))
