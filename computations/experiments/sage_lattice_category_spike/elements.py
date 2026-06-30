r"""Elements of owned synthetic lattices."""

from __future__ import annotations

from sage.modules.free_module_element import vector
from sage.rings.rational_field import QQ
from sage.structure.element import Element


class SyntheticLatticeElement(Element):
    r"""Element of an owned synthetic lattice parent."""

    def __init__(self, parent, coordinates):
        Element.__init__(self, parent)
        coords = vector(parent.base_ring(), coordinates)
        if len(coords) != parent.rank():
            raise ValueError(
                "coordinate length must equal lattice rank; "
                f"rank={parent.rank()}, coordinates={coordinates}"
            )
        coords.set_immutable()
        self._coordinates = coords

    def _repr_(self):
        return repr(self._coordinates)

    def coordinates(self):
        return self._coordinates

    def rational_coordinates(self):
        return vector(QQ, self._coordinates) * self.parent().basis_matrix()

    def b(self, other):
        return self.parent().b(self, other)

    def q(self):
        return self.b(self)

    def _add_(self, other):
        return self.parent()(self.coordinates() + other.coordinates())

    def _sub_(self, other):
        return self.parent()(self.coordinates() - other.coordinates())

    def _neg_(self):
        return self.parent()(-self.coordinates())

    def _lmul_(self, scalar):
        return self.parent()(scalar * self.coordinates())

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticLatticeElement)
            and self.parent() == other.parent()
            and self.coordinates() == other.coordinates()
        )
