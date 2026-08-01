r"""Objects equipped with a chosen ordered direct-sum decomposition."""

from typing import Any

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.structure.parent import Parent


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
        case _:
            summand_index_set = finite_ordered_set(
                summand_index_set
            )
    return DirectSumObject(
        underlying_object,
        summands,
        summand_index_set,
    )


def _expand_direct_sum_hom_dict(domain: Any, mapping: dict) -> list:
    r"""Expand a summand-level assignment to the domain's framing labels."""
    images = {}
    for source, target in mapping.items():
        if source in Subobjects():
            source_images = source.embedded_gens()
            if target in Subobjects():
                target_images = target.embedded_gens()
            elif isinstance(target, (list, tuple)):
                target_images = tuple(target)
            else:
                assert len(source_images) == 1, (
                    "one target element requires a rank-one source"
                )
                target_images = (target,)
            assert len(source_images) == len(target_images), (
                "source and target image counts differ"
            )
            images.update(zip(source_images, target_images))
        else:
            if target in Subobjects():
                assert target.rank() == 1, (
                    "a target subobject must have rank one"
                )
                target = target.embedded_gens()[0]
            images[source] = target
    return [images[generator] for generator in domain.gens()]
