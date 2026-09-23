r"""Archive reconciliation for profinite-group topology and finite coordinates."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/profinite/profinite_groups.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/profinite/profinite_groups.py",
    "disposition": "reconciled-live-owner",
}






def test_topological_generator_maps_to_generators_of_finite_coordinates() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.topological_group_generators()[0]

    for degree in (2, 3, 4):
        stage = group.finite_extension(degree)
        quotient = group.finite_quotient(stage)
        image = group.restriction_map(stage)(frobenius)
        assert image.multiplicative_order() == quotient.order()
