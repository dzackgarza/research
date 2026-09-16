r"""Kähler differentials of represented commutative algebras."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.algebras.derivations import (
    Derivation,
    _commutative_presentation_data,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _presented_module_from_morphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


class _KahlerDifferentialConstruction:
    r"""The selected algebra and conormal data defining one differential module."""

    def __init__(
        self,
        source_algebra,
        *,
        conormal_module=None,
        ambient_differentials=None,
        conormal_morphism=None,
    ) -> None:
        self._source_algebra = source_algebra
        self._conormal_module = conormal_module
        self._ambient_differentials = ambient_differentials
        self._conormal_morphism = conormal_morphism

    def source_algebra(self):
        return self._source_algebra

    def conormal_module(self):
        return self._conormal_module

    def ambient_differentials(self):
        return self._ambient_differentials

    def conormal_morphism(self):
        return self._conormal_morphism


class KahlerDifferentialModules(OwnedCategoryOverBaseRing):
    r"""Selected modules ``Omega^1_{A/R}`` for the coefficient algebra ``A``."""

    def an_object(self):
        r"""``Omega^1_{A/R}`` for the coefficient algebra ``A`` of this category."""
        return self(self.base_ring())

    def _call_(self, algebra):
        r"""Construct ``Omega^1_{A/R}`` from the algebra ``A`` itself.

        ``KahlerDifferentialModules(A)`` is a category of ``A``-modules, so
        the parameter and the source algebra are definitionally the same
        object.  Localization and conormal-sequence realizations are private
        branches of this constructor; ``A.kahler_differentials()`` is the
        algebra's spelling of it.
        """
        if algebra is not self.base_ring():
            raise ValueError(
                "KahlerDifferentialModules(A) constructs the differentials of that same algebra A"
            )
        cached = _KAHLER_DIFFERENTIAL_CACHE.get(id(algebra))
        if cached is not None and cached.source_algebra() is algebra:
            return cached
        result = _construct_kahler_differentials(algebra)
        _KAHLER_DIFFERENTIAL_CACHE[id(algebra)] = result
        return result

    @classmethod
    def _repr_object_names(cls):
        return "Kähler differential modules"

    def super_categories(self):
        return [ModulesWithChosenFinitePresentation(self.base_ring())]

    class ParentMethods:
        def __init__(self, kahler_construction, **rest) -> None:
            self._kahler_construction = kahler_construction
            super().__init__(**rest)

        def kahler_construction(self):
            return self._kahler_construction

        def source_algebra(self):
            return self.kahler_construction().source_algebra()

        def conormal_module(self):
            r"""Return ``A tensor_P I ~= I/I^2`` for the selected quotient ``P -> A``."""

            conormal = self.kahler_construction().conormal_module()
            assert conormal is not None, (
                "conormal_module requires selected quotient-presentation conormal data"
            )
            return conormal

        def ambient_differentials(self):
            r"""Return ``Omega^1_{P/R} tensor_P A`` in the selected conormal sequence."""

            ambient = self.kahler_construction().ambient_differentials()
            assert ambient is not None, (
                "ambient_differentials requires selected quotient-presentation differential data"
            )
            return ambient

        def conormal_morphism(self):
            r"""Return ``I/I^2 -> Omega^1_{P/R} tensor_P A``, ``f |-> df``."""

            morphism = self.kahler_construction().conormal_morphism()
            assert morphism is not None, (
                "conormal_morphism requires selected quotient-presentation conormal data"
            )
            return morphism

        def differential_projection(self):
            r"""Return the quotient map onto ``Omega^1_{A/R}`` in the conormal sequence."""

            self.conormal_morphism()
            return self.cokernel_projection()

        @cached_method
        def cotangent_space(self, point):
            r"""Return ``Omega^1_{A/R} tensor_A kappa(point)``."""

            algebra = self.source_algebra()
            spectrum = algebra.spectrum()
            if getattr(point, "parent", lambda: None)() is not spectrum:
                point = spectrum(point)
            # The cotangent fiber is canonically the direct scalar extension
            # Omega^1_{A/R} tensor_A kappa(p); no localization realization is
            # needed to define or compute this selected fiber.
            return self.base_change(point.residue_map())

        @cached_method
        def tangent_space(self, point):
            r"""Return the relative Zariski tangent space dual to ``cotangent_space(point)``."""


            algebra = self.source_algebra()
            spectrum = algebra.spectrum()
            if getattr(point, "parent", lambda: None)() is not spectrum:
                point = spectrum(point)
            cotangent = self.cotangent_space(point)
            return cotangent.module_category().Mor(
                cotangent,
                point.residue_field().regular_module(),
            )

        def tangent_dimension(self, point):
            r"""Return the dimension of the relative Zariski tangent space."""

            return self.cotangent_space(point).dimension()

        def conormal_morphism_at(self, point):
            r"""Base-change the selected conormal map to ``kappa(point)``."""

            algebra = self.source_algebra()
            spectrum = algebra.spectrum()
            if getattr(point, "parent", lambda: None)() is not spectrum:
                point = spectrum(point)
            return self.conormal_morphism().base_change(point.residue_map())

        @cached_method
        def universal_derivation(self):
            algebra = self.source_algebra()
            generator_algebra = (
                algebra.localization_source()
                if algebra in LocalizationRings()
                else algebra
            )
            return algebra.derivations(self)(
                {
                    label: self.differential_generator(label)
                    for label in generator_algebra.algebra_generating_set()
                }
            )

        def differential_generator(self, algebra_generator_label):
            return self.module_generator(("d", algebra_generator_label))

        def from_derivation(self, derivation):
            if not isinstance(derivation, Derivation):
                raise TypeError("the universal factorization starts from a derivation")
            if derivation.domain() is not self.source_algebra():
                raise ValueError("the derivation has the wrong source algebra")

            return self.module_category().Mor(self, derivation.codomain())(
                {
                    ("d", label): derivation.generator_image(label)
                    for label in derivation.parent().generator_labels()
                }
            )

        def non_smooth_locus(self, relative_dimension):
            r"""Return ``V(Fitt_d(Omega^1_{A/R}))`` for the supplied relative dimension ``d``.

            The ``d``-th Fitting ideal of a finitely presented module cuts out
            exactly the points where its rank exceeds ``d``.  On an algebra of
            finite type over a field, of relative dimension ``d``, the
            differentials have rank at least ``d`` everywhere and rank exactly
            ``d`` where the algebra is smooth, so this closed set is the
            singular locus.

            The relative dimension is a supplied datum, not a reading of the
            presentation: local dimension and component data are properties of
            the algebra and are not determined by its module of differentials.
            """

            from dzack_research.preamble.categories.rings.ring_foundation import OwnedFields

            algebra = self.base_ring()
            assert algebra.base_ring() in OwnedFields(), (
                "the Fitting-ideal criterion for the singular locus is stated here "
                f"for an algebra of finite type over a field, and {algebra} has "
                f"scalars {algebra.base_ring()}"
            )
            return algebra.spectrum().V(self.fitting_ideal(relative_dimension))

        def derivation_classifier_isomorphism(self, target_module):
            r"""Return ``Hom_A(Omega^1_{A/R},M) ~= Der_R(A,M)`` as an ``A``-module isomorphism."""

            algebra = self.source_algebra()
            if target_module.base_ring() is not algebra:
                raise TypeError("the Kähler representing property targets an A-module")
            classifiers = self.module_category().Mor(self, target_module)
            assert classifiers in ModulesWithChosenFinitePresentation(algebra), (
                "the represented Kähler Hom-Der isomorphism requires a selected finite presentation of Hom_A(Omega^1,M)"
            )
            derivations = algebra.derivations(target_module)
            if derivations not in ModulesWithChosenFinitePresentation(algebra):
                raise TypeError(
                    "the represented Kähler classifier must construct Der_R(A,M) "
                    "with its chosen finite presentation"
                )

            forward = classifiers.module_category().Mor(classifiers, derivations)(
                derivations.module_generator
            )
            inverse = derivations.module_category().Mor(derivations, classifiers)(
                classifiers.module_generator
            )
            result = Modules(algebra).Core().Mor(classifiers, derivations)(forward, inverse)
            if result not in Modules(algebra).Iso(classifiers, derivations):
                raise ArithmeticError(
                    "the represented Kähler classifier maps failed to define an A-module isomorphism"
                )
            return result

        representing_isomorphism = derivation_classifier_isomorphism


_KAHLER_DIFFERENTIAL_CACHE = {}


def _construct_kahler_differentials(algebra):
    r"""Private realization selected by ``KahlerDifferentialModules(A)(A)``."""
    if algebra in LocalizationRings():
        source = algebra.localization_source()
        if source.base_ring() is not algebra.base_ring():
            raise ValueError(
                "localization of differentials requires the localization to preserve the algebra base"
            )
        source_omega = source.kahler_differentials()
        from dzack_research.preamble.categories.modules.localizations import (
            _localized_module,
        )

        # Localization is an algebra base change A -> S^{-1}A and Kähler
        # differentials commute with it:
        #
        #   Omega^1_{S^{-1}A/R} = S^{-1}A tensor_A Omega^1_{A/R}.
        #
        # Choose that localized module itself as the represented differential
        # object.  Its _localized_modules data therefore retains the comparison
        # source and localization unit rather than merely recording an
        # isomorphic but unrelated presentation.
        return _localized_module(
            source_omega,
            algebra,
            algebra.localization_functor(),
            extra_categories=(KahlerDifferentialModules(algebra),),
            extra_construction_data={
                "kahler_construction": _KahlerDifferentialConstruction(algebra)
            },
        )

    presentation, labels, _variables, relations, _lift = _commutative_presentation_data(
        algebra
    )
    differential_labels = finite_ordered_set(
        tuple(("d", label) for label in labels)
    )
    if relations.cardinality() != 0:
        presentation_ideal = presentation.ideal(*tuple(relations))
        presentation_omega = presentation.kahler_differentials()
        presentation_derivation = presentation_omega.universal_derivation()
        ideal_generators = dict(
            zip(
                presentation_ideal.module_generating_set(),
                presentation_ideal.ideal_generators(),
                strict=True,
            )
        )
        quotient_map = algebra.algebra_presentation_morphism()
        scalar_extension = Modules(quotient_map.domain()).scalar_extension(quotient_map)
        conormal_module = scalar_extension(presentation_ideal)
        ambient_differentials = algebra.free_module(differential_labels)

        def conormal_image(label):
            differential = presentation_derivation(ideal_generators[label])
            coefficients = presentation_omega.framing_coefficients(differential)
            return ambient_differentials.linear_combination(
                {
                    differential_label: quotient_map(coefficient)
                    for differential_label, coefficient in coefficients.items()
                    if coefficient
                }
            )

        conormal_morphism = conormal_module.module_category().Mor(conormal_module, ambient_differentials)(conormal_image)
        relation_module = algebra._fresh_free_module_on(
            conormal_module.module_generating_set(),
        )
        relation_map = relation_module.module_category().Mor(relation_module, ambient_differentials)(conormal_morphism.module_generator_images().value)
        omega = _presented_module_from_morphism(
            relation_map,
            _cokernel_morphism=relation_map,
            _extra_categories=(KahlerDifferentialModules(algebra),),
            _extra_construction_data={
                "kahler_construction": _KahlerDifferentialConstruction(
                    algebra,
                    conormal_module=conormal_module,
                    ambient_differentials=ambient_differentials,
                    conormal_morphism=conormal_morphism,
                ),
            },
        )
    else:
        omega = algebra._fresh_free_module_on(
            differential_labels,
            _extra_categories=(KahlerDifferentialModules(algebra),),
            _extra_construction_data={
                "kahler_construction": _KahlerDifferentialConstruction(algebra)
            },
        )
    return omega


__all__ = ["KahlerDifferentialModules"]
