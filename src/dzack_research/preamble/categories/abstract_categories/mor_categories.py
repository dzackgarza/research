r"""Mor/End/Mono/Epi/Iso/Aut category packets.

For every category ``C`` and objects ``A,B`` in ``C`` we represent
``Hom_C(A,B)`` itself as a category.  Its objects are the actual arrows
``A -> B``.  In the absence of represented 2-morphisms this category is
discrete.  An inclusion ``C <= D`` can include these fixed categories' arrows
without identifying ``Hom_C(A,B)`` with ``Hom_D(A,B)``.  The families classify
the selected category objects, not their individual arrows: their inclusions
must preserve those category objects.  In particular ``Ends(C) <= Mors(C)``
and ``Auts(C) <= Isos(C)`` reuse the same diagonal categories.  A functor
changing the fixed category acts through ``induced_mor_functor``,
``induced_end_functor`` or ``induced_aut_functor``.

This is intentionally distinct from the *underlying Mor object parent*.  The
latter may carry additional enrichment -- for example ``Hom_R(M,N)`` is an
``R``-module -- while there remains exactly one categorical Mor object for the
chosen category and endpoints.

An arrow ``f: A -> B`` regarded as an object is an object of the arrow
category ``Ar(C)``, built through that category's entry; ``Hom_C(A,B)`` read
as a category is the fibre of ``(dom, cod): Ar(C) -> C x C`` at ``(A, B)``.
In a 1-category its morphisms are squares whose two endpoint maps are
identities: commutativity then says that their two arrows are equal.  It is
therefore discrete, not the full arrow subcategory on these objects (which
also has squares with nonidentity endpoint endomorphisms).  A Mor category
reuses the arrow objects without inheriting all the squares between them.
"""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category
from sage.categories.mor import Hom as SageHom, Mor as SageMor
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

from dzack_research.preamble.categories.abstract_categories.mor_foundation import (
    CategoryPacketMethods,
    OwnedMor,
    _has_category_packet_surface,
    _underlying_set_mor,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.lexicon.category_theory import ObjectOfCategory
from dzack_research.preamble.lexicon.set_theory import SetObject
from dzack_research.preamble.owned_category_bases import Category as OwnedCategoryBase
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.refine import (
    construction_scope,
    realize_owned_category,
    refine,
    run_construction_hooks,
)


def _category_mor(
    category: Category | None,
    domain: Parent,
    codomain: Parent,
) -> FixedMorObject | SageMor:
    r"""The complete selected Mor, including any defining arrow predicate.

    Mathematical admission uses this object's ``accepts`` operation via
    :func:`_category_accepts_morphism`. Category containment instead concerns
    its constructed arrow objects. Its private ``arrow_set`` may also
    represent maps outside a restricted Mor category, so membership in that
    parent alone is not admission to the selected category.
    """
    if _has_category_packet_surface(category):
        # Admission follows the category's public Mor selector.  Most owned
        # categories inherit the packet implementation, while constructions
        # such as G-objects and functor categories legitimately specialize
        # ``Mor`` for their represented object type.  Bypassing that selector
        # rebuilds the packet Mor against endpoints that may be wrappers for a
        # more specific representation.
        return category.Mor(domain, codomain)
    return SageHom(domain, codomain, category)


def _category_accepts_morphism(
    category: Category | None,
    domain: Parent,
    codomain: Parent,
    arrow: Morphism,
) -> bool:
    r"""Ask the selected Mor owner to admit an arrow with these endpoints.

    This is the shared admission adapter for functors and categorical
    constructions. An owned fixed Mor category distinguishes an arrow's
    defining datum from the object constructed on it: ``accepts`` admits
    that datum; ``in`` reads object placement. The native Sage-Mor boundary
    instead uses its element-membership operation. Neither route constructs
    a trial object or drops a selected restriction by asking ``arrow_set``.
    """
    selected = _category_mor(category, domain, codomain)
    match selected:
        case Category():
            return selected.accepts(arrow)
        case _:
            return arrow in selected


def _arrow_is_inherited_from_subcategory(target, arrow: Morphism) -> bool:
    r"""Return whether ``arrow`` lies in a stronger Mor category below ``target``.

    If ``D <= C``, every ``D``-morphism is definitionally a ``C``-morphism.
    A structured Mor parent may represent that stronger arrow by a different
    morphism class, so admission follows the Mor-category edge itself rather
    than reconstructing and re-verifying the same arrow in ``C``.
    """
    parent = arrow.parent()
    return (
        parent in MorCategories()
        and parent.domain_object() is target.domain_object()
        and parent.codomain_object() is target.codomain_object()
        and _declared_category_reaches(parent, target)
    )


def _category_mor_parent(
    category: Category | None,
    domain: Parent,
    codomain: Parent,
) -> SageMor:
    r"""Return the declared Mor object for an explicitly selected category.

    Selecting ``C`` must not forget its structure: linear, algebra and equivariant maps are
    constructed by ``C``'s declared Mor family, not by the private
    function-map substrate. An enriched Mor is also a mathematical parent;
    its inherited parent-level ``Mor`` is not the Mor of that category.
    Native Sage categories retain their native Mor ingress.

    Use ``_category_mor`` for admission. This adapter provides the runtime
    parent required by Sage morphisms, and a restricted Mor need not contain
    every map represented by that parent.
    """
    selected = _category_mor(category, domain, codomain)
    match selected:
        case Category():
            return selected.arrow_set()
        case _:
            return selected


def _declared_category_reaches(category: Category, target: Category) -> bool:
    r"""Return whether ``target`` occurs in ``category``'s declared supergraph.

    Fixed Mor objects can be distinct runtime parents even when one is the
    inherited specialization of the other.  Sage's ``is_subcategory`` is not
    reliable for these mixed Category/Parent Mor objects, so selection follows
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
    r"""Discard inherited Mor objects strictly above another candidate.

    A join of object properties may reach the same arrow theory through several
    branches.  If one branch carries a genuinely stronger Mor object (for
    example commuting triangles between represented subobjects), that object is
    the Mor of the join; its ordinary underlying Mor is only a supercategory.
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
    native Mor dispatch is endpoint-driven and can jump back into a stronger
    owned category, so transporting Mor/End/Aut packets through them creates
    cycles and, more importantly, the wrong semantic graph.

    These are *declared supercategories*.  Each supplies its own Mor family;
    an endpoint's default Mor does not choose that family.  In particular a
    subobject's inherited Mor comes from the declared category of the base
    object, not from rediscovering the subobject category through its
    inclusion.
    """
    return tuple(
        supercategory
        for supercategory in category.super_categories()
        if _has_category_packet_surface(supercategory)
    )


def _precomposable(second: Morphism, first) -> bool:
    r"""Whether ``first`` composes before ``second`` in ``second``'s Mor theory.

    The right operand of ``*`` is arbitrary, so this is the admission of the
    composition operator: ``first`` is an arrow of the same base category whose
    codomain is ``second``'s domain.  The arrow's own Mor is asked.
    """
    match first:
        case Morphism() if first.codomain() is second.domain():
            base = second.parent().base_category()
            return _category_accepts_morphism(base, first.domain(), first.codomain(), first)
        case _:
            return False


@cached_function(key=lambda category, arrow: (id(category), id(arrow)))
def _fixed_mor_arrow_object(
    category: FixedMorObject,
    arrow: Morphism,
) -> ObjectOfCategory:
    r"""Construct the one object of a fixed Mor on this admitted arrow.

    The two fixed-Mor realizations share this entry. Their raw arrows have
    parent semantics, while their objects carry the fixed Mor's category
    placement and the walking-arrow functor. Interning by those two
    identities makes every spelling of an endpoint select the same object;
    it does not identify two distinct arrow data by a sampled equality test.
    """
    if not category.accepts(arrow):
        raise ValueError(f"{arrow} is not an arrow of {category}")
    arrows = category.base_category().ArrowCategory()
    represented = arrows(arrow)
    return _object_of(
        Category.join((arrows, category)),
        functor=represented.functor(),
    )


class MorArrowIdentity(Morphism):
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
        # The discrete 2-Mor on one arrow object holds its identity only, so
        # the composable arrows are exactly the elements of this parent.
        if other not in self.parent():
            return NotImplemented
        return self.parent().identity()


class CategoricalMor(CategoryPacketMethods, OwnedMor, Category):
    r"""A represented Mor object which is both a Sage Mor and a category.

    This mixed runtime parent deliberately retains Sage's raw ``Category`` base.
    Its ``Parent.category()`` records the Mor object's enrichment placement;
    replacing that parent role by ``OwnedCategoryObject`` would instead force
    ``category()`` to be ``Cat()`` and erase the represented Mor object structure.
    Pure category objects in this module use :class:`OwnedCategoryBase`; this
    one is the boundary where the two runtime roles genuinely coincide.

    This is the live counterpart of the archived owned Mor-category base.  It
    keeps Sage's hard requirement that every ``Morphism`` be parented by an
    actual ``Mor``, while also making that same parent the discrete category
    ``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
    the *same object*.
    """

    @staticmethod
    def __classcall__(cls, *arguments, **options):
        # ``Category`` is a UniqueRepresentation whose default classcall does
        # not include fixed Mor endpoints in the identity of this mixed
        # Mor/category object.  The owning Mor family already interns by
        # ``(domain,codomain)``, so bypass Category's cache here.  Subclasses
        # name their own construction data, so the signature stays open.
        return typecall(cls, *arguments, **options)

    def __init__(
        self,
        family: _MorCategoryOf,
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
        # The semantic Mor/End supertree is deliberately richer than the
        # method-provider hierarchy Sage should use to synthesize Python
        # classes for this mixed Mor/category parent.  Feeding fixed Mor
        # objects back into Sage's C3 category-class builder creates cycles as
        # soon as a super-Mor is refined (for example End_R(M) as a ring).
        # Packet/enrichment code transports the mathematical structure
        # explicitly, so the runtime method spine stays at Objects().
        self._super_categories_for_classes = [SageObjects()]
        Category.__init__(self)
        SageMor.__init__(
            self,
            domain,
            codomain,
            category=SageSets(),
            base=base,
        )
        if category is not None:
            # Sage ``Mor`` insists on constructing first in ``Sets`` so it
            # can form its private Mors/Endsets runtime category.  Complete
            # the owned enrichment while this constructor is still active;
            # callers never observe an un-enriched module Mor parent.
            refine(self, category)

    def _already_parented_arrow(self, candidate: Morphism) -> bool:
        r"""Whether ``candidate`` is already represented by this Mor theory."""
        return candidate.parent() is self or _arrow_is_inherited_from_subcategory(self, candidate)

    def __call__(self, *args, **kwargs):
        r"""Construct an arrow, preserving one already represented here.

        If ``D <= C``, a ``D``-arrow is already a ``C``-arrow.  Reading it in
        the weaker Mor must therefore preserve the arrow rather than
        reinterpret its object as generator images or presentation data.
        """
        match args:
            case (Morphism() as arrow,) if not kwargs and self._already_parented_arrow(arrow):
                return arrow
        return self._element_constructor_(*args, **kwargs)

    def mor_family(self) -> _MorCategoryOf:
        return self._family

    @property
    def _MorCategory(self) -> type[_MorCategoryOf]:
        # The Mor objects and their family are mutually recursive types.
        # Resolve the family's declaration only after this module is loaded.
        return _DiscreteTwoMorCategoryOf

    def mor_category(self) -> Category:
        r"""Return the owned mathematical category whose Mor object this is.

        Sage's ``Mor`` initialization still uses ``Sets()`` only as the
        private runtime method spine.  The semantic Mor category is the base
        category of the owned Mor family.
        """
        return self.mor_family().base_category()

    def identity_at(self, obj: Parent) -> Morphism:
        return self.mor_family().Of(obj, obj).arrow_set().identity()

    def attach_end_family(self, family: _EndCategoryOf) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an endomorphism Mor category can carry an End-family role")
        owner = _category_packet(self.base_category()).Ends()
        if family is not owner:
            represented = _category_packet(family.base_category()).Mors().Of(
                self.domain_object(), self.codomain_object()
            )
            if represented is not self and represented.arrow_set() is not self:
                raise ValueError("the End family selects a different fixed Mor object")
        if self._end_family is not None and self._end_family is not owner:
            raise ValueError("one fixed Mor category cannot carry two End-family roles")
        self._end_family = owner
        owner._remember_between(self.domain_object(), self.codomain_object(), self)

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
        owner._remember_between(self.domain_object(), self.codomain_object(), self)

    def aut_family(self) -> _AutCategoryOf | None:
        return self._aut_family

    def identity_endomorphism(self) -> Morphism:
        if self.end_family() is None:
            raise ValueError("this fixed Mor category has not been given an End-family role")
        identity = self.arrow_set().identity()
        return self(identity)

    one = identity_endomorphism

    def base_category(self) -> Category:
        return self.mor_family().base_category()

    def domain_object(self) -> ObjectOfCategory:
        return self._domain_object

    def codomain_object(self) -> ObjectOfCategory:
        return self._codomain_object

    def arrow_set(self) -> SetObject:
        return self

    underlying_mor = arrow_set

    def accepts(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` is an arrow of this Mor category.

        An arrow placed here, or in the Mor of a subcategory with the same
        endpoints, is one.  Constructing a new arrow from its defining data
        is a separate operation: constructor failure is not a membership
        decision, and successful conversion does not place the input here.
        """
        if arrow.domain() is not self.domain_object() or arrow.codomain() is not self.codomain_object():
            return False
        return self._already_parented_arrow(arrow)

    def object(self, arrow: Parent | Morphism):
        r"""``arrow`` as an object placed in this fixed Mor and in ``Ar(C)``."""
        match arrow:
            case Morphism():
                if not self.accepts(arrow):
                    arrow = self(arrow)
                return _fixed_mor_arrow_object(self, arrow)
            case _ if Category.__contains__(self, arrow):
                return arrow
            case _ if arrow in self.base_category().ArrowCategory():
                return self.object(arrow.arrow())
            case _:
                raise TypeError("a fixed Mor object is constructed from an arrow or an arrow object")

    def _mor_endpoint(self, obj: Parent | Category | Morphism):
        return self.object(obj)

    def __contains__(self, candidate: Any) -> bool:
        r"""Read raw-map element membership separately from object placement.

        An enriched Mor can be a mathematical set of maps, whose owner may
        decide an exact element predicate (injectivity of a finite set map,
        for example). An arrow object is instead placed in a category; its
        underlying arrow is not reclassified by that element predicate.
        """
        match candidate:
            case Morphism():
                return self.accepts(candidate)
            case _:
                return Category.__contains__(self, candidate)

    def super_categories(self):
        supers = []
        for supercategory in _packet_supercategories(self.base_category()):
            supers.append(
                self.mor_family().family_over(supercategory).Of(
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

    def two_mor(
        self,
        domain: Parent | Morphism,
        codomain: Parent | Morphism,
    ) -> CategoricalMor:
        return self.MorCategory().Of(domain, codomain)

    Mor = two_mor

    def identity_2(self, arrow: Morphism) -> Morphism:
        arrow_object = self.object(arrow)
        return self.two_mor(arrow_object, arrow_object).identity()


class MorArrowDiscreteMor(CategoricalMor):
    r"""The discrete 2-Mor between two arrow objects.

    The objects of a fixed Mor category are the arrows themselves, so this is
    the Mor object of that category: it is discrete because no 2-morphisms are
    represented.
    """

    Element = MorArrowIdentity

    def __init__(
        self,
        family: _DiscreteTwoMorCategoryOf,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(self, family, domain, codomain)

    def mor_category(self) -> Category:
        return self.base_category()

    def _element_constructor_(self, value=None):
        if self.domain() is not self.codomain():
            raise ValueError("distinct arrows have no represented 2-morphism")
        if value is not None:
            if parent(value) is not self:
                raise ValueError("the discrete 2-Mor contains only its identity")
            return value
        return self.element_class(self)

    @cached_method
    def identity(self) -> MorArrowIdentity:
        return self()


class FixedMorCategory(CategoryPacketMethods, OwnedCategoryBase):
    r"""The category ``Hom_C(A,B)`` of arrows with fixed endpoints.

    Its objects are the objects of ``Ar(C)`` lying over ``(A, B)``; it owns
    no object class, and ``object(f)`` builds through ``Ar(C)``'s entry.
    """

    @staticmethod
    def __classcall__(cls, family, domain, codomain):
        # The owning Mor-family already interns fixed categories by their
        # endpoint identities.  Sage ``Category``'s UniqueRepresentation cache
        # does not include those endpoints and can otherwise collapse
        # ``Hom_C(A,B)`` with a previously created ``Hom_C(A',B')``.
        return typecall(cls, family, domain, codomain)

    def __init__(
        self,
        family: _MorCategoryOf,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        self._family = family
        self._end_family = None
        self._aut_family = None
        self._domain_object = domain
        self._codomain_object = codomain
        # As for ``CategoricalMor``, semantic packet supercategories are
        # not Python implementation mixins.  In particular ``Iso_C(A,B)``
        # simultaneously lies over ``Hom_C``, ``Mono_C`` and ``Epi_C``; asking
        # Sage to synthesize one C3 class from those fixed categories creates
        # artificial MRO cycles.  Keep the runtime method spine at the owned
        # root instead, which realizes the host ``Parent`` for the objects a
        # fixed Mor category builds through its own entry (the functors of
        # ``[A, B]``), while ``super_categories`` states the mathematics.
        self._super_categories_for_classes = [Objects()]
        super().__init__()

    def category(self) -> Category:
        r"""A fixed Mor category is placed in ``MorCategories``, below ``Cat``."""
        return MorCategories()

    def _make_named_class_key(self, name):
        return (self._family, id(self._domain_object), id(self._codomain_object))

    def mor_family(self) -> _MorCategoryOf:
        return self._family

    @property
    def _MorCategory(self) -> type[_MorCategoryOf]:
        return _DiscreteTwoMorCategoryOf

    def attach_end_family(self, family: _EndCategoryOf) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an endomorphism Mor category can carry an End-family role")
        owner = _category_packet(self.base_category()).Ends()
        if family is not owner:
            represented = _category_packet(family.base_category()).Mors().Of(
                self.domain_object(), self.codomain_object()
            )
            if represented is not self and represented.arrow_set() is not self:
                raise ValueError("the End family selects a different fixed Mor object")
        if self._end_family is not None and self._end_family is not owner:
            raise ValueError("one fixed Mor category cannot carry two End-family roles")
        self._end_family = owner
        owner._remember_between(self.domain_object(), self.codomain_object(), self)

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
        owner._remember_between(self.domain_object(), self.codomain_object(), self)

    def aut_family(self) -> _AutCategoryOf | None:
        return self._aut_family

    def identity_endomorphism(self) -> Morphism:
        if self.end_family() is None:
            raise ValueError("this fixed Mor category has not been given an End-family role")
        return self(self.arrow_set().identity())

    one = identity_endomorphism

    def base_category(self) -> Category:
        return self.mor_family().base_category()

    def domain_object(self) -> ObjectOfCategory:
        return self._domain_object

    def codomain_object(self) -> ObjectOfCategory:
        return self._codomain_object

    def arrow_set(self) -> SetObject:
        r"""The substrate of a Mor with no more specific declared constructor.

        Only an unreduced root family constructs this class.  Re-entering the
        public category Mor here would ask that same family to construct
        itself.  Restrictions instead inherit the actual Mor object below.
        """
        if _has_category_packet_surface(self.base_category()):
            return _underlying_set_mor(self.domain_object(), self.codomain_object())
        return SageHom(self.domain_object(), self.codomain_object(), self.base_category())

    underlying_mor = arrow_set

    def accepts(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` is an arrow of this Mor category.

        An arrow of the selected Mor object, or of the Mor of a subcategory with
        the same endpoints, is one.  Inherited arrows retain their stronger
        mathematical parent; the category graph supplies this inclusion,
        not an attempted conversion through a possibly undecidable constructor.
        """
        if arrow.domain() is not self.domain_object() or arrow.codomain() is not self.codomain_object():
            return False
        mor = self.arrow_set()
        return arrow.parent() is mor or _arrow_is_inherited_from_subcategory(self, arrow)

    def object(self, arrow: Parent | Morphism):
        r"""``arrow`` as an object placed in this fixed Mor and in ``Ar(C)``."""
        match arrow:
            case Morphism():
                return _fixed_mor_arrow_object(self, arrow)
            case _ if Category.__contains__(self, arrow):
                return arrow
            case _ if arrow in self.base_category().ArrowCategory():
                return self.object(arrow.arrow())
            case _:
                raise TypeError("a fixed Mor object is constructed from an arrow or an arrow object")

    __call__ = object

    def _mor_endpoint(self, obj: Parent | Category | Morphism):
        return self.object(obj)

    def __contains__(self, candidate: Any) -> bool:
        return Category.__contains__(self, candidate)

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
    ) -> CategoricalMor:
        return self.MorCategory().Of(domain, codomain)

    two_mor = Mor

    def identity_2(self, arrow: Parent | Morphism) -> Morphism:
        return self.Mor(arrow, arrow).identity()

    def identity(self, arrow_object: Parent | Morphism) -> Morphism:
        return self.Mor(arrow_object, arrow_object).identity()

    def super_categories(self):
        supers = []
        for supercategory in _packet_supercategories(self.base_category()):
            supers.append(
                self.mor_family().family_over(supercategory).Of(
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


class FixedEndCategory(FixedMorCategory):
    r"""The category ``End_C(A)`` of endomorphisms of one object."""

    def identity_endomorphism(self) -> Morphism:
        return self(self.arrow_set().identity())

    one = identity_endomorphism

    def _repr_(self) -> str:
        return f"End_{self.base_category()}({self.domain_object()})"


class FixedRestrictedMorCategory(FixedMorCategory):
    def arrow_set(self) -> SetObject:
        r"""Return the existing ``Mor`` parent for these endpoints.

        A restricted Mor category classifies some arrows in the base
        category's already-existing Mor object.  It therefore reuses the
        endpoint Mor owned by the base category packet.
        """
        return _category_packet(self.base_category()).Mors().Of(
            self.domain_object(), self.codomain_object()
        ).arrow_set()

    underlying_mor = arrow_set

    def accepts(self, arrow: Morphism) -> bool:
        return super().accepts(arrow) and self.mor_family().accepts(arrow)

    def super_categories(self):
        base = _category_packet(self.base_category()).Mors().Of(
            self.domain_object(), self.codomain_object()
        )
        inherited = [
            self.mor_family().family_over(supercategory).Of(
                self.domain_object(), self.codomain_object()
            )
            for supercategory in _packet_supercategories(self.base_category())
        ]
        return [base, *inherited]


class RestrictedMorCategoryParent(FixedRestrictedMorCategory):
    r"""A restricted Mor category that also carries independent enrichment.

    Its elements may be structured witnesses (for example derivations) whose
    actual categorical arrows live in :meth:`arrow_set`.  Unlike
    :class:`CategoricalMor`, this parent is therefore not itself a Mor
    and cannot become a second Mor for the same fixed endpoints.

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
        family: _RestrictedMorCategoryOf,
        domain: Parent,
        codomain: Parent,
        *,
        category: Category | None = None,
    ) -> None:
        FixedRestrictedMorCategory.__init__(self, family, domain, codomain)
        if category is None:
            from dzack_research.preamble.categories.sets.set_categories import Sets

            category = Sets()
        with construction_scope(self) as reached:
            SageCategoryObject._init_category_(self, category)
            realize_owned_category(self)
            run_construction_hooks(self, reached)

    def category(self) -> Category:
        r"""Return the independent enrichment carried by this parent.

        ``RestrictedMorCategoryParent`` has two roles: its restricted-Mor
        methods describe which arrows its elements represent, while as a Sage
        parent its elements may independently form a set, module, group, or
        another category selected by ``category=``.  The fixed-Mor base is an
        owned category object, whose inherited ``category()`` names its
        placement among Mor categories.  That answer would erase the
        enrichment recorded on the parent.  Read the latter here.
        """
        return Parent.category(self)

    def __call__(self, *args, **kwargs):
        r"""Construct an element through the independent Parent role.

        The fixed restricted-Mor category also has an explicit :meth:`object`
        operation for regarding an accepted underlying arrow as an object of
        the Mor category.  That categorical conversion must not replace this
        parent's ordinary element constructor: derivations, connections, and
        absolute-Galois automorphisms are structured elements specified by
        their own defining data.
        """
        return self._element_constructor_(*args, **kwargs)

    def __contains__(self, candidate: Any) -> bool:
        match candidate:
            case _ if parent(candidate) is self:
                return True
            case _:
                return Category.__contains__(self, candidate)


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
        # A represented isomorphism can be parented by an ordinary Mor object of
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
        core = self.parent().mor_category().Core()
        if other not in core.Mor(other.domain(), self.domain()):
            return self.forward() * other
        forward = self.forward() * other.forward()
        inverse = other.inverse() * self.inverse()
        return CategoricalIsomorphism(
            _category_mor_parent(self.parent().mor_category(), other.domain(), self.codomain()),
            forward,
            inverse,
            verify=False,
        )


class FixedIsoCategory(FixedRestrictedMorCategory):
    def accepts(self, arrow: Morphism) -> bool:
        r"""An arrow of ``Iso_C(A,B)`` is an isomorphism of ``C`` from ``A`` to ``B``.

        The core of ``C`` owns which arrows are represented isomorphisms, so
        its Mor decides.
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
            self.mor_family().family_over(supercategory).Of(domain, codomain)
            for supercategory in _packet_supercategories(self.base_category())
        ]
        supers = [
            packet.Mors().Of(domain, codomain),
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
            self.mor_family().family_over(supercategory).Of(obj)
            for supercategory in _packet_supercategories(self.base_category())
        ]
        return [
            packet.Ends().Of(obj),
            packet.Isos().Of(obj, obj),
            *inherited,
        ]

    def _repr_(self) -> str:
        return f"Aut_{self.base_category()}({self.domain_object()})"


class MorCategories(OwnedCategoryBase):
    r"""The category of represented fixed-endpoint Mor categories.

    Its objects are the categories ``Hom_C(A,B)``, each built by the ``Of``
    entry of the Mor family of its base category ``C``.
    """

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return [Cat()]

    def an_object(self) -> Category:
        r"""The Mor of the witness of the category of sets to itself."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        witness = Sets().an_object()
        return Sets().Mor(witness, witness)

    def __contains__(self, candidate: Any) -> bool:
        r"""Whether ``candidate`` is a fixed Mor category.

        A fixed Mor category built over the owned category base records this
        placement as its ``category()``.  A Mor realized on Sage's ``Mor``,
        or a restricted Mor with independently enriched elements, has one
        ``category()`` slot holding that enrichment (a set, a module).  Its
        placement here is therefore recorded where it was made:
        by the family whose ``Of`` entry built it for its endpoints. Read
        that recorded construction; containment must not call ``Of`` again
        and select or construct another Mor as a side effect.
        """
        match candidate:
            case CategoricalMor() | RestrictedMorCategoryParent():
                return (
                    candidate.mor_family()._cached_between(
                        candidate.domain_object(), candidate.codomain_object()
                    )
                    is candidate
                )
            case _:
                return super().__contains__(candidate)


FixedMorObject = CategoricalMor | FixedMorCategory
FixedMorClass = type[CategoricalMor] | type[FixedMorCategory]


class CategoryPacket:
    r"""The coordinated ``C / Hom_C / End_C / Iso_C / Aut_C`` families of one category.

    Not a mathematical object: the six families are the values of six
    operations of ``C`` (``MorCategory()``, ``EndCategory()``, ...), and this
    is the memo that holds them so that each is built once.  It is interned
    by the identity of ``C`` in :func:`_category_packet`.
    """

    def __init__(self, category: Category) -> None:
        self._category = category
        # Family objects are deliberately lazy.  The End family has the Mor
        # family as a semantic supercategory, which Sage requests during End
        # initialization.  Eager construction would re-enter a half-built packet.
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

    def Mors(self) -> _MorCategoryOf:
        if self._homs is None:
            self._homs = _declared_family(
                self.category(), "_MorCategory", _MorCategoryOf
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
        return finite_family(
            (
                _category_packet(category)
                for category in _packet_supercategories(self.category())
            ),
            name="Supercategory packets",
        )

    def __repr__(self) -> str:
        return f"Category packet of {self.category()}"


def _declared_construction(category, declaration_name):
    r"""Return the first packet-family declaration on the category MRO, if any.

    This reads the ``_MorCategory`` / ``_EndCategory`` / ... declarations a
    category class makes, the same way the owned root reads a category's
    ``ParentMethods`` declaration: off the declaring class graph, never off
    an instance.  This is the ``OWN-06`` runtime adapter for that declaration
    protocol: class/descriptor inspection here selects the implementation of
    a mathematical Mor construction already chosen by category placement; it
    does not infer mathematical structure from an owned object.
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

    Unverified specimen: a Mor's native value comparison must not identify
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
        sage: first.category_packet().Mors().base_category() is first
        True
        sage: second.category_packet().Mors().base_category() is second
        True
        sage: first.category_packet() is not second.category_packet()
        True
    """
    return CategoryPacket(category)


class _MorCategoryOf(OwnedCategoryBase):
    r"""The family ``(A,B) |-> Hom_C(A,B)`` attached to one category ``C``.

    An object here is the exact category selected by ``Of``, not an arbitrary
    subcategory of it.  Restricting its arrows or changing their base theory
    need not select that same category, so neither operation declares an
    inclusion of the classifying families.  A property category may still
    reuse an individual fixed Mor literally; its constructor records that
    shared object in both families.
    """

    FixedCategoryClass = FixedMorCategory
    _declaration_name = "_MorCategory"

    @staticmethod
    @cached_function(key=lambda cls, base_category: (cls, id(base_category)))
    def __classcall__(cls, base_category):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(base_category)
        # A category that declares its own Mor family has exactly one; naming
        # the generic family on it resolves to the declared one.
        declared = _declared_construction(base_category, cls._declaration_name)
        if declared is not None and not issubclass(cls, declared):
            return declared(base_category)
        # A fixed Mor is also a Mor whose native comparison may compare
        # its endpoints by value. The family is attached to the exact category,
        # not to another Mor with equal-but-distinct endpoint objects.
        return typecall(cls, base_category)

    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        # Several owned Mor-family specializations choose a concrete fixed
        # Mor parent class from the endpoints.  Keep that endpoint cache on
        # the common family object rather than relying on Sage category
        # internals for it.
        self._objects = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return id(self._base_category)

    def base_category(self) -> Category:
        return self._base_category

    def family_over(self, category: Category) -> _MorCategoryOf:
        return _category_packet(category).Mors()

    def fixed_category_class(self) -> FixedMorClass:
        return self.FixedCategoryClass

    def fixed_category_class_for(
        self,
        domain: Parent,
        codomain: Parent,
    ) -> FixedMorClass:
        r"""Return the represented fixed Mor class for these endpoints."""
        return self.fixed_category_class()

    def _inherits_morphisms_from(self, supercategory, domain, codomain) -> bool:
        r"""Whether this family may reuse ``supercategory``'s object literally.

        The Mor family itself has nothing further to ask: the class of what it
        would build against the class of what it inherits already decides it.
        A family that carves its objects out of a Mor overrides this, because
        the carving is only the same when the Mor is.
        """
        return True

    def _cached_between(self, domain, codomain):
        r"""Return the exact cached fixed-endpoint object, if present.

        Endpoint identity is part of the mathematical type.  Hashing/equality of
        endpoints is deliberately irrelevant here and can itself re-enter Mor
        construction, so every Mor-family specialization shares this one
        identity-sensitive lookup.
        """
        cached = self._objects.get((id(domain), id(codomain)))
        if cached is None:
            return None
        return cached if (
            cached.domain_object() is domain and cached.codomain_object() is codomain
        ) else None

    def _remember_between(self, domain, codomain, value):
        r"""Record this family's constructed fixed Mor, including literal reuse.

        All ``Of`` specializations finish here.  The canonical End/Aut role
        attachments use this same record when an inherited family constructs
        their shared object first.  Containment only reads the record; it
        neither populates it nor infers a different family from the endpoints.
        """
        self._objects[id(domain), id(codomain)] = value
        return value

    def an_object(self) -> Category:
        r"""The Mor of the base category's witness to itself."""
        witness = self.base_category().an_object()
        return self.Of(witness, witness)

    def super_categories(self):
        return [MorCategories()]

    def Of(self, domain: Parent, codomain: Parent) -> FixedMorObject:
        r"""Select the defining Mor object without losing inherited structure.

        This is the constructor entry for the objects of this family and the
        ``OWN-06`` private realization boundary, so the one place the runtime class a
        fixed Mor is realized by is compared:
        a property subcategory inherits the declaration of the category it
        refines and reuses the parent that category built.

        Unverified specimens: a property category shares its defining Mor;
        a restricted category shares the underlying Mor object, not its predicate::

            sage: from dzack_research.preamble.categories.sets.set_categories import Sets, FiniteSets
            sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
            sage: points = finite_ordered_set(("a", "b"))
            sage: Mor = FiniteSets().category_packet().Mors().Of(points, points)
            sage: Mor is Sets().Mor(points, points)
            True
            sage: end = FiniteSets().category_packet().Ends().Of(points)
            sage: end is Mor and end.end_family() is Sets().category_packet().Ends()
            True
            sage: monos = Sets().category_packet().Monos().Of(points, points)
            sage: epis = Sets().category_packet().Epis().Of(points, points)
            sage: monos.arrow_set() is Mor and epis.arrow_set() is Mor
            True
            sage: constant = Mor(lambda point: "a")
            sage: constant in Mor, constant in monos, constant in epis
            (True, False, False)
            sage: swap = Mor(lambda point: "b" if point == "a" else "a")
            sage: swap in monos and swap in epis
            True
            sage: aut = FiniteSets().category_packet().Auts().Of(points)
            sage: aut is Sets().category_packet().Isos().Of(points, points)
            True
            sage: aut.aut_family() is Sets().category_packet().Auts()
            True
            sage: identity = Mor.identity_2(swap)
            sage: identity * identity == identity
            True
        """
        if _has_category_packet_surface(self.base_category()):
            domain = self.base_category()._mor_endpoint(domain)
            codomain = self.base_category()._mor_endpoint(codomain)
        if domain not in self.base_category() or codomain not in self.base_category():
            raise TypeError("Mor endpoints must lie in the base category")
        # Endpoint identity, not a hash: hashing a Mor endpoint re-enters Mor
        # construction, so Sage's cached_method recurses here.  Endpoint
        # refinement may strengthen the represented fixed Mor, so a
        # cached parent is reusable only if it still has the selected class.
        fixed_class = self.fixed_category_class_for(domain, codomain)
        cached = self._cached_between(domain, codomain)
        # What decides whether this category needs a Mor parent of its own is
        # whether the Mor it would build differs from one it already inherits,
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
            # supercategory.  A Mor can only be inherited from a supercategory
            # when that supercategory actually admits both endpoints; otherwise
            # there is no fixed Mor object there to reuse.
            if domain not in supercategory or codomain not in supercategory:
                continue
            candidate = self.family_over(supercategory).Of(domain, codomain)
            if not (
                fixed_class is FixedMorCategory or isinstance(candidate, fixed_class)
            ):
                continue
            if all(candidate is not known for known in inherited):
                inherited.append(candidate)

        inherited = _minimal_inherited_homs(inherited)
        if len(inherited) == 1:
            # One inherited Mor of the class this category would have built:
            # the subcategory adds no morphisms, so reuse that object literally
            # rather than fabricating a second parent for the same maps.
            result = inherited[0]
        elif fixed_class is not FixedMorCategory:
            # This family states a Mor class of its own.  Nothing it inherits
            # is that class, or several inherited ones disagree; either way it
            # is not, for morphism purposes, a subcategory of any single one,
            # and it builds what it declared.
            result = (
                cached
                if isinstance(cached, fixed_class) and cached.mor_family() is self
                else fixed_class(self, domain, codomain)
            )
        elif inherited:
            raise TypeError(
                f"{self.base_category()} inherits incompatible Mor constructions; "
                "declare _MorCategory explicitly"
            )
        else:
            # No declared or inherited implementation remains.  The root
            # fixed category owns its private Mor object; the public Mor ingress
            # must not be called recursively while this object is constructed.
            result = (
                cached
                if isinstance(cached, fixed_class) and cached.mor_family() is self
                else fixed_class(self, domain, codomain)
            )
        return self._remember_between(domain, codomain, result)

    Between = Of

    def __contains__(self, candidate: Any) -> bool:
        r"""Read the fixed Mor selected at this family's construction entry.

        ``Of`` records both a newly constructed Mor and an inherited Mor that
        is reused literally.  Membership reads that same identity-sensitive
        record; it does not select a construction from the candidate's
        endpoints or implicitly pass to another base category.  An End or
        Aut attachment records its canonical owning family at attachment, so
        an inherited constructor need not be followed by an owner query.

        ``Cat.object(M)`` is the already-constructed Sage-Mor endpoint for
        the exact category ``M``.  At this representation boundary its stored
        category is the same object to look up, not new defining data to feed
        to ``Of``.  No arbitrary object with similar methods is unwrapped.
        """
        from dzack_research.preamble.categories.abstract_categories.cat import CategoryObject

        match candidate:
            case CategoryObject():
                candidate = candidate.represented_category()
        if candidate not in MorCategories():
            return False
        return self._cached_between(
            candidate.domain_object(), candidate.codomain_object()
        ) is candidate

    def _repr_(self) -> str:
        return f"Mor-category packet of {self.base_category()}"


class _DiscreteTwoMorCategoryOf(_MorCategoryOf):
    r"""The Mor family of a fixed Mor category with only identity 2-arrows.

    An object of the base is a represented arrow. Between identical arrow
    objects there is its identity; between distinct objects there is no arrow.
    The ordinary Mor-family cache owns both constructions.

    Unverified specimens: the explicit 2-Mor and the packet select one parent,
    and an ordinary identity functor can act on its actual identity arrow::

        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: from dzack_research.preamble.categories.functors.core import IdentityFunctor
        sage: points = finite_ordered_set(("a", "b"))
        sage: Mor = Sets().Mor(points, points)
        sage: swap = Mor(lambda point: {"a": "b", "b": "a"}[point])
        sage: obj = Mor.object(swap)
        sage: two_mor = Mor.two_mor(swap, swap)
        sage: two_mor is Mor.MorCategory().Of(obj, obj)
        True
        sage: two_mor is Mor.category_packet().Mors().Between(swap, swap)
        True
        sage: two_mor is _category_mor_parent(Mor, obj, obj)
        True
        sage: identity = two_mor.identity()
        sage: IdentityFunctor(Mor)(identity) is identity
        True
        sage: identity * identity == identity
        True
        sage: monos = Sets().Mono(points, points)
        sage: two_mor is monos.Mor(swap, swap)
        True
        sage: monos.two_mor(swap, swap) is monos.category_packet().Mors().Of(obj, obj)
        True
        sage: Mor.two_mor(swap, Mor.identity()).identity()
        Traceback (most recent call last):
        ...
        ValueError: distinct arrows have no represented 2-morphism

    Unverified specimen for a Mor that also has a module structure::

        sage: from dzack_research.preamble.all import Modules, QQ
        sage: module = QQ.free_module(1)
        sage: linear_mor = Modules(QQ).Mor(module, module)
        sage: identity = linear_mor.identity()
        sage: obj = linear_mor.object(identity)
        sage: two_mor = linear_mor.two_mor(identity, identity)
        sage: _category_mor_parent(linear_mor, obj, obj) is two_mor
        True
        sage: IdentityFunctor(linear_mor)(two_mor.identity()) is two_mor.identity()
        True
    """

    FixedCategoryClass = MorArrowDiscreteMor


def _carves_the_same_mor(self, supercategory, domain, codomain) -> bool:
    r"""Whether this category and ``supercategory`` have one and the same Mor.

    The monomorphisms, epimorphisms and isomorphisms of a category are cut out
    of its Mor, so a subcategory inherits them exactly when it inherits the
    Mor they are cut from.  A category of Lie algebras and the modules under
    it agree on which linear maps are bijections and disagree on which maps
    are morphisms at all, so its automorphisms are its own.
    """
    if _declared_construction(
        self.base_category(), self._declaration_name
    ) is not _declared_construction(supercategory, self._declaration_name):
        # A declared restriction may change even when the underlying Mor
        # does not.  Do not replace that predicate by an ancestor's predicate
        # merely because both use FixedRestrictedMorCategory to represent it.
        return False
    return (
        _category_packet(self.base_category()).Mors().Of(domain, codomain)
        is _category_packet(supercategory).Mors().Of(domain, codomain)
    )


class _EndCategoryOf(_MorCategoryOf):
    r"""The diagonal Mor family, with ``End_C(A) is Hom_C(A,A)``."""

    FixedCategoryClass = FixedEndCategory
    _declaration_name = "_EndCategory"

    def family_over(self, category: Category) -> _EndCategoryOf:
        return _category_packet(category).Ends()

    def super_categories(self):
        return [_category_packet(self.base_category()).Mors()]

    def an_object(self) -> Category:
        return self.Of(self.base_category().an_object())

    def Of(
        self,
        obj: Parent,
        codomain: Parent | None = None,
    ) -> FixedMorObject:
        if _has_category_packet_surface(self.base_category()):
            obj = self.base_category()._mor_endpoint(obj)
            if codomain is not None:
                codomain = self.base_category()._mor_endpoint(codomain)
        if codomain is not None and codomain is not obj:
            raise ValueError("an endomorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the endomorphism object must lie in the base category")
        endomorphisms = _category_packet(self.base_category()).Mors().Of(obj, obj)
        # A Mor shared with the category above is the same set of morphisms, so
        # its endomorphisms are the same too and the End object is that one.
        # Its defining category owns the role regardless of which inherited
        # family is queried first.
        if endomorphisms.end_family() is None:
            endomorphisms.attach_end_family(_category_packet(endomorphisms.base_category()).Ends())
        return self._remember_between(obj, obj, endomorphisms)

    def Between(self, domain: Parent, codomain: Parent) -> FixedMorObject:
        return self.Of(domain, codomain)

    def _repr_(self) -> str:
        return f"End-category packet of {self.base_category()}"


class _RestrictedMorCategoryOf(_MorCategoryOf):
    r"""A family of fixed-endpoint subcategories of an existing ``Mor``."""

    FixedCategoryClass = FixedRestrictedMorCategory

    _inherits_morphisms_from = _carves_the_same_mor

    @abstract_method
    def accepts(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` belongs to this restricted Mor family."""

    def _accepts_by_placement(self, arrow: Morphism) -> bool:
        r"""Whether a stronger represented Mor already places ``arrow`` here.

        A restriction with no theory-specific decision procedure cannot infer
        its predicate from methods exposed by an arbitrary arrow.  What it can
        know is construction: an arrow parent which is this fixed restricted
        Mor, or a declared subcategory of it, already carries the restriction.
        Concrete theories such as sets may override :meth:`accepts` with a
        theorem-backed decision procedure for their own morphisms.
        """
        if (
            arrow.domain() not in self.base_category()
            or arrow.codomain() not in self.base_category()
        ):
            return False
        selected = self.Of(arrow.domain(), arrow.codomain())
        arrow_parent = arrow.parent()
        return arrow_parent is selected or (
            arrow_parent in MorCategories()
            and _declared_category_reaches(arrow_parent, selected)
        )


_RestrictedCategoryOf = _RestrictedMorCategoryOf


class _MonoCategoryOf(_RestrictedMorCategoryOf):
    r"""Represented monomorphisms absent a stronger theory-specific decision.

    The generic family is placement-only.  It does not interpret an
    ``is_injective`` method as categorical monicity; categories such as sets
    that have a theorem identifying the two override :meth:`accepts` at their
    own declaration.
    """

    _declaration_name = "_MonoCategory"

    def family_over(self, category: Category) -> _MonoCategoryOf:
        return _category_packet(category).Monos()

    def accepts(self, arrow: Morphism) -> bool:
        return self._accepts_by_placement(arrow)


class _EpiCategoryOf(_RestrictedMorCategoryOf):
    r"""Represented epimorphisms absent a stronger theory-specific decision.

    An arbitrary ``is_surjective`` method is likewise not the definition of a
    categorical epimorphism.  Theory-specific declarations may supply their
    own exact admission rule.
    """

    _declaration_name = "_EpiCategory"

    def family_over(self, category: Category) -> _EpiCategoryOf:
        return _category_packet(category).Epis()

    def accepts(self, arrow: Morphism) -> bool:
        return self._accepts_by_placement(arrow)


class _IsoCategoryOf(_MorCategoryOf):
    FixedCategoryClass = FixedIsoCategory
    _declaration_name = "_IsoCategory"

    _inherits_morphisms_from = _carves_the_same_mor

    def family_over(self, category: Category) -> _IsoCategoryOf:
        return _category_packet(category).Isos()


class _AutCategoryOf(_IsoCategoryOf):
    r"""The diagonal Iso family, with ``Aut_C(A) is Iso_C(A,A)``."""

    FixedCategoryClass = FixedAutCategory
    _declaration_name = "_AutCategory"

    def family_over(self, category: Category) -> _AutCategoryOf:
        return _category_packet(category).Auts()

    def an_object(self) -> Category:
        return self.Of(self.base_category().an_object())

    def super_categories(self):
        return [_category_packet(self.base_category()).Isos()]

    def Of(
        self,
        obj: Parent,
        codomain: Parent | None = None,
    ) -> FixedMorObject:
        if _has_category_packet_surface(self.base_category()):
            obj = self.base_category()._mor_endpoint(obj)
            if codomain is not None:
                codomain = self.base_category()._mor_endpoint(codomain)
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

    def Between(self, domain: Parent, codomain: Parent) -> FixedMorObject:
        return self.Of(domain, codomain)

    def _repr_(self) -> str:
        return f"Aut-category packet of {self.base_category()}"


class MorCategoryConstruction(_MorCategoryOf):
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
    "CategoricalMor",
    "CategoricalIsomorphism",
    "EndCategoryConstruction",
    "EpiCategoryConstruction",
    "FixedAutCategory",
    "FixedEndCategory",
    "FixedMorCategory",
    "FixedIsoCategory",
    "MorArrowIdentity",
    "MorCategories",
    "MorCategoryConstruction",
    "IsoCategoryConstruction",
    "MonoCategoryConstruction",
    "RestrictedMorCategoryParent",
]
