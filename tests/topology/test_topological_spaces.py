r"""Topological spaces are sets with a selected topology and continuous-map Hom."""

import pytest

from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces


def test_sierpinski_space_retains_its_topology_and_continuous_identity() -> None:
    points = Sets.Δ[1]
    spaces = TopologicalSpaces()
    space = spaces(points, ((), (points(1),), points))
    opens = space.open_subsets()
    singleton = space.power_set()((points(1),))

    assert space in spaces
    assert space in Sets()
    assert singleton in opens
    assert space.power_set().bottom() in opens
    assert space.power_set().top() in opens
    assert spaces.Mor(space, space).identity()(points(0)) == points(0)


def test_constant_map_into_sierpinski_space_is_continuous() -> None:
    points = Sets.Δ[1]
    spaces = TopologicalSpaces()
    source = spaces(points, ((), points))
    target = spaces(points, ((), (points(1),), points))
    constant = spaces.Mor(source, target)(lambda _point: points(1))

    assert constant(source(points(0))) == target(points(1))


def test_indiscrete_to_sierpinski_identity_is_rejected_as_discontinuous() -> None:
    points = Sets.Δ[1]
    spaces = TopologicalSpaces()
    source = spaces(points, ((), points))
    target = spaces(points, ((), (points(1),), points))

    with pytest.raises(ValueError, match="not continuous"):
        spaces.Mor(source, target)(lambda point: target(point))
