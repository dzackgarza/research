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
            "Computed by `latticedb certify` with `Genus(G).representatives()` of SageMath; for an indefinite binary form, the representatives counted up to equivalence. "
            "Requires a nonzero determinant; absent when it is not computed."
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
    automorphism_group_order: int | None = Field(default=None, description="Order of $O(L)$, computed by `latticedb certify` with `qfauto` of PARI/GP.")
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
    def is_two_elementary_even(self) -> bool:
        """Whether $L$ is even and nondegenerate with $2 A_L = 0$: the lattices with Nikulin's invariants $(r, a, \\delta)$."""
        integral = self.integral
        if integral is None or integral.parity != "even" or integral.discriminant_group is None:
            return False
        return all(factor == 2 for factor in integral.discriminant_group)

    @property
    def is_hyperbolic(self) -> bool:
        return self.is_nondegenerate and self.rank >= 2 and min(self.signature) == 1

    @property
    def is_integer_valued(self) -> bool:
        return all(entry.denominator == 1 for row in self.gram_tensor for entry in row)

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

    @model_validator(mode="after")
    def _well_defined(self) -> Self:
        """The fields have the shapes of the schema, and each block is present exactly when the stored fields state its hypothesis."""
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
            if self.is_integer_valued:
                yield _problem("integral_block_missing", "every b(e_i, e_j) is an integer, so the `integral` block is required", ("integral",))
            return
        if not self.is_integer_valued:
            yield _problem("integral_requires_integer_values", "the `integral` block requires every b(e_i, e_j) to be an integer", ("integral",))
            return
        if self.determinant == 0:
            if self.integral.discriminant_group is not None:
                message = "the discriminant group is finite only when the determinant is not zero"
                yield _problem("discriminant_group_requires_nondegenerate", message, ("integral", "discriminant_group"))
            if self.integral.genus_symbol is not None:
                yield _problem("genus_requires_nondegenerate", "the genus symbol requires a nonzero determinant", ("integral", "genus_symbol"))
            if self.integral.genus_class_count is not None:
                message = "the class number of the genus requires a nonzero determinant"
                yield _problem("genus_class_count_requires_nondegenerate", message, ("integral", "genus_class_count"))
            if self.integral.overlattice_count is not None:
                message = "the number of overlattices is finite only when the determinant is not zero"
                yield _problem("overlattice_count_requires_nondegenerate", message, ("integral", "overlattice_count"))
        elif self.integral.discriminant_group is None:
            yield _problem("discriminant_group_missing", "the determinant is not zero, so `discriminant_group` is required", ("integral", "discriminant_group"))
        defined = self.is_two_elementary_even
        if defined and self.integral.delta is None:
            yield _problem("delta_missing", "the lattice is even with 2 A_L = 0, so `delta` is required", ("integral", "delta"))
        if not defined and self.integral.delta is not None:
            yield _problem("delta_requires_two_elementary_even", "`delta` requires an even lattice with 2 A_L = 0 and a nonzero determinant", ("integral", "delta"))

    def _definite_problems(self) -> Iterator[InitErrorDetails]:
        if self.definite is None:
            if self.is_definite:
                yield _problem("definite_block_missing", "the form is definite, so the `definite` block is required", ("definite",))
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

    def _indefinite_problems(self) -> Iterator[InitErrorDetails]:
        indefinite = self.definiteness == "indefinite"
        if self.indefinite is None and indefinite:
            yield _problem("indefinite_block_missing", "b(x, x) takes both signs, so the `indefinite` block is required", ("indefinite",))
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
        decided = self.is_definite or span is not None
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
    """A morphism $\\varphi \\colon S(c) \\to T$ of lattices: a $\\mathbb{Z}$-linear map with $b_T(\\varphi x, \\varphi y) = c \\, b_S(x, y)$ for a nonzero integer $c$, 1 by default.

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
