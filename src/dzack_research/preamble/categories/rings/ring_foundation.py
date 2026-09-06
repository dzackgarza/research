"""Owned scalar hierarchy and the boundary to Sage computation rings."""

from functools import wraps

from sage.all import (
    GF as _SageGF,
)
from sage.all import (
    ComplexField as _SageComplexField,
)
from sage.all import (
    Qp as _SageQp,
)
from sage.all import (
    RealField as _SageRealField,
)
from sage.all import (
    Zmod as _SageZmod,
)
from sage.categories.category import Category
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.fields import Fields as SageFields
from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as SagePrincipalIdealDomains
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.rings.ring import Ring
from sage.structure.element import CommutativeRingElement, RingElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE, richcmp
from sage.structure.sage_object import SageObject
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    AdditiveMonoids,
    Monoids,
    Semigroups,
)
from dzack_research.preamble.categories.sets.cardinals import (
    aleph0,
    cardinal,
    continuum,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import (
    CountablyInfiniteSets,
    FiniteSets,
    Sets,
    UncountableSets,
)
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import realize_owned_category, refine


class RingMorphism(Morphism):
    r"""A unital ring morphism in the owned ring category."""

    def __init__(self, parent, function, *, engine_morphism=None) -> None:
        Morphism.__init__(self, parent)
        if not callable(function):
            raise TypeError("a ring morphism requires an exact element map")
        self._function = function
        self._engine_morphism = engine_morphism
        self._preamble_is_identity = False

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        return self.codomain()(self._function(self.domain()(element)))

    def _engine_morphism_crossing(self):
        r"""Return the private engine realization when one was selected."""
        if self._engine_morphism is None:
            raise NotImplementedError("this ring morphism has no selected engine realization")
        return self._engine_morphism

    def __mul__(self, other):
        if not isinstance(other, RingMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        if self.is_identity():
            return other
        if other.is_identity():
            return self
        return ring_homset(other.domain(), self.codomain()).elementwise(
            lambda element: self(other(element)),
        )

    def compose(self, before):
        result = self * before
        if result is NotImplemented:
            raise ValueError("the ring morphisms are not composable")
        return result

    def is_identity(self) -> bool:
        if self.domain() is not self.codomain():
            return False
        if self._preamble_is_identity:
            return True
        return self._engine_is_identity()

    def _engine_is_identity(self) -> bool:
        r"""Ask only the selected private engine realization about identity."""
        if self._engine_morphism is None:
            return False
        try:
            return bool(self._engine_morphism.is_identity())
        except AttributeError, NotImplementedError, TypeError, ValueError:
            return False

    def kernel(self):
        r"""Return the represented kernel ideal of this ring morphism."""
        provider = self.__dict__.get("_preamble_kernel_ideal_provider")
        if provider is not None:
            represented = provider._represented_annihilator_ideal()
            if represented is not NotImplemented:
                return represented
        raise NotImplementedError("the kernel ideal of this ring morphism has no represented backend")


class RingHomset(CategoricalHomset):
    r"""The owned set ``Hom_Ring(A,B)``."""

    Element = RingMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def __call__(self, datum):
        return self._element_constructor_(datum)

    def is_endomorphism_set(self):
        return self.domain() is self.codomain()

    def _element_constructor_(self, datum):
        if isinstance(datum, RingMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the ring morphism has the wrong source or target")
            if datum.parent() is self:
                return datum
            return self.elementwise(datum)
        if isinstance(datum, Map):
            source_engine = _engine_ring(self.domain())
            target_engine = _engine_ring(self.codomain())
            if _engine_ring(datum.domain()) is not source_engine:
                raise ValueError("the engine ring map has the wrong domain")
            if _engine_ring(datum.codomain()) is not target_engine:
                raise ValueError("the engine ring map has the wrong codomain")
            return self.element_class(
                self,
                lambda element: target_engine(datum(source_engine(element))),
                engine_morphism=datum,
            )
        if callable(datum):
            return self.elementwise(datum)
        raise TypeError("a ring morphism is supplied by an exact map or engine morphism")

    def elementwise(self, function):
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on a ring endomorphism Hom-set")
        identity = self.elementwise(lambda element: element)
        identity._preamble_is_identity = True
        return identity

    def _repr_(self):
        return f"Mor_Ring({self.domain()}, {self.codomain()})"


class RingHomCategoryConstruction(HomCategoryConstruction):
    r"""The owned family ``(A,B) |-> Hom_Ring(A,B)``."""

    def fixed_category_class(self):
        return RingHomset


def ring_homset(domain, codomain) -> RingHomset:
    r"""Return the canonical owned ``Mor_Ring(domain, codomain)`` object."""
    return OwnedRings().Mor(domain, codomain)


def _ring_mor_category(domain, codomain) -> RingHomset:
    r"""Build ``Mor_Ring(domain, codomain)`` from its owned family.

    `OwnedRings.Mor` is the public route and delegates here.  It must not call
    `ring_homset`, which is that same public route under another name: while
    the category method and the module function had different names the cycle
    was invisible, and naming both `Mor` made it a self-call.
    """
    return RingHomCategoryConstruction(OwnedRings()).Of(domain, codomain)


def ring_morphism(domain, codomain, function, *, engine_morphism=None) -> RingMorphism:
    r"""Construct one owned ring morphism with an optional engine realization."""
    return RingMorphism(
        ring_homset(domain, codomain),
        function,
        engine_morphism=engine_morphism,
    )


class PredicateSubrings(OwnedCategory):
    def an_object(self):
        r"""The integers inside the rationals, cut out by integrality."""
        rationals = _own_ring(SageQQ)
        return predicate_subring(
            rationals,
            lambda element: element.denominator() == 1,
            "z is an integer",
        )

    def super_categories(self):
        return [OwnedRings()]

    class ParentMethods:
        def ambient_ring(self):
            return self._ambient_ring

        def defining_predicate(self):
            return self._predicate

        def __contains__(self, element):
            if element not in self._ambient_ring:
                return False
            answer = self._predicate(element)
            if answer is True or answer is False:
                return answer
            raise NotImplementedError(f"membership in {self} is not decided for {element}")

        def _element_constructor_(self, element):
            try:
                candidate = self._ambient_ring(element)
            except TypeError, ValueError:
                raise ValueError(f"{element} is not in the ambient ring {self._ambient_ring}") from None
            if candidate not in self:
                raise ValueError(f"{candidate} does not satisfy {self._description}")
            return candidate

        def one(self):
            return self._one

        def zero(self):
            return self._zero

        def inclusion(self):
            return ring_morphism(
                self,
                self._ambient_ring,
                lambda element: element,
            )

        def _repr_(self):
            return f"{{z in {self._ambient_ring} : {self._description}}}"


class LocalizationRings(OwnedCategory):
    r"""Commutative localizations carrying their selected source and submonoid."""

    class ElementMethods(CommutativeRingElement):
        r"""A represented fraction ``a/s`` in ``S^{-1}R``."""

        def __init__(self, parent, numerator, denominator) -> None:
            self._numerator = parent.localization_source()(numerator)
            self._denominator = parent.localization_source()(denominator)
            super().__init__(parent)

        def numerator(self):
            return self._numerator

        def denominator(self):
            return self._denominator

        def _add_(self, other):
            return self.parent().fraction(
                self.numerator() * other.denominator() + other.numerator() * self.denominator(),
                self.denominator() * other.denominator(),
                _trusted_denominator=True,
            )

        def _mul_(self, other):
            return self.parent().fraction(
                self.numerator() * other.numerator(),
                self.denominator() * other.denominator(),
                _trusted_denominator=True,
            )

        def __mul__(self, other):
            if other.parent() is self.parent():
                if other.parent() is not self.parent():
                    return NotImplemented
                return self._mul_(other)
            other_parent = getattr(other, "parent", lambda: None)()
            if other_parent is not None:
                try:
                    if other_parent.base_ring() is self.parent():
                        return other_parent.scalar_multiple(self, other)
                except AttributeError, TypeError, ValueError:
                    pass
            return NotImplemented

        def inverse_of_unit(self):
            parent = self.parent()
            engine = parent._selected_engine_ring()
            source = parent.localization_source()
            represented = engine(_engine_element(source, self.numerator())) / engine(_engine_element(source, self.denominator()))
            if not represented.is_unit():
                raise ZeroDivisionError(f"{self} is not a unit")
            inverse = represented**-1
            source_engine = _engine_ring(source)
            return parent.fraction(
                source._from_engine_element(source_engine(inverse.numerator())),
                source._from_engine_element(source_engine(inverse.denominator())),
                _trusted_denominator=True,
            )

        def is_unit(self):
            engine = self.parent()._selected_engine_ring()
            source = self.parent().localization_source()
            represented = engine(_engine_element(source, self.numerator())) / engine(_engine_element(source, self.denominator()))
            return bool(represented.is_unit())

        def __truediv__(self, other):
            other = self.parent()(other)
            return self * other.inverse_of_unit()

        def _neg_(self):
            return self.parent().fraction(
                -self.numerator(),
                self.denominator(),
                _trusted_denominator=True,
            )

        def equality_status(self, other):
            if other.parent() is not self.parent() or other.parent() is not self.parent():
                return False
            return self.parent()._fraction_equality_status(self, other)

        def _richcmp_(self, other, op):
            from sage.misc.unknown import Unknown

            if op not in (op_EQ, op_NE):
                return NotImplemented
            status = self.equality_status(other)
            if status is Unknown:
                raise NotImplementedError("equality of these localization fractions is not decidable from the represented data")
            return bool(status) if op == op_EQ else not bool(status)

        def _repr_(self):
            if self.denominator() == self.parent().localization_source().one():
                return repr(self.numerator())
            return f"({self.numerator()})/({self.denominator()})"

    def super_categories(self):
        return [OwnedRings().Commutative()]

    class ParentMethods:
        def __init__(
            self,
            source,
            submonoid,
            _engine_ring=None,
            *,
            algebra_source=None,
            **rest,
        ) -> None:
            self._preamble_localization_source = source
            self._preamble_localization_submonoid = submonoid
            self._preamble_engine_ring = _engine_ring
            if algebra_source is not None:
                self._preamble_algebra_base_ring = algebra_source.base_ring()
            super().__init__(base_ring=source.base_ring(), **rest)

            self._preamble_localization_map = ring_morphism(
                source,
                self,
                lambda element: self.fraction(element),
            )
            if algebra_source is not None:
                self._preamble_structure_map = self._preamble_localization_map * algebra_source.algebra_structure_morphism()

        def _selected_engine_ring(self):
            r"""Return the private realization that computes in this localization.

            Protected contract: the element arithmetic of this category asks its
            parent for the realization that decides invertibility.
            """
            engine = self._preamble_engine_ring
            if engine is None:
                raise NotImplementedError("this localization has no selected computation realization")
            return engine

        def localize_module(self, module):
            r"""Return ``S^{-1}M`` through the module-localization theory."""

            if module.base_ring() is not self.localization_source():
                raise ValueError("the module has the wrong source ring for this localization")
            from dzack_research.preamble.categories.functors.module_localization import (
                module_localization_functor,
            )

            return module_localization_functor(self)(module)

        def _valid_denominator(self, denominator) -> bool:
            try:
                return denominator in self.localization_submonoid()
            except NotImplementedError:
                return False

        def fraction(self, numerator, denominator=None, *, _trusted_denominator=False):
            source = self.localization_source()
            numerator = source(numerator)
            denominator = source.one() if denominator is None else source(denominator)
            if not _trusted_denominator and not self._valid_denominator(denominator):
                raise ValueError(f"{denominator} is not represented in the localization submonoid")
            return self.element_class(self, numerator, denominator)

        def _element_constructor_(self, value):
            if isinstance(value, self.category().ElementType) and value.parent() is self:
                return value
            if isinstance(value, tuple) and len(value) == 2:
                return self.fraction(value[0], value[1])
            if self._preamble_engine_ring is not None:
                try:
                    value_parent = getattr(value, "parent", lambda: None)()
                    engine_value = _engine_element(value_parent, value) if value_parent in OwnedRings() else value
                    represented = self._preamble_engine_ring(engine_value)
                    structure = self.localization_submonoid().structure_data()
                    trusted_denominator = structure.get("kind") != "prime_complement"
                    source = self.localization_source()
                    source_engine = _engine_ring(source)
                    return self.fraction(
                        source._from_engine_element(source_engine(represented.numerator())),
                        source._from_engine_element(source_engine(represented.denominator())),
                        _trusted_denominator=trusted_denominator,
                    )
                except AttributeError, TypeError, ValueError:
                    pass
            return self.fraction(value)

        def __call__(self, value):
            return self._element_constructor_(value)

        def __contains__(self, value) -> bool:
            if isinstance(value, self.category().ElementType) and value.parent() is self:
                return True
            try:
                self(value)
            except NotImplementedError, TypeError, ValueError:
                return False
            return True

        def _from_engine_element(self, value):
            engine = self._preamble_engine_ring
            if engine is None:
                raise NotImplementedError("this localization has no selected computation realization")
            represented = engine(value)
            source = self.localization_source()
            return self.fraction(
                source._from_engine_element(_engine_ring(source)(represented.numerator())),
                source._from_engine_element(_engine_ring(source)(represented.denominator())),
                _trusted_denominator=True,
            )

        def _engine_element(self, value):
            engine = self._preamble_engine_ring
            if engine is None:
                raise NotImplementedError("this localization has no selected computation realization")
            element = self(value)
            numerator = _engine_element(self.localization_source(), element.numerator())
            denominator = _engine_element(self.localization_source(), element.denominator())
            return engine(numerator) / engine(denominator)

        def zero(self):
            return self.fraction(self.localization_source().zero())

        def one(self):
            return self.fraction(self.localization_source().one())

        def _fraction_equality_status(self, left, right):
            from sage.misc.unknown import Unknown

            source = self.localization_source()
            left_product = left.numerator() * right.denominator()
            right_product = right.numerator() * left.denominator()
            # Use the owned additive operations rather than Python subtraction.
            # In particular, represented quotient classes implement addition and
            # negation directly, while Sage's inherited binary-subtraction
            # dispatch need not recognize their common owned parent.
            difference = source(left_product + (-right_product))
            if difference == source.zero():
                return True

            if source in OwnedIntegralDomains():
                return False

            structure = self.localization_submonoid().structure_data()
            if structure.get("kind") == "prime_complement":
                prime = structure.get("prime_ideal")
                if prime is None:
                    return Unknown
                try:
                    annihilator = source.ideal(source.zero()).colon(source.ideal(difference))
                    return any(not prime.contains_ambient_element(generator) for generator in annihilator.ideal_generators())
                except AttributeError, NotImplementedError, TypeError, ValueError:
                    pass

            from dzack_research.preamble.categories.rings.commutative_algebra import (
                QuotientRings,
            )

            if source in QuotientRings():
                try:
                    source_ring = source.quotient_source()
                    representative = source_ring(difference.lift())
                    lifted_generators = tuple(source_ring(generator.lift()) for generator in self.localization_submonoid().monoid_generators())
                    if lifted_generators:
                        product = source_ring.one()
                        for generator in lifted_generators:
                            product *= generator
                        saturated = source.defining_ideal().saturation(source_ring.ideal(product))
                        return saturated.contains_ambient_element(representative)
                except AttributeError, NotImplementedError, TypeError, ValueError:
                    pass

            # A selected exact coefficient presentation A = P/I contains the
            # same data needed for localization equality as an explicit
            # QuotientRing object.  For a finitely generated multiplicative set
            # S = <f_1,...,f_r>, a class d vanishes in S^{-1}A exactly when its
            # lift to P belongs to I : (f_1 ... f_r)^∞.  Indeed, a monomial in
            # the f_i kills d iff a sufficiently large common power of their
            # product kills d, and conversely every such common power lies in S.
            try:
                has_presentation = source._has_selected_exact_coefficient_presentation()
            except AttributeError, NotImplementedError, TypeError, ValueError:
                has_presentation = False
            if has_presentation:
                try:
                    presentation_ring = source._exact_coefficient_presentation_ring()
                    representative = presentation_ring(source._lift_coefficient_to_presentation(difference))
                    lifted_generators = tuple(
                        presentation_ring(source._lift_coefficient_to_presentation(generator)) for generator in self.localization_submonoid().monoid_generators()
                    )
                    if not lifted_generators:
                        return False
                    product = presentation_ring.one()
                    for generator in lifted_generators:
                        product *= generator
                    relations = tuple(presentation_ring(relation) for relation in source._exact_coefficient_presentation_relations())
                    defining_ideal = presentation_ring.ideal(*(relations or (presentation_ring.zero(),)))
                    saturated = defining_ideal.saturation(presentation_ring.ideal(product))
                    return saturated.contains_ambient_element(representative)
                except AttributeError, NotImplementedError, TypeError, ValueError:
                    pass

            try:
                engine = _engine_ring(source)
                if bool(engine.is_finite()):
                    generators = tuple(self.localization_submonoid().monoid_generators())
                    pending = [difference]
                    seen = []
                    while pending:
                        current = pending.pop()
                        if current == source.zero():
                            return True
                        if any(current == old for old in seen):
                            continue
                        seen.append(current)
                        pending.extend(source(generator * current) for generator in generators)
                    return False
            except AttributeError, NotImplementedError, TypeError, ValueError:
                pass
            return Unknown

        def _repr_(self):
            return f"Localization of {self.localization_source()} at {self.localization_submonoid()}"

        def localization_source(self):
            return self._preamble_localization_source

        def localization_submonoid(self):
            return self._preamble_localization_submonoid

        def inverted_elements(self):
            try:
                return self.localization_submonoid().monoid_generators()
            except NotImplementedError as error:
                raise NotImplementedError("this localization submonoid has no chosen finite generating set") from error

        def localization_map(self):
            return self._preamble_localization_map

        def localization_fraction_data(self, element):
            r"""Return one represented fraction ``(r,s)`` for ``element=r/s``."""
            value = self(element)
            source = self.localization_source()
            return source(value.numerator()), source(value.denominator())


class _PredicateSubringParent(Parent):
    def __init__(self, ambient_ring, predicate, description, category):
        if ambient_ring not in SageRings() and ambient_ring not in OwnedRings():
            raise TypeError(f"{ambient_ring} is not a ring")
        self._ambient_ring = ambient_ring
        self._predicate = predicate
        self._description = description
        commutative_rings = OwnedRings().Commutative()
        self._preamble_is_commutative = category.is_subcategory(commutative_rings) or ambient_ring.is_commutative() is True
        self._one = ambient_ring.one()
        self._zero = ambient_ring.zero()
        Parent.__init__(self, facade=ambient_ring, category=category)
        realize_owned_category(self)

    def is_commutative(self):
        if self._preamble_is_commutative:
            return True
        from sage.misc.unknown import Unknown

        return Unknown

    def __call__(self, element):
        r"""Construct an element of the predicate subring directly."""
        return self._element_constructor_(element)

    def _element_constructor_(self, element):
        try:
            candidate = self._ambient_ring(element)
        except TypeError, ValueError:
            raise ValueError(f"{element} is not in the ambient ring {self._ambient_ring}") from None
        if candidate not in self:
            raise ValueError(f"{candidate} does not satisfy {self._description}")
        return candidate

    def _from_engine_element(self, element):
        r"""Cross one ambient-engine element into this predicate subring."""
        converter = getattr(self._ambient_ring, "_from_engine_element", None)
        candidate = converter(element) if converter is not None else self._ambient_ring(element)
        return self(candidate)

    def __contains__(self, element):
        try:
            candidate = self._ambient_ring(element)
        except TypeError, ValueError:
            return False
        answer = self._predicate(candidate)
        if answer is True or answer is False:
            return answer
        raise NotImplementedError(f"membership in {self} is not decided for {candidate}")


def predicate_subring(ambient_ring, predicate, description, category=None):
    placement = PredicateSubrings()
    if category is not None:
        placement = Category.join((placement, category))
    return _PredicateSubringParent(
        ambient_ring,
        predicate,
        description,
        placement,
    )


class OwnedSemirings(OwnedCategory):
    """Semirings on the owned operation spine."""

    def an_object(self):
        r"""The integers, which are in particular a semiring."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [Monoids(), AdditiveMonoids()]


class OwnedRngs(OwnedCategory):
    """Rngs on the owned operation spine."""

    def an_object(self):
        r"""The integers, which happen to be unital."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [Semigroups(), AdditiveGroups()]


class OwnedRings(CategoryPacketMethods, OwnedCategory):
    """Unital rings whose notebook-facing ring interface is owned here."""

    _HomCategory = RingHomCategoryConstruction

    def an_object(self):
        r"""The integers, the initial object of this category."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [OwnedSemirings(), OwnedRngs()]

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a ring morphism object requires two owned rings")
        return _ring_mor_category(domain, codomain)

    class Commutative(CategoryWithAxiom):
        r"""Commutative unital rings in the owned mathematical graph."""

        @classmethod
        def _repr_object_names(cls):
            return "commutative rings"

        def an_object(self):
            r"""The integers."""
            return _own_ring(SageZZ)

        class ParentMethods:
            def is_commutative(self):
                return True

            def as_algebra_over(self, base_ring):
                from dzack_research.preamble.categories.algebras.algebras import refine_algebra

                base = _own_ring(base_ring)
                engine = _engine_ring(self)
                if not engine.has_coerce_map_from(_engine_ring(base)):
                    raise ValueError(f"{self} has no represented canonical algebra structure over {base}")
                return refine_algebra(self, base)

            def as_ZZ_algebra(self):
                return self.as_algebra_over(_own_ring(SageZZ))

            def ideal(self, *generators):
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    LocalizedMaximalIdeal,
                    PrimeLocalizations,
                )
                from dzack_research.preamble.categories.rings.commutative_ideals import (
                    CommutativeIdeal,
                )

                if self in PrimeLocalizations():
                    normalized = tuple(self(generator) for generator in generators)
                    source = self.localization_source()
                    fraction_engine = _engine_ring(self.fraction_field())
                    numerators = tuple(
                        source._from_engine_element(_engine_ring(source)(fraction_engine(_engine_element(self, generator)).numerator())) for generator in normalized
                    )
                    source_ideal = source.ideal(*numerators)
                    return LocalizedMaximalIdeal(self, normalized, source_ideal=source_ideal)
                return CommutativeIdeal(self, *generators)

            def quotient_ring(self, ideal):
                from dzack_research.preamble.categories.rings.commutative_algebra import QuotientRing

                return QuotientRing(self, ideal)

            def localization(self, *elements):
                from dzack_research.preamble.categories.rings.commutative_algebra import Localization

                return Localization(self, *elements)

            def localize_at_prime(self, prime):
                from dzack_research.preamble.categories.rings.commutative_algebra import PrimeLocalization

                return PrimeLocalization(self, prime)

            def adic_completion(self, ideal, precision=20):
                from dzack_research.preamble.categories.rings.commutative_algebra import AdicCompletion

                return AdicCompletion(self, ideal, precision=precision)

            @cached_method
            def spectrum(self):
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    PrimeSpectra,
                )
                from dzack_research.preamble.owned_category import object_of

                return object_of(PrimeSpectra(), ring=self)

    class ParentMethods:
        def __init_extra__(self) -> None:
            r"""Place this ring as an algebra: over ``ZZ`` always, over itself when commutative.

            Every ring is a ``ZZ``-algebra through the unique morphism from the
            initial ring, and a commutative ring is a commutative algebra over
            itself, its centre being all of it.  Sage calls this hook from
            ``Parent.__init__`` for every parent of this category, whatever
            route constructed it, so the placement is decided here once and
            no owned ring escapes it; commutativity is asked of the ring here
            and nowhere else.
            """
            from dzack_research.preamble.categories.algebras.algebras import (
                Algebras,
                CommutativeAlgebras,
            )

            # The integers are being constructed when this runs for them, so
            # asking the adapter for them again would construct them again.
            integers = self if _engine_ring(self) is SageZZ else _own_ring(SageZZ)
            placements = [Algebras(integers)]
            if self.is_commutative() is True:
                placements.extend((OwnedRings().Commutative(), CommutativeAlgebras(self)))
            refine(self, placements)

        def _fresh_free_module_on(self, labels):
            r"""Return the selected free module on ``labels`` over this ring."""
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FreshFreeModuleOn,
            )

            return FreshFreeModuleOn(self, labels)

        def __pow__(self, exponent):
            r"""Return the free module ``R^n`` through the owned module constructor."""
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FreeModule,
            )

            return FreeModule(self, exponent)

        def __getitem__(self, names):
            r"""Use standard polynomial/algebraic adjunction syntax on an owned ring."""
            from dzack_research.preamble.categories.algebras.free_algebras import (
                PolynomialRing,
            )
            from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebra
            from dzack_research.preamble.categories.group.groups import OwnedGroups
            from dzack_research.preamble.categories.rings.number_fields import (
                _refine_number_field_view,
                _refine_order_view,
            )

            match names:
                case str():
                    return PolynomialRing(self, names)
                case _ if names in OwnedGroups():
                    return GroupAlgebra(self, names)
                case tuple() if all(isinstance(part, str) for part in names):
                    return PolynomialRing(self, names)
                case list():
                    result = _own_if_ring(_engine_ring(self)[names])
                case _ if names in self:
                    return self
                case _:
                    result = _own_if_ring(_engine_ring(self)[names])

            if result not in OwnedRings():
                return result
            engine = _engine_ring(result)
            if isinstance(engine, SageNumberFieldOrder):
                return _refine_order_view(result)
            if engine in SageNumberFields():
                return _refine_number_field_view(result)
            return result

        def Mor(self, codomain, category=None):
            rings = OwnedRings()
            if category is None or (isinstance(category, OwnedCategory) and category.is_subcategory(rings)):
                return rings.Mor(self, codomain)
            # A Sage category here is not a mathematical request: it is Sage's
            # coercion machinery asking for somewhere to keep a conversion map,
            # naming its own `SetsWithPartialMaps`.  `SageHom` would check that
            # this owned ring lies in that Sage category, which it does not and
            # need not (`ARC-00`).  Build the homset directly at the engine
            # boundary instead, without the membership check.
            from sage.categories.homset import Homset

            return Homset(self, codomain, category=category, check=False)

        def _Hom_(self, codomain, category=None):
            rings = OwnedRings()
            if codomain not in rings:
                raise TypeError("a ring Hom requires two owned rings")
            if category is not None and not category.is_subcategory(rings):
                raise TypeError("this is not a ring homset category")
            return ring_homset(self, codomain)

        def cardinality(self):
            r"""Return the exact represented cardinal of the underlying set."""

            category = self.category()
            if category.is_subcategory(FiniteSets()):
                from sage.rings.integer_ring import ZZ as SageZZ

                integers = _own_ring(SageZZ)
                return cardinal(integers._from_engine_element(SageZZ(_engine_ring(self).cardinality())))
            if category.is_subcategory(CountablyInfiniteSets()):
                return aleph0
            if category.is_subcategory(UncountableSets()):
                return continuum
            assert False, f"cardinality is defined for every ring, but the current exact computation does not cover the represented ring {self}"

        def _has_selected_exact_coefficient_presentation(self) -> bool:
            r"""Return whether this ring carries a nontrivial selected exact presentation.

            Module algorithms use this capability without knowing which higher
            mathematical structure supplied the presentation.
            """
            return False

        def _exact_coefficient_presentation_ring(self):
            r"""Return the owned ring in which coefficient computations are lifted."""
            return self

        def _exact_coefficient_presentation_relations(self):
            r"""Return the selected coefficient relations in the computation ring."""

            return finite_ordered_set(())

        def _lift_coefficient_to_presentation(self, value):
            return self(value)

        def _descend_coefficient_from_presentation(self, value):
            return self(value)

        def is_central(self, element):
            r"""Return whether ``element`` is central in the foundational ring regimes."""
            if element not in self:
                return False
            if self in OwnedRings().Commutative():
                return True
            raise NotImplementedError(f"{self} has no ring-theoretic centrality decision without selected higher structure")

        @cached_method
        def _ring_morphism_defining_algebra_structure(self):
            r"""Return the canonical ring map \(R\to Z(R)\) when it is the identity."""
            if self not in OwnedRings().Commutative():
                raise TypeError(f"{self} is noncommutative, so the identity does not land in its center")
            center = self.ring_center()
            return ring_morphism(self, center, lambda scalar: scalar)

        def algebra_structure_morphism(self):
            r"""The structure morphism of this ring as an algebra over itself.

            For a commutative ring this is the identity \(R\to R\).
            """
            return self._ring_morphism_defining_algebra_structure()

        @cached_method
        def ring_center(self):
            r"""Return the centre ``Z(R)`` as a predicate-defined subring."""
            if self in OwnedRings().Commutative():
                return self
            return predicate_subring(
                self,
                self.is_central,
                "z commutes with every element",
                OwnedRings().Commutative(),
            )

        def fraction_field(self):
            r"""Return the fraction field through the computation ring."""
            if self in OwnedFields():
                return self
            return _own_ring(_engine_ring(self).fraction_field())


class OwnedOrderedRings(OwnedCategory):
    r"""Totally ordered rings in the owned scalar hierarchy."""

    def an_object(self):
        r"""The integers with their usual order."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [OwnedRings()]

    class ElementMethods:
        def __abs__(self):
            zero = self.parent().zero()
            return self if self >= zero else -self


class OwnedIntegralDomains(OwnedCategory):
    r"""Commutative rings without zero divisors."""

    def an_object(self):
        r"""The integers."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [OwnedRings().Commutative()]

    class ParentMethods:
        def is_integral_domain(self, *args, **kwargs):
            return True

        @cached_method
        def fraction_field_map(self):
            r"""Return the localization map ``R -> Frac(R)``.

            This is the localization of ``R`` at its nonzero elements, so it is
            injective exactly because ``R`` is a domain.  Scalar extension along
            it is the generic fibre: a module dies under it exactly on its
            torsion, and an ideal extends along it to the unit ideal exactly
            when it is nonzero.
            """
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                _canonical_map,
            )

            field = self.fraction_field()
            if field is self:
                return ring_homset(self, self).identity()
            return _canonical_map(self, field)


class OwnedPrincipalIdealDomains(OwnedCategory):
    r"""Principal ideal domains in the owned ring hierarchy."""

    def an_object(self):
        r"""The integers."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [OwnedIntegralDomains(), OwnedNoetherianRings()]


def _engine_krull_dimension(ring):
    engine = _engine_ring(ring)
    method = getattr(engine, "krull_dimension", None)
    if method is not None:
        try:
            return method()
        except NotImplementedError:
            pass
    try:
        return engine.defining_ideal().dimension()
    except (AttributeError, NotImplementedError, TypeError, ValueError) as error:
        raise NotImplementedError(f"Krull dimension of {ring} has no active backend") from error


class OwnedNoetherianRings(OwnedCategory):
    r"""Noetherian commutative rings."""

    def an_object(self):
        r"""The integers."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [OwnedRings().Commutative()]

    class ParentMethods:
        def is_noetherian(self):
            return True

        def krull_dimension(self):
            return _engine_krull_dimension(self)


class OwnedArtinianRings(OwnedCategory):
    r"""Artinian commutative rings."""

    def an_object(self):
        r"""The field of two elements: a field is artinian."""
        return GF(2)

    def super_categories(self):
        return [OwnedNoetherianRings()]

    class ParentMethods:
        def is_artinian(self):
            return True


class OwnedLocalRings(OwnedCategory):
    r"""Commutative rings equipped with their unique maximal ideal."""

    def an_object(self):
        r"""The integers localized at the prime (2)."""
        from dzack_research.preamble.categories.rings.commutative_algebra import PrimeLocalization

        return PrimeLocalization(_own_ring(SageZZ), 2)

    def super_categories(self):
        return [OwnedRings().Commutative()]

    class ParentMethods:
        def is_local(self):
            return True

        def maximal_ideal(self):
            return self._preamble_maximal_ideal

        def residue_field(self):
            return self._preamble_residue_field

        def residue_map(self):
            r"""Return the represented local quotient map ``R -> kappa(m)``."""
            morphism = self.__dict__.get("_preamble_residue_map")
            if morphism is not None:
                return morphism
            if self.residue_field() is self:
                return ring_homset(self, self).identity()
            raise NotImplementedError(f"the residue map of {self} is not represented")

        def fraction_field(self):
            represented = self.__dict__.get("_preamble_fraction_field")
            if represented is not None:
                return represented
            return super().fraction_field()


class OwnedAdicallyCompleteRings(OwnedCategory):
    r"""Commutative rings represented as complete for a chosen adic topology."""

    def an_object(self):
        r"""The 2-adic integers: complete, and local because (2) is maximal."""
        from dzack_research.preamble.categories.rings.commutative_algebra import AdicCompletion

        return AdicCompletion(_own_ring(SageZZ), 2)

    def super_categories(self):
        return [OwnedRings().Commutative()]

    class ParentMethods:
        def is_adically_complete(self):
            return True

        def ideal_of_definition(self):
            return self._preamble_ideal_of_definition


class OwnedCompleteLocalRings(OwnedCategory):
    r"""Local rings complete for the represented maximal-ideal/adic topology."""

    def an_object(self):
        r"""The 2-adic integers: complete, and local because (2) is maximal."""
        from dzack_research.preamble.categories.rings.commutative_algebra import AdicCompletion

        return AdicCompletion(_own_ring(SageZZ), 2)

    def super_categories(self):
        return [OwnedLocalRings(), OwnedAdicallyCompleteRings()]


class OwnedDivisionRings(OwnedCategory):
    def an_object(self):
        r"""The field of two elements."""
        return GF(2)

    def super_categories(self):
        return [OwnedRings()]


class OwnedFields(OwnedCategory):
    def an_object(self):
        r"""The field of two elements."""
        return GF(2)

    def super_categories(self):
        return [
            OwnedDivisionRings(),
            OwnedIntegralDomains(),
            OwnedPrincipalIdealDomains(),
            OwnedNoetherianRings(),
            OwnedArtinianRings(),
            OwnedLocalRings(),
        ]

    class ParentMethods:
        def maximal_ideal(self):
            r"""Return the zero ideal, the unique maximal ideal of a field."""
            return self.ideal(self.zero())

        def residue_field(self):
            return self

        def residue_map(self):
            return ring_homset(self, self).identity()


class OwnedOrders(OwnedCategory):
    r"""Orders in number fields as a ring-theoretic property category."""

    _certifying_predicate = "_preamble_is_number_field_order"

    def an_object(self):
        r"""The integers, the ring of integers of the rationals."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [
            OwnedIntegralDomains(),
            OwnedNoetherianRings(),
        ]

    class ParentMethods:
        def cardinality(self):

            return aleph0

        def is_maximal(self) -> bool:
            r"""Return whether this is the maximal order of its fraction field."""
            engine = _engine_ring(self)
            if engine is SageZZ:
                return True
            return bool(engine.is_maximal())


class PrimeFields(OwnedCategory):
    r"""Prime fields \(\mathbf F_p\)."""

    def an_object(self):
        r"""The field of two elements."""
        return GF(2)

    def super_categories(self):
        return [OwnedFields()]


class OwnedCategoryOverBaseRing(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""A category over a ring, normalized to the session's owned ring."""

    @staticmethod
    def __classcall__(cls, base_ring, *args, **kwargs):
        # During construction of an engine-backed owned ring, ``self`` already
        # exists and already carries its engine, but ``Parent.__init__`` has not
        # yet installed its category.  A self-referential placement such as
        # ``CommutativeAlgebras(R)`` must therefore accept that constructing
        # parent directly rather than asking category membership of an object
        # whose category is precisely what is being built.
        if not isinstance(base_ring, _OwnedRingParent):
            base_ring = _owned_ring(base_ring)
        return OwnedParameterizedCategory.__classcall__(
            cls,
            base_ring,
            *args,
            **kwargs,
        )

    def base_ring(self):
        return self.base()

    def __contains__(self, candidate) -> bool:
        try:
            return self in candidate.category().all_super_categories(proper=False)
        except AttributeError, TypeError, ValueError:
            return False


def _cross_engine_ring_value(value):
    r"""Cross a private engine-ring value back into the owned universe when possible."""
    parent = getattr(value, "parent", lambda: None)()
    if parent in SageRings():
        return _own_ring(parent)._from_engine_element(value)
    return value


def _proper_restriction_base_ring(ring):
    r"""Return the next proper scalar base in the represented ring tower.

    A represented ring keeps its distinguished construction base through
    ``base_ring()``.  When that base is the ring itself, the canonical map
    from the initial ring still makes every module or algebra over it a module
    or algebra over ``ZZ``.  The integers are the terminal case and therefore
    have no proper restriction base.

    The engine test is essential while ``ZZ`` itself is being constructed:
    asking ``_own_ring(SageZZ)`` again before its cache entry exists would
    recursively start a second construction of the same parent.
    """
    base = ring.base_ring()
    if base is None:
        return None if _engine_ring(ring) is SageZZ else _own_ring(SageZZ)
    if base is not ring:
        return _owned_ring(base)
    if _engine_ring(ring) is SageZZ:
        return None
    return _own_ring(SageZZ)


def _engine_multiplicative_generator(engine):
    r"""Return the selected engine's multiplicative generator at the private boundary."""
    generator = getattr(engine, "multiplicative_generator", None)
    if generator is None:
        raise AttributeError(f"{engine} has no represented multiplicative generator")
    return generator()


class _OwnedRingElement(RingElement):
    r"""An element of an owned ring with a private backend realization."""

    def __init__(self, parent, backend_value) -> None:
        RingElement.__init__(self, parent)
        self._backend_value = backend_value

    def _backend(self):
        r"""Return the private backend value for boundary code in this module."""
        return self._backend_value

    def _add_(self, other):
        parent = self.parent()
        return parent._from_engine_element(self._backend() + other._backend())

    def __add__(self, other):
        try:
            other = self.parent()(other)
        except TypeError, ValueError:
            return NotImplemented
        return self._add_(other)

    __radd__ = __add__

    def __sub__(self, other):
        try:
            other = self.parent()(other)
        except TypeError, ValueError:
            return NotImplemented
        return self._add_(-other)

    def __rsub__(self, other):
        try:
            other = self.parent()(other)
        except TypeError, ValueError:
            return NotImplemented
        return other._add_(-self)

    def _mul_(self, other):
        parent = self.parent()
        return parent._from_engine_element(self._backend() * other._backend())

    def __mul__(self, other):
        other_parent = getattr(other, "parent", lambda: None)()
        if other_parent is not None and other_parent is not self.parent():
            try:
                if other_parent.base_ring() is self.parent():
                    return other_parent.scalar_multiple(self, other)
            except AttributeError, TypeError, ValueError:
                return NotImplemented
        try:
            other = self.parent()(other)
        except TypeError, ValueError:
            return NotImplemented
        return self._mul_(other)

    def __rmul__(self, other):
        try:
            other = self.parent()(other)
        except TypeError, ValueError:
            return NotImplemented
        return self._mul_(other)

    def _neg_(self):
        return self.parent()._from_engine_element(-self._backend())

    def _richcmp_(self, other, op):
        if not isinstance(other, _OwnedRingElement) or other.parent() is not self.parent():
            try:
                other = self.parent()(other)
            except TypeError, ValueError:
                return NotImplemented
        return richcmp(self._backend(), other._backend(), op)

    def __eq__(self, other):
        try:
            other = self.parent()(other)
        except TypeError, ValueError:
            # Not this ring's decision: a cardinal, say, knows whether it
            # equals a natural number of the ring, so Python asks it next.
            return NotImplemented
        return bool(self._backend() == other._backend())

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((id(self.parent()), self._backend()))

    def __bool__(self):
        return bool(self._backend())

    def __int__(self):
        return int(self._backend())

    def __index__(self):
        return int(self._backend())

    def __float__(self):
        return float(self._backend())

    def __complex__(self):
        return complex(self._backend())

    def _repr_(self):
        return repr(self._backend())

    def _latex_(self):
        return str(latex(self._backend()))

    def is_zero(self):
        return bool(self._backend() == self.parent()._engine.zero())

    def is_one(self):
        return bool(self._backend() == self.parent()._engine.one())

    def is_unit(self):
        return bool(self._backend().is_unit())

    def inverse_of_unit(self):
        if not self.is_unit():
            raise ZeroDivisionError(f"{self} is not a unit")
        return self.parent()._from_engine_element(self._backend() ** -1)

    def __invert__(self):
        return self.parent()._from_engine_element(~self._backend())

    def __truediv__(self, other):
        other = self.parent()(other)
        value = self._backend() / other._backend()
        value_parent = getattr(value, "parent", lambda: None)()
        if value_parent is self.parent()._engine:
            return self.parent()._from_engine_element(value)
        if value_parent in SageRings():
            return _own_ring(value_parent)._from_engine_element(value)
        return value

    def __pow__(self, exponent, modulus=None):
        if modulus is not None:
            try:
                modulus = self.parent()(modulus)
            except TypeError, ValueError:
                return NotImplemented
            value = pow(self._backend(), exponent, modulus._backend())
        else:
            try:
                exponent = exponent.__index__()
            except AttributeError:
                return NotImplemented
            value = self._backend() ** exponent
        value_parent = getattr(value, "parent", lambda: None)()
        if value_parent is self.parent()._engine:
            return self.parent()._from_engine_element(value)
        if value_parent in SageRings():
            return _own_ring(value_parent)._from_engine_element(value)
        return value

    def __rtruediv__(self, other):
        try:
            numerator = self.parent()(other)
        except TypeError, ValueError:
            return NotImplemented
        return numerator.__truediv__(self)

    def __floordiv__(self, other):
        other = self.parent()(other)
        return self.parent()._from_engine_element(self._backend() // other._backend())

    def __mod__(self, other):
        other = self.parent()(other)
        return self.parent()._from_engine_element(self._backend() % other._backend())

    def quo_rem(self, other):
        other = self.parent()(other)
        quotient, remainder = self._backend().quo_rem(other._backend())
        return (
            self.parent()._from_engine_element(quotient),
            self.parent()._from_engine_element(remainder),
        )

    def divides(self, other):
        other = self.parent()(other)
        return bool(self._backend().divides(other._backend()))

    def gcd(self, other):
        other = self.parent()(other)
        return self.parent()._from_engine_element(self._backend().gcd(other._backend()))

    def lcm(self, other):
        other = self.parent()(other)
        return self.parent()._from_engine_element(self._backend().lcm(other._backend()))

    def valuation(self, prime):
        prime = self.parent()(prime)
        integers = _own_ring(SageZZ)
        return integers._from_engine_element(SageZZ(self._backend().valuation(prime._backend())))

    def prime_divisors(self):
        return tuple(self.parent()._from_engine_element(prime) for prime in self._backend().prime_divisors())

    def is_prime(self):
        return bool(self._backend().is_prime())

    def factorial(self):
        return self.parent()._from_engine_element(self._backend().factorial())

    def is_square(self):
        return bool(self._backend().is_square())

    def sqrt(self):
        return _cross_engine_ring_value(self._backend().sqrt())

    def numerator(self):
        value = self._backend().numerator()
        parent = value.parent()
        return _own_ring(parent)._from_engine_element(value)

    def denominator(self):
        value = self._backend().denominator()
        parent = value.parent()
        return _own_ring(parent)._from_engine_element(value)

    def additive_order(self):
        value = self._backend().additive_order()
        return _own_ring(SageZZ)._from_engine_element(SageZZ(value))

    def multiplicative_order(self):
        value = self._backend().multiplicative_order()
        return _own_ring(SageZZ)._from_engine_element(SageZZ(value))

    def degree(self):
        value = self._backend().degree()
        return _own_ring(SageZZ)._from_engine_element(SageZZ(value))

    def trace(self):
        return _cross_engine_ring_value(self._backend().trace())

    def norm(self):
        return _cross_engine_ring_value(self._backend().norm())

    def minpoly(self):
        polynomial = self._backend().minpoly()
        return _own_ring(polynomial.parent())._from_engine_element(polynomial)


class _OwnedRingParent(UniqueRepresentation, Parent):
    r"""An owned ring parent with one private computational realization.

    The parent and its elements belong to the preamble universe.  ``engine``
    is implementation state only; raw backend elements enter through
    ``_from_engine_element`` and leave through ``_engine_element``.
    """

    _preamble_owned_ring_parent = True

    Element = _OwnedRingElement

    def __init__(self, engine: Ring, *, category=None) -> None:
        self._engine = engine
        placement = _owned_ring_category(engine)
        if category is not None:
            placement = Category.join((placement, category))
        Parent.__init__(self, category=placement)
        realize_owned_category(self)

    def _from_engine_element(self, value):
        if getattr(value, "parent", lambda: None)() is not self._engine:
            value = self._engine(value)
        return self.element_class(self, value)

    def _engine_element(self, value):
        value = self(value)
        return value._backend()

    def __call__(self, value):
        r"""Construct an owned ring element without Sage coercion discovery."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        parent = getattr(value, "parent", lambda: None)()
        if parent is self:
            return value
        if parent is not None:
            try:
                if parent in OwnedRings():
                    return self._from_engine_element(self._engine(_engine_element(parent, value)))
            except TypeError, ValueError, AttributeError:
                pass
            if parent in SageRings() or parent is self._engine:
                raise TypeError("raw backend ring elements are not accepted by the public preamble API")
        if isinstance(value, SageObject):
            raise TypeError("raw backend objects are not accepted by the public preamble API")
        return self._from_engine_element(self._engine(value))

    def __contains__(self, value) -> bool:
        return isinstance(value, self.element_class) and value.parent() is self

    def zero(self):
        return self._from_engine_element(self._engine.zero())

    def one(self):
        return self._from_engine_element(self._engine.one())

    def multiplicative_generator(self):
        return self._from_engine_element(_engine_multiplicative_generator(self._engine))

    def an_element(self):
        return self._from_engine_element(self._engine.an_element())

    def characteristic(self):
        integers = _own_ring(SageZZ)
        return integers._from_engine_element(SageZZ(self._engine.characteristic()))

    def is_exact(self):
        return self._engine.is_exact()

    def is_field(self, *args, **kwargs):
        return self._engine.is_field(*args, **kwargs)

    def is_commutative(self):
        return self._engine.is_commutative()

    def is_integral_domain(self, *args, **kwargs):
        return self._engine.is_integral_domain(*args, **kwargs)

    def is_finite(self):
        return self._engine.is_finite()

    def _preamble_is_number_field_order(self):
        return self._engine is SageZZ or isinstance(self._engine, SageNumberFieldOrder)

    def is_projective(self) -> bool:
        r"""Projectivity as a module over the base ring.

        A ring is free of rank one over itself, and a number-field order is
        free of finite rank over the integers (its integral basis).
        """
        if self.base_ring() is self or self._preamble_is_number_field_order():
            return True
        raise AssertionError(f"projectivity of {self} over {self.base_ring()} is not decided here")

    def _preamble_is_number_field(self):
        return self._engine in SageNumberFields()

    def _preamble_has_chosen_primitive_element(self):
        return self._engine in SageNumberFields() and self._engine is not SageQQ

    def base_ring(self):
        base = self._engine.base_ring()
        if base is self._engine:
            return self
        return _own_ring(base) if base in SageRings() else base

    def variable_names(self):
        return self._engine.variable_names()

    def _first_ngens(self, n):
        return tuple(self._from_engine_element(value) for value in self._engine.gens()[:n])

    def _repr_(self):
        return repr(self._engine)

    def _latex_(self):
        return str(latex(self._engine))


def _owned_ring_category(engine: Ring) -> Category:
    """Return the strongest owned ring category witnessed by ``engine``."""
    category = engine.category()
    extra = []
    base = engine.base_ring()
    if base is not engine and base in SageRings():
        # The engine presents this ring as an algebra over a base -- a number
        # field over QQ, a p-adic ring over ZZ -- and that is the structure
        # ``base_ring()`` reports, so it is the placement recorded here.
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        extra.append(Algebras(_own_ring(base)))
    if category.is_subcategory(SageIntegralDomains()):
        extra.append(OwnedIntegralDomains())
    if engine is SageZZ or engine is SageQQ:
        extra.append(OwnedOrderedRings())
    if engine is SageQQ:
        extra.append(PrimeFields())
    if category.is_subcategory(SagePrincipalIdealDomains()):
        extra.append(OwnedPrincipalIdealDomains())
    try:
        noetherian = engine.is_noetherian()
    except AttributeError, NotImplementedError, TypeError, ValueError:
        noetherian = engine is SageZZ
    if noetherian is True or engine is SageZZ:
        extra.append(OwnedNoetherianRings())
    if category.is_subcategory(SageFields()):
        placement = OwnedFields()
    elif category.is_subcategory(SageDivisionRings()):
        placement = OwnedDivisionRings()
    else:
        placement = OwnedRings()
    joined = Category.join((placement, _owned_ring_size(engine), *extra))
    if engine is SageZZ or isinstance(engine, SageNumberFieldOrder):
        return Category.join((joined, OwnedOrders()))
    return joined


def _owned_ring_size(engine):
    r"""Return the exact Set-cardinality placement known from the engine kind."""
    from sage.categories.number_fields import NumberFields
    from sage.categories.sets_cat import Sets as SageSets
    from sage.rings.qqbar import QQbar as SageQQbar

    if engine.category().is_subcategory(SageSets().Finite()):
        return FiniteSets()
    if not engine.is_exact():
        return UncountableSets()
    if engine is SageZZ or engine is SageQQ or engine in NumberFields() or engine is SageQQbar:
        return CountablyInfiniteSets()
    return Sets()


def _own_if_ring(result):
    return _own_ring(result) if result in SageRings() else result


@cached_function
def _owned_engine_ring(engine: Ring) -> _OwnedRingParent:
    return _OwnedRingParent(engine)


def _own_ring(ring):
    r"""Private backend adapter: build the preamble ring represented by ``ring``.

    One engine has one owned view: the number-field and order views refine
    this object in place, so ``ZZ.base_ring() is ZZ`` and every morphism
    ``R[G] -> R`` finds one common base ring.
    """
    if ring in OwnedRings():
        return ring
    if ring not in SageRings():
        raise TypeError(f"{ring} is not a ring")
    return _owned_engine_ring(ring)


def _owned_ring(ring):
    r"""Return ``ring`` after asserting it already belongs to the preamble universe."""
    if ring not in OwnedRings():
        raise TypeError("this API expects a preamble ring")
    return ring


def _engine_ring(ring):
    r"""Return the Sage computation parent behind an owned ring."""
    represented = getattr(ring, "_preamble_engine_ring", None)
    if represented is not None:
        ring = represented
    # An owned view can stand over another owned view: an algebra view over a
    # ring view, say.  One unwrap would then still hand back an owned parent,
    # which is not an engine object at all, so the descent continues to the
    # Sage parent underneath.
    while True:
        if isinstance(ring, _OwnedRingParent):
            ring = ring._engine
            continue
        if isinstance(ring, _PredicateSubringParent):
            ring = ring._ambient_ring
            continue
        return ring


def _engine_quotient_cover_ideal(ring, engine_ideal):
    r"""Lift an ideal of a selected quotient engine to its cover ring.

    If the computation parent of ``ring`` is ``S/J``, then an ideal generated
    by classes ``f_i`` is represented upstairs by ``J + (\tilde f_i)``.  This
    private crossing is the exact backend datum needed by Singular operations
    that work over ``S`` but not over Sage's generic quotient-ring parent.
    """
    engine = _engine_ring(ring)
    cover = engine.cover_ring()
    defining = engine.defining_ideal()
    lifted = tuple(engine(generator).lift() for generator in engine_ideal.gens())
    return cover.ideal(tuple(defining.gens()) + lifted)


def _engine_element(ring, element):
    r"""Return the private computation-engine realization of ``element``.

    ``_engine_ring(R)`` identifies a currently selected CAS realization of the
    owned ring ``R``.  This companion crossing converts an element of the
    *owned* ring into that engine without asking the engine's coercion graph to
    know about the owned parent.  Quotients, localizations, completions, and
    future Julia/OSCAR-backed rings can therefore keep one public mathematical
    parent while changing computational realizations independently.
    """
    owned = _own_ring(ring)
    if isinstance(owned, _PredicateSubringParent):
        return _engine_element(owned._ambient_ring, owned(element))
    if getattr(element, "parent", lambda: None)() is owned:
        backend = getattr(element, "_backend", None)
        if callable(backend):
            return backend()
    converter = getattr(owned, "_engine_element", None)
    if converter is not None:
        return converter(element)
    engine = _engine_ring(owned)
    if engine is owned:
        return owned(element)
    return engine(element)


def _engine_numeral(ring, value):
    r"""Cross an ingress numeral to the selected private Sage ring.

    Constructor arguments can arrive as Python numerals, owned ring elements,
    or raw Sage ring elements from backend code.  Public owned-ring coercion
    deliberately rejects the last case; this private constructor boundary is
    precisely where all three spellings are normalized before entering Sage.
    """

    owned = _own_ring(ring)
    engine = _engine_ring(owned)
    parent = getattr(value, "parent", lambda: None)()
    if parent in OwnedRings():
        value = _engine_element(parent, value)
    elif parent is not None and parent not in SageRings():
        raise TypeError("an engine numeral must come from a ring")
    return engine(value)


def _owning_constructor(constructor):
    @wraps(constructor)
    def construct(*args, **kwargs):
        result = constructor(*args, **kwargs)
        return _own_ring(result) if result in SageRings() else result

    return construct


def _constructor_over_ring(constructor):
    @wraps(constructor)
    def construct(base_ring, *args, **kwargs):
        result = constructor(_engine_ring(base_ring), *args, **kwargs)
        return _own_ring(result) if result in SageRings() else result

    return construct


def GF(*args, **kwargs):
    engine = _SageGF(*args, **kwargs)
    field = _own_ring(engine)
    if engine.degree() == 1:
        refine(field, PrimeFields())
    return field


FiniteField = GF


def PrimeField(characteristic):
    return GF(characteristic)


def Zmod(*args, **kwargs):
    return _own_ring(_SageZmod(*args, **kwargs))


IntegerModRing = Zmod
Integers = Zmod


def Qp(*args, **kwargs):
    return _own_ring(_SageQp(*args, **kwargs))


def RealField(*args, **kwargs):
    return _own_ring(_SageRealField(*args, **kwargs))


def ComplexField(*args, **kwargs):
    return _own_ring(_SageComplexField(*args, **kwargs))


Rings = OwnedRings
OrderedRings = OwnedOrderedRings
DivisionRings = OwnedDivisionRings
Fields = OwnedFields
IntegralDomains = OwnedIntegralDomains
PrincipalIdealDomains = OwnedPrincipalIdealDomains
NoetherianRings = OwnedNoetherianRings
ArtinianRings = OwnedArtinianRings
LocalRings = OwnedLocalRings
AdicallyCompleteRings = OwnedAdicallyCompleteRings
CompleteLocalRings = OwnedCompleteLocalRings


def CommutativeRings():
    r"""The category of commutative unital rings.

    The session name for ``OwnedRings().Commutative()``: commutativity is an
    axiom on the operation, and this is the category it cuts out.
    """
    return OwnedRings().Commutative()


OwnedCommutativeRings = CommutativeRings
