r"""Scalar-extension helpers shared by owned module constructions."""

from sage.categories.map import Map

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _owned_ring,
)


def _base_change_codomain(module, ring_map):
    r"""Validate ``R -> S`` against ``module`` and return the owned ring ``S``."""
    if not isinstance(ring_map, Map):
        raise TypeError(
            f"cannot extend scalars of {module} along {ring_map!r}: base change needs a ring "
            f"morphism {module.base_ring()} -> S, and {ring_map!r} is not a morphism"
        )
    if _engine_ring(ring_map.domain()) is not _engine_ring(module.base_ring()):
        raise ValueError(
            f"cannot extend scalars of {module} along {ring_map}: {module} is a module over "
            f"{module.base_ring()}, but the ring morphism starts at {ring_map.domain()}"
        )
    return _owned_ring(ring_map.codomain())


def _base_change_scalar(ring_map, scalar):
    r"""Apply ``R -> S`` and return the resulting element of the owned ring ``S``."""
    target = _owned_ring(ring_map.codomain())
    return target(ring_map(scalar))


def _base_change_element(module, changed_module, ring_map, element):
    r"""Apply the represented scalar-extension unit to one framed-module element."""
    coefficients = module.framing_coefficients(module(element))
    return changed_module.linear_combination(
        {
            label: _base_change_scalar(ring_map, coefficient)
            for label, coefficient in coefficients.items()
        }
    )
