"""Finitely generated commutative ideals as module subobjects of the ring."""

from dzack_research.preamble.categories.abstract_categories import SubobjectsOf
from dzack_research.preamble.categories.rings.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    own_ring,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class CommutativeIdeals(OwnedCategoryOverBaseRing):
    r"""Ideals of ``R``: subobjects of the rank-one ``R``-module ``R``."""

    def super_categories(self):
        from dzack_research.preamble.categories.modules import Modules, ring_as_module

        ring = self.base_ring()
        return [SubobjectsOf(Modules(ring), ring_as_module(ring))]

    class ParentMethods:
        def ring(self):
            return self.base_ring()

        def inclusion(self):
            return self._preamble_inclusion

        def ideal_generators(self):
            return self._preamble_ideal_generators

        gens = ideal_generators

        def _engine_ideal(self):
            represented = getattr(self, "_preamble_engine_ideal", None)
            if represented is not None:
                return represented
            engine = engine_ring(self.ring())
            if engine is self.ring():
                raise NotImplementedError(
                    "this ideal has no active engine-ideal realization"
                )
            try:
                return engine.ideal(
                    tuple(engine(generator) for generator in self.ideal_generators())
                )
            except (AttributeError, NotImplementedError, TypeError, ValueError) as error:
                raise NotImplementedError(
                    "this ideal has no active engine-ideal realization"
                ) from error

        def extension_to_localization(self, localization_ring):
            r"""Return ``S^{-1}I <= S^{-1}R`` by localizing the inclusion."""
            from dzack_research.preamble.categories.rings import LocalizationRings

            if localization_ring not in LocalizationRings():
                raise TypeError("ideal localization requires a represented ring localization")
            if localization_ring.localization_source() is not self.ring():
                raise ValueError("the localization has the wrong source ring")

            from dzack_research.preamble.categories.modules import (
                FramedModules,
                module_homset,
                ring_as_module,
            )

            localized = self.localize(localization_ring)
            localized_inclusion = localized.localization_functor()(self.inclusion())
            localized_ambient = localized_inclusion.codomain()
            standard_ambient = ring_as_module(localization_ring)
            if localized_ambient is standard_ambient:
                inclusion = localized_inclusion
            else:
                if localized_ambient not in FramedModules(localization_ring):
                    raise NotImplementedError(
                        "transporting this localized ideal to the standard rank-one module requires a represented framing"
                    )
                source_labels = tuple(localized_ambient.module_generating_set())
                target_labels = tuple(standard_ambient.module_generating_set())
                if len(source_labels) != 1 or len(target_labels) != 1:
                    raise ArithmeticError("a localized ring must be free rank one over itself")
                transport = module_homset(localized_ambient, standard_ambient)(
                    {
                        source_labels[0]: standard_ambient.module_generator(
                            target_labels[0]
                        )
                    }
                )
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                    ModuleEmbedding,
                )

                inclusion = ModuleEmbedding(
                    module_homset(localized, standard_ambient),
                    lambda element: transport(localized_inclusion(element)),
                    elementwise=True,
                    verify_linearity=False,
                )

            localized._preamble_inclusion = inclusion
            localized._preamble_ideal_generators = tuple(
                localization_ring.localization_map()(generator)
                for generator in self.ideal_generators()
            )
            localized._preamble_localization_source_ideal = self
            refine(localized, CommutativeIdeals(localization_ring))
            return localized

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
            method = getattr(self._engine_ideal(), "quotient", None)
            if method is None:
                raise NotImplementedError("this ideal backend has no colon/ideal-quotient operation")
            return _from_engine_ideal(self.ring(), method(other._engine_ideal()))

        ideal_quotient = colon

        def saturation(self, other):
            r"""Return ``(self : other^infinity)`` when the backend supports it."""
            _require_same_ring(self, other)
            method = getattr(self._engine_ideal(), "saturation", None)
            if method is None:
                raise NotImplementedError("this ideal backend has no saturation operation")
            result = method(other._engine_ideal())
            saturated = result[0] if isinstance(result, tuple) else result
            return _from_engine_ideal(self.ring(), saturated)

        def contraction_from_localization(self):
            r"""Contract this selected localized extension back to its source ring."""
            source_ideal = getattr(self, "_preamble_localization_source_ideal", None)
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
            engine = engine_ring(source_ring)
            source_backend = source_ideal._engine_ideal()
            saturation_method = getattr(source_backend, "saturation", None)
            if saturation_method is not None:
                product = engine.one()
                for generator in generators:
                    product *= engine(generator)
                result = saturation_method(engine.ideal(product))
                saturated = result[0] if isinstance(result, tuple) else result
                return _from_engine_ideal(source_ring, saturated)

            # Principal-ideal-domain fallback.  If I=(a), saturation by
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
                        gcd = generator.gcd(engine(denominator))
                        if gcd != 0 and not gcd.is_unit():
                            generator = engine(generator / gcd)
                            changed = True
                return source_ring.ideal(generator)

            raise NotImplementedError(
                "this source ideal backend has neither saturation nor a supported PID fallback"
            )

        contraction = contraction_from_localization

        def contains_ambient_element(self, element) -> bool:
            r"""Return whether an ambient ring element lies in this ideal."""
            ring = self.ring()
            value = ring(element)
            from dzack_research.preamble.categories.rings import LocalizationRings

            if ring in LocalizationRings() and hasattr(
                self, "_preamble_localization_source_ideal"
            ):
                numerator, _denominator = ring.localization_fraction_data(value)
                contracted = self.contraction_from_localization()
                return numerator in contracted._engine_ideal()
            try:
                return engine_ring(ring)(value) in self._engine_ideal()
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
            method = getattr(self._engine_ideal(), "primary_decomposition", None)
            if method is None:
                raise NotImplementedError("this ideal backend has no primary decomposition")
            return tuple(_from_engine_ideal(self.ring(), ideal) for ideal in method())

        def associated_primes(self):
            method = getattr(self._engine_ideal(), "associated_primes", None)
            if method is None:
                raise NotImplementedError("this ideal backend has no associated-prime computation")
            return tuple(_from_engine_ideal(self.ring(), ideal) for ideal in method())

        def _repr_(self):
            listed = ", ".join(str(generator) for generator in self.ideal_generators())
            return f"Ideal ({listed}) of {self.ring()}"


def _require_same_ring(left, right):
    if left.ring() is not right.ring():
        raise ValueError("ideal arithmetic requires one ambient ring")


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
    source = own_ring(ring)
    return source.ideal(*tuple(engine_ideal.gens()))


def CommutativeIdeal(ring, *generators):
    r"""Return ``(generators) <= R`` with its selected module inclusion."""
    source = own_ring(ring)
    engine = engine_ring(source)
    if len(generators) == 1 and isinstance(generators[0], (tuple, list)):
        generators = tuple(generators[0])
    values = tuple(engine(generator) for generator in generators)
    if not values:
        values = (engine.zero(),)
    backend = engine.ideal(values)
    if not hasattr(backend, "syzygy_module"):
        raise NotImplementedError(
            "the general owned ideal constructor currently requires an exact syzygy backend"
        )
    selected = tuple(backend.gens())
    syzygies = backend.syzygy_module()

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        BasedFreeModule,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.ring_as_module import (
        ring_as_module,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_embedding,
        module_homset,
    )
    labels = finite_ordered_set(range(len(selected)))
    relation_labels = finite_ordered_set(range(int(syzygies.nrows())))
    free_generators = BasedFreeModule(source, labels)
    free_relations = BasedFreeModule(source, relation_labels)
    presentation = module_homset(free_relations, free_generators)(
        {
            label: _relation_element(
                free_generators,
                tuple(syzygies[position, column] for column in range(syzygies.ncols())),
            )
            for position, label in enumerate(relation_labels)
        }
    )
    ideal = FinitelyPresentedModule(presentation)
    ambient_module = ring_as_module(source)
    inclusion = module_embedding(
        ideal,
        ambient_module,
        {
            label: ambient_module((selected[position],))
            for position, label in enumerate(labels)
        },
    )
    ideal._preamble_inclusion = inclusion
    ideal._preamble_engine_ideal = backend
    ideal._preamble_ideal_generators = tuple(source(generator) for generator in selected)
    refine(ideal, CommutativeIdeals(source))
    return ideal


__all__ = ["CommutativeIdeal", "CommutativeIdeals"]
