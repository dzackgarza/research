from __future__ import annotations

from collections.abc import Sequence
from functools import reduce

from sage.all import QQ, ZZ, Integer, block_diagonal_matrix, identity_matrix, matrix, zero_matrix
from sage.structure.parent import Parent
from src.lattices.categories.bilinear_modules import BilinearModules
from src.lattices.validation.presentations import BilinearModulePresentation, CoordinatePresentation


class BilinearForm:
    def __init__(self, domain: BilinearModule):
        self._domain = domain

    def domain(self) -> BilinearModule:
        return self._domain

    def codomain(self):
        return self._domain.value_ring()

    def __call__(self, left, right):
        return self._domain.b(left, right)

    def __repr__(self):
        return f"BilinearForm({self.domain()!r})"


class BilinearModule(Parent):
    def __init__(self, module, gram, *, value_ring, generator_names: Sequence[str] = ()):
        presentation = BilinearModulePresentation(
            module=module,
            value_ring=value_ring,
            gram=gram,
            generator_names=tuple(generator_names),
        )
        self._module = presentation.module
        self._value_ring = presentation.value_ring
        self._gram = presentation.gram
        self._generator_names = presentation.generator_names
        self._summands = ()
        self._embeddings = ()
        self._ambient = None
        self._ambient_generators = ()
        self._ambient_submodule = None
        Parent.__init__(self, category=BilinearModules(self.base_ring()))

    def base_ring(self):
        return self._module.V().base_ring()

    def value_ring(self):
        return self._value_ring

    @classmethod
    def from_presented_module(cls, module, gram, *, value_ring, generator_names: Sequence[str] = ()):
        from src.lattices.core.free import FreeBilinearModule
        from src.lattices.core.integral import Lattice
        from src.lattices.core.rational import RationalLattice
        from src.lattices.core.torsion import TorsionBilinearModule

        gram_matrix = matrix(value_ring, gram)
        if module.V().base_ring().is_field():
            invariants = module.ngens() * (Integer(0),)
        else:
            invariants = tuple(Integer(invariant) for invariant in module.invariants())
        if all(invariant == 0 for invariant in invariants):
            base_ring = module.V().base_ring()
            if value_ring is ZZ and base_ring is ZZ and (gram_matrix.nrows() == 0 or gram_matrix.det() != 0):
                return Lattice.from_gram(matrix(ZZ, gram_matrix), generator_names=tuple(generator_names))
            if value_ring is QQ and base_ring is QQ and (gram_matrix.nrows() == 0 or gram_matrix.det() != 0):
                return RationalLattice.from_gram(matrix(QQ, gram_matrix), generator_names=tuple(generator_names))
            return FreeBilinearModule(base_ring, gram_matrix, value_ring=value_ring, generator_names=tuple(generator_names))
        if all(invariant != 0 for invariant in invariants):
            return TorsionBilinearModule(module, gram_matrix, value_ring=value_ring, generator_names=tuple(generator_names))
        return cls(module, gram_matrix, value_ring=value_ring, generator_names=tuple(generator_names))

    def rank(self) -> int:
        return sum(invariant == 0 for invariant in self.invariants())

    def ngens(self) -> int:
        return len(self._generator_names)

    def gram_matrix(self):
        return self._gram

    def invariants(self) -> tuple[Integer, ...]:
        if self.base_ring().is_field():
            return self.ngens() * (Integer(0),)
        return tuple(Integer(invariant) for invariant in self._module.invariants())

    def has_free_part(self) -> bool:
        return any(invariant == 0 for invariant in self.invariants())

    def has_torsion_part(self) -> bool:
        return any(invariant != 0 for invariant in self.invariants())

    def is_torsionfree(self) -> bool:
        return not self.has_torsion_part()

    def is_nondegenerate(self) -> bool:
        return self.ngens() == 0 or self.gram_matrix().det() != 0

    def gens(self):
        return tuple(self._wrap_element(generator) for generator in self._module.gens())

    def element_from(self, coordinates):
        presentation = CoordinatePresentation(
            module_ring=self.base_ring(),
            rank=self.ngens(),
            coordinates=coordinates,
        )
        return self._wrap_element(self._module(presentation.coordinates))

    def generator_names(self) -> tuple[str, ...]:
        return self._generator_names

    def coordinate_module(self):
        return self._module.V()

    def relation_module(self):
        return self._module.W()

    def gen(self, index: int):
        return self.gens()[index]

    def basis(self):
        return self.gens()

    def __call__(self, coordinates):
        if type(coordinates) is self._element_cls() and coordinates.parent() is self:
            return coordinates
        return self.element_from(coordinates)

    def b(self, left, right):
        return self(left).inner_product(self(right))

    def hom(self, codomain):
        return self.Hom(codomain)

    def bilinear_form(self) -> BilinearForm:
        return BilinearForm(self)

    def twist(self, scalar):
        scale = QQ(scalar)
        value_ring = QQ if self.value_ring() is QQ or not scale.denominator().is_one() else self.value_ring()
        return BilinearModule.from_presented_module(
            self._module_like(),
            matrix(value_ring, scale * self.gram_matrix()),
            value_ring=value_ring,
            generator_names=self.generator_names(),
        )

    def rescale(self, scalar):
        return self.twist(scalar)

    def submodule(self, generators):
        generator_tuple = tuple(self(generator) for generator in generators)
        sage_generators = tuple(generator._sage_like() for generator in generator_tuple)
        submodule = self._module_like().submodule(sage_generators)
        return self._wrap_sage_submodule(submodule)

    def _wrap_sage_submodule(self, submodule):
        submodule_generators = tuple(self.element_from(generator.lift()) for generator in submodule.gens())
        if not submodule_generators:
            submodule_gram = matrix(self.value_ring(), 0, 0)
        else:
            submodule_gram = matrix(
                self.value_ring(),
                [[left.inner_product(right) for right in submodule_generators] for left in submodule_generators],
            )
        wrapped = BilinearModule.from_presented_module(submodule, submodule_gram, value_ring=self.value_ring())
        wrapped._ambient = self
        wrapped._ambient_generators = submodule_generators
        wrapped._ambient_submodule = submodule
        return wrapped

    def span(self, generators):
        return self.submodule(generators)

    def quotient_by(self, submodule):
        ambient_submodule = (
            submodule._ambient_submodule
            if isinstance(submodule, BilinearModule) and submodule._ambient is self and submodule._ambient_submodule is not None
            else submodule._module_like()
        )
        quotient = self._module_like() / ambient_submodule
        return self._wrap_sage_quotient(quotient)

    def _wrap_sage_quotient(self, quotient):
        quotient_generators = tuple(quotient.gens())
        if not quotient_generators:
            quotient_gram = matrix(self.value_ring(), 0, 0)
        else:
            quotient_gram = matrix(
                self.value_ring(),
                [
                    [
                        self.element_from(left.lift()).inner_product(self.element_from(right.lift()))
                        for right in quotient_generators
                    ]
                    for left in quotient_generators
                ],
            )
        return BilinearModule.from_presented_module(quotient, quotient_gram, value_ring=self.value_ring())

    def orthogonal_submodule_to(self, elements):
        generators = tuple(self(generator) for generator in elements)
        if not generators:
            return self
        pairing_rows = matrix(self.value_ring(), [generator.to_vector() * self.gram_matrix() for generator in generators])
        kernel_basis = pairing_rows.right_kernel().basis_matrix()
        return self.submodule(tuple(self.element_from(row) for row in kernel_basis.rows()))

    def perp(self):
        assert self._ambient is not None, "Orthogonal complements are defined for subobjects in a fixed ambient bilinear module"
        return self._ambient.orthogonal_submodule_to(self._ambient_generators)

    def __add__(self, other):
        value_ring = QQ if self.value_ring() is QQ or other.value_ring() is QQ else self.value_ring()
        gram = matrix(
            value_ring,
            block_diagonal_matrix(
                [matrix(value_ring, self.gram_matrix()), matrix(value_ring, other.gram_matrix())],
                subdivide=False,
            ),
        )
        coordinate_module = self.coordinate_module().direct_sum(other.coordinate_module())
        relation_module = self.relation_module().direct_sum(other.relation_module())
        direct_sum = BilinearModule.from_presented_module(coordinate_module / relation_module, gram, value_ring=value_ring)
        direct_sum._install_direct_sum_structure(self, other)
        return direct_sum

    def __pow__(self, exponent: int):
        exponent = int(exponent)
        assert exponent >= 1, "Direct-sum powers require a positive exponent"
        return reduce(lambda left, right: left + right, exponent * [self])

    def __contains__(self, value):
        return type(value) is self._element_cls() and value.parent() is self

    def _wrap_element(self, element):
        return self._element_cls()(self, element)

    def _install_direct_sum_structure(self, left, right):
        left_columns = left.ngens()
        left_rows = left_columns
        right_columns = right.ngens()
        module_ring = self.base_ring()
        left_matrix = identity_matrix(module_ring, left_columns).stack(zero_matrix(module_ring, right_columns, left_columns))
        right_matrix = zero_matrix(module_ring, left_rows, right_columns).stack(identity_matrix(module_ring, right_columns))
        left_embedding = left.hom(self).element_from_matrix(left_matrix)
        right_embedding = right.hom(self).element_from_matrix(right_matrix)
        self._summands = (left_embedding.image(), right_embedding.image())
        self._embeddings = (left_embedding, right_embedding)

    @property
    def summands(self):
        return self._summands

    @property
    def embeddings(self):
        return self._embeddings

    def _sage_like(self):
        return self._module

    def _module_like(self):
        return self._module

    def _element_cls(self):
        from src.lattices.core.elements import FreeBilinearModuleElement

        return getattr(type(self), "Element", FreeBilinearModuleElement)

    def __repr__(self):
        return f"{type(self).__name__}(invariants={self.invariants()!r}, gram={self.gram_matrix()!r})"


class QuadraticModule:
    def q(self, value):
        return self(value) * self(value)


class _TorsionBilinearModulesCategory:
    def __contains__(self, value):
        from src.lattices.core.torsion import TorsionBilinearModule

        return isinstance(value, TorsionBilinearModule)

    def __repr__(self):
        return "TorsionBilinearModules"


TorsionBilinearModules = _TorsionBilinearModulesCategory()
