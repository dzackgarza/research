from __future__ import annotations

from sage.all import QQ, ZZ, QuadraticForm, matrix, vector
from sage.modules.fg_pid.fgp_module import FGP_Module
from src.lattices.core.abstract import BilinearModule
from src.lattices.core.elements import DualLatticeElement, RationalLatticeElement
from src.lattices.core.free import FreeBilinearModule
from src.lattices.validation.presentations import CoordinatePresentation, RationalLatticePresentation


class RationalLattice(FreeBilinearModule):
    Element = RationalLatticeElement

    @classmethod
    def _coordinate_ring(cls):
        return QQ

    def __init__(self, gram, *, generator_names: tuple[str, ...] = ()):
        presentation = RationalLatticePresentation(gram=gram, generator_names=generator_names)
        super().__init__(self._coordinate_ring(), presentation.gram, generator_names=presentation.generator_names)

    @classmethod
    def from_gram(cls, gram, *, generator_names: tuple[str, ...] = ()):
        from src.lattices.core.integral import Lattice

        gram_matrix = matrix(QQ, gram)
        if gram_matrix.denominator().is_one() and gram_matrix.det() != 0:
            return Lattice.from_gram(matrix(ZZ, gram_matrix), generator_names=generator_names)
        return cls(gram_matrix, generator_names=generator_names)

    def element_from(self, coordinates):
        presentation = CoordinatePresentation(module_ring=QQ, rank=self.ngens(), coordinates=coordinates)
        return self.Element(self, presentation.coordinates)

    def is_integral(self):
        return self.gram_matrix().denominator().is_one()

    def _scalar_multiple(self, element, scalar):
        return self.element_from(QQ(scalar) * element.to_vector())

    def dual(self):
        return RationalLattice(self.gram_matrix().inverse(), generator_names=self.generator_names())

    def signature_pair(self):
        positive, negative, _zero = QuadraticForm(QQ, self.gram_matrix()).signature_vector()
        return positive, negative

    def signature(self):
        return self.signature_pair()

    @classmethod
    def _neg_root_gram_qq(cls, cartan_type: str):
        from sage.all import RootSystem

        space = RootSystem(cartan_type).ambient_space()
        simple_roots = list(space.simple_roots())
        return -matrix(QQ, [[left.inner_product(right) for right in simple_roots] for left in simple_roots])

    @classmethod
    def F4(cls):
        return cls.from_gram(cls._neg_root_gram_qq("F4"))

    @classmethod
    def G2(cls):
        from src.lattices.core.integral import Lattice

        return cls.from_gram(Lattice._integral_root_gram("G2"))


class DualLattice(RationalLattice):
    Element = DualLatticeElement

    def __init__(self, source_lattice):
        self._source_lattice = source_lattice
        coordinate_module = ZZ ** source_lattice.ngens()
        BilinearModule.__init__(
            self,
            FGP_Module(coordinate_module, coordinate_module.zero_submodule()),
            matrix(QQ, source_lattice.gram_matrix().inverse()),
            value_ring=QQ,
            generator_names=source_lattice.generator_names(),
        )

    @classmethod
    def from_lattice(cls, lattice):
        return cls(lattice)

    def source_lattice(self):
        return self._source_lattice

    def inclusion_morphism(self):
        source = self.source_lattice()
        gram = source.gram_matrix()
        return source.hom(self).element_from_matrix(gram)

    def dual(self):
        return self._source_lattice

    def element_from(self, coordinates):
        presentation = CoordinatePresentation(module_ring=ZZ, rank=self.ngens(), coordinates=coordinates)
        return self.Element(self, presentation.coordinates)

    def _scalar_multiple(self, element, scalar):
        assert scalar in ZZ, "Scalar multiplication on the dual lattice is integral in the dual basis"
        return self.element_from(ZZ(scalar) * element.to_vector())

    def element_from_dual_coordinates(self, coordinates):
        return self.element_from(coordinates)

    def element_from_primal_coordinates(self, coordinates):
        presentation = CoordinatePresentation(module_ring=QQ, rank=self.ngens(), coordinates=coordinates)
        dual_coordinates = self._source_lattice.gram_matrix() * presentation.coordinates.column()
        dual_vector = vector(QQ, dual_coordinates.column(0))
        assert dual_vector.denominator().is_one(), (
            "Primal coordinates define a dual-lattice element exactly when the dual coordinates are integral"
        )
        return self.element_from_dual_coordinates(vector(ZZ, dual_vector))

    def primal_coordinates_of(self, value):
        element = value if value.parent() is self else self.element_from_dual_coordinates(value)
        primal = self.gram_matrix() * element.to_vector().column()
        return vector(QQ, primal.column(0))

    def discriminant_class_of(self, value):
        element = value if value.parent() is self else self.element_from_dual_coordinates(value)
        return self._source_lattice.discriminant_group()(element)

    def discriminant_group(self):
        return self._source_lattice.discriminant_group()
