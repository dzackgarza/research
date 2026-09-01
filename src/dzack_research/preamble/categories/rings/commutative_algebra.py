r"""Basic commutative-algebra constructions needed by affine scheme theory."""

from sage.categories.category import Category
from sage.categories.homset import Hom
from sage.categories.rings import Rings as SageRings
from sage.categories.morphism import SetMorphism
from sage.structure.sage_object import SageObject
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.rings.rings import (
    OwnedAdicallyCompleteRings,
    OwnedArtinianRings,
    OwnedCommutativeRings,
    OwnedCompleteLocalRings,
    OwnedIntegralDomains,
    OwnedFields,
    OwnedLocalRings,
    OwnedNoetherianRings,
    engine_ring,
    own_ring,
)
from dzack_research.preamble.categories.group.submonoids import (
    Submonoids,
    generated_submonoid,
    predicate_submonoid,
)
from dzack_research.preamble.refine import refine


def _engine_ideal(ring, ideal):
    r"""Return the computation-ring ideal represented by ``ideal``."""
    engine = engine_ring(ring)
    if getattr(ideal, "ring", lambda: None)() is engine:
        return ideal
    values = getattr(ideal, "_preamble_module_generator_values", None)
    if values is not None:
        return engine.ideal(tuple(engine(value) for value in values))
    if isinstance(ideal, (tuple, list)):
        return engine.ideal(tuple(engine(value) for value in ideal))
    return engine.ideal(engine(ideal))


def _canonical_map(domain, codomain, engine_map=None):
    source_engine = engine_ring(domain)
    target_engine = engine_ring(codomain)
    if engine_map is None and target_engine is not codomain:
        engine_map = target_engine.coerce_map_from(source_engine)

    def image(element):
        source = source_engine(element)
        value = engine_map(source) if engine_map is not None else source
        return codomain(value)

    return SetMorphism(Hom(domain, codomain, SageRings()), image)


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

        def characteristic(self):
            source = self.quotient_source()
            source_engine = engine_ring(source)
            defining = self.defining_ideal()
            if source_engine is SageZZ:
                generator = abs(SageZZ(defining.gen()))
                return generator
            coefficient_ring = getattr(source_engine, "base_ring", lambda: None)()
            if coefficient_ring is not None:
                try:
                    if bool(coefficient_ring.is_field()):
                        return coefficient_ring.characteristic()
                except (AttributeError, NotImplementedError, TypeError, ValueError):
                    pass
            try:
                return engine_ring(self).characteristic()
            except NotImplementedError as error:
                raise NotImplementedError(
                    "characteristic of this quotient requires contraction of the defining ideal to the prime subring"
                ) from error


class LocalizationRings(Category):
    r"""Localizations ``S^{-1}R`` equipped with ``S -> (R,*)`` and ``R -> S^{-1}R``."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def localization_source(self):
            return self._preamble_localization_source

        def localization_submonoid(self):
            return self._preamble_localization_submonoid

        def inverted_elements(self):
            try:
                return self.localization_submonoid().monoid_generators()
            except NotImplementedError as error:
                raise NotImplementedError(
                    "this localization submonoid has no chosen finite generating set"
                ) from error

        def localization_map(self):
            return self._preamble_localization_map


class PrimeLocalizations(Category):
    r"""Prime local rings ``R_p`` represented inside ``Frac(R)``."""

    def super_categories(self):
        return [OwnedLocalRings(), OwnedIntegralDomains()]

    class ParentMethods:
        def localization_source(self):
            return self._preamble_localization_source

        def localized_prime(self):
            return self._preamble_prime_ideal

        def localization_map(self):
            return self._preamble_localization_map


class AdicCompletions(Category):
    r"""Adic completions equipped with source and ideal of definition."""

    def super_categories(self):
        return [OwnedAdicallyCompleteRings()]

    class ParentMethods:
        def completion_map(self):
            return self._preamble_completion_map

        def computation_precision(self):
            return self._preamble_computation_precision


class GeneratedIdealView(SageObject):
    r"""An ideal remembered by its ambient ring and chosen generators."""

    def __init__(self, ring, generators, source_ideal=None) -> None:
        self._ring = ring
        self._generators = tuple(generators)
        self._source_ideal = source_ideal

    def ring(self):
        return self._ring

    def gens(self):
        return self._generators

    generators = gens

    def source_ideal(self):
        return self._source_ideal

    def _repr_(self):
        return f"Ideal ({', '.join(map(str, self.gens()))}) of {self.ring()}"


class LocalizedMaximalIdeal(GeneratedIdealView):
    def __contains__(self, element) -> bool:
        ring = self.ring()
        if element not in ring:
            return False
        fraction = engine_ring(ring.fraction_field())(element)
        numerator = fraction.numerator()
        return numerator in self.source_ideal()


def _refine_noetherian_from_source(result, source):
    if source in OwnedNoetherianRings():
        refine(result, OwnedNoetherianRings())
    return result


def QuotientRing(ring, ideal):
    r"""Return the commutative quotient ring ``R/I`` with its quotient map."""
    source = own_ring(ring)
    engine = engine_ring(source)
    defining = _engine_ideal(source, ideal)
    quotient_engine = engine.quotient(defining)
    from dzack_research.preamble.categories.algebras.algebras import refine_algebra

    quotient = refine_algebra(own_ring(quotient_engine), source)
    refine(quotient, [OwnedCommutativeRings(), QuotientRings()])
    _refine_noetherian_from_source(quotient, source)
    quotient._preamble_quotient_source = source
    quotient._preamble_defining_ideal = defining
    quotient._preamble_quotient_map = _canonical_map(
        source,
        quotient,
        quotient_engine.coerce_map_from(engine),
    )
    return quotient


def _finite_generated_localization(source, submonoid):
    engine = engine_ring(source)
    try:
        generators = tuple(submonoid.monoid_generators())
    except NotImplementedError as error:
        raise NotImplementedError(
            "the active Sage localization engine requires a chosen finite generating set"
        ) from error
    if not generators:
        return source
    values = tuple(engine(value) for value in generators)
    localization_engine = engine.localization(values)
    from dzack_research.preamble.categories.algebras.algebras import refine_algebra

    localization = refine_algebra(own_ring(localization_engine), source)
    placements = [OwnedCommutativeRings(), LocalizationRings()]
    if source in OwnedIntegralDomains():
        placements.append(OwnedIntegralDomains())
    if source in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    refine(localization, placements)
    localization._preamble_localization_source = source
    localization._preamble_localization_submonoid = submonoid
    localization._preamble_localization_map = _canonical_map(
        source,
        localization,
        localization_engine.coerce_map_from(engine),
    )
    return localization


def Localization(ring, *datum):
    r"""Return ``S^{-1}R`` from a submonoid ``S -> (R,*)``.

    Passing ring elements is convenience syntax for the submonoid they generate.
    The mathematical localization datum stored on the result is always the
    represented subobject ``S -> (R,*)``.
    """
    source = own_ring(ring)
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


def ResidueField(ring, ideal=None):
    r"""Return ``R/m`` for a maximal ideal, or the represented local residue field."""
    source = own_ring(ring)
    if ideal is None:
        if source not in OwnedLocalRings():
            raise TypeError("a residue field without an ideal requires a represented local ring")
        return source.residue_field()
    defining = _engine_ideal(source, ideal)
    if not bool(defining.is_maximal()):
        raise ValueError("a residue field is the quotient by a maximal ideal")
    quotient = QuotientRing(source, defining)
    if not bool(engine_ring(quotient).is_field()):
        raise ArithmeticError("the quotient by a maximal ideal was not returned as a field")
    return quotient


def _PrimeLocalizationFromSubmonoid(source, submonoid):
    structure = submonoid.structure_data()
    prime_ideal = structure.get("prime_ideal")
    if prime_ideal is None:
        raise ValueError("prime-complement localization requires its represented prime ideal")
    fraction_field = source.fraction_field()
    fraction_engine = engine_ring(fraction_field)

    def denominator_avoids_prime(element):
        fraction = fraction_engine(element)
        return fraction.denominator() not in prime_ideal

    from dzack_research.preamble.categories.rings.predicate_subrings import predicate_subring

    placements = [PrimeLocalizations(), LocalizationRings()]
    if source in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    local = predicate_subring(
        fraction_field,
        denominator_avoids_prime,
        f"denominator is not in {prime_ideal}",
        Category.join(tuple(placements)),
    )
    local._preamble_localization_source = source
    local._preamble_localization_submonoid = submonoid
    local._preamble_prime_ideal = prime_ideal
    local._preamble_fraction_field = fraction_field
    local._preamble_localization_map = _canonical_map(source, local)
    generators = tuple(local(generator) for generator in prime_ideal.gens())
    local._preamble_maximal_ideal = LocalizedMaximalIdeal(
        local,
        generators,
        source_ideal=prime_ideal,
    )
    quotient = QuotientRing(source, prime_ideal)
    if bool(engine_ring(quotient).is_field()):
        residue = quotient
    else:
        residue = quotient.fraction_field()
    refine(residue, OwnedFields())
    local._preamble_residue_field = residue
    return local


def PrimeLocalization(ring, prime):
    r"""Return ``R_p`` using the submonoid ``R \ p -> (R,*)``."""
    source = own_ring(ring)
    if source not in OwnedIntegralDomains():
        raise TypeError("prime localization is currently represented for integral domains")
    prime_ideal = _engine_ideal(source, prime)
    if not bool(prime_ideal.is_prime()):
        raise ValueError("R_p requires a prime ideal p")
    complement = predicate_submonoid(
        source,
        lambda element: engine_ring(source)(element) not in prime_ideal,
        f"{source} \\ {prime_ideal}",
        structure_data={"kind": "prime_complement", "prime_ideal": prime_ideal},
    )
    return Localization(source, complement)


def AdicCompletion(ring, ideal, *, precision=20):
    r"""Return a computational realization of the adic completion ``R^``.

    The mathematical parent records ``R`` and the ideal of definition;
    ``precision`` records only the chosen Sage realization.
    """
    source = own_ring(ring)
    defining = _engine_ideal(source, ideal)
    generators = tuple(defining.gens())
    if len(generators) != 1:
        raise NotImplementedError(
            "the active completion seam currently constructs principal adic completions"
        )
    generator = generators[0]
    engine = engine_ring(source)
    if engine is SageZZ:
        prime = abs(SageZZ(generator))
        if not prime.is_prime():
            raise ValueError("the represented ZZ-adic completion is at a prime ideal (p)")
        completion_engine = engine.completion(prime, int(precision))
    else:
        completion_engine = engine.completion(generator, prec=precision)
    from dzack_research.preamble.categories.algebras.algebras import refine_algebra

    completion = refine_algebra(own_ring(completion_engine), source)
    placements = [OwnedCommutativeRings(), OwnedAdicallyCompleteRings(), AdicCompletions()]
    if source in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    is_maximal = bool(defining.is_maximal())
    if is_maximal:
        placements.append(OwnedCompleteLocalRings())
    refine(completion, placements)
    completion._preamble_completion_source = source
    completion._preamble_ideal_of_definition = defining
    completion._preamble_computation_precision = precision
    completion._preamble_completion_map = _canonical_map(source, completion)
    if is_maximal:
        uniformizer = completion(completion_engine.uniformizer())
        completion._preamble_maximal_ideal = GeneratedIdealView(
            completion,
            (uniformizer,),
            source_ideal=defining,
        )
        completion._preamble_residue_field = ResidueField(source, defining)
    return completion


def refine_power_series_ring(power_series_ring, base_ring, variable=None):
    r"""Record ``R[[t]]`` as a ``(t)``-adically complete ``R``-algebra."""
    ring = power_series_ring
    base = own_ring(base_ring)
    engine = engine_ring(ring)
    uniformizer = engine.gen() if variable is None else engine(variable)
    ring._preamble_ideal_of_definition = GeneratedIdealView(
        ring,
        (ring(uniformizer),),
    )
    refine(ring, OwnedAdicallyCompleteRings())
    if base in OwnedNoetherianRings():
        refine(ring, OwnedNoetherianRings())
    if base in OwnedLocalRings():
        refine(ring, OwnedCompleteLocalRings())
        ring._preamble_maximal_ideal = GeneratedIdealView(
            ring,
            (ring(uniformizer),),
        )
        ring._preamble_residue_field = base.residue_field()
    return ring


def DualNumbers(base_ring, name="epsilon"):
    r"""Return the dual-number algebra ``R[epsilon]/(epsilon^2)``."""
    base = own_ring(base_ring)
    from dzack_research.preamble.categories.rings.rings import PolynomialRing
    from dzack_research.preamble.categories.algebras.algebras import refine_algebra

    polynomial = PolynomialRing(base, name)
    engine_polynomial = engine_ring(polynomial)
    epsilon = engine_polynomial.gen()
    quotient_engine = engine_polynomial.quotient(engine_polynomial.ideal(epsilon**2))
    dual = refine_algebra(own_ring(quotient_engine), base, (name,))
    placements = [OwnedCommutativeRings(), QuotientRings()]
    if base in OwnedNoetherianRings():
        placements.append(OwnedNoetherianRings())
    if base in OwnedArtinianRings():
        placements.append(OwnedArtinianRings())
    if base in OwnedLocalRings():
        placements.append(OwnedLocalRings())
    refine(dual, placements)
    dual._preamble_quotient_source = polynomial
    dual._preamble_defining_ideal = engine_polynomial.ideal(epsilon**2)
    dual._preamble_quotient_map = _canonical_map(
        polynomial,
        dual,
        quotient_engine.coerce_map_from(engine_polynomial),
    )
    if base in OwnedLocalRings():
        epsilon_bar = dual(quotient_engine.gen())
        dual._preamble_maximal_ideal = GeneratedIdealView(dual, (epsilon_bar,))
        dual._preamble_residue_field = base.residue_field()
    return dual


__all__ = [
    "AdicCompletion",
    "AdicCompletions",
    "DualNumbers",
    "GeneratedIdealView",
    "Localization",
    "LocalizationRings",
    "PrimeLocalization",
    "PrimeLocalizations",
    "QuotientRing",
    "QuotientRings",
    "ResidueField",
    "refine_power_series_ring",
]
