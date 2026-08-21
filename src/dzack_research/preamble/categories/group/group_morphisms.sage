r"""Native homsets, homomorphisms, and \(\operatorname{Aut}(G)\) for owned groups.

A homomorphism out of a group is declared by the images of its distinguished
generators -- the house spelling is a dictionary ``{generator: image}`` -- and
its parent is the canonical homset of the named domain and codomain, placed in
the owned groups category.  Construction checks the relations of the domain,
so membership in a homset is parenthood and nothing else.

The engine behind construction and application is GAP, consumed through Sage's
maintained :class:`~sage.groups.libgap_morphism.GroupMorphism_libgap` and
:class:`~sage.groups.libgap_morphism.GroupHomset_libgap` rather than
reimplemented: the owned classes subclass them, add the house spelling, and
translate every answer back into the group's own elements.
\(\operatorname{Aut}(G)\) is the endomorphism homset with one more condition
on its elements, refined into the category of groups: it is the unit group of
\(\operatorname{End}(G)\).
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.groups import Group, GroupElement
    from sage.structure.parent import ElementConstructorInput, MembershipInput
    from dzack_research.preamble.lexicon import OrderedSet

from sage.categories.groups import Groups as SageGroups
from sage.groups.libgap_morphism import GroupHomset_libgap, GroupMorphism_libgap
from sage.groups.libgap_wrapper import ParentLibGAP
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.libs.gap.element import GapElement
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.lazy_attribute import lazy_attribute
from sage.structure.element import Element

from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _finiteness,
    _gap_model,
)
from dzack_research.preamble.owned_category_bases import Category
from dzack_research.preamble.categories.sets.cardinals import cardinal


def _element_to_engine(group: "Group", element: "GroupElement") -> GapElement:
    r"""Return the GAP element behind ``element`` in ``group``'s model.

    Defined exactly where the model is element-faithful: a GAP-backed group's
    elements carry their own GAP object, so nothing is guessed.  A group whose
    model is a permutation normalization (the ``AbelianGroup_class`` and
    generic-matrix arms of :func:`_gap_model`) forgets which element is which,
    so element-level transport there is a stated gap, not a lookup.
    """
    match group:
        case GroupAutomorphismGroup() | PermutationGroup_generic() | ParentLibGAP():
            engine_element: GapElement = element.gap()
            return engine_element
        case _:
            assert False, (
                f"{group}'s GAP model is a normalization that forgets which "
                "element is which, so element-level transport is a stated gap"
            )


def _element_from_engine(
    group: "Group", engine_element: GapElement
) -> "GroupElement":
    r"""Return the owned element represented by ``engine_element``."""
    match group:
        case GroupAutomorphismGroup():
            element: "GroupElement" = group(engine_element, check=False)
            return element
        case PermutationGroup_generic() | ParentLibGAP():
            element = group(engine_element)
            return element
        case _:
            assert False, (
                f"{group}'s GAP model is a normalization that forgets which "
                "element is which"
            )


class GroupHomomorphism(GroupMorphism_libgap):
    r"""A homomorphism of groups, held as GAP holds it.

    Application, the kernel, pushforward, lift, preimage and section are the
    maintained implementations of
    :class:`~sage.groups.libgap_morphism.GroupMorphism_libgap`; what is added
    is the owned surface: diagrammatic composition and the image *of the
    morphism*.
    """

    if TYPE_CHECKING:
        # Built only by ``GroupHomset._element_constructor_``, so that homset
        # is the parent, and the engine datum is the stored GAP homomorphism.
        def parent(self) -> "GroupHomset": ...
        def gap(self) -> GapElement: ...
        def domain(self) -> "Group": ...
        def codomain(self) -> "Group": ...

class GroupHomset(GroupHomset_libgap):
    r"""The homset \(\operatorname{Hom}(G,H)\) of two owned groups.

    Construction accepts the house spelling -- a dictionary
    ``{generator: image}`` on the domain's distinguished generators -- and
    everything Sage's own homset accepts (an ordered list of images, a GAP
    homomorphism).  Reached through :func:`group_homset` and the owned
    accessors (``End``, ``Aut``, ``conjugation_morphism``); Sage's own
    ``Hom``/``hom`` routing is left untouched, because the owned module tree
    seats torsion modules in the abelian-groups node and their morphisms are
    module morphisms, not these.
    """

    Element = GroupHomomorphism

    if TYPE_CHECKING:
        def domain(self) -> "Group": ...
        def codomain(self) -> "Group": ...

    def __init__(self, domain: "Group", codomain: "Group") -> None:
        # ``check=False``: Sage's check insists on its own two backends, and
        # the owned surface admits more -- Aut(G) itself, and the groups whose
        # model ``_gap_model`` normalizes.  What is modelable is decided
        # there, at the point of computing, never here.
        GroupHomset_libgap.__init__(
            self, domain, codomain, category=OwnedGroups(), check=False
        )

    def _element_constructor_(
        self,
        images: "ElementConstructorInput",
        check: bool = True,
        **options: "ElementConstructorInput",
    ) -> GroupHomomorphism:
        match images:
            case dict():
                return self._from_group_generator_images(images, check=check)
            case _:
                morphism = GroupHomset_libgap._element_constructor_(
                    self, images, check=check, **options
                )
                assert isinstance(morphism, GroupHomomorphism), (
                    f"this homset builds owned homomorphisms; got {morphism}"
                )
                return morphism

    def _image_in_codomain(
        self, value: "ElementConstructorInput"
    ) -> "GroupElement":
        r"""Return ``value`` as an element of the codomain."""
        if isinstance(value, Element) and value.parent() is self.codomain():
            return value
        element: "GroupElement" = self.codomain()(value)
        return element

    def _from_group_generator_images(
        self,
        images: "dict[GroupElement, ElementConstructorInput]",
        check: bool = True,
    ) -> GroupHomomorphism:
        r"""Extend the assignment on the distinguished generators over \(G\).

        The extension exists if and only if the images satisfy the domain's
        relations, and that is what the engine's construction decides:
        ``GroupHomomorphismByImages`` answers ``fail`` on a broken relation,
        which is the whole content of "the assignment is a homomorphism".
        """
        domain = self.domain()
        codomain = self.codomain()
        generators = tuple(domain.group_generators())
        assert set(images) == set(generators), (
            "the assignment must name exactly the distinguished generators; "
            f"got {set(images)} against {set(generators)}"
        )
        generator_models = [
            _element_to_engine(domain, generator) for generator in generators
        ]
        image_models = [
            _element_to_engine(codomain, self._image_in_codomain(images[generator]))
            for generator in generators
        ]
        if check:
            engine_morphism = libgap.GroupHomomorphismByImages(
                _gap_model(domain),
                _gap_model(codomain),
                generator_models,
                image_models,
            )
            assert not engine_morphism.is_bool(), (
                "the images do not satisfy the domain's relations, so "
                "they define no homomorphism"
            )
        else:
            engine_morphism = libgap.GroupHomomorphismByImagesNC(
                _gap_model(domain),
                _gap_model(codomain),
                generator_models,
                image_models,
            )
        homomorphism: GroupHomomorphism = self.element_class(
            self, engine_morphism, check=False
        )
        return homomorphism

    def _repr_(self) -> str:
        return f"Hom({self.domain()}, {self.codomain()})"


@cached_function
def group_homset(domain: "Group", codomain: "Group") -> GroupHomset:
    r"""Return the canonical homset: one object per ordered pair of groups."""
    return GroupHomset(domain, codomain)


class GroupAutomorphism(GroupHomomorphism):
    r"""An invertible endomorphism, as an element of \(\operatorname{Aut}(G)\)."""

    if TYPE_CHECKING:
        def parent(self) -> "GroupAutomorphismGroup": ...

class GroupAutomorphismGroups(Category):
    r"""Automorphism groups of owned groups."""

    def super_categories(self) -> list:
        return [OwnedGroups()]

    class ElementMethods:
        def inverse(self) -> "GroupAutomorphism":
            r"""Return \(f^{-1}\), which exists because \(f\) is bijective."""
            automorphism: "GroupAutomorphism" = self.parent()(
                self.gap().InverseGeneralMapping(), check=False
            )
            return automorphism

        def _composition_(
            self,
            right: "GroupAutomorphism",
            homset: "GroupHomset",
        ) -> "GroupAutomorphism":
            r"""Return the group product in the automorphism group."""
            assert right.parent() is self.parent(), (
                "the two automorphisms must belong to one automorphism group"
            )
            return self.parent()(right.gap() * self.gap(), check=False)

    class ParentMethods:
        @cached_method
        def _libgap_(self) -> GapElement:
            r"""Return the GAP automorphism group used for computation."""
            engine_subgroup = self.engine_subgroup()
            if engine_subgroup is not None:
                return engine_subgroup
            from sage.groups.abelian_gps.abelian_group_gap import AbelianGroup_gap
            from sage.groups.finitely_presented import FinitelyPresentedGroup
            from sage.groups.free_group import FreeGroup_class
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                PredicateSubgroups,
            )

            group = self.domain()
            match group:
                case FreeGroup_class() | FinitelyPresentedGroup():
                    assert False, (
                        f"Aut({group}) exists, but computing it from a bare "
                        "presentation requires coset enumeration"
                    )
                case _ if group in PredicateSubgroups():
                    assert False, (
                        f"{group} has no generating set from which to compute Aut"
                    )
                case AbelianGroup_gap():
                    assert _finiteness(group) is True, (
                        f"the GAP automorphism algorithm requires {group} finite"
                    )
                    engine_group: GapElement = group.automorphism_group().gap()
                    return engine_group
                case _:
                    assert _finiteness(group) is True, (
                        f"the GAP automorphism algorithm requires {group} finite"
                    )
                    computed: GapElement = libgap.AutomorphismGroup(
                        _gap_model(group)
                    )
                    return computed

        def _element_constructor_(
            self,
            images: "ElementConstructorInput",
            check: bool = True,
            **options: "ElementConstructorInput",
        ) -> "GroupAutomorphism":
            match images:
                case GapElement():
                    automorphism: "GroupAutomorphism" = self.element_class(
                        self, images, check=False
                    )
                case _:
                    automorphism = super()._element_constructor_(
                        images, check=check, **options
                    )
            if check:
                assert bool(automorphism.gap().IsBijective()), (
                    "the assignment is an endomorphism but not an automorphism"
                )
            return automorphism

        def _subgroup_from_engine(
            self, engine_subgroup: GapElement
        ) -> "GroupAutomorphismGroup":
            r"""Return the subgroup named by the engine."""
            from dzack_research.preamble.refine import refine

            subgroup = GroupAutomorphismGroup(
                self.domain(), engine_subgroup=engine_subgroup
            )
            subgroup.set_supergroup(self)
            return refine(subgroup, [OwnedGroups().Subobjects()])

        def one(self) -> "GroupAutomorphism":
            r"""Return the identity automorphism."""
            return self(
                libgap.IdentityMapping(_gap_model(self.domain())), check=False
            )

        def group_generators(self) -> "OrderedSet":
            r"""Return the automorphisms in a computed generating set."""
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            return finite_ordered_set(
                tuple(
                    self(generator, check=False)
                    for generator in self._libgap_().GeneratorsOfGroup()
                )
            )

        @lazy_attribute
        def _cardinality(self):
            r"""Compute the set-level cardinality datum through GAP."""
            assert _finiteness(self.domain()) is True, (
                "the GAP cardinality algorithm requires a finite domain"
            )
            return cardinal(self._libgap_().Size().sage())

        def _repr_(self) -> str:
            if self.engine_subgroup() is not None:
                return f"Subgroup of Aut({self.domain()})"
            return f"Aut({self.domain()})"


class GroupAutomorphismGroup(GroupHomset):
    r"""\(\operatorname{Aut}(G)\), the unit group of \(\operatorname{End}(G)\).

    Constructed for *every* owned group: the object always exists, and what
    some groups lack is an algorithm, an absence stated at the point of
    computing (:meth:`_libgap_`) rather than at construction.
    """

    Element = GroupAutomorphism

    def __init__(
        self,
        group: "Group",
        engine_subgroup: GapElement | None = None,
    ) -> None:
        # Local: a module-level import here would close a cycle; by call time
        # the refine module is built.
        from dzack_research.preamble.refine import refine

        GroupHomset.__init__(self, group, group)
        self._engine_subgroup = engine_subgroup
        self._supergroup = self
        # \(\operatorname{Aut}\) in groups is a group, so that is the
        # placement.  Not the endomorphism-homset role as well:
        # \(\operatorname{End}(G)\) is a monoid under composition, and
        # \(\operatorname{Aut}(G)\) is its group of units -- multiplicative
        # placement, exactly as the endset of a formed module is placed.
        # The homset surface comes from the category it is an object of.
        refine(self, GroupAutomorphismGroups())

    def engine_subgroup(self) -> GapElement | None:
        return self._engine_subgroup

    def supergroup(self) -> "Group":
        return self._supergroup

    def set_supergroup(self, supergroup: "GroupAutomorphismGroup") -> None:
        self._supergroup = supergroup
