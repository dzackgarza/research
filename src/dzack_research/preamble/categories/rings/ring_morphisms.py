"""Owned morphisms of rings with optional private engine realizations."""

from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.sets import Sets


class RingMorphism(Morphism):
    r"""A unital ring morphism in the owned ring category."""

    def __init__(self, parent, function, *, engine_morphism=None) -> None:
        Morphism.__init__(self, parent)
        if not callable(function):
            raise TypeError("a ring morphism requires an exact element map")
        self._function = function
        self._engine_morphism = engine_morphism

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        return self.codomain()(self._function(self.domain()(element)))

    def engine_morphism(self):
        if self._engine_morphism is None:
            raise NotImplementedError("this ring morphism has no selected engine realization")
        return self._engine_morphism

    def __mul__(self, other):
        if not isinstance(other, RingMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        return ring_homset(other.domain(), self.codomain()).elementwise(
            lambda element: self(other(element)),
        )

    def compose(self, before):
        result = self * before
        if result is NotImplemented:
            raise ValueError("the ring morphisms are not composable")
        return result


class RingHomset(Homset):
    r"""The owned set ``Hom_Ring(A,B)``."""

    Element = RingMorphism

    def __init__(self, domain, codomain) -> None:
        Homset.__init__(self, domain, codomain, category=Sets())

    def __call__(self, datum):
        return self._element_constructor_(datum)

    def is_endomorphism_set(self):
        return self.domain() is self.codomain()

    def _element_constructor_(self, datum):
        if isinstance(datum, RingMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the ring morphism has the wrong source or target")
            if datum.parent() is self:
                return datum
            return self.elementwise(datum)
        if isinstance(datum, Map):
            from dzack_research.preamble.categories.rings import engine_ring

            source_engine = engine_ring(self.domain())
            target_engine = engine_ring(self.codomain())
            if engine_ring(datum.domain()) is not source_engine:
                raise ValueError("the engine ring map has the wrong domain")
            if engine_ring(datum.codomain()) is not target_engine:
                raise ValueError("the engine ring map has the wrong codomain")
            return self.element_class(
                self,
                lambda element: target_engine(datum(source_engine(element))),
                engine_morphism=datum,
            )
        if callable(datum):
            return self.elementwise(datum)
        raise TypeError("a ring morphism is supplied by an exact map or engine morphism")

    def elementwise(self, function):
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on a ring endomorphism Hom-set")
        return self.elementwise(lambda element: element)

    def _repr_(self):
        return f"Hom_Ring({self.domain()}, {self.codomain()})"


def ring_homset(domain, codomain) -> RingHomset:
    r"""Return the owned Hom-set of unital ring morphisms ``domain -> codomain``."""
    return RingHomset(domain, codomain)


def ring_morphism(domain, codomain, function, *, engine_morphism=None) -> RingMorphism:
    r"""Construct one owned ring morphism with an optional engine realization."""
    return RingMorphism(
        ring_homset(domain, codomain),
        function,
        engine_morphism=engine_morphism,
    )


__all__ = ["RingHomset", "RingMorphism", "ring_homset", "ring_morphism"]
