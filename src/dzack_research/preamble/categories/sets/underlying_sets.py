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

from collections.abc import Iterator
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
    from sage.structure.parent import ElementConstructorInput

    from dzack_research.preamble.owned_category import ConstructionData

_E = TypeVar("_E")

if TYPE_CHECKING:
    class _StructuredParent(SageParent[_E], Generic[_E]):
        _underlying_set: SageParent[_E]
        def cardinality(self) -> Cardinal: ...
        def __iter__(self) -> Iterator[_E]: ...

    class _UnderlyingSetSurface(SageParent[_E], Generic[_E]):
        r"""What ``U(X)`` answers: this level's methods, plus the generic
        set surface the owned ``Sets()`` axioms of its placement supply."""

        def cardinality(self) -> Cardinal: ...
        def is_finite(self) -> bool: ...
        def is_countable(self) -> bool: ...
        def is_uncountable(self) -> bool: ...
        def index(self, element: _E) -> int: ...
        def __getitem__(self, n: int) -> _E: ...
        def structured_parent(self) -> _StructuredParent[_E]: ...
        def enumeration_injection(self) -> SetMorphism[_E, Integer]: ...


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
            self, structured: SageParent[_E], **rest: ConstructionData
        ) -> None:
            self._structured = cast("_StructuredParent[_E]", structured)
            super().__init__(facade=structured, **rest)

        def cardinality(self) -> Cardinal:
            r"""Return $|U(X)|$.

            Cardinality is total on sets, so the structured parent answers it.

            ``U`` is where a Sage-structured parent enters the owned sets, so it
            is where its count enters the owned cardinals: Sage answers with a raw
            ``Integer`` or ``+Infinity``, which are elements of a ring and of an
            extended scalar line and answer none of the questions a cardinal does.
            The single conversion is here, at the crossing.

            ``+Infinity`` is where Sage's line stops and the cardinals begin: it
            is a single point, while above it sit $\aleph_0$, $2^{\aleph_0}$ and
            the rest, which the extended scalar line does not tell apart.  Which
            one it is, is a fact about $X$, so a bare ``+Infinity`` determines a
            cardinal only for a countable $X$, where it is $\aleph_0$.  Anything
            else has to say its own size: an uncountable set is not thereby of the
            continuum, and guessing would assert a theorem (the continuum
            hypothesis, in the worst case) that nobody proved.  A parent that
            knows states its count and never arrives here -- which is what the
            owned rings do, naming their countable engines and reading a
            completion as being of the continuum (``rings.sage``).
            """
            counted = self._structured.cardinality()
            if isinstance(counted, Cardinal) or counted != Infinity:
                return cardinal(counted)
            assert "Countable" in placement_of(self._structured).axioms(), (
                f"{self._structured} answers +Infinity and does not declare itself "
                f"countable, so its cardinal is not determined -- every infinite "
                f"cardinal lies above that one point of the extended scalars. "
                f"State the count on the parent, or declare its countability."
            )
            return cardinal(counted)

        def is_finite(self) -> bool:
            r"""Return whether $U(X)$ is finite.

            Forgetting structure does not change the elements, so the
            structured parent decides it.
            """
            return bool(self.cardinality().is_finite())

        def _repr_(self) -> str:
            return f"Underlying set of {self._structured}"

        def structured_parent(self) -> _StructuredParent[_E]:
            r"""The structured parent this set underlies."""
            return self._structured

        def _element_constructor_(self, element: ElementConstructorInput) -> _E:
            r"""U(X) has the same elements as X: conversion into the facade IS
            the host's conversion. Without this, Sage's generic conversion
            discovery wanders into the structured parent's homset machinery
            (surfaced by the #197 route audit's morphism-action check)."""
            return self._structured(element)

        def __iter__(self) -> Iterator[_E]:
            # The structured parent's enumeration is its witness data, supplied
            # dynamically; the static Parent surface cannot see it.
            return iter(self._structured)

        def __contains__(self, x: ElementConstructorInput) -> bool:
            return x in self._structured


@cached_function
def _underlying_set_of(structured: SageParent[_E]) -> SageParent:
    r"""Build ``U(X)`` over the owned placement its structured parent carries."""
    placement = placement_of(structured).Facade()
    return object_of(UnderlyingSets(placement), structured=structured)


def UnderlyingSet(structured: SageParent[_E]) -> _UnderlyingSetSurface[_E]:
    r"""Return the set ``U(X)`` underlying the structured parent ``X``.

    The answer is kept on ``X`` itself.  A refinement of ``X`` leaves the
    object -- and its elements -- the same, and reaches no attribute of ``X``.
    """
    stored = getattr(structured, "_underlying_set", None)
    if stored is None:
        stored = _underlying_set_of(structured)
        try:
            structured._underlying_set = stored
        except AttributeError:
            # A Cython parent carries no instance dictionary and so cannot
            # hold the answer; it also cannot be refined, so the cache above
            # already gives one object per parent.
            pass
    return cast("_UnderlyingSetSurface[_E]", stored)


class ViaUnderlyingSet(Generic[_E]):
    r"""The forwarding owner's parent methods: every generic set behavior
    of a structured parent is the corresponding behavior of its underlying
    set. Installed at each structured root (the operation roots, the G-set root) and nowhere below."""

    def underlying_set(self) -> _UnderlyingSetSurface[_E]:
        r"""The set ``U(X)`` underlying this structured parent: the same
        elements with the operations forgotten — the single functorial
        obligation everything else rolls up through."""
        return UnderlyingSet(cast("_StructuredParent[_E]", self))

    def cardinality(self) -> Cardinal:
        return self.underlying_set().cardinality()

    def is_finite(self) -> bool:
        return self.underlying_set().is_finite()

    def is_infinite(self) -> bool:
        return not self.underlying_set().is_finite()

    def is_countable(self) -> bool:
        return self.underlying_set().is_countable()

    def is_uncountable(self) -> bool:
        return self.underlying_set().is_uncountable()

    def index(self, element: _E) -> int:
        return self.underlying_set().index(element)
