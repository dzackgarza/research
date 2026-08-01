r"""Objects equipped with a chosen ordered direct-sum decomposition."""

from collections.abc import Iterable
from typing import Any

from sage.categories.category import Category
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets


class DirectSumObjects(Category):
    r"""Pairs \((M,(M_i)_i)\) with a chosen ordered direct-sum structure."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "objects with a direct-sum decomposition"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        def underlying_object(self: Any) -> Any:
            return self._underlying_object

        def summands(self: Any) -> tuple:
            return self._summands

        def summand_index_set(self: Any) -> Any:
            return self._summand_index_set

        def summand(self: Any, label: Any) -> Any:
            assert label in self._summand_index_set, (
                f"{label!r} is not a summand label"
            )
            return self._summands[self._summand_index_set.index(label)]

        def gens(self: Any) -> Any:
            return self._underlying_object.gens()

        def generating_set(self: Any) -> Any:
            return self._underlying_object.generating_set()

        def rank(self: Any) -> Any:
            return self._underlying_object.rank()

        def group(self: Any) -> Any:
            return self._underlying_object.group()

        def embedding(self: Any) -> Any:
            return self._underlying_object.embedding()


class DirectSumObject(Parent):
    r"""One object together with one chosen ordered tuple of summands."""

    def __init__(
        self,
        underlying_object: Any,
        summands: Any,
        summand_index_set: Any,
    ) -> None:
        self._underlying_object = underlying_object
        self._summands = tuple(summands)
        self._summand_index_set = summand_index_set
        assert summand_index_set.cardinality() == len(self._summands), (
            "the summand-indexing set and summand family have different sizes"
        )
        Parent.__init__(self, category=DirectSumObjects())

    def _repr_(self) -> str:
        return (
            f"{self._underlying_object} with {len(self._summands)} "
            "chosen summands"
        )


def DirectSum(
    underlying_object: Any,
    summands: Any,
    summand_index_set: Any = None,
) -> DirectSumObject:
    summands = tuple(summands)
    match summand_index_set:
        case None:
            summand_index_set = Sets.Δ[len(summands) - 1]
        case Parent() | Iterable():
            summand_index_set = finite_ordered_set(
                summand_index_set
            )
        case _:
            raise TypeError(
                "a summand index set is a finite set or finite iterable"
            )
    return DirectSumObject(
        underlying_object,
        summands,
        summand_index_set,
    )


def _direct_sum_assignment_pairs(source: Any, target: Any) -> tuple:
    r"""Expand one declared summand assignment into generator-image pairs."""
    match source in Subobjects(), target in Subobjects(), target:
        case True, True, _:
            source_images = source.embedded_gens()
            target_images = target.embedded_gens()
        case True, False, list() | tuple():
            source_images = source.embedded_gens()
            target_images = tuple(target)
        case True, False, _:
            source_images = source.embedded_gens()
            assert len(source_images) == 1, (
                "one target element requires a rank-one source"
            )
            target_images = (target,)
        case False, True, _:
            assert target.rank() == 1, (
                "a target subobject must have rank one"
            )
            return ((source, target.embedded_gens()[0]),)
        case False, False, list() | tuple():
            raise TypeError(
                "a list of target images requires a source subobject"
            )
        case False, False, _:
            return ((source, target),)

    assert len(source_images) == len(target_images), (
        "source and target image counts differ"
    )
    return tuple(zip(source_images, target_images, strict=True))


def _expand_direct_sum_hom_dict(domain: Any, mapping: dict) -> list:
    r"""Expand a summand-level assignment to the domain's framing labels."""
    images = dict(
        pair
        for source, target in mapping.items()
        for pair in _direct_sum_assignment_pairs(source, target)
    )
    return [images[generator] for generator in domain.gens()]
