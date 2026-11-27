"""
Semantic lattice base for the Coble project.
"""

from __future__ import annotations

from collections.abc import Sequence
from functools import reduce
from itertools import repeat
from typing import Self

from sage.all import ZZ, FreeQuadraticModule, Integer, IntegralLattice, MatrixSpace, gcd
from sage.modules.fg_pid.fgp_morphism import FGP_Morphism
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.vector_integer_dense import Vector_integer_dense

_ONE = ZZ.one()
_ZERO = ZZ.zero()
_NEGATIVE_ONE = -_ONE
_ZERO_GRAM = MatrixSpace(ZZ, _ONE)([_ZERO])
_A1_LATTICE = IntegralLattice("A1")
_E8_LATTICE = IntegralLattice("E8")
_SAMPLE_FREE_BILINEAR_MODULE = FreeQuadraticModule(ZZ, _ONE, _ZERO_GRAM)
_SAMPLE_DISCRIMINANT_GROUP = _A1_LATTICE.discriminant_group()

_FreeBilinearModuleBase = type(_SAMPLE_FREE_BILINEAR_MODULE)
_LatticeBase = type(_A1_LATTICE)
_DiscriminantGroupBase = type(_SAMPLE_DISCRIMINANT_GROUP)
_DiscriminantGroupElementBase = type(next(iter(_SAMPLE_DISCRIMINANT_GROUP.gens())))


class FreeBilinearModuleElement(Vector_integer_dense):
    def is_isotropic(self):
        assert self.parent().base_ring() is ZZ
        return self.inner_product(self).is_zero()


class LatticeElement(FreeBilinearModuleElement):
    def divisibility(self) -> Integer:
        assert self.parent().base_ring() is ZZ
        return gcd(tuple(self * self.parent().inner_product_matrix())).abs()

    def is_primitive(self):
        divisor = self.divisibility()
        assert divisor in ZZ
        return divisor.is_one()

    def discriminant_class(self) -> DiscriminantGroupElement:
        assert self.parent().base_ring() is ZZ
        return self.parent().discriminant_group()(self)


class LatticeMorphism(FreeModuleMorphism):
    def image_lattice(self) -> Lattice:
        image = self.image()
        assert image.base_ring() is ZZ
        return Lattice.from_sage(image)

    def orthogonal_complement_of_image(self) -> Lattice:
        assert self.codomain().base_ring() is ZZ
        return self.codomain().orthogonal_complement(self.image_lattice())


class DiscriminantGroupElement(_DiscriminantGroupElementBase):
    def is_isotropic(self):
        assert self.parent().base_ring() is ZZ
        return self.quadratic_product().is_zero()


class DiscriminantGroupMorphism(FGP_Morphism):
    def image_generators(self):
        assert self.domain().base_ring() is ZZ
        return self.im_gens()


class FreeBilinearModule(_FreeBilinearModuleBase):
    Element = FreeBilinearModuleElement

    @classmethod
    def from_sage(cls, module: _FreeBilinearModuleBase) -> Self:
        assert module.base_ring() is ZZ
        return cls(
            module.base_ring(),
            module.rank(),
            module.inner_product_matrix(),
            sparse=module.is_sparse(),
        )


class DiscriminantGroup(_DiscriminantGroupBase):
    Element = DiscriminantGroupElement

    @classmethod
    def from_sage(cls, group: _DiscriminantGroupBase) -> Self:
        assert group.base_ring() is ZZ
        return cls(
            group.V(),
            group.W(),
            group.gens(),
            group._modulus,
            group._modulus_qf,
        )

    @classmethod
    def from_lattice(cls, lattice: Lattice) -> Self:
        assert lattice.base_ring() is ZZ
        return cls.from_sage(_LatticeBase.discriminant_group(lattice))

    def hom(
        self,
        codomain: Self,
        images: Sequence[DiscriminantGroupElement],
    ) -> DiscriminantGroupMorphism:
        assert codomain.base_ring() is ZZ
        homset = self.Hom(codomain)
        return DiscriminantGroupMorphism(homset, homset(images))


class Lattice(_LatticeBase):
    Element = LatticeElement

    @classmethod
    def from_sage(cls, lattice: _LatticeBase) -> Self:
        assert lattice.base_ring() is ZZ
        return cls(
            lattice.ambient_module(),
            lattice.basis_matrix(),
            lattice.inner_product_matrix(),
        )

    @classmethod
    def rank_one(cls, scale: Integer) -> Self:
        assert scale in ZZ
        return cls(
            _A1_LATTICE.ambient_module(),
            _A1_LATTICE.basis_matrix(),
            MatrixSpace(ZZ, _ONE)([scale]),
        )

    @classmethod
    def hyperbolic_plane(cls) -> Self:
        plane = IntegralLattice("U")
        assert plane.is_even()
        return cls.from_sage(plane)

    @classmethod
    def a1_negative(cls) -> Self:
        assert _A1_LATTICE.is_even()
        return cls(
            _A1_LATTICE.ambient_module(),
            _A1_LATTICE.basis_matrix(),
            _NEGATIVE_ONE * _A1_LATTICE.inner_product_matrix(),
        )

    @classmethod
    def e8_negative(cls) -> Self:
        assert _E8_LATTICE.is_even()
        return cls(
            _E8_LATTICE.ambient_module(),
            _E8_LATTICE.basis_matrix(),
            _NEGATIVE_ONE * _E8_LATTICE.inner_product_matrix(),
        )

    @classmethod
    def coble_picard(cls) -> Self:
        positive_line = cls.rank_one(ZZ("2"))
        negative_line = cls.rank_one(ZZ("-2"))
        picard = reduce(
            _LatticeBase.direct_sum,
            repeat(negative_line, int(ZZ("10"))),
            positive_line,
        )
        assert picard.is_even()
        return cls.from_sage(picard)

    @classmethod
    def coble_transcendental(cls) -> Self:
        transcendental = _LatticeBase.direct_sum(
            _LatticeBase.direct_sum(
                cls.rank_one(ZZ("2")),
                cls.hyperbolic_plane(),
            ),
            cls.e8_negative(),
        )
        assert transcendental.is_even()
        return cls.from_sage(transcendental)

    @classmethod
    def k3(cls) -> Self:
        k3_lattice = reduce(
            _LatticeBase.direct_sum,
            (
                cls.hyperbolic_plane(),
                cls.hyperbolic_plane(),
                cls.e8_negative(),
                cls.e8_negative(),
            ),
            cls.hyperbolic_plane(),
        )
        assert k3_lattice.is_even()
        return cls.from_sage(k3_lattice)

    def discriminant_group(self) -> DiscriminantGroup:
        assert self.base_ring() is ZZ
        return DiscriminantGroup.from_sage(_LatticeBase.discriminant_group(self))

    def orthogonal_complement(self, sublattice: Self) -> Self:
        assert sublattice.base_ring() is ZZ
        return type(self).from_sage(
            _LatticeBase.orthogonal_complement(self, sublattice)
        )

    def hom(self, codomain: Self, images: Sequence[LatticeElement]) -> LatticeMorphism:
        assert codomain.base_ring() is ZZ
        return LatticeMorphism(self.Hom(codomain), images)
