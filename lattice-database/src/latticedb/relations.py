"""Derived information from relations between stored lattice records."""

from collections.abc import Sequence

from latticedb.corpus import Entry
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


def hyperbolic_index_bounds(entries: Sequence[Entry]) -> dict[str, int]:
    """Return the largest stored embedding U^n -> T for each target T."""
    by_tag = {entry.lattice.tag: entry.lattice for entry in entries}
    bounds: dict[str, int] = {}
    for entry in entries:
        source = entry.lattice
        planes = hyperbolic_planes(source)
        if planes is None:
            continue
        for morphism in source.morphisms:
            if morphism.scale == 1 and morphism.target in by_tag:
                bounds[morphism.target] = max(
                    planes, bounds.get(morphism.target, 0)
                )
    return bounds
