r"""Finite subobject operations retain undecidable characteristic predicates."""

from dzack_research.preamble.all import *  # noqa: F401,F403
from dzack_research.preamble.logic import AtomicProposition


def test_finite_subobject_boolean_operations_retain_propositions() -> None:
    ambient = Sets.Δ[1]
    subsets = ambient.power_set()
    unknown = subsets.from_predicate(
        lambda member: AtomicProposition("unknown_subset_membership", member)
    )
    empty = subsets.from_predicate(lambda _member: False)
    full = subsets.from_predicate(lambda _member: True)

    assert unknown.intersection(full).is_parent_of(ambient(0)) is not False
    assert unknown.union(empty).is_parent_of(ambient(0)) is not False
    assert unknown.difference(empty).is_parent_of(ambient(0)) is not False
    assert unknown.complement().is_parent_of(ambient(0)) is not False
    assert unknown.symmetric_difference(empty).is_parent_of(ambient(0)) is not False
    assert (unknown <= full) is True
    assert (empty <= unknown) is True
    assert (unknown <= empty) is not True
    assert (unknown == full) is not True
