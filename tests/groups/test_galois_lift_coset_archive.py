"""Archive reconciliation for lift cosets of finite Galois coordinates."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def test_lift_coset_retains_ambient_kernel_and_finite_coordinate() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    stage = group.finite_extension(3)
    group.finite_quotient(stage)
    restriction = group.restriction_map(stage)
    sigma = restriction(group.frobenius())
    coset = group.lifts(sigma)

    assert coset in Sets().Subobjects(group)
    assert coset.inclusion().codomain() is group
    assert coset.ambient() is group
    assert coset.supergroup() is group
    assert coset.kernel().fixed_extension() is stage
    assert restriction.kernel().fixed_extension() is stage
    representative = coset.representative()
    assert representative in coset
    assert restriction(representative) == sigma


def test_multiplying_a_lift_by_the_kernel_stays_in_the_same_coset() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    stage = group.finite_extension(2)
    restriction = group.restriction_map(stage)
    sigma = restriction(group.frobenius())
    coset = group.lifts(sigma)
    representative = coset.representative()
    kernel_element = group.frobenius() ** 2

    assert kernel_element in coset.kernel()
    assert representative * kernel_element in coset
