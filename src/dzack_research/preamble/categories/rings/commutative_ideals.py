"""Finitely generated commutative ideals as module subobjects of the ring."""

from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.arrow_categories import SubobjectsOf
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedIntegralDomains,
    OwnedCategoryOverBaseRing,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
    FreshFreeModuleOn,
    ring_as_module,
)
from dzack_research.preamble.categories.modules.localizations import (
    LocalizedModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    ModuleSubobjects,
    Modules,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def _localized_commutative_ideal(source_ideal, localization_ring):
    r"""Return ``S^{-1}I <= S^{-1}R``, the localization of one ideal."""
    from dzack_research.preamble.categories.functors.module_localization import (
        module_localization_functor,
    )

    localization_map = localization_ring.localization_map()
    source_regular_module = ring_as_module(source_ideal.ring())
    target_regular_module = ring_as_module(localization_ring)
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
        coefficient = module_coefficients(source_image, source_regular_module).get(
            source_regular_label,
            source_ideal.ring().zero(),
        )
        return target_regular_module.scalar_multiple(
            localization_map(coefficient),
            target_regular_module.module_generator(target_regular_label),
        )

    ideal = LocalizedModule(
        source_ideal,
        localization_ring,
        module_localization_functor(localization_ring),
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

        return [Modules(self.base_ring())]

    def subobject_category(self):

        ring = self.base_ring()
        return SubobjectsOf(Modules(ring), ring_as_module(ring))

    def __contains__(self, candidate) -> bool:
        try:
            if candidate.base_ring() is not self.base_ring():
                return False
        except (AttributeError, TypeError):
            return False
        return candidate in self.subobject_category()

    class ParentMethods:
        def __init__(
            self,
            ideal_generators=None,
            engine_ideal=None,
            localization_source_ideal=None,
            **rest,
        ) -> None:
            if ideal_generators is not None:
                self._preamble_ideal_generators = tuple(ideal_generators)
            if engine_ideal is not None:
                self._preamble_engine_ideal = engine_ideal
            if localization_source_ideal is not None:
                self._preamble_localization_source_ideal = localization_source_ideal
            super().__init__(**rest)

        def ring(self):
            return self.base_ring()

        def ideal_generators(self):
            return self._preamble_ideal_generators

        def __eq__(self, other):
            try:
                return (
                    other in CommutativeIdeals(self.ring())
                    and self._engine_ideal() == other._engine_ideal()
                )
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                return False

        def __ne__(self, other):
            return not self == other

        def _richcmp_(self, other, op):
            if op not in (op_EQ, op_NE):
                return NotImplemented
            equal = self == other
            return equal if op == op_EQ else not equal

        def __eq__(self, other) -> bool:
            try:
                return bool(
                    other in CommutativeIdeals(self.ring())
                    and self._engine_ideal() == other._engine_ideal()
                )
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                return False

        def __ne__(self, other) -> bool:
            return not self == other

        def _engine_ideal(self):
            represented = getattr(self, "_preamble_engine_ideal", None)
            if represented is not None:
                return represented
            engine = _engine_ring(self.ring())
            if engine is self.ring():
                raise NotImplementedError(
                    "this ideal has no active engine-ideal realization"
                )
            try:
                return engine.ideal(
                    tuple(
                        _engine_element(self.ring(), generator)
                        for generator in self.ideal_generators()
                    )
                )
            except (AttributeError, NotImplementedError, TypeError, ValueError) as error:
                raise NotImplementedError(
                    "this ideal has no active engine-ideal realization"
                ) from error

        def extension_to_localization(self, localization_ring):
            r"""Return the represented localization ``S^{-1}I <= S^{-1}R``."""
            if localization_ring not in LocalizationRings():
                raise TypeError("ideal localization requires a represented ring localization")
            if localization_ring.localization_source() is not self.ring():
                raise ValueError("the localization has the wrong source ring")
            return _localized_commutative_ideal(self, localization_ring)

        extension = extension_to_localization

        def is_prime(self):
            return bool(self._engine_ideal().is_prime())

        def is_maximal(self):
            return bool(self._engine_ideal().is_maximal())

        def radical(self):
            return _from_engine_ideal(self.ring(), self._engine_ideal().radical())

        def colon(self, other):
            r"""Return the ideal quotient ``(self : other)`` when the backend supports it."""
            _require_same_ring(self, other)
            method = _engine_ideal_method(
                self,
                "quotient",
                "this ideal backend has no colon/ideal-quotient operation",
            )
            return _from_engine_ideal(self.ring(), method(other._engine_ideal()))

        ideal_quotient = colon

        def saturation(self, other):
            r"""Return ``(self : other^infinity)`` when the backend supports it."""
            _require_same_ring(self, other)
            method = _engine_ideal_method(
                self,
                "saturation",
                "this ideal backend has no saturation operation",
            )
            result = method(other._engine_ideal())
            saturated = result[0] if isinstance(result, tuple) else result
            return _from_engine_ideal(self.ring(), saturated)

        def contraction_from_localization(self):
            r"""Contract this selected localized extension back to its source ring."""
            source_ideal = self.__dict__.get("_preamble_localization_source_ideal")
            if source_ideal is None:
                raise NotImplementedError(
                    "contraction is currently represented for ideals selected as localization extensions"
                )
            localization_ring = self.ring()
            submonoid = localization_ring.localization_submonoid()
            try:
                generators = tuple(submonoid.monoid_generators())
            except NotImplementedError as error:
                raise NotImplementedError(
                    "contraction from this localization requires a represented finite generating set for the localization submonoid"
                ) from error
            if not generators:
                return source_ideal

            source_ring = localization_ring.localization_source()
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
                return source_ring.ideal(source_ring._from_engine_element(engine(generator)))

            raise NotImplementedError(
                "this source ideal backend has neither saturation nor a supported PID fallback"
            )

        contraction = contraction_from_localization

        def contains_ambient_element(self, element) -> bool:
            r"""Return whether an ambient ring element lies in this ideal."""
            ring = self.ring()
            value = ring(element)
            if (
                ring in LocalizationRings()
                and self.__dict__.get("_preamble_localization_source_ideal") is not None
            ):
                numerator, _denominator = ring.localization_fraction_data(value)
                contracted = self.contraction_from_localization()
                return _engine_ring_value(contracted.ring(), numerator) in contracted._engine_ideal()
            try:
                return _engine_element(ring, value) in self._engine_ideal()
            except NotImplementedError as error:
                raise NotImplementedError(
                    "ambient ideal membership has no active backend in this regime"
                ) from error

        def __contains__(self, candidate) -> bool:
            if getattr(candidate, "parent", lambda: None)() is self:
                return True
            try:
                return self.contains_ambient_element(candidate)
            except (TypeError, ValueError):
                return False

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

        def syzygy_matrix(self):
            return self._engine_ideal().syzygy_module()

        def primary_decomposition(self):
            method = _engine_ideal_method(
                self,
                "primary_decomposition",
                "this ideal backend has no primary decomposition",
            )
            return tuple(_from_engine_ideal(self.ring(), ideal) for ideal in method())

        def associated_primes(self):
            method = _engine_ideal_method(
                self,
                "associated_primes",
                "this ideal backend has no associated-prime computation",
            )
            return tuple(_from_engine_ideal(self.ring(), ideal) for ideal in method())

        def _repr_(self):
            listed = ", ".join(str(generator) for generator in self.ideal_generators())
            return f"Ideal ({listed}) of {self.ring()}"


def _require_same_ring(left, right):
    if left.ring() is not right.ring():
        raise ValueError("ideal arithmetic requires one ambient ring")


def _optional_engine_method(engine, name):
    r"""Return one optional operation of a private computational realization."""
    return getattr(engine, name, None)


def _engine_ideal_method(ideal, name, unavailable_message):
    r"""Resolve an optional ideal-engine operation only at the private boundary."""
    method = _optional_engine_method(ideal._engine_ideal(), name)
    if method is None:
        raise NotImplementedError(unavailable_message)
    return method


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
    source = _own_ring(ring)
    return source.ideal(*tuple(engine_ideal.gens()))


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
    ambient = getattr(source, "_ambient_ring", None)
    if ambient is not None:
        return source(ambient._from_engine_element(engine_value))
    return source._from_engine_element(engine_value)


def CommutativeIdeal(ring, *generators):
    r"""Return ``(generators) <= R`` with its selected module inclusion."""
    source = _own_ring(ring)
    engine = _engine_ring(source)
    if len(generators) == 1 and isinstance(generators[0], (tuple, list)):
        generators = tuple(generators[0])
    values = tuple(_engine_ring_value(source, generator) for generator in generators)
    if not values:
        values = (engine.zero(),)
    backend = engine.ideal(values)
    selected = tuple(backend.gens())
    if not hasattr(backend, "syzygy_module"):
        if source not in OwnedIntegralDomains() or len(selected) != 1:
            raise NotImplementedError(
                "this ideal has no selected exact module-presentation backend"
            )

        generator = selected[0]
        ambient_module = ring_as_module(source)
        if generator == engine.zero():
            ideal = FreshFreeModuleOn(
                source,
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
            ideal = FreshFreeModuleOn(
                source,
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
    syzygies = backend.syzygy_module()

    labels = finite_ordered_set(range(len(selected)))
    relation_labels = finite_ordered_set(range(int(syzygies.nrows())))
    free_generators = BasedFreeModule(source, labels)
    free_relations = BasedFreeModule(source, relation_labels)
    presentation = module_homset(free_relations, free_generators)(
        {
            label: _relation_element(
                free_generators,
                tuple(
                    _owned_engine_value(source, syzygies[position, column])
                    for column in range(syzygies.ncols())
                ),
            )
            for position, label in enumerate(relation_labels)
        }
    )
    ambient_module = ring_as_module(source)
    ideal = FinitelyPresentedModule(
        presentation,
        _subobject_ambient=ambient_module,
        _subobject_generator_images={
            label: ambient_module((_owned_engine_value(source, selected[position]),))
            for position, label in enumerate(labels)
        },
        _extra_categories=(CommutativeIdeals(source),),
        _extra_construction_data={
            "engine_ideal": backend,
            "ideal_generators": tuple(
                _owned_engine_value(source, generator)
                for generator in selected
            ),
        },
    )
    return ideal


__all__ = ["CommutativeIdeal", "CommutativeIdeals"]
