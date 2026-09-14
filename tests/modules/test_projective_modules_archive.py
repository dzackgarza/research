r"""Archive reconciliation for projective modules as a module property."""

from dzack_research.preamble.all import QQ, FreeModules, ProjectiveModules

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/pure/projective_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    "disposition": "reconciled-live-owner",
}


def test_free_modules_lie_in_projective_modules_and_certify_projectivity() -> None:
    free = FreeModules(QQ).an_object()

    assert free in FreeModules(QQ)
    assert free in ProjectiveModules(QQ)
    assert free.is_free()
    assert free.is_projective()


def test_projective_modules_are_modules_over_the_same_base_ring() -> None:
    projectives = ProjectiveModules(QQ)
    example = projectives.an_object()

    assert example.base_ring() is QQ
    assert example in projectives
    assert example.is_projective()
