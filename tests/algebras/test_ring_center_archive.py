from dzack_research.preamble.all import CommutativeRings, MatrixSpace, OwnedRings, QQ
from dzack_research.preamble.categories.abstract_categories.arrow_categories import Core
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/functors/ring_centers.sage",
    "live_owner": "src/dzack_research/preamble/categories/rings/ring_foundation.py",
    "disposition": "reconciled-live-owner",
}


def test_ring_center_is_functorial_on_a_nonidentity_ring_isomorphism() -> None:
    matrices = MatrixSpace(QQ, 2)
    conjugator = matrices([[0, 1], [1, 0]])
    conjugation = ring_morphism(
        matrices,
        matrices,
        lambda element: conjugator * element * conjugator,
    )
    core = Core(OwnedRings())
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
    matrices = MatrixSpace(QQ, 2)
    center_functor = OwnedRings().center_functor()

    assert matrices in center_functor.domain()
    assert center_functor(matrices) is matrices.ring_center()
    assert QQ in center_functor.domain()
    assert center_functor(QQ) is QQ
