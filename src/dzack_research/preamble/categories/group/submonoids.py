"""Submonoids represented as monomorphism subobjects of an ambient monoid."""

from sage.categories.monoids import Monoids as SageMonoids
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.arrow_categories import SubobjectsOf
from dzack_research.preamble.categories.group.magmas import (
    MonoidMorphism,
    Monoids,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.refine import realize_owned_category


class SubmonoidInclusion(MonoidMorphism):
    """The chosen monomorphism ``S -> M`` representing a submonoid."""

    def is_injective(self):
        return True

    def factor_through(self, target_inclusion):
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError("submonoid factorization requires one ambient monoid")
        if target_inclusion is self:
            return Monoids().Mor(self.domain(), self.domain()).identity()
        source = self.domain()
        target = target_inclusion.domain()
        try:
            generators = tuple(source.monoid_generators())
        except NotImplementedError as error:
            raise NotImplementedError(
                "submonoid containment has no represented decision procedure"
            ) from error
        if not all(generator in target for generator in generators):
            raise ValueError("the source submonoid is not contained in the target")
        return Monoids().Mor(source, target)(
            lambda element: target(element)
        )


class _SubmonoidParent(Parent):
    """A source monoid equipped with its chosen inclusion into an ambient monoid."""

    def __init__(
        self,
        ambient,
        *,
        generators=None,
        predicate=None,
        description=None,
        structure_data=None,
    ) -> None:
        if ambient not in Monoids() and ambient not in SageMonoids():
            raise TypeError(f"{ambient} is not a monoid")
        if generators is None and predicate is None:
            raise ValueError("a represented submonoid needs generators or a membership predicate")
        self._preamble_ambient_monoid = ambient
        self._preamble_defining_predicate = predicate
        self._preamble_description = description
        self._preamble_submonoid_structure_data = dict(structure_data or {})
        self._preamble_monoid_generators = (
            None if generators is None else finite_ordered_set(tuple(generators))
        )
        Parent.__init__(self, facade=ambient, category=Submonoids(ambient))
        self._preamble_inclusion = SubmonoidInclusion(
            Monoids().Mor(self, ambient),
            lambda element: element,
        )
        realize_owned_category(self)
        if predicate is not None and not bool(predicate(ambient.one())):
            raise ValueError("a submonoid must contain the ambient multiplicative identity")

    def ambient_monoid(self):
        return self._preamble_ambient_monoid

    supermonoid = ambient_monoid

    def inclusion(self):
        return self._preamble_inclusion

    def structure_data(self):
        return dict(self._preamble_submonoid_structure_data)

    def defining_predicate(self):
        if self._preamble_defining_predicate is None:
            raise NotImplementedError(
                "this submonoid is represented by generators, not a membership predicate"
            )
        return self._preamble_defining_predicate

    def monoid_generators(self):
        if self._preamble_monoid_generators is None:
            raise NotImplementedError("this submonoid has no chosen generating set")
        return self._preamble_monoid_generators


    def one(self):
        return self.ambient_monoid().one()

    def _normalize(self, datum):
        ambient = self.ambient_monoid()
        if getattr(datum, "parent", lambda: None)() is ambient:
            return datum
        return ambient(datum)

    def __contains__(self, datum):
        try:
            element = self._normalize(datum)
        except (TypeError, ValueError):
            return False
        if self._preamble_defining_predicate is not None:
            return bool(self._preamble_defining_predicate(element))
        if element == self.one():
            return True
        generators = tuple(self._preamble_monoid_generators)
        if any(element == generator for generator in generators):
            return True
        raise NotImplementedError(
            "membership in this generated submonoid has no active decision procedure"
        )

    def _element_constructor_(self, datum):
        element = self._normalize(datum)
        answer = element in self
        if answer is not True:
            raise ValueError(f"{element} is not in {self}")
        return element

    def _repr_(self):
        if self._preamble_description is not None:
            return self._preamble_description
        return f"Submonoid of {self.ambient_monoid()}"


def Submonoids(ambient_monoid):
    """Return the generic subobject category of submonoids of ``ambient_monoid``."""
    return SubobjectsOf(Monoids(), ambient_monoid)


def generated_submonoid(ambient, generators, *, description=None, structure_data=None):
    normalized = tuple(ambient(generator) for generator in generators)
    return _SubmonoidParent(
        ambient,
        generators=normalized,
        description=description,
        structure_data=structure_data,
    )


def predicate_submonoid(
    ambient,
    predicate,
    description,
    *,
    structure_data=None,
):
    return _SubmonoidParent(
        ambient,
        predicate=predicate,
        description=description,
        structure_data=structure_data,
    )


__all__ = [
    "SubmonoidInclusion",
    "Submonoids",
    "generated_submonoid",
    "predicate_submonoid",
]
