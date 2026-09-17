"""Submonoids represented as monomorphism subobjects of an ambient monoid."""

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
            raise ValueError("the source submonoid is not contained in the target")
        return factor

    def factor_through_or_none(self, target_inclusion):
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError("submonoid factorization requires one ambient monoid")
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
            raise TypeError(f"{ambient} is not an owned monoid")
        if generators is None and predicate is None:
            raise ValueError("a represented submonoid needs generators or a membership predicate")
        self._preamble_ambient_monoid = ambient
        self._preamble_defining_predicate = predicate
        self._preamble_description = description
        self._preamble_submonoid_structure_data = dict(structure_data or {})
        self._preamble_monoid_generators = (
            None if generators is None else finite_ordered_set(tuple(generators))
        )
        super().__init__(facade=ambient, **rest)
        if predicate is not None and not bool(predicate(ambient.one())):
            raise ValueError("a submonoid must contain the ambient multiplicative identity")

    def ambient_monoid(self):
        return self._preamble_ambient_monoid

    supermonoid = ambient_monoid

    @cached_method
    def inclusion(self):
        return SubmonoidInclusion(
            Monoids().Mor(self, self.ambient_monoid()), lambda element: element
        )

    def structure_data(self):
        return dict(self._preamble_submonoid_structure_data)

    def defining_predicate(self):
        assert self._preamble_defining_predicate is not None, (
            "defining_predicate requires a submonoid represented by a selected membership predicate"
        )
        return self._preamble_defining_predicate

    def monoid_generators(self):
        assert self._preamble_monoid_generators is not None, (
            "monoid_generators requires a submonoid represented by a chosen generating set"
        )
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
        is_selected_generator = any(element == generator for generator in generators)
        assert is_selected_generator, (
            "membership beyond the identity and selected generators requires a represented "
            "generated-submonoid decision procedure"
        )
        return True

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
    structure_data=None,
):
    category = Monoids().Subobjects(ambient)
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
