"""Torsion modules and the finitely-presented torsion specialization."""

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
    _own_ring,
)
class TorsionModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "torsion modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_torsion(self) -> bool:
            return True


class FinitelyPresentedTorsionModules(OwnedCategoryOverBaseRing):
    r"""Finitely presented torsion modules over a PID."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented torsion modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            FinitelyPresentedModules,
        )

        return [
            FinitelyPresentedModules(self.base_ring()),
            TorsionModules(self.base_ring()),
        ]

    class ParentMethods:
        def is_torsion(self) -> bool:
            return True

        @cached_method
        def elements(self):
            r"""Return all elements through the private finite Smith workspace."""
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                finite_ordered_image,
            )
            from dzack_research.preamble.categories.sets.set_categories import Sets

            if _engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError(
                    "finite enumeration is currently the ZZ torsion specialization"
                )
            engine = self._smith_engine()
            if engine is None:
                raise NotImplementedError(
                    "finite torsion enumeration requires the represented Smith workspace"
                )
            positions = Sets.Δ[int(engine.cardinality()) - 1]
            return finite_ordered_image(
                positions,
                lambda position: self._from_smith_engine_element(
                    engine[int(position)]
                ),
                name="Finite torsion elements",
            )

        def __iter__(self):
            return iter(self.elements())

    def direct_sum_of_cyclics(self, orders):
        if _engine_ring(self.base_ring()) is not SageZZ:
            raise NotImplementedError(
                "direct sums by integer orders are currently the ZZ specialization"
            )
        ring = self.base_ring()
        orders = tuple(ring(order) for order in orders)
        if any(order <= ring.one() for order in orders):
            raise ValueError("cyclic summand orders must be greater than one")
        size = len(orders)
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace

        relations = MatrixSpace(
            ring,
            size,
            size,
        ).from_rows(
            tuple(
                tuple(
                    order if row == column else ring.zero()
                    for column in range(size)
                )
                for row, order in enumerate(orders)
            )
        )
        return _torsion_module_presented_by_matrix(relations)


def _torsion_module_presented_by_matrix(relations, module_generating_set=None):
    r"""Return the ``ZZ``-module presented by relation rows ``relations``."""
    from dzack_research.preamble.categories.modules.pure.modules import MatrixSpaces
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        BasedFreeModule,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.sets.finite_ordered_sets import (
        finite_ordered_set,
    )

    ring = _own_ring(SageZZ)
    try:
        relation_parent = relations.parent()
    except AttributeError:
        relation_parent = None
    represented_matrix = (
        relation_parent is not None and relation_parent in MatrixSpaces(ring)
    )
    if represented_matrix:
        width = relations.parent().ncols()
        relation_count = relations.parent().nrows()
    else:
        rows = tuple(tuple(row) for row in relations)
        relation_count = len(rows)
        width = 0 if not rows else len(rows[0])
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace

        relations = MatrixSpace(ring, relation_count, width).from_rows(rows)
        represented_matrix = True
    labels = (
        finite_ordered_set(range(width))
        if module_generating_set is None
        else finite_ordered_set(module_generating_set)
    )
    if labels.cardinality() != width:
        raise ValueError(
            "the module-generating set and relation matrix have different widths"
        )
    target = BasedFreeModule(ring, labels)
    source = BasedFreeModule(ring, relation_count)

    def relation_entry(row_position, column_position):
        row_label = relations.parent().row_index_set().unrank(row_position)
        column_label = relations.parent().column_index_set().unrank(column_position)
        return relations.matrix_entry(row_label, column_label)

    def relation_image(row_position):
        return target.linear_combination(
            {
                label: relation_entry(row_position, column_position)
                for column_position, label in enumerate(labels)
                if relation_entry(row_position, column_position)
            }
        )

    images = {
        source_label: relation_image(row_position)
        for row_position, source_label in enumerate(source.module_generating_set())
    }
    return TorsionModule(module_homset(source, target)(images))


def TorsionModule(presentation):
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
    )

    return refine_finitely_presented_torsion_module(
        FinitelyPresentedModule(presentation)
    )


def refine_finitely_presented_torsion_module(module):
    r"""Attach the torsion intersection after verifying the represented property."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModules,
    )
    from dzack_research.preamble.refine import refine

    ring = module.base_ring()
    if module not in FinitelyPresentedModules(ring):
        raise TypeError("torsion refinement requires a finitely presented module")
    if not module.is_torsion():
        raise ValueError(
            "the supplied finite presentation does not present a torsion module"
        )
    return refine(module, FinitelyPresentedTorsionModules(ring))


__all__ = [
    "FinitelyPresentedTorsionModules",
    "TorsionModule",
    "TorsionModules",
    "refine_finitely_presented_torsion_module",
]
