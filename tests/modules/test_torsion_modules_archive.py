r"""Archive reconciliation for the torsion-module category."""

from dzack_research.preamble.all import QQ, ZZ, FinitelyPresentedTorsionModules, TorsionModules
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
)

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/modules/pure/torsion_modules.sage",
        "live_owner": "src/dzack_research/preamble/categories/modules/pure/torsion_modules.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage",
        "live_owner": "src/dzack_research/preamble/categories/modules/pure/torsion_modules.py",
        "disposition": "reconciled-live-owner",
    },
)


def test_archive_torsion_category_is_inherited_by_finitely_presented_torsion_modules() -> None:
    category = TorsionModules(ZZ)
    finitely_presented = FinitelyPresentedTorsionModules(ZZ)
    module = finitely_presented.direct_sum_of_cyclics((2, 3))

    assert finitely_presented.is_subcategory(category)
    assert module in category
    assert module in finitely_presented
    assert module.is_torsion()


def test_archive_torsion_category_does_not_reclassify_a_free_module() -> None:
    free = BasedFreeModule(ZZ, 1)

    assert not free.is_torsion()
    assert free not in TorsionModules(ZZ)


def test_cyclic_torsion_construction_uses_the_same_diagonal_presentation_over_a_field() -> None:
    module = FinitelyPresentedTorsionModules(QQ).direct_sum_of_cyclics((QQ(6),))

    assert module in FinitelyPresentedTorsionModules(QQ)
    assert module.is_torsion()
    assert module.is_zero()
    assert module.projective_dimension() == 0
