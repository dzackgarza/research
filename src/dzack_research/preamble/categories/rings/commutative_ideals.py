"""Finitely generated commutative ideals as module subobjects of the ring."""

from sage.categories.category import Category
from dzack_research.preamble.categories.modules.pure.modules import ModulesWithChosenFinitePresentation

from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.quotient_ring import QuotientRing_generic
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.modules.localizations import (
    _localized_module,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    ModuleSubobjects,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_quotient_cover_ideal,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.set_categories import Sets


def _engine_commutative_ideal(ideal):
    r"""Lower one owned commutative ideal to its selected computation model.

    Protected commutative-ideal contract under OWN-05--07. The permitted
    external caller role is the commutative-algebra construction adapter when
    an engine operation literally takes an ideal of the selected computation
    ring. The input remains the owned ideal; the raw ideal must not escape that
    adapter, and ordinary ideal mathematics uses public ideal operations.
    """
    return ideal._engine_ideal()


@cached_function
def _localized_commutative_ideal(source_ideal, localization_ring):
    r"""Return ``S^{-1}I <= S^{-1}R``, the localization of one ideal.

    Interned on the source ideal and the localization, which together
    determine it, so an ideal of a localization is one object however often
    it is asked for.
    """
    localization_map = localization_ring.localization_map()
    source_regular_module = source_ideal.ring().regular_module()
    target_regular_module = localization_ring.regular_module()
    source_regular_labels = tuple(source_regular_module.module_generating_set())
    target_regular_labels = tuple(target_regular_module.module_generating_set())
    if len(source_regular_labels) != 1 or len(target_regular_labels) != 1:
        raise ArithmeticError("a ring viewed as a module over itself must have rank one")
    source_regular_label = source_regular_labels[0]
    target_regular_label = target_regular_labels[0]

    def embedded(label):
        source_image = source_ideal.inclusion()(
            source_ideal.module_generator(label)
        )
        coefficient = source_regular_module.framing_coefficients(source_image).get(
            source_regular_label,
            source_ideal.ring().zero(),
        )
        return target_regular_module.scalar_multiple(
            localization_map(coefficient),
            target_regular_module.module_generator(target_regular_label),
        )

    ideal = _localized_module(
        source_ideal,
        localization_ring,
        localization_ring.localization_functor(),
        subobject_ambient=target_regular_module,
        subobject_generator_images=embedded,
        extra_categories=(CommutativeIdeals(localization_ring),),
        extra_construction_data={
            "ideal_generators": tuple(
                localization_map(generator)
                for generator in source_ideal.ideal_generators()
            ),
            "localization_source_ideal": source_ideal,
        },
    )
    return ideal


class CommutativeIdeals(OwnedCategoryOverBaseRing):
    r"""Ideals of ``R``: subobjects of the rank-one ``R``-module ``R``."""

    def an_object(self):
        r"""The ideal (2)."""
        return self.base_ring().ideal(2)

    def super_categories(self):
        return [ModuleSubobjects(self.base_ring())]

    def subobject_category(self):

        ring = self.base_ring()
        return Modules(ring).Subobjects(ring.regular_module())

    @cached_method
    def extension_to_fraction_field(self):
        r"""The functor ``CommutativeIdeals(R) -> FractionalIdeals(R)``, ``I |-> I`` inside ``Frac(R)``."""
        from dzack_research.preamble.categories.modules.fractional_ideals import (
            _FractionalIdealExtension,
        )

        return _FractionalIdealExtension(self)

    class ParentMethods:
        def __init__(
            self,
            ideal_generators=None,
            engine_ideal=None,
            localization_source_ideal=None,
            **rest,
        ) -> None:
            self._ideal_generators = (
                None
                if ideal_generators is None
                else finite_family(ideal_generators, name="Selected ideal generators")
            )
            self._selected_engine_ideal = engine_ideal
            self._localization_source_ideal = localization_source_ideal
            super().__init__(**rest)

        def ring(self):
            return self.base_ring()

        def ideal_generators(self):
            generators = self._ideal_generators
            assert generators is not None, "a represented commutative ideal must retain its selected generators"
            return generators

        def __eq__(self, other) -> bool:
            r"""Two ideals of one ring are equal when each contains the other.

            Over a localization the equality is decided that way rather than by
            the computation realization.  ``R_p`` is realized by ``Frac(R)``,
            where every nonzero ideal is the unit ideal, so an engine
            comparison there would identify ideals that differ; mutual
            containment is decided in ``R`` by the localization criterion in
            :meth:`contains_ambient_element`.
            """
            if other not in CommutativeIdeals(self.ring()):
                return False
            if self.ring() in LocalizationRings():
                return all(
                    other.contains_ambient_element(generator)
                    for generator in self.ideal_generators()
                ) and all(
                    self.contains_ambient_element(generator)
                    for generator in other.ideal_generators()
                )
            return bool(self._engine_ideal() == other._engine_ideal())

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self):
            r"""Hash on the ring alone, which equality then refines.

            Equal ideals must hash equally, and equality here is containment
            each way: ``(2)`` and ``(2,4)`` are one ideal of the integers
            written twice, so no invariant of a generating set can be hashed.
            The ring is the coarsest thing every equal pair shares, and the
            decision is left to ``__eq__``.

            ponytail: every ideal of one ring collides, so a dict keyed on
            ideals scans that ring's entries; refine only if such a dict grows.
            """
            return hash(self.ring())

        def _richcmp_(self, other, op):
            if op not in (op_EQ, op_NE):
                return NotImplemented
            equal = self == other
            return equal if op == op_EQ else not equal

        def _engine_ideal(self):
            r"""Return this ideal's private selected computation realization.

            This is the implementation endpoint of
            :func:\`_engine_commutative_ideal\`.  Ordinary mathematical
            consumers do not call it directly; the only external crossing is
            the declared commutative-algebra construction adapter.
            """
            represented = self._selected_engine_ideal
            if represented is not None:
                return represented
            engine = _engine_ring(self.ring())
            assert engine is not self.ring(), (
                "this ideal operation requires an active engine-ideal realization"
            )
            return engine.ideal(
                tuple(
                    _engine_element(self.ring(), generator)
                    for generator in self.ideal_generators()
                )
            )

        def extension_to_localization(self, localization_ring):
            r"""Return the represented localization ``S^{-1}I <= S^{-1}R``."""
            if localization_ring not in LocalizationRings():
                raise TypeError("ideal localization requires a represented ring localization")
            if localization_ring.localization_source() is not self.ring():
                raise ValueError("the localization has the wrong source ring")
            return _localized_commutative_ideal(self, localization_ring)

        def is_prime(self):
            backend = self._engine_ideal()
            match _realized_as_quotient(self.ring()):
                case True:
                    return bool(_cover_lifted_ideal(self).is_prime())
                case False:
                    return bool(backend.is_prime())

        def is_maximal(self):
            backend = self._engine_ideal()
            match _realized_as_quotient(self.ring()):
                case True:
                    selected = _cover_lifted_ideal(self)
                case False:
                    selected = backend
            selected_ring = selected.ring()
            match selected_ring:
                case PolynomialRing_generic() | MPolynomialRing_base() if bool(
                    selected_ring.base_ring().is_field()
                ):
                    return bool(selected.is_prime() and selected.dimension() == 0)
                case _:
                    return bool(selected.is_maximal())

        def radical(self):
            r"""Return ``sqrt(I)``.

            Over a realized quotient ``P/K`` the radical is computed on the
            preimage: an element is nilpotent modulo ``I`` exactly when its
            lift is nilpotent modulo the preimage, so ``sqrt(I)`` is
            ``sqrt(I~)/K``.
            """
            ring = self.ring()
            if ring._has_selected_exact_coefficient_presentation():
                presentation_ring = ring._exact_coefficient_presentation_ring()
                lifted_generators = tuple(
                    presentation_ring(
                        ring._lift_coefficient_to_presentation(generator)
                    )
                    for generator in self.ideal_generators()
                )
                presentation_relations = tuple(
                    presentation_ring(relation)
                    for relation in ring._exact_coefficient_presentation_relations()
                )
                lifted = presentation_ring.ideal(
                    *(
                        presentation_relations
                        + lifted_generators
                        or (presentation_ring.zero(),)
                    )
                )
                radical = lifted.radical()
                descended_generators = tuple(
                    ring._descend_coefficient_from_presentation(generator)
                    for generator in radical.ideal_generators()
                )
                return ring.ideal(
                    *(descended_generators or (ring.zero(),))
                )
            if _realized_as_quotient(ring):
                return _descend_cover_ideal(ring, _cover_lifted_ideal(self).radical())
            return _from_engine_ideal(ring, self._engine_ideal().radical())

        def colon(self, other):
            r"""Return the ideal quotient ``(I : J)``.

            Where the ring is realized as a quotient ``P/K``, the colon is
            computed on preimages.  Taking preimages along ``P -> P/K`` is a
            bijection onto the ideals of ``P`` containing ``K`` and it respects
            products, so ``a J <= I`` upstairs says the same thing as it does
            downstairs and ``(I : J)`` is ``(I~ : J~)/K``.  Singular computes a
            colon for an ideal of ``P``, and Sage's quotient-ring ideal offers
            none, so the computation is lifted and the result descended.
            """
            _require_same_ring(self, other)
            if _realized_as_quotient(self.ring()):
                return _descend_cover_ideal(
                    self.ring(),
                    _cover_lifted_ideal(self).quotient(_cover_lifted_ideal(other)),
                )
            method = _optional_engine_method(self._engine_ideal(), "quotient")
            match method:
                case None:
                    ring = self.ring()
                    assert ring in OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals(), (
                        "ideal colon without an engine quotient operation requires the owned PID fallback"
                    )
                    numerator = _pid_principal_ideal_generator(self)
                    denominator = _pid_principal_ideal_generator(other)
                    match denominator == ring.zero():
                        case True:
                            return ring.ideal(ring.one())
                        case False:
                            common = numerator.gcd(denominator)
                            quotient, remainder = numerator.quo_rem(common)
                    match remainder == ring.zero():
                        case True:
                            return ring.ideal(quotient)
                        case False:
                            raise ArithmeticError(
                                "a PID gcd did not divide the ideal generator exactly"
                            )
                case _:
                    return _from_engine_ideal(
                        self.ring(), method(other._engine_ideal())
                    )

        ideal_quotient = colon

        def ideal_saturation(self, other):
            r"""Return ``(I : J^infinity)``.

            This name keeps ideal saturation distinct from saturation of a
            module subobject.  Preimages behave as they do for a colon, so a
            saturation over a realized quotient ``P/K`` is
            ``(I~ : J~^infinity)/K``.  Sage answers with the ideal and the
            exponent that reached it; the exponent is a fact about the
            computation, not about the ideal.
            """
            _require_same_ring(self, other)
            if _realized_as_quotient(self.ring()):
                saturated, _reached_at_exponent = _cover_lifted_ideal(self).saturation(
                    _cover_lifted_ideal(other)
                )
                return _descend_cover_ideal(self.ring(), saturated)
            method = _optional_engine_method(self._engine_ideal(), "saturation")
            match method:
                case None:
                    ring = self.ring()
                    assert ring in OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals(), (
                        "ideal saturation without an engine operation requires the owned PID fallback"
                    )

                    numerator = _pid_principal_ideal_generator(self)
                    denominator = _pid_principal_ideal_generator(other)
                    match (numerator == ring.zero(), denominator == ring.zero()):
                        case (_, True):
                            return ring.ideal(ring.one())
                        case (True, False):
                            return ring.ideal(ring.zero())
                        case (False, False):
                            current = numerator

                    while True:
                        common = current.gcd(denominator)
                        match common.is_unit():
                            case True:
                                return ring.ideal(current)
                            case False:
                                quotient, remainder = current.quo_rem(common)
                                match remainder == ring.zero():
                                    case True:
                                        current = quotient
                                    case False:
                                        raise ArithmeticError(
                                            "a PID gcd did not divide the ideal generator exactly"
                                        )
                case _:
                    saturated, _reached_at_exponent = method(other._engine_ideal())
                    return _from_engine_ideal(self.ring(), saturated)

        saturation = ideal_saturation

        def contraction_from_localization(self):
            r"""Contract this selected localized extension back to its source ring."""
            source_ideal = self._localization_source_ideal
            assert source_ideal is not None, (
                "ideal contraction here requires an ideal selected as a localization extension"
            )
            localization_ring = self.ring()
            submonoid = localization_ring.localization_submonoid()
            generators = tuple(submonoid.monoid_generators())
            if not generators:
                return source_ideal

            source_ring = localization_ring.localization_source()

            # If the source is represented as A = P/I, compute contraction in
            # the selected presentation ring P rather than asking Singular to
            # saturate an ideal inside Sage's generic quotient parent.  For
            # S=<s_1,...,s_r>, the contraction of S^{-1}J is
            #
            #     (I + J~) : (s~_1 ... s~_r)^infinity / I,
            #
            # where tildes denote the selected lifts to P.  This is the same
            # exact presentation data used by quotient-coefficient module
            # equality and by localization fraction equality.
            has_presentation = (
                source_ring._has_selected_exact_coefficient_presentation()
            )
            if has_presentation:
                presentation_ring = source_ring._exact_coefficient_presentation_ring()
                lifted_ideal_generators = tuple(
                    presentation_ring(
                        source_ring._lift_coefficient_to_presentation(generator)
                    )
                    for generator in source_ideal.ideal_generators()
                )
                presentation_relations = tuple(
                    presentation_ring(relation)
                    for relation in source_ring._exact_coefficient_presentation_relations()
                )
                lifted_denominators = tuple(
                    presentation_ring(
                        source_ring._lift_coefficient_to_presentation(generator)
                    )
                    for generator in generators
                )
                product = presentation_ring.one()
                for denominator in lifted_denominators:
                    product *= denominator
                lifted_ideal = presentation_ring.ideal(
                    *(
                        presentation_relations
                        + lifted_ideal_generators
                        or (presentation_ring.zero(),)
                    )
                )
                saturated = lifted_ideal.saturation(
                    presentation_ring.ideal(product)
                )
                descended_generators = tuple(
                    source_ring._descend_coefficient_from_presentation(generator)
                    for generator in saturated.ideal_generators()
                )
                return source_ring.ideal(
                    *(descended_generators or (source_ring.zero(),))
                )

            engine = _engine_ring(source_ring)
            source_backend = source_ideal._engine_ideal()
            saturation_method = _optional_engine_method(source_backend, "saturation")
            if saturation_method is not None:
                product = engine.one()
                for generator in generators:
                    product *= _engine_ring_value(source_ring, generator)
                result = saturation_method(engine.ideal(product))
                saturated = result[0] if isinstance(result, tuple) else result
                return _from_engine_ideal(source_ring, saturated)

            # Principal-ideal-domain computation.  If I=(a), saturation by
            # <s_1,...,s_n> removes from a every prime factor occurring in
            # one of the s_i.  Repeated gcd division does this without a
            # separate factorization algorithm.
            from sage.categories.principal_ideal_domains import PrincipalIdealDomains

            if engine in PrincipalIdealDomains():
                generator = engine(source_backend.gen())
                if generator == 0:
                    return source_ideal
                changed = True
                while changed:
                    changed = False
                    for denominator in generators:
                        gcd = generator.gcd(_engine_ring_value(source_ring, denominator))
                        if gcd != 0 and not gcd.is_unit():
                            generator = engine(generator / gcd)
                            changed = True
                return source_ring.ideal(_owned_engine_element(source_ring, engine(generator)))

            assert engine in PrincipalIdealDomains(), (
                "localization-ideal contraction requires either engine saturation or the supported PID fallback"
            )

        contraction = contraction_from_localization

        def contains_ambient_element(self, element) -> bool:
            r"""Return whether an ambient ring element lies in this ideal."""
            ring = self.ring()
            value = ring(element)
            source_ideal = self._localization_source_ideal
            if ring in LocalizationRings() and source_ideal is not None:
                numerator, _denominator = ring.localization_fraction_data(value)
                structure = ring.localization_submonoid()._structure_data()
                if structure.get("kind") == "prime_complement":
                    # ``a/s`` lies in ``I R_p`` exactly when some element
                    # outside ``p`` carries ``a`` into ``I``, and the elements
                    # that carry ``a`` into ``I`` are the colon ideal
                    # ``(I : a)``.  So membership says that ``(I : a)`` is not
                    # contained in ``p``, and an ideal lies in a prime exactly
                    # when its generators do.  The complement of a prime has no
                    # finite generating set, so no contraction is available to
                    # ask instead.
                    prime = structure["prime_ideal"]
                    source = source_ideal.ring()
                    colon_ideal = source_ideal.colon(source.ideal(numerator))
                    return any(
                        not prime.contains_ambient_element(generator)
                        for generator in colon_ideal.ideal_generators()
                    )
                contracted = self.contraction_from_localization()
                return _engine_ring_value(contracted.ring(), numerator) in contracted._engine_ideal()
            return _engine_element(ring, value) in self._engine_ideal()

        def __contains__(self, candidate) -> bool:
            if getattr(candidate, "parent", lambda: None)() is self:
                return True
            if candidate not in self.ring():
                return False
            return self.contains_ambient_element(candidate)

        def sum(self, other):
            _require_same_ring(self, other)
            return _from_engine_ideal(
                self.ring(), self._engine_ideal() + other._engine_ideal()
            )

        def product(self, other):
            _require_same_ring(self, other)
            return _from_engine_ideal(
                self.ring(), self._engine_ideal() * other._engine_ideal()
            )

        def intersection(self, other):
            _require_same_ring(self, other)
            return _from_engine_ideal(
                self.ring(), self._engine_ideal().intersection(other._engine_ideal())
            )

        def power(self, exponent):
            exponent = int(exponent)
            if exponent < 0:
                raise ValueError("an integral ideal power has nonnegative exponent")
            return _from_engine_ideal(self.ring(), self._engine_ideal() ** exponent)

        def quotient_ring(self):
            return self.ring().quotient_ring(self)

        def image_under_fraction_field_automorphism(self, morphism):
            r"""Return the conjugate ideal under an automorphism of the fraction field.

            The ideal is transported from its owned generators.  No
            number-field ideal realization crosses to the caller.
            """
            ring = self.ring()
            field = ring.fraction_field()
            if morphism.domain() is not field or morphism.codomain() is not field:
                raise ValueError(
                    "ideal conjugation requires an automorphism of the ambient fraction field"
                )
            images = tuple(
                ring(morphism(field(generator)))
                for generator in self.ideal_generators()
            )
            return ring.ideal(*images)

        def congruent(self, left, right) -> bool:
            r"""Return whether left and right have the same image in the quotient ring."""
            ring = self.ring()
            return ring(left) - ring(right) in self

        def residue_cardinality(self):
            r"""Return the cardinality of the quotient ring when it is finite."""
            return self.quotient_ring().cardinality()

        def syzygy_matrix(self):

            backend = self._engine_ideal()
            selected = tuple(backend.gens())
            rows = _engine_ideal_syzygy_rows(self.ring(), backend, selected)
            assert rows is not None, (
                "syzygy_matrix requires a selected exact ideal module-presentation backend"
            )
            ring = self.ring()
            owned_rows = tuple(
                tuple(
                    _owned_engine_element(ring, coefficient)
                    for coefficient in row
                )
                for row in rows
            )
            return ring.matrix_space(
                len(owned_rows),
                len(selected),
            ).from_rows(owned_rows)

        def primary_decomposition(self):
            method = _engine_ideal_method(
                self,
                "primary_decomposition",
                "this ideal backend has no primary decomposition",
            )
            return finite_ordered_set(
                tuple(_from_engine_ideal(self.ring(), ideal) for ideal in method())
            )

        def hilbert_polynomial_value(self, argument):
            r"""Return the value at \`argument\` of the Hilbert polynomial of \`R/I\`.

            The maintained ideal engine computes the polynomial, but the
            engine polynomial itself does not cross the ideal boundary.  Only
            its exact scalar value is raised into the owned coefficient ring.
            """
            method = _engine_ideal_method(
                self,
                "hilbert_polynomial",
                "this ideal backend has no Hilbert-polynomial computation",
            )
            value = method()(SageZZ(argument))
            parent = getattr(value, "parent", lambda: None)()
            if parent is None:
                return _owned_engine_element(SageZZ, SageZZ(value))
            return _owned_engine_element(parent, value)

        def associated_primes(self):
            method = _engine_ideal_method(
                self,
                "associated_primes",
                "this ideal backend has no associated-prime computation",
            )
            return finite_ordered_set(
                tuple(_from_engine_ideal(self.ring(), ideal) for ideal in method())
            )

        def _repr_(self):
            listed = ", ".join(str(generator) for generator in self.ideal_generators())
            return f"Ideal ({listed}) of {self.ring()}"


def _require_same_ring(left, right):
    if left.ring() is not right.ring():
        raise ValueError("ideal arithmetic requires one ambient ring")


def _pid_principal_ideal_generator(ideal):
    r"""Return a generator of an ideal in a represented principal ideal domain."""
    ring = ideal.ring()
    generators = tuple(ideal.ideal_generators())
    match generators:
        case ():
            return ring.zero()
        case (first, *rest):
            generator = ring(first)
            for candidate in rest:
                generator = generator.gcd(ring(candidate))
            return generator


def _optional_engine_method(engine, name):
    r"""Return one optional operation of a private computational realization."""
    return getattr(engine, name, None)


def _engine_ideal_method(ideal, name, unavailable_message):
    r"""Resolve a selected ideal-engine operation only at the private boundary."""
    method = _optional_engine_method(ideal._engine_ideal(), name)
    assert callable(method), unavailable_message
    return method


def _realized_as_quotient(ring) -> bool:
    r"""Return whether the realization of ``ring`` is a quotient ``P/K``.

    Only a quotient realization presents a cover ring, and an ideal of one is
    a Singular ideal whose parent Singular itself refuses: the operation is
    offered and then declines when called.  So the routing is decided from the
    ring rather than from whether the operation is present.
    """
    match _engine_ring(ring):
        case QuotientRing_generic():
            return True
        case _:
            return False


def _cover_lifted_ideal(ideal):
    r"""Return the preimage in ``P`` of an ideal of a ring realized as ``P/K``.

    The preimage of ``I`` is ``K`` together with lifts of its generators, which
    is what :func:`_engine_quotient_cover_ideal` builds.  Singular performs an
    ideal operation over ``P`` and not over Sage's quotient parent, so the
    operation is computed on preimages and its result descended.
    """
    ring = ideal.ring()
    assert _realized_as_quotient(ring), (
        f"an ideal operation of {ring} is computed by its own realization, or in the "
        "cover ring when that realization is a quotient; this realization is neither"
    )
    return _engine_quotient_cover_ideal(ring, ideal._engine_ideal())


def _descend_cover_ideal(ring, cover_ideal):
    r"""Return the ideal of ``P/K`` whose preimage in ``P`` is ``cover_ideal``."""
    source = _own_ring(ring)
    descended = tuple(
        _owned_engine_value(source, generator) for generator in cover_ideal.gens()
    )
    return source.ideal(*(descended or (source.zero(),)))


def _engine_ideal_syzygy_rows(ring, backend, selected):
    r"""Return exact relation rows for selected ideal generators.

    Singular computes syzygies directly for polynomial-ring ideals, but Sage's
    generic quotient-ring ideal forwards ``syz`` with an unsupported quotient
    parent.  For ``R=S/J`` and ``I=(f_1,...,f_n)`` we instead compute syzygies
    of ``(f_1,...,f_n,J)`` in ``S`` and project the first ``n`` coordinates to
    ``R``.  This projection is exactly ``ker(R^n -> I)``: a tuple ``a`` is a
    relation modulo ``J`` iff ``sum a_i f_i`` is a linear combination of the
    generators of ``J``.
    """
    engine = _engine_ring(ring)
    match engine:
        case SageNumberFieldOrder():
            return _order_ideal_syzygy_rows(engine, selected)
        case QuotientRing_generic():
            cover = engine.cover_ring()
            defining = engine.defining_ideal()
            lifted = tuple(engine(generator).lift() for generator in selected)
            augmented = cover.ideal(lifted + tuple(defining.gens()))
            syzygies = augmented.syzygy_module()

            rows = tuple(
                tuple(
                    engine(syzygies[position, column])
                    for column in range(len(selected))
                )
                for position in range(syzygies.nrows())
            )
            zero = engine.zero()
            return tuple(
                row
                for row in rows
                if any(coefficient != zero for coefficient in row)
            )
        case _:
            method = _optional_engine_method(backend, "syzygy_module")
            if method is None:
                return None
            syzygies = method()

    return tuple(
        tuple(syzygies[position, column] for column in range(syzygies.ncols()))
        for position in range(syzygies.nrows())
    )


def _order_ideal_syzygy_rows(order, selected):
    r"""Return relation rows for the generators of an ideal of a number-field order.

    ``O`` is free of finite rank over ``ZZ`` on the engine's integral basis
    ``b_1..b_n``, so ``ker(O^k -> O, (a_i) |-> sum a_i g_i)`` is the integer
    left kernel of the ``nk x n`` matrix whose rows are the ``ZZ``-coordinates
    of the products ``g_i b_j``; each kernel basis vector, read in blocks of
    ``n``, is one relation ``(a_1, ..., a_k)`` in ``O``.
    """
    basis = tuple(order(element) for element in order.basis())
    rank = len(basis)
    images = matrix(
        SageZZ,
        [
            [SageZZ(coordinate) for coordinate in order.coordinates(order(generator) * element)]
            for generator in selected
            for element in basis
        ],
    )
    return tuple(
        tuple(
            sum(
                coefficient * element
                for coefficient, element in zip(
                    relation[position * rank : (position + 1) * rank], basis, strict=True
                )
            )
            for position in range(len(selected))
        )
        for relation in images.left_kernel().basis()
    )


def _relation_element(free_module, row):
    return free_module.linear_combination(
        {
            label: coefficient
            for label, coefficient in zip(
                free_module.module_generating_set(), row, strict=True
            )
            if coefficient
        }
    )


def _from_engine_ideal(ring, engine_ideal):
    r"""Return the owned ideal of ``R`` generated by an engine ideal's generators.

    The generators arrive as engine values and cross back through the ring
    before reaching its ideal constructor, which is a public one and refuses
    raw backend elements.
    """
    source = _own_ring(ring)
    return source.ideal(
        *(_owned_engine_value(source, generator) for generator in engine_ideal.gens())
    )


def _engine_ring_value(ring, value):
    r"""Cross one ring element to the private engine of ``ring``."""
    source = _own_ring(ring)
    engine = _engine_ring(source)
    parent = getattr(value, "parent", lambda: None)()
    if parent is engine:
        return engine(value)
    return engine(_engine_element(source, source(value)))


def _owned_engine_value(ring, value):
    r"""Cross one private engine value back into the owned ring."""
    source = _own_ring(ring)
    engine_value = _engine_ring(source)(value)
    ambient_ring = getattr(source, "ambient_ring", None)
    if callable(ambient_ring):
        return source(_owned_engine_element(ambient_ring(), engine_value))
    return _owned_engine_element(source, engine_value)


def _flat_extension_commutative_ideal(source_ideal, morphism):
    r"""Return ``I S`` by scalar-extending a finite presentation along a flat map.

    If ``R -> S`` is flat, tensoring the exact presentation of ``I <= R``
    with ``S`` remains exact, so the resulting presented ``S``-module is the
    image ideal generated by the transported generators.  Completion of a
    Noetherian ring is the consumer of this route; it avoids asking a formal
    power-series backend to recompute syzygies it does not expose.
    """
    source = source_ideal.ring()
    if morphism.domain() is not source:
        raise ValueError("a flat ideal extension starts at the ideal's ring")
    target = morphism.codomain()
    source_generators = tuple(source_ideal.ideal_generators())
    target_generators = tuple(morphism(generator) for generator in source_generators)
    if len(source_generators) <= 1:
        return target.ideal(*target_generators)
    changed = source_ideal.base_change(morphism)
    labels = tuple(changed.module_generating_set())
    if len(labels) != len(target_generators):
        raise ArithmeticError("scalar extension changed the selected ideal framing")

    ambient_module = target.regular_module()
    target_engine = _engine_ring(target)
    backend = target_engine.ideal(
        tuple(_engine_element(target, generator) for generator in target_generators)
    )
    generator_images = {
        label: ambient_module((target_generators[position],))
        for position, label in enumerate(labels)
    }
    construction_data = {
        "engine_ideal": backend,
        "ideal_generators": target_generators,
    }
    if changed not in ModulesWithChosenFinitePresentation(target):
        return target._fresh_free_module_on(
            changed.module_generating_set(),
            _subobject_ambient=ambient_module,
            _subobject_generator_images=generator_images,
            _extra_categories=(CommutativeIdeals(target),),
            _extra_construction_data=construction_data,
        )
    return ModulesWithChosenFinitePresentation(target)(
        changed.presentation(),
        subobject_ambient=ambient_module,
        subobject_generator_images=generator_images,
        category=Category.join((CommutativeIdeals(target),)),
        **construction_data,
    )


@cached_function
def _commutative_ideal(source, generators):
    r"""Return the one ideal of ``R`` built from this generating family.

    An ideal is determined by its ring and its elements, so two calls that
    write the same generators name one subobject and get one object.  The key
    is the family as written: ``(2)`` and ``(2,4)`` are equal ideals but reach
    two entries here, and they compare equal afterwards.
    """
    engine = _engine_ring(source)
    values = tuple(_engine_ring_value(source, generator) for generator in generators)
    if not values:
        values = (engine.zero(),)
    backend = engine.ideal(values)
    selected = tuple(backend.gens())
    syzygy_rows = _engine_ideal_syzygy_rows(source, backend, selected)
    if syzygy_rows is None:
        assert source in OwnedRings().Commutative().NoZeroDivisors() and len(selected) == 1, (
            "ideal construction without a syzygy backend requires one principal generator in an integral domain"
        )

        generator = selected[0]
        ambient_module = source.regular_module()
        if generator == engine.zero():
            ideal = source._fresh_free_module_on(
                Sets.Δ[-1],
                _subobject_ambient=ambient_module,
                _subobject_generator_images={},
                _extra_categories=(CommutativeIdeals(source),),
                _extra_construction_data={
                    "engine_ideal": backend,
                    "ideal_generators": (
                        _owned_engine_value(source, generator),
                    ),
                },
            )
        else:
            ideal = source._fresh_free_module_on(
                Sets.Δ[0],
                _subobject_ambient=ambient_module,
                _subobject_generator_images={
                    0: ambient_module((_owned_engine_value(source, generator),))
                },
                _extra_categories=(CommutativeIdeals(source),),
                _extra_construction_data={
                    "engine_ideal": backend,
                    "ideal_generators": (
                        _owned_engine_value(source, generator),
                    ),
                },
            )
        return ideal

    labels = finite_ordered_set(range(len(selected)))
    relation_labels = finite_ordered_set(range(len(syzygy_rows)))
    free_generators = source.free_module(labels)
    free_relations = source.free_module(relation_labels)
    presentation = free_relations.module_category().Mor(free_relations, free_generators)(
        {
            label: _relation_element(
                free_generators,
                tuple(
                    _owned_engine_value(source, coefficient)
                    for coefficient in syzygy_rows[position]
                ),
            )
            for position, label in enumerate(relation_labels)
        }
    )
    ambient_module = source.regular_module()
    ideal = ModulesWithChosenFinitePresentation(source)(
        presentation,
        subobject_ambient=ambient_module,
        subobject_generator_images={
            label: ambient_module((_owned_engine_value(source, selected[position]),))
            for position, label in enumerate(labels)
        },
        category=Category.join((CommutativeIdeals(source),)),
        **{
            "engine_ideal": backend,
            "ideal_generators": tuple(
                _owned_engine_value(source, generator)
                for generator in selected
            ),
        },
    )
    return ideal


__all__ = ["CommutativeIdeals"]
