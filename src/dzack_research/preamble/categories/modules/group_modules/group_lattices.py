r"""Lattices equipped with a chosen form-preserving group action."""

from sage.categories.category import Category
from sage.categories.morphism import SetMorphism
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebra
from dzack_research.preamble.categories.group.groups import _owned_group
from dzack_research.preamble.categories.lattices import (
    FiniteRankLattices,
    Lattice,
    Lattices,
    RootLattices,
)
from dzack_research.preamble.categories.modules.group_modules.group_modules import _equip_action
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_coefficients
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.sets.set_categories import Sets


class GroupLattices(OwnedCategory):
    r"""Lattices carrying a specified action by lattice isometries."""

    @staticmethod
    def __classcall__(cls, base_ring, group):
        return Category.__classcall__(cls, _owned_ring(base_ring), _owned_group(group))

    def __init__(self, base_ring, group) -> None:
        self._base_ring = base_ring
        self._group = group
        OwnedCategory.__init__(self)

    def base_ring(self):
        return self._base_ring

    def acting_group(self):
        return self._group

    def _repr_object_names(self):
        return f"{self.acting_group()}-lattices over {self.base_ring()}"

    def super_categories(self):

        return [
            Lattices(self.base_ring()),
            Modules(GroupAlgebra(self.base_ring(), self.acting_group())),
        ]

    class ParentMethods:
        def group(self):
            return self._preamble_group_module_source.group()

        def is_trivial_action(self) -> bool:
            return self._preamble_group_module_source.is_trivial_action()

        def unacted_module(self):
            return self._preamble_group_module_source.unacted_module()

        @cached_method
        def action(self):
            source_group_module = self._preamble_group_module_source
            group = source_group_module.group()

            def transported_image(group_element, label):
                backing_image = source_group_module.act(
                    group_element,
                    source_group_module.module_generator(label),
                )
                return self.linear_combination(
                    module_coefficients(backing_image, source_group_module)
                )

            orthogonal_group = self.Aut()
            action = SetMorphism(
                Sets().Mor(group, orthogonal_group),
                lambda group_element: orthogonal_group(
                    lambda label: transported_image(group_element, label)
                ),
            )
            assert group.is_finitely_generated() is True
            for group_generator in group.group_generators():
                action(group_generator)
            return action

        @cached_method
        def group_module(self):
            return _equip_action(self, self.action())

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
            return self.group_module().module_invariants()

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
            return self.group_module().module_coinvariants()

        def formed_coinvariants(self):
            r"""Return ``(L^G)^perp`` as a formed subobject of ``L``.

            Module coinvariants remain available separately as
            ``module_coinvariants() = L / <g v-v>``.
            """
            return self.invariant_lattice().orthogonal_complement()

        def character(self):
            return self.group_module().character()


def GroupLattice(lattice, group_or_action, action=None):
    r"""Equip ``lattice`` with a selected action preserving its form."""

    base_ring = lattice.base_ring()
    assert lattice in FiniteRankLattices(base_ring)
    source_group_module = _equip_action(lattice, group_or_action, action)
    group = source_group_module.group()

    prototype = Lattices(base_ring)(
        lattice.gram_tensor(),
        module_generators=lattice.module_generating_set(),
    )
    extra_categories = [GroupLattices(base_ring, group)]
    construction_data = [("group_module_source", source_group_module)]
    if lattice in RootLattices():
        extra_categories.append(RootLattices())
        construction_data.append(("cartan_type", lattice.cartan_type()))
    result = Lattice(
        prototype._module,
        prototype.gram_tensor(),
        Lattices(base_ring),
        prototype._sage_lattice,
        extra_categories=tuple(extra_categories),
        construction_data=tuple(construction_data),
    )
    result = result.lattice_category()._refine_lattice_object(result)
    assert group.is_finitely_generated() is True
    for group_generator in group.group_generators():
        result.action()(group_generator)
    return result


__all__ = ["GroupLattice", "GroupLattices"]
