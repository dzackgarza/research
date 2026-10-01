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

from latticedb import arithmetic, root_systems, roots
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


def _problem(kind: str, message: str, location: tuple[str, ...], context: dict[str, str | int] | None = None) -> InitErrorDetails:
    return InitErrorDetails(type=PydanticCustomError(kind, message, context), loc=location, input=None)


class Record(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)


class Related(Record):
    tag: Tag = Field(description="Tag of another lattice in the catalogue.")
    relation: str = Field(description="How that lattice is related to this one, as a short phrase.")


class Summand(Record):
    """A lattice $M(k)$: a record $M$ of the catalogue with its form scaled by a nonzero integer $k$.

    The catalogue records no twist $M(k)$ with $|k| \\geq 2$, and no $M(-1)$ outside its sign convention,
    so a summand of a root sublattice such as $A_1 = \\langle 1 \\rangle(2)$ names the record and the scale.
    """

    tag: Tag = Field(description="Tag of the lattice $M$ in the catalogue.")
    scale: int = Field(description="The nonzero integer $k$: the summand is $M$ with the form $k b_M$.")

    @model_validator(mode="after")
    def _nonzero_scale(self) -> Self:
        if self.scale == 0:
            raise ValidationError.from_exception_data(type(self).__name__, [_problem("summand_scale_zero", "M(0) has the zero form and is not a summand of a root sublattice", ("scale",))])
        return self


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

    minimum: Rational = Field(description="Least value of $b(x, x)$ over nonzero $x$. The build computes it and rejects another value.")
    kissing_number: int = Field(
        description="Number of $x$ with $b(x, x)$ equal to the minimum. The number is finite because the form is definite. The build computes it and rejects another value."
    )
    automorphism_group_order: int | None = Field(
        default=None, description="Order of the group of isometries of the lattice. Declared: the build checks only that it is even, and the prose gives its source."
    )
    theta_series: Annotated[tuple[int, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Entry $k$ is the number of $x$ with $b(x, x) = k$, for $k = 0, 1, 2, \\dots$ Required for, and only for, integer values. "
            "The build computes every entry and rejects another value; `latticedb new` writes the entries past the minimum, further for small ranks."
        ),
    )
    root_system: Annotated[tuple[AdeType, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "ADE type of $\\Phi_{\\{2\\}}(L) = \\{r \\in L : b(r, r) = 2\\}$, as irreducible components in any order: `[E8]`, `[A1, A1]`, or `[]` when it is empty. "
            "$\\mathbb{Z}\\Phi_{\\{2\\}}(L)$ is the orthogonal sum of the root lattices of the components (Witt's theorem); it is not primitive in $L$ in general. "
            "The field `roots` states all of $\\Phi(L)$. Required for, and only for, integer values. The build computes it and rejects another value."
        ),
    )
    roots: Annotated[tuple[RootSystemComponent, ...], Field(strict=False)] = Field(
        description=(
            "The root system $\\Phi(L)$ as its irreducible components, each with a base; `[]` when $L$ has no roots. "
            "The build lists the roots of $L$, and it rejects a declaration that is not $\\Phi(L)$. `latticedb new` writes the field."
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
    summands: Annotated[tuple[Summand, ...], Field(strict=False)] | None = Field(
        default=None,
        description=(
            "Lattices $M_1(k_1), M_2(k_2), \\dots$, each a record with a scale, with $\\mathbb{Z}\\Phi(L) \\cong M_1(k_1) \\oplus M_2(k_2) \\oplus \\cdots$, an orthogonal sum. "
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
        """Whether the root sublattice $R(L) = \\mathbb{Z}\\Phi(L)$ is primitive in $L$; `None` when $\\mathbb{Z}\\Phi(L)$ is not decided."""
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
                *self._twist_problems(),
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

    def _twist_problems(self) -> Iterator[InitErrorDetails]:
        """The corpus records one lattice of each class under scaling $L \\mapsto L(n)$, $n$ a nonzero integer.

        $L$ is admitted when it is not $M(n)$ for a lattice $M$ and an integer $n$ with $|n| \\geq 2$,
        that is, when the scale of $b$ has numerator 1, and when its sign is the conventional one:
        $b$ is positive when it takes one sign, and $n_+ \\leq n_-$ when it takes both.
        The zero form is $M(0)$ for every $M$ and is not admitted.
        """
        scale = arithmetic.scale(self.gram_tensor)
        if scale == 0:
            yield _problem("twisted", "b = 0 is M(0) for every lattice M of rank {rank}; the corpus records no zero form", ("gram_tensor",), {"rank": self.rank})
            return
        if scale.numerator != 1:
            yield _problem(
                "twisted",
                "the lattice is M({n}) for the lattice M with Gram tensor b/{n}; the corpus records M and not its twist",
                ("gram_tensor",),
                {"n": scale.numerator},
            )
        n_plus, n_minus, _ = arithmetic.inertia(self.gram_tensor)
        if (n_plus == 0 and n_minus > 0) or (n_plus > n_minus > 0):
            yield _problem(
                "twisted",
                "the lattice is M(-1) for the lattice M with Gram tensor -b and signature ({n_minus}, {n_plus}); the corpus records M: positive when b has one sign, n_plus <= n_minus when it has both",
                ("gram_tensor",),
                {"n_plus": n_plus, "n_minus": n_minus},
            )

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
        computed = definiteness(n_plus, n_minus, n_zero)
        if self.definiteness != computed:
            yield _problem(
                "definiteness_mismatch",
                "a form of signature ({n_plus}, {n_minus}) and nullity {n_zero} is {computed}, the record states {stated}",
                ("definiteness",),
                {"n_plus": n_plus, "n_minus": n_minus, "n_zero": n_zero, "computed": computed, "stated": self.definiteness},
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
        """The `definite` block is required exactly on a definite form, and its computed fields are compared with the Gram tensor."""
        n_plus, n_minus, n_zero = arithmetic.inertia(self.gram_tensor)
        definite = n_zero == 0 and (n_plus == 0 or n_minus == 0)
        if self.definite is None:
            if definite:
                yield _problem("definite_block_missing", "the form is definite, so the `definite` block is required", ("definite",))
            return
        if not definite:
            yield _problem("definite_requires_definite", "the `definite` block requires a positive definite or negative definite form", ("definite",))
            return
        data = self.definite
        integer_valued = arithmetic.is_integer_valued(self.gram_tensor)
        minimum, kissing = arithmetic.minimum_and_kissing_number(self.gram_tensor)
        if data.minimum != minimum:
            yield _problem(
                "minimum_mismatch",
                "the least |b(x, x)| over nonzero x is {computed}, the record states {stated}",
                ("definite", "minimum"),
                {"computed": str(minimum), "stated": str(data.minimum)},
            )
        if data.kissing_number != kissing:
            yield _problem(
                "kissing_number_mismatch",
                "{computed} vectors attain the minimum, the record states {stated}",
                ("definite", "kissing_number"),
                {"computed": kissing, "stated": data.kissing_number},
            )

        order = data.automorphism_group_order
        if order is not None and (order <= 0 or order % 2 == 1):
            yield _problem("automorphism_order_odd", "x -> -x is an isometry of order 2, so the order is even", ("definite", "automorphism_group_order"))

        theta = data.theta_series
        location = ("definite", "theta_series")
        if not integer_valued:
            if theta is not None:
                yield _problem("theta_requires_integral", "`theta_series` is indexed by integer values of b(x, x), so it requires an integer-valued form", location)
        elif theta is None:
            yield _problem("theta_series_missing", "every b(e_i, e_j) is an integer, so `theta_series` is required", location)
        elif len(theta) <= theta_bound(self.rank, minimum):
            yield _problem(
                "theta_series_short",
                "the theta series of a lattice of rank {rank} and minimum {minimum} states the counts through norm {bound}",
                location,
                {"rank": self.rank, "minimum": str(minimum), "bound": theta_bound(self.rank, minimum)},
            )
        else:
            computed = arithmetic.theta_coefficients(self.gram_tensor, len(theta) - 1)
            if theta != computed:
                yield _problem(
                    "theta_series_mismatch",
                    "the counts of x with |b(x, x)| = 0, 1, 2, ... are {computed}, the record states {stated}",
                    location,
                    {"computed": str(list(computed)), "stated": str(list(theta))},
                )

        root_system = data.root_system
        location = ("definite", "root_system")
        if not integer_valued:
            if root_system is not None:
                yield _problem("root_system_requires_integral", "`root_system` requires an integer-valued form", location)
        elif root_system is None:
            yield _problem("root_system_missing", "every b(e_i, e_j) is an integer, so `root_system` is required", location)
        else:
            computed = roots.norm_two_types(self.gram_tensor, arithmetic.definite_roots(self.gram_tensor))
            if sorted(root_system) != sorted(computed):
                yield _problem(
                    "root_system_mismatch",
                    "the r in L with |b(r, r)| = 2 form a root system of type {computed}, the record states {stated}",
                    location,
                    {"computed": " ".join(computed) or "[]", "stated": " ".join(root_system) or "[]"},
                )

    def _indefinite_problems(self) -> Iterator[InitErrorDetails]:
        """The `indefinite` block is required exactly on a form that takes both signs, and `isotropic` is compared with the Gram tensor."""
        n_plus, n_minus, n_zero = arithmetic.inertia(self.gram_tensor)
        indefinite = n_plus > 0 and n_minus > 0
        if self.indefinite is None:
            if indefinite:
                yield _problem("indefinite_block_missing", "b(x, x) takes both signs, so the `indefinite` block is required", ("indefinite",))
            return
        if not indefinite:
            yield _problem("indefinite_requires_indefinite", "the `indefinite` block requires a form that takes both signs", ("indefinite",))
            return
        # The radical of a degenerate form is nonzero and isotropic; `qfsolve` decides a nondegenerate rational form.
        isotropic = n_zero > 0 or arithmetic.is_isotropic(self.gram_tensor)
        if self.indefinite.isotropic != isotropic:
            yield _problem(
                "isotropy_mismatch",
                "the form is {computed}, the record states {stated}",
                ("indefinite", "isotropic"),
                {"computed": "isotropic" if isotropic else "anisotropic", "stated": "isotropic" if self.indefinite.isotropic else "anisotropic"},
            )

    def _hyperbolic_problems(self) -> Iterator[InitErrorDetails]:
        if self.hyperbolic is None:
            return
        n_plus, n_minus, n_zero = arithmetic.inertia(self.gram_tensor)
        if n_zero > 0 or self.rank < 2 or min(n_plus, n_minus) != 1:
            message = "the `hyperbolic` block requires a nondegenerate form of signature (1, n) or (n, 1) with n >= 1"
            yield _problem("hyperbolic_requires_hyperbolic", message, ("hyperbolic",))

    def _root_system_problems(self) -> Iterator[InitErrorDetails]:
        """Whether `definite.roots` is $\\Phi(L)$.

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
