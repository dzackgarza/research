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
    from collections.abc import Iterator
    from sage.categories.groups import Group, GroupElement
    from sage.structure.parent import ElementConstructorInput, MembershipInput

from sage.categories.groups import Groups as SageGroups
from sage.groups.libgap_morphism import GroupHomset_libgap, GroupMorphism_libgap
from sage.groups.libgap_wrapper import ParentLibGAP
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.libs.gap.element import GapElement
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.structure.element import Element

from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _finiteness,
    _gap_model,
)
from dzack_research.preamble.categories.sets.cardinals import Cardinal


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

    def then(self, other: "GroupHomomorphism") -> "GroupHomomorphism":
        r"""Return the composite of ``self`` \(=f\) then ``other`` \(=g\)."""
        assert other.domain() is self.codomain(), (
            "the codomain of the first map is not the domain of the second"
        )
        # GAP composes mappings left to right under ``*``, so this product is
        # the mapping that applies ``self`` first.
        return group_homset(self.domain(), other.codomain())(
            self.gap() * other.gap()
        )

    def is_injective(self) -> bool:
        r"""Return whether the kernel is trivial, decided by the engine."""
        return bool(self.gap().IsInjective())

    def image(self) -> "Group":
        r"""Return \(\operatorname{im}(f)\le H\), the image subgroup.

        The image of the morphism itself, which is the notion the owned
        surface names.  Sage's ``image = pushforward`` alias -- the image of a
        *subgroup or element* handed in -- is shadowed here and remains
        available as :meth:`pushforward`.
        """
        engine_image = self.gap().Image()
        codomain = self.codomain()
        match codomain:
            case GroupAutomorphismGroup():
                return codomain._subgroup_from_engine(engine_image)
            case _:
                subgroup: "Group" = codomain._subgroup_constructor(engine_image)
                return subgroup


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


def group_homset(domain: "Group", codomain: "Group") -> GroupHomset:
    r"""Return the canonical homset: one object per ordered pair of groups."""
    cache = domain.__dict__.setdefault("_group_homsets", {})
    homset: GroupHomset | None = cache.get(codomain)
    if homset is None:
        homset = GroupHomset(domain, codomain)
        cache[codomain] = homset
    return homset


class GroupAutomorphism(GroupHomomorphism):
    r"""An invertible endomorphism, as an element of \(\operatorname{Aut}(G)\)."""

    if TYPE_CHECKING:
        def parent(self) -> "GroupAutomorphismGroup": ...

    def inverse(self) -> "GroupAutomorphism":
        r"""Return \(f^{-1}\), which exists because \(f\) is bijective."""
        automorphism: "GroupAutomorphism" = self.parent()(
            self.gap().InverseGeneralMapping(), check=False
        )
        return automorphism

    def __mul__(self, other: "MembershipInput") -> "GroupAutomorphism":
        r"""Return \(f\circ g\): composition is the group law of \(\operatorname{Aut}(G)\)."""
        assert (
            isinstance(other, GroupAutomorphism)
            and other.parent() is self.parent()
        ), "multiplication here is internal to one automorphism group"
        # GAP composes left to right under ``*``: applying ``other`` first is
        # ``other.gap() * self.gap()``, which is \(f\circ g\).
        product: "GroupAutomorphism" = self.parent()(
            other.gap() * self.gap(), check=False
        )
        return product


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
        # \(\operatorname{Aut}\) in groups is a group, so that is the
        # placement.  Not the endomorphism-homset role as well:
        # \(\operatorname{End}(G)\) is a monoid under composition, and
        # \(\operatorname{Aut}(G)\) is its group of units -- multiplicative
        # placement, exactly as ``FormAutomorphismGroup`` is placed.  The
        # homset surface comes from the class it subclasses.
        refine(self, [SageGroups()])

    @cached_method
    def _libgap_(self) -> GapElement:
        r"""Return the engine's automorphism group -- the gate to computation.

        Every computed answer below reaches GAP through this one method, so
        the honest gaps are stated here, once, by the arm that meets them:

        * a group given only by a presentation -- free or finitely presented
          -- would need coset enumeration, which is not run silently;
        * a predicate subgroup has no generating set by construction;
        * a group not decidably finite (\(GL_n(\ZZ)\) and its kin) is one
          this engine has no algorithm for.

        For a GAP-backed abelian group the engine is Sage's one
        abstract-group ``automorphism_group``
        (``AbelianGroup_gap.automorphism_group``), consumed behind the same
        public spelling; everything else reaches
        ``libgap.AutomorphismGroup`` on the group's model.
        """
        if self._engine_subgroup is not None:
            return self._engine_subgroup
        # Local: module-level imports here would close cycles with the group
        # intake modules; by call time they are built.
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
                    "presentation requires coset enumeration, which is not "
                    "run silently; the object stands, the algorithm is the gap"
                )
            case _ if group in PredicateSubgroups():
                assert False, (
                    f"{group} has no generating set by construction, so no "
                    "engine holds a model to compute Aut from; the gap is a "
                    "fact about the object"
                )
            case AbelianGroup_gap():
                assert _finiteness(group) is True, (
                    f"Aut({group}) exists, but this engine has no algorithm "
                    "for a group it cannot decide finite"
                )
                engine_group: GapElement = group.automorphism_group().gap()
                return engine_group
            case _:
                assert _finiteness(group) is True, (
                    f"Aut({group}) exists, but this engine has no algorithm "
                    "for a group it cannot decide finite"
                )
                computed: GapElement = libgap.AutomorphismGroup(
                    _gap_model(group)
                )
                return computed

    gap = _libgap_

    def _element_constructor_(
        self,
        images: "ElementConstructorInput",
        check: bool = True,
        **options: "ElementConstructorInput",
    ) -> GroupAutomorphism:
        match images:
            case GapElement():
                automorphism: GroupAutomorphism = self.element_class(
                    self, images, check=False
                )
            case _:
                automorphism = GroupHomset._element_constructor_(
                    self, images, check=check, **options
                )
        if check:
            assert bool(automorphism.gap().IsBijective()), (
                "the assignment is an endomorphism but not invertible, so "
                "it is no automorphism"
            )
        return automorphism

    def _subgroup_from_engine(
        self, engine_subgroup: GapElement
    ) -> "GroupAutomorphismGroup":
        r"""Return the subgroup of this automorphism group the engine names."""
        # Local: a module-level import here would close a cycle.
        from dzack_research.preamble.refine import refine

        subgroup = GroupAutomorphismGroup(
            self.domain(), engine_subgroup=engine_subgroup
        )
        subgroup._supergroup = self
        return refine(subgroup, [OwnedGroups(), SageGroups().Subobjects()])

    def supergroup(self) -> "Group":
        containing: "Group" = self.__dict__.get("_supergroup", self)
        return containing

    def one(self) -> GroupAutomorphism:
        r"""Return \(\operatorname{id}_G\), available whatever else is not.

        The identity needs only the group's model, never the computed
        automorphism group, so \(\operatorname{Aut}(G)\) of a group whose
        engine states a gap still has its identity.
        """
        identity: GroupAutomorphism = self(
            libgap.IdentityMapping(_gap_model(self.domain())), check=False
        )
        return identity

    def gens(self) -> tuple[GroupAutomorphism, ...]:
        r"""Return the engine's generators, as this group's own elements.

        The spelling Sage's category machinery reads; the owned vocabulary
        (``group_generators``) reaches it through the groups category.
        """
        return tuple(
            self(generator, check=False)
            for generator in self._libgap_().GeneratorsOfGroup()
        )

    def is_finite(self) -> "bool | Unknown":
        r"""Return finiteness, read off the domain and never probed in GAP.

        An automorphism of a finite group is a permutation of its underlying
        finite set, so \(\operatorname{Aut}(G)\le\operatorname{Sym}(G)\) is
        finite with \(G\).  A domain not decidably finite leaves the honest
        answer ``Unknown``: \(\operatorname{Aut}(F_2)\) is a theorem away,
        and this method states no theorems.
        """
        if _finiteness(self.domain()) is True:
            return True
        return Unknown

    def order(self) -> Cardinal:
        r"""Return \(|\operatorname{Aut}(G)|\), computed by the engine."""
        return Cardinal(self._libgap_().Size().sage())

    def __iter__(self) -> "Iterator[GroupAutomorphism]":
        r"""Enumerate the elements, which a finite group is entitled to."""
        assert self.is_finite() is True, (
            "the automorphism group of a group not known finite is not "
            "enumerable"
        )
        for engine_element in self._libgap_().AsList():
            yield self(engine_element, check=False)

    def __contains__(self, element: "MembershipInput") -> bool:
        # ``in`` is asked of an arbitrary value.
        return (
            isinstance(element, GroupAutomorphism)
            and element.parent() is self
        )

    def _repr_(self) -> str:
        if self._engine_subgroup is not None:
            return f"Subgroup of Aut({self.domain()})"
        return f"Aut({self.domain()})"
