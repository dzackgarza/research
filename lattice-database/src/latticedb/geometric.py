"""Records of smooth connected projective complex varieties and their Hodge numbers."""

from pathlib import Path
from typing import Annotated, Self

from pydantic import Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError

from latticedb.model import Record, Reference, Tag


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
    hodge_numbers: Annotated[tuple[Annotated[tuple[Annotated[int, Field(ge=0)], ...], Field(strict=False)], ...], Field(strict=False)] = Field(
        description="Square matrix with entry [p][q] equal to h^(p,q), for p,q from 0 through dimension."
    )
    cohomology_lattices: Annotated[tuple[CohomologyLattice, ...], Field(strict=False)] = ()
    references: Annotated[tuple[Reference, ...], Field(strict=False)] = ()

    @model_validator(mode="after")
    def check_hodge_numbers(self) -> Self:
        n = self.dimension
        h = self.hodge_numbers
        if len(h) != n + 1 or any(len(row) != n + 1 for row in h):
            raise PydanticCustomError("hodge_shape", "hodge_numbers must be a square matrix of side dimension + 1")
        if h[0][0] != 1:
            raise PydanticCustomError("hodge_connected", "a connected variety has h^(0,0) = 1")
        for p in range(n + 1):
            for q in range(n + 1):
                if h[p][q] != h[q][p] or h[p][q] != h[n - p][n - q]:
                    raise PydanticCustomError("hodge_symmetry", "Hodge symmetry and Serre duality must hold")
        degrees = [link.degree for link in self.cohomology_lattices]
        if len(degrees) != len(set(degrees)):
            raise PydanticCustomError("cohomology_degree", "a cohomology degree has more than one lattice")
        if any(degree > 2 * n for degree in degrees):
            raise PydanticCustomError("cohomology_degree", "a cohomology degree exceeds twice the dimension")
        return self

    def betti_number(self, degree: int) -> int:
        return sum(self.hodge_numbers[p][degree - p] for p in range(self.dimension + 1) if 0 <= degree - p <= self.dimension)


def problems(path: Path, error: ValidationError) -> list[str]:
    return [f"{path}: {'.'.join(str(part) for part in issue['loc']) or 'record'}: {issue['msg']}" for issue in error.errors()]
