from __future__ import annotations

from typing import TYPE_CHECKING

from sage.all import QQ, ZZ, Integer, vector
from sage.structure.element_wrapper import ElementWrapper

if TYPE_CHECKING:
    from src.lattices.core.abstract import BilinearModule


class FreeBilinearModuleElement(ElementWrapper):
    def __init__(self, parent: BilinearModule, sage_element):
        module = parent._module_like()
        if type(sage_element) is module.element_class and sage_element.parent() is module:
            ElementWrapper.__init__(self, parent, sage_element)
            return
        ElementWrapper.__init__(self, parent, module(sage_element))

    def _sage_like(self):
        return self.value

    def to_vector(self):
        if self.parent().base_ring().is_field():
            return vector(self.parent().base_ring(), self.value)
        return self.value.vector()

    def to_coordinates(self):
        return self.to_vector()

    def to_primal_coordinates(self):
        return vector(QQ, self.to_vector())

    def bilinear_product_with(self, other):
        assert type(other) is type(self) and other.parent() is self.parent(), (
            "Bilinear products are defined only for elements of a fixed parent"
        )
        return (self.to_vector() * self.parent().gram_matrix() * other.to_vector().column())[0]

    def inner_product(self, other):
        return self.bilinear_product_with(other)

    def q(self):
        return self * self

    def is_isotropic(self):
        return self.q().is_zero()

    def span(self):
        return self.parent().span((self,))

    def perp(self):
        return self.parent().orthogonal_submodule_to((self,))

    def __iter__(self):
        return iter(self.to_vector())

    def __len__(self):
        return len(self.to_vector())

    def __getitem__(self, index):
        return self.to_vector()[index]

    def __neg__(self):
        return self.parent()._wrap_element(-self.value)

    def __add__(self, other):
        assert type(other) is type(self) and other.parent() is self.parent(), (
            "Addition is defined only for elements of a fixed parent"
        )
        return self.parent()._wrap_element(self.value + other.value)

    def __sub__(self, other):
        assert type(other) is type(self) and other.parent() is self.parent(), (
            "Subtraction is defined only for elements of a fixed parent"
        )
        return self.parent()._wrap_element(self.value - other.value)

    def __mul__(self, other):
        if type(other) is type(self) and other.parent() is self.parent():
            return self.bilinear_product_with(other)
        return self.parent()._scalar_multiple(self, other)

    def __rmul__(self, scalar):
        return self.parent()._scalar_multiple(self, scalar)

    def __truediv__(self, scalar):
        return self.parent()._scalar_multiple(self, QQ.one() / QQ(scalar))

    def __eq__(self, other):
        return type(other) is type(self) and self.parent() is other.parent() and self.to_vector() == other.to_vector()

    def __hash__(self):
        return hash((id(self.parent()), tuple(self.to_vector())))

    def __repr__(self):
        pieces = []
        for coefficient, name in zip(self.to_vector(), self.parent().generator_names(), strict=True):
            if coefficient == 0:
                continue
            if coefficient == 1:
                pieces.append(name)
                continue
            if coefficient == -1:
                pieces.append(f"-{name}")
                continue
            pieces.append(f"{coefficient}*{name}")
        if not pieces:
            return "0"
        rendered = pieces[0]
        for piece in pieces[1:]:
            if piece.startswith("-"):
                rendered = f"{rendered} - {piece[1:]}"
                continue
            rendered = f"{rendered} + {piece}"
        return rendered


class RationalLatticeElement(FreeBilinearModuleElement): ...


class DualLatticeElement(RationalLatticeElement):
    def to_primal_coordinates(self):
        return self.parent().primal_coordinates_of(self)

    def discriminant_class(self):
        return self.parent().discriminant_class_of(self)


class LatticeElement(RationalLatticeElement):
    def to_vector(self):
        return vector(ZZ, [Integer(entry) for entry in super().to_vector()])

    def to_primal_coordinates(self):
        return vector(QQ, self.to_vector())

    def divisibility(self):
        pairings = tuple(self * generator for generator in self.parent().gens())
        ideal = ZZ.ideal(pairings)
        assert len(ideal.gens()) == 1, "Divisibility ideal in ZZ must be principal"
        return ideal.gens()[0]

    def is_primitive(self):
        ideal = ZZ.ideal(tuple(Integer(entry) for entry in self.to_vector()))
        assert len(ideal.gens()) == 1, "Coordinate ideal in ZZ must be principal"
        return ideal.gens()[0] == 1

    def discriminant_class(self):
        return self.parent().discriminant_group().zero()
