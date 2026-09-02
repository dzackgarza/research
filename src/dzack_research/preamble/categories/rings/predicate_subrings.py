"""Subrings specified by a membership predicate and their inclusion."""

from sage.categories.category import Category
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.structure.parent import Parent

from dzack_research.preamble.categories.rings.rings import OwnedRings
from dzack_research.preamble.refine import refine


class PredicateSubrings(Category):
    def super_categories(self):
        return [OwnedRings()]

    class ParentMethods:
        def ambient_ring(self):
            return self._ambient_ring

        def defining_predicate(self):
            return self._predicate

        def __contains__(self, element):
            if element not in self._ambient_ring:
                return False
            answer = self._predicate(element)
            if answer is True or answer is False:
                return answer
            raise NotImplementedError(
                f"membership in {self} is not decided for {element}"
            )

        def _element_constructor_(self, element):
            if element not in self:
                raise ValueError(f"{element} does not satisfy {self._description}")
            return element

        def one(self):
            return self._one

        def zero(self):
            return self._zero

        def inclusion(self):
            return SetMorphism(
                self.Hom(self._ambient_ring),
                lambda element: element,
            )

        def _repr_(self):
            return f"{{z in {self._ambient_ring} : {self._description}}}"


class _PredicateSubringParent(Parent):
    def __init__(self, ambient_ring, predicate, description, category):
        if ambient_ring not in SageRings() and ambient_ring not in OwnedRings():
            raise TypeError(f"{ambient_ring} is not a ring")
        self._ambient_ring = ambient_ring
        self._predicate = predicate
        self._description = description
        self._one = ambient_ring.one()
        self._zero = ambient_ring.zero()
        Parent.__init__(self, facade=ambient_ring, category=category)
        refine(self, category)

    def _element_constructor_(self, element):
        from dzack_research.preamble.categories.rings.rings import engine_ring

        candidate = engine_ring(self._ambient_ring)(element)
        if candidate not in self:
            raise ValueError(f"{candidate} does not satisfy {self._description}")
        return candidate

    def __contains__(self, element):
        from dzack_research.preamble.categories.rings.rings import engine_ring

        try:
            candidate = engine_ring(self._ambient_ring)(element)
        except (TypeError, ValueError):
            return False
        answer = self._predicate(candidate)
        if answer is True or answer is False:
            return answer
        raise NotImplementedError(
            f"membership in {self} is not decided for {candidate}"
        )


def predicate_subring(ambient_ring, predicate, description, category=None):
    placement = PredicateSubrings()
    if category is not None:
        placement = Category.join((placement, category))
    return _PredicateSubringParent(
        ambient_ring,
        predicate,
        description,
        placement,
    )
