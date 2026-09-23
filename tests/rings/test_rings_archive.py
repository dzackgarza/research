r"""Archive reconciliation for the core owned-ring surface.

The archived ring category supplied polynomial extensions, free module powers,
the canonical algebra structure over the ring itself, centers/centrality and
prime fields.  These are now operations of the live owned ring rather than an
installed compatibility layer.
"""

from dzack_research.preamble.all import (
    QQ,
    CommutativeRings,
    OwnedRings,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/rings/rings.sage",
    "live_owner": "src/dzack_research/preamble/categories/rings/rings.py",
    "owner_overrides": {
        "OwnedFields.ParentMethods.absolute_galois_group": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
    },
    "disposition": "reconciled-live-owner",
}




def test_archived_ring_center_and_centrality_are_live_subring_semantics() -> None:
    matrices = QQ.matrix_space(2)
    center = matrices.ring_center()

    assert center in OwnedRings()
    assert center in CommutativeRings()
    assert center.ambient_ring() is matrices
    assert center.inclusion().codomain() is matrices
    assert matrices.one() in center
    assert matrices.is_central(matrices.one()) is True
    noncentral = next(iter(matrices.algebra_generators()))
    assert noncentral not in center
    assert matrices.is_central(noncentral) is False


