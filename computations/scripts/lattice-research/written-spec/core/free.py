from __future__ import annotations

from collections.abc import Sequence

from sage.all import QQ, ZZ, matrix
from sage.modules.fg_pid.fgp_module import FGP_Module
from sage.modules.free_quadratic_module import FreeQuadraticModule
from src.lattices.core.abstract import BilinearModule
from src.lattices.core.elements import FreeBilinearModuleElement
from src.lattices.validation.presentations import FreeModulePresentation


def _presented_bilinear_module(base_ring, gram, *, value_ring=None, generator_names: tuple[str, ...] = ()):
    from src.lattices.core.integral import Lattice
    from src.lattices.core.rational import RationalLattice

    target_value_ring = base_ring if value_ring is None else value_ring
    gram_matrix = matrix(target_value_ring, gram)
    if base_ring is ZZ and target_value_ring is ZZ and gram_matrix.det() != 0:
        return Lattice.from_gram(gram_matrix, generator_names=generator_names)
    if base_ring is QQ and target_value_ring is QQ and gram_matrix.det() != 0:
        return RationalLattice.from_gram(gram_matrix, generator_names=generator_names)
    return FreeBilinearModule(base_ring, gram_matrix, value_ring=target_value_ring, generator_names=generator_names)


class FreeBilinearModule(BilinearModule):
    Element = FreeBilinearModuleElement

    def __init__(self, base_ring, gram, *, value_ring=None, generator_names: Sequence[str] = ()):
        presentation = FreeModulePresentation(
            module_ring=base_ring,
            value_ring=base_ring if value_ring is None else value_ring,
            gram=gram,
            generator_names=tuple(generator_names),
        )
        coordinate_module = presentation.module_ring ** presentation.gram.nrows()
        super().__init__(
            FGP_Module(coordinate_module, coordinate_module.zero_submodule()),
            presentation.gram,
            value_ring=presentation.value_ring,
            generator_names=presentation.generator_names,
        )
        if presentation.value_ring is presentation.module_ring:
            self._sage_module = FreeQuadraticModule(
                self.base_ring(),
                self.ngens(),
                inner_product_matrix=self.gram_matrix(),
            )

    def inner_product_matrix(self):
        return self.gram_matrix()

    def det(self):
        return self.gram_matrix().det()

    def determinant(self):
        return self.det()

    def _scalar_multiple(self, element, scalar):
        assert scalar in self.base_ring(), "Scalar multiplication on a free bilinear module requires a scalar in the base ring"
        return self.element_from(self.base_ring()(scalar) * element.to_vector())

    def __eq__(self, other):
        return (
            type(other) is type(self)
            and other.base_ring() is self.base_ring()
            and other.value_ring() is self.value_ring()
            and other.gram_matrix() == self.gram_matrix()
        )

    def __hash__(self):
        return hash((type(self), self.base_ring(), self.value_ring(), tuple(self.gram_matrix().list())))
