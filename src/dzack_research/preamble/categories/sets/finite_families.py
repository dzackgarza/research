"""Finite indexed families on the canonical finite ordinal."""

from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def finite_family(values, *, name=None):
    r"""Return the family over \(\Delta[k-1]\) taking the stated values in order.

    A finite sequence of owned values is a family, not a set: two of them may be
    equal, which a set would collapse, and each is addressed by its position.
    """
    if isinstance(values, IndexedFamily):
        return values
    entries = tuple(values)
    positions = Sets.Δ[len(entries) - 1]
    return indexed_family(
        positions,
        lambda position: entries[int(position)],
        name=name,
    )


__all__ = ["finite_family"]
