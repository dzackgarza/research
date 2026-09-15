"""Subgroups specified by a membership predicate rather than generators."""

from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    Subgroups,
    _owned_group,
)
from dzack_research.preamble.categories.orthogonal_quotients import (
    OrthogonalCharacterQuotient,
    subgroup_isotropic_are_equivalent,
    subgroup_isotropic_orbit_representatives,
    subgroup_vector_orbit_representatives,
    subgroup_vectors_are_equivalent,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.set_categories import Set
from dzack_research.preamble.owned_category import object_of


class PredicateSubgroups(OwnedParameterizedCategory):

    @staticmethod
    def __classcall__(cls, supergroup):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(supergroup))

    def parameter_category(self):
        return OwnedGroups()

    def an_object(self):
        r"""The whole parameter group cut out by the tautological predicate.

        Every element commutes with the identity, so this is the whole group --
        cut out by a predicate, which is what membership here states.
        """
        group = self.base()
        return group.centralizer(group.one())

    def _repr_object_names(self):
        return "predicate subgroups"

    def super_categories(self):
        return [Subgroups(self.base())]

    def _call_(
        self,
        predicate,
        description,
        *,
        character_data=None,
        character_data_complete=None,
    ):
        r"""Construct the predicate subgroup of this category's ambient group."""
        return object_of(
            self,
            supergroup=self.base(),
            predicate=predicate,
            description=description,
            character_data=character_data,
            character_data_complete=character_data_complete,
        )

    class ParentMethods:
        def __init__(
            self,
            supergroup,
            predicate,
            description,
            character_data=None,
            character_data_complete=None,
            **rest,
        ) -> None:
            self._containing_group = supergroup
            self._predicate = predicate
            self._description = description
            self._character_data = dict(character_data or {})
            self._character_data_complete = (
                bool(character_data)
                if character_data_complete is None
                else bool(character_data_complete)
            )
            super().__init__(supergroup=supergroup, **rest)

        def supergroup(self):
            return self._containing_group

        def defining_predicate(self):
            return self._predicate

        def character_data(self):
            return dict(self._character_data)

        def character_data_is_complete(self) -> bool:
            r"""Whether the retained finite characters define this whole subgroup."""
            return self._character_data_complete

        def contains_character_kernel(self) -> bool:
            data = self.character_data()
            return self.character_data_is_complete() and bool(
                data.get("determinant_kernel", False)
                or data.get("spinor_kernel", False)
                or data.get("discriminant_preimages", ())
            )

        def cardinality(self):
            supergroup_cardinality = self.supergroup().cardinality()
            if self.contains_character_kernel():
                quotient = self.finite_character_quotient()
                image_size = int(quotient.image_keys().cardinality())
                subgroup_image_size = int(quotient.subgroup_image_keys().cardinality())
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
            return intersection_subgroup(
                self.supergroup(),
                (self, other),
                character_data=data,
                character_data_complete=(
                    self.character_data_is_complete()
                    and other.character_data_is_complete()
                ),
            )

        def finite_character_quotient(self):
            if not self.character_data_is_complete():
                raise ValueError(
                    "the retained finite characters do not define this whole subgroup"
                )
            return OrthogonalCharacterQuotient(self)

        def vector_orbit_representatives(self, square):

            return subgroup_vector_orbit_representatives(self, square)

        def vectors_are_equivalent(self, left, right) -> bool:

            return subgroup_vectors_are_equivalent(self, left, right)

        def vector_equivalence_witness(self, left, right):
            from dzack_research.preamble.categories.orthogonal_quotients import (
                subgroup_vector_equivalence_witness,
            )

            return subgroup_vector_equivalence_witness(self, left, right)

        def isotropic_orbit_representatives(self, rank, *, flag=False):

            return subgroup_isotropic_orbit_representatives(
                self, rank, flag=flag
            )

        def isotropic_are_equivalent(self, left, right, *, flag=False) -> bool:

            return subgroup_isotropic_are_equivalent(
                self, left, right, flag=flag
            )

        def isotropic_equivalence_witness(self, left, right, *, flag=False):
            from dzack_research.preamble.categories.orthogonal_quotients import (
                subgroup_isotropic_equivalence_witness,
            )

            return subgroup_isotropic_equivalence_witness(
                self, left, right, flag=flag
            )

        def cusps(self, rank=1):
            r"""Return this arithmetic subgroup's primitive-isotropic cusp orbits."""
            from dzack_research.preamble.categories.isotropic_orbits import ArithmeticCusp
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                finite_ordered_set,
            )

            return finite_ordered_set(
                tuple(
                    ArithmeticCusp(self, representative)
                    for representative in self.isotropic_orbit_representatives(rank)
                )
            )

        def tits_building_incidence(self):
            r"""Return this subgroup's rank-one/rank-two quotient-building incidence."""
            from dzack_research.preamble.categories.isotropic_orbits import (
                arithmetic_tits_building_incidence,
            )

            return arithmetic_tits_building_incidence(self)

        def _repr_(self):
            return f"{{g in {self._containing_group} : {self._description}}}"


class _PredicateSubgroupConstruction(OwnedParameterizedCategory):
    @staticmethod
    def __classcall__(cls, supergroup):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(supergroup))

    def parameter_category(self):
        return OwnedGroups()

    def super_categories(self):
        return [PredicateSubgroups(self.base())]

class KernelSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):

        group = self.base()
        return self(group.Mor(group).identity())

    def _call_(self, morphism):
        r"""Construct the kernel subgroup retaining its defining morphism."""
        group = self.base()
        if morphism.domain() is not group:
            raise ValueError("the kernel morphism has the wrong domain group")
        identity = morphism.codomain().one()
        return object_of(
            self,
            supergroup=group,
            predicate=lambda element: morphism(element) == identity,
            description=f"{morphism}(g)=1",
            kernel_morphism=morphism,
        )

    @classmethod
    def _repr_object_names(cls):
        return "kernel subgroups"

    class ParentMethods:
        def __init__(self, kernel_morphism, **rest) -> None:
            self._preamble_kernel_morphism = kernel_morphism
            super().__init__(**rest)

        def kernel_morphism(self):
            return self._preamble_kernel_morphism

        def cardinality(self):
            r"""Return the exact kernel order when the ambient group is finite."""
            if self.supergroup().is_finite() is True:
                return cardinal(int(self.kernel_morphism().gap().Kernel().Size()))
            return super().cardinality()

        def is_abelian(self):
            r"""Decide abelianity from the represented exact kernel when finite."""
            if self.supergroup().is_finite() is True:
                return bool(self.kernel_morphism().gap().Kernel().IsAbelian())
            assert False, (
                "kernel abelianity is mathematically defined generally, but the current "
                "exact computation requires a finite ambient group with a GAP-backed morphism"
            )


class PreimageSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):

        group = self.base()
        whole = PredicateSubgroups(group)(lambda _element: True, "the whole group")
        return self(group.Mor(group).identity(), whole)

    def _call_(
        self,
        morphism,
        subgroup,
        *,
        predicate=None,
        description=None,
        character_data=None,
        character_data_complete=None,
    ):
        r"""Construct the inverse image of ``subgroup`` along ``morphism``."""
        group = self.base()
        if morphism.domain() is not group:
            raise ValueError("the preimage morphism has the wrong domain group")
        if predicate is None:
            def predicate(element):
                return morphism(element) in subgroup
        if description is None:
            description = f"{morphism}(g) lies in {subgroup}"
        return object_of(
            self,
            supergroup=group,
            predicate=predicate,
            description=description,
            character_data=character_data,
            character_data_complete=character_data_complete,
            preimage_morphism=morphism,
            target_subgroup=subgroup,
        )

    @classmethod
    def _repr_object_names(cls):
        return "preimage subgroups"

    class ParentMethods:
        def __init__(self, preimage_morphism, target_subgroup, **rest) -> None:
            self._preamble_preimage_morphism = preimage_morphism
            self._preamble_target_subgroup = target_subgroup
            super().__init__(**rest)

        def preimage_morphism(self):
            return self._preamble_preimage_morphism

        def target_subgroup(self):
            return self._preamble_target_subgroup


class StabilizerSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):
        group = self.base()
        identity = group.one()
        return self(
            identity,
            "conjugation",
            lambda element: element * identity * element.inverse() == identity,
        )

    def _call_(
        self,
        stabilized_object,
        action,
        predicate,
        *,
        description=None,
    ):
        r"""Construct the stabilizer retaining the stabilized object and action."""
        group = self.base()
        if description is None:
            description = f"g stabilizes {stabilized_object} {action}"
        return object_of(
            self,
            supergroup=group,
            predicate=predicate,
            description=description,
            stabilized_object=stabilized_object,
            stabilizer_action=action,
        )

    @classmethod
    def _repr_object_names(cls):
        return "stabilizer subgroups"

    class ParentMethods:
        def __init__(self, stabilized_object, stabilizer_action, **rest) -> None:
            self._preamble_stabilized_object = stabilized_object
            self._preamble_stabilizer_action = stabilizer_action
            super().__init__(**rest)

        def stabilized_object(self):
            return self._preamble_stabilized_object

        def stabilizer_action(self):
            return self._preamble_stabilizer_action


class CentralizerSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):
        group = self.base()
        return self(group.one())

    def _call_(self, element):
        r"""Construct the centralizer of ``element`` in the ambient group."""
        group = self.base()
        if element not in group:
            raise ValueError(f"{element} is not in {group}")
        return object_of(
            self,
            supergroup=group,
            predicate=lambda candidate: element * candidate == candidate * element,
            description=f"g commutes with {element}",
            centralizing_element=element,
        )

    @classmethod
    def _repr_object_names(cls):
        return "centralizer subgroups"

    class ParentMethods:
        def __init__(self, centralizing_element, **rest) -> None:
            self._preamble_centralizing_element = centralizing_element
            super().__init__(**rest)

        def centralizing_element(self):
            return self._preamble_centralizing_element


class IntersectionSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):
        group = self.base()
        whole = PredicateSubgroups(group)(lambda _element: True, "the whole group")
        return self((whole, whole))

    def _call_(
        self,
        subgroups,
        *,
        character_data=None,
        character_data_complete=None,
    ):
        r"""Construct the intersection of subgroups of this ambient group."""
        group = self.base()
        subgroups = tuple(subgroups)
        if any(subgroup.supergroup() is not group for subgroup in subgroups):
            raise ValueError("an intersection requires subgroups of one ambient group")
        return object_of(
            self,
            supergroup=group,
            predicate=lambda element: all(element in subgroup for subgroup in subgroups),
            description="g lies in every selected subgroup",
            character_data=character_data,
            character_data_complete=character_data_complete,
            intersected_subgroups=subgroups,
        )

    @classmethod
    def _repr_object_names(cls):
        return "intersection subgroups"

    class ParentMethods:
        def __init__(self, intersected_subgroups, **rest) -> None:
            self._preamble_intersected_subgroups = Set(tuple(intersected_subgroups))
            super().__init__(**rest)

        def intersected_subgroups(self):
            return self._preamble_intersected_subgroups


def predicate_subgroup_category(containing_group):
    return PredicateSubgroups(containing_group)


def kernel_subgroup(morphism):
    r"""Notebook notation for the category-owned kernel subgroup."""
    return KernelSubgroups(morphism.domain())(morphism)


def preimage_subgroup(
    morphism,
    subgroup,
    *,
    predicate=None,
    description=None,
    character_data=None,
    character_data_complete=None,
):
    r"""Notebook notation for the category-owned inverse-image subgroup."""
    return PreimageSubgroups(morphism.domain())(
        morphism,
        subgroup,
        predicate=predicate,
        description=description,
        character_data=character_data,
        character_data_complete=character_data_complete,
    )


def stabilizer_subgroup(
    containing_group,
    stabilized_object,
    action,
    predicate,
    *,
    description=None,
):
    r"""Notebook notation for the category-owned stabilizer subgroup."""
    return StabilizerSubgroups(containing_group)(
        stabilized_object,
        action,
        predicate,
        description=description,
    )


def intersection_subgroup(
    containing_group,
    subgroups,
    *,
    character_data=None,
    character_data_complete=None,
):
    r"""Notebook notation for the category-owned subgroup intersection."""
    return IntersectionSubgroups(containing_group)(
        subgroups,
        character_data=character_data,
        character_data_complete=character_data_complete,
    )


def is_predicate_subgroup(group):
    return any(
        isinstance(category, PredicateSubgroups)
        for category in group.category().all_super_categories(proper=False)
    )


__all__ = [
    "CentralizerSubgroups",
    "IntersectionSubgroups",
    "KernelSubgroups",
    "PredicateSubgroups",
    "PreimageSubgroups",
    "StabilizerSubgroups",
    "intersection_subgroup",
    "is_predicate_subgroup",
    "kernel_subgroup",
    "preimage_subgroup",
    "stabilizer_subgroup",
]
