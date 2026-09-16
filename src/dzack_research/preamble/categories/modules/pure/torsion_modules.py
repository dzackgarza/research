"""Torsion modules and the finitely-presented torsion specialization."""

from itertools import product

from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.categories.groups import Groups as SageGroups
from sage.matrix.constructor import matrix as engine_matrix
from sage.misc.cachefunc import cached_method
from sage.misc.misc_c import prod
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import (
    _row_normal_form,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyPresentedModules,
    MatrixSpaces,
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    PrincipalIdealDomains,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.refine import refine


class TorsionModules(OwnedCategoryOverBaseRing):
    _certifying_predicate = "is_torsion"

    def an_object(self):
        r"""The discriminant group of U, which is torsion."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U").discriminant_group()

    @classmethod
    def _repr_object_names(cls):
        return "torsion modules"

    def super_categories(self):

        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_torsion(self) -> bool:
            return True


class FinitelyPresentedTorsionModules(OwnedCategoryOverBaseRing):
    r"""Finitely presented torsion modules over a PID."""

    def an_object(self):
        r"""The discriminant group of U."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U").discriminant_group()

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented torsion modules"

    def super_categories(self):

        return [
            FinitelyPresentedModules(self.base_ring()),
            TorsionModules(self.base_ring()),
        ]

    def _call_(self, presentation):
        module = presentation.cokernel()
        if module.base_ring() is not self.base_ring():
            raise ValueError("a torsion presentation belongs to its coefficient ring")
        return _refine_finitely_presented_torsion_module(module)

    class ParentMethods:
        def is_torsion(self) -> bool:
            return True

        def invariants(self):
            r"""Return the invariant factors of this finite presented torsion module."""
            return self.invariant_factors()

        @cached_method
        def elements(self):
            r"""Return all elements through the private finite Smith workspace."""

            assert _engine_ring(self.base_ring()) is SageZZ, (
                "finite torsion enumeration is represented here in the ZZ Smith specialization"
            )
            engine = self._smith_engine()
            assert engine is not None, (
                "finite torsion enumeration requires the represented Smith workspace"
            )
            positions = Sets.Δ[int(engine.cardinality()) - 1]
            return FiniteOrderedSets().from_indexed(
                positions,
                lambda position: self._from_smith_engine_element(
                    engine[int(position)]
                ),
                name="Finite torsion elements",
            )

        def __iter__(self):
            return iter(self.elements())

    def direct_sum_of_cyclics(self, orders):
        r"""Return ``\bigoplus_i R/(a_i)`` for the selected nonzero scalars.

        Over ``ZZ`` the ``a_i`` are the usual cyclic-group orders.  Over a
        general PID the same diagonal presentation is the invariant-factor
        construction; unit entries contribute zero summands, as they should.
        A zero entry would contribute a free copy of ``R`` and hence would not
        define an object of the torsion category.
        """
        ring = self.base_ring()
        assert ring in PrincipalIdealDomains(), (
            "direct sums of cyclic torsion modules require a represented PID"
        )
        orders = tuple(ring(order) for order in orders)
        if any(order == ring.zero() for order in orders):
            raise ValueError("a cyclic torsion summand requires a nonzero relation scalar")
        orders = tuple(order for order in orders if not order.is_unit())
        size = len(orders)

        relations = ring.matrix_space(size, size).from_rows(
            tuple(
                tuple(
                    order if row == column else ring.zero()
                    for column in range(size)
                )
                for row, order in enumerate(orders)
            )
        )
        return _torsion_module_presented_by_matrix(relations, base_ring=ring)

    def from_abelian_group(self, group):
        r"""Return a finite abelian group as a torsion ``ZZ``-module presentation.

        The selected group generators remain the module-generator labels.  In
        particular a represented ``C_2 x C_3`` remains a two-generator object;
        it is not silently replaced by an isomorphic one-generator ``C_6``.
        Relations are the complete kernel of the map from the free abelian
        group on those selected generators, found inside the finite box cut out
        by their individual orders and reduced to Hermite row normal form.
        """
        assert _engine_ring(self.base_ring()) is SageZZ, (
            "finite abelian groups are represented here as ZZ-torsion modules"
        )
        if not group.is_finite():
            raise ValueError("a torsion-module crossing requires a finite group")
        additive = group.category().is_subcategory(CommutativeAdditiveGroups())
        if not additive:
            commutative = group.category().is_subcategory(SageGroups().Commutative())
            if not commutative and not bool(group.is_abelian()):
                raise ValueError("a ZZ-module crossing requires an abelian group")

        generators = tuple(group.group_generators())
        ring = self.base_ring()
        if not generators:
            return _torsion_module_presented_by_matrix(
                engine_matrix(SageZZ, 0, 0),
                finite_ordered_set(()),
                base_ring=ring,
            )
        orders = tuple(int(generator.order()) for generator in generators)
        search_size = prod(orders)
        assert search_size <= 10**6, (
            "exact relation enumeration uses the selected generator-order box only up to size 10^6; "
            "larger groups require a represented finite presentation"
        )

        if additive:
            identity = group.zero()

            def combine(exponents):
                return sum(
                    (exponent * generator for exponent, generator in zip(exponents, generators, strict=True)),
                    identity,
                )
        else:
            identity = group.one()

            def combine(exponents):
                return prod(
                    (generator**exponent for exponent, generator in zip(exponents, generators, strict=True)),
                    identity,
                )

        relation_rows = [
            exponents
            for exponents in product(*(range(order) for order in orders))
            if combine(exponents) == identity
        ]
        relation_rows.extend(
            tuple(order if row == column else 0 for column in range(len(orders)))
            for row, order in enumerate(orders)
        )
        relations = engine_matrix(SageZZ, relation_rows)
        reduced = _row_normal_form(relations, include_zero_rows=True)
        full_rank_rows = reduced.matrix_from_rows(tuple(range(len(generators))))
        return _torsion_module_presented_by_matrix(
            full_rank_rows,
            finite_ordered_set(generators),
            base_ring=ring,
        )


def _torsion_module_presented_by_matrix(
    relations, module_generating_set=None, *, base_ring=None
):
    r"""Return the torsion module presented by relation rows ``relations``."""

    ring = _own_ring(SageZZ) if base_ring is None else base_ring
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

        relations = ring.matrix_space(relation_count, width).from_rows(rows)
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
    target = ring.free_module(labels)
    source = ring.free_module(relation_count)

    def relation_entry(row_position, column_position):
        row_label = relations.parent().row_index_set()[row_position]
        column_label = relations.parent().column_index_set()[column_position]
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
    return FinitelyPresentedTorsionModules(ring)(
        source.module_category().Mor(source, target)(images)
    )


def _refine_finitely_presented_torsion_module(module):
    r"""Attach the torsion intersection after verifying the represented property."""

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
    "TorsionModules",
]
