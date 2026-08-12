r"""Integral lattices equipped with a group action by isometries."""

from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.group_modules.characters import Character
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.lexicon import Group
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from dzack_research.preamble.lexicon import Module
    from dzack_research.preamble.lexicon import ModuleElement
    from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix

from sage.rings.integer_ring import ZZ as SageZZ
from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import GroupAction
from sage.structure.parent import Parent
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.direct_sum_objects import DirectSumObject
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from sage.categories.homset import Homset

from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormHomset
import logging
from typing import Self, TYPE_CHECKING

from sage.misc.cachefunc import cached_method
from sage.categories.category import Category
from sage.categories.morphism import SetMorphism

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    from collections.abc import Callable

    from sage.categories.morphism import Morphism

    from dzack_research.preamble.categories.forms.forms import Form

    # The admissible ways to name an equivariant form-preserving map, in the
    # order the constructors match them: an existing morphism (``SetMorphism``
    # and the preamble's ``ModuleMorphism`` are both ``Morphism``), a finite
    # assignment of generator images, or any function on the generating set.
    # Drawn from Sage's hierarchy rather than the preamble's own classes,
    # because a union is a type only when every member is one and the preamble
    # has no stubs yet (issue #354).
    EquivariantAssignment = Morphism | dict | Callable

    class GroupLatticeParent(Protocol):
        r"""What a parent placed in ``GroupLattices(G)`` supplies: the ring
        underneath, the two forgetful maps off the pair $(L,\rho)$, the form
        itself, and this parent's own element wrapping."""

        def base_ring(self) -> "Ring": ...
        def forget_form(self) -> "Module": ...
        def form(self) -> "Form": ...
        def group(self) -> "Group": ...
        def action_of(self, element: "Element") -> FormMorphism: ...
        def module_representation(self) -> "Module": ...
        def _over(self, element: "Element") -> "ModuleElement": ...

        # Installed on the object by the constructor: $\rho$ recorded through
        # the form-bearing wrapping, so it moves this parent's own elements.
        _formed_action: GroupAction

        # The category's own operations, which its methods call on each other.
        def forget_action(self) -> "Module": ...
        def act(self, element: "Element", vector_: "ModuleElement") -> "ModuleElement": ...
        def subobject_on(self, module_generators: "OrderedSet") -> "Subobject": ...
        def isotypic_decomposition(self) -> "DirectSumObject": ...
        def invariant_lattice(self) -> "Subobject": ...
        def _equip(self, submodule: "Module") -> "Module": ...

    class GroupLatticeElement(Protocol):
        r"""What an element of a group lattice supplies: the lattice it lies
        in, and its image after the form is forgotten."""

        def parent(self) -> "GroupLatticeParent": ...
        def forget_form(self) -> "ModuleElement": ...



# ``ParentMethods`` methods run on parents, but a bare methods class has no
# base to say so, and ``Parent.Hom``'s fallback branch needs nominal
# parenthood.  Runtime-identical: a bare class already derives from object.
if TYPE_CHECKING:
    _ParentBase = Parent
else:
    _ParentBase = object

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

    def _repr_object_names(self) -> str:
        return f"integral lattices with an action of {self._group}"

    def super_categories(self) -> list:
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
        from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModules

        return [
            GroupModules(SageZZ, self._group),
            IntegralLattices(),
        ]

    class ParentMethods(_ParentBase):
        # Installed on the object by the constructor: $\rho$ recorded through
        # the form-bearing wrapping, so it moves this parent's own elements.
        _formed_action: GroupAction

        def Hom(self: Self, codomain: "Module", category: "Category | None" = None) -> "Homset":
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModules

            if codomain in GroupModules(self.base_ring(), self.group()):
                return group_lattice_homset(self, codomain)
            return Parent.Hom(self, codomain, category)

        def hom(self: "GroupLatticeParent", images: "EquivariantAssignment", codomain: "Module | None" = None) -> "ModuleMorphism":
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FinitelyGeneratedFormModules

            return FinitelyGeneratedFormModules.ParentMethods.hom(
                self,
                images,
                codomain,
            )

        def module_representation(self: "GroupLatticeParent") -> "Module":
            r"""Forget the form and retain the specified \(G\)-module."""
            return self.forget_form()

        @cached_method
        def forget_action(self: "GroupLatticeParent") -> "Module":
            r"""Forget the action and retain the formed module."""
            stored = self.__dict__.get("_action_forgotten_form")
            if stored is not None:
                return stored
            module = self.forget_form().forget_action()
            stored = FormModule(self.form().on_module(module))
            self._action_forgotten_form = stored
            return stored

        def action(self: "GroupLatticeParent") -> GroupAction:
            return self._formed_action

        def group(self: Self) -> "Group":
            return self._formed_action.domain()

        def action_of(self: "GroupLatticeParent", element: "Element") -> FormMorphism:
            return self._formed_action(element)

        def action_matrix(self: "GroupLatticeParent", element: "Element") -> "MorphismMatrix":
            return self.action_of(element).matrix()

        def act(self: "GroupLatticeParent", element: "Element", vector_: "ModuleElement") -> "ModuleElement":
            return self.action_of(element)(vector_)

        def is_invariant(self: "GroupLatticeParent", vector_: "ModuleElement") -> bool:
            r"""Return whether \(g\cdot v=v\) for every \(g\in G\).

            Decided on generators: the elements fixing \(v\) form a
            subgroup, so it contains \(G\) as soon as it contains a
            generating set.
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.group.groups import refine_group

            return all(
                self.act(generator, vector_) == vector_
                for generator in refine_group(self.group()).group_generators()
            )

        def subobject_on(self: "GroupLatticeParent", module_generators: "OrderedSet") -> "Subobject":
            module_generators = tuple(module_generators)
            assert all(generator.parent() is self for generator in module_generators), (
                "a subobject is generated by elements of this group lattice"
            )
            representation_subobject = self.module_representation().subobject_on(
                [generator.forget_form() for generator in module_generators]
            )
            return _formed_group_subobject(self, representation_subobject)

        def isotypic_decomposition(self: "GroupLatticeParent") -> "DirectSumObject":
            return self.module_representation().isotypic_decomposition()

        def isotypic_lattice(self: "GroupLatticeParent", character: "Character") -> "Subobject":
            return self._equip(
                self.isotypic_decomposition().summand(character)
            )

        @cached_method
        def invariant_lattice(self: "GroupLatticeParent") -> "Subobject":
            return self._equip(self.module_representation().module_invariants())

        @cached_method
        def coinvariant_lattice(self: "GroupLatticeParent") -> "Subobject":
            return self.invariant_lattice().embedding().orthogonal_complement()

        formed_coinvariants = coinvariant_lattice

        def _over_forgotten(self: "GroupLatticeParent", element: "Element") -> "Element":
            r"""Return the element of this \(G\)-lattice underlying ``element``.

            The inverse of :meth:`ElementMethods.forget_action`: forgetting
            the action does not change which elements there are, so the two
            are a bijection and this is the other half of it.
            """
            assert element.parent() is self.forget_action(), (
                f"{element} is not an element of {self.forget_action()}"
            )
            return self._over(self.forget_form()._over(element.forget_form()))

        def _equip(self: "GroupLatticeParent", submodule: "Module") -> "Module":
            assert submodule.embedding_codomain() is self.module_representation(), (
                "the group submodule belongs to a different representation"
            )
            return _formed_group_subobject(self, submodule)

    class ElementMethods:
        def forget_action(self: "GroupLatticeElement") -> "Module":
            lattice = self.parent().forget_action()
            return lattice._over(
                self.forget_form().forget_action()
            )



class GroupLatticeHomset(FormHomset):
    r"""Form-preserving equivariant maps of two lattices for one \(G\)."""

    def __init__(self, domain: "Module", codomain: "Module") -> None:
        assert codomain in GroupLattices(domain.group()), (
            "the codomain is not a lattice for the stated group"
        )
        assert domain.group() == codomain.group(), (
            "a group-lattice homset has one specified acting group"
        )
        FormHomset.__init__(
            self,
            domain,
            codomain,
            GroupLattices(domain.group()),
        )

    def _element_constructor_(self, images: "EquivariantAssignment", check_equivariance: bool = False) -> FormMorphism:
        r"""Build the morphism, and check equivariance where that is possible.

        ``check_equivariance`` forces the check in the branches that would
        otherwise decline it.  It sits on morphism construction, not on the
        homset: one homset serves many morphisms, and whether a given one was
        checked is a fact about that morphism.
        """
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

        match images:
            case FormMorphism():
                assert images.parent() is self, (
                    "an existing group-lattice morphism belongs to its own homset"
                )
                return images
            case ModuleMorphism() | SetMorphism() | dict():
                morphism = FormHomset._element_constructor_(self, images)
            case _ if callable(images):
                morphism = FormHomset._element_constructor_(self, images)
            case _:
                assert False, (
                    "a group-lattice morphism is specified by its generator "
                    "morphism or finite generator assignment"
                )
        self._check_equivariance(morphism, forced=check_equivariance)
        return morphism

    def _check_equivariance(self, morphism: FormMorphism, forced: bool) -> None:
        r"""Check \(f(g\cdot m)=g\cdot f(m)\), and record whether it happened.

        The check ranges over *generators*, of the group and of the module.
        A module map commuting with a generating set commutes with the whole
        group, because the action is by module maps and the identity extends
        along products -- so the check is \(|S|\times|\text{module generators}|\)
        comparisons, and finiteness of \(G\) is not what it needs.  Ranging
        over \(G\) itself is what forced the finiteness assumption and shut
        out every infinite-order isometry, which is the generic case for an
        indefinite lattice.

        Four routes, and the morphism records which one it took:

        - generators already in hand: check, always, since it is free;
        - computable but not yet computed: check when forced, otherwise say
          so and leave the morphism unchecked, since the computation can be
          long -- \(O(L)\) for a definite lattice;
        - not known to be finitely generated: with ``forced``, assert; the
          assertion is the honest statement that no algorithm is known here.
          Unforced, say so and leave it unchecked;
        - no generators at all: ask anyway when forced, and let the group
          fail however it chooses.
        """
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.group.groups import refine_group

        group = refine_group(self.domain().group())
        morphism._equivariance_checked = False

        if group.has_computed_group_generators() is not True:
            if group.is_finitely_generated() is not True:
                if forced:
                    assert group.is_finitely_generated() is True, (
                        "no known way to check equivariance computationally "
                        "for non-finitely-generated groups yet"
                    )
                logging.info(
                    "%s is not known to be finitely generated; the morphism "
                    "is not checked for equivariance",
                    group,
                )
                return
            if group.group_generators_are_computable() is not True:
                logging.info(
                    "no algorithm is known to produce generators of %s; the "
                    "morphism is not checked for equivariance",
                    group,
                )
                return
            if not forced:
                logging.info(
                    "generators of %s are computable but not yet computed; "
                    "pass check_equivariance=True to compute them and check",
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


def group_lattice_homset(domain: "Module", codomain: "Module") -> GroupLatticeHomset:
    r"""Return the canonical form-preserving equivariant homset."""
    cache = domain.__dict__.setdefault("_group_lattice_homsets", {})
    homset: GroupLatticeHomset | None = cache.get(codomain)
    if homset is None:
        homset = GroupLatticeHomset(domain, codomain)
        cache[codomain] = homset
    return homset


def _action_preserves_form(formed_module: "Module") -> bool:
    module = formed_module.forget_form()
    return all(
        formed_module.form().pullback(module.action_of(element))
        == formed_module.form()
        for element in module.group()
    )


def _install_group_lattice_structure(formed_module: "Module") -> None:
    r"""Install the action on a formed \(G\)-module after invariance is known."""
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import group_action_homset

    module = formed_module.forget_form()
    group = module.group()
    isometries = formed_module.Aut()
    values = {
        element: isometries(
            {
                label: formed_module._over(
                    module.action_of(element)(module.module_generator(label))
                )
                for label in module.module_generating_set()
            }
        )
        for element in group
    }
    formed_module._formed_action = group_action_homset(
        group,
        formed_module,
    )(values)


def _formed_group_subobject(
    group_lattice_: "FormModule",
    representation_subobject: "Subobject",
) -> "Subobject":
    r"""Equip a \(G\)-submodule with the pulled-back form and its inclusion."""
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject

    module_embedding = representation_subobject.embedding()
    representation = module_embedding.domain()
    restricted = FormModule(
        group_lattice_.form().pullback(module_embedding)
    )
    assert restricted in GroupLattices(group_lattice_.group()), (
        "a stable submodule of a group lattice must inherit the isometric action"
    )
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
    from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import group_action_homset

    assert lattice in IntegralLattices(), (
        "a group lattice is constructed from an actual integral lattice"
    )
    assert (
        isinstance(action, GroupAction)
        and action.module() is lattice
        and action.parent() is group_action_homset(action.domain(), lattice)
    ), "the action must be an element of the lattice's action homset"

    module = lattice.forget_form()
    automorphisms = module.Aut()
    values = {
        element: automorphisms(
            {
                label: action(element)(
                    lattice.module_generator(label)
                ).forget_form()
                for label in module.module_generating_set()
            }
        )
        for element in action.domain()
    }
    representation = GroupModule(
        module,
        group_action_homset(action.domain(), module)(values),
    )
    formed_module = FormModule(
        lattice.form().on_module(representation)
    )
    assert formed_module in GroupLattices(action.domain()), (
        "the supplied action did not refine to isometries"
    )
    formed_module._action_forgotten_form = lattice
    return formed_module
