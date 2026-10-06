"""Typed records for lattice groups, genera, polytopes, and geometric constructions.

The records name mathematical objects and their defining data. Matrices and vectors
are coordinates in the bases named by their parent records. Source claims belong in
the Markdown prose with BibTeX citations.
"""

import ast
from typing import Annotated, Literal, Self

from flint import fmpz_mat
from pydantic import Field, model_validator
from pydantic_core import PydanticCustomError

from latticedb.model import Rational, Record, Slug, Tag


class CatalogueRecord(Record):
    slug: Slug


class LatticeGenus(CatalogueRecord):
    """A genus of integral quadratic lattices; member tags name isometry classes."""

    signature: Annotated[tuple[int, int], Field(strict=False)]
    determinant: int
    parity: Literal["even", "odd"]
    symbol: str = Field(min_length=1)
    representative_tags: list[Tag]
    class_number: Annotated[int, Field(gt=0)] | None = None
    representatives_complete: bool = False
    mass: Rational | None = None

    @model_validator(mode="after")
    def check_genus(self) -> Self:
        if self.determinant == 0 or len(set(self.representative_tags)) != len(
            self.representative_tags
        ):
            raise PydanticCustomError(
                "genus_members",
                "a genus has nonzero determinant and distinct representative tags",
            )
        if self.representatives_complete and self.class_number != len(
            self.representative_tags
        ):
            raise PydanticCustomError(
                "genus_complete", "a complete list has exactly its stated class number"
            )
        if self.mass is not None and self.mass <= 0:
            raise PydanticCustomError("genus_mass", "a genus mass is positive")
        return self


def _expression_value(node: ast.AST, parameter: str, value: int) -> int:
    """The value of a Gram-template entry: integer arithmetic in `parameter`."""
    match node:
        case ast.Expression():
            return _expression_value(node.body, parameter, value)
        case ast.Constant() if type(node.value) is int:
            return node.value
        case ast.Name() if node.id == parameter:
            return value
        case ast.BinOp() if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
            left = _expression_value(node.left, parameter, value)
            right = _expression_value(node.right, parameter, value)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            return left * right
        case ast.UnaryOp() if isinstance(node.op, (ast.USub, ast.UAdd)):
            operand = _expression_value(node.operand, parameter, value)
            return -operand if isinstance(node.op, ast.USub) else operand
    raise PydanticCustomError(
        "family_expression",
        "a Gram-template entry is an integer or integer arithmetic in the parameter",
    )


class LatticeFamily(CatalogueRecord):
    """An infinite parameterized family of lattices sharing one Gram template.

    The family holds the lattice with `gram_template` with `parameter`
    replaced by each integer `>= minimum`. Template entries are integers or
    integer arithmetic in the parameter.
    """

    name: str = Field(min_length=1)
    parameter: str = Field(min_length=1)
    minimum: int
    rank: Annotated[int, Field(gt=0)]
    signature: Annotated[tuple[int, int], Field(strict=False)]
    gram_template: Annotated[
        tuple[Annotated[tuple[int | str, ...], Field(strict=False)], ...],
        Field(strict=False),
    ]

    @model_validator(mode="after")
    def check_template(self) -> Self:
        if not self.parameter.isidentifier():
            raise PydanticCustomError(
                "family_parameter", "the parameter is an identifier"
            )
        rows = self.gram_template
        if len(rows) != self.rank or any(len(row) != self.rank for row in rows):
            raise PydanticCustomError(
                "family_shape", "the template has rank rows of rank components"
            )
        seen = False
        for row in rows:
            for entry in row:
                if isinstance(entry, str):
                    seen = True
                if isinstance(entry, bool):
                    raise PydanticCustomError(
                        "family_expression",
                        "a Gram-template entry is an integer or integer arithmetic in the parameter",
                    )
                if isinstance(entry, str):
                    try:
                        tree = ast.parse(entry, mode="eval")
                    except SyntaxError:
                        raise PydanticCustomError(
                            "family_expression",
                            "a Gram-template entry is an integer or integer arithmetic in the parameter",
                        ) from None
                    names = {
                        node.id
                        for node in ast.walk(tree)
                        if isinstance(node, ast.Name)
                    }
                    if names != {self.parameter}:
                        raise PydanticCustomError(
                            "family_parameter",
                            "each template expression names the parameter and nothing else",
                        )
        if not seen:
            raise PydanticCustomError(
                "family_parameter",
                "the parameter occurs in the template",
            )
        if any(
            rows[i][j] != rows[j][i]
            for i in range(self.rank)
            for j in range(self.rank)
        ):
            raise PydanticCustomError(
                "family_symmetric", "the template is a symmetric tensor"
            )
        # PARI starts once per process; only family records pay it.
        import cypari2

        pari = cypari2.Pari()
        for probe in (self.minimum, self.minimum + 1):
            matrix = [
                [
                    entry
                    if isinstance(entry, int)
                    else _expression_value(
                        ast.parse(entry, mode="eval"), self.parameter, probe
                    )
                    for entry in row
                ]
                for row in rows
            ]
            if int(fmpz_mat(matrix).det()) == 0:
                raise PydanticCustomError(
                    "family_degenerate",
                    "the template is nonsingular at its probe points",
                )
            signature = tuple(
                int(part)
                for part in pari.qfsign(
                    pari.matrix(
                        self.rank,
                        self.rank,
                        [entry for row in matrix for entry in row],
                    )
                )
            )
            if signature != tuple(self.signature):
                raise PydanticCustomError(
                    "family_signature",
                    "the stated signature is the signature at its probe points",
                )
        return self


class DualIsometry(CatalogueRecord):
    """An isometry L -> L*(k), with matrix in the basis dual to the record basis."""

    lattice: Tag
    scale: Annotated[int, Field(gt=0)]
    matrix: list[list[int]]


class LatticePolytope(CatalogueRecord):
    """A lattice polytope in a based free abelian group, separate from a quadratic lattice."""

    ambient_rank: Annotated[int, Field(gt=0)]
    vertices: list[list[int]] = Field(min_length=1)
    polar: Slug | None = None
    reflexive: bool | None = None
    lattice_point_count: Annotated[int, Field(gt=0)] | None = None
    source_identifier: str | None = None
    metric_lattice: Tag | None = None
    delaunay_center: list[Rational] | None = None
    delaunay_radius_squared: Rational | None = None

    @model_validator(mode="after")
    def check_vertices(self) -> Self:
        coordinates = [tuple(row) for row in self.vertices]
        if any(len(row) != self.ambient_rank for row in coordinates) or len(
            set(coordinates)
        ) != len(coordinates):
            raise PydanticCustomError(
                "polytope_vertices",
                "polytope vertices must be distinct points of the ambient lattice",
            )
        differences = [
            [point[i] - coordinates[0][i] for i in range(self.ambient_rank)]
            for point in coordinates[1:]
        ]
        if fmpz_mat(differences).rank() != self.ambient_rank:
            raise PydanticCustomError(
                "polytope_dimension",
                "the vertices must span a full-dimensional polytope",
            )
        if self.lattice_point_count is not None and self.lattice_point_count < len(
            self.vertices
        ):
            raise PydanticCustomError(
                "polytope_points", "a lattice-point count includes every vertex"
            )
        if (self.delaunay_center is None) != (self.delaunay_radius_squared is None) or (
            self.delaunay_center is not None and self.metric_lattice is None
        ):
            raise PydanticCustomError(
                "delaunay_datum",
                "a Delaunay sphere needs its metric lattice, center and squared radius",
            )
        if (
            self.delaunay_center is not None
            and len(self.delaunay_center) != self.ambient_rank
        ):
            raise PydanticCustomError(
                "delaunay_center",
                "a Delaunay center has one coordinate per ambient dimension",
            )
        return self


class ToricVariety(CatalogueRecord):
    """The toric variety of the normal fan of a lattice polytope."""

    name: str = Field(min_length=1)
    polytope: Slug
    fan: Literal["normal_fan"] = "normal_fan"
    subdivision_rays: list[list[int]] | None = None


class GeometricReference(Record):
    kind: Literal["object", "family", "toric_variety"]
    slug: Slug


class GeometricMap(CatalogueRecord):
    """A map of geometric objects or families, including fibrations."""

    kind: Literal["fibration", "embedding", "construction"]
    source: GeometricReference
    target: GeometricReference
    generic_fiber: GeometricReference | None = None
    singular_locus: str | None = None

    @model_validator(mode="after")
    def check_fibration(self) -> Self:
        if self.kind == "fibration" and self.generic_fiber is None:
            raise PydanticCustomError(
                "fibration_fiber", "a fibration must name its generic fiber"
            )
        return self


class ModuliProblem(CatalogueRecord):
    """A specified moduli problem, distinct from local deformations of one variety."""

    name: str = Field(min_length=1)
    geometric_family: Slug
    dimension: Annotated[int, Field(ge=0)]
    polarization_orbit: Slug | None = None
    arithmetic_subgroup: str | None = Field(
        default=None,
        description="A key of the `groups` block of a lattice record, such as `Gamma_En_2`, that acts on the period domain.",
    )


class MonodromyGenerator(Record):
    loop: str = Field(min_length=1)
    matrix: list[list[int]]


class IntegralLocalSystem(CatalogueRecord):
    """An integral local system on the smooth base of a geometric family."""

    family: Slug
    degree: Annotated[int, Field(ge=0)]
    rank: Annotated[int, Field(gt=0)]
    fibration: Slug
    fiber_lattice: Tag | None = None
    monodromy_generators: list[MonodromyGenerator] = Field(default_factory=list)
    monodromy_group_structure: str | None = None

    @model_validator(mode="after")
    def check_monodromy(self) -> Self:
        if any(
            len(g.matrix) != self.rank or any(len(row) != self.rank for row in g.matrix)
            for g in self.monodromy_generators
        ):
            raise PydanticCustomError(
                "monodromy_matrix", "monodromy matrices act on the stated rank"
            )
        if any(
            abs(int(fmpz_mat(g.matrix).det())) != 1 for g in self.monodromy_generators
        ):
            raise PydanticCustomError(
                "monodromy_unimodular",
                "integral monodromy matrices are invertible over the integers",
            )
        if len({g.loop for g in self.monodromy_generators}) != len(
            self.monodromy_generators
        ):
            raise PydanticCustomError(
                "monodromy_loop", "each named loop has one monodromy matrix"
            )
        return self


class OperatorSingularity(Record):
    coordinate: str = Field(min_length=1)
    exponents: list[Rational]


class OperatorRealization(Record):
    family: Slug
    cohomology_degree: Annotated[int, Field(ge=0)]
    period: str = Field(min_length=1)
    local_system: Slug | None = None
    relation: Literal["picard_fuchs", "factor"]


class PicardFuchsOperator(CatalogueRecord):
    """An operator sum a_i(x) theta^i over Q[x], theta = x d/dx."""

    coordinate: str = Field(min_length=1)
    normalization: str = Field(min_length=1)
    order: Annotated[int, Field(gt=0)]
    coefficients: list[list[Rational]]
    singularities: list[OperatorSingularity] = Field(default_factory=list)
    realizations: list[OperatorRealization] = Field(default_factory=list)

    @model_validator(mode="after")
    def check_order(self) -> Self:
        if (
            len(self.coefficients) != self.order + 1
            or not self.coefficients[-1]
            or all(c == 0 for c in self.coefficients[-1])
        ):
            raise PydanticCustomError(
                "operator_order",
                "the highest theta coefficient is a nonzero polynomial of the stated order",
            )
        if any(not polynomial for polynomial in self.coefficients):
            raise PydanticCustomError(
                "operator_polynomial",
                "each polynomial has at least its constant coefficient",
            )
        return self
