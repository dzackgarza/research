r"""Archive reconciliation for profinite-group topology and finite coordinates."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.groups import TopologicalGroups
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.profinite_groups import (
    ProfiniteGroups,
)


ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/profinite/profinite_groups.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/profinite/profinite_groups.py",
    "disposition": "reconciled-live-owner",
}


def test_finite_field_absolute_galois_group_is_profinite_not_finitely_generated_algebraically() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()

    assert group in ProfiniteGroups()
    assert group in TopologicalGroups()
    assert group.is_profinite() is True
    assert group.is_finitely_generated() is False
    assert tuple(group.topological_group_generators()) == (frobenius,)


def test_finite_galois_quotients_are_actual_continuous_coordinates() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    degree_two = group.finite_extension(2)
    degree_six = group.finite_extension(6)
    quotient_two = group.finite_quotient(degree_two)
    quotient_six = group.finite_quotient(degree_six)
    coordinate_two = group.restriction_map(degree_two)
    coordinate_six = group.restriction_map(degree_six)

    assert quotient_two.order() == 2
    assert quotient_six.order() == 6
    assert coordinate_two.is_continuous()
    assert coordinate_six.is_continuous()
    assert coordinate_two.is_surjective()
    assert coordinate_six.is_surjective()
    assert coordinate_two(frobenius**2) == quotient_two.one()
    assert coordinate_six(frobenius**6) == quotient_six.one()


def test_topological_generator_maps_to_generators_of_finite_coordinates() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.topological_group_generators()[0]

    for degree in (2, 3, 4):
        stage = group.finite_extension(degree)
        quotient = group.finite_quotient(stage)
        image = group.restriction_map(stage)(frobenius)
        assert image.multiplicative_order() == quotient.order()
