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

from dzack_research.preamble.lexicon.interop import SageParent, SageUniqueRepresentation
from dzack_research.preamble.categories.sets.cardinals import Cardinal
from dzack_research.preamble.categories.sets.owned_sets import Sets, placement_of

if TYPE_CHECKING:
    from sage.categories.morphism import SetMorphism
    from sage.rings.integer import Integer
    from sage.structure.parent import ElementConstructorInput

_E = TypeVar("_E")

if TYPE_CHECKING:
    class _StructuredParent(SageParent[_E], Generic[_E]):
        _underlying_set: UnderlyingSet[_E]
        def cardinality(self) -> Cardinal: ...
        def __iter__(self) -> Iterator[_E]: ...

    _UnderlyingSetParent = SageParent[_E]
else:
    _StructuredParent = SageParent
    _UnderlyingSetParent = SageParent

class UnderlyingSet(SageUniqueRepresentation, _UnderlyingSetParent, Generic[_E]):
    r"""The underlying set ``U(X)`` of a structured parent: same elements,
    structure forgotten.

    ``U`` is the object half of the forgetful functor right adjoint to the
    free functor, so it must be well defined on objects: ``U(X)`` has to
    *be* the codomain of ``U(f)`` for every ``f`` out of ``X``, not merely
    an equal copy.  ``UniqueRepresentation`` keys on ``X``, and refining
    ``X`` into a subcategory changes that key while leaving the object --
    and its elements -- the same.  The answer is therefore kept on ``X``
    itself, where no refinement can reach it.
    """

    @staticmethod
    def __classcall__(
        cls: type[UnderlyingSet[_E]],
        structured: SageParent[_E],
    ) -> UnderlyingSet[_E]:
        structured_parent = cast(_StructuredParent, structured)
        stored = getattr(structured_parent, "_underlying_set", None)
        if stored is not None:
            return cast(UnderlyingSet[_E], stored)
        underlying = super().__classcall__(cls, structured)
        try:
            structured_parent._underlying_set = underlying
        except AttributeError:
            # A Cython parent carries no instance dictionary and so cannot
            # hold the answer; it also cannot be refined, which is the only
            # thing that moves the key, so its key is already fixed.
            pass
        return underlying

    if TYPE_CHECKING:
        # The generic set surface is injected by the owned Sets() axiom
        # categories at parent construction; every UnderlyingSet lives in
        # those axioms, so the surface is a real invariant of the class.
        def is_countable(self) -> bool: ...
        def is_uncountable(self) -> bool: ...
        def index(self, element: _E) -> int: ...
        def __getitem__(self, n: int) -> _E: ...
        def enumeration_injection(self) -> SetMorphism[_E, Integer]: ...

    def __init__(self, structured: SageParent[_E]) -> None:
        self._structured = cast(_StructuredParent, structured)
        SageParent.__init__(self, facade=structured, category=placement_of(structured).Facade())

    def cardinality(self) -> Cardinal:
        r"""Return $|U(X)|$.

        Cardinality is total on sets, so the structured parent answers it.
        The former fallbacks read a generating set instead -- which counts
        generators, not elements, and answers a different question.
        """
        return self._structured.cardinality()

    def is_finite(self) -> bool:
        r"""Return whether $U(X)$ is finite.

        Concrete for the same reason as :meth:`cardinality`: the axiom
        categories inject this surface only when the facade placement carries
        the axiom, so a set whose placement does not is left unable to answer
        a question every set has an answer to. Forgetting structure does not
        change the elements, so the structured parent decides it.
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


class ViaUnderlyingSet(Generic[_E]):
    r"""The forwarding owner's parent methods: every generic set behavior
    of a structured parent is the corresponding behavior of its underlying
    set. Installed at each structured root (the operation roots, the G-set root) and nowhere below."""

    def underlying_set(self) -> UnderlyingSet[_E]:
        r"""The set ``U(X)`` underlying this structured parent: the same
        elements with the operations forgotten — the single functorial
        obligation everything else rolls up through."""
        return UnderlyingSet(cast(_StructuredParent, self))

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
