"""Prime spectra and Zariski basic subsets of commutative rings."""

from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.rings.commutative_algebra import _engine_ideal
from dzack_research.preamble.categories.rings.rings import (
    OwnedCommutativeRings,
    engine_ring,
    own_ring,
)
from dzack_research.preamble.categories.sets import PartiallyOrderedSets, SetInclusion


class PrimeIdealPoint(Element):
    r"""A point ``p in Spec(R)``, represented by its prime ideal ``p <= R``."""

    def __init__(self, parent, ideal) -> None:
        self._ideal = ideal
        Element.__init__(self, parent)

    def ideal(self):
        return self._ideal

    prime_ideal = ideal

    @cached_method
    def local_ring(self):
        return self.parent().ring().localize_at_prime(self.ideal())

    stalk = local_ring

    @cached_method
    def residue_field(self):
        return self.local_ring().residue_field()

    def specializes_to(self, other) -> bool:
        if other.parent() is not self.parent():
            raise ValueError("specialization compares points of one spectrum")
        return bool(self.ideal() <= other.ideal())

    def _richcmp_(self, other, op):
        if not isinstance(other, PrimeIdealPoint) or other.parent() is not self.parent():
            return NotImplemented
        from sage.structure.richcmp import op_EQ, op_LE, op_LT, op_NE

        if op == op_EQ:
            return self.ideal() == other.ideal()
        if op == op_NE:
            return self.ideal() != other.ideal()
        if op == op_LE:
            return self.specializes_to(other)
        if op == op_LT:
            return self.ideal() != other.ideal() and self.specializes_to(other)
        return NotImplemented

    def _repr_(self):
        return f"Point {self.ideal()} of {self.parent()}"


class ZariskiClosedSubobject(SetInclusion):
    r"""The closed subobject ``V(I) -> Spec(R)``."""

    def __init__(self, spectrum, ideal) -> None:
        self._defining_ideal = ideal
        from sage.sets.condition_set import ConditionSet

        domain = ConditionSet(
            spectrum,
            lambda point: bool(self.defining_ideal() <= point.ideal()),
        )
        SetInclusion.__init__(self, domain, spectrum)

    def defining_ideal(self):
        return self._defining_ideal

    def __contains__(self, point) -> bool:
        try:
            point = self.codomain()(point)
        except (TypeError, ValueError):
            return False
        return bool(self.defining_ideal() <= point.ideal())

    def _repr_(self):
        return f"V({self.defining_ideal()}) in {self.codomain()}"


class DistinguishedOpenSubobject(SetInclusion):
    r"""The distinguished open subobject ``D(f) -> Spec(R)``."""

    def __init__(self, spectrum, function) -> None:
        self._function = spectrum.ring()(function)
        from sage.sets.condition_set import ConditionSet

        domain = ConditionSet(
            spectrum,
            lambda point: self.function() not in point.ideal(),
        )
        SetInclusion.__init__(self, domain, spectrum)

    def function(self):
        return self._function

    def __contains__(self, point) -> bool:
        try:
            point = self.codomain()(point)
        except (TypeError, ValueError):
            return False
        return self.function() not in point.ideal()

    def coordinate_ring(self):
        return self.codomain().ring().localization(self.function())

    def _repr_(self):
        return f"D({self.function()}) in {self.codomain()}"


class PrimeSpectrum(Parent):
    Element = PrimeIdealPoint

    def __init__(self, ring) -> None:
        self._ring = own_ring(ring)
        if self._ring not in OwnedCommutativeRings():
            raise TypeError("Spec(R) requires a commutative ring")
        Parent.__init__(self, category=PartiallyOrderedSets())

    def ring(self):
        return self._ring

    coordinate_ring = ring

    def _element_constructor_(self, ideal):
        if isinstance(ideal, PrimeIdealPoint) and ideal.parent() is self:
            return ideal
        candidate = _engine_ideal(self.ring(), ideal)
        if not bool(candidate.is_prime()):
            raise ValueError(f"{candidate} is not a prime ideal of {self.ring()}")
        return self.element_class(self, candidate)

    def __contains__(self, candidate) -> bool:
        if isinstance(candidate, PrimeIdealPoint):
            return candidate.parent() is self
        try:
            ideal = _engine_ideal(self.ring(), candidate)
            return bool(ideal.is_prime())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return False

    def le(self, left, right) -> bool:
        return self(left).specializes_to(self(right))

    def closed_set(self, ideal):
        return ZariskiClosedSubobject(self, _engine_ideal(self.ring(), ideal))

    V = closed_set

    def distinguished_open(self, function):
        return DistinguishedOpenSubobject(self, function)

    D = distinguished_open

    def generic_point(self):
        engine = engine_ring(self.ring())
        zero = engine.ideal(0)
        if not bool(zero.is_prime()):
            raise ValueError(f"{self.ring()} is not integral, so Spec has no unique generic point")
        return self(zero)

    def _repr_(self):
        return f"Spec({self.ring()})"


__all__ = [
    "DistinguishedOpenSubobject",
    "PrimeIdealPoint",
    "PrimeSpectrum",
    "ZariskiClosedSubobject",
]
