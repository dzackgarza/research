r"""Archive reconciliation for the torsion-module category."""

from dzack_research.preamble.all import (
    CC,
    QQ,
    ZZ,
    FinitelyPresentedTorsionModules,
    PowerSeriesRing,
    TorsionModules,
)
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


def test_unit_relation_over_an_inexact_field_is_the_zero_vector_space() -> None:
    module = FinitelyPresentedTorsionModules(CC).direct_sum_of_cyclics((CC(6),))

    assert module.module_rank() == 0
    assert module.is_zero()
    assert module.is_torsion()
    assert module.is_torsion_free()
    assert module.cardinality() == 1


def test_unit_relation_over_formal_power_series_constructs_the_zero_torsion_module() -> None:
    ring = PowerSeriesRing(QQ, "t")
    module = FinitelyPresentedTorsionModules(ring).direct_sum_of_cyclics((ring.one(),))

    assert module.base_ring() is ring
    assert module.is_torsion()
    assert module.is_zero()
    assert module.projective_dimension() == 0


def test_zero_presented_module_has_only_its_zero_subobject_over_a_polynomial_pid() -> None:
    ring = __import__("dzack_research.preamble.all", fromlist=["GF", "PolynomialRing"])
    pid = ring.PolynomialRing(ring.GF(5), "t")
    zero = FinitelyPresentedTorsionModules(pid).direct_sum_of_cyclics((pid.one(),))
    subobject = zero.subobject_on(())

    assert subobject.is_zero()
    assert subobject.inclusion().codomain() is zero
    assert subobject.inclusion()(subobject.zero()) == zero.zero()
