r"""Hom/End/Mono/Epi/Iso/Aut category packets.

For every category ``C`` and objects ``A,B`` in ``C`` we represent
``Hom_C(A,B)`` itself as a category.  Its objects are the actual arrows
``A -> B``.  In the absence of represented 2-morphisms this category is
discrete.  The Hom/End/Aut families travel functorially with the main category
graph: every supercategory ``C <= D`` induces corresponding supercategory
edges ``Hom_C <= Hom_D``, ``End_C <= End_D`` and ``Aut_C <= Aut_D``.

This is intentionally distinct from the *underlying Hom-set parent*.  The
latter may carry additional enrichment -- for example ``Hom_R(M,N)`` is an
``R``-module -- while there remains exactly one categorical Hom object for the
chosen category and endpoints.

An arrow ``f: A -> B`` regarded as an object is an object of the arrow
category ``Ar(C)``, built through that category's entry; ``Hom_C(A,B)`` read
as a category is the fibre of ``(dom, cod): Ar(C) -> C x C`` at ``(A, B)``.
In a 1-category its morphisms are squares whose two endpoint maps are
identities: commutativity then says that their two arrows are equal.  It is
therefore discrete, not the full arrow subcategory on these objects (which
also has squares with nonidentity endpoint endomorphisms).  A Hom category
reuses the arrow objects without inheriting all the squares between them.
"""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism
from sage.categories.objects import Objects as SageObjects
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.unknown import Unknown, UnknownClass
from sage.structure.category_object import CategoryObject as SageCategoryObject
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.element import parent
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.hom_foundation import (
    CategoryPacketMethods,
    OwnedHomset,
    _has_category_packet_surface,
    _underlying_set_homset,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.owned_category_bases import Category as OwnedCategoryBase
from dzack_research.preamble.refine import (
    construction_scope,
    realize_owned_category,
    refine,
    run_construction_hooks,
)


def _category_hom(
    category: Category | None,
    domain: Parent,
    codomain: Parent,
) -> FixedHomObject | Homset:
    r"""The complete selected Hom, including any defining arrow predicate.

    Mathematical admission uses this object. Its private ``arrow_set`` may
    also represent maps outside a restricted Hom category, so membership in
    that parent alone is not admission to the selected category.
    """
    if _has_category_packet_surface(category):
        # Admission follows the category's public Hom selector.  Most owned
        # categories inherit the packet implementation, while constructions
        # such as G-objects and functor categories legitimately specialize
        # ``Mor`` for their represented object type.  Bypassing that selector
        # rebuilds the packet Hom against endpoints that may be wrappers for a
        # more specific representation.
        return category.Mor(domain, codomain)
    return Hom(domain, codomain, category)


def _arrow_is_inherited_from_subcategory(target, arrow: Morphism) -> bool:
    r"""Return whether ``arrow`` lies in a stronger Hom category below ``target``.

    If ``D <= C``, every ``D``-morphism is definitionally a ``C``-morphism.
    A structured Hom parent may represent that stronger arrow by a different
    morphism class, so admission follows the Hom-category edge itself rather
    than reconstructing and re-verifying the same arrow in ``C``.
    """
    parent = arrow.parent()
    return (
        parent in HomCategories()
        and parent.domain_object() is target.domain_object()
        and parent.codomain_object() is target.codomain_object()
        and parent.base_category().is_subcategory(target.base_category())
    )


def _category_homset(
    category: Category | None,
    domain: Parent,
    codomain: Parent,
) -> Homset:
    r"""Return the declared Hom-set for an explicitly selected category.

    Selecting ``C`` must not forget its structure: linear, algebra and equivariant maps are
    constructed by ``C``'s declared Hom family, not by the private
    function-map substrate. An enriched Hom is also a mathematical parent;
    its inherited parent-level ``Mor`` is not the Hom of that category.
    Native Sage categories retain their native Hom ingress.

    Use ``_category_hom`` for admission. This adapter provides the runtime
    parent required by Sage morphisms, and a restricted Hom need not contain
    every map represented by that parent.
    """
    selected = _category_hom(category, domain, codomain)
    match selected:
        case Category():
            return selected.arrow_set()
        case _:
            return selected


def _declared_category_reaches(category: Category, target: Category) -> bool:
    r"""Return whether ``target`` occurs in ``category``'s declared supergraph.

    Fixed Hom objects can be distinct runtime parents even when one is the
    inherited specialization of the other.  Sage's ``is_subcategory`` is not
    reliable for these mixed Category/Parent Hom objects, so selection follows
    the explicit immediate-supercategory graph by identity.
    """
    pending = [category]
    seen = set()
    while pending:
        current = pending.pop()
        if current is target:
            return True
        identity = id(current)
        if identity in seen:
            continue
        seen.add(identity)
        pending.extend(current.super_categories())
    return False


def _minimal_inherited_homs(candidates):
    r"""Discard inherited Hom objects strictly above another candidate.

    A join of object properties may reach the same arrow theory through several
    branches.  If one branch carries a genuinely stronger Hom object (for
    example commuting triangles between represented subobjects), that object is
    the Hom of the join; its ordinary underlying Hom is only a supercategory.
    Unrelated surviving candidates remain an ambiguity and are rejected by the
    caller.
    """
    return [
        candidate
        for candidate in candidates
        if not any(
            other is not candidate and _declared_category_reaches(other, candidate)
            for other in candidates
        )
    ]


def _packet_supercategories(category):
    r"""Return semantic supercategories participating in the owned packet graph.

    Sage categories in ``super_categories()`` are runtime substrates.  Their
    native Hom dispatch is endpoint-driven and can jump back into a stronger
    owned category, so transporting Hom/End/Aut packets through them creates
    cycles and, more importantly, the wrong semantic graph.

    These are *declared supercategories*.  Each supplies its own Hom family;
    an endpoint's default Hom does not choose that family.  In particular a
    subobject's inherited Hom comes from the declared category of the base
    object, not from rediscovering the subobject category through its
    inclusion.
    """
    return tuple(
        supercategory
        for supercategory in category.super_categories()
        if _has_category_packet_surface(supercategory)
    )


def _precomposable(second: Morphism, first) -> bool:
    r"""Whether ``first`` composes before ``second`` in ``second``'s Hom theory.

    The right operand of ``*`` is arbitrary, so this is the admission of the
    composition operator: ``first`` is an arrow of the same base category whose
    codomain is ``second``'s domain.  The arrow's own Hom is asked.
    """
    match first:
        case Morphism() if first.codomain() is second.domain():
            base = second.parent().base_category()
            return first in _category_hom(base, first.domain(), first.codomain())
        case _:
            return False


class HomArrowIdentity(Morphism):
    r"""The identity 2-arrow on one arrow object."""

    def _call_(self, value):
        return value

    def __eq__(self, other: Any) -> bool:
        return parent(other) is self.parent()

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        # The discrete 2-Hom on one arrow object holds its identity only, so
        # the composable arrows are exactly the elements of this parent.
        if other not in self.parent():
            return NotImplemented
        return self.parent().identity()


class CategoricalHomset(CategoryPacketMethods, OwnedHomset, Category):
    r"""A represented Hom object which is both a Sage Homset and a category.

    This mixed runtime parent deliberately retains Sage's raw ``Category`` base.
    Its ``Parent.category()`` records the Hom object's enrichment placement;
    replacing that parent role by ``OwnedCategoryObject`` would instead force
    ``category()`` to be ``Cat()`` and erase the represented Hom-set structure.
    Pure category objects in this module use :class:`OwnedCategoryBase`; this
    one is the boundary where the two runtime roles genuinely coincide.

    This is the live counterpart of the archived owned Hom-category base.  It
    keeps Sage's hard requirement that every ``Morphism`` be parented by an
    actual ``Homset``, while also making that same parent the discrete category
    ``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
    the *same object*.
    """

    @staticmethod
    def __classcall__(cls, *arguments, **options):
        # ``Category`` is a UniqueRepresentation whose default classcall does
        # not include fixed Hom endpoints in the identity of this mixed
        # Homset/category object.  The owning Hom family already interns by
        # ``(domain,codomain)``, so bypass Category's cache here.  Subclasses
        # name their own construction data, so the signature stays open.
        return typecall(cls, *arguments, **options)

    def __init__(
        self,
        family: _HomCategoryOf,
        domain: Parent,
        codomain: Parent,
        *,
        category: Category | None = None,
        base: Parent | None = None,
    ) -> None:
        self._family = family
        self._end_family = None
        self._aut_family = None
        self._domain_object = domain
        self._codomain_object = codomain
        # The semantic Hom/End supertree is deliberately richer than the
        # method-provider hierarchy Sage should use to synthesize Python
        # classes for this mixed Homset/category parent.  Feeding fixed Hom
        # objects back into Sage's C3 category-class builder creates cycles as
        # soon as a super-Hom is refined (for example End_R(M) as a ring).
        # Packet/enrichment code transports the mathematical structure
        # explicitly, so the runtime method spine stays at Objects().
        self._super_categories_for_classes = [SageObjects()]
        Category.__init__(self)
        Homset.__init__(
            self,
            domain,
            codomain,
            category=SageSets(),
            base=base,
        )
        if category is not None:
            # Sage ``Homset`` insists on constructing first in ``Sets`` so it
            # can form its private Homsets/Endsets runtime category.  Complete
            # the owned enrichment while this constructor is still active;
            # callers never observe an un-enriched module Hom parent.
            refine(self, category)

    def _already_parented_arrow(self, candidate: Morphism) -> bool:
        r"""Whether ``candidate`` is already represented by this Hom theory."""
        return candidate.parent() is self or _arrow_is_inherited_from_subcategory(self, candidate)

    def __call__(self, *args, **kwargs):
        r"""Construct an arrow, preserving one already represented here.

        If ``D <= C``, a ``D``-arrow is already a ``C``-arrow.  Reading it in
        the weaker Hom must therefore preserve the arrow rather than
        reinterpret its object as generator images or presentation data.
        """
        match args:
            case (Morphism() as arrow,) if not kwargs and self._already_parented_arrow(arrow):
                return arrow
        return self._element_constructor_(*args, **kwargs)

    def hom_family(self) -> _HomCategoryOf:
        return self._family

    @property
    def _HomCategory(self) -> type[_HomCategoryOf]:
        # The Hom objects and their family are mutually recursive types.
        # Resolve the family's declaration only after this module is loaded.
        return _DiscreteTwoHomCategoryOf

    def homset_category(self) -> Category:
        r"""Return the owned mathematical category whose Hom object this is.

        Sage's ``Homset`` initialization still uses ``Sets()`` only as the
        private runtime method spine.  The semantic Hom category is the base
        category of the owned Hom family.
        """
        return self.hom_family().base_category()

    def identity_at(self, obj: Parent) -> Morphism:
        return self.hom_family().Of(obj, obj).arrow_set().identity()

    def attach_end_family(self, family: _EndCategoryOf) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an endomorphism Hom category can carry an End-family role")
        owner = _category_packet(self.base_category()).Ends()
        if family is not owner:
            represented = _category_packet(family.base_category()).Homs().Of(
                self.domain_object(), self.codomain_object()
            )
            if represented is not self and represented.arrow_set() is not self:
                raise ValueError("the End family selects a different fixed Hom object")
        if self._end_family is not None and self._end_family is not owner:
            raise ValueError("one fixed Hom category cannot carry two End-family roles")
        self._end_family = owner

    def end_family(self) -> _EndCategoryOf | None:
        return self._end_family

    def attach_aut_family(self, family: _AutCategoryOf) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an equal-endpoint Iso category can carry an Aut-family role")
        owner = _category_packet(self.base_category()).Auts()
        if family is not owner:
            represented = _category_packet(family.base_category()).Isos().Of(
                self.domain_object(), self.codomain_object()
            )
            if represented is not self and represented.arrow_set() is not self:
                raise ValueError("the Aut family selects a different fixed Iso object")
        if self._aut_family is not None and self._aut_family is not owner:
            raise ValueError("one fixed Iso category cannot carry two Aut-family roles")
        self._aut_family = owner

    def aut_family(self) -> _AutCategoryOf | None:
        return self._aut_family

    def identity_endomorphism(self) -> Morphism:
        if self.end_family() is None:
            raise ValueError("this fixed Hom category has not been given an End-family role")
        identity = self.arrow_set().identity()
        return self(identity)

    one = identity_endomorphism

    def base_category(self) -> Category:
        return self.hom_family().base_category()

    def domain_object(self) -> Parent:
        return self._domain_object

    def codomain_object(self) -> Parent:
        return self._codomain_object

    def arrow_set(self) -> Parent:
        return self

    underlying_homset = arrow_set

    def accepts(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` is an arrow of this Hom category.

        An arrow placed here, or in the Hom of a subcategory with the same
        endpoints, is one.  Constructing a new arrow from its defining data
        is a separate operation: constructor failure is not a membership
        decision, and successful conversion does not place the input here.
        """
        if arrow.domain() is not self.domain_object() or arrow.codomain() is not self.codomain_object():
            return False
        return self._already_parented_arrow(arrow)

    def object(self, arrow: Morphism):
        r"""``arrow`` as an object of this category: the object of ``Ar(C)`` on it."""
        if not self.accepts(arrow):
            arrow = self(arrow)
        return self.base_category().ArrowCategory()(arrow)

    def _hom_endpoint(self, obj: Parent | Category | Morphism):
        match obj:
            case Morphism():
                return self.object(obj)
            case _ if obj in self.base_category().ArrowCategory():
                return obj
            case _:
                return self.object(obj)

    def __contains__(self, candidate: Any) -> bool:
        # The candidate is arbitrary.  An object of ``Ar(C)`` lies here when
        # its arrow does; otherwise only a map can be an arrow, and whether it
        # is one of these is this Hom's own construction protocol.
        match candidate:
            case Morphism():
                return self.accepts(candidate)
            case _ if candidate in self.base_category().ArrowCategory():
                return self.accepts(candidate.arrow())
            case _:
                return False

    def super_categories(self):
        supers = []
        for supercategory in _packet_supercategories(self.base_category()):
            supers.append(
                self.hom_family().family_over(supercategory).Of(
                    self.domain_object(), self.codomain_object()
                )
            )
            if self.end_family() is not None:
                supers.append(
                    self.end_family().family_over(supercategory).Of(
                        self.domain_object()
                    )
                )
        return supers or [Objects()]

    def two_hom(
        self,
        domain: Parent | Morphism,
        codomain: Parent | Morphism,
    ) -> CategoricalHomset:
        return self.HomCategory().Of(domain, codomain)

    Mor = two_hom

    def identity_2(self, arrow: Morphism) -> Morphism:
        arrow_object = self.object(arrow)
        return self.two_hom(arrow_object, arrow_object).identity()


class HomArrowDiscreteHomset(CategoricalHomset):
    r"""The discrete 2-Hom between two arrow objects.

    The objects of a fixed Hom category are the arrows themselves, so this is
    the Hom object of that category: it is discrete because no 2-morphisms are
    represented.
    """

    Element = HomArrowIdentity

    def __init__(
        self,
        family: _DiscreteTwoHomCategoryOf,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(self, family, domain, codomain)

    def hom_category(self) -> Category:
        return self.base_category()

    def _element_constructor_(self, value=None):
        if self.domain() is not self.codomain():
            raise ValueError("distinct arrows have no represented 2-morphism")
        if value is not None:
            if parent(value) is not self:
                raise ValueError("the discrete 2-Hom contains only its identity")
            return value
        return self.element_class(self)

    @cached_method
    def identity(self) -> HomArrowIdentity:
        return self()


class FixedHomCategory(CategoryPacketMethods, OwnedCategoryBase):
    r"""The category ``Hom_C(A,B)`` of arrows with fixed endpoints.

    Its objects are the objects of ``Ar(C)`` lying over ``(A, B)``; it owns
    no object class, and ``object(f)`` builds through ``Ar(C)``'s entry.
    """

    @staticmethod
    def __classcall__(cls, family, domain, codomain):
        # The owning Hom-family already interns fixed categories by their
        # endpoint identities.  Sage ``Category``'s UniqueRepresentation cache
        # does not include those endpoints and can otherwise collapse
        # ``Hom_C(A,B)`` with a previously created ``Hom_C(A',B')``.
        return typecall(cls, family, domain, codomain)

    def __init__(
        self,
        family: _HomCategoryOf,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        self._family = family
        self._end_family = None
        self._aut_family = None
        self._domain_object = domain
        self._codomain_object = codomain
        # As for ``CategoricalHomset``, semantic packet supercategories are
        # not Python implementation mixins.  In particular ``Iso_C(A,B)``
        # simultaneously lies over ``Hom_C``, ``Mono_C`` and ``Epi_C``; asking
        # Sage to synthesize one C3 class from those fixed categories creates
        # artificial MRO cycles.  Keep the runtime method spine at the owned
        # root instead, which realizes the host ``Parent`` for the objects a
        # fixed Hom category builds through its own entry (the functors of
        # ``[A, B]``), while ``super_categories`` states the mathematics.
        self._super_categories_for_classes = [Objects()]
        super().__init__()

    def category(self) -> Category:
        r"""A fixed Hom category is placed in ``HomCategories``, below ``Cat``."""
        return HomCategories()

    def _make_named_class_key(self, name):
        return (self._family, id(self._domain_object), id(self._codomain_object))

    def hom_family(self) -> _HomCategoryOf:
        return self._family

    @property
    def _HomCategory(self) -> type[_HomCategoryOf]:
        return _DiscreteTwoHomCategoryOf

    def attach_end_family(self, family: _EndCategoryOf) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an endomorphism Hom category can carry an End-family role")
        owner = _category_packet(self.base_category()).Ends()
        if family is not owner:
            represented = _category_packet(family.base_category()).Homs().Of(
                self.domain_object(), self.codomain_object()
            )
            if represented is not self and represented.arrow_set() is not self:
                raise ValueError("the End family selects a different fixed Hom object")
        if self._end_family is not None and self._end_family is not owner:
            raise ValueError("one fixed Hom category cannot carry two End-family roles")
        self._end_family = owner

    def end_family(self) -> _EndCategoryOf | None:
        return self._end_family

    def attach_aut_family(self, family: _AutCategoryOf) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an equal-endpoint Iso category can carry an Aut-family role")
        owner = _category_packet(self.base_category()).Auts()
        if family is not owner:
            represented = _category_packet(family.base_category()).Isos().Of(
                self.domain_object(), self.codomain_object()
            )
            if represented is not self and represented.arrow_set() is not self:
                raise ValueError("the Aut family selects a different fixed Iso object")
        if self._aut_family is not None and self._aut_family is not owner:
            raise ValueError("one fixed Iso category cannot carry two Aut-family roles")
        self._aut_family = owner

    def aut_family(self) -> _AutCategoryOf | None:
        return self._aut_family

    def identity_endomorphism(self) -> Morphism:
        if self.end_family() is None:
            raise ValueError("this fixed Hom category has not been given an End-family role")
        return self(self.arrow_set().identity())

    one = identity_endomorphism

    def base_category(self) -> Category:
        return self.hom_family().base_category()

    def domain_object(self) -> Parent:
        return self._domain_object

    def codomain_object(self) -> Parent:
        return self._codomain_object

    def arrow_set(self) -> Parent:
        r"""The substrate of a Hom with no more specific declared constructor.

        Only an unreduced root family constructs this class.  Re-entering the
        public category Hom here would ask that same family to construct
        itself.  Restrictions instead inherit the actual Hom-set below.
        """
        if _has_category_packet_surface(self.base_category()):
            return _underlying_set_homset(self.domain_object(), self.codomain_object())
        return Hom(self.domain_object(), self.codomain_object(), self.base_category())

    underlying_homset = arrow_set

    def accepts(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` is an arrow of this Hom category.

        An arrow of the selected Hom-set, or of the Hom of a subcategory with
        the same endpoints, is one.  Inherited arrows retain their stronger
        mathematical parent; the category graph supplies this inclusion,
        not an attempted conversion through a possibly undecidable constructor.
        """
        if arrow.domain() is not self.domain_object() or arrow.codomain() is not self.codomain_object():
            return False
        homset = self.arrow_set()
        return arrow.parent() is homset or _arrow_is_inherited_from_subcategory(self, arrow)

    def object(self, arrow: Parent | Morphism):
        r"""``arrow`` as an object of this category: the object of ``Ar(C)`` on it."""
        arrows = self.base_category().ArrowCategory()
        match arrow:
            case Morphism():
                pass
            case _:
                arrow = arrow.arrow()
        if not self.accepts(arrow):
            raise ValueError(f"{arrow} is not an arrow of {self}")
        return arrows(arrow)

    __call__ = object

    def _hom_endpoint(self, obj: Parent | Category | Morphism):
        match obj:
            case Morphism():
                return self.object(obj)
            case _ if obj in self.base_category().ArrowCategory():
                return obj
            case _:
                return self.object(obj)

    def __contains__(self, candidate: Any) -> bool:
        # The candidate is arbitrary: an object of ``Ar(C)`` lies here when it
        # lies over these endpoints; a map when this Hom accepts it.
        match candidate:
            case Morphism():
                return self.accepts(candidate)
            case _ if candidate in self.base_category().ArrowCategory():
                return self.accepts(candidate.arrow())
            case _:
                return False

    def objects(self) -> IndexedFamily:
        arrows = self.arrow_set()
        return indexed_family(
            arrows,
            self,
            name=f"Arrow objects of {self}",
        )

    def Mor(
        self,
        domain: Parent | Morphism,
        codomain: Parent | Morphism,
    ) -> CategoricalHomset:
        return self.HomCategory().Of(domain, codomain)

    two_hom = Mor

    def identity_2(self, arrow: Parent | Morphism) -> Morphism:
        return self.Mor(arrow, arrow).identity()

    def identity(self, arrow_object: Parent | Morphism) -> Morphism:
        return self.Mor(arrow_object, arrow_object).identity()

    def super_categories(self):
        supers = []
        for supercategory in _packet_supercategories(self.base_category()):
            supers.append(
                self.hom_family().family_over(supercategory).Of(
                    self.domain_object(),
                    self.codomain_object(),
                )
            )
            if self.end_family() is not None:
                supers.append(
                    self.end_family().family_over(supercategory).Of(
                        self.domain_object()
                    )
                )
        return supers or [Objects()]

    def _repr_(self) -> str:
        return (
            f"Mor_{self.base_category()}({self.domain_object()}, "
            f"{self.codomain_object()})"
        )


class FixedEndCategory(FixedHomCategory):
    r"""The category ``End_C(A)`` of endomorphisms of one object."""

    def identity_endomorphism(self) -> Morphism:
        return self(self.arrow_set().identity())

    one = identity_endomorphism

    def _repr_(self) -> str:
        return f"End_{self.base_category()}({self.domain_object()})"


class FixedRestrictedHomCategory(FixedHomCategory):
    def arrow_set(self) -> Parent:
        r"""Return the existing ``Mor`` parent for these endpoints.

        A restricted Hom category classifies some arrows in the base
        category's already-existing Hom object.  It therefore reuses the
        endpoint Homset owned by the base category packet.
        """
        return _category_packet(self.base_category()).Homs().Of(
            self.domain_object(), self.codomain_object()
        ).arrow_set()

    underlying_homset = arrow_set

    def accepts(self, arrow: Morphism) -> bool:
        return super().accepts(arrow) and self.hom_family().accepts(arrow)

    def super_categories(self):
        base = _category_packet(self.base_category()).Homs().Of(
            self.domain_object(), self.codomain_object()
        )
        inherited = [
            self.hom_family().family_over(supercategory).Of(
                self.domain_object(), self.codomain_object()
            )
            for supercategory in _packet_supercategories(self.base_category())
        ]
        return [base, *inherited]


class RestrictedHomCategoryParent(FixedRestrictedHomCategory):
    r"""A restricted Hom category that also carries independent enrichment.

    Its elements may be structured witnesses (for example derivations) whose
    actual categorical arrows live in :meth:`arrow_set`.  Unlike
    :class:`CategoricalHomset`, this parent is therefore not itself a Homset
    and cannot become a second Homset for the same fixed endpoints.

    The owned category base already makes it a parent; what this level adds
    is the category its *elements* form (a set, a module, a group), recorded
    and realized exactly as the owned root records a category on an object:
    the category is written on the parent and its owned methods are realized,
    with no second class rewrite.
    """

    @staticmethod
    def __classcall__(cls, *arguments, **options):
        return typecall(cls, *arguments, **options)

    def __init__(
        self,
        family: _RestrictedHomCategoryOf,
        domain: Parent,
        codomain: Parent,
        *,
        category: Category | None = None,
    ) -> None:
        FixedRestrictedHomCategory.__init__(self, family, domain, codomain)
        if category is None:
            from dzack_research.preamble.categories.sets.set_categories import Sets

            category = Sets()
        with construction_scope(self) as reached:
            SageCategoryObject._init_category_(self, category)
            realize_owned_category(self)
            run_construction_hooks(self, reached)

    def category(self) -> Category:
        r"""Return the independent enrichment carried by this parent.

        ``RestrictedHomCategoryParent`` has two roles: its restricted-Hom
        methods describe which arrows its elements represent, while as a Sage
        parent its elements may independently form a set, module, group, or
        another category selected by ``category=``.  The fixed-Hom base is an
        owned category object, whose inherited ``category()`` names its
        placement among Hom categories.  That answer would erase the
        enrichment recorded on the parent.  Read the latter here.
        """
        return Parent.category(self)

    def __call__(self, *args, **kwargs):
        r"""Construct an element through the independent Parent role.

        The fixed restricted-Hom category also has an explicit :meth:`object`
        operation for regarding an accepted underlying arrow as an object of
        the Hom category.  That categorical conversion must not replace this
        parent's ordinary element constructor: derivations, connections, and
        absolute-Galois automorphisms are structured elements specified by
        their own defining data.
        """
        return self._element_constructor_(*args, **kwargs)

    def __contains__(self, candidate: Any) -> bool:
        # The candidate is arbitrary: an object of ``Ar(C)``, a structured
        # element of this parent (read through its underlying arrow), or a map.
        match candidate:
            case _ if parent(candidate) is self:
                return self.accepts(candidate.as_morphism())
            case Morphism():
                return self.accepts(candidate)
            case _ if candidate in self.base_category().ArrowCategory():
                return self.accepts(candidate.arrow())
            case _:
                return False


class CategoricalIsomorphism(Morphism):
    r"""An isomorphism represented by mutually inverse arrows."""

    def __init__(
        self,
        parent: Parent,
        forward: Morphism,
        inverse: Morphism,
        *,
        verify: bool = True,
    ) -> None:
        Morphism.__init__(self, parent)
        if forward.domain() is not self.domain() or forward.codomain() is not self.codomain():
            raise ValueError("the forward map has the wrong endpoints")
        if inverse.domain() is not self.codomain() or inverse.codomain() is not self.domain():
            raise ValueError("the inverse map has the wrong endpoints")
        if verify:
            left = inverse * forward
            right = forward * inverse
            if (left == left.parent().identity()) is not True:
                raise ValueError("the supplied maps do not establish a left inverse")
            if (right == right.parent().identity()) is not True:
                raise ValueError("the supplied maps do not establish a right inverse")
        self._forward = forward
        self._inverse = inverse

    def forward(self) -> Morphism:
        return self._forward

    def inverse(self) -> Morphism:
        return self._inverse

    def __call__(self, element):
        return self.forward()(element)

    def _call_(self, element):
        return self.forward()(element)

    def __eq__(self, other: Any) -> bool | UnknownClass:
        if self is other:
            return True
        # A represented isomorphism can be parented by an ordinary Hom-set of
        # its base category, beside maps that are not isomorphisms.
        match other:
            case CategoricalIsomorphism() if parent(other) is self.parent():
                pass
            case _:
                return False
        equalities = (self.forward() == other.forward(), self.inverse() == other.inverse())
        if any(answer is False for answer in equalities):
            return False
        return True if all(answer is True for answer in equalities) else Unknown

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        # An isomorphism composed with an isomorphism into its domain is an
        # isomorphism; composed with any other arrow it is that composite.
        if not _precomposable(self, other):
            return NotImplemented
        core = self.parent().homset_category().Core()
        if other not in core.Mor(other.domain(), self.domain()):
            return self.forward() * other
        forward = self.forward() * other.forward()
        inverse = other.inverse() * self.inverse()
        return CategoricalIsomorphism(
            _category_homset(self.parent().homset_category(), other.domain(), self.codomain()),
            forward,
            inverse,
            verify=False,
        )


class FixedIsoCategory(FixedRestrictedHomCategory):
    def accepts(self, arrow: Morphism) -> bool:
        r"""An arrow of ``Iso_C(A,B)`` is an isomorphism of ``C`` from ``A`` to ``B``.

        The core of ``C`` owns which arrows are represented isomorphisms, so
        its Hom decides.
        """
        if (
            arrow.domain() is not self.domain_object()
            or arrow.codomain() is not self.codomain_object()
        ):
            return False
        return arrow in self.base_category().Core().Mor(
            self.domain_object(), self.codomain_object()
        )

    def super_categories(self):
        packet = _category_packet(self.base_category())
        domain = self.domain_object()
        codomain = self.codomain_object()
        inherited = [
            self.hom_family().family_over(supercategory).Of(domain, codomain)
            for supercategory in _packet_supercategories(self.base_category())
        ]
        supers = [
            packet.Homs().Of(domain, codomain),
            packet.Monos().Of(domain, codomain),
            packet.Epis().Of(domain, codomain),
            *inherited,
        ]
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(domain))
            supers.extend(
                self.aut_family().family_over(supercategory).Of(domain)
                for supercategory in _packet_supercategories(self.base_category())
            )
        return supers

    def identity_automorphism(self) -> CategoricalIsomorphism:
        if self.aut_family() is None:
            raise ValueError("this isomorphism category has not been given an Aut-family role")
        if self.domain_object() is not self.codomain_object():
            raise ValueError("an automorphism category has equal endpoints")
        identity = self.arrow_set().identity()
        return self(
            CategoricalIsomorphism(
                identity.parent(), identity, identity, verify=False
            )
        )

    one = identity_automorphism

    def _repr_(self) -> str:
        if self.aut_family() is not None:
            return f"Aut_{self.base_category()}({self.domain_object()})"
        return (
            f"Iso_{self.base_category()}({self.domain_object()}, "
            f"{self.codomain_object()})"
        )


class FixedAutCategory(FixedIsoCategory):
    def identity_automorphism(self) -> CategoricalIsomorphism:
        identity = self.arrow_set().identity()
        return self(
            CategoricalIsomorphism(
                identity.parent(), identity, identity, verify=False
            )
        )

    one = identity_automorphism

    def super_categories(self):
        packet = _category_packet(self.base_category())
        obj = self.domain_object()
        inherited = [
            self.hom_family().family_over(supercategory).Of(obj)
            for supercategory in _packet_supercategories(self.base_category())
        ]
        return [
            packet.Ends().Of(obj),
            packet.Isos().Of(obj, obj),
            *inherited,
        ]

    def _repr_(self) -> str:
        return f"Aut_{self.base_category()}({self.domain_object()})"


class HomCategories(OwnedCategoryBase):
    r"""The category of represented fixed-endpoint Hom categories.

    Its objects are the categories ``Hom_C(A,B)``, each built by the ``Of``
    entry of the Hom family of its base category ``C``.
    """

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return [Cat()]

    def an_object(self) -> Category:
        r"""The Hom of the witness of the category of sets to itself."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        witness = Sets().an_object()
        return Sets().Mor(witness, witness)

    def __contains__(self, candidate: Any) -> bool:
        r"""Whether ``candidate`` is a fixed Hom category.

        A fixed Hom category built over the owned category base records this
        placement as its ``category()``.  A Hom realized on Sage's ``Homset``
        has one ``category()`` slot, holding the enrichment its arrows form (a
        set, a module), so its placement here is recorded where it was made:
        by the family whose ``Of`` entry built it for its endpoints.
        """
        match candidate:
            case CategoricalHomset():
                return (
                    candidate.hom_family().Of(
                        candidate.domain_object(), candidate.codomain_object()
                    )
                    is candidate
                )
            case _:
                return super().__contains__(candidate)


FixedHomObject = CategoricalHomset | FixedHomCategory
FixedHomClass = type[CategoricalHomset] | type[FixedHomCategory]


class CategoryPacket:
    r"""The coordinated ``C / Hom_C / End_C / Iso_C / Aut_C`` families of one category.

    Not a mathematical object: the six families are the values of six
    operations of ``C`` (``HomCategory()``, ``EndCategory()``, ...), and this
    is the memo that holds them so that each is built once.  It is interned
    by the identity of ``C`` in :func:`_category_packet`.
    """

    def __init__(self, category: Category) -> None:
        self._category = category
        # Family objects are deliberately lazy.  A family category such as
        # ``Mono_C`` has ``Hom_C`` as a semantic supercategory, and Sage asks
        # for that supercategory while constructing ``Mono_C`` itself.  Eager
        # construction therefore recurses through an only half-built packet.
        # The packet object is interned first; each family can then safely ask
        # for its siblings during category initialization.
        self._homs = None
        self._ends = None
        self._monos = None
        self._epis = None
        self._isos = None
        self._auts = None

    def category(self) -> Category:
        return self._category

    C = category

    def Homs(self) -> _HomCategoryOf:
        if self._homs is None:
            self._homs = _declared_family(
                self.category(), "_HomCategory", _HomCategoryOf
            )
        return self._homs

    def Ends(self) -> _EndCategoryOf:
        if self._ends is None:
            self._ends = _declared_family(
                self.category(), "_EndCategory", _EndCategoryOf
            )
        return self._ends

    def Monos(self) -> _MonoCategoryOf:
        if self._monos is None:
            self._monos = _declared_family(
                self.category(), "_MonoCategory", _MonoCategoryOf
            )
        return self._monos

    def Epis(self) -> _EpiCategoryOf:
        if self._epis is None:
            self._epis = _declared_family(
                self.category(), "_EpiCategory", _EpiCategoryOf
            )
        return self._epis

    def Isos(self) -> _IsoCategoryOf:
        if self._isos is None:
            self._isos = _declared_family(
                self.category(), "_IsoCategory", _IsoCategoryOf
            )
        return self._isos

    def Auts(self) -> _AutCategoryOf:
        if self._auts is None:
            self._auts = _declared_family(
                self.category(), "_AutCategory", _AutCategoryOf
            )
        return self._auts

    def super_packets(self):
        return tuple(
            _category_packet(category)
            for category in _packet_supercategories(self.category())
        )

    def __repr__(self) -> str:
        return f"Category packet of {self.category()}"


def _declared_construction(category, declaration_name):
    r"""Return the first packet-family declaration on the category MRO, if any.

    This reads the ``_HomCategory`` / ``_EndCategory`` / ... declarations a
    category class makes, the same way the owned root reads a category's
    ``ParentMethods`` declaration: off the declaring class graph, never off
    an instance.  It is the reader of that declaration protocol.
    """
    declaring = type(category)
    if declaring.__name__.endswith("_with_category"):
        declaring = declaring.__base__
    for ancestor in declaring.__mro__:
        construction = ancestor.__dict__.get(declaration_name)
        if isinstance(construction, property):
            # A recursive category construction may declare its family lazily.
            # Read only the explicit descriptor at its declaring owner, rather
            # than invoking Sage's dynamic category attribute fallback.
            construction = construction.__get__(category, declaring)
        if isinstance(construction, type):
            return construction
    return None


def _declared_family(category, declaration_name, default):
    r"""Construct the packet family ``category`` declares, else ``default``."""
    construction = _declared_construction(category, declaration_name)
    return (default if construction is None else construction)(category)


@cached_function(key=lambda category: id(category))
def _category_packet(category: Category) -> CategoryPacket:
    r"""The packet attached to this exact category object.

    Unverified specimen: a Homset's native value comparison must not identify
    two categories whose endpoint parents are distinct::

        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: left = finite_ordered_set(("a", "b"))
        sage: right = finite_ordered_set(("a", "b"))
        sage: left == right and left is not right
        True
        sage: first, second = Sets().Mor(left, left), Sets().Mor(right, right)
        sage: first.category_packet().C() is first
        True
        sage: second.category_packet().C() is second
        True
        sage: first.category_packet().Homs().base_category() is first
        True
        sage: second.category_packet().Homs().base_category() is second
        True
        sage: first.category_packet() is not second.category_packet()
        True
    """
    return CategoryPacket(category)


class _HomCategoryOf(OwnedCategoryBase):
    r"""The family ``(A,B) |-> Hom_C(A,B)`` attached to one category ``C``."""

    FixedCategoryClass = FixedHomCategory
    _declaration_name = "_HomCategory"

    @staticmethod
    @cached_function(key=lambda cls, base_category: (cls, id(base_category)))
    def __classcall__(cls, base_category):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(base_category)
        # A category that declares its own Hom family has exactly one; naming
        # the generic family on it resolves to the declared one.
        declared = _declared_construction(base_category, cls._declaration_name)
        if declared is not None and not issubclass(cls, declared):
            return declared(base_category)
        # A fixed Hom is also a Homset whose native comparison may compare
        # its endpoints by value. The family is attached to the exact category,
        # not to another Hom with equal-but-distinct endpoint objects.
        return typecall(cls, base_category)

    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        # Several owned Hom-family specializations choose a concrete fixed
        # Hom parent class from the endpoints.  Keep that endpoint cache on
        # the common family object rather than relying on Sage category
        # internals for it.
        self._objects = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return id(self._base_category)

    def base_category(self) -> Category:
        return self._base_category

    def family_over(self, category: Category) -> _HomCategoryOf:
        return _category_packet(category).Homs()

    def fixed_category_class(self) -> FixedHomClass:
        return self.FixedCategoryClass

    def fixed_category_class_for(
        self,
        domain: Parent,
        codomain: Parent,
    ) -> FixedHomClass:
        r"""Return the represented fixed Hom class for these endpoints."""
        return self.fixed_category_class()

    def _inherits_morphisms_from(self, supercategory, domain, codomain) -> bool:
        r"""Whether this family may reuse ``supercategory``'s object literally.

        The Hom family itself has nothing further to ask: the class of what it
        would build against the class of what it inherits already decides it.
        A family that carves its objects out of a Hom overrides this, because
        the carving is only the same when the Hom is.
        """
        return True

    def _cached_between(self, domain, codomain):
        r"""Return the exact cached fixed-endpoint object, if present.

        Endpoint identity is part of the mathematical type.  Hashing/equality of
        endpoints is deliberately irrelevant here and can itself re-enter Hom
        construction, so every Hom-family specialization shares this one
        identity-sensitive lookup.
        """
        cached = self._objects.get((id(domain), id(codomain)))
        if cached is None:
            return None
        return cached if (
            cached.domain_object() is domain and cached.codomain_object() is codomain
        ) else None

    def _remember_between(self, domain, codomain, value):
        self._objects[id(domain), id(codomain)] = value
        return value

    def an_object(self) -> Category:
        r"""The Hom of the base category's witness to itself."""
        witness = self.base_category().an_object()
        return self.Of(witness, witness)

    def super_categories(self):
        supers = [
            self.family_over(category)
            for category in _packet_supercategories(self.base_category())
        ]
        return supers + [HomCategories()]

    def Of(self, domain: Parent, codomain: Parent) -> FixedHomObject:
        r"""Select the defining Hom object without losing inherited structure.

        This is the constructor entry for the objects of this family, so the
        one place the runtime class a fixed Hom is realized by is compared:
        a property subcategory inherits the declaration of the category it
        refines and reuses the parent that category built.

        Unverified specimens: a property category shares its defining Hom;
        a restricted category shares the underlying Hom-set, not its predicate::

            sage: from dzack_research.preamble.categories.sets.set_categories import Sets, FiniteSets
            sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
            sage: points = finite_ordered_set(("a", "b"))
            sage: hom = FiniteSets().category_packet().Homs().Of(points, points)
            sage: hom is Sets().Mor(points, points)
            True
            sage: end = FiniteSets().category_packet().Ends().Of(points)
            sage: end is hom and end.end_family() is Sets().category_packet().Ends()
            True
            sage: monos = Sets().category_packet().Monos().Of(points, points)
            sage: epis = Sets().category_packet().Epis().Of(points, points)
            sage: monos.arrow_set() is hom and epis.arrow_set() is hom
            True
            sage: constant = hom(lambda point: "a")
            sage: constant in hom, constant in monos, constant in epis
            (True, False, False)
            sage: swap = hom(lambda point: "b" if point == "a" else "a")
            sage: swap in monos and swap in epis
            True
            sage: aut = FiniteSets().category_packet().Auts().Of(points)
            sage: aut is Sets().category_packet().Isos().Of(points, points)
            True
            sage: aut.aut_family() is Sets().category_packet().Auts()
            True
            sage: identity = hom.identity_2(swap)
            sage: identity * identity == identity
            True
        """
        if _has_category_packet_surface(self.base_category()):
            domain = self.base_category()._hom_endpoint(domain)
            codomain = self.base_category()._hom_endpoint(codomain)
        if domain not in self.base_category() or codomain not in self.base_category():
            raise TypeError("Hom endpoints must lie in the base category")
        # Endpoint identity, not a hash: hashing a Hom endpoint re-enters Hom
        # construction, so Sage's cached_method recurses here.  Endpoint
        # refinement may strengthen the represented fixed homset, so a
        # cached parent is reusable only if it still has the selected class.
        fixed_class = self.fixed_category_class_for(domain, codomain)
        cached = self._cached_between(domain, codomain)
        # What decides whether this category needs a Hom parent of its own is
        # whether the Hom it would build differs from one it already inherits,
        # not whether a class was declared somewhere in its Python ancestry: a
        # property subcategory inherits the declaration of the category it
        # refines and would build exactly the parent that category built.  So
        # the supercategories are always walked, and a candidate survives when
        # this category states nothing stronger than the class it already is.
        inherited = []
        for supercategory in _packet_supercategories(self.base_category()):
            if not self._inherits_morphisms_from(supercategory, domain, codomain):
                continue
            # Some owned categories admit substrate objects by their own
            # mathematical recognition rule (Sets admits Sage set parents, for
            # example) without mutating those parents into every semantic
            # supercategory.  A Hom can only be inherited from a supercategory
            # when that supercategory actually admits both endpoints; otherwise
            # there is no fixed Hom object there to reuse.
            if domain not in supercategory or codomain not in supercategory:
                continue
            candidate = self.family_over(supercategory).Of(domain, codomain)
            if not (
                fixed_class is FixedHomCategory or isinstance(candidate, fixed_class)
            ):
                continue
            if all(candidate is not known for known in inherited):
                inherited.append(candidate)

        inherited = _minimal_inherited_homs(inherited)
        if len(inherited) == 1:
            # One inherited Hom of the class this category would have built:
            # the subcategory adds no morphisms, so reuse that object literally
            # rather than fabricating a second parent for the same maps.
            result = inherited[0]
        elif fixed_class is not FixedHomCategory:
            # This family states a Hom class of its own.  Nothing it inherits
            # is that class, or several inherited ones disagree; either way it
            # is not, for morphism purposes, a subcategory of any single one,
            # and it builds what it declared.
            result = (
                cached
                if isinstance(cached, fixed_class) and cached.hom_family() is self
                else fixed_class(self, domain, codomain)
            )
        elif inherited:
            raise TypeError(
                f"{self.base_category()} inherits incompatible Hom constructions; "
                "declare _HomCategory explicitly"
            )
        else:
            # No declared or inherited implementation remains.  The root
            # fixed category owns its private Hom-set; the public Hom ingress
            # must not be called recursively while this object is constructed.
            result = (
                cached
                if isinstance(cached, fixed_class) and cached.hom_family() is self
                else fixed_class(self, domain, codomain)
            )
        return self._remember_between(domain, codomain, result)

    Between = Of

    def __contains__(self, candidate: Any) -> bool:
        r"""A fixed Hom category of this family: the object built for its endpoints."""
        if candidate not in HomCategories():
            return False
        domain = candidate.domain_object()
        codomain = candidate.codomain_object()
        if domain not in self.base_category() or codomain not in self.base_category():
            return False
        return self.Of(domain, codomain) is candidate

    def _repr_(self) -> str:
        return f"Hom-category packet of {self.base_category()}"


class _DiscreteTwoHomCategoryOf(_HomCategoryOf):
    r"""The Hom family of a fixed Hom category with only identity 2-arrows.

    An object of the base is a represented arrow. Between identical arrow
    objects there is its identity; between distinct objects there is no arrow.
    The ordinary Hom-family cache owns both constructions.

    Unverified specimens: the explicit 2-Hom and the packet select one parent,
    and an ordinary identity functor can act on its actual identity arrow::

        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: from dzack_research.preamble.categories.functors.core import IdentityFunctor
        sage: points = finite_ordered_set(("a", "b"))
        sage: hom = Sets().Mor(points, points)
        sage: swap = hom(lambda point: {"a": "b", "b": "a"}[point])
        sage: obj = hom.object(swap)
        sage: two_hom = hom.two_hom(swap, swap)
        sage: two_hom is hom.HomCategory().Of(obj, obj)
        True
        sage: two_hom is hom.category_packet().Homs().Between(swap, swap)
        True
        sage: two_hom is _category_homset(hom, obj, obj)
        True
        sage: identity = two_hom.identity()
        sage: IdentityFunctor(hom)(identity) is identity
        True
        sage: identity * identity == identity
        True
        sage: monos = Sets().Mono(points, points)
        sage: two_hom is monos.Mor(swap, swap)
        True
        sage: monos.two_hom(swap, swap) is monos.category_packet().Homs().Of(obj, obj)
        True
        sage: hom.two_hom(swap, hom.identity()).identity()
        Traceback (most recent call last):
        ...
        ValueError: distinct arrows have no represented 2-morphism

    Unverified specimen for a Hom that also has a module structure::

        sage: from dzack_research.preamble.all import Modules, QQ
        sage: module = QQ.free_module(1)
        sage: linear_hom = Modules(QQ).Mor(module, module)
        sage: identity = linear_hom.identity()
        sage: obj = linear_hom.object(identity)
        sage: two_hom = linear_hom.two_hom(identity, identity)
        sage: _category_homset(linear_hom, obj, obj) is two_hom
        True
        sage: IdentityFunctor(linear_hom)(two_hom.identity()) is two_hom.identity()
        True
    """

    FixedCategoryClass = HomArrowDiscreteHomset


def _carves_the_same_hom(self, supercategory, domain, codomain) -> bool:
    r"""Whether this category and ``supercategory`` have one and the same Hom.

    The monomorphisms, epimorphisms and isomorphisms of a category are cut out
    of its Hom, so a subcategory inherits them exactly when it inherits the
    Hom they are cut from.  A category of Lie algebras and the modules under
    it agree on which linear maps are bijections and disagree on which maps
    are morphisms at all, so its automorphisms are its own.
    """
    if _declared_construction(
        self.base_category(), self._declaration_name
    ) is not _declared_construction(supercategory, self._declaration_name):
        # A declared restriction may change even when the underlying Hom
        # does not.  Do not replace that predicate by an ancestor's predicate
        # merely because both use FixedRestrictedHomCategory to represent it.
        return False
    return (
        _category_packet(self.base_category()).Homs().Of(domain, codomain)
        is _category_packet(supercategory).Homs().Of(domain, codomain)
    )


class _EndCategoryOf(_HomCategoryOf):
    r"""The family ``A |-> End_C(A)``."""

    FixedCategoryClass = FixedEndCategory
    _declaration_name = "_EndCategory"

    def family_over(self, category: Category) -> _EndCategoryOf:
        return _category_packet(category).Ends()

    def an_object(self) -> Category:
        return self.Of(self.base_category().an_object())

    def Of(
        self,
        obj: Parent,
        codomain: Parent | None = None,
    ) -> FixedHomObject:
        if _has_category_packet_surface(self.base_category()):
            obj = self.base_category()._hom_endpoint(obj)
            if codomain is not None:
                codomain = self.base_category()._hom_endpoint(codomain)
        if codomain is not None and codomain is not obj:
            raise ValueError("an endomorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the endomorphism object must lie in the base category")
        endomorphisms = _category_packet(self.base_category()).Homs().Of(obj, obj)
        # A Hom shared with the category above is the same set of morphisms, so
        # its endomorphisms are the same too and the End object is that one.
        # Its defining category owns the role regardless of which inherited
        # family is queried first.
        if endomorphisms.end_family() is None:
            endomorphisms.attach_end_family(_category_packet(endomorphisms.base_category()).Ends())
        return self._remember_between(obj, obj, endomorphisms)

    def Between(self, domain: Parent, codomain: Parent) -> FixedHomObject:
        return self.Of(domain, codomain)

    def _repr_(self) -> str:
        return f"End-category packet of {self.base_category()}"


class _RestrictedHomCategoryOf(_HomCategoryOf):
    r"""A family of fixed-endpoint subcategories of an existing ``Mor``."""

    FixedCategoryClass = FixedRestrictedHomCategory

    _inherits_morphisms_from = _carves_the_same_hom

    @abstract_method
    def accepts(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` belongs to this restricted Hom family."""

    def super_categories(self):
        inherited = [
            self.family_over(category)
            for category in _packet_supercategories(self.base_category())
        ]
        return [_category_packet(self.base_category()).Homs(), *inherited, HomCategories()]


_RestrictedCategoryOf = _RestrictedHomCategoryOf


class _MonoCategoryOf(_RestrictedHomCategoryOf):
    _declaration_name = "_MonoCategory"

    def family_over(self, category: Category) -> _MonoCategoryOf:
        return _category_packet(category).Monos()

    def accepts(self, arrow: Morphism) -> bool:
        try:
            return arrow.is_injective() is True
        except (AttributeError, NotImplementedError):
            return False


class _EpiCategoryOf(_RestrictedHomCategoryOf):
    _declaration_name = "_EpiCategory"

    def family_over(self, category: Category) -> _EpiCategoryOf:
        return _category_packet(category).Epis()

    def accepts(self, arrow: Morphism) -> bool:
        try:
            return arrow.is_surjective() is True
        except (AttributeError, NotImplementedError):
            return False


class _IsoCategoryOf(_HomCategoryOf):
    FixedCategoryClass = FixedIsoCategory
    _declaration_name = "_IsoCategory"

    _inherits_morphisms_from = _carves_the_same_hom

    def family_over(self, category: Category) -> _IsoCategoryOf:
        return _category_packet(category).Isos()

    def super_categories(self):
        packet = _category_packet(self.base_category())
        inherited = [
            self.family_over(category)
            for category in _packet_supercategories(self.base_category())
        ]
        return [
            packet.Homs(),
            packet.Monos(),
            packet.Epis(),
            *inherited,
            HomCategories(),
        ]


class _AutCategoryOf(_IsoCategoryOf):
    r"""The family ``A |-> Aut_C(A)``."""

    FixedCategoryClass = FixedAutCategory
    _declaration_name = "_AutCategory"

    def family_over(self, category: Category) -> _AutCategoryOf:
        return _category_packet(category).Auts()

    def an_object(self) -> Category:
        return self.Of(self.base_category().an_object())

    def super_categories(self):
        packet = _category_packet(self.base_category())
        inherited = [
            self.family_over(category)
            for category in _packet_supercategories(self.base_category())
        ]
        return [packet.Ends(), packet.Isos(), *inherited, HomCategories()]

    def Of(
        self,
        obj: Parent,
        codomain: Parent | None = None,
    ) -> FixedHomObject:
        if _has_category_packet_surface(self.base_category()):
            obj = self.base_category()._hom_endpoint(obj)
            if codomain is not None:
                codomain = self.base_category()._hom_endpoint(codomain)
        if codomain is not None and codomain is not obj:
            raise ValueError("an automorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the automorphism object must lie in the base category")
        automorphisms = _category_packet(self.base_category()).Isos().Of(obj, obj)
        # As for End above: a shared Iso object has the same isomorphisms, so
        # the same automorphisms. Their defining category owns the role.
        if automorphisms.aut_family() is None:
            automorphisms.attach_aut_family(_category_packet(automorphisms.base_category()).Auts())
        return self._remember_between(obj, obj, automorphisms)

    def Between(self, domain: Parent, codomain: Parent) -> FixedHomObject:
        return self.Of(domain, codomain)

    def _repr_(self) -> str:
        return f"Aut-category packet of {self.base_category()}"


class HomCategoryConstruction(_HomCategoryOf):
    pass


class EndCategoryConstruction(_EndCategoryOf):
    pass


class MonoCategoryConstruction(_MonoCategoryOf):
    pass


class EpiCategoryConstruction(_EpiCategoryOf):
    pass


class IsoCategoryConstruction(_IsoCategoryOf):
    pass


class AutCategoryConstruction(_AutCategoryOf):
    pass


__all__ = [
    "AutCategoryConstruction",
    "CategoryPacketMethods",
    "CategoricalHomset",
    "CategoricalIsomorphism",
    "EndCategoryConstruction",
    "EpiCategoryConstruction",
    "FixedAutCategory",
    "FixedEndCategory",
    "FixedHomCategory",
    "FixedIsoCategory",
    "HomArrowIdentity",
    "HomCategories",
    "HomCategoryConstruction",
    "IsoCategoryConstruction",
    "MonoCategoryConstruction",
    "RestrictedHomCategoryParent",
]
