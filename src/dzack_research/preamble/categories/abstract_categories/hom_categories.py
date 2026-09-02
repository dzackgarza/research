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
"""

from sage.categories.category import Category
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism
from sage.categories.objects import Objects
from sage.categories.sets_cat import Sets as SageSets
from dzack_research.preamble.categories.sets.owned_sets import Sets as _OwnedSets
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.structure.sage_object import SageObject
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    CategoricalIsomorphism,
)


def _category_homset(category, domain, codomain):
    r"""Return the one represented Hom-set parent for ``category`` and endpoints."""
    constructor = getattr(category, "homset", None)
    if constructor is not None:
        return constructor(domain, codomain)
    constructor = getattr(category, "hom", None)
    if constructor is not None:
        try:
            return constructor(domain, codomain)
        except (TypeError, ValueError):
            pass
    try:
        return Hom(domain, codomain, category)
    except (TypeError, ValueError):
        return Hom(domain, codomain, _OwnedSets())


class CategoryPacketMethods:
    r"""The coordinated ``C/Hom_C/End_C/Iso_C/Aut_C`` construction surface.

    This is deliberately a small live analogue of the archived ``Cat``
    construction kernel.  It belongs on owned category base classes, not on
    arbitrary Sage parents: the category chooses which Hom notion is meant,
    and its Hom/End/Aut families then mirror ``super_categories()``.
    """

    def HomCategory(self):
        return category_packet(self).Homs()

    def EndCategory(self):
        return category_packet(self).Ends()

    def MonoCategory(self):
        return category_packet(self).Monos()

    def EpiCategory(self):
        return category_packet(self).Epis()

    def IsoCategory(self):
        return category_packet(self).Isos()

    def AutCategory(self):
        return category_packet(self).Auts()

    def Hom(self, source, target):
        return self.HomCategory().Of(source, target)

    def End(self, obj):
        return self.EndCategory().Of(obj)

    def Mono(self, source, target):
        return self.MonoCategory().Of(source, target)

    def Epi(self, source, target):
        return self.EpiCategory().Of(source, target)

    def Iso(self, source, target):
        return self.IsoCategory().Of(source, target)

    def Aut(self, obj):
        return self.AutCategory().Of(obj)


def _packet_supercategories(category):
    r"""Return semantic supercategories participating in the owned packet graph.

    Sage categories in ``super_categories()`` are runtime substrates.  Their
    native Hom dispatch is endpoint-driven and can jump back into a stronger
    owned category, so transporting Hom/End/Aut packets through them creates
    cycles and, more importantly, the wrong semantic graph.
    """
    return tuple(
        supercategory
        for supercategory in category.super_categories()
        if isinstance(supercategory, CategoryPacketMethods)
    )


class HomArrowObject(Parent):
    r"""An arrow regarded as an object of a fixed-endpoint Hom category."""

    def __init__(self, arrow) -> None:
        self._arrow = arrow
        Parent.__init__(self, category=SageSets())

    def arrow(self):
        return self._arrow

    underlying_arrow = arrow

    def _repr_(self) -> str:
        return f"Arrow object ({self.arrow()})"


_ARROW_OBJECTS = {}


def _arrow_object(arrow) -> HomArrowObject:
    # Arrow identity, not a hash: an arbitrary arrow need not be hashable.
    key = id(arrow)
    cached = _ARROW_OBJECTS.get(key)
    if cached is not None and cached.arrow() is arrow:
        return cached
    result = HomArrowObject(arrow)
    _ARROW_OBJECTS[key] = result
    return result


class HomArrowIdentity(Morphism):
    r"""The identity 2-arrow on one arrow object."""

    def _call_(self, value):
        return value


class HomArrowDiscreteHomset(Homset):
    r"""The discrete 2-Hom between two arrow objects."""

    Element = HomArrowIdentity

    def __init__(self, hom_category, domain, codomain) -> None:
        self._hom_category = hom_category
        Homset.__init__(self, domain, codomain, category=SageSets())

    def hom_category(self):
        return self._hom_category

    def _element_constructor_(self, value=None):
        if self.domain() is not self.codomain():
            raise ValueError("distinct arrows have no represented 2-morphism")
        return self.element_class(self)

    def identity(self):
        return self()


class CategoricalHomset(Homset, Category):
    r"""A represented Hom object which is both a Sage Homset and a category.

    This is the live counterpart of the archived owned Hom-category base.  It
    keeps Sage's hard requirement that every ``Morphism`` be parented by an
    actual ``Homset``, while also making that same parent the discrete category
    ``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
    the *same object*.
    """

    @staticmethod
    def __classcall__(cls, family, domain, codomain, **options):
        # ``Category`` is a UniqueRepresentation whose default classcall does
        # not include fixed Hom endpoints in the identity of this mixed
        # Homset/category object.  The owning Hom family already interns by
        # ``(domain,codomain)``, so bypass Category's cache here.
        return typecall(cls, family, domain, codomain, **options)

    def __init__(self, family, domain, codomain, *, homset_category=None) -> None:
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
        self._super_categories_for_classes = [Objects()]
        Category.__init__(self)
        Homset.__init__(
            self,
            domain,
            codomain,
            category=SageSets() if homset_category is None else homset_category,
        )

    def hom_family(self):
        return self._family

    def attach_end_family(self, family) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an endomorphism Hom category can carry an End-family role")
        if self._end_family is not None and self._end_family is not family:
            raise ValueError("one fixed Hom category cannot carry two End-family roles")
        self._end_family = family

    def end_family(self):
        return self._end_family

    def attach_aut_family(self, family) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an equal-endpoint Iso category can carry an Aut-family role")
        if self._aut_family is not None and self._aut_family is not family:
            raise ValueError("one fixed Iso category cannot carry two Aut-family roles")
        self._aut_family = family

    def aut_family(self):
        return self._aut_family

    def identity_endomorphism(self):
        if self.end_family() is None:
            raise ValueError("this fixed Hom category has not been given an End-family role")
        identity = self.arrow_set().identity()
        return self(identity)

    one = identity_endomorphism

    def base_category(self):
        return self.hom_family().base_category()

    def domain_object(self):
        return self._domain_object

    def codomain_object(self):
        return self._codomain_object

    def arrow_set(self):
        return self

    underlying_homset = arrow_set

    def accepts(self, arrow) -> bool:
        if not (
            isinstance(arrow, Morphism)
            and arrow.domain() is self.domain_object()
            and arrow.codomain() is self.codomain_object()
        ):
            return False
        if arrow.parent() is self:
            return True
        try:
            self(arrow)
        except (TypeError, ValueError, NotImplementedError):
            return False
        return True

    def object(self, arrow):
        if not self.accepts(arrow):
            arrow = self(arrow)
        return _arrow_object(arrow)

    def super_categories(self):
        supers = []
        for supercategory in _packet_supercategories(self.base_category()):
            if (
                self.domain_object() in supercategory
                and self.codomain_object() in supercategory
            ):
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

    def two_hom(self, domain, codomain):
        if not isinstance(domain, HomArrowObject):
            domain = self.object(domain)
        if not isinstance(codomain, HomArrowObject):
            codomain = self.object(codomain)
        return HomArrowDiscreteHomset(self, domain, codomain)

    def identity_2(self, arrow):
        arrow_object = self.object(arrow)
        return self.two_hom(arrow_object, arrow_object).identity()


class FixedHomCategory(Category):
    r"""The category ``Hom_C(A,B)`` of arrows with fixed endpoints."""

    @staticmethod
    def __classcall__(cls, family, domain, codomain):
        # The owning Hom-family already interns fixed categories by their
        # endpoint identities.  Sage ``Category``'s UniqueRepresentation cache
        # does not include those endpoints and can otherwise collapse
        # ``Hom_C(A,B)`` with a previously created ``Hom_C(A',B')``.
        return typecall(cls, family, domain, codomain)

    def __init__(self, family, domain, codomain) -> None:
        self._family = family
        self._end_family = None
        self._aut_family = None
        self._domain_object = domain
        self._codomain_object = codomain
        # As for ``CategoricalHomset``, semantic packet supercategories are
        # not Python implementation mixins.  In particular ``Iso_C(A,B)``
        # simultaneously lies over ``Hom_C``, ``Mono_C`` and ``Epi_C``; asking
        # Sage to synthesize one C3 class from those fixed categories creates
        # artificial MRO cycles.  Keep the runtime method spine discrete while
        # exposing the full mathematical supertree through ``super_categories``.
        self._super_categories_for_classes = [Objects()]
        super().__init__()

    def _make_named_class_key(self, name):
        return (self._family, id(self._domain_object), id(self._codomain_object))

    def hom_family(self):
        return self._family

    def attach_end_family(self, family) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an endomorphism Hom category can carry an End-family role")
        if self._end_family is not None and self._end_family is not family:
            raise ValueError("one fixed Hom category cannot carry two End-family roles")
        self._end_family = family

    def end_family(self):
        return self._end_family

    def attach_aut_family(self, family) -> None:
        if self.domain_object() is not self.codomain_object():
            raise ValueError("only an equal-endpoint Iso category can carry an Aut-family role")
        if self._aut_family is not None and self._aut_family is not family:
            raise ValueError("one fixed Iso category cannot carry two Aut-family roles")
        self._aut_family = family

    def aut_family(self):
        return self._aut_family

    def identity_endomorphism(self):
        if self.end_family() is None:
            raise ValueError("this fixed Hom category has not been given an End-family role")
        return self(self.arrow_set().identity())

    one = identity_endomorphism

    def base_category(self):
        return self.hom_family().base_category()

    def domain_object(self):
        return self._domain_object

    def codomain_object(self):
        return self._codomain_object

    def arrow_set(self):
        return _category_homset(
            self.base_category(),
            self.domain_object(),
            self.codomain_object(),
        )

    underlying_homset = arrow_set

    def accepts(self, arrow) -> bool:
        if not (
            isinstance(arrow, Morphism)
            and arrow.domain() is self.domain_object()
            and arrow.codomain() is self.codomain_object()
        ):
            return False
        homset = self.arrow_set()
        if arrow.parent() is homset:
            return True
        # Structured subcategories may represent an arrow by a stronger
        # morphism class while retaining the same underlying categorical map.
        # The fixed Hom category therefore accepts a morphism exactly when the
        # canonical Hom parent can adopt/validate it.
        try:
            homset(arrow)
        except (TypeError, ValueError, NotImplementedError):
            return False
        return True

    def object(self, arrow):
        if isinstance(arrow, HomArrowObject):
            arrow = arrow.arrow()
        if not self.accepts(arrow):
            raise ValueError(f"{arrow} is not an arrow of {self}")
        return _arrow_object(arrow)

    __call__ = object

    def __contains__(self, candidate) -> bool:
        arrow = candidate.arrow() if isinstance(candidate, HomArrowObject) else candidate
        return self.accepts(arrow)

    def objects(self):
        arrows = self.arrow_set()
        if not hasattr(arrows, "__iter__"):
            raise TypeError("this Hom category has no chosen enumeration of its arrows")
        return tuple(self(arrow) for arrow in arrows)

    def hom(self, domain, codomain):
        if not isinstance(domain, HomArrowObject):
            domain = self(domain)
        if not isinstance(codomain, HomArrowObject):
            codomain = self(codomain)
        if domain not in self or codomain not in self:
            raise TypeError("a 2-Hom requires two arrow objects in this Hom category")
        return HomArrowDiscreteHomset(self, domain, codomain)

    Hom = hom

    def identity(self, arrow_object):
        return self.hom(arrow_object, arrow_object).identity()

    def super_categories(self):
        supers = []
        for supercategory in _packet_supercategories(self.base_category()):
            if (
                self.domain_object() in supercategory
                and self.codomain_object() in supercategory
            ):
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
            f"Hom_{self.base_category()}({self.domain_object()}, "
            f"{self.codomain_object()})"
        )


class FixedEndCategory(FixedHomCategory):
    r"""The category ``End_C(A)`` of endomorphisms of one object."""

    def identity_endomorphism(self):
        return self(self.arrow_set().identity())

    one = identity_endomorphism

    def _repr_(self) -> str:
        return f"End_{self.base_category()}({self.domain_object()})"


class FixedRestrictedHomCategory(FixedHomCategory):
    def accepts(self, arrow) -> bool:
        return super().accepts(arrow) and self.hom_family().accepts(arrow)

    def super_categories(self):
        base = category_packet(self.base_category()).Homs().Of(
            self.domain_object(), self.codomain_object()
        )
        inherited = [
            self.hom_family().family_over(supercategory).Of(
                self.domain_object(), self.codomain_object()
            )
            for supercategory in _packet_supercategories(self.base_category())
            if self.domain_object() in supercategory
            and self.codomain_object() in supercategory
        ]
        return [base, *inherited]


class FixedIsoCategory(FixedHomCategory):
    def accepts(self, arrow) -> bool:
        if not isinstance(arrow, CategoricalIsomorphism):
            return False
        if (
            arrow.domain() is not self.domain_object()
            or arrow.codomain() is not self.codomain_object()
        ):
            return False
        packet = category_packet(self.base_category())
        return (
            arrow.forward()
            in packet.Homs().Of(self.domain_object(), self.codomain_object())
            and arrow.inverse()
            in packet.Homs().Of(self.codomain_object(), self.domain_object())
        )

    def super_categories(self):
        packet = category_packet(self.base_category())
        domain = self.domain_object()
        codomain = self.codomain_object()
        inherited = [
            self.hom_family().family_over(supercategory).Of(domain, codomain)
            for supercategory in _packet_supercategories(self.base_category())
            if domain in supercategory and codomain in supercategory
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
                if domain in supercategory
            )
        return supers

    def identity_automorphism(self):
        if self.aut_family() is None:
            raise ValueError("this isomorphism category has not been given an Aut-family role")
        if self.domain_object() is not self.codomain_object():
            raise ValueError("an automorphism category has equal endpoints")
        identity = self.arrow_set().identity()
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            Isomorphism,
        )

        return self(Isomorphism(identity, identity))

    one = identity_automorphism

    def _repr_(self) -> str:
        if self.aut_family() is not None:
            return f"Aut_{self.base_category()}({self.domain_object()})"
        return (
            f"Iso_{self.base_category()}({self.domain_object()}, "
            f"{self.codomain_object()})"
        )


class FixedAutCategory(FixedIsoCategory):
    def identity_automorphism(self):
        identity = self.arrow_set().identity()
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            Isomorphism,
        )

        return self(Isomorphism(identity, identity))

    one = identity_automorphism

    def super_categories(self):
        packet = category_packet(self.base_category())
        obj = self.domain_object()
        inherited = [
            self.hom_family().family_over(supercategory).Of(obj)
            for supercategory in _packet_supercategories(self.base_category())
            if obj in supercategory
        ]
        return [
            packet.Ends().Of(obj),
            packet.Isos().Of(obj, obj),
            *inherited,
        ]

    def _repr_(self) -> str:
        return f"Aut_{self.base_category()}({self.domain_object()})"


class HomCategories(Category):
    r"""The category of represented fixed-endpoint Hom categories."""

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return isinstance(candidate, (FixedHomCategory, CategoricalHomset))


class CategoryPacket(SageObject):
    r"""The coordinated ``C / Hom_C / End_C / Iso_C / Aut_C`` packet."""

    def __init__(self, category) -> None:
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

    def category(self):
        return self._category

    C = category

    def Homs(self):
        if self._homs is None:
            self._homs = _declared_family(
                self.category(), "_HomCategory", HomCategoryOf
            )
        return self._homs

    def Ends(self):
        if self._ends is None:
            self._ends = _declared_family(
                self.category(), "_EndCategory", EndCategoryOf
            )
        return self._ends

    def Monos(self):
        if self._monos is None:
            self._monos = _declared_family(
                self.category(), "_MonoCategory", MonoCategoryOf
            )
        return self._monos

    def Epis(self):
        if self._epis is None:
            self._epis = _declared_family(
                self.category(), "_EpiCategory", EpiCategoryOf
            )
        return self._epis

    def Isos(self):
        if self._isos is None:
            self._isos = _declared_family(
                self.category(), "_IsoCategory", IsoCategoryOf
            )
        return self._isos

    def Auts(self):
        if self._auts is None:
            self._auts = _declared_family(
                self.category(), "_AutCategory", AutCategoryOf
            )
        return self._auts

    def super_packets(self):
        return tuple(
            category_packet(category)
            for category in _packet_supercategories(self.category())
        )

    def _repr_(self) -> str:
        return f"Category packet of {self.category()}"


def _declared_construction(category, declaration_name):
    r"""Return the first packet-family declaration on the category MRO, if any."""
    declaring = type(category)
    if declaring.__name__.endswith("_with_category"):
        declaring = declaring.__base__
    for ancestor in declaring.__mro__:
        construction = ancestor.__dict__.get(declaration_name)
        if isinstance(construction, type):
            return construction
    return None


def _declared_family(category, declaration_name, default):
    r"""Construct the packet family ``category`` declares, else ``default``."""
    construction = _declared_construction(category, declaration_name)
    return (default if construction is None else construction)(category)


@cached_function
def category_packet(category) -> CategoryPacket:
    return CategoryPacket(category)


class HomCategoryOf(Category):
    r"""The family ``(A,B) |-> Hom_C(A,B)`` attached to one category ``C``."""

    FixedCategoryClass = FixedHomCategory
    _declaration_name = "_HomCategory"

    @staticmethod
    def __classcall__(cls, base_category):
        # A category that declares its own Hom family has exactly one; naming
        # the generic family on it resolves to the declared one.
        declared = _declared_construction(base_category, cls._declaration_name)
        if declared is not None and not issubclass(cls, declared):
            return declared(base_category)
        return super(HomCategoryOf, cls).__classcall__(cls, base_category)

    def __init__(self, base_category) -> None:
        self._base_category = base_category
        # Several owned Hom-family specializations choose a concrete fixed
        # Hom parent class from the endpoints.  Keep that endpoint cache on
        # the common family object rather than relying on Sage category
        # internals for it.
        self._objects = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self):
        return self._base_category

    def family_over(self, category):
        return category_packet(category).Homs()

    def fixed_category_class(self):
        return self.FixedCategoryClass

    def super_categories(self):
        supers = [
            self.family_over(category)
            for category in _packet_supercategories(self.base_category())
        ]
        return supers + [HomCategories()]

    def Of(self, domain, codomain):
        if domain not in self.base_category() or codomain not in self.base_category():
            raise TypeError("Hom endpoints must lie in the base category")
        # Endpoint identity, not a hash: hashing a Hom endpoint re-enters Hom
        # construction, so Sage's cached_method recurses here.
        key = id(domain), id(codomain)
        cached = self._objects.get(key)
        if (
            cached is not None
            and cached.domain_object() is domain
            and cached.codomain_object() is codomain
        ):
            return cached
        fixed_class = self.fixed_category_class()
        if self.FixedCategoryClass is FixedHomCategory and fixed_class is FixedHomCategory:
            inherited = []
            for supercategory in _packet_supercategories(self.base_category()):
                if domain not in supercategory or codomain not in supercategory:
                    continue
                candidate = self.family_over(supercategory).Of(domain, codomain)
                if all(candidate is not known for known in inherited):
                    inherited.append(candidate)

            if len(inherited) == 1:
                # No new Hom declaration means this is a full/property
                # subcategory for morphism purposes.  Reuse the inherited Hom
                # object literally rather than fabricating a second carrier.
                result = inherited[0]
            elif len(inherited) > 1:
                raise TypeError(
                    f"{self.base_category()} inherits incompatible Hom constructions; "
                    "declare _HomCategory explicitly"
                )
            else:
                represented = _category_homset(self.base_category(), domain, codomain)
                if isinstance(represented, Category):
                    result = represented
                else:
                    result = fixed_class(self, domain, codomain)
        else:
            result = fixed_class(self, domain, codomain)
        self._objects[key] = result
        return result

    Between = Of

    def __contains__(self, candidate) -> bool:
        try:
            domain = candidate.domain_object()
            codomain = candidate.codomain_object()
        except AttributeError:
            return False
        if domain not in self.base_category() or codomain not in self.base_category():
            return False
        return self.Of(domain, codomain) is candidate

    def _repr_(self) -> str:
        return f"Hom-category packet of {self.base_category()}"


class EndCategoryOf(HomCategoryOf):
    r"""The family ``A |-> End_C(A)``."""

    FixedCategoryClass = FixedEndCategory
    _declaration_name = "_EndCategory"

    def family_over(self, category):
        return category_packet(category).Ends()

    def Of(self, obj, codomain=None):
        if codomain is not None and codomain is not obj:
            raise ValueError("an endomorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the endomorphism object must lie in the base category")
        key = id(obj), id(obj)
        cached = self._objects.get(key)
        if cached is not None:
            return cached
        endomorphisms = category_packet(self.base_category()).Homs().Of(obj, obj)
        attach = getattr(endomorphisms, "attach_end_family", None)
        if attach is not None:
            attach(self)
        self._objects[key] = endomorphisms
        return endomorphisms

    def Between(self, domain, codomain):
        if domain is not codomain:
            raise ValueError("an endomorphism category has equal endpoints")
        return self.Of(domain)

    def _repr_(self) -> str:
        return f"End-category packet of {self.base_category()}"


class _RestrictedCategoryOf(HomCategoryOf):
    FixedCategoryClass = FixedRestrictedHomCategory

    def accepts(self, arrow) -> bool:
        raise NotImplementedError

    def super_categories(self):
        inherited = [
            self.family_over(category)
            for category in _packet_supercategories(self.base_category())
        ]
        return [category_packet(self.base_category()).Homs(), *inherited, HomCategories()]


class MonoCategoryOf(_RestrictedCategoryOf):
    _declaration_name = "_MonoCategory"

    def family_over(self, category):
        return category_packet(category).Monos()

    def accepts(self, arrow) -> bool:
        try:
            return arrow.is_injective() is True
        except (AttributeError, NotImplementedError):
            return False


class EpiCategoryOf(_RestrictedCategoryOf):
    _declaration_name = "_EpiCategory"

    def family_over(self, category):
        return category_packet(category).Epis()

    def accepts(self, arrow) -> bool:
        try:
            return arrow.is_surjective() is True
        except (AttributeError, NotImplementedError):
            return False


class IsoCategoryOf(HomCategoryOf):
    FixedCategoryClass = FixedIsoCategory
    _declaration_name = "_IsoCategory"

    def family_over(self, category):
        return category_packet(category).Isos()

    def super_categories(self):
        packet = category_packet(self.base_category())
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


class AutCategoryOf(IsoCategoryOf):
    r"""The family ``A |-> Aut_C(A)``."""

    FixedCategoryClass = FixedAutCategory
    _declaration_name = "_AutCategory"

    def family_over(self, category):
        return category_packet(category).Auts()

    def super_categories(self):
        packet = category_packet(self.base_category())
        inherited = [
            self.family_over(category)
            for category in _packet_supercategories(self.base_category())
        ]
        return [packet.Ends(), packet.Isos(), *inherited, HomCategories()]

    def Of(self, obj, codomain=None):
        if codomain is not None and codomain is not obj:
            raise ValueError("an automorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the automorphism object must lie in the base category")
        key = id(obj), id(obj)
        cached = self._objects.get(key)
        if cached is not None:
            return cached
        automorphisms = category_packet(self.base_category()).Isos().Of(obj, obj)
        attach = getattr(automorphisms, "attach_aut_family", None)
        if attach is None:
            raise TypeError("the represented equal-endpoint Iso object cannot carry an Aut-family role")
        attach(self)
        self._objects[key] = automorphisms
        return automorphisms

    def Between(self, domain, codomain):
        if domain is not codomain:
            raise ValueError("an automorphism category has equal endpoints")
        return self.Of(domain)

    def _repr_(self) -> str:
        return f"Aut-category packet of {self.base_category()}"


class HomCategoryConstruction(HomCategoryOf):
    pass


class EndCategoryConstruction(EndCategoryOf):
    pass


class MonoCategoryConstruction(MonoCategoryOf):
    pass


class EpiCategoryConstruction(EpiCategoryOf):
    pass


class IsoCategoryConstruction(IsoCategoryOf):
    pass


class AutCategoryConstruction(AutCategoryOf):
    pass


__all__ = [
    "AutCategoryConstruction",
    "AutCategoryOf",
    "CategoryPacket",
    "CategoryPacketMethods",
    "CategoricalHomset",
    "EndCategoryConstruction",
    "EndCategoryOf",
    "EpiCategoryConstruction",
    "EpiCategoryOf",
    "FixedAutCategory",
    "FixedEndCategory",
    "FixedHomCategory",
    "FixedIsoCategory",
    "HomArrowObject",
    "HomCategories",
    "HomCategoryConstruction",
    "HomCategoryOf",
    "IsoCategoryConstruction",
    "IsoCategoryOf",
    "MonoCategoryConstruction",
    "MonoCategoryOf",
    "category_packet",
]
