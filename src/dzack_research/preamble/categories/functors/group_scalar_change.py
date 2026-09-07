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
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebra
from dzack_research.preamble.categories.modules.pure.modules import Modules, restrict_scalars
from dzack_research.preamble.categories.modules.group_modules.group_modules import (

    _equip_action,
    group_module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.functors.scalar_change import (
    RestrictionOfScalarsFunctor,
    ScalarExtensionFunctor,
    base_change_adjunction,
)


def _unacted_module(group_module):
    return group_module.unacted_module()


def _forget_action_element(group_module, element):
    return group_module.forget_action_morphism()(element)


def _equip_action_element(group_module, element):
    return group_module.equip_action_morphism()(element)


class GroupModuleScalarExtensionFunctor(Functor):
    r"""``S tensor_R - : R[G]-Mod -> S[G]-Mod`` along one scalar map."""

    def __init__(self, ring_map, group) -> None:
        self._ring_map = ring_map
        self._group = group
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(
            Modules(GroupAlgebra(self._source_ring, group)),
            Modules(GroupAlgebra(self._target_ring, group)),
        )

    def ring_map(self):
        return self._ring_map

    def group(self):
        return self._group

    def _apply_object(self, group_module):
        return group_module.base_change(self.ring_map())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        underlying = morphism.underlying_module_morphism()
        scalar_extension = ScalarExtensionFunctor(self.ring_map())
        scalar_extension.adopt_object_image(
            morphism.domain().unacted_module(), source.unacted_module()
        )
        scalar_extension.adopt_object_image(
            morphism.codomain().unacted_module(), target.unacted_module()
        )
        transported = scalar_extension(underlying)
        return group_module_homset(source, target)._from_equivariant_images(
            transported,
            verify_linearity=False,
        )

    def _repr_(self):
        return f"Scalar extension of {self.group()}-modules along {self.ring_map()}"


class GroupModuleRestrictionOfScalarsFunctor(Functor):
    r"""``Res_f : S[G]-Mod -> R[G]-Mod``."""

    def __init__(self, ring_map, group) -> None:
        self._ring_map = ring_map
        self._group = group
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        super().__init__(
            Modules(GroupAlgebra(self._target_ring, group)),
            Modules(GroupAlgebra(self._source_ring, group)),
        )

    def ring_map(self):
        return self._ring_map

    def group(self):
        return self._group

    def _apply_object(self, group_module):
        unacted_extension = _unacted_module(group_module)
        unacted_restricted = restrict_scalars(unacted_extension, self.ring_map())

        def action(group_element, vector):
            acted_source = _equip_action_element(
                group_module,
                vector.underlying_element(),
            )
            acted_image = group_module.act(
                group_element,
                acted_source,
            )
            return unacted_restricted.wrap(
                _forget_action_element(group_module, acted_image)
            )

        return _equip_action(
            unacted_restricted,
            self.group(),
            action,
            _action_is_trivial=group_module.is_trivial_action(),
        )

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        restriction = RestrictionOfScalarsFunctor(self.ring_map())
        restriction.adopt_object_image(
            morphism.domain().unacted_module(),
            source.unacted_module(),
        )
        restriction.adopt_object_image(
            morphism.codomain().unacted_module(),
            target.unacted_module(),
        )
        transported = restriction(morphism.underlying_module_morphism())
        return group_module_homset(source, target)._from_equivariant_images(
            transported,
            verify_linearity=False,
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

    def _underlying_adjunction(self):

        return base_change_adjunction(self._ring_map)

    def unit(self, group_module):
        extended = self.left_adjoint()(group_module)
        restricted = self.right_adjoint()(extended)
        underlying = self._underlying_adjunction()
        source_module = group_module.unacted_module()
        extended_module = extended.unacted_module()
        restricted_module = restricted.unacted_module()
        underlying.left_adjoint().adopt_object_image(source_module, extended_module)
        underlying.right_adjoint().adopt_object_image(extended_module, restricted_module)
        unit = underlying.unit(source_module)
        return group_module_homset(group_module, restricted)._from_equivariant_images(
            unit,
            verify_linearity=False,
        )

    def counit(self, group_module):
        restricted = self.right_adjoint()(group_module)
        extended = self.left_adjoint()(restricted)
        underlying = self._underlying_adjunction()
        target_module = group_module.unacted_module()
        restricted_module = restricted.unacted_module()
        extended_module = extended.unacted_module()
        underlying.right_adjoint().adopt_object_image(target_module, restricted_module)
        underlying.left_adjoint().adopt_object_image(restricted_module, extended_module)
        counit = underlying.counit(target_module)
        return group_module_homset(extended, group_module)._from_equivariant_images(
            counit,
            verify_linearity=False,
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
