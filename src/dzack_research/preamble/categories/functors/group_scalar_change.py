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
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


class _GroupModuleScalarExtensionFunctor(Functor):
    r"""``S tensor_R - : R[G]-Mod -> S[G]-Mod`` along one scalar map."""

    def __init__(self, ring_map, group, scalar_extension) -> None:
        self._ring_map = ring_map
        self._group = group
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        self._scalar_extension = scalar_extension
        super().__init__(
            Modules(self._source_ring[group]),
            Modules(self._target_ring[group]),
        )

    def ring_map(self):
        return self._ring_map

    def group(self):
        return self._group

    def _underlying_scalar_extension(self):
        return self._scalar_extension

    def _apply_object(self, group_module):
        r"""Transport one ``R[G]``-module through this coefficient scalar extension."""
        unformed = group_module.unformed_module()
        scalar_extension = self._underlying_scalar_extension()
        changed_module = scalar_extension(unformed)
        if group_module.is_trivial_action():
            return Modules(changed_module.base_ring()).trivial_action(self.group())(changed_module)

        def changed_action(group_element, vector):
            return scalar_extension(group_module.action_of(group_element))(vector)

        return self.codomain()(changed_module, changed_action)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        underlying = morphism.underlying_module_morphism()
        transported = self._underlying_scalar_extension()(underlying)
        return source.Mor(target)._from_equivariant_images(
            transported,
        )

    def _repr_(self):
        return f"Scalar extension of {self.group()}-modules along {self.ring_map()}"


class _GroupModuleRestrictionOfScalarsFunctor(Functor):
    r"""``Res_f : S[G]-Mod -> R[G]-Mod``."""

    def __init__(self, ring_map, group, restriction) -> None:
        self._ring_map = ring_map
        self._group = group
        self._source_ring = _owned_ring(ring_map.domain())
        self._target_ring = _owned_ring(ring_map.codomain())
        self._restriction = restriction
        super().__init__(
            Modules(self._target_ring[group]),
            Modules(self._source_ring[group]),
        )

    def ring_map(self):
        return self._ring_map

    def group(self):
        return self._group

    def _underlying_restriction(self):
        return self._restriction

    def _apply_object(self, group_module):
        unformed = group_module.unformed_module()
        restricted = self._underlying_restriction()(unformed)

        def action(group_element, vector):
            acted_image = group_module.act(
                group_element,
                group_module(vector.underlying_element()),
            )
            return restricted.wrap(unformed(acted_image))

        return self.codomain()(restricted, action)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        transported = self._underlying_restriction()(
            morphism.underlying_module_morphism()
        )
        return source.Mor(target)._from_equivariant_images(
            transported,
        )

    def _repr_(self):
        return f"Restriction of {self.group()}-modules along {self.ring_map()}"


class _GroupModuleBaseChangeAdjunction(Adjunction):
    r"""``S tensor_R - ⊣ Res_f`` on modules carrying a fixed ``G``-action."""

    def __init__(self, ring_map, group) -> None:
        self._ring_map = ring_map
        self._group = group
        self._underlying = Modules(ring_map.domain()).base_change_adjunction(ring_map)
        super().__init__(
            _GroupModuleScalarExtensionFunctor(
                ring_map, group, self._underlying.left_adjoint()
            ),
            _GroupModuleRestrictionOfScalarsFunctor(
                ring_map, group, self._underlying.right_adjoint()
            ),
        )

    def _underlying_adjunction(self):
        return self._underlying

    def _unit_component(self, group_module):
        extended = self.left_adjoint()(group_module)
        restricted = self.right_adjoint()(extended)
        underlying = self._underlying_adjunction()
        source_module = group_module.unformed_module()
        unit = underlying.unit(source_module)
        return group_module.Mor(restricted)._from_equivariant_images(
            unit,
        )

    def _counit_component(self, group_module):
        restricted = self.right_adjoint()(group_module)
        extended = self.left_adjoint()(restricted)
        underlying = self._underlying_adjunction()
        target_module = group_module.unformed_module()
        counit = underlying.counit(target_module)
        return extended.Mor(group_module)._from_equivariant_images(
            counit,
        )

    def _repr_(self):
        return (
            f"Scalar-extension/restriction adjunction for {self._group}-modules "
            f"along {self._ring_map}"
        )


@cached_function
def _group_module_base_change_adjunction(ring_map, group) -> _GroupModuleBaseChangeAdjunction:
    return _GroupModuleBaseChangeAdjunction(ring_map, group)


__all__ = []
