r"""Lattices equipped with a chosen form-preserving group action."""

from sage.categories.morphism import SetMorphism

from dzack_research.preamble.categories.modules.group_modules.group_modules import (
    GroupModule,
    GroupModules,
    _CategoryOverRingAndActingGroup,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.lattices import (
    FiniteRankLattices,
    Lattices,
    RootLattices,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_coefficients
from dzack_research.preamble.categories.sets.set_categories import Sets


class GroupLattices(_CategoryOverRingAndActingGroup):
    r"""Lattices carrying a specified action by lattice isometries."""

    def _repr_object_names(self):
        return f"{self.acting_group()}-lattices over {self.base_ring()}"

    def super_categories(self):

        return [
            Lattices(self.base_ring()),
            GroupModules(self.base_ring(), self.acting_group()),
        ]

    class ParentMethods:
        def group(self):
            return self._preamble_group_module.group()

        def action(self):
            return self._preamble_lattice_action

        def act(self, group_element, vector):

            if vector.parent() is not self:
                raise TypeError(f"the action is on elements of {self}")
            return self.action()(group_element)(vector)

        def action_of(self, group_element):
            return self.action()(group_element)

        def is_invariant(self, vector) -> bool:
            group = self.group()
            assert group.is_finitely_generated() is True
            return all(self.act(group_generator, vector) == vector for group_generator in group.group_generators())

        def module_invariants(self):
            r"""Return the native fixed submodule of the underlying group module."""
            return self._preamble_group_module.module_invariants()

        def invariant_lattice(self):
            r"""Return ``L^G`` as a formed subobject of this lattice.

            This intersects the fixed lattices of a chosen finite generating
            set.  It deliberately does not reuse ``module_invariants()``, whose
            codomain is the unformed underlying module.
            """
            group = self.group()
            if group.is_finitely_generated() is not True:
                raise NotImplementedError("constructing an invariant lattice requires a chosen finite group generating set")
            generators = tuple(group.group_generators())
            if not generators:
                return self.subobject_on(self.module_generators())
            invariants = self.action_of(generators[0]).invariant_lattice()
            for generator in generators[1:]:
                invariants = invariants.intersection(self.action_of(generator).invariant_lattice())
            return invariants

        def module_coinvariants(self):
            r"""Return the underlying module quotient by ``(g-1)M``."""
            return self._preamble_group_module.module_coinvariants()

        def formed_coinvariants(self):
            r"""Return ``(L^G)^perp`` as a formed subobject of ``L``.

            Module coinvariants remain available separately as
            ``module_coinvariants() = L / <g v-v>``.
            """
            return self.invariant_lattice().orthogonal_complement()

        def character(self):
            return self._preamble_group_module.character()


def GroupLattice(lattice, group_or_action, action=None):
    r"""Equip ``lattice`` with a selected action preserving its form."""

    base_ring = lattice.base_ring()
    assert lattice in FiniteRankLattices(base_ring)
    source_group_module = GroupModule(lattice, group_or_action, action)
    group = source_group_module.group()

    result = Lattices(base_ring)(
        lattice.gram_tensor(),
        module_generators=lattice.module_generating_set(),
    )

    assert group.is_finitely_generated() is True

    def transported_image(group_element, label):
        backing_image = source_group_module.act(
            group_element,
            source_group_module.module_generator(label),
        )
        return result.linear_combination(
            module_coefficients(backing_image, source_group_module)
        )

    orthogonal_group = result.Aut()
    lattice_action = SetMorphism(
        Sets().Mor(group, orthogonal_group),
        lambda group_element: orthogonal_group(
            lambda label: transported_image(group_element, label)
        ),
    )

    # The selected action is represented by a map into Aut(L).  For a chosen
    # finite group presentation it suffices to force the generator images
    # through that Hom here; form preservation and invertibility are owned by
    # the lattice-isometry constructor.
    for group_generator in group.group_generators():
        lattice_action(group_generator)

    group_module = GroupModule(result, lattice_action)
    result._preamble_group_module = group_module
    result._preamble_lattice_action = lattice_action

    result = refine(result, GroupLattices(base_ring, group))


    if lattice in RootLattices():
        result = result.lattice_category()._refine_root_lattice(
            result, lattice.cartan_type()
        )
    return result


__all__ = ["GroupLattice", "GroupLattices"]
