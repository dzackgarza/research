"""Derived information from relations between stored lattice records."""

from collections.abc import Sequence

from latticedb.corpus import Entry, MorphismEntry
from latticedb.model import Lattice


def hyperbolic_planes(lattice: Lattice) -> int | None:
    """Return n when ``lattice`` is the even unimodular lattice U^n."""
    if lattice.signature is None or lattice.determinant is None:
        return None
    positive, negative = lattice.signature
    if (
        lattice.integral is None
        or lattice.integral.parity != "even"
        or abs(lattice.determinant) != 1
        or positive != negative
        or positive == 0
    ):
        return None
    return positive


def hyperbolic_index_bounds(
    morphisms: Sequence[MorphismEntry], entries: Sequence[Entry]
) -> dict[str, int]:
    """Return the largest stored embedding U^n -> T for each target T."""
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    bounds: dict[str, int] = {}
    for entry in morphisms:
        record = entry.morphisms
        source = by_tag.get(record.source)
        planes = hyperbolic_planes(source) if source is not None else None
        if planes is not None and any(
            morphism.scale == 1 for morphism in record.morphisms
        ):
            bounds[record.target] = max(planes, bounds.get(record.target, 0))
    return bounds
