r"""Objects of a category with a chosen finite direct-sum decomposition.

For a category ``C`` with finite biproducts, an object of ``DirectSumObjects(C)``
is an object ``X`` of ``C`` together with a chosen indexed family of summands
whose biproduct in ``C`` is ``X``.  The injections and projections of that
decomposition are morphisms of ``C``, so the notion is relative to ``C``: an
orthogonal decomposition of a lattice is a decomposition in ``Lattices(R)``,
and the decomposition of its underlying module is its image in
``Modules(R)``.  Forgetting the choice lands in ``C`` itself, which is the one
declaration this construction makes.
"""

from collections.abc import Iterable
from typing import TypeVar

from sage.categories.category import Category
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets

LabelT = TypeVar("LabelT")


class DirectSumObjects(OwnedCategory):
    r"""Objects of ``C`` carrying a selected ordered family of direct summands."""

    @staticmethod
    def __classcall__(cls, base_category: Category):
        return Category.__classcall__(cls, base_category)

    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        OwnedCategory.__init__(self)

    def base_category(self) -> Category:
        r"""The category ``C`` in which the biproducts are taken."""
        return self._base_category

    def _repr_object_names(self):
        return f"objects of {self.base_category()._repr_object_names()} with a chosen direct-sum decomposition"

    def an_object(self) -> Parent:
        r"""``X (+) X`` for an object ``X`` of ``C``, decomposed into its two summands."""
        witness = self.base_category().an_object()
        return self.base_category().biproduct((witness, witness))

    def super_categories(self):
        return [self.base_category()]

    def verify_decomposition(
        self,
        underlying_object: Parent,
        summands: IndexedFamily | Iterable[Parent],
        summand_index_set: Parent | None = None,
    ) -> Parent:
        r"""Verify the constructor-owned decomposition ``underlying_object = ⊕ M_i``."""
        match summands:
            case IndexedFamily():
                if summand_index_set is not None and summands.index_set() is not summand_index_set:
                    raise ValueError("an indexed summand family already owns its index set")
                family = summands
                labels = family.index_set()
            case _:
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

        if underlying_object not in self:
            raise ValueError(
                "direct-sum decomposition data must be supplied by the object's constructor"
            )
        # An object placed here answers its decomposition by this category's
        # own accessors; the decomposition is its constructor datum.
        selected = underlying_object.summands()
        selected_labels = underlying_object.summand_index_set()
        if labels != selected_labels:
            raise ValueError("the stated summand labels differ from the constructor-owned labels")
        if any(selected[label] is not family[label] for label in labels):
            raise ValueError("the stated summands differ from the constructor-owned summands")
        return underlying_object

    class ParentMethods:
        def __init__(self, summands: IndexedFamily, **rest) -> None:
            match summands:
                case IndexedFamily():
                    pass
                case _:
                    raise TypeError("a selected direct-sum decomposition is an indexed family")
            self._preamble_direct_sum_summands = summands
            super().__init__(**rest)

        def summands(self) -> IndexedFamily:
            return self._preamble_direct_sum_summands

        def summand_index_set(self) -> Parent:
            return self.summands().index_set()

        def summand(self, label: LabelT) -> Parent:
            labels = self.summand_index_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a summand label")
            return self.summands()[label]

        def number_of_summands(self) -> Parent:
            return self.summand_index_set().cardinality()

__all__ = ["DirectSumObjects"]
