r"""Scalar-extension helpers shared by owned module constructions."""

from sage.categories.map import Map

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _owned_ring,
)


def base_change_codomain(module, ring_map):
    r"""Validate ``R -> S`` against ``module`` and return the owned ring ``S``."""
    if not isinstance(ring_map, Map):
        raise TypeError("base change is specified by a ring morphism")
    if _engine_ring(ring_map.domain()) is not _engine_ring(module.base_ring()):
        raise ValueError(
            f"the scalar map starts at {ring_map.domain()}, not {module.base_ring()}"
        )
    return _owned_ring(ring_map.codomain())


def base_change_scalar(ring_map, scalar):
    r"""Apply ``R -> S`` and return the resulting element of the owned ring ``S``."""
    target = _owned_ring(ring_map.codomain())
    return target(ring_map(scalar))


__all__ = ["base_change_codomain", "base_change_scalar"]
