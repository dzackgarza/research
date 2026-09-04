r"""Kähler differentials of represented commutative algebras."""

from sage.misc.cachefunc import cached_function
from dzack_research.preamble.categories.algebras.derivations import (
    Derivation,
    Derivations,
    _commutative_presentation_data,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.abstract_categories.arrow_categories import Isomorphism
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
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


class KahlerDifferentialModules(OwnedCategoryOverBaseRing):
    r"""Selected modules ``Omega^1_{A/R}`` for the coefficient algebra ``A``."""

    @classmethod
    def _repr_object_names(cls):
        return "Kähler differential modules"

    def super_categories(self):

        return [
            FinitelyPresentedModules(self.base_ring()),
            FramedModules(self.base_ring()),
        ]

    class ParentMethods:
        def source_algebra(self):
            return self._preamble_source_algebra

        algebra = source_algebra

        def universal_derivation(self):
            return self._preamble_universal_derivation

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

            def to_derivation(classifier):
                return derivations(
                    {
                        label: classifier(self.differential_generator(label))
                        for label in derivations.generator_labels()
                    }
                )

            def to_classifier(derivation):
                return self.from_derivation(derivation)

            # Transport the already-computed internal-Hom presentation to the
            # actual derivation parent.  This adds coordinates to the same
            # derivation object; it does not create a second Der_R carrier.
            if derivations.__dict__.get("_preamble_kahler_classifier_module") is None:
                derivations._preamble_module_generating_set = (
                    classifiers.module_generating_set()
                )
                derivations._preamble_relation_matrix = classifiers.presentation_matrix()
                derivations._preamble_presentation = classifiers.presentation()
                derivations._preamble_module_generator_function = (
                    lambda label: to_derivation(classifiers.module_generator(label))
                )
                derivations._preamble_module_coefficient_function = (
                    lambda derivation: module_coefficients(
                        to_classifier(derivation),
                        classifiers,
                    )
                )
                derivations._preamble_kahler_classifier_module = classifiers
                refine(
                    derivations,
                    ModulesWithChosenFinitePresentation(algebra),
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
    presentation, labels, variables, relations, _lift = _commutative_presentation_data(
        algebra
    )
    differential_labels = finite_ordered_image(
        labels,
        lambda label: ("d", label),
    )


    free_differentials = BasedFreeModule(algebra, differential_labels)
    if relations.cardinality():
        relation_indices = relations.index_set()
        relation_module = BasedFreeModule(algebra, relation_indices)
        presentation_engine = _engine_ring(presentation)
        algebra_engine = _engine_ring(algebra)

        def relation_image(relation_index):
            relation = relations[relation_index]
            engine_relation = presentation._engine_element(relation)
            coefficients = {}
            for differential_label, variable in zip(
                differential_labels,
                variables,
                strict=True,
            ):
                engine_variable = presentation._engine_element(variable)
                coefficient = algebra._from_engine_element(
                    algebra_engine(
                        presentation_engine(engine_relation).derivative(engine_variable)
                    )
                )
                if coefficient != algebra.zero():
                    coefficients[differential_label] = coefficient
            return free_differentials.linear_combination(coefficients)

        relation_map = module_homset(relation_module, free_differentials)(relation_image)
        omega = FinitelyPresentedModule(relation_map)
    else:
        omega = free_differentials

    omega._preamble_source_algebra = algebra
    omega = refine(omega, KahlerDifferentialModules(algebra))
    universal = Derivations(algebra, omega)(
        {
            label: omega.differential_generator(label)
            for label in labels
        }
    )
    omega._preamble_universal_derivation = universal
    return omega


__all__ = ["KahlerDifferentialModules", "KahlerDifferentials"]
