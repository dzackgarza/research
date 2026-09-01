r"""Scalar extension and restriction for modules carrying a fixed group action.

For a ring morphism ``f:R -> S`` and a fixed group ``G`` the ordinary
extension/restriction adjunction lifts to representation categories:

``S tensor_R - ⊣ Res_f : R[G]-Mod <-> S[G]-Mod``.

The group action is transported, not recomputed: scalar extension reads each
action matrix over ``S``; restriction keeps the same additive-group action and
only restricts the scalar ring.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules import (
    module_homset,
    restrict_scalars,
)
from dzack_research.preamble.categories.modules.group_modules.group_modules import (
    GroupModules,
    group_module_homset,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings import owned_ring_view
from dzack_research.preamble.refine import refine


def _unacted_module(group_module):
    try:
        return group_module.unacted_module()
    except AttributeError:
        return group_module


def _forget_action_element(group_module, element):
    try:
        return group_module.forget_action_morphism()(element)
    except AttributeError:
        return element


def _equip_action_element(group_module, element):
    try:
        return group_module.equip_action_morphism()(element)
    except AttributeError:
        return group_module(element)


class GroupModuleScalarExtensionFunctor(Functor):
    r"""``S tensor_R - : R[G]-Mod -> S[G]-Mod`` along one scalar map."""

    def __init__(self, ring_map, group) -> None:
        self._ring_map = ring_map
        self._group = group
        self._source_ring = owned_ring_view(ring_map.domain())
        self._target_ring = owned_ring_view(ring_map.codomain())
        super().__init__(
            GroupModules(self._source_ring, group),
            GroupModules(self._target_ring, group),
        )

    def ring_map(self):
        return self._ring_map

    def group(self):
        return self._group

    def _apply_object(self, group_module):
        from dzack_research.preamble.categories.functors.scalar_change import (
            ScalarExtensionFunctor,
        )
        from dzack_research.preamble.categories.modules.group_modules.group_modules import (
            GroupModule,
        )
        from dzack_research.preamble.tensors import tensor

        unacted = _unacted_module(group_module)
        changed_module = ScalarExtensionFunctor(self.ring_map())(unacted)
        labels = tuple(changed_module.module_generating_set())

        def action(group_element, vector):
            coefficients = module_coefficients(vector, changed_module)
            coordinates = tensor.vector(
                self._target_ring,
                [coefficients.get(label, self._target_ring.zero()) for label in labels],
            )
            source_tensor = group_module.action_tensor(group_element)
            action_tensor = tensor.matrix(
                self._target_ring,
                [
                    [self._target_ring(self.ring_map()(entry)) for entry in row]
                    for row in source_tensor.rows()
                ],
            )
            image = action_tensor * coordinates
            return changed_module.linear_combination(
                {
                    label: image[index]
                    for index, label in enumerate(labels)
                    if image[index]
                }
            )

        extended = GroupModule(changed_module, self.group(), action)
        extended._preamble_scalar_extension_source_group_module = group_module
        if group_module.is_trivial_action():
            extended._preamble_action_is_trivial = True
        return extended

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())

        def image(label):
            original = morphism.domain().module_generator(label)
            coefficients = module_coefficients(
                morphism(original), morphism.codomain()
            )
            return target.linear_combination(
                {
                    target_label: self._target_ring(
                        self.ring_map()(coefficient)
                    )
                    for target_label, coefficient in coefficients.items()
                }
            )

        return group_module_homset(source, target)(image)

    def _repr_(self):
        return f"Scalar extension of {self.group()}-modules along {self.ring_map()}"


class GroupModuleRestrictionOfScalarsFunctor(Functor):
    r"""``Res_f : S[G]-Mod -> R[G]-Mod``."""

    def __init__(self, ring_map, group) -> None:
        self._ring_map = ring_map
        self._group = group
        self._source_ring = owned_ring_view(ring_map.domain())
        self._target_ring = owned_ring_view(ring_map.codomain())
        super().__init__(
            GroupModules(self._target_ring, group),
            GroupModules(self._source_ring, group),
        )

    def ring_map(self):
        return self._ring_map

    def group(self):
        return self._group

    def _apply_object(self, group_module):
        unacted_extension = _unacted_module(group_module)
        unacted_restricted = restrict_scalars(unacted_extension, self.ring_map())
        restricted = restrict_scalars(unacted_extension, self.ring_map())
        restricted._preamble_acting_group = self.group()

        def action(group_element, vector):
            acted_source = _equip_action_element(
                group_module,
                vector.underlying_element(),
            )
            acted_image = group_module.act(
                group_element,
                acted_source,
            )
            return restricted.element_class(
                restricted,
                _forget_action_element(group_module, acted_image),
            )

        restricted._preamble_action = action
        restricted._preamble_unacted_module = unacted_restricted
        restricted._preamble_restricted_group_module_source = group_module
        restricted._preamble_action_is_trivial = group_module.is_trivial_action()
        restricted._preamble_forget_action_morphism = module_homset(
            restricted, unacted_restricted
        )(
            lambda label: unacted_restricted(
                restricted.module_generator(label).underlying_element()
            )
        )
        restricted._preamble_equip_action_morphism = module_homset(
            unacted_restricted, restricted
        )(
            lambda label: restricted(
                unacted_restricted.module_generator(label).underlying_element()
            )
        )
        return refine(restricted, GroupModules(self._source_ring, self.group()))

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return group_module_homset(source, target)(
            lambda label: target(
                _forget_action_element(
                    morphism.codomain(),
                    morphism(
                        _equip_action_element(
                            morphism.domain(),
                            source.module_generator(label).underlying_element(),
                        )
                    ),
                )
            )
        )

    def _repr_(self):
        return f"Restriction of {self.group()}-modules along {self.ring_map()}"


class GroupModuleBaseChangeAdjunction(Adjunction):
    r"""``S tensor_R - ⊣ Res_f`` on modules carrying a fixed ``G``-action."""

    def __init__(self, ring_map, group) -> None:
        self._ring_map = ring_map
        self._group = group
        super().__init__(
            GroupModuleScalarExtensionFunctor(ring_map, group),
            GroupModuleRestrictionOfScalarsFunctor(ring_map, group),
        )

    def unit(self, group_module):
        extended = self.left_adjoint()(group_module)
        restricted = self.right_adjoint()(extended)
        return group_module_homset(group_module, restricted)(
            lambda label: restricted(
                _forget_action_element(
                    extended,
                    extended.module_generator(label),
                )
            )
        )

    def counit(self, group_module):
        restricted = self.right_adjoint()(group_module)
        extended = self.left_adjoint()(restricted)
        return group_module_homset(extended, group_module)(
            lambda label: _equip_action_element(
                group_module,
                restricted.module_generator(label).underlying_element(),
            )
        )

    def hom_set_isomorphism_forward(self, extended_morphism):
        extended_source = extended_morphism.domain()
        source = getattr(
            extended_source,
            "_preamble_scalar_extension_source_group_module",
            None,
        )
        if source is None:
            raise ValueError("the extended source was not produced by this scalar-extension functor")
        target_restricted = self.right_adjoint()(extended_morphism.codomain())
        return group_module_homset(source, target_restricted)(
            lambda label: target_restricted(
                _forget_action_element(
                    extended_morphism.codomain(),
                    extended_morphism(extended_source.module_generator(label)),
                )
            )
        )

    def hom_set_isomorphism_inverse(self, restricted_morphism, codomain=None):
        restricted_target = restricted_morphism.codomain()
        target = getattr(
            restricted_target,
            "_preamble_restricted_group_module_source",
            None,
        )
        if target is None:
            raise TypeError(
                "the inverse transpose must land in a restricted S[G]-module"
            )
        if codomain is not None and codomain is not target:
            raise ValueError("the stated codomain is not the S[G]-module being restricted")
        source = self.left_adjoint()(restricted_morphism.domain())
        return group_module_homset(source, target)(
            lambda label: _equip_action_element(
                target,
                restricted_morphism(
                    restricted_morphism.domain().module_generator(label)
                ).underlying_element(),
            )
        )

    def _repr_(self):
        return (
            f"Scalar-extension/restriction adjunction for {self._group}-modules "
            f"along {self._ring_map}"
        )


@cached_function
def group_module_base_change_adjunction(ring_map, group) -> GroupModuleBaseChangeAdjunction:
    return GroupModuleBaseChangeAdjunction(ring_map, group)


__all__ = [
    "GroupModuleBaseChangeAdjunction",
    "GroupModuleRestrictionOfScalarsFunctor",
    "GroupModuleScalarExtensionFunctor",
    "group_module_base_change_adjunction",
]
