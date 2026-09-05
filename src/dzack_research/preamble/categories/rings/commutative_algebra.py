r"""Basic commutative-algebra constructions needed by affine scheme theory."""

from sage.all import (
    PolynomialRing as _SagePolynomialRing,
    PowerSeriesRing as _SagePowerSeriesRing,
    Zp as _SageZp,
)
from sage.categories.category import Category
from sage.categories.rings import Rings as SageRings
from sage.categories.morphism import SetMorphism
from sage.misc.cachefunc import cached_method
from sage.structure.element import Element
from sage.structure.element import CommutativeRingElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE
from sage.structure.sage_object import SageObject
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    CommutativeAlgebras,
    OwnedAlgebras,
    _OwnedAlgebraParent,
    refine_algebra,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedAdicallyCompleteRings,
    OwnedCategoryOverBaseRing,
    OwnedArtinianRings,
    OwnedCommutativeRings,
    OwnedCompleteLocalRings,
    OwnedIntegralDomains,
    OwnedFields,
    OwnedLocalRings,
    OwnedNoetherianRings,
    LocalizationRings,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.group.submonoids import (
    Submonoids,
    generated_submonoid,
    predicate_submonoid,
)
from dzack_research.preamble.categories.sets.set_categories import (
    PartiallyOrderedSets,
    SetInclusion,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.functors.module_localization import module_localization_functor
from dzack_research.preamble.categories.rings.commutative_ideals import CommutativeIdeal
from dzack_research.preamble.categories.rings.ring_foundation import (
    predicate_subring,
    ring_morphism,
)
from dzack_research.preamble.categories.sets.set_categories import FiniteSets
from dzack_research.preamble.categories.sets.cardinals import cardinal


def refine_commutative_algebra(algebra, base_ring, labels=None, *categories):
    r"""Construct the commutative owned algebra view over ``base_ring``."""
    return refine_algebra(algebra, base_ring, labels, *categories)


class PrimeSpectra(OwnedCategory):
    r"""The prime spectra \(\operatorname{Spec}R\), ordered by inclusion."""

    def an_object(self):
        r"""\(\operatorname{Spec}\mathbb{Z}\)."""
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
        from sage.rings.integer_ring import ZZ as SageZZ

        return _own_ring(SageZZ).spectrum()

    def super_categories(self):
        return [PartiallyOrderedSets()]

    class ElementMethods(Element):
        r"""What a prime point is."""

        def __init__(self, parent, ideal) -> None:
            self._ideal = ideal
            Element.__init__(self, parent)

        def ideal(self):
            return self._ideal

        prime_ideal = ideal

        @cached_method
        def local_ring(self):
            return self.parent().ring().localize_at_prime(self.ideal())

        stalk = local_ring

        @cached_method
        def residue_field(self):
            return self.local_ring().residue_field()

        @cached_method
        def residue_map(self):
            r"""Return the canonical map ``R -> kappa(p)`` attached to this point."""
            local = self.local_ring()
            selected = local.__dict__.get("_preamble_source_residue_map")
            if selected is not None:
                return selected
            return local.residue_map() * local.localization_map()

        def specializes_to(self, other) -> bool:
            if other.parent() is not self.parent():
                raise ValueError("specialization compares points of one spectrum")
            ring = self.parent().ring()
            return bool(_engine_ideal(ring, self.ideal()) <= _engine_ideal(ring, other.ideal()))

        def _richcmp_(self, other, op):
            if not other.parent() is self.parent() or other.parent() is not self.parent():
                return NotImplemented
            from sage.structure.richcmp import op_EQ, op_LE, op_LT, op_NE

            ring = self.parent().ring()
            left_ideal = _engine_ideal(ring, self.ideal())
            right_ideal = _engine_ideal(ring, other.ideal())
            if op == op_EQ:
                return left_ideal == right_ideal
            if op == op_NE:
                return left_ideal != right_ideal
            if op == op_LE:
                return self.specializes_to(other)
            if op == op_LT:
                return left_ideal != right_ideal and self.specializes_to(other)
            return NotImplemented

        def __hash__(self):
            r"""Hash the prime ideal equality compares, so a point may key a cache."""
            return hash(_engine_ideal(self.parent().ring(), self.ideal()))

        def _repr_(self):
            return f"Point {self.ideal()} of {self.parent()}"

    class ParentMethods:

        def __init__(self, ring, **rest) -> None:
            self._ring = _own_ring(ring)
            assert self._ring in OwnedCommutativeRings(), (
                "Spec(R) requires a commutative ring"
            )
            super().__init__(**rest)

        def ring(self):
            return self._ring

        coordinate_ring = ring

        def __call__(self, ideal):
            r"""Construct a prime point directly from its represented ideal."""
            return self._element_constructor_(ideal)

        def _element_constructor_(self, ideal):
            if isinstance(ideal, self.category().ElementType) and ideal.parent() is self:
                return ideal
            candidate = _engine_ideal(self.ring(), ideal)
            if not bool(candidate.is_prime()):
                raise ValueError(f"{candidate} is not a prime ideal of {self.ring()}")
            return self.element_class(self, _owned_ideal(self.ring(), candidate))

        def __contains__(self, candidate) -> bool:
            if isinstance(candidate, self.category().ElementType):
                return candidate.parent() is self
            try:
                ideal = _engine_ideal(self.ring(), candidate)
                return bool(ideal.is_prime())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                return False

        def le(self, left, right) -> bool:
            return self._element_constructor_(left).specializes_to(
                self._element_constructor_(right)
            )

        def closed_set(self, ideal):
            return ZariskiClosedSubobject(self, _owned_ideal(self.ring(), ideal))

        V = closed_set

        def distinguished_open(self, function):
            return DistinguishedOpenSubobject(self, function)

        D = distinguished_open

        def generic_point(self):
            engine = _engine_ring(self.ring())
            zero = engine.ideal(0)
            if not bool(zero.is_prime()):
                raise ValueError(f"{self.ring()} is not integral, so Spec has no unique generic point")
            return self._element_constructor_(zero)

        def _repr_(self):
            return f"Spec({self.ring()})"


def _engine_ring_value(ring, value):
    r"""Cross one owned/ordinary ring value to ``ring``'s private engine."""
    source = _own_ring(ring)
    engine = _engine_ring(source)
    parent = getattr(value, "parent", lambda: None)()
    if parent is engine:
        return engine(value)
    return engine(_engine_element(source, source(value)))


def _engine_ideal(ring, ideal):
    r"""Return the computation-ring ideal represented by ``ideal``."""
    engine = _engine_ring(ring)
    represented = getattr(ideal, "_preamble_engine_ideal", None)
    if represented is not None:
        return represented
    if getattr(ideal, "ring", lambda: None)() is engine:
        return ideal
    values = getattr(ideal, "_preamble_module_generator_values", None)
    if values is not None:
        return engine.ideal(tuple(_engine_ring_value(ring, value) for value in values))
    ideal_generators = getattr(ideal, "ideal_generators", None)
    if ideal_generators is not None:
        return engine.ideal(
            tuple(_engine_element(ring, value) for value in ideal_generators())
        )
    generators = getattr(ideal, "gens", None)
    if generators is not None and not isinstance(ideal, (tuple, list)):
        try:
            return engine.ideal(tuple(_engine_ring_value(ring, value) for value in generators()))
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
    if isinstance(ideal, (tuple, list)):
        return engine.ideal(tuple(_engine_ring_value(ring, value) for value in ideal))
    return engine.ideal(_engine_ring_value(ring, ideal))


def _engine_coefficient_ring(engine):
    r"""Return an optional coefficient ring of a private engine realization."""
    base_ring = getattr(engine, "base_ring", None)
    return None if base_ring is None else base_ring()


def _selected_localization_engine(localization_ring):
    r"""Return the selected private realization of a localization ring."""
    engine = localization_ring.__dict__.get("_preamble_engine_ring")
    if engine is None:
        raise NotImplementedError(
            "this localization has no selected computation realization"
        )
    return engine


def _owned_ideal(ring, ideal):
    r"""Return the live ideal subobject represented by ``ideal`` when available."""
    source = _own_ring(ring)
    try:
        if ideal.ring() is source and ideal.inclusion().codomain() is not None:
            return ideal
    except (AttributeError, TypeError):
        pass
    backend = _engine_ideal(source, ideal)
    engine = _engine_ring(source)
    return source.ideal(
        *(source._from_engine_element(engine(generator)) for generator in backend.gens())
    )


def _canonical_map(domain, codomain, engine_map=None):
    source_engine = _engine_ring(domain)
    target_engine = _engine_ring(codomain)
    if engine_map is None and target_engine is not codomain:
        engine_map = target_engine.coerce_map_from(source_engine)

    def image(element):
        source = _engine_element(domain, domain(element))
        value = engine_map(source) if engine_map is not None else source
        converter = getattr(codomain, "_from_engine_element", None)
        if converter is not None:
            return converter(target_engine(value))
        ambient_ring = getattr(codomain, "ambient_ring", None)
        if ambient_ring is not None:
            ambient = ambient_ring()
            ambient_engine = _engine_ring(ambient)
            represented = ambient._from_engine_element(ambient_engine(value))
            return codomain(represented)
        return codomain(value)


    return ring_morphism(
        domain,
        codomain,
        image,
        engine_morphism=engine_map,
    )




class ZariskiClosedSubobject(SetInclusion):
    r"""The closed subobject ``V(I) -> Spec(R)``."""

    def __init__(self, spectrum, ideal) -> None:
        self._defining_ideal = ideal
        from sage.sets.condition_set import ConditionSet

        domain = ConditionSet(
            spectrum,
            lambda point: bool(
                _engine_ideal(spectrum.ring(), self.defining_ideal())
                <= _engine_ideal(spectrum.ring(), point.ideal())
            ),
        )
        SetInclusion.__init__(self, domain, spectrum)

    def defining_ideal(self):
        return self._defining_ideal

    def __contains__(self, point) -> bool:
        try:
            point = self.codomain()(point)
        except (TypeError, ValueError):
            return False
        ring = self.codomain().ring()
        return bool(
            _engine_ideal(ring, self.defining_ideal())
            <= _engine_ideal(ring, point.ideal())
        )

    def _repr_(self):
        return f"V({self.defining_ideal()}) in {self.codomain()}"


class DistinguishedOpenSubobject(SetInclusion):
    r"""The distinguished open subobject ``D(f) -> Spec(R)``."""

    def __init__(self, spectrum, function) -> None:
        self._function = spectrum.ring()(function)
        from sage.sets.condition_set import ConditionSet

        domain = ConditionSet(
            spectrum,
            lambda point: _engine_element(spectrum.ring(), self.function())
            not in _engine_ideal(spectrum.ring(), point.ideal()),
        )
        SetInclusion.__init__(self, domain, spectrum)

    def function(self):
        return self._function

    def __contains__(self, point) -> bool:
        try:
            point = self.codomain()(point)
        except (TypeError, ValueError):
            return False
        ring = self.codomain().ring()
        return _engine_element(ring, self.function()) not in _engine_ideal(ring, point.ideal())

    def coordinate_ring(self):
        return self.codomain().ring().localization(self.function())

    def _repr_(self):
        return f"D({self.function()}) in {self.codomain()}"



class QuotientRings(Category):
    r"""Commutative quotient rings equipped with their quotient map."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def quotient_source(self):
            return self._preamble_quotient_source

        def defining_ideal(self):
            return self._preamble_defining_ideal

        def quotient_map(self):
            return self._preamble_quotient_map

        def localization_comparison(self, localization_ring):
            r"""Return ``S^{-1}(R/I) ~= S^{-1}R/S^{-1}I`` with both maps."""
            return quotient_localization_comparison(self, localization_ring)

        def characteristic(self):
            source = self.quotient_source()
            source_engine = _engine_ring(source)
            defining = self.defining_ideal()
            if source_engine is SageZZ:
                generators = tuple(defining.ideal_generators())
                generator = abs(
                    SageZZ(generators[0]) if generators else SageZZ.zero()
                )
                return generator
            coefficient_ring = _engine_coefficient_ring(source_engine)
            if coefficient_ring is not None:
                try:
                    if bool(coefficient_ring.is_field()):
                        return coefficient_ring.characteristic()
                except (AttributeError, NotImplementedError, TypeError, ValueError):
                    pass
            try:
                return _engine_ring(self).characteristic()
            except NotImplementedError as error:
                raise NotImplementedError(
                    "characteristic of this quotient requires contraction of the defining ideal to the prime subring"
                ) from error


class GeneralQuotientRingElement(CommutativeRingElement):
    r"""A coset in a represented quotient ``R/I`` without a native CAS parent."""

    def __init__(self, parent, representative) -> None:
        self._representative = parent.quotient_source()(representative)
        CommutativeRingElement.__init__(self, parent)

    def lift(self):
        return self._representative

    representative = lift

    def _add_(self, other):
        return self.parent()(self.lift() + other.lift())

    def _mul_(self, other):
        return self.parent()(self.lift() * other.lift())

    def _neg_(self):
        return self.parent()(-self.lift())

    def is_unit(self):
        parent = self.parent()
        if parent._preamble_engine_ring is None:
            raise NotImplementedError(
                "unit testing in this quotient has no selected computation realization"
            )
        return bool(parent._engine_element(self).is_unit())

    def inverse_of_unit(self):
        parent = self.parent()
        if parent._preamble_engine_ring is None:
            raise NotImplementedError(
                "unit inversion in this quotient has no selected computation realization"
            )
        represented = parent._engine_element(self)
        if not represented.is_unit():
            raise ZeroDivisionError(f"{self} is not a unit")
        return parent(represented**-1)

    def __truediv__(self, other):
        return self * self.parent()(other).inverse_of_unit()

    def _richcmp_(self, other, op):
        if not isinstance(other, GeneralQuotientRingElement) or other.parent() is not self.parent():
            return NotImplemented
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = self.parent().defining_ideal().contains_ambient_element(
            self.lift() - other.lift()
        )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        return f"{self.lift()} mod {self.parent().defining_ideal()}"


class GeneralQuotientRingParent(Parent):
    r"""The literal quotient ring ``R/I`` using the ideal congruence."""

    Element = GeneralQuotientRingElement

    def __init__(
        self,
        source,
        defining_ideal,
        _engine_ring=None,
        *,
        categories=(),
    ) -> None:
        self._preamble_quotient_source = source
        self._preamble_defining_ideal = defining_ideal
        self._preamble_engine_ring = _engine_ring
        self._preamble_algebra_base_ring = source
        self._preamble_base_ring = source
        Parent.__init__(
            self,
            category=Category.join(
                (QuotientRings(), CommutativeAlgebras(source), *tuple(categories))
            ),
        )

        self._preamble_quotient_map = ring_morphism(
            source,
            self,
            lambda element: self(element),
        )

    def _element_constructor_(self, value):
        if isinstance(value, GeneralQuotientRingElement) and value.parent() is self:
            return value
        source = self.quotient_source()
        source_engine = _engine_ring(source)
        value_parent = getattr(value, "parent", lambda: None)()
        quotient_engine = self._preamble_engine_ring
        if quotient_engine is not None and value_parent is quotient_engine:
            backend_value = quotient_engine(value)
            lift = getattr(backend_value, "lift", None)
            if lift is None:
                raise TypeError(
                    "the selected quotient-engine element has no lift to the source ring"
                )
            value = source._from_engine_element(source_engine(lift()))
        elif quotient_engine is not None and value_parent in OwnedRings():
            try:
                same_engine = _engine_ring(value_parent) is quotient_engine
            except (TypeError, ValueError, AttributeError):
                same_engine = False
            if same_engine:
                backend_value = quotient_engine(_engine_element(value_parent, value))
                lift = getattr(backend_value, "lift", None)
                if lift is None:
                    raise TypeError(
                        "the equivalent owned quotient element has no lift to the source ring"
                    )
                value = source._from_engine_element(source_engine(lift()))
        elif value_parent is source_engine:
            value = source._from_engine_element(source_engine(value))
        return self.element_class(self, value)

    def __call__(self, value):
        return self._element_constructor_(value)

    def _from_engine_element(self, value):
        r"""Cross one element of the selected quotient engine into this quotient."""
        engine = self._preamble_engine_ring
        if engine is None:
            raise NotImplementedError(
                "this quotient ring has no selected computation realization"
            )
        return self._element_constructor_(engine(value))

    def _engine_element(self, value):
        engine = self._preamble_engine_ring
        if engine is None:
            raise NotImplementedError(
                "this quotient ring has no selected computation realization"
            )
        element = self(value)
        source_value = _engine_element(self.quotient_source(), element.lift())
        try:
            return engine(source_value)
        except (TypeError, ValueError):
            quotient_map = engine.coerce_map_from(_engine_ring(self.quotient_source()))
            if quotient_map is None:
                raise
            return quotient_map(source_value)

    def zero(self):
        return self(self.quotient_source().zero())

    def one(self):
        return self(self.quotient_source().one())

    def an_element(self):
        return self.one()

    def is_finite(self):
        if self._preamble_engine_ring is None:
            from sage.misc.unknown import Unknown

            return Unknown
        return bool(self._preamble_engine_ring.is_finite())

    def cardinality(self):
        if self._preamble_engine_ring is not None:
            return cardinal(self._preamble_engine_ring.cardinality())
        assert False, (
            "cardinality is defined for every quotient ring, but this represented "
            "quotient has no selected exact-cardinality computation"
        )

    def is_field(self):
        if self._preamble_engine_ring is None:
            return False
        return bool(self._preamble_engine_ring.is_field())

    def is_integral_domain(self):
        if self._preamble_engine_ring is None:
            raise NotImplementedError(
                "integral-domain testing for this quotient has no selected computation"
            )
        return bool(self._preamble_engine_ring.is_integral_domain())

    def krull_dimension(self):
        if self._preamble_engine_ring is None:
            raise NotImplementedError(
                "Krull dimension of this quotient has no selected computation"
            )
        return self._preamble_engine_ring.krull_dimension()

    def _repr_(self):
        return f"{self.quotient_source()} / {self.defining_ideal()}"


class QuotientLocalizationComparison(SageObject):
    r"""The canonical compatibility of quotient and localization."""

    def __init__(
        self,
        source_quotient,
        localization_ring,
        localized_quotient,
        quotient_after_localization,
        forward,
        inverse,
        extended_ideal,
    ) -> None:
        self._source_quotient = source_quotient
        self._localization_ring = localization_ring
        self._localized_quotient = localized_quotient
        self._quotient_after_localization = quotient_after_localization
        self._forward = forward
        self._inverse = inverse
        self._extended_ideal = extended_ideal

    def source_quotient(self):
        return self._source_quotient

    def localization_ring(self):
        return self._localization_ring

    def localized_quotient(self):
        r"""Return ``S^{-1}(R/I)``."""
        return self._localized_quotient

    def quotient_after_localization(self):
        r"""Return ``S^{-1}R/S^{-1}I``."""
        return self._quotient_after_localization

    def extended_ideal(self):
        return self._extended_ideal

    def forward(self):
        return self._forward

    isomorphism = forward

    def inverse(self):
        return self._inverse

    def _repr_(self):
        return (
            f"{self.localized_quotient()} ~= "
            f"{self.quotient_after_localization()}"
        )


class GeneralLocalizationRingElement(CommutativeRingElement):
    r"""A literal fraction ``r/s`` in a represented commutative localization."""

    def __init__(self, parent, numerator, denominator) -> None:
        self._numerator = parent.localization_source()(numerator)
        self._denominator = parent.localization_source()(denominator)
        CommutativeRingElement.__init__(self, parent)

    def numerator(self):
        return self._numerator

    def denominator(self):
        return self._denominator

    def _add_(self, other):
        return self.parent().fraction(
            self.numerator() * other.denominator()
            + other.numerator() * self.denominator(),
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
        if isinstance(other, GeneralLocalizationRingElement):
            if other.parent() is not self.parent():
                return NotImplemented
            return self._mul_(other)
        other_parent = getattr(other, "parent", lambda: None)()
        if other_parent is not None:
            try:
                if other_parent.base_ring() is self.parent():
                    return other_parent.scalar_multiple(self, other)
            except (AttributeError, TypeError, ValueError):
                pass
        return NotImplemented

    def inverse_of_unit(self):
        parent = self.parent()
        engine = _selected_localization_engine(parent)
        source = parent.localization_source()
        represented = engine(
            _engine_element(source, self.numerator())
        ) / engine(_engine_element(source, self.denominator()))
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
        engine = _selected_localization_engine(self.parent())
        source = self.parent().localization_source()
        represented = engine(
            _engine_element(source, self.numerator())
        ) / engine(_engine_element(source, self.denominator()))
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
        if not isinstance(other, GeneralLocalizationRingElement) or other.parent() is not self.parent():
            return False
        return self.parent()._fraction_equality_status(self, other)

    def _richcmp_(self, other, op):
        from sage.misc.unknown import Unknown

        if op not in (op_EQ, op_NE):
            return NotImplemented
        status = self.equality_status(other)
        if status is Unknown:
            raise NotImplementedError(
                "equality of these localization fractions is not decidable from the represented data"
            )
        return bool(status) if op == op_EQ else not bool(status)

    def _repr_(self):
        if self.denominator() == self.parent().localization_source().one():
            return repr(self.numerator())
        return f"({self.numerator()})/({self.denominator()})"


class GeneralLocalizationRingParent(Parent):
    r"""The universal fraction model ``S^{-1}R`` for a represented submonoid ``S``."""

    Element = GeneralLocalizationRingElement

    def __init__(
        self,
        source,
        submonoid,
        _engine_ring=None,
        *,
        categories=(),
        algebra_source=None,
    ) -> None:
        self._preamble_localization_source = source
        self._preamble_localization_submonoid = submonoid
        self._preamble_engine_ring = _engine_ring
        algebra_categories = []
        if algebra_source is not None:
            base = algebra_source.base_ring()
            self._preamble_algebra_base_ring = base
            algebra_categories.extend([Algebras(base), OwnedAlgebras(base)])
            if algebra_source in CommutativeAlgebras(base):
                algebra_categories.append(CommutativeAlgebras(base))
        Parent.__init__(
            self,
            base=source.base_ring(),
            category=Category.join(
                (LocalizationRings(), *tuple(categories), *tuple(algebra_categories))
            ),
        )

        self._preamble_localization_map = ring_morphism(
            source,
            self,
            lambda element: self.fraction(element),
        )
        if algebra_source is not None:
            self._preamble_structure_map = (
                self._preamble_localization_map
                * algebra_source.algebra_structure_morphism()
            )

    def localize_module(self, module):
        r"""Return ``S^{-1}M`` through the module-localization theory."""

        if module.base_ring() is not self.localization_source():
            raise ValueError("the module has the wrong source ring for this localization")
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
        if isinstance(value, GeneralLocalizationRingElement) and value.parent() is self:
            return value
        if isinstance(value, tuple) and len(value) == 2:
            return self.fraction(value[0], value[1])
        if self._preamble_engine_ring is not None:
            try:
                represented = self._preamble_engine_ring(value)
                return self.fraction(
                    self.localization_source()(represented.numerator()),
                    self.localization_source()(represented.denominator()),
                    _trusted_denominator=True,
                )
            except (AttributeError, TypeError, ValueError):
                pass
        return self.fraction(value)

    def __call__(self, value):
        return self._element_constructor_(value)

    def _from_engine_element(self, value):
        engine = self._preamble_engine_ring
        if engine is None:
            raise NotImplementedError(
                "this localization has no selected computation realization"
            )
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
            raise NotImplementedError(
                "this localization has no selected computation realization"
            )
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
        difference = (
            left.numerator() * right.denominator()
            - right.numerator() * left.denominator()
        )
        if difference == source.zero():
            return True

        if source in OwnedIntegralDomains():
            return False

        if source in QuotientRings():
            try:
                source_ring = source.quotient_source()
                representative = source_ring(_quotient_representative(difference))
                lifted_generators = tuple(
                    source_ring(_quotient_representative(generator))
                    for generator in self.localization_submonoid().monoid_generators()
                )
                if lifted_generators:
                    product = source_ring.one()
                    for generator in lifted_generators:
                        product *= generator
                    saturated = source.defining_ideal().saturation(
                        source_ring.ideal(product)
                    )
                    return saturated.contains_ambient_element(representative)
            except (AttributeError, NotImplementedError, TypeError, ValueError):
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
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
        return Unknown

    def _repr_(self):
        return (
            f"Localization of {self.localization_source()} at "
            f"{self.localization_submonoid()}"
        )


class PrimeLocalizations(Category):
    r"""Prime local rings ``R_p`` represented inside ``Frac(R)``."""

    def super_categories(self):
        return [OwnedLocalRings(), OwnedIntegralDomains()]

    class ParentMethods:
        def localize_module(self, module):
            r"""Return ``R_p tensor_R M`` through the module-localization theory."""

            if module.base_ring() is not self.localization_source():
                raise ValueError("the module has the wrong source ring for this localization")
            return module_localization_functor(self)(module)

        def localization_source(self):
            return self._preamble_localization_source

        def localized_prime(self):
            return self._preamble_prime_ideal

        def localization_map(self):
            return self._preamble_localization_map

        def is_field(self):
            r"""A domain localization ``R_p`` is a field exactly for ``p=(0)``."""
            source = self.localization_source()
            prime = self.localized_prime()
            return bool(prime == _engine_ring(source).ideal(0))


class AdicCompletions(Category):
    r"""Adic completions equipped with source and ideal of definition."""

    def super_categories(self):
        return [OwnedAdicallyCompleteRings()]

    class ParentMethods:
        def completion_source(self):
            return self._preamble_completion_source

        def completion_map(self):
            return self._preamble_completion_map

        def computation_precision(self):
            return self._preamble_computation_precision


class _AdicCompletionAlgebraParent(_OwnedAlgebraParent):
    r"""An engine-backed adic completion with its defining data fixed at construction."""

    def __init__(self, engine, source, defining_ideal, precision) -> None:
        self._preamble_completion_source = source
        self._preamble_ideal_of_definition = defining_ideal
        self._preamble_computation_precision = int(precision)
        placements = [AdicCompletions()]
        if source in OwnedNoetherianRings():
            placements.append(OwnedNoetherianRings())
        is_maximal = bool(defining_ideal.is_maximal())
        if is_maximal:
            placements.append(OwnedCompleteLocalRings())
        _OwnedAlgebraParent.__init__(
            self,
            engine,
            source,
            None,
            categories=tuple(placements),
        )
        self._preamble_completion_map = _canonical_map(source, self)
        if is_maximal:
            uniformizer = self._from_engine_element(engine.uniformizer())
            self._preamble_maximal_ideal = GeneratedIdealView(
                self,
                (uniformizer,),
                source_ideal=defining_ideal,
            )
            self._preamble_residue_field = ResidueField(source, defining_ideal)


class GeneratedIdealView(SageObject):
    r"""An ideal remembered by its ambient ring and chosen generators."""

    def __init__(self, ring, generators, source_ideal=None) -> None:
        self._ring = ring
        self._generators = tuple(generators)
        self._source_ideal = source_ideal

    def ring(self):
        return self._ring

    def ideal_generators(self):
        return self._generators

    def source_ideal(self):
        return self._source_ideal

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if not isinstance(other, GeneratedIdealView) or other.ring() is not self.ring():
            return False
        if self.source_ideal() is not None and other.source_ideal() is not None:
            source = getattr(self.ring(), "localization_source", lambda: None)()
            if source is not None:
                return bool(
                    _engine_ideal(source, self.source_ideal())
                    == _engine_ideal(source, other.source_ideal())
                )
            return bool(self.source_ideal() == other.source_ideal())
        return self.ideal_generators() == other.ideal_generators()

    def __ne__(self, other) -> bool:
        return not self == other

    def _repr_(self):
        return f"Ideal ({', '.join(map(str, self.ideal_generators()))}) of {self.ring()}"


class LocalizedMaximalIdeal(GeneratedIdealView):
    def __contains__(self, element) -> bool:
        ring = self.ring()
        if element not in ring:
            return False
        if ring in LocalizationRings():
            numerator, _ = ring.localization_fraction_data(element)
            return _engine_element(ring.localization_source(), numerator) in self.source_ideal()
        fraction = _engine_ring(ring.fraction_field())(element)
        return fraction.numerator() in self.source_ideal()


class PrimeLocalizationParent(GeneralLocalizationRingParent):
    r"""A prime localization ``R_p`` with all local-ring data constructor-owned."""

    def __init__(
        self,
        source,
        submonoid,
        prime_ideal,
        fraction_field,
        *,
        engine_ring=None,
        categories=(),
    ) -> None:
        self._preamble_prime_ideal = prime_ideal
        self._preamble_fraction_field = fraction_field
        base = source.base_ring()
        algebra_source = (
            source
            if base is not None and source in Algebras(base)
            else None
        )
        GeneralLocalizationRingParent.__init__(
            self,
            source,
            submonoid,
            _engine_ring=engine_ring,
            categories=(PrimeLocalizations(), *tuple(categories)),
            algebra_source=algebra_source,
        )

        source_engine = _engine_ring(source)
        generators = tuple(
            self.fraction(source._from_engine_element(source_engine(generator)))
            for generator in prime_ideal.gens()
        )
        self._preamble_maximal_ideal = LocalizedMaximalIdeal(
            self,
            generators,
            source_ideal=prime_ideal,
        )

        quotient = QuotientRing(source, prime_ideal)
        residue = quotient if quotient in OwnedFields() else quotient.fraction_field()
        self._preamble_residue_field = residue
        source_to_quotient = quotient.quotient_map()
        source_to_residue = (
            source_to_quotient
            if residue is quotient
            else _canonical_map(quotient, residue) * source_to_quotient
        )

        def local_residue_image(element):
            element = self(element)
            numerator = source_to_residue(element.numerator())
            denominator = source_to_residue(element.denominator())
            return residue(numerator / denominator)

        self._preamble_residue_map = ring_morphism(
            self,
            residue,
            local_residue_image,
        )
        self._preamble_source_residue_map = source_to_residue


def QuotientRing(ring, ideal):
    r"""Return the commutative quotient ring ``R/I`` with its quotient map."""
    source = _own_ring(ring)
    engine = _engine_ring(source)
    defining_ideal = _owned_ideal(source, ideal)
    defining = _engine_ideal(source, defining_ideal)
    try:
        quotient_engine = engine.quotient(defining)
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        quotient_engine = None

    placements = []
    if source in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    if quotient_engine is not None:
        try:
            if bool(quotient_engine.is_field()):
                placements.append(OwnedFields())
            elif bool(quotient_engine.is_integral_domain()):
                placements.append(OwnedIntegralDomains())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
        try:
            if bool(quotient_engine.is_finite()):

                placements.append(FiniteSets())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
        try:
            if source in OwnedNoetherianRings() and quotient_engine.krull_dimension() == 0:
                placements.append(OwnedArtinianRings())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
    return GeneralQuotientRingParent(
        source,
        defining_ideal,
        _engine_ring=quotient_engine,
        categories=tuple(placements),
    )


def _finite_generated_localization(source, submonoid):
    engine = _engine_ring(source)
    try:
        generators = tuple(submonoid.monoid_generators())
    except NotImplementedError as error:
        raise NotImplementedError(
            "the active Sage localization engine requires a chosen finite generating set"
        ) from error
    if not generators:
        return source
    values = tuple(_engine_element(source, value) for value in generators)
    try:
        localization_engine = engine.localization(values)
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        localization_engine = None
    placements = []
    if source in OwnedIntegralDomains():
        placements.append(OwnedIntegralDomains())
    if source in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    base = source.base_ring()
    algebra_source = (
        source
        if base is not None and source in Algebras(base)
        else None
    )
    return GeneralLocalizationRingParent(
        source,
        submonoid,
        _engine_ring=localization_engine,
        categories=tuple(placements),
        algebra_source=algebra_source,
    )


def Localization(ring, *datum):
    r"""Return ``S^{-1}R`` from a submonoid ``S -> (R,*)``.

    Passing ring elements is convenience syntax for the submonoid they generate.
    The mathematical localization datum stored on the result is always the
    represented subobject ``S -> (R,*)``.
    """
    source = _own_ring(ring)
    if len(datum) == 1 and datum[0] in Submonoids(source):
        submonoid = datum[0]
    else:
        if len(datum) == 1 and isinstance(datum[0], (tuple, list)):
            datum = tuple(datum[0])
        submonoid = generated_submonoid(
            source,
            datum,
            description=f"Submonoid generated by {tuple(datum)!r} in {source}",
            structure_data={"kind": "finitely_generated"},
        )

    structure = submonoid.structure_data()
    if structure.get("kind") == "prime_complement":
        return _PrimeLocalizationFromSubmonoid(source, submonoid)
    return _finite_generated_localization(source, submonoid)


def _quotient_representative(element):
    lift = getattr(element, "lift", None)
    if lift is None:
        raise NotImplementedError(
            "this quotient element has no represented lift to the source ring"
        )
    return lift()


def _localization_element_from_source_fraction(localization_ring, numerator, denominator):
    fraction = getattr(localization_ring, "fraction", None)
    if fraction is not None:
        return fraction(numerator, denominator)
    numerator_image = localization_ring.localization_map()(numerator)
    denominator_image = localization_ring.localization_map()(denominator)
    return localization_ring(numerator_image / denominator_image)


def quotient_localization_comparison(source_quotient, localization_ring):
    r"""Return the canonical isomorphism

    ``S^{-1}(R/I) -> S^{-1}R/S^{-1}I``.

    The currently represented comparison requires a chosen finite generating
    set of ``S`` so that its image in ``R/I`` is an actual represented
    submonoid.
    """
    if source_quotient not in QuotientRings():
        raise TypeError("quotient/localization compatibility starts from a represented quotient ring")
    source_ring = source_quotient.quotient_source()
    if localization_ring not in LocalizationRings():
        raise TypeError("the comparison requires a represented localization of the quotient source")
    if localization_ring.localization_source() is not source_ring:
        raise ValueError("the localization has the wrong source ring")

    source_submonoid = localization_ring.localization_submonoid()
    try:
        source_generators = tuple(source_submonoid.monoid_generators())
    except NotImplementedError as error:
        raise NotImplementedError(
            "the quotient/localization comparison currently requires a chosen finite generating set for S"
        ) from error

    quotient_map = source_quotient.quotient_map()
    quotient_submonoid = generated_submonoid(
        source_quotient,
        tuple(quotient_map(generator) for generator in source_generators),
        description=f"Image of {source_submonoid} in {source_quotient}",
        structure_data={"kind": "quotient_image"},
    )
    localized_quotient = Localization(source_quotient, quotient_submonoid)

    defining_ideal = source_quotient.defining_ideal()
    extended_ideal = defining_ideal.extension_to_localization(localization_ring)
    quotient_after_localization = QuotientRing(localization_ring, extended_ideal)

    right_quotient_map = quotient_after_localization.quotient_map()

    def forward_image(element):
        numerator, denominator = localized_quotient.localization_fraction_data(element)
        numerator_lift = source_ring(_quotient_representative(numerator))
        denominator_lift = source_ring(_quotient_representative(denominator))
        localized = _localization_element_from_source_fraction(
            localization_ring,
            numerator_lift,
            denominator_lift,
        )
        return right_quotient_map(localized)


    forward = ring_morphism(
        localized_quotient,
        quotient_after_localization,
        forward_image,
    )

    def inverse_image(element):
        representative = _quotient_representative(element)
        numerator, denominator = localization_ring.localization_fraction_data(representative)
        return localized_quotient.fraction(
            quotient_map(numerator),
            quotient_map(denominator),
        )

    inverse = ring_morphism(
        quotient_after_localization,
        localized_quotient,
        inverse_image,
    )
    return QuotientLocalizationComparison(
        source_quotient,
        localization_ring,
        localized_quotient,
        quotient_after_localization,
        forward,
        inverse,
        extended_ideal,
    )


def ResidueField(ring, ideal=None):
    r"""Return ``R/m`` for a maximal ideal, or the represented local residue field."""
    source = _own_ring(ring)
    if ideal is None:
        if source not in OwnedLocalRings():
            raise TypeError("a residue field without an ideal requires a represented local ring")
        return source.residue_field()
    defining = _engine_ideal(source, ideal)
    if not bool(defining.is_maximal()):
        raise ValueError("a residue field is the quotient by a maximal ideal")
    quotient = QuotientRing(source, defining)
    if not bool(_engine_ring(quotient).is_field()):
        raise ArithmeticError("the quotient by a maximal ideal was not returned as a field")
    return quotient


def _PrimeLocalizationFromSubmonoid(source, submonoid):
    structure = submonoid.structure_data()
    prime_ideal = structure.get("prime_ideal")
    if prime_ideal is None:
        raise ValueError("prime-complement localization requires its represented prime ideal")
    fraction_field = source.fraction_field()
    fraction_engine = _engine_ring(fraction_field)
    placements = []
    if source in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    return PrimeLocalizationParent(
        source,
        submonoid,
        prime_ideal,
        fraction_field,
        engine_ring=fraction_engine,
        categories=tuple(placements),
    )


def PrimeLocalization(ring, prime):
    r"""Return ``R_p`` using the submonoid ``R \ p -> (R,*)``."""
    source = _own_ring(ring)
    if source not in OwnedIntegralDomains():
        raise TypeError("prime localization is currently represented for integral domains")
    prime_ideal = _engine_ideal(source, prime)
    if not bool(prime_ideal.is_prime()):
        raise ValueError("R_p requires a prime ideal p")
    complement = predicate_submonoid(
        source,
        lambda element: _engine_ring_value(source, element) not in prime_ideal,
        f"{source} \\ {prime_ideal}",
        structure_data={"kind": "prime_complement", "prime_ideal": prime_ideal},
    )
    return Localization(source, complement)


def AdicCompletion(ring, ideal, *, precision=20):
    r"""Return a computational realization of the adic completion ``R^``.

    The mathematical parent records ``R`` and the ideal of definition;
    ``precision`` records only the chosen Sage realization.
    """
    source = _own_ring(ring)
    defining = _engine_ideal(source, ideal)
    generators = tuple(defining.gens())
    if len(generators) != 1:
        raise NotImplementedError(
            "the active completion seam currently constructs principal adic completions"
        )
    generator = generators[0]
    engine = _engine_ring(source)
    if engine is SageZZ:
        prime = abs(SageZZ(generator))
        if not prime.is_prime():
            raise ValueError("the represented ZZ-adic completion is at a prime ideal (p)")
        completion_engine = engine.completion(prime, int(precision))
    else:
        completion_engine = engine.completion(generator, prec=precision)
    return _AdicCompletionAlgebraParent(
        completion_engine,
        source,
        defining,
        precision,
    )


class FormalPowerSeriesRings(OwnedCategoryOverBaseRing):
    r"""Formal power-series rings ``R[[t]]`` over the owned ring ``R``."""

    def an_object(self):
        r"""The formal power series ring in one variable."""
        from dzack_research.preamble.rings import PowerSeriesRing

        return PowerSeriesRing(self.base_ring(), "t")

    @classmethod
    def _repr_object_names(cls):
        return "formal power-series rings"

    def super_categories(self):
        return [
            CommutativeAlgebras(self.base_ring()),
            OwnedAdicallyCompleteRings(),
        ]

    class ParentMethods:
        def power_series_variable(self):
            labels = self.algebra_generating_set()
            if int(labels.cardinality()) != 1:
                raise ArithmeticError(
                    "a one-variable formal power-series ring has one selected variable"
                )
            return self.algebra_generator(labels.unrank(0))

    class ElementMethods:
        def coefficient(self, degree):
            degree = int(degree)
            if degree < 0:
                return self.parent().base_ring().zero()
            parent = self.parent()
            base = parent.base_ring()
            backend = parent._engine_element(self)
            return base._from_engine_element(backend[degree])

        def __getitem__(self, degree):
            return self.coefficient(degree)


class _FormalPowerSeriesAlgebraParent(_OwnedAlgebraParent):
    r"""A formal power-series algebra whose adic data are constructor-owned."""

    def __init__(self, engine, base, labels, variable=None) -> None:
        placements = [FormalPowerSeriesRings(base)]
        if base in OwnedNoetherianRings():
            placements.append(OwnedNoetherianRings())
        if base in OwnedLocalRings():
            placements.append(OwnedCompleteLocalRings())
        _OwnedAlgebraParent.__init__(
            self,
            engine,
            base,
            labels,
            categories=tuple(placements),
        )
        uniformizer = engine.gen() if variable is None else engine(variable)
        selected_uniformizer = self._from_engine_element(uniformizer)
        self._preamble_ideal_of_definition = GeneratedIdealView(
            self,
            (selected_uniformizer,),
        )
        if base in OwnedLocalRings():
            self._preamble_maximal_ideal = GeneratedIdealView(
                self,
                (selected_uniformizer,),
            )
            self._preamble_residue_field = base.residue_field()


def Zp(*args, **kwargs):
    engine = _SageZp(*args, **kwargs)
    prime = SageZZ(args[0] if args else kwargs.get("p"))
    source = _own_ring(SageZZ)
    defining = SageZZ.ideal(prime)
    return _AdicCompletionAlgebraParent(
        engine,
        source,
        defining,
        int(engine.precision_cap()),
    )


def PowerSeriesRing(base_ring, *args, **kwargs):
    base = _own_ring(base_ring)
    engine = _SagePowerSeriesRing(_engine_ring(base), *args, **kwargs)
    labels = tuple(engine.variable_names())
    return _FormalPowerSeriesAlgebraParent(
        engine,
        base,
        labels,
    )


class _DualNumbersAlgebraParent(_OwnedAlgebraParent):
    r"""The dual-number quotient with its defining quotient data fixed at construction."""

    def __init__(self, engine, base, polynomial, defining_ideal, label) -> None:
        self._preamble_quotient_source = polynomial
        self._preamble_defining_ideal = defining_ideal
        placements = [QuotientRings()]
        if base in OwnedNoetherianRings():
            placements.append(OwnedNoetherianRings())
        if base in OwnedArtinianRings():
            placements.append(OwnedArtinianRings())
        if base in OwnedLocalRings():
            placements.append(OwnedLocalRings())
        _OwnedAlgebraParent.__init__(
            self,
            engine,
            base,
            (label,),
            categories=tuple(placements),
        )
        self._preamble_quotient_map = _canonical_map(
            polynomial,
            self,
            engine.coerce_map_from(_engine_ring(polynomial)),
        )
        if base in OwnedLocalRings():
            epsilon_bar = self._from_engine_element(engine.gen())
            self._preamble_maximal_ideal = GeneratedIdealView(self, (epsilon_bar,))
            self._preamble_residue_field = base.residue_field()


def DualNumbers(base_ring, name="epsilon"):
    r"""Return the dual-number algebra ``R[epsilon]/(epsilon^2)``."""
    base = _own_ring(base_ring)
    polynomial = refine_algebra(
        _own_ring(_SagePolynomialRing(_engine_ring(base), name)),
        base,
        (name,),
    )
    engine_polynomial = _engine_ring(polynomial)
    epsilon = engine_polynomial.gen()
    defining_ideal = engine_polynomial.ideal(epsilon**2)
    quotient_engine = engine_polynomial.quotient(defining_ideal)
    return _DualNumbersAlgebraParent(
        quotient_engine,
        base,
        polynomial,
        defining_ideal,
        name,
    )


__all__ = [
    "AdicCompletion",
    "AdicCompletions",
    "DualNumbers",
    "GeneratedIdealView",
    "Localization",
    "LocalizationRings",
    "PrimeLocalization",
    "PrimeLocalizations",
    "PowerSeriesRing",
    "QuotientRing",
    "QuotientRings",
    "ResidueField",
    "Zp",
]
