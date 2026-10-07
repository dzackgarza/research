"""Typed records for lattice groups, genera, polytopes, and geometric constructions.

The records name mathematical objects and their defining data. Matrices and vectors
are coordinates in the bases named by their parent records. Source claims belong in
the Markdown prose with BibTeX citations.
"""

import ast
from typing import Annotated, Literal, Self

from pydantic import Field, model_validator
from pydantic_core import PydanticCustomError

from latticedb.model import GroupData, OrbitGroup, Rational, Record, Reference, Slug, Tag


class CatalogueRecord(Record):
    slug: Slug


class LieGroup(CatalogueRecord):
    """A real or complex Lie group recorded independently of any lattice realization."""

    name: str = Field(min_length=1)
    latex: str = Field(min_length=1)
    base_field: Literal["real", "complex"]
    dimension: Annotated[int, Field(ge=0)]
    real_rank: Annotated[int, Field(ge=0)] | None = None
    connected_components: Annotated[int, Field(gt=0)] | None = None
    lie_algebra: str | None = None
    orthogonal_signature: Annotated[tuple[int, int], Field(strict=False)] | None = None
    maximal_compact_factors: Annotated[tuple[Slug, ...], Field(strict=False)] = ()
    references: Annotated[tuple[Reference, ...], Field(strict=False)] = ()

    @model_validator(mode="after")
    def check_orthogonal_signature(self) -> Self:
        if self.orthogonal_signature is None:
            return self
        p, q = self.orthogonal_signature
        if self.base_field != "real" or p < 0 or q < p:
            raise PydanticCustomError(
                "lie_group_orthogonal_signature",
                "an orthogonal signature records the canonical real form O(p,q) with 0 <= p <= q",
            )
        return self


class ArithmeticGroup(CatalogueRecord):
    """An arithmetic subgroup of the real orthogonal group attached to a lattice."""

    name: str = Field(min_length=1)
    latex: str = Field(min_length=1)
    lattice: Tag
    ambient_lie_group: Slug
    standard_name: OrbitGroup | None = None
    parent_group: Slug | None = None
    data: GroupData = Field(default_factory=GroupData)

    @model_validator(mode="after")
    def check_parent_location(self) -> Self:
        if self.data.parent is not None:
            raise PydanticCustomError(
                "arithmetic_group_parent",
                "an arithmetic-group card names its parent by `parent_group`, not by the lattice-local `data.parent` field",
            )
        return self


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
        if len(set(self.representative_tags)) != len(self.representative_tags):
            raise PydanticCustomError(
                "genus_members",
                "a genus lists each representative tag at most once",
            )
        if self.representatives_complete and self.class_number != len(
            self.representative_tags
        ):
            raise PydanticCustomError(
                "genus_complete", "a complete list has exactly its stated class number"
            )
        return self


def _expression_value(node: ast.AST, parameter: str, value: int) -> int:
    """The value of an entry of `gram_template`: integer arithmetic in `parameter`."""
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
        "an entry of gram_template is an integer or integer arithmetic in the parameter",
    )


class LatticeFamily(CatalogueRecord):
    """An infinite parameterized family of lattices whose Gram matrix is a function of one integer parameter.

    For each integer `n >= minimum` the family holds the lattice whose Gram
    matrix is `gram_template` with `parameter` replaced by `n`. The entries of
    `gram_template` are integers or integer arithmetic in the parameter.
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
                "family_shape", "gram_template has rank rows of rank components"
            )
        seen = False
        for row in rows:
            for entry in row:
                if isinstance(entry, str):
                    seen = True
                if isinstance(entry, bool):
                    raise PydanticCustomError(
                        "family_expression",
                        "an entry of gram_template is an integer or integer arithmetic in the parameter",
                    )
                if isinstance(entry, str):
                    try:
                        tree = ast.parse(entry, mode="eval")
                    except SyntaxError:
                        raise PydanticCustomError(
                            "family_expression",
                            "an entry of gram_template is an integer or integer arithmetic in the parameter",
                        ) from None
                    names = {
                        node.id
                        for node in ast.walk(tree)
                        if isinstance(node, ast.Name)
                    }
                    if names != {self.parameter}:
                        raise PydanticCustomError(
                            "family_parameter",
                            "each expression in gram_template names the parameter and nothing else",
                        )
        if not seen:
            raise PydanticCustomError(
                "family_parameter",
                "the parameter occurs in gram_template",
            )
        if any(
            rows[i][j] != rows[j][i]
            for i in range(self.rank)
            for j in range(self.rank)
        ):
            raise PydanticCustomError(
                "family_symmetric", "gram_template is a symmetric tensor"
            )
        return self


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
    arithmetic_subgroup: Slug | None = Field(
        default=None,
        description="The arithmetic-group card of the group acting on the period domain.",
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
