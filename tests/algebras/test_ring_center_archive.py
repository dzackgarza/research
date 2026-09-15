import pytest

from dzack_research.preamble.all import QQ, CommutativeRings, OwnedRings

from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/functors/ring_centers.sage",
        "live_owner": "src/dzack_research/preamble/categories/rings/ring_foundation.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/test_ring_centers.sage",
        "live_owner": "src/dzack_research/preamble/categories/rings/ring_foundation.py",
        "disposition": "reconciled-live-owner",
    },
)


def test_ring_center_is_functorial_on_a_nonidentity_ring_isomorphism() -> None:
    matrices = QQ.matrix_space(2)
    conjugator = matrices([[0, 1], [1, 0]])
    conjugation = matrices.Mor(matrices)(
        lambda element: conjugator * element * conjugator,
    )
    core = OwnedRings().Core()
    automorphism = core.Mor(matrices, matrices)(conjugation, conjugation)

    center_functor = OwnedRings().center_functor()
    transported = center_functor(automorphism)
    center = matrices.ring_center()

    assert center_functor.domain() is core
    assert center_functor.codomain() is CommutativeRings()
    assert transported.domain() is center
    assert transported.codomain() is center
    assert transported(center.one()) == center.one()


def test_ring_center_functor_has_the_same_objects_only_after_taking_centers() -> None:
    matrices = QQ.matrix_space(2)
    center_functor = OwnedRings().center_functor()

    assert matrices in center_functor.domain()
    assert center_functor(matrices) is matrices.ring_center()
    assert QQ in center_functor.domain()
    assert center_functor(QQ) is QQ


def test_ring_center_functor_refuses_a_noninvertible_ring_map() -> None:
    algebra = QQ.free_module(finite_ordered_set(("t",))).symmetric_algebra()
    collapse = algebra.Mor(algebra)({"t": algebra.zero()})
    center_functor = OwnedRings().center_functor()

    with pytest.raises(TypeError):
        center_functor(collapse)
