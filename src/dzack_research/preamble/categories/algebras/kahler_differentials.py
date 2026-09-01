r"""Kähler differentials of represented commutative algebras."""

from dzack_research.preamble.categories.algebras.derivations import (
    Derivation,
    Derivations,
    _commutative_presentation_data,
)
from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing, engine_ring
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class KahlerDifferentialModules(OwnedCategoryOverBaseRing):
    r"""Selected modules ``Omega^1_{A/R}`` for the coefficient algebra ``A``."""

    @classmethod
    def _repr_object_names(cls):
        return "Kähler differential modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import (
            FinitelyPresentedModules,
            FramedModules,
        )

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
            from dzack_research.preamble.categories.modules import module_homset

            return module_homset(self, derivation.codomain())(
                {
                    ("d", label): derivation.generator_image(label)
                    for label in derivation.parent().generator_labels()
                }
            )


_KAHLER_CACHE = {}


def KahlerDifferentials(algebra):
    r"""Return ``Omega^1_{A/R}`` with its universal ``R``-derivation."""
    cached = _KAHLER_CACHE.get(id(algebra))
    if cached is not None and cached.source_algebra() is algebra:
        return cached

    presentation, labels, variables, relations, _lift = _commutative_presentation_data(
        algebra
    )
    differential_labels = finite_ordered_set(("d", label) for label in labels)

    from dzack_research.preamble.categories.modules import (
        BasedFreeModule,
        FinitelyPresentedModule,
        module_homset,
    )

    free_differentials = BasedFreeModule(algebra, differential_labels)
    if relations:
        relation_labels = finite_ordered_set(range(len(relations)))
        relation_module = BasedFreeModule(algebra, relation_labels)
        presentation_engine = engine_ring(presentation)
        algebra_engine = engine_ring(algebra)
        rows = tuple(
            tuple(
                algebra_engine(presentation_engine(relation).derivative(variable))
                for variable in variables
            )
            for relation in relations
        )
        relation_map = module_homset(relation_module, free_differentials)(
            {
                relation_label: free_differentials.linear_combination(
                    {
                        differential_label: coefficient
                        for differential_label, coefficient in zip(
                            differential_labels,
                            row,
                            strict=True,
                        )
                        if coefficient
                    }
                )
                for relation_label, row in zip(
                    relation_labels,
                    rows,
                    strict=True,
                )
            }
        )
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
    _KAHLER_CACHE[id(algebra)] = omega
    return omega


__all__ = ["KahlerDifferentialModules", "KahlerDifferentials"]
