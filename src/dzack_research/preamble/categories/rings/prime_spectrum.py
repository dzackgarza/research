"""Prime spectra and Zariski basic subsets of commutative rings."""

from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.rings.commutative_algebra import (
    _engine_ideal,
    _owned_ideal,
)
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

    @cached_method
    def residue_map(self):
        r"""Return the canonical map ``R -> kappa(p)`` attached to this point."""
        local = self.local_ring()
        selected = getattr(local, "_preamble_source_residue_map", None)
        if selected is not None:
            return selected
        return local.residue_map() * local.localization_map()

    def specializes_to(self, other) -> bool:
        if other.parent() is not self.parent():
            raise ValueError("specialization compares points of one spectrum")
        ring = self.parent().ring()
        return bool(_engine_ideal(ring, self.ideal()) <= _engine_ideal(ring, other.ideal()))

    def _richcmp_(self, other, op):
        if not isinstance(other, PrimeIdealPoint) or other.parent() is not self.parent():
            return NotImplemented
        from sage.structure.richcmp import op_EQ, op_LE, op_LT, op_NE

        ring = self.parent().ring()
        left_ideal = _engine_ideal(ring, self.ideal())
        right_ideal = _engine_ideal(ring, other.ideal())
        if op == op_EQ:
            return left_ideal == right_ideal
        if op == op_NE:
            return left_ideal != right_ideal
        if op == op_LE:
            return self.specializes_to(other)
        if op == op_LT:
            return left_ideal != right_ideal and self.specializes_to(other)
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
            lambda point: bool(
                _engine_ideal(spectrum.ring(), self.defining_ideal())
                <= _engine_ideal(spectrum.ring(), point.ideal())
            ),
        )
        SetInclusion.__init__(self, domain, spectrum)

    def defining_ideal(self):
        return self._defining_ideal

    def __contains__(self, point) -> bool:
        try:
            point = self.codomain()(point)
        except (TypeError, ValueError):
            return False
        ring = self.codomain().ring()
        return bool(
            _engine_ideal(ring, self.defining_ideal())
            <= _engine_ideal(ring, point.ideal())
        )

    def _repr_(self):
        return f"V({self.defining_ideal()}) in {self.codomain()}"


class DistinguishedOpenSubobject(SetInclusion):
    r"""The distinguished open subobject ``D(f) -> Spec(R)``."""

    def __init__(self, spectrum, function) -> None:
        self._function = spectrum.ring()(function)
        from sage.sets.condition_set import ConditionSet

        domain = ConditionSet(
            spectrum,
            lambda point: engine_ring(spectrum.ring())(self.function())
            not in _engine_ideal(spectrum.ring(), point.ideal()),
        )
        SetInclusion.__init__(self, domain, spectrum)

    def function(self):
        return self._function

    def __contains__(self, point) -> bool:
        try:
            point = self.codomain()(point)
        except (TypeError, ValueError):
            return False
        ring = self.codomain().ring()
        return engine_ring(ring)(self.function()) not in _engine_ideal(ring, point.ideal())

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

    def __call__(self, ideal):
        r"""Construct a prime point directly from its represented ideal."""
        return self._element_constructor_(ideal)

    def _element_constructor_(self, ideal):
        if isinstance(ideal, PrimeIdealPoint) and ideal.parent() is self:
            return ideal
        candidate = _engine_ideal(self.ring(), ideal)
        if not bool(candidate.is_prime()):
            raise ValueError(f"{candidate} is not a prime ideal of {self.ring()}")
        return self.element_class(self, _owned_ideal(self.ring(), candidate))

    def __contains__(self, candidate) -> bool:
        if isinstance(candidate, PrimeIdealPoint):
            return candidate.parent() is self
        try:
            ideal = _engine_ideal(self.ring(), candidate)
            return bool(ideal.is_prime())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            return False

    def le(self, left, right) -> bool:
        return self._element_constructor_(left).specializes_to(
            self._element_constructor_(right)
        )

    def closed_set(self, ideal):
        return ZariskiClosedSubobject(self, _owned_ideal(self.ring(), ideal))

    V = closed_set

    def distinguished_open(self, function):
        return DistinguishedOpenSubobject(self, function)

    D = distinguished_open

    def generic_point(self):
        engine = engine_ring(self.ring())
        zero = engine.ideal(0)
        if not bool(zero.is_prime()):
            raise ValueError(f"{self.ring()} is not integral, so Spec has no unique generic point")
        return self._element_constructor_(zero)

    def _repr_(self):
        return f"Spec({self.ring()})"


__all__ = [
    "DistinguishedOpenSubobject",
    "PrimeIdealPoint",
    "PrimeSpectrum",
    "ZariskiClosedSubobject",
]
