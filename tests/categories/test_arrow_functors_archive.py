r"""Archived domain/codomain functors on the represented arrow category."""

from dzack_research.preamble.all import (
    CodomainFunctor,
    DomainFunctor,
    Sets,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def test_domain_and_codomain_functors_select_the_two_edges_of_a_commuting_square() -> None:
    one = finite_ordered_set(("*",))
    two = finite_ordered_set(("a", "b"))
    pick_a = Sets().Mor(one, two)(lambda _point: two[0])
    identity_two = Sets().Mor(two, two).identity()
    collapse_to_a = Sets().Mor(two, two)(lambda _point: two[0])

    arrows = Sets().ArrowCategory()
    source = arrows(pick_a)
    target = arrows(identity_two)
    square = arrows.Mor(source, target)(pick_a, collapse_to_a)

    domain = DomainFunctor(Sets())
    codomain = CodomainFunctor(Sets())

    assert domain(source) is one
    assert domain(target) is two
    assert domain(square) is pick_a

    assert codomain(source) is two
    assert codomain(target) is two
    assert codomain(square) is collapse_to_a
