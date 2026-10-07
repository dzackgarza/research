"""Geometric records, including projective varieties and symmetric spaces."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Literal, Self

from pydantic import Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError

from latticedb.model import Rational, Record, Slug, Tag


class HodgeTerm(Record):
    """The nonzero coefficient of u^p v^q in the Hodge–Poincaré series."""

    p: Annotated[int, Field(ge=0)]
    q: Annotated[int, Field(ge=0)]
    coefficient: Annotated[int, Field(ge=1)]


class ChernNumber(Record):
    """The integral of a top-degree product of Chern classes of the tangent bundle."""

    indices: Annotated[tuple[Annotated[int, Field(ge=1)], ...], Field(strict=False)]
    value: int


class PontryaginNumber(Record):
    """The integral of a top-degree product of Pontryagin classes of the real tangent bundle."""

    indices: list[Annotated[int, Field(ge=1)]]
    value: int


class RiemannRochPolynomial(Record):
    """Coefficients of the Euler characteristic polynomial in the BBF square of a line bundle."""

    coefficients: list[Rational] = Field(min_length=1)


class AlgebraicGroup(Record):
    """A cited identification of the identity component of an automorphism group."""

    name: str = Field(min_length=1)
    dimension: Annotated[int, Field(ge=0)]
    structure: str = Field(min_length=1)
    cohomology_action: Slug | None = Field(
        default=None,
        description="Arithmetic-group card for the induced integral cohomology action, when recorded.",
    )


class HomotopyGroup(Record):
    degree: Annotated[int, Field(ge=1)]
    name: str = Field(min_length=1)
    free_rank: Annotated[int, Field(ge=0)] | None = None
    torsion_factors: list[Annotated[int, Field(gt=1)]] | None = None


class ClassificationLabel(Record):
    convention: str = Field(min_length=1)
    label: str = Field(min_length=1)


class IwasawaDecomposition(Record):
    positive_restricted_roots: str = Field(min_length=1)
    k: str = Field(min_length=1)
    a: str = Field(min_length=1)
    n: str = Field(min_length=1)


class CohomologyGroup(Record):
    degree: Annotated[int, Field(ge=0)]
    coefficients: str = Field(min_length=1)
    group: str = Field(min_length=1)


class FanoData(Record):
    picard_rank: Annotated[int, Field(gt=0)]
    index: Annotated[int, Field(gt=0)]
    anticanonical_degree: Annotated[int, Field(gt=0)]


class SurfaceData(Record):
    kodaira_dimension: Literal["minus_infinity", 0, 1, 2]


class HomogeneousConstruction(Record):
    kind: Literal["homogeneous"] = "homogeneous"
    group: str = Field(min_length=1)
    parabolic_nodes: list[Annotated[int, Field(gt=0)]] = Field(min_length=1)


class HorosphericalConstruction(Record):
    kind: Literal["horospherical"] = "horospherical"
    group: str = Field(min_length=1)
    parameters: str = Field(min_length=1)


class CompleteIntersectionConstruction(Record):
    kind: Literal["calabi_yau_complete_intersection"] = "calabi_yau_complete_intersection"
    ambient_projective_dimensions: list[Annotated[int, Field(ge=0)]] = Field(min_length=1)
    equation_multidegrees: list[list[Annotated[int, Field(ge=0)]]] = Field(min_length=1)

    @model_validator(mode="after")
    def check_configuration_shape(self) -> Self:
        count = len(self.ambient_projective_dimensions)
        if any(len(degrees) != count for degrees in self.equation_multidegrees):
            raise PydanticCustomError("configuration_shape", "each equation has one degree in each projective factor")
        return self


class ToricHypersurfaceConstruction(Record):
    kind: Literal["toric_anticanonical_hypersurface"] = "toric_anticanonical_hypersurface"
    toric_variety: Slug


type GeometricConstruction = HomogeneousConstruction | HorosphericalConstruction | CompleteIntersectionConstruction | ToricHypersurfaceConstruction


class GeometricFamily(Record):
    """A parameterized deformation family whose instances have their own Hodge series."""

    slug: Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
    name: str = Field(min_length=1)
    parameter: str = Field(min_length=1)
    minimum: Annotated[int, Field(ge=0)]
    construction: GeometricConstruction | None = Field(default=None, discriminator="kind")


class CohomologyLattice(Record):
    degree: Annotated[int, Field(ge=0)] = Field(description="The degree k of integral cohomology H^k(X, Z) modulo torsion.")
    pairing: str = Field(min_length=1, description="The bilinear form on this cohomology group, such as the cup-product intersection form.")
    tag: Tag = Field(description="The tag of the lattice that represents this group with the named form, up to the stated scale.")
    scale: int = Field(description="The form on this cohomology group is scale times the form of the tagged lattice.")

    @model_validator(mode="after")
    def nonzero_scale(self) -> Self:
        if self.scale == 0:
            raise PydanticCustomError("cohomology_scale", "a cohomology lattice scale must be nonzero")
        return self


class LocallyRingedSpace(Record):
    """The shared record identity for geometric spaces with a structure sheaf."""

    slug: Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
    name: str = Field(min_length=1)


class ComplexManifold(LocallyRingedSpace):
    """A connected complex manifold, including an analytification when named."""

    kind: Literal["complex_manifold"]
    complex_dimension: Annotated[int, Field(ge=0)]
    algebraic_model: Slug | None = None


class ProjectiveComplexVariety(LocallyRingedSpace):
    """One smooth connected projective complex variety or a class with constant stated invariants."""

    kind: Literal["projective_complex_variety"]
    analytic_space: Slug | None = None
    dimension: Annotated[int, Field(ge=0)]
    hodge_poincare: Annotated[tuple[HodgeTerm, ...], Field(strict=False)] = Field(description="Nonzero coefficients of H_X(u,v) = sum h^(p,q) u^p v^q.")
    symmetry_group: Literal["V4", "D4"] | None = Field(default=None, description="The full subgroup of square symmetries preserving the Hodge diamond.")
    local_deformation_dimension: Annotated[int, Field(ge=0)] | None = Field(default=None, description="The dimension of the local complex deformation space when unobstructed.")
    betti_numbers: Annotated[tuple[Annotated[int, Field(ge=0)], ...], Field(strict=False)] = Field(
        default=(),
        description="b_0, ..., b_{2 dimension}: the ranks of H^k(X; Z), transcribed from the card's source.",
    )
    euler_characteristic: int | None = Field(
        default=None,
        description="The topological Euler characteristic of X, transcribed from the card's source.",
    )
    chern_numbers: Annotated[tuple[ChernNumber, ...], Field(strict=False)] = ()
    pontryagin_numbers: list[PontryaginNumber] = Field(default_factory=list)
    riemann_roch_polynomial: RiemannRochPolynomial | None = None
    automorphism_identity_component: AlgebraicGroup | None = None
    homotopy_groups: list[HomotopyGroup] = Field(default_factory=list)
    fano: FanoData | None = None
    surface: SurfaceData | None = None
    construction: GeometricConstruction | None = Field(default=None, discriminator="kind")
    family: str | None = None
    family_parameter: int | None = None
    cohomology_lattices: Annotated[tuple[CohomologyLattice, ...], Field(strict=False)] = ()

    @model_validator(mode="after")
    def check_hodge_poincare(self) -> Self:
        if len({(term.p, term.q) for term in self.hodge_poincare}) != len(self.hodge_poincare):
            raise PydanticCustomError("hodge_duplicate", "a Hodge–Poincaré monomial occurs more than once")
        if self.betti_numbers and len(self.betti_numbers) != 2 * self.dimension + 1:
            raise PydanticCustomError("betti_shape", "Betti numbers list b_0 through b_(2 dimension)")
        if (self.family is None) != (self.family_parameter is None):
            raise PydanticCustomError("family_parameter", "family and family_parameter must occur together")
        chern_indices: set[tuple[int, ...]] = set()
        for number in self.chern_numbers:
            if (
                tuple(sorted(number.indices)) != number.indices
                or sum(number.indices) != self.dimension
                or number.indices in chern_indices
            ):
                raise PydanticCustomError("chern_number", "Chern indices must be an ordered partition of the dimension, each occurring once")
            chern_indices.add(number.indices)
        if any(2 * sum(number.indices) != self.dimension for number in self.pontryagin_numbers):
            raise PydanticCustomError("pontryagin_degree", "Pontryagin indices must be a partition of a quarter of the real dimension")
        if len({tuple(number.indices) for number in self.pontryagin_numbers}) != len(self.pontryagin_numbers):
            raise PydanticCustomError("pontryagin_duplicate", "a Pontryagin number occurs more than once")
        if self.surface is not None and self.dimension != 2:
            raise PydanticCustomError("surface_dimension", "surface data require complex dimension two")
        if len({group.degree for group in self.homotopy_groups}) != len(self.homotopy_groups):
            raise PydanticCustomError("homotopy_duplicate", "a homotopy degree occurs more than once")
        degrees = [link.degree for link in self.cohomology_lattices]
        if len(degrees) != len(set(degrees)):
            raise PydanticCustomError("cohomology_degree", "a cohomology degree has more than one lattice")
        return self

    def hodge_number(self, p: int, q: int) -> int:
        """The stored coefficient of u^p v^q in the Hodge–Poincaré series; zero when the card omits it."""
        return next(
            (term.coefficient for term in self.hodge_poincare if (term.p, term.q) == (p, q)),
            0,
        )


class RiemannianSymmetricSpace(LocallyRingedSpace):
    """A connected Riemannian symmetric space with a specified symmetric presentation."""

    kind: Literal["riemannian_symmetric_space"]
    real_dimension: Annotated[int, Field(gt=0)]
    group: str = Field(min_length=1)
    isotropy_group: str = Field(min_length=1)
    involution: str = Field(min_length=1)
    metric_normalization: str = Field(min_length=1)
    curvature_type: Literal["euclidean", "compact", "noncompact"]
    compact: bool
    rank: Annotated[int, Field(gt=0)]
    classification: Annotated[tuple[ClassificationLabel, ...], Field(strict=False)] = ()
    lie_algebra: str | None = None
    restricted_roots: str | None = None
    root_multiplicities: str | None = None
    diagrams: Annotated[tuple[Slug, ...], Field(strict=False)] = ()
    holonomy: str | None = None
    iwasawa: IwasawaDecomposition | None = None
    compact_dual: Slug | None = None
    noncompact_dual: Slug | None = None
    homotopy_groups: Annotated[tuple[HomotopyGroup, ...], Field(strict=False)] = ()
    cohomology_groups: Annotated[tuple[CohomologyGroup, ...], Field(strict=False)] = ()

    @model_validator(mode="after")
    def check_symmetric_data(self) -> Self:
        if len(set(self.diagrams)) != len(self.diagrams):
            raise PydanticCustomError("diagram_duplicate", "diagram links must be unique")
        if len({group.degree for group in self.homotopy_groups}) != len(self.homotopy_groups):
            raise PydanticCustomError("homotopy_duplicate", "a homotopy degree occurs more than once")
        if len({(group.degree, group.coefficients) for group in self.cohomology_groups}) != len(self.cohomology_groups):
            raise PydanticCustomError("cohomology_duplicate", "a cohomology degree and coefficient ring occur more than once")
        return self


class HermitianSymmetricSpace(RiemannianSymmetricSpace, ComplexManifold):
    """A Riemannian symmetric space with an invariant complex and Hermitian structure."""

    kind: Literal["hermitian_symmetric_space"]
    hermitian_classification: Annotated[tuple[ClassificationLabel, ...], Field(strict=False)] = ()
    tube_type: bool | None = None
    bounded_realization: str | None = None
    compact_dual_parabolic: str | None = None


type GeometricObject = Annotated[
    ProjectiveComplexVariety | ComplexManifold | RiemannianSymmetricSpace | HermitianSymmetricSpace,
    Field(discriminator="kind"),
]


def problems(path: Path, error: ValidationError) -> list[str]:
    return [f"{path}: {'.'.join(str(part) for part in issue['loc']) or 'record'}: {issue['msg']}" for issue in error.errors()]
