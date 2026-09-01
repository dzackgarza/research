r"""Scalar-extension helpers shared by owned module constructions."""

from sage.categories.map import Map

from dzack_research.preamble.categories.rings import engine_ring, owned_ring_view


def base_change_codomain(module, ring_map):
    r"""Validate ``R -> S`` against ``module`` and return the owned ring ``S``."""
    if not isinstance(ring_map, Map):
        raise TypeError("base change is specified by a ring morphism")
    if engine_ring(ring_map.domain()) is not engine_ring(module.base_ring()):
        raise ValueError(
            f"the scalar map starts at {ring_map.domain()}, not {module.base_ring()}"
        )
    return owned_ring_view(ring_map.codomain())


def base_change_scalar(ring_map, scalar):
    r"""Apply the coefficient map and return its computation-ring element."""
    return engine_ring(ring_map.codomain())(ring_map(scalar))


__all__ = ["base_change_codomain", "base_change_scalar"]
