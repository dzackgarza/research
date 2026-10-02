"""Records of smooth connected projective complex varieties and their Hodge numbers."""

from pathlib import Path
from typing import Annotated, Literal, Self

from pydantic import Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError

from latticedb.model import Record, Tag


class HodgeTerm(Record):
    """The nonzero coefficient of u^p v^q in the Hodge–Poincaré series."""

    p: Annotated[int, Field(ge=0)]
    q: Annotated[int, Field(ge=0)]
    coefficient: Annotated[int, Field(ge=1)]


class ChernNumber(Record):
    """The integral of a top-degree product of Chern classes of the tangent bundle."""

    indices: Annotated[tuple[Annotated[int, Field(ge=1)], ...], Field(strict=False)]
    value: int


class GeometricFamily(Record):
    """A parameterized deformation family whose instances have their own Hodge series."""

    slug: Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
    name: str = Field(min_length=1)
    parameter: str = Field(min_length=1)
    minimum: Annotated[int, Field(ge=0)]


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


class GeometricObject(Record):
    """One smooth connected projective complex variety or a class with constant stated invariants."""

    slug: Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
    name: str = Field(min_length=1)
    dimension: Annotated[int, Field(ge=0)]
    hodge_poincare: Annotated[tuple[HodgeTerm, ...], Field(strict=False)] = Field(description="Nonzero coefficients of H_X(u,v) = sum h^(p,q) u^p v^q.")
    symmetry_group: Literal["V4", "D4"] | None = Field(default=None, description="The full subgroup of square symmetries preserving the Hodge diamond.")
    local_deformation_dimension: Annotated[int, Field(ge=0)] | None = Field(default=None, description="The dimension of the local complex deformation space when unobstructed.")
    chern_numbers: Annotated[tuple[ChernNumber, ...], Field(strict=False)] = ()
    family: str | None = None
    family_parameter: int | None = None
    cohomology_lattices: Annotated[tuple[CohomologyLattice, ...], Field(strict=False)] = ()

    @model_validator(mode="after")
    def check_hodge_poincare(self) -> Self:
        n = self.dimension
        h = {(term.p, term.q): term.coefficient for term in self.hodge_poincare}
        if len(h) != len(self.hodge_poincare):
            raise PydanticCustomError("hodge_duplicate", "a Hodge–Poincaré monomial occurs more than once")
        if any(p > n or q > n for p, q in h):
            raise PydanticCustomError("hodge_degree", "a Hodge–Poincaré exponent exceeds the dimension")
        if h.get((0, 0)) != 1:
            raise PydanticCustomError("hodge_connected", "a connected variety has h^(0,0) = 1")
        for p in range(n + 1):
            for q in range(n + 1):
                if h.get((p, q), 0) != h.get((q, p), 0) or h.get((p, q), 0) != h.get((n - p, n - q), 0):
                    raise PydanticCustomError("hodge_symmetry", "Hodge symmetry and Serre duality must hold")
        # The square action and its hyperkähler enlargement are stated at https://hyperkaehler.info/hodge/.
        group = "D4" if all(h.get((p, q), 0) == h.get((n - p, q), 0) for p in range(n + 1) for q in range(n + 1)) else "V4"
        if self.symmetry_group is not None and self.symmetry_group != group:
            raise PydanticCustomError("hodge_group", "the declared symmetry group does not preserve exactly the Hodge–Poincaré series")
        if (self.family is None) != (self.family_parameter is None):
            raise PydanticCustomError("family_parameter", "family and family_parameter must occur together")
        chern_indices: set[tuple[int, ...]] = set()
        for number in self.chern_numbers:
            if sum(number.indices) != n or tuple(sorted(number.indices)) != number.indices or number.indices in chern_indices:
                raise PydanticCustomError("chern_number", "Chern indices must be ordered, unique and sum to the dimension")
            chern_indices.add(number.indices)
            if number.indices == (n,) and number.value != self.euler_characteristic():
                raise PydanticCustomError("chern_euler", "the top Chern number equals the Euler characteristic")
        degrees = [link.degree for link in self.cohomology_lattices]
        if len(degrees) != len(set(degrees)):
            raise PydanticCustomError("cohomology_degree", "a cohomology degree has more than one lattice")
        if any(degree > 2 * n for degree in degrees):
            raise PydanticCustomError("cohomology_degree", "a cohomology degree exceeds twice the dimension")
        return self

    def betti_number(self, degree: int) -> int:
        return sum(term.coefficient for term in self.hodge_poincare if term.p + term.q == degree)

    def hodge_number(self, p: int, q: int) -> int:
        return next((term.coefficient for term in self.hodge_poincare if term.p == p and term.q == q), 0)

    def euler_characteristic(self) -> int:
        return sum((-1) ** (term.p + term.q) * term.coefficient for term in self.hodge_poincare)


def problems(path: Path, error: ValidationError) -> list[str]:
    return [f"{path}: {'.'.join(str(part) for part in issue['loc']) or 'record'}: {issue['msg']}" for issue in error.errors()]
