from __future__ import annotations

from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict, model_validator
from sage.all import QQ, ZZ, Integer, lcm, matrix, vector
from sage.matrix.matrix0 import Matrix
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.quotient_module import FreeModule_ambient_field_quotient
from sage.rings.rational import Rational
from sage.structure.element import Vector
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent

type ScalarLike = int | Integer | Rational
type MatrixInput = Matrix | Sequence[Sequence[ScalarLike]]
type VectorInput = Vector | ElementWrapper | Sequence[ScalarLike]


def default_generator_names(rank: int) -> tuple[str, ...]:
    return tuple(f"e_{index + 1}" for index in range(rank))


def clear_denominators(candidate):
    denominators = [QQ(entry).denominator() for entry in candidate.list()]
    factor = Integer(lcm(denominators)) if denominators else ZZ.one()
    return matrix(ZZ, factor * candidate)


def canonical_modulo(value, modulus: int):
    lifted = QQ(value)
    step = QQ(modulus)
    half_step = step / 2
    while lifted > half_step:
        lifted -= step
    while lifted <= -half_step:
        lifted += step
    return lifted


class FreeModulePresentation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    module_ring: Parent
    value_ring: Parent
    gram: MatrixInput
    generator_names: tuple[str, ...] = ()

    @model_validator(mode="after")
    def _validate(self) -> FreeModulePresentation:
        gram_matrix = matrix(self.value_ring, self.gram)
        assert gram_matrix.nrows() == gram_matrix.ncols(), "Gram matrix must be square"
        assert gram_matrix == gram_matrix.transpose(), "Gram matrix must be symmetric"
        names = self.generator_names or default_generator_names(gram_matrix.nrows())
        assert len(names) == gram_matrix.nrows(), "Generator-name tuple must match the rank"
        self.gram = gram_matrix
        self.generator_names = tuple(names)
        return self


class BilinearModulePresentation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    module: FGP_Module_class | FreeModule_ambient_field_quotient
    value_ring: Parent
    gram: MatrixInput
    generator_names: tuple[str, ...] = ()

    @model_validator(mode="after")
    def _validate(self) -> BilinearModulePresentation:
        gram_matrix = matrix(self.value_ring, self.gram)
        assert gram_matrix.nrows() == gram_matrix.ncols(), "Gram matrix must be square"
        assert gram_matrix == gram_matrix.transpose(), "Gram matrix must be symmetric"
        generator_count = len(tuple(self.module.gens()))
        names = self.generator_names or default_generator_names(generator_count)
        assert generator_count == gram_matrix.nrows(), "Gram matrix size must match the chosen generator count"
        assert len(names) == generator_count, "Generator-name tuple must match the chosen generator count"
        self.gram = gram_matrix
        self.generator_names = tuple(names)
        return self


class LatticePresentation(FreeModulePresentation):
    module_ring: Parent = ZZ
    value_ring: Parent = ZZ

    @model_validator(mode="after")
    def _validate_lattice(self) -> LatticePresentation:
        super()._validate()
        assert self.gram.det() != 0 or self.gram.nrows() == 0, "Integral lattices must be nondegenerate"
        self.gram = matrix(ZZ, self.gram)
        return self


class RationalLatticePresentation(FreeModulePresentation):
    module_ring: Parent = QQ
    value_ring: Parent = QQ

    @model_validator(mode="after")
    def _validate_rational_lattice(self) -> RationalLatticePresentation:
        super()._validate()
        assert self.gram.det() != 0 or self.gram.nrows() == 0, "Rational lattices must be nondegenerate"
        self.gram = matrix(QQ, self.gram)
        return self


class CoordinatePresentation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    module_ring: Parent
    rank: int
    coordinates: VectorInput

    @model_validator(mode="after")
    def _validate(self) -> CoordinatePresentation:
        coordinate_vector = vector(self.module_ring, self.coordinates)
        assert len(coordinate_vector) == int(self.rank), "Coordinate vector must have the module rank"
        self.coordinates = coordinate_vector
        return self


class IntegralCoordinatePresentation(CoordinatePresentation):
    module_ring: Parent = ZZ

    @model_validator(mode="after")
    def _validate_integral(self) -> IntegralCoordinatePresentation:
        super()._validate()
        assert all(entry in ZZ for entry in self.coordinates), f"{self.coordinates!r} is not an integral coordinate vector"
        self.coordinates = vector(ZZ, [Integer(entry) for entry in self.coordinates])
        return self


class PrimePresentation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    prime: int | Integer

    @model_validator(mode="after")
    def _validate(self) -> PrimePresentation:
        self.prime = Integer(self.prime)
        assert self.prime.is_prime(), "Prime-indexed invariant requires a prime index"
        return self


class MorphismPresentation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    module_ring: Parent
    value_ring: Parent
    domain_ngens: int
    codomain_ngens: int
    domain_gram: MatrixInput
    codomain_gram: MatrixInput
    matrix_data: MatrixInput

    @model_validator(mode="after")
    def _validate(self) -> MorphismPresentation:
        morphism_matrix = matrix(self.module_ring, self.matrix_data)
        assert morphism_matrix.nrows() == self.codomain_ngens, "Morphism matrix has the wrong codomain generator count"
        assert morphism_matrix.ncols() == self.domain_ngens, "Morphism matrix has the wrong domain generator count"
        left = morphism_matrix.transpose() * matrix(self.value_ring, self.codomain_gram) * morphism_matrix
        assert left == matrix(self.value_ring, self.domain_gram), "Morphism must preserve the bilinear form exactly"
        self.matrix_data = morphism_matrix
        return self


class GeneratorImagePresentation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    domain: Parent
    codomain: Parent
    images: Sequence[ElementWrapper]

    @model_validator(mode="after")
    def _validate(self) -> GeneratorImagePresentation:
        image_tuple = tuple(self.images)
        assert len(image_tuple) == self.domain.ngens(), "A hom-space element needs one image for each domain generator"
        assert all(image.parent() is self.codomain for image in image_tuple), "Generator images must lie in the codomain"
        self.images = image_tuple
        return self


class DiscriminantPresentation(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    invariants: Sequence[int | Integer]
    gram: MatrixInput
    modulus: int = 1
    quadratic_modulus: int = 2

    @model_validator(mode="after")
    def _validate(self) -> DiscriminantPresentation:
        invariant_factors = tuple(Integer(invariant) for invariant in self.invariants)
        assert all(invariant >= 1 for invariant in invariant_factors), "Invariant factors must be positive"
        gram_matrix = matrix(QQ, self.gram)
        assert gram_matrix.nrows() == gram_matrix.ncols(), "Discriminant Gram matrix must be square"
        assert gram_matrix == gram_matrix.transpose(), "Discriminant Gram matrix must be symmetric"
        assert gram_matrix.nrows() == len(invariant_factors), (
            "Invariant factors and discriminant Gram matrix must have the same rank"
        )
        assert all(
            invariant_factors[i] * invariant_factors[j] * gram_matrix[i, j] in ZZ
            for i in range(len(invariant_factors))
            for j in range(len(invariant_factors))
        ), "Discriminant Gram entries must respect the invariant factors"
        self.invariants = invariant_factors
        self.gram = gram_matrix
        self.modulus = int(self.modulus)
        self.quadratic_modulus = int(self.quadratic_modulus)
        return self
