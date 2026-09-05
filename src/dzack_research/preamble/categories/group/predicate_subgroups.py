"""Subgroups specified by a membership predicate rather than generators."""

from dzack_research.preamble.categories.abstract_categories.objects import OwnedParameterizedCategory

from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _canonical_subgroup_inclusion,
    _owned_group,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.orthogonal_quotients import (
    OrthogonalCharacterQuotient,
    subgroup_isotropic_are_equivalent,
    subgroup_isotropic_orbit_representatives,
    subgroup_vector_orbit_representatives,
    subgroup_vectors_are_equivalent,
)


class PredicateSubgroups(OwnedParameterizedCategory):

    def an_object(self):
        r"""The centralizer of the identity in an object of the parameter category.

        Every element commutes with the identity, so this is the whole group --
        cut out by a predicate, which is what membership here states.
        """
        group = self.base().an_object()
        return centralizer(group, group.one())

    def _repr_object_names(self):
        return "predicate subgroups"

    def super_categories(self):
        return [self.base()]

    class ParentMethods:
        def __init__(
            self,
            containing_group,
            predicate,
            description,
            character_data=None,
            **rest,
        ) -> None:
            self._containing_group = containing_group
            self._predicate = predicate
            self._description = description
            self._character_data = dict(character_data or {})
            super().__init__(facade=True, **rest)

        def supergroup(self):
            return self._containing_group

        def defining_predicate(self):
            return self._predicate

        def character_data(self):
            return dict(self._character_data)

        def contains_character_kernel(self) -> bool:
            data = self.character_data()
            return bool(
                data.get("determinant_kernel", False)
                or data.get("spinor_kernel", False)
                or data.get("discriminant_preimages", ())
            )

        def cardinality(self):
            supergroup_cardinality = self.supergroup().cardinality()
            if self.contains_character_kernel():
                quotient = self.finite_character_quotient()
                image_size = len(quotient.image_keys())
                subgroup_image_size = len(quotient.subgroup_image_keys())
                if supergroup_cardinality.is_finite():
                    order = int(supergroup_cardinality.finite_value())
                    return cardinal(order * subgroup_image_size // image_size)
                if supergroup_cardinality.is_countably_infinite():
                    return supergroup_cardinality
            assert False, (
                "cardinality is defined for every predicate subgroup, but the current "
                "exact computation requires represented finite-character data over a "
                "finite or countably infinite supergroup"
            )

        def __contains__(self, element):
            parent = getattr(element, "parent", lambda: None)()
            if parent is not self._containing_group and element not in self._containing_group:
                return False
            return bool(self._predicate(element))

        def _element_constructor_(self, datum):
            element = (
                datum
                if datum in self._containing_group
                else self._containing_group(datum)
            )
            if element not in self:
                raise ValueError(f"{element} does not satisfy {self._description}")
            return element

        def one(self):
            identity = self._containing_group.one()
            if identity not in self:
                raise ValueError(
                    f"{self._description} does not contain the identity; this is not a subgroup"
                )
            return identity

        def inclusion(self):
            return _canonical_subgroup_inclusion(self)

        def intersection(self, other):
            if other.supergroup() is not self.supergroup():
                raise ValueError("predicate-subgroup intersections require one ambient group")
            left = self.character_data()
            right = other.character_data()
            data = {
                "determinant_kernel": bool(left.get("determinant_kernel", False))
                or bool(right.get("determinant_kernel", False)),
                "spinor_kernel": bool(left.get("spinor_kernel", False))
                or bool(right.get("spinor_kernel", False)),
                "discriminant_preimages": tuple(left.get("discriminant_preimages", ()))
                + tuple(right.get("discriminant_preimages", ())),
            }
            return predicate_subgroup(
                self.supergroup(),
                lambda element: element in self and element in other,
                f"({self._description}) and ({other._description})",
                character_data=data,
            )

        def finite_character_quotient(self):

            return OrthogonalCharacterQuotient(self)

        def vector_orbit_representatives(self, square):

            return subgroup_vector_orbit_representatives(self, square)

        def vectors_are_equivalent(self, left, right) -> bool:

            return subgroup_vectors_are_equivalent(self, left, right)

        def isotropic_orbit_representatives(self, rank, *, flag=False):

            return subgroup_isotropic_orbit_representatives(
                self, rank, flag=flag
            )

        def isotropic_are_equivalent(self, left, right, *, flag=False) -> bool:

            return subgroup_isotropic_are_equivalent(
                self, left, right, flag=flag
            )

        def _repr_(self):
            return f"{{g in {self._containing_group} : {self._description}}}"


def predicate_subgroup_category():
    return PredicateSubgroups(OwnedGroups())


def predicate_subgroup(
    containing_group,
    predicate,
    description,
    *,
    character_data=None,
):
    containing_group = _owned_group(containing_group)
    if containing_group not in OwnedGroups():
        raise TypeError(f"{containing_group} is not a group")
    return object_of(
        predicate_subgroup_category(),
        containing_group=containing_group,
        predicate=predicate,
        description=description,
        character_data=character_data,
    )


def is_predicate_subgroup(group):
    return any(
        isinstance(category, PredicateSubgroups)
        for category in group.category().all_super_categories(proper=False)
    )


def centralizer(containing_group, element):
    if element not in containing_group:
        raise ValueError(f"{element} is not in {containing_group}")
    return predicate_subgroup(
        containing_group,
        lambda candidate: element * candidate == candidate * element,
        f"g commutes with {element}",
    )
