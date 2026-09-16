r"""Lattices with a group action: ``Lattices(R[G])``.

An object of ``Lattices(R[G])`` is an ``R[G]``-module whose underlying
``R``-module is a lattice with a form the group preserves, so the action is
a group morphism ``G -> O(L)``.  ``Lattices(S)`` constructs this category
whenever ``S`` is a group algebra; the constructor is
``Lattices(R[G])(L, action)``.
"""

from sage.categories.morphism import SetMorphism
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.lattice_morphisms import (
    LatticeHomset,
    LatticeMorphism,
)
from dzack_research.preamble.categories.lattices import (
    FiniteRankLattices,
    Lattices,
    RootLattices,
)
from dzack_research.preamble.categories.modules.group_modules.group_modules import (
    ModulesOverGroupAlgebra,
    _equip_action,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


class GroupLatticeMorphism(LatticeMorphism):
    r"""A form-preserving equivariant morphism of lattices with one group action."""

    def __mul__(self, other):
        if not isinstance(other, GroupLatticeMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain()).elementwise(
            lambda element: self(other(element))
        )


class GroupLatticeHomset(LatticeHomset):
    r"""Form-preserving maps commuting with one selected group action."""

    Element = GroupLatticeMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if domain.group() != codomain.group():
            raise ValueError("a group-lattice Hom has one acting group")
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("a group-lattice Hom has one coefficient ring")
        super().__init__(hom_family, domain, codomain)

    def _check_equivariance(self, morphism) -> None:
        group = self.domain().group()
        assert group.is_finitely_generated() is True, (
            "verifying a group-lattice morphism requires a represented finite generating set of the acting group"
        )
        domain = self.domain()
        codomain = self.codomain()
        for group_generator in group.group_generators():
            for label in domain.module_generating_set():
                vector = domain.module_generator(label)
                if morphism(domain.act(group_generator, vector)) != codomain.act(
                    group_generator, morphism(vector)
                ):
                    raise ValueError("a group-lattice morphism must be G-equivariant")

    def _element_constructor_(self, images):
        morphism = super()._element_constructor_(images)
        self._check_equivariance(morphism)
        return morphism

    def elementwise(self, function, *, verify_linearity=True):
        morphism = super().elementwise(function, verify_linearity=verify_linearity)
        self._check_equivariance(morphism)
        return morphism


class GroupLatticeHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GroupLatticeHomset


class LatticesOverGroupAlgebra(OwnedCategoryOverBaseRing):
    r"""``Lattices(R[G])``: lattices over ``R`` carrying an action by isometries."""

    def group_algebra(self):
        return self.base_ring()

    def coefficient_ring(self):
        return self.base_ring().base_ring()

    def acting_group(self):
        return self.base_ring().group()

    def _repr_object_names(self):
        return f"lattices over {self.base_ring()}"

    def super_categories(self):
        return [
            GObjects(self.acting_group(), Lattices(self.coefficient_ring())),
            ModulesOverGroupAlgebra(self.base_ring()),
        ]

    _HomCategory = GroupLatticeHomCategoryConstruction

    def an_object(self):
        r"""The hyperbolic plane with the swap of its two isotropic generators."""
        plane = Lattices(self.coefficient_ring())("U")
        labels = plane.module_generating_set()
        left, right = plane.module_generators()
        swap = plane.Aut()({labels[0]: right, labels[1]: left})
        group = self.acting_group()
        assert group.cardinality() == 2, "the sample action is a swap, an action of C_2"
        return self(plane, lambda g, vector: vector if g == group.one() else swap(vector))

    def _call_(self, lattice, action):
        r"""Equip ``lattice`` with the action ``action(g, v)``, which must preserve its form."""
        return _group_lattice(lattice, self.acting_group(), action)

    class ParentMethods:
        def group(self):
            return self._preamble_group_module_source.group()

        def group_algebra(self):
            return self._preamble_group_module_source.group_algebra()

        def Mor(self, codomain, category=None):
            group_lattices = Lattices(self.group_algebra())
            if codomain in group_lattices and (
                category is None or category.is_subcategory(group_lattices)
            ):
                return group_lattices.Mor(self, codomain)
            return super().Mor(codomain, category)

        def _Hom_(self, codomain, category=None):
            group_lattices = Lattices(self.group_algebra())
            if codomain in group_lattices and (
                category is None or category.is_subcategory(group_lattices)
            ):
                return group_lattices.Mor(self, codomain)
            return super()._Hom_(codomain, category)

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
                    source_group_module.framing_coefficients(backing_image)
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
            assert group.is_finitely_generated() is True, (
                "constructing an invariant lattice requires a chosen finite group generating set"
            )
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

        @cached_method
        def coinvariant_lattice(self):
            r"""Return ``(L^G)^perp`` as a formed subobject of ``L``.

            Module coinvariants remain available separately as
            ``module_coinvariants() = L / <g v-v>``.
            """
            return self.invariant_lattice().orthogonal_complement()

        formed_coinvariants = coinvariant_lattice

        def isotypic_lattice(self, character):
            r"""Return the formed ``character``-isotypic sublattice with its restricted action.

            The underlying module component is the exact isotypic subobject of
            the associated ``R[G]``-module.  Its embedded basis is used to
            rebuild the restricted lattice form, and the ambient action is
            then restricted through that represented inclusion.  The result
            remains a subobject of this lattice rather than an isomorphic
            detached copy.
            """
            component = self.group_module().isotypic_component(character)
            module_inclusion = component.inclusion()
            component_module = module_inclusion.domain()
            if module_inclusion.codomain() is not self:
                raise ArithmeticError(
                    "the isotypic module component is not embedded in the group lattice"
                )
            embedded_basis = tuple(
                module_inclusion(component_module.module_generator(label))
                for label in component_module.module_generating_set()
            )
            formed = self.subobject_on(embedded_basis)
            inclusion = formed.inclusion()

            def restricted_action(group_element, vector):
                return inclusion.lift(
                    self.action_of(group_element)(inclusion(vector))
                )

            return Lattices(self.group_algebra())(formed, restricted_action)

        def character(self):
            return self.group_module().character()


def _group_lattice(lattice, group_or_action, action=None):
    r"""Equip ``lattice`` with a selected action preserving its form."""

    base_ring = lattice.base_ring()
    assert lattice in FiniteRankLattices(base_ring)
    source_group_module = _equip_action(lattice, group_or_action, action)
    group = source_group_module.group()

    prototype = Lattices(base_ring)(
        lattice.gram_tensor(),
        module_generators=lattice.module_generating_set(),
    )
    extra_categories = [Lattices(base_ring[group])]
    construction_data = [("group_module_source", source_group_module)]
    if lattice in RootLattices():
        extra_categories.append(RootLattices())
        construction_data.append(("cartan_type", lattice.cartan_type()))
    result = Lattices(base_ring)._specialize_existing_lattice(
        prototype,
        extra_categories=tuple(extra_categories),
        construction_data=tuple(construction_data),
        subobject_source=lattice,
    )
    assert group.is_finitely_generated() is True
    for group_generator in group.group_generators():
        result.action()(group_generator)
    return result



__all__ = [
    "GroupLatticeHomCategoryConstruction",
    "GroupLatticeHomset",
    "GroupLatticeMorphism",
    "LatticesOverGroupAlgebra",
]
