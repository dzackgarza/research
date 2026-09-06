r"""Objects equipped with a chosen finite direct-sum decomposition."""

from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.abstract_categories.constructions import Biproduct


class DirectSumObjects(OwnedCategory):
    r"""Objects carrying a selected ordered family of direct summands."""

    def an_object(self):
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
        def __init__(self, summands, **rest) -> None:
            if not isinstance(summands, IndexedFamily):
                raise TypeError("a selected direct-sum decomposition is an indexed family")
            self._preamble_direct_sum_summands = summands
            self._preamble_direct_sum_index_set = summands.index_set()
            super().__init__(**rest)

        def summands(self):
            return self._preamble_direct_sum_summands

        def summand_index_set(self):
            return self._preamble_direct_sum_index_set

        def summand(self, label):
            labels = self.summand_index_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a summand label")
            return self.summands()[label]

        def number_of_summands(self):
            return self.summand_index_set().cardinality()


def _binary_decomposition_is_valid(underlying_object, summands) -> bool:
    if summands.cardinality() != cardinal(2):
        return False
    left = summands[0]
    right = summands[1]
    try:
        represented = underlying_object.biproduct_factors()
        return represented[0] is left and represented[1] is right
    except (AttributeError, TypeError, ValueError):
        pass

    try:
        left_inclusion = left.inclusion()
        right_inclusion = right.inclusion()
    except AttributeError:
        return False
    if (
        left_inclusion.codomain() is not underlying_object
        or right_inclusion.codomain() is not underlying_object
    ):
        return False


    biproduct = Biproduct(left, right)
    map_to_object = biproduct.from_summands(left_inclusion, right_inclusion)
    try:
        return map_to_object.is_injective() and map_to_object.is_surjective()
    except (AttributeError, NotImplementedError):
        return False


def DirectSumDecomposition(underlying_object, summands, summand_index_set=None):
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

    size = family.cardinality()
    if size == cardinal(2) and not _binary_decomposition_is_valid(underlying_object, family):
        raise ValueError(
            "the represented backend cannot verify that the stated family is a direct-sum decomposition"
        )
    if size == cardinal(1):
        only = family[0]
        if only is not underlying_object:
            try:
                inclusion = only.inclusion()
            except AttributeError as error:
                raise ValueError("a one-summand decomposition must be the object itself") from error
            if inclusion.codomain() is not underlying_object or not inclusion.is_surjective():
                raise ValueError("the stated one summand does not equal the object")

    selected = underlying_object.__dict__.get("_preamble_direct_sum_summands")
    selected_labels = underlying_object.__dict__.get("_preamble_direct_sum_index_set")
    if selected is None or selected_labels is None:
        raise ValueError(
            "direct-sum decomposition data must be supplied by the object's constructor"
        )
    if labels != selected_labels:
        raise ValueError("the stated summand labels differ from the constructor-owned labels")
    if any(selected[label] is not family[label] for label in labels):
        raise ValueError("the stated summands differ from the constructor-owned summands")
    return underlying_object



__all__ = ["DirectSumDecomposition", "DirectSumObjects"]
