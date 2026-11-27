r"""Internal Sage ``ConditionSet`` interop for predicate-defined subobjects.

``ConditionSet`` is not a public category in this subtree.  Public construction
of predicate-defined subsets lives on ``Sets().Subobjects().Of(...)``; this file
keeps Sage's raw constructor localized behind that mathematical surface.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, cast

from sage.sets.condition_set import ConditionSet as SageConditionSet

if TYPE_CHECKING:
    from ...types import Set, SetElement, Subset


def condition_subset(
    ambient: Set,
    predicates: Sequence[Callable[[SetElement], bool]],
    *,
    names: str | tuple[str, ...] | None = None,
) -> Subset:
    r"""Return Sage's predicate-backed subset object."""
    return cast(Subset, SageConditionSet(ambient, *predicates, names=names))
