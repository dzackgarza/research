r"""Archive reconciliation for the torsion-module category."""

from dzack_research.preamble.all import FinitelyPresentedTorsionModules, TorsionModules, ZZ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
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
