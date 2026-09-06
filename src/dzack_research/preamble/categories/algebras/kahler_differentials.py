r"""Kähler differentials of represented commutative algebras."""

from sage.misc.cachefunc import cached_function, cached_method
from dzack_research.preamble.categories.algebras.derivations import (
    Derivation,
    Derivations,
    _commutative_presentation_data,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
    _engine_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.categories.abstract_categories.arrow_categories import Isomorphism
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.internal_hom import InternalHom
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
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

    def an_object(self):
        r"""``Omega^1_{R[x]/R}``, the differentials of the polynomial algebra.

        Kähler differentials are taken of a commutative algebra over the
        parameter.  The parameter is such an algebra over itself through the
        identity, but that placement is not represented, so the witness is the
        polynomial algebra on one generator.
        """
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras

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
        def __init__(self, source_algebra, **rest) -> None:
            self._preamble_source_algebra = source_algebra
            super().__init__(**rest)

        def source_algebra(self):
            return self._preamble_source_algebra

        algebra = source_algebra

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

        def cotangent_space(self, point):
            r"""Return ``Omega^1_{A/R} tensor_A kappa(p)``, the cotangent space at ``p``.

            The cotangent space is the fibre of the differential module, so it
            is the module fibre already owned by finitely generated modules and
            not a second construction.  Its dimension over the residue field is
            the embedding dimension at ``p``, which is why smoothness is read
            here.
            """
            return self.fiber(point)

        def tangent_space(self, point):
            r"""Return the Zariski tangent space, the dual of the cotangent space.

            A derivation into the residue field is a ``kappa(p)``-linear map on
            the cotangent space, by the representing property of
            ``Omega^1_{A/R}``.  So the tangent space is the internal Hom of the
            cotangent space into the residue field, taken in vector spaces over
            it, and no separate model of tangent vectors is built.
            """
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                ring_as_module,
            )

            residue = point.residue_field()
            return InternalHom(self.cotangent_space(point), ring_as_module(residue))

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

    presentation, labels, variables, relations, _lift = _commutative_presentation_data(
        algebra
    )
    differential_labels = finite_ordered_image(
        labels,
        lambda label: ("d", label),
    )


    free_differentials = BasedFreeModule(algebra, differential_labels)
    if relations.cardinality() != 0:
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
        omega = FinitelyPresentedModule(
            relation_map,
            _extra_categories=(KahlerDifferentialModules(algebra),),
            _extra_construction_data={"source_algebra": algebra},
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
