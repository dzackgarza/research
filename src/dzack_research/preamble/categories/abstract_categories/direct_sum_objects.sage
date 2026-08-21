r"""Objects equipped with a chosen ordered direct-sum decomposition."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from sage.categories.modules import Module

from dzack_research.preamble.categories.sets.sets import finite_ordered_set
from collections.abc import Iterable
from typing import Self, TYPE_CHECKING

from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.owned_category import ConstructionData


def _is_subobject(source: "Module") -> bool:
    r"""Return whether ``source`` is a module carrying a chosen embedding.

    ``source`` is also called with elements and with lists of images.  An
    element's category is ``Elements(P)``, never \(P\)'s own, and a list has
    no category at all, so both answer no.
    """
    # Local: at module level this closes an import cycle; the subobject module
    # is built by the time a decomposition is asked about one.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobjects

    return source in Subobjects()


class DirectSumObjects(Category):
    r"""Pairs \((M,(M_i)_i)\) with a chosen ordered direct-sum structure."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "objects with a direct-sum decomposition"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        # Installed on the object by the constructor: the ordered summands
        # and the set indexing them.
        _summands: tuple
        _summand_index_set: "OrderedSet"

        # No ``underlying_object``/``module_generating_set``/``rank``/
        # ``group`` here.  ``group_modules`` refines a module *in place* into
        # this category, and on that object those names must keep answering
        # from the module's own category; a delegation through
        # ``_underlying_object`` would shadow them with an attribute only the
        # ``DirectSumObject`` wrapper has.  A decomposition contributes the
        # summands and nothing else.

        def summands(self: Self) -> tuple:
            summands: tuple = self._summands
            return summands

        def summand_index_set(self: Self) -> "OrderedSet":
            return self._summand_index_set

        def summand(self: Self, label: "Element") -> "Module":
            assert label in self._summand_index_set, (
                f"{label!r} is not a summand label"
            )
            return self._summands[self._summand_index_set.position(label)]

        def __init__(
            self: Self,
            underlying_object: "Module",
            summands: "OrderedSet",
            summand_index_set: "OrderedSet",
            **rest: "ConstructionData",
        ) -> None:
            self._underlying_object = underlying_object
            self._summands = tuple(summands)
            self._summand_index_set = summand_index_set
            assert summand_index_set.cardinality() == len(self._summands), (
                "the summand-indexing set and summand family have different sizes"
            )
            super().__init__(**rest)

        def _repr_(self: Self) -> str:
            return (
                f"{self._underlying_object} with {len(self._summands)} "
                "chosen summands"
            )


def DirectSumDecomposition(
    underlying_object: "Module",
    summands: "OrderedSet",
    summand_index_set: "OrderedSet | None" = None,
) -> Parent:
    r"""Return the decomposition \(M=\bigoplus_i M_i\) of an object already in hand.

    This asserts of \(M\) that the given family decomposes it; it does not
    build \(\bigoplus_i M_i\) out of anything.  ``DirectSum`` is the
    construction --- the biproduct of the summands, read off its projections
    and injections --- and lives in ``products.sage``.  The two are different
    operations even though in \(R\)-**Mod** they name the same object: one
    starts from the structure morphisms and produces the apex, the other
    starts from the apex and records a chosen splitting of it.
    """
    summands = tuple(summands)
    match summand_index_set:
        case None:
            summand_index_set = Sets.Δ[len(summands) - 1]
        case Parent() | Iterable():
            summand_index_set = finite_ordered_set(
                summand_index_set
            )
        case _:
            assert False, (
                "a summand index set is a finite set or finite iterable"
            )
    return object_of(
        DirectSumObjects(),
        underlying_object=underlying_object,
        summands=summands,
        summand_index_set=summand_index_set,
    )


def _direct_sum_assignment_pairs(source: "Module", target: "Module") -> tuple:
    r"""Expand one declared summand assignment into generator-image pairs."""
    source_is_subobject = _is_subobject(source)
    target_is_subobject = _is_subobject(target)

    # ``embedded_module_generators`` is an ordered set, not a sequence: it
    # answers ``cardinality`` and has no ``len``.  Pairing source generators
    # with target images is positional, so the order is read out into a tuple
    # here, at the one boundary where position is what is wanted.
    match source_is_subobject, target_is_subobject, target:
        case True, True, _:
            source_images = tuple(source.embedded_module_generators())
            target_images = tuple(target.embedded_module_generators())
        case True, False, list() | tuple():
            source_images = tuple(source.embedded_module_generators())
            target_images = tuple(target)
        case True, False, _:
            source_images = tuple(source.embedded_module_generators())
            assert len(source_images) == 1, (
                "one target element requires a rank-one source"
            )
            target_images = (target,)
        case False, True, _:
            assert target.rank() == 1, (
                "a target subobject must have rank one"
            )
            return ((source, tuple(target.embedded_module_generators())[0]),)
        case False, False, list() | tuple():
            assert False, (
                "a list of target images requires a source subobject"
            )
        case False, False, _:
            return ((source, target),)

    assert len(source_images) == len(target_images), (
        "source and target image counts differ"
    )
    return tuple(zip(source_images, target_images, strict=True))


def _expand_direct_sum_hom_dict(domain: "Module", mapping: dict) -> list:
    r"""Expand a summand-level assignment to one image per domain generator."""
    images = dict(
        pair
        for source, target in mapping.items()
        for pair in _direct_sum_assignment_pairs(source, target)
    )
    # Keyed by the summands' embedded generators, which are elements of the
    # domain -- not by the framing labels, which for an iterated direct sum
    # are nested index tuples and name no element.
    return [images[generator] for generator in domain.module_generators()]
