r"""Integral lattices equipped with a group action by isometries."""

from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.group_modules.characters import Character
    from dzack_research.preamble.lexicon import Element
    from sage.categories.groups import Group
    from sage.matrix.matrix0 import Matrix
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import ModuleElement

from sage.rings.integer_ring import ZZ as SageZZ
from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
from dzack_research.preamble.categories.modules.framed.formed.form_modules import is_form_morphism
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import GroupAction, GroupActionHomsets
if TYPE_CHECKING:
    from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import DirectSumObject
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from sage.categories.homset import Homset

import logging
from typing import Self, TYPE_CHECKING

from sage.misc.cachefunc import cached_function, cached_method
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category, HomCategoryConstruction
from sage.categories.morphism import SetMorphism

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    from collections.abc import Callable

    from sage.categories.morphism import Morphism

    from dzack_research.preamble.categories.forms.forms import Form
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.structure.parent import Parent

    # The admissible ways to name an equivariant form-preserving map, in the
    # order the constructors match them: an existing morphism (``SetMorphism``
    # and the preamble's ``ModuleMorphism`` are both ``Morphism``), a finite
    # assignment of generator images, or any function on the generating set.
    # Drawn from Sage's hierarchy rather than the preamble's own classes,
    # because a union is a type only when every member is one and the preamble
    # has no stubs yet (issue #354).
    EquivariantAssignment = Morphism | dict | Callable

    class GroupLatticeParent(Protocol):
        r"""What a parent placed in ``GroupLattices(G)`` supplies."""

        def base_ring(self) -> "Ring": ...
        def form(self) -> "Form": ...
        def group(self) -> "Group": ...
        def action_of(self, element: "Element") -> Morphism: ...
        def _over(self, element: "Element") -> "ModuleElement": ...

        # The category's own operations, which its methods call on each other.
        def act(self, element: "Element", vector_: "ModuleElement") -> "ModuleElement": ...
        def subobject_on(self, module_generators: "OrderedSet") -> "Subobject": ...
        def isotypic_decomposition(self) -> "DirectSumObject": ...
        def invariant_lattice(self) -> "Subobject": ...
        def _equip(self, submodule: "Module") -> "Module": ...

class GroupLattices(Category):
    r"""The pullback of \(G\)-modules and integral lattices."""

    def __init__(self, group: "Group") -> None:
        # Finiteness is not what a G-lattice needs.  Equivariance is checked
        # on generators, so the requirement is a generating set -- and an
        # infinite-order isometry generates an infinite cyclic group with one
        # of them.  A group that cannot produce generators is still a group
        # acting on a lattice; its morphisms go unchecked and say so.
        self._group = group
        Category.__init__(self)

    def acting_group(self) -> "Group":
        return self._group

    def base_ring(self) -> "Ring":
        return SageZZ

    def _repr_object_names(self) -> str:
        return f"integral lattices with an action of {self._group}"

    def super_categories(self) -> list:
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
        from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModules

        return [
            GroupModules(SageZZ, self._group),
            IntegralLattices(SageZZ),
        ]

    class ParentMethods:
        def is_integral(self: "GroupLatticeParent") -> bool:
            return all(
                bool(entry.is_integral())
                for row in self.gram_matrix().rows()
                for entry in row
            )

        def is_nondegenerate(self: "GroupLatticeParent") -> bool:
            return bool(self.gram_matrix().determinant() != 0)

        def _Hom_(self: Self, codomain: "Module", category: "Category | None" = None) -> "Homset":
            r"""Return the homset in the strongest owned category of both ends."""
            from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModules

            if category is None and codomain in GroupModules(self.base_ring(), self.group()):
                category = GroupLattices(self.group())
            homset: "Homset" = super()._Hom_(codomain, category)
            return homset

        def subobject_on(self: "GroupLatticeParent", module_generators: "OrderedSet") -> "Subobject":
            module_generators = tuple(module_generators)
            assert all(generator in self for generator in module_generators), (
                "a subobject is generated by elements of this group lattice"
            )
            # The $G$-module's own subobject, on these same elements: a
            # $G$-lattice is that module, so there is nothing to take down to
            # it first -- and ``self.subobject_on`` is this method.
            # Local: a module-level import would close a cycle; the module is
            # built by the time a subobject is asked for.
            from dzack_research.preamble.categories.modules.group_modules.group_modules import _group_subobject

            representation_subobject = _group_subobject(self, module_generators)
            return _formed_group_subobject(self, representation_subobject)

        def isotypic_lattice(self: "GroupLatticeParent", character: "Character") -> "Subobject":
            return self._equip(
                self.isotypic_decomposition().summand(character)
            )

        @cached_method
        def invariant_lattice(self: "GroupLatticeParent") -> "Subobject":
            return self._equip(self.module_invariants())

        @cached_method
        def coinvariant_lattice(self: "GroupLatticeParent") -> "Subobject":
            return self.invariant_lattice().structure_morphism().orthogonal_complement()

        formed_coinvariants = coinvariant_lattice

        def _equip(self: "GroupLatticeParent", submodule: "Module") -> "Module":
            assert submodule.structure_morphism().codomain() is self, (
                "the group submodule belongs to a different representation"
            )
            return _formed_group_subobject(self, submodule)

    class _HomCategory(HomCategoryConstruction):
        r"""Form-preserving equivariant maps of two lattices for one \(G\)."""

        def extra_super_categories(self) -> list:
            r"""A homset of \(G\)-lattices is a homset of formed modules.

            Adding the action changes the *condition* on a morphism, never the
            datum that names one: it is the same generator assignment, plus
            equivariance.  Without this edge the owned homset chain reached
            only its root, so every spelling but an existing morphism fell
            through to Sage's ``Homset``, which converts none of them.
            """
            # Local: a module-level import would close a cycle; the module is
            # built by the time supercategories are asked for.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules

            return super().extra_super_categories() + [
                FormModules(SageZZ).HomCategory()
            ]

        class ParentMethods:
            def __init__(
                self,
                domain: "Module",
                codomain: "Module",
                **rest: "ConstructionData",
            ) -> None:
                assert codomain in GroupLattices(domain.group()), (
                    "the codomain is not a lattice for the stated group"
                )
                assert domain.group() == codomain.group(), (
                    "a group-lattice homset has one specified acting group"
                )
                super().__init__(domain=domain, codomain=codomain, **rest)

            def _element_constructor_(self, images: "EquivariantAssignment", check_equivariance: bool = False) -> Morphism:
                r"""Build the morphism, and check equivariance where that is possible.

                ``check_equivariance`` forces the check in the branches that would
                otherwise decline it.  It sits on morphism construction, not on the
                homset: one homset serves many morphisms, and whether a given one was
                checked is a fact about that morphism.
                """
                # Local: a module-level import would close a cycle; the module is built by the time this runs.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

                match images:
                    case _ if is_form_morphism(images):
                        assert images.parent() is self, (
                            "an existing group-lattice morphism belongs to its own homset"
                        )
                        return images
                    case ModuleMorphism() | SetMorphism() | dict():
                        morphism = super()._element_constructor_(images)
                    case _ if callable(images):
                        morphism = super()._element_constructor_(images)
                    case _:
                        assert False, (
                            "a group-lattice morphism is specified by its generator "
                            "morphism or finite generator assignment"
                        )
                self._check_equivariance(morphism, forced=check_equivariance)
                return morphism

            def _check_equivariance(self, morphism: Morphism, forced: bool) -> None:
                r"""Check \(f(g\cdot m)=g\cdot f(m)\), and record whether it happened.

                The check ranges over *generators*, of the group and of the module.
                A module map commuting with a generating set commutes with the whole
                group, because the action is by module maps and the identity extends
                along products -- so the check is \(|S|\times|\text{module generators}|\)
                comparisons, and finiteness of \(G\) is not what it needs.  Ranging
                over \(G\) itself is what forced the finiteness assumption and shut
                out every infinite-order isometry, which is the generic case for an
                indefinite lattice.

                A finitely generated group carries its generating set as category
                data, so the check uses it.  For another group, ``forced`` requires
                that datum and an unforced construction records that it did not
                perform the check.
                """
                # Local: a module-level import would close a cycle; the module is built by the time this runs.
                from dzack_research.preamble.categories.group.groups import refine_group

                group = refine_group(self.domain().group())
                morphism._equivariance_checked = False

                if group.is_finitely_generated() is not True:
                    assert not forced, (
                        "a forced equivariance check requires a group with a "
                        "specified finite generating set"
                    )
                    logging.info(
                        "%s has no specified finite generating set; the morphism "
                        "is not checked for equivariance",
                        group,
                    )
                    return

                domain = self.domain()
                codomain = self.codomain()
                assert all(
                    morphism(domain.act(generator, domain.module_generator(element_of_S)))
                    == codomain.act(
                        generator,
                        morphism(domain.module_generator(element_of_S)),
                    )
                    for generator in group.group_generators()
                    for element_of_S in domain.module_generating_set()
                ), "the proposed lattice map is not equivariant"
                morphism._equivariance_checked = True

            def _repr_(self) -> str:
                return (
                    f"Isometric Hom_{self.domain().group()}("
                    f"{self.domain()}, {self.codomain()})"
                )


@cached_function
def group_lattice_homset(domain: "Module", codomain: "Module") -> Parent:
    r"""Return the canonical form-preserving equivariant homset."""
    homset: Parent = domain._Hom_(codomain, GroupLattices(domain.group()))
    return homset


def _action_preserves_form(formed_module: "Module") -> bool:
    r"""Whether every $g$ acts by an isometry: $\rho(g)^*b = b$.
    """
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    form = formed_module.form()
    module = form.module()
    for element in formed_module.group().group_generators():
        action = formed_module.action_of(element)
        underlying_action = module.Hom(module, Modules(module.base_ring()))(
            {
                label: action(generator).underlying_element()
                for label, generator in zip(
                    module.module_generating_set(),
                    formed_module.module_generators(),
                )
            }
        )
        if form.pullback(underlying_action) != form:
            return False
    return True


def _formed_group_subobject(
    group_lattice_: "FormModule",
    representation_subobject: "Subobject",
) -> "Subobject":
    r"""Equip a \(G\)-submodule with the pulled-back form and its inclusion."""
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    module_embedding = representation_subobject.structure_morphism()
    representation = module_embedding.domain()
    form_module = group_lattice_.form().module()
    underlying_embedding = representation.Hom(
        form_module,
        Modules(representation.base_ring()),
    )(
        {
            label: module_embedding(
                representation.module_generator(label)
            ).underlying_element()
            for label in representation.module_generating_set()
        }
    )
    from dzack_research.preamble.refine import refine

    group_lattices = GroupLattices(group_lattice_.group())
    restricted = object_of(
        group_lattices,
        form=group_lattice_.form().pullback(underlying_embedding),
        action=representation.action(),
        module_generating_set=representation.module_generating_set(),
    )
    restricted = refine(restricted, group_lattices)
    embedding = restricted.Hom(group_lattice_)(
        {
            label: group_lattice_._over(
                module_embedding(representation.module_generator(label))
            )
            for label in representation.module_generating_set()
        }
    )
    return Subobject(embedding)


def group_lattice(lattice: "FormModule", action: GroupAction) -> FormModule:
    r"""Equip ``lattice`` with the specified action by isometries."""
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
    from dzack_research.preamble.refine import refine

    assert lattice in IntegralLattices(SageZZ), (
        "a group lattice is constructed from an actual integral lattice"
    )
    assert (
        isinstance(action, GroupAction)
        and action.codomain().domain() is lattice
        and action.parent() in GroupActionHomsets()
    ), "the action must be an element of the lattice's action homset"

    formed_module = object_of(
        GroupLattices(action.domain()),
        form=lattice.form(),
        action=action,
        module_generating_set=lattice.module_generating_set(),
    )
    return refine(formed_module, GroupLattices(action.domain()))
