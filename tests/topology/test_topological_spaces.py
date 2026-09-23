r"""Continuity between the indiscrete and the Sierpinski topologies on two points.

Derivation: on `\{0, 1\}` the Sierpinski topology has opens `\emptyset, \{1\},
\{0, 1\}` and the indiscrete topology has opens `\emptyset, \{0, 1\}`.  The identity
from the indiscrete space to the Sierpinski space pulls the open `\{1\}` back to
`\{1\}`, which is not open, so it is not continuous; in the other direction every
preimage of an open is open, so it is continuous.
"""

from dzack_research.preamble.all import Sets, TopologicalSpaces


def test_the_identity_is_continuous_from_sierpinski_to_indiscrete_but_not_back() -> None:
    points = Sets.Δ[1]
    spaces = TopologicalSpaces()
    indiscrete = spaces(points, ((), points))
    sierpinski = spaces(points, ((), (points(1),), points))
    identity = Sets().Mor(points, points).identity()

    assert identity in spaces.Mor(sierpinski, indiscrete)
    assert identity not in spaces.Mor(indiscrete, sierpinski)
    assert sierpinski.open_subsets().cardinality() == 3
