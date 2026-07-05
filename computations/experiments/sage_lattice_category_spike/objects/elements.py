r"""Elements of owned synthetic lattices."""

from __future__ import annotations

from sage.modules.free_module_element import vector
from sage.rings.rational_field import QQ
from sage.structure.element import Element

from ..algebra.domain_algebra import LatticeElement as ElementCarrier


class SyntheticLatticeElement(ElementCarrier, Element):
    r"""Element of an owned synthetic lattice parent."""

    def __init__(self, parent, coordinates):
        Element.__init__(self, parent)
        coords = vector(parent.base_ring(), coordinates)
        assert len(coords) == parent.rank(), (
            "coordinate length must equal lattice rank; "
            f"rank={parent.rank()}, coordinates={coordinates}; fix the caller's coordinates"
        )
        coords.set_immutable()
        self._coordinates = coords

    def parent(self):
        return Element.parent(self)

    def _repr_(self):
        return repr(self._coordinates)

    def coefficient_vector(self):
        return self._coordinates

    def rational_coordinates(self):
        r"""This element's coordinates in the root parent's intrinsic basis."""
        return vector(QQ, self._coordinates) * self.parent()._inclusion_rows()

    def b(self, other):
        return self.parent().b(self, other)

    def q(self):
        return self.b(self)

    def _add_(self, other):
        return self.parent()(self.coefficient_vector() + other.coefficient_vector())

    def _sub_(self, other):
        return self.parent()(self.coefficient_vector() - other.coefficient_vector())

    def _neg_(self):
        return self.parent()(-self.coefficient_vector())

    def _lmul_(self, scalar):
        return self.parent()(scalar * self.coefficient_vector())

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticLatticeElement)
            and self.parent() == other.parent()
            and self.coefficient_vector() == other.coefficient_vector()
        )
