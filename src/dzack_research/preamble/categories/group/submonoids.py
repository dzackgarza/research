"""Submonoids represented as monomorphism subobjects of an ambient monoid."""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.group.magmas import Monoids
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.logic import AtomicProposition, Predicate
from dzack_research.preamble.owned_category import _object_of, owned_category_join


class _SubmonoidEngine:
    r"""A source monoid with its chosen inclusion into an ambient monoid.

    For a predicate presentation, the caller supplies the identity and
    multiplication-closure premises stated by ``Monoids.predicate_submonoid``.
    This realization retains that predicate; it does not require a decision
    algorithm for membership or for those laws.
    """

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
        if predicate is not None:
            identity_membership = predicate(ambient.one())
            if not isinstance(identity_membership, Predicate) and not bool(identity_membership):
                raise ValueError(
                    f"the predicate {description or predicate} does not define a submonoid of "
                    f"{ambient}: the identity {ambient.one()} does not satisfy it"
                )

    def ambient_monoid(self):
        return self._ambient_monoid

    supermonoid = ambient_monoid

    @cached_method
    def inclusion(self):
        return Monoids().Mor(self, self.ambient_monoid())._from_submonoid_inclusion()

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
        membership = ambient.is_parent_of(datum)
        if membership is False:
            raise ValueError(
                f"{datum} cannot be an element of the submonoid {self}: it is not an element "
                f"of the monoid {ambient}"
            )
        assert membership is True, (
            f"cannot admit {datum} into the submonoid {self}: membership in its "
            f"ambient monoid {ambient} is undecided"
        )
        return ambient(datum)

    def __contains__(self, datum) -> bool | Predicate:
        r"""Return the membership proposition without forcing its truth value."""
        ambient = self.ambient_monoid()
        match ambient.is_parent_of(datum):
            case False:
                return False
            case True:
                element = ambient(datum)
            case _:
                return AtomicProposition("is_parent_of", self, datum)
        if self._defining_predicate is not None:
            membership = self._defining_predicate(element)
            return membership if isinstance(membership, Predicate) else bool(membership)
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

    is_parent_of = __contains__

    def _element_constructor_(self, datum):
        element = self._normalize(datum)
        answer = self.is_parent_of(element)
        if answer is False:
            raise ValueError(f"{element} is not in {self}")
        assert answer is True, (
            f"cannot admit {element} into {self}: its membership is undecided"
        )
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
    r"""Realize the predicate submonoid declared at the monoid owner.

    Protected constructor under OWN-05. ``Monoids.predicate_submonoid`` is
    the caller. The predicate is defined on this exact ambient monoid and
    its truth set contains one and is multiplicatively closed. Any stronger
    placements are supplied with their mathematical premises by that caller.
    The result is the existing facade submonoid with its actual inclusion;
    an undecided predicate value is retained, not treated as nonmembership.
    """
    category = owned_category_join((Monoids().Subobjects(ambient), *placements))
    return _object_of(
        category,
        _engine=(category, _SubmonoidEngine, None),
        ambient=ambient,
        predicate=predicate,
        description=description,
        structure_data=structure_data,
    )
