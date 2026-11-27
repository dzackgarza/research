r"""Finite actions on discriminant-form elements."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from sage.libs.gap.libgap import libgap

if TYPE_CHECKING:
    from ....types import Group, TorsionQuadraticModuleElement


def discriminant_form_orbit(
    G: Group,
    x: TorsionQuadraticModuleElement,
) -> tuple[TorsionQuadraticModuleElement, ...]:
    r"""Return ``orbit_G(x)`` as elements of the torsion quadratic module."""
    D = G.invariant_form()
    A = G.domain()
    x_gap = A(D(x)).gap()
    orbit = G.gap().Orbit(x_gap, libgap.OnPoints)
    return tuple(
        D.linear_combination_of_smith_form_gens(A(y).exponents()) for y in orbit
    )


def discriminant_form_stabilizer(
    G: Group,
    x: TorsionQuadraticModuleElement,
) -> Group:
    r"""Return ``Stab_G(x)`` as a subgroup of the original orthogonal group."""
    D = G.invariant_form()
    A = G.domain()
    x_gap = A(D(x)).gap()
    stabilizer = libgap.Stabilizer(G.gap(), x_gap, libgap.OnPoints)
    return G._subgroup_constructor(stabilizer)


def discriminant_form_stable_subset(
    G: Group,
    X: Iterable[TorsionQuadraticModuleElement],
) -> tuple[TorsionQuadraticModuleElement, ...]:
    r"""Return ``X`` after checking it is a finite subset preserved by ``G``."""
    D = G.invariant_form()
    subset = tuple(D(x) for x in X)
    for index, x in enumerate(subset):
        assert x not in subset[:index], "finite subset contains duplicate elements"
    for x in subset:
        for g in G.gens():
            assert x * g in subset, "generator does not preserve finite subset"
    return subset


def discriminant_form_subset_orbit(
    G: Group,
    X: Iterable[TorsionQuadraticModuleElement],
    x: TorsionQuadraticModuleElement,
) -> tuple[TorsionQuadraticModuleElement, ...]:
    r"""Return ``orbit_G(x)`` inside a checked finite ``G``-stable subset."""
    D = G.invariant_form()
    subset = discriminant_form_stable_subset(G, X)
    point = D(x)
    assert point in subset, "orbit representative is not in the finite subset"
    orbit = discriminant_form_orbit(G, point)
    assert all(y in subset for y in orbit), "orbit leaves the finite subset"
    return orbit


def discriminant_form_subset_orbits(
    G: Group,
    X: Iterable[TorsionQuadraticModuleElement],
) -> tuple[tuple[TorsionQuadraticModuleElement, ...], ...]:
    r"""Return the finite orbit decomposition of a checked ``G``-stable subset."""
    subset = discriminant_form_stable_subset(G, X)
    remaining = list(subset)
    orbits: list[tuple[TorsionQuadraticModuleElement, ...]] = []
    while remaining:
        orbit = discriminant_form_subset_orbit(G, subset, remaining[0])
        orbits.append(orbit)
        remaining = [x for x in remaining if x not in orbit]
    return tuple(orbits)
