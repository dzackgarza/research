from __future__ import annotations

from collections.abc import Sequence

from sage.all import ZZ, Integer
from src.lattices.core.abstract import BilinearModule
from src.lattices.core.elements import FreeBilinearModuleElement


class TorsionBilinearModule(BilinearModule):
    Element = FreeBilinearModuleElement

    def __init__(self, module, gram, *, value_ring, generator_names: Sequence[str] = ()):
        super().__init__(module, gram, value_ring=value_ring, generator_names=generator_names)
        assert not self.has_free_part(), "Torsion bilinear modules must have trivial free part"

    @classmethod
    def from_invariants_and_gram(cls, invariants: Sequence[int], gram, *, generator_names: Sequence[str] = ()):
        ambient = ZZ ** len(tuple(invariants))
        relation_generators = [
            Integer(invariant) * ambient.gen(index)
            for index, invariant in enumerate(tuple(Integer(invariant) for invariant in invariants))
        ]
        relation_module = ambient.span(relation_generators)
        return cls(
            ambient / relation_module,
            gram,
            value_ring=ZZ,
            generator_names=tuple(generator_names),
        )

    def invariants(self) -> tuple[Integer, ...]:
        return tuple(invariant for invariant in super().invariants() if invariant != 0)

    def _scalar_multiple(self, element, scalar):
        return self.element_from(self.base_ring()(scalar) * element.to_vector())

    def __eq__(self, other):
        return type(other) is type(self) and other.base_ring() == self.base_ring() and other.gram_matrix() == self.gram_matrix()

    def __hash__(self):
        return hash((type(self), self.base_ring(), tuple(self.gram_matrix().list())))
