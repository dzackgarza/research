"""Submonoids represented as monomorphism subobjects of an ambient monoid."""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.group.magmas import (
    MonoidMorphism,
    Monoids,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category import _object_of


class SubmonoidInclusion(MonoidMorphism):
    """The chosen monomorphism ``S -> M`` representing a submonoid."""

    def is_injective(self):
        return True

    def factor_through(self, target_inclusion):
        factor = self.factor_through_or_none(target_inclusion)
        if factor is None:
            raise ValueError(
                f"{self.domain()} is not contained in {target_inclusion.domain()}: "
                f"some monoid generator of {self.domain()} does not lie in "
                f"{target_inclusion.domain()}"
            )
        return factor

    def factor_through_or_none(self, target_inclusion):
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError(
                f"cannot factor {self.domain()} through {target_inclusion.domain()}: they are "
                f"submonoids of different monoids, {self.codomain()} and "
                f"{target_inclusion.codomain()}"
            )
        if target_inclusion is self:
            return Monoids().Mor(self.domain(), self.domain()).identity()
        source = self.domain()
        target = target_inclusion.domain()
        generators = tuple(source.monoid_generators())
        if not all(generator in target for generator in generators):
            return None
        return Monoids().Mor(source, target)(
            lambda element: target(element)
        )


class _SubmonoidEngine:
    """A source monoid equipped with its chosen inclusion into an ambient monoid."""

    def __init__(
        self,
        ambient,
        *,
        generators=None,
        predicate=None,
        description=None,
        structure_data=None,
        **rest,
    ) -> None:
        if ambient not in Monoids():
            raise TypeError(
                f"cannot form a submonoid of {ambient}: it is not a monoid, "
                f"only known to be in {ambient.category()}"
            )
        if generators is None and predicate is None:
            raise ValueError(
                f"cannot form a submonoid of {ambient}: give monoid generators "
                f"or a membership predicate"
            )
        self._ambient_monoid = ambient
        self._defining_predicate = predicate
        self._description = description
        self._submonoid_structure_data = dict(structure_data or {})
        self._monoid_generators = (
            None if generators is None else finite_ordered_set(tuple(generators))
        )
        super().__init__(facade=ambient, **rest)
        if predicate is not None and not bool(predicate(ambient.one())):
            raise ValueError(
                f"the predicate {description or predicate} does not define a submonoid of "
                f"{ambient}: the identity {ambient.one()} does not satisfy it"
            )

    def ambient_monoid(self):
        return self._ambient_monoid

    supermonoid = ambient_monoid

    @cached_method
    def inclusion(self):
        return SubmonoidInclusion(
            Monoids().Mor(self, self.ambient_monoid()), lambda element: element
        )

    def _structure_data(self):
        r"""Return private constructor metadata for localization adapters."""
        return dict(self._submonoid_structure_data)

    def _selected_representation_kind(self):
        r"""Return the representation selected when this submonoid was built.

        Protected construction contract for localization adapters.  A
        predicate-presented submonoid has exact membership by that predicate;
        otherwise the constructor retained a chosen finite generating family.
        Consumers use this datum instead of attempting one representation and
        selecting another when it raises.
        """
        if self._defining_predicate is not None:
            return "predicate"
        return "generators"

    def defining_predicate(self):
        assert self._defining_predicate is not None, (
            f"the submonoid {self} was defined by monoid generators, not by a membership "
            f"predicate, so it has no defining predicate"
        )
        return self._defining_predicate

    def monoid_generators(self):
        assert self._monoid_generators is not None, (
            f"the submonoid {self} was defined by a membership predicate, not by monoid "
            f"generators, so it has no chosen generating set"
        )
        return self._monoid_generators


    def one(self):
        return self.ambient_monoid().one()

    def _normalize(self, datum):
        ambient = self.ambient_monoid()
        assert datum in ambient, (
            f"{datum} cannot be an element of the submonoid {self}: it is not an element "
            f"of the monoid {ambient}"
        )
        return ambient(datum)

    def __contains__(self, datum):
        ambient = self.ambient_monoid()
        match datum:
            case _ if datum not in ambient:
                return False
            case _:
                element = ambient(datum)
        if self._defining_predicate is not None:
            return bool(self._defining_predicate(element))
        if element == self.one():
            return True
        generators = tuple(self._monoid_generators)
        is_selected_generator = any(element == generator for generator in generators)
        assert is_selected_generator, (
            f"cannot decide whether {element} lies in the submonoid {self} of {ambient}: "
            f"it is neither the identity nor a monoid generator, and no algorithm for "
            f"membership in a finitely generated submonoid is available"
        )
        return True

    def _element_constructor_(self, datum):
        element = self._normalize(datum)
        answer = element in self
        if answer is not True:
            raise ValueError(f"{element} is not in {self}")
        return element

    def _repr_(self):
        if self._description is not None:
            return self._description
        return f"Submonoid of {self.ambient_monoid()}"


def _generated_submonoid(ambient, generators, *, description=None, structure_data=None):
    normalized = tuple(ambient(generator) for generator in generators)
    category = Monoids().Subobjects(ambient)
    return _object_of(
        category,
        _engine=(category, _SubmonoidEngine, None),
        ambient=ambient,
        generators=normalized,
        description=description,
        structure_data=structure_data,
    )


def _predicate_submonoid(
    ambient,
    predicate,
    description,
    *,
    placements=(),
    structure_data=None,
):
    category = Category.join((Monoids().Subobjects(ambient), *placements))
    return _object_of(
        category,
        _engine=(category, _SubmonoidEngine, None),
        ambient=ambient,
        predicate=predicate,
        description=description,
        structure_data=structure_data,
    )


__all__ = [
    "SubmonoidInclusion",
]
