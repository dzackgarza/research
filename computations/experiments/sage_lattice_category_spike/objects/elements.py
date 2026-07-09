r"""Elements of owned synthetic lattices."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, cast

from sage.modules.free_module_element import vector
from sage.rings.rational_field import QQ
from sage.structure.element import Element, RingElement

from ..lexicon import ExactScalar, LatticeElement, Vector

if TYPE_CHECKING:
    from .parents import SyntheticLattice


class SyntheticLatticeElement(LatticeElement, Element):
    r"""Element of an owned synthetic lattice parent."""

    def __init__(self, parent: SyntheticLattice, coordinates: Sequence[ExactScalar] | Vector | SyntheticLatticeElement) -> None:
        Element.__init__(self, parent)
        if isinstance(coordinates, SyntheticLatticeElement):
            coordinates = coordinates.coefficient_vector()
        coords: Vector = vector(parent.base_ring(), coordinates)
        assert len(coords) == parent.rank(), f"coordinate length must equal lattice rank; rank={parent.rank()}, coordinates={coordinates}; fix the caller's coordinates"
        coords.set_immutable()
        self._coordinates = coords

    def parent(self) -> SyntheticLattice:
        return cast("SyntheticLattice", Element.parent(self))

    def coefficient_vector(self) -> Vector:
        return self._coordinates

    def rational_coordinates(self) -> Vector:
        r"""This element's coordinates in the root parent's intrinsic basis."""
        return vector(QQ, self._coordinates) * self.parent()._inclusion_rows()

    def b(self, other: LatticeElement) -> ExactScalar:
        return self.parent().b(self, other)

    def q(self) -> ExactScalar:
        return self.b(self)

    def _add_(self, other: SyntheticLatticeElement) -> SyntheticLatticeElement:
        return self.parent()(self.coefficient_vector() + other.coefficient_vector())

    def _sub_(self, other: SyntheticLatticeElement) -> SyntheticLatticeElement:
        return self.parent()(self.coefficient_vector() - other.coefficient_vector())

    def _neg_(self) -> SyntheticLatticeElement:
        return self.parent()(-self.coefficient_vector())

    def _lmul_(self, scalar: RingElement) -> SyntheticLatticeElement:
        return self.parent()(scalar * self.coefficient_vector())

    def __mul__(self, other: SyntheticLatticeElement | RingElement) -> SyntheticLatticeElement | ExactScalar:
        r"""``v * w`` = bilinear pairing (same parent); ``s * v`` = scalar action.

        For ``s ∈ R``: the R-module action, result in M.
        For ``s ∈ S`` with ``R → S``: base change to ``M ⊗_R S``, then S-action.
        """
        assert isinstance(other, (SyntheticLatticeElement, RingElement)), (
            f"unsupported operand for *: expected SyntheticLatticeElement or RingElement, got {type(other).__name__}"
        )
        R = self.parent().base_ring()
        match other:
            case SyntheticLatticeElement() if self.parent() is other.parent():
                return self.parent().b(self, other)
            case SyntheticLatticeElement():
                assert False, "different-parent lattice element; use the isometry/hom API"
            case RingElement() if other in R:
                return self._lmul_(other)
            case RingElement() as s if s.parent().coerce_map_from(R) is not None:
                base_changed = self.parent().base_extend(s.parent())
                return base_changed(s * self.coefficient_vector())
            case _:
                assert False, f"scalar has no coercion from the base ring; scalar={other}, scalar_ring={other.parent()}, base_ring={R}"
