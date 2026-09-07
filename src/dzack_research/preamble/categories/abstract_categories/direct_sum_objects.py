r"""Objects equipped with a chosen finite direct-sum decomposition."""

from collections.abc import Iterable
from typing import TypeVar

from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.cardinals import cardinal


LabelT = TypeVar("LabelT")


class DirectSumObjects(OwnedCategory):
    r"""Objects carrying a selected ordered family of direct summands."""

    def an_object(self) -> Parent:
        r"""``R (+) R`` over the integers, decomposed into its two summands."""
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            BasedFreeModule,
        )
        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set
        from sage.rings.integer_ring import ZZ as SageZZ

        ring = _own_ring(SageZZ)
        summand = BasedFreeModule(ring, finite_ordinal_set(1))
        return Modules(ring).biproduct([summand, summand])

    def super_categories(self):
        return [Objects()]

    class ParentMethods:
        def __init__(self, summands: IndexedFamily, **rest) -> None:
            if not isinstance(summands, IndexedFamily):
                raise TypeError("a selected direct-sum decomposition is an indexed family")
            self._preamble_direct_sum_summands = summands
            self._preamble_direct_sum_index_set = summands.index_set()
            super().__init__(**rest)

        def summands(self) -> IndexedFamily:
            return self._preamble_direct_sum_summands

        def summand_index_set(self) -> Parent:
            return self._preamble_direct_sum_index_set

        def summand(self, label: LabelT) -> Parent:
            labels = self.summand_index_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a summand label")
            return self.summands()[label]

        def number_of_summands(self) -> Parent:
            return self.summand_index_set().cardinality()


def DirectSumDecomposition(
    underlying_object: Parent,
    summands: IndexedFamily | Iterable[Parent],
    summand_index_set: Parent | None = None,
) -> Parent:
    r"""Verify the constructor-owned decomposition ``underlying_object = ⊕ M_i``.

    Direct-sum data is construction data, so this accessor never equips an
    already existing parent.  It only verifies that the stated family agrees
    with the decomposition selected by that parent's constructor.
    """
    if isinstance(summands, IndexedFamily):
        if summand_index_set is not None and summands.index_set() is not summand_index_set:
            raise ValueError("an indexed summand family already owns its index set")
        family = summands
        labels = family.index_set()
    else:
        values = tuple(summands)
        labels = (
            Sets.Δ[len(values) - 1]
            if summand_index_set is None
            else finite_ordered_set(summand_index_set)
        )
        if labels.cardinality() != cardinal(len(values)):
            raise ValueError("the summand family and its index set have different cardinalities")
        family = indexed_family(
            labels,
            lambda label: values[int(labels.ranking_map()(label))],
            name=f"Direct summands of {underlying_object}",
        )

    if underlying_object not in DirectSumObjects():
        raise ValueError(
            "direct-sum decomposition data must be supplied by the object's constructor"
        )
    selected = underlying_object.summands()
    selected_labels = underlying_object.summand_index_set()
    if labels != selected_labels:
        raise ValueError("the stated summand labels differ from the constructor-owned labels")
    if any(selected[label] is not family[label] for label in labels):
        raise ValueError("the stated summands differ from the constructor-owned summands")
    return underlying_object



__all__ = ["DirectSumDecomposition", "DirectSumObjects"]
