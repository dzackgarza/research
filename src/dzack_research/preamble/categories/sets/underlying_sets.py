r"""Underlying sets: the object action of the structure-forgetting functors.

``UnderlyingSet(X)`` is the set ``U(X)`` of a structured parent ``X`` —
the same elements with the operations forgotten, realized as a facade over
``X`` and placed in the owned ``Sets()`` axioms by translating the set
axioms declared on ``X``'s category. The structured parent supplies only
its enumeration (the witness data); every generic set behavior of ``U(X)``
then resolves through CP1's owners, and structured categories forward
their set behavior here instead of inheriting it — composition, not
subcategory inclusion (a forgetful functor is faithful, not monic).
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import cast, Generic, TYPE_CHECKING, TypeVar

from sage.categories.category import Category as SageCategory
from sage.misc.cachefunc import cached_function
from sage.rings.infinity import Infinity

from dzack_research.preamble.lexicon.interop import SageParent
from dzack_research.preamble.categories.sets.cardinals import Cardinal, cardinal
from dzack_research.preamble.categories.sets.owned_sets import placement_of
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import CategoryWithParameters

if TYPE_CHECKING:
    from sage.categories.morphism import SetMorphism
    from sage.rings.integer import Integer
    from dzack_research.preamble.owned_category import ConstructionData

_E = TypeVar("_E")

if TYPE_CHECKING:
    class _StructuredParent(SageParent[_E], Generic[_E]):
        def cardinality(self) -> Cardinal: ...

    class _UnderlyingSetSurface(SageParent[_E], Generic[_E]):
        r"""What ``U(X)`` answers: this level's methods, plus the generic
        set surface the owned ``Sets()`` axioms of its placement supply."""

        def cardinality(self) -> Cardinal: ...
        def is_finite(self) -> bool: ...
        def is_countable(self) -> bool: ...
        def is_uncountable(self) -> bool: ...
        def position(self, element: _E) -> int: ...
        def __getitem__(self, n: int) -> _E: ...
        def structured_parent(self) -> _StructuredParent[_E]: ...
        def enumeration_injection(self) -> SetMorphism[_E, Integer]: ...

        def chosen_enumeration(self) -> Iterator[_E]: ...


class UnderlyingSets(CategoryWithParameters):
    r"""Sets that come with the structured parent they underlie.

    An object is the set ``U(X)`` together with ``X``.  ``U`` is the object
    half of the forgetful functor right adjoint to the free functor, so it
    must be well defined on objects: ``U(X)`` has to *be* the codomain of
    ``U(f)`` for every ``f`` out of ``X``, not merely an equal copy.  The
    construction below keeps the answer on ``X`` itself, where a refinement
    of ``X`` cannot move it.

    The parameter is the owned ``Sets()`` placement that ``X`` carries.
    Forgetting the structure keeps the elements, so ``U(X)`` is a set of that
    placement, and this category states it: the placement is its super
    category.  That statement also orders the classes -- this level answers
    before the placement does.  A join states less.  Sage orders the two
    parts of a join by axiom flags, and the placement then answers first.
    """

    def __init__(self, placement: SageCategory) -> None:
        self._placement = placement
        super().__init__()

    def super_categories(self) -> list[SageCategory]:
        return [self._placement]

    def _make_named_class_key(self, name: str) -> SageCategory:
        r"""The classes of this level depend on the placement alone."""
        return self._placement

    def _repr_object_names(self) -> str:
        return "underlying sets"

    class ParentMethods:
        r"""The set ``U(X)``: the same elements, the structure forgotten."""

        def __init__(
            self,
            structured: SageParent[_E],
            enumeration: Callable[[], Iterator[_E]] | None = None,
            **rest: ConstructionData,
        ) -> None:
            self._structured = cast("_StructuredParent[_E]", structured)
            self._enumeration = enumeration
            super().__init__(facade=structured, **rest)

        def _repr_(self) -> str:
            return f"Underlying set of {self._structured}"

        def structured_parent(self) -> _StructuredParent[_E]:
            r"""The structured parent this set underlies."""
            return self._structured

        def chosen_enumeration(self) -> Iterator[_E]:
            assert self._enumeration is not None, (
                f"{self} has no chosen enumeration"
            )
            return iter(self._enumeration())

@cached_function
def _underlying_set_of(
    structured: SageParent[_E],
    enumeration: Callable[[], Iterator[_E]] | None = None,
) -> SageParent:
    r"""Build ``U(X)`` over the owned placement its structured parent carries."""
    placement = placement_of(structured)
    counted = structured.cardinality()
    assert counted != Infinity or "Countable" in placement.axioms(), (
        f"{structured} answers +Infinity and does not declare itself countable, "
        "so its cardinal is not determined"
    )
    return object_of(
        UnderlyingSets(placement.Facade()),
        structured=structured,
        enumeration=enumeration,
        cardinality=cardinal(counted),
    )


def UnderlyingSet(
    structured: SageParent[_E],
    enumeration: Callable[[], Iterator[_E]] | None = None,
) -> _UnderlyingSetSurface[_E]:
    r"""Return the set ``U(X)`` underlying the structured parent ``X``.

    The cached construction is stable under later refinement of ``X``.
    """
    return cast(
        "_UnderlyingSetSurface[_E]",
        _underlying_set_of(structured, enumeration),
    )
