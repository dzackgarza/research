r"""Objects equipped with a chosen finite direct-sum decomposition."""

from sage.categories.category import Category

from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.refine import refine


class DirectSumObjects(Category):
    r"""Objects carrying a selected ordered family of direct summands."""

    def super_categories(self):
        return [Objects()]

    class ParentMethods:
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
    if cardinal(summands.cardinality()) != cardinal(2):
        return False
    left = summands.unrank(0)
    right = summands.unrank(1)
    try:
        represented = underlying_object.biproduct_factors()
        return represented.unrank(0) is left and represented.unrank(1) is right
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

    from dzack_research.preamble.categories.abstract_categories.constructions import Biproduct

    biproduct = Biproduct(left, right)
    map_to_object = biproduct.from_summands(left_inclusion, right_inclusion)
    try:
        return map_to_object.is_injective() and map_to_object.is_surjective()
    except (AttributeError, NotImplementedError):
        return False


def DirectSumDecomposition(underlying_object, summands, summand_index_set=None):
    r"""Equip ``underlying_object`` with the selected decomposition ``⊕ M_i``.

    This does not construct a new direct sum. It records an indexed family of
    summands of an object already in hand, after verifying the represented
    binary universal map when that is the active backend.
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
        if cardinal(labels.cardinality()) != cardinal(len(values)):
            raise ValueError("the summand family and its index set have different cardinalities")
        family = indexed_family(
            labels,
            lambda label: values[int(labels.rank(label))],
            name=f"Direct summands of {underlying_object}",
        )

    size = cardinal(family.cardinality())
    if size == cardinal(2) and not _binary_decomposition_is_valid(underlying_object, family):
        raise ValueError(
            "the represented backend cannot verify that the stated family is a direct-sum decomposition"
        )
    if size == cardinal(1):
        only = family.unrank(0)
        if only is not underlying_object:
            try:
                inclusion = only.inclusion()
            except AttributeError as error:
                raise ValueError("a one-summand decomposition must be the object itself") from error
            if inclusion.codomain() is not underlying_object or not inclusion.is_surjective():
                raise ValueError("the stated one summand does not equal the object")
    underlying_object._preamble_direct_sum_summands = family
    underlying_object._preamble_direct_sum_index_set = labels
    return refine(underlying_object, DirectSumObjects())



__all__ = ["DirectSumDecomposition", "DirectSumObjects"]
