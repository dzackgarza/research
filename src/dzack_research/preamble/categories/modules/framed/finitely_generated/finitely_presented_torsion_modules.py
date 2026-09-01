"""Finitely presented torsion modules."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
)
from dzack_research.preamble.tensors import tensor


class FinitelyPresentedTorsionModules(OwnedCategoryOverBaseRing):
    r"""Finitely presented torsion modules over a PID."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented torsion modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            FinitelyPresentedModules,
        )
        from dzack_research.preamble.categories.modules.pure.torsion_modules import (
            TorsionModules,
        )

        return [
            FinitelyPresentedModules(self.base_ring()),
            TorsionModules(self.base_ring()),
        ]

    class ParentMethods:
        def is_torsion(self) -> bool:
            return True

        def elements(self):
            r"""Return all elements, enumerated from Smith generators."""
            from itertools import product
            from dzack_research.preamble.categories.sets import finite_ordered_set

            if engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError(
                    "finite enumeration is currently the ZZ torsion specialization"
                )
            invariants = tuple(SageZZ(n) for n in self.invariants() if SageZZ(n) > 1)
            generators = tuple(self.smith_form_module_generators())
            if len(generators) != len(invariants):
                raise RuntimeError("Smith generators and nontrivial invariant factors disagree")
            return finite_ordered_set(
                sum(
                    (coefficient * generator for coefficient, generator in zip(coefficients, generators, strict=True)),
                    self.zero(),
                )
                for coefficients in product(*(range(int(order)) for order in invariants))
            )

        def __iter__(self):
            return iter(self.elements())

    def direct_sum_of_cyclics(self, orders):
        if engine_ring(self.base_ring()) is not SageZZ:
            raise NotImplementedError(
                "direct sums by integer orders are currently the ZZ specialization"
            )
        orders = tuple(SageZZ(order) for order in orders)
        if any(order <= 1 for order in orders):
            raise ValueError("cyclic summand orders must be greater than one")
        return _torsion_module_presented_by_matrix(
            tensor.matrix.diagonal(SageZZ, orders)
        )


def _torsion_module_presented_by_matrix(relations, module_generating_set=None):
    r"""Return the ``ZZ``-module presented by relation rows ``relations``."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        BasedFreeModule,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.sets import finite_ordered_set

    relations = tensor.matrix(SageZZ, relations)
    width = relations.ncols()
    labels = (
        finite_ordered_set(range(width))
        if module_generating_set is None
        else finite_ordered_set(module_generating_set)
    )
    if labels.cardinality() != width:
        raise ValueError(
            "the module-generating set and relation matrix have different widths"
        )
    target = BasedFreeModule(SageZZ, labels)
    source = BasedFreeModule(SageZZ, relations.nrows())
    images = {
        source_label: sum(
            (
                coefficient * target.module_generator(label)
                for label, coefficient in zip(labels, row, strict=True)
                if coefficient
            ),
            target.zero(),
        )
        for source_label, row in zip(
            source.module_generating_set(), relations.rows(), strict=True
        )
    }
    return TorsionModule(module_homset(source, target)(images))


def TorsionModule(presentation):
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
    )

    module = FinitelyPresentedModule(presentation)
    if not module.is_torsion():
        raise ValueError(
            "the supplied finite presentation does not present a torsion module"
        )
    return module


__all__ = [
    "FinitelyPresentedTorsionModules",
    "TorsionModule",
]
