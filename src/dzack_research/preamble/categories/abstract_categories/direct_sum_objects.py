r"""Objects equipped with a chosen finite direct-sum decomposition."""

from sage.categories.category import Category
from sage.categories.sets_cat import Sets as SageSets

from dzack_research.preamble.categories.sets import Sets, finite_ordered_set
from dzack_research.preamble.refine import refine


class DirectSumObjects(Category):
    r"""Objects carrying a selected ordered family of direct summands."""

    def super_categories(self):
        return [SageSets()]

    class ParentMethods:
        def summands(self):
            return self._preamble_direct_sum_summands

        def summand_index_set(self):
            return self._preamble_direct_sum_index_set

        def summand(self, label):
            labels = self.summand_index_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a summand label")
            return self.summands()[labels.position(label)]

        def number_of_summands(self):
            return self.summand_index_set().cardinality()


def _binary_decomposition_is_valid(underlying_object, summands) -> bool:
    if len(summands) != 2:
        return False
    try:
        return tuple(underlying_object.biproduct_factors()) == tuple(summands)
    except AttributeError:
        pass

    left, right = summands
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

    from dzack_research.preamble.categories.abstract_categories import Biproduct

    biproduct = Biproduct(left, right)
    map_to_object = biproduct.from_summands(left_inclusion, right_inclusion)
    try:
        return map_to_object.is_injective() and map_to_object.is_surjective()
    except (AttributeError, NotImplementedError):
        return False


def DirectSumDecomposition(underlying_object, summands, summand_index_set=None):
    r"""Equip ``underlying_object`` with the selected decomposition ``⊕ M_i``.

    This does not construct a new direct sum.  It records a decomposition of an
    object already in hand, after verifying the represented binary universal
    map when that is the active backend.
    """
    family = tuple(summands)
    if summand_index_set is None:
        labels = Sets.Δ[len(family) - 1]
    else:
        labels = finite_ordered_set(summand_index_set)
    if labels.cardinality() != len(family):
        raise ValueError("the summand family and its index set have different cardinalities")
    if len(family) > 1 and not _binary_decomposition_is_valid(underlying_object, family):
        raise ValueError(
            "the represented backend cannot verify that the stated family is a direct-sum decomposition"
        )
    if len(family) == 1 and family[0] is not underlying_object:
        try:
            inclusion = family[0].inclusion()
        except AttributeError as error:
            raise ValueError("a one-summand decomposition must be the object itself") from error
        if inclusion.codomain() is not underlying_object or not inclusion.is_surjective():
            raise ValueError("the stated one summand does not equal the object")
    underlying_object._preamble_direct_sum_summands = family
    underlying_object._preamble_direct_sum_index_set = labels
    return refine(underlying_object, DirectSumObjects())


__all__ = ["DirectSumDecomposition", "DirectSumObjects"]
