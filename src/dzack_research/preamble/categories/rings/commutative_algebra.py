r"""Basic commutative-algebra constructions needed by affine scheme theory."""

from sage.all import (
    PolynomialRing as _SagePolynomialRing,
    PowerSeriesRing as _SagePowerSeriesRing,
    Zp as _SageZp,
)
from sage.categories.category import Category
from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.categories.rings import Rings as SageRings
from sage.categories.morphism import SetMorphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.structure.element import Element
from sage.structure.element import CommutativeRingElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE
from sage.structure.sage_object import SageObject
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.owned_category import object_of
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
    OwnedRings,
    OwnedCompleteLocalRings,
    OwnedIntegralDomains,
    OwnedFields,
    OwnedLocalRings,
    OwnedNoetherianRings,
    LocalizationRings,
    OwnedRings,
    PrincipalIdealDomains,
    _engine_element,
    _engine_krull_dimension,
    _engine_quotient_cover_ideal,
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
            r"""Return the canonical map ``R -> kappa(p)`` attached to this point.

            This is the map whose factorization through ``R_p`` is the residue
            map of the local ring, so it is asked of the local ring rather than
            recomposed from it.
            """
            return self.local_ring().source_residue_map()

        @cached_method
        def height(self):
            r"""Return the height of this point, the codimension of its closure.

            The height of ``p`` is the dimension of the local ring ``R_p``, and
            in a domain that is finitely generated over a field, or of
            dimension at most one, the dimension formula
            ``height(p) + dim(R/p) = dim(R)`` holds, because such a ring is
            catenary and equidimensional.  So the height is read from two
            dimensions the ring already answers, rather than from a chain of
            primes nobody can enumerate.
            """

            ring = self.parent().ring()
            assert ring in OwnedIntegralDomains(), (
                f"the dimension formula that computes height here needs {ring} to be "
                "an integral domain"
            )
            assert (
                ring in PrincipalIdealDomains()
                or ring.base_ring() in OwnedFields()
            ), (
                f"the dimension formula that computes height here needs {ring} to be "
                "a principal ideal domain or finitely generated over a field, which is "
                "what makes it catenary and equidimensional"
            )
            quotient = QuotientRing(ring, self.ideal())
            return int(ring.krull_dimension()) - int(quotient.krull_dimension())

        def order_of_vanishing(self, function):
            r"""Return ``ord_p(f)`` at this height-one point.

            At a height-one prime of a normal domain ``R_p`` is a discrete
            valuation ring, and the order of vanishing is the length of
            ``R_p/(f)``, which is the valuation of ``f``.  Where the prime is
            generated by one element that element is a uniformizer, its powers
            are the powers of the maximal ideal, and the valuation is the
            multiplicity with which it divides ``f``.

            A prime that is not principal has no uniformizer, and its ordinary
            and symbolic powers can differ, so the multiplicity may not be read
            from membership in ``p^n``; that case is not computed here.
            """

            ring = self.parent().ring()
            function = ring(function)
            assert int(self.height()) == 1, (
                "an order of vanishing is stated at a prime of height one, and "
                f"{self.ideal()} has height {self.height()}"
            )
            prime = self.ideal()
            uniformizer = next(
                (
                    generator
                    for generator in prime.ideal_generators()
                    if ring.ideal(generator) == prime
                ),
                None,
            )
            assert uniformizer is not None, (
                "the order of vanishing is read from a uniformizer, so this prime must "
                f"be generated by one of its chosen generators, and {prime} is not"
            )
            assert not function.is_zero(), (
                "the zero function vanishes to infinite order, which is not an integer"
            )
            return function.valuation(uniformizer)

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
            assert self._ring in OwnedRings().Commutative(), (
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
            candidate = _owned_ideal(self.ring(), ideal)
            if not bool(candidate.is_prime()):
                raise ValueError(f"{candidate} is not a prime ideal of {self.ring()}")
            return self.element_class(self, candidate)

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



class QuotientRings(OwnedCategory):
    r"""Commutative quotient rings equipped with their quotient map."""

    class ElementMethods(Element):
        r"""What a class in \(R/I\) is."""

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
            if not other.parent() is self.parent() or other.parent() is not self.parent():
                return NotImplemented
            if op not in (op_EQ, op_NE):
                return NotImplemented
            equal = self.parent().defining_ideal().contains_ambient_element(
                self.lift() - other.lift()
            )
            return equal if op == op_EQ else not equal

        def _repr_(self):
            return f"{self.lift()} mod {self.parent().defining_ideal()}"

    class ParentMethods:

        def __init__(
            self,
            source,
            defining_ideal,
            _engine_ring=None,
            **rest,
        ) -> None:
            self._preamble_quotient_source = source
            self._preamble_defining_ideal = defining_ideal
            self._preamble_engine_ring = _engine_ring
            self._preamble_algebra_base_ring = source
            # The module level above needs the ring this quotient is an
            # algebra over; a level supplies what the one above declares, and
            # the module level records it.
            super().__init__(base_ring=source, **rest)

            self._preamble_quotient_map = ring_morphism(
                source,
                self,
                lambda element: self(element),
            )

        def _element_constructor_(self, value):
            if isinstance(value, self.category().ElementType) and value.parent() is self:
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
            elif value_parent in OwnedRings():
                try:
                    value_engine = _engine_ring(value_parent)
                except (TypeError, ValueError, AttributeError):
                    value_engine = None
                if value_parent is source or value_engine is source_engine:
                    value = source._from_engine_element(
                        source_engine(_engine_element(value_parent, value))
                    )
                elif quotient_engine is not None and value_engine is quotient_engine:
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
            return _engine_krull_dimension(self)

        def _repr_(self):
            return f"{self.quotient_source()} / {self.defining_ideal()}"

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

    def super_categories(self):
        return [OwnedRings().Commutative()]







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






class PrimeLocalizations(OwnedCategory):
    r"""Prime local rings ``R_p`` represented by fractions with denominator outside ``p``."""

    def super_categories(self):
        r"""``R_p`` is the localization at the multiplicative set ``R \ p``."""
        return [LocalizationRings(), OwnedLocalRings()]

    class ElementMethods:
        def is_unit(self):
            parent = self.parent()
            return not parent.localized_prime().contains_ambient_element(
                self.numerator()
            )

        def inverse_of_unit(self):
            if not self.is_unit():
                raise ZeroDivisionError(f"{self} is not a unit")
            return self.parent().fraction(
                self.denominator(),
                self.numerator(),
            )

    class ParentMethods:
        def __init__(
            self,
            source,
            submonoid,
            prime_ideal,
            fraction_field=None,
            *,
            engine_ring=None,
            **rest,
        ) -> None:
            self._preamble_prime_ideal = prime_ideal
            self._preamble_fraction_field = fraction_field
            base = source.base_ring()
            algebra_source = (
                source
                if base is not None and source in Algebras(base)
                else None
            )
            super().__init__(
                source,
                submonoid,
                _engine_ring=engine_ring,
                algebra_source=algebra_source,
                **rest,
            )

        @cached_method
        def residue_field(self):
            r"""Return ``kappa(p) = R_p / p R_p``.

            ``R/p`` is a domain because ``p`` is prime, and the classes of
            ``R \\ p`` are exactly its nonzero elements, so inverting them gives
            ``Frac(R/p)`` and killing ``p R_p`` afterwards changes nothing.
            When ``p`` is maximal that fraction field is ``R/p`` itself, which
            is what a closed point of the spectrum has.

            This asks ``R`` for a quotient and a fraction field and never for a
            fraction field of its own, so a reducible or nonreduced ``R``,
            which has none, still has a residue field at every point.
            """
            quotient = QuotientRing(self.localization_source(), self.localized_prime())
            if quotient in OwnedFields():
                return quotient
            return quotient.fraction_field()

        @cached_method
        def source_residue_map(self):
            r"""Return ``R -> kappa(p)``, the value of a function at this point."""
            quotient = QuotientRing(self.localization_source(), self.localized_prime())
            residue = self.residue_field()
            if residue is quotient:
                return quotient.quotient_map()
            return _canonical_map(quotient, residue) * quotient.quotient_map()

        @cached_method
        def residue_map(self):
            r"""Return ``R_p -> kappa(p)``, the quotient by the maximal ideal.

            ``R -> kappa(p)`` carries every ``s`` outside ``p`` to a nonzero
            class of the domain ``R/p``, hence to a unit of its fraction field.
            So it inverts ``R \\ p`` and the universal property of ``R_p``
            factors it uniquely through this ring; that factorization is the
            residue map, and its kernel is ``p R_p``.
            """
            return self.induced_morphism(self.source_residue_map())

        @cached_method
        def maximal_ideal(self):
            r"""Return ``p R_p``, the extension of ``p`` along ``R -> R_p``.

            The maximal ideal of a local ring is its non-units, and ``a/s`` is
            a non-unit of ``R_p`` exactly when ``a`` lies in ``p``, so the
            non-units are the ideal ``p`` generates here.  Constructing it as
            the extension of ``p`` is what gives it the operations of an ideal
            rather than a name and a generating set.
            """
            return self.localized_prime().extension_to_localization(self)

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
            r"""Return whether the maximal ideal ``p R_p`` vanishes."""
            return all(
                self(generator) == self.zero()
                for generator in self.localized_prime().ideal_generators()
            )


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


def _maximal_ideal_over_local_base(algebra, base, uniformizers):
    r"""Return the maximal ideal ``m A + (t_1, ..., t_n)`` of a local-base construction.

    Let ``(R, m)`` be local and let ``A`` be ``R[[t_1, ..., t_n]]`` or
    ``R[e]/(e^2)``.  An element of ``A`` is a unit exactly when its constant
    term is a unit of ``R``, hence exactly when that constant term lies outside
    ``m``.  So the non-units of ``A`` are the elements whose constant term lies
    in ``m``, and that set is the ideal generated by the image of ``m``
    together with the new variables.  Either part alone understates it: over a
    field ``m`` is zero and only the variables remain, while over ``Z_(p)`` the
    scalar ``p`` is a non-unit of ``A`` as well.

    The residue field is unchanged by the extra generators, because
    ``A/(m A + (t)) = R/m``.
    """

    engine = _engine_ring(algebra)
    base_maximal = tuple(
        algebra._from_engine_element(engine(_engine_element(base, generator)))
        for generator in base.maximal_ideal().ideal_generators()
    )
    return GeneratedIdealView(
        algebra,
        tuple(generator for generator in (*base_maximal, *uniformizers) if not generator.is_zero()),
    )


def QuotientRing(ring, ideal):
    r"""Return the commutative quotient ring ``R/I`` with its quotient map."""
    source = _own_ring(ring)
    return _quotient_ring(source, _owned_ideal(source, ideal))


@cached_function
def _quotient_ring(source, defining_ideal):
    r"""Return the one ``R/I`` for this ring and this ideal.

    ``R/I`` is determined by ``R`` and ``I``, so it is interned on them.  The
    key is the ideal itself rather than a generating set, and ideals decide
    their own equality, so ``(2)`` and ``(2,4)`` reach the same quotient of the
    integers.

    A prime localization is realized by a fraction field, where every nonzero
    ideal is the unit ideal, so a quotient read from that realization would be
    the zero ring however small ``I`` is.  ``R_p/I R_p`` is therefore left to
    the represented classes, whose equality is the owned membership
    ``a - b in I R_p`` and is exact.
    """
    if source in PrimeLocalizations():
        quotient_engine = None
    else:
        engine = _engine_ring(source)
        defining = _engine_ideal(source, defining_ideal)
        try:
            lifted = _engine_quotient_cover_ideal(source, defining)
            quotient_engine = lifted.ring().quotient(lifted)
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            try:
                quotient_engine = engine.quotient(defining)
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                quotient_engine = None

    dimension = None
    if quotient_engine is not None and source in OwnedNoetherianRings():
        try:
            dimension = _engine_krull_dimension(quotient_engine)
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass

    quotient_is_field = False
    quotient_is_domain = False
    if quotient_engine is not None:
        try:
            quotient_is_field = bool(quotient_engine.is_field())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
        try:
            quotient_is_domain = bool(quotient_engine.is_integral_domain())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
        if quotient_is_domain and dimension == 0:
            quotient_is_field = True
        if quotient_is_domain or quotient_is_field:
            # Sage builds every quotient in its quotient-ring category and
            # never refines it, so the realization refuses to build a fraction
            # field over an ideal it has just proved prime.  The residue field
            # at a point that is not closed is exactly that fraction field, so
            # the realization is told the fact it computed.
            quotient_engine._refine_category_(SageIntegralDomains())

    placements = []
    if source in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    if quotient_is_field:
        placements.append(OwnedFields())
    elif quotient_is_domain:
        placements.append(OwnedIntegralDomains())
    if quotient_engine is not None:
        try:
            if bool(quotient_engine.is_finite()):
                placements.append(FiniteSets())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
    if dimension == 0:
        placements.append(OwnedArtinianRings())

    return object_of(
        Category.join((QuotientRings(), CommutativeAlgebras(source), *placements)),
        source=source,
        defining_ideal=defining_ideal,
        _engine_ring=quotient_engine,
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
    algebra_categories = []
    if algebra_source is not None:
        algebra_base = algebra_source.base_ring()
        algebra_categories = [Algebras(algebra_base), OwnedAlgebras(algebra_base)]
        if algebra_source in CommutativeAlgebras(algebra_base):
            algebra_categories.append(CommutativeAlgebras(algebra_base))
    return object_of(
        Category.join((LocalizationRings(), *placements, *algebra_categories)),
        source=source,
        submonoid=submonoid,
        _engine_ring=localization_engine,
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
        return _localization_at_submonoid(source, datum[0])
    return _localization_at_elements(
        source,
        tuple(source(element) for element in datum),
    )


@cached_function
def _localization_at_elements(source, elements):
    r"""Return the one ``S^{-1}R`` for the submonoid these elements generate.

    The interning is keyed here rather than on the submonoid, because the
    submonoid is built from the elements and is a fresh subobject on every
    call.  So the key is the chosen generating family, and two families that
    generate one submonoid stay two objects: ``<2>`` and ``<2,4>`` are the same
    submonoid of ``(Z,*)`` and give the same ring, but deciding that two
    finitely generated submonoids of a commutative monoid coincide is not
    something the preamble can do, and it is not claimed here.
    """
    return _localization_at_submonoid(
        source,
        generated_submonoid(
            source,
            elements,
            description=f"Submonoid generated by {elements!r} in {source}",
            structure_data={"kind": "finitely_generated"},
        ),
    )


@cached_function
def _localization_at_submonoid(source, submonoid):
    r"""Return the one ``S^{-1}R`` for this ring and this represented submonoid."""
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

    Localizing ``R/I`` means inverting the image of ``S``.  Where ``S`` is
    given by a chosen finite generating set that image is the submonoid the
    images of those generators generate.  Where ``S`` is the complement of a
    prime ``p`` containing ``I``, the image is the complement of the prime
    ``p/I``, so the left side is the prime localization ``(R/I)_{p/I}`` and the
    comparison is the local ring of a point of the closed subscheme ``V(I)``
    read either way round.
    """
    if source_quotient not in QuotientRings():
        raise TypeError("quotient/localization compatibility starts from a represented quotient ring")
    source_ring = source_quotient.quotient_source()
    if localization_ring not in LocalizationRings():
        raise TypeError("the comparison requires a represented localization of the quotient source")
    if localization_ring.localization_source() is not source_ring:
        raise ValueError("the localization has the wrong source ring")

    source_submonoid = localization_ring.localization_submonoid()
    quotient_map = source_quotient.quotient_map()
    defining_ideal = source_quotient.defining_ideal()

    if localization_ring in PrimeLocalizations():
        prime = localization_ring.localized_prime()
        assert all(
            prime.contains_ambient_element(generator)
            for generator in defining_ideal.ideal_generators()
        ), (
            f"the image of the complement of {prime} in {source_quotient} is the complement "
            f"of a prime only when {defining_ideal} lies inside {prime}; otherwise that "
            "image contains zero and both sides of the comparison are the zero ring, which "
            "is not constructed here"
        )
        localized_quotient = PrimeLocalization(
            source_quotient,
            quotient_map.extension_of_ideal(prime),
        )
    else:
        try:
            source_generators = tuple(source_submonoid.monoid_generators())
        except NotImplementedError as error:
            raise NotImplementedError(
                "the quotient/localization comparison reads the image of S from a chosen "
                "finite generating set, or from the prime whose complement S is"
            ) from error

        quotient_submonoid = generated_submonoid(
            source_quotient,
            tuple(quotient_map(generator) for generator in source_generators),
            description=f"Image of {source_submonoid} in {source_quotient}",
            structure_data={"kind": "quotient_image"},
        )
        localized_quotient = Localization(source_quotient, quotient_submonoid)

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
    r"""Return ``R_p`` for a submonoid represented as the complement of ``p``.

    ``R -> R_p`` is injective exactly when ``R`` is a domain, and then ``R_p``
    is the subring of ``Frac(R)`` whose denominators avoid ``p``, which is the
    realization selected below.  A reducible or nonreduced ``R`` has no
    fraction field to sit in, so it selects none: the represented fractions are
    the object, and every question about them -- which are units, when two are
    equal, which lie in an ideal -- is an ideal computation in ``R`` against
    ``p`` rather than a question put to a realization.
    """
    structure = submonoid.structure_data()
    prime_ideal = structure.get("prime_ideal")
    if prime_ideal is None:
        raise ValueError("prime-complement localization requires its represented prime ideal")
    placements = []
    if source in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    if source in OwnedIntegralDomains():
        placements.append(OwnedIntegralDomains())
        fraction_field = source.fraction_field()
        fraction_engine = _engine_ring(fraction_field)
    else:
        fraction_field = None
        fraction_engine = None
    base = source.base_ring()
    algebra_source = (
        source
        if base is not None and source in Algebras(base)
        else None
    )
    if algebra_source is not None:
        placements.extend((Algebras(base), OwnedAlgebras(base)))
        if source in CommutativeAlgebras(base):
            placements.append(CommutativeAlgebras(base))
    return object_of(
        Category.join([PrimeLocalizations(), *placements]),
        source=source,
        submonoid=submonoid,
        prime_ideal=prime_ideal,
        fraction_field=fraction_field,
        engine_ring=fraction_engine,
    )


def PrimeLocalization(ring, prime):
    r"""Return ``R_p`` using the submonoid ``R \ p -> (R,*)``."""
    source = _own_ring(ring)
    if source not in OwnedRings().Commutative():
        raise TypeError("prime localization requires a commutative source ring")
    prime_ideal = _owned_ideal(source, prime)
    if not prime_ideal.is_prime():
        raise ValueError("R_p requires a prime ideal p")
    return _prime_localization(source, prime_ideal)


@cached_function
def _prime_localization(source, prime_ideal):
    r"""Return the one ``R_p`` for this ring and this prime.

    The complement of a prime is a predicate submonoid, freshly built on each
    call and never recognizable as a copy of itself, so the interning is keyed
    on the prime instead.  That key is exact, because the prime is an ideal and
    ideals decide their own equality.
    """
    prime_engine = _engine_ideal(source, prime_ideal)
    complement = predicate_submonoid(
        source,
        lambda element: _engine_ring_value(source, element) not in prime_engine,
        f"{source} \\ {prime_ideal}",
        structure_data={"kind": "prime_complement", "prime_ideal": prime_ideal},
    )
    return _localization_at_submonoid(source, complement)


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
            return self.algebra_generator(labels[0])

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
        uniformizers = tuple(engine.gens()) if variable is None else (engine(variable),)
        selected_uniformizers = tuple(self._from_engine_element(uniformizer) for uniformizer in uniformizers)
        self._preamble_ideal_of_definition = GeneratedIdealView(
            self,
            selected_uniformizers,
        )
        if base in OwnedLocalRings():
            self._preamble_maximal_ideal = _maximal_ideal_over_local_base(
                self,
                base,
                selected_uniformizers,
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
            self._preamble_maximal_ideal = _maximal_ideal_over_local_base(
                self,
                base,
                (epsilon_bar,),
            )
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
