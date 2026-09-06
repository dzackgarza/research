r"""Kähler differentials of represented commutative algebras."""

from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.algebras.derivations import (
    Derivation,
    Derivations,
    _commutative_presentation_data,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModule,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.internal_hom import InternalHom
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyPresentedModules,
    FramedModules,
    Modules,
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
)


class KahlerDifferentialModules(OwnedCategoryOverBaseRing):
    r"""Selected modules ``Omega^1_{A/R}`` for the coefficient algebra ``A``."""

    def an_object(self):
        r"""``Omega^1_{R[x]/R}``, the differentials of the polynomial algebra.

        Kähler differentials are taken of a commutative algebra over the
        parameter.  The parameter is such an algebra over itself through the
        identity, but that placement is not represented, so the witness is the
        polynomial algebra on one generator.
        """
        from dzack_research.preamble.categories.algebras.algebras import (
            CommutativeAlgebras,
        )

        return KahlerDifferentials(CommutativeAlgebras(self.base_ring()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "Kähler differential modules"

    def super_categories(self):

        return [
            FinitelyPresentedModules(self.base_ring()),
            FramedModules(self.base_ring()),
        ]

    class ParentMethods:
        def __init__(
            self,
            source_algebra,
            conormal_module=None,
            ambient_differentials=None,
            conormal_morphism=None,
            **rest,
        ) -> None:
            self._preamble_source_algebra = source_algebra
            self._preamble_conormal_module = conormal_module
            self._preamble_ambient_differentials = ambient_differentials
            self._preamble_conormal_morphism = conormal_morphism
            super().__init__(**rest)

        def source_algebra(self):
            return self._preamble_source_algebra

        def conormal_module(self):
            r"""Return ``A tensor_P I ~= I/I^2`` for the selected quotient ``P -> A``."""

            conormal = self._preamble_conormal_module
            if conormal is None:
                raise NotImplementedError(
                    "this differential object has no selected quotient presentation conormal module"
                )
            return conormal

        def ambient_differentials(self):
            r"""Return ``Omega^1_{P/R} tensor_P A`` in the selected conormal sequence."""

            ambient = self._preamble_ambient_differentials
            if ambient is None:
                raise NotImplementedError(
                    "this differential object has no selected quotient presentation ambient differential module"
                )
            return ambient

        def conormal_morphism(self):
            r"""Return ``I/I^2 -> Omega^1_{P/R} tensor_P A``, ``f |-> df``."""

            morphism = self._preamble_conormal_morphism
            if morphism is None:
                raise NotImplementedError(
                    "this differential object has no selected quotient presentation conormal morphism"
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
            try:
                return self.fiber(point)
            except NotImplementedError:
                # The fiber is canonically the direct scalar extension along
                # A -> kappa(p).  This exact route remains available when the
                # optional localization-first realization cannot decide
                # equality of localization fractions.
                return self.base_change(point.residue_map())

        @cached_method
        def tangent_space(self, point):
            r"""Return the relative Zariski tangent space dual to ``cotangent_space(point)``."""

            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                ring_as_module,
            )

            algebra = self.source_algebra()
            spectrum = algebra.spectrum()
            if getattr(point, "parent", lambda: None)() is not spectrum:
                point = spectrum(point)
            cotangent = self.cotangent_space(point)
            return InternalHom(
                cotangent,
                ring_as_module(point.residue_field()),
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
            return Derivations(algebra, self)(
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

            return module_homset(self, derivation.codomain())(
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
            classifiers = InternalHom(self, target_module)
            if classifiers not in ModulesWithChosenFinitePresentation(algebra):
                raise NotImplementedError(
                    "the represented Kähler Hom isomorphism currently requires a finite presentation of Hom_A(Omega^1,M)"
                )
            derivations = Derivations(algebra, target_module)
            if derivations not in ModulesWithChosenFinitePresentation(algebra):
                raise TypeError(
                    "the represented Kähler classifier must construct Der_R(A,M) "
                    "with its chosen finite presentation"
                )

            forward = module_homset(classifiers, derivations)(
                derivations.module_generator
            )
            inverse = module_homset(derivations, classifiers)(
                classifiers.module_generator
            )
            result = Isomorphism(forward, inverse)
            if result not in Modules(algebra).Iso(classifiers, derivations):
                raise ArithmeticError(
                    "the represented Kähler classifier maps failed to define an A-module isomorphism"
                )
            return result

        representing_isomorphism = derivation_classifier_isomorphism


@cached_function(key=lambda algebra: id(algebra))
def KahlerDifferentials(algebra):
    r"""Return ``Omega^1_{A/R}`` with its universal ``R``-derivation."""
    if algebra in LocalizationRings():
        source = algebra.localization_source()
        if source.base_ring() is not algebra.base_ring():
            raise ValueError(
                "localization of differentials requires the localization to preserve the algebra base"
            )
        source_omega = KahlerDifferentials(source)
        from dzack_research.preamble.categories.functors.module_localization import (
            module_localization_functor,
        )
        from dzack_research.preamble.categories.modules.localizations import (
            LocalizedModule,
        )

        # Localization is an algebra base change A -> S^{-1}A and Kähler
        # differentials commute with it:
        #
        #   Omega^1_{S^{-1}A/R} = S^{-1}A tensor_A Omega^1_{A/R}.
        #
        # Choose that localized module itself as the represented differential
        # object.  Its LocalizedModules data therefore retains the comparison
        # source and localization unit rather than merely recording an
        # isomorphic but unrelated presentation.
        return LocalizedModule(
            source_omega,
            algebra,
            module_localization_functor(algebra),
            extra_categories=(KahlerDifferentialModules(algebra),),
            extra_construction_data={"source_algebra": algebra},
        )

    presentation, labels, _variables, relations, _lift = _commutative_presentation_data(
        algebra
    )
    differential_labels = finite_ordered_image(
        labels,
        lambda label: ("d", label),
    )
    if relations.cardinality() != 0:
        from dzack_research.preamble.categories.functors.scalar_change import (
            ScalarExtensionFunctor,
        )

        presentation_ideal = presentation.ideal(*tuple(relations))
        presentation_omega = KahlerDifferentials(presentation)
        presentation_derivation = presentation_omega.universal_derivation()
        ideal_generators = dict(
            zip(
                presentation_ideal.module_generating_set(),
                presentation_ideal.ideal_generators(),
                strict=True,
            )
        )
        quotient_map = algebra.algebra_presentation_morphism()
        scalar_extension = ScalarExtensionFunctor(quotient_map)
        conormal_module = scalar_extension(presentation_ideal)
        ambient_differentials = BasedFreeModule(algebra, differential_labels)

        def conormal_image(label):
            differential = presentation_derivation(ideal_generators[label])
            coefficients = module_coefficients(differential, presentation_omega)
            return ambient_differentials.linear_combination(
                {
                    differential_label: quotient_map(coefficient)
                    for differential_label, coefficient in coefficients.items()
                    if coefficient
                }
            )

        conormal_morphism = module_homset(
            conormal_module,
            ambient_differentials,
        )(conormal_image)
        relation_module = FreshFreeModuleOn(
            algebra,
            conormal_module.module_generating_set(),
        )
        relation_map = module_homset(
            relation_module,
            ambient_differentials,
        )(
            lambda label: conormal_morphism(conormal_module.module_generator(label))
        )
        omega = FinitelyPresentedModule(
            relation_map,
            _cokernel_morphism=relation_map,
            _extra_categories=(KahlerDifferentialModules(algebra),),
            _extra_construction_data={
                "source_algebra": algebra,
                "conormal_module": conormal_module,
                "ambient_differentials": ambient_differentials,
                "conormal_morphism": conormal_morphism,
            },
        )
    else:
        omega = FreshFreeModuleOn(
            algebra,
            differential_labels,
            _extra_categories=(KahlerDifferentialModules(algebra),),
            _extra_construction_data={"source_algebra": algebra},
        )
    return omega


__all__ = ["KahlerDifferentialModules", "KahlerDifferentials"]
