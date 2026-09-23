r"""Archive reconciliation for the torsion-module category."""

import pytest

from dzack_research.preamble.all import (
    CC,
    QQ,
    ZZ,
    FinitelyPresentedTorsionModules,
    TorsionModules,
)

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/modules/pure/torsion_modules.sage",
        "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage",
        "live_owner": "src/dzack_research/preamble/categories/modules/pure/modules.py",
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
    free = ZZ.free_module(1)

    assert not free.is_torsion()
    assert free not in TorsionModules(ZZ)


def test_explicit_torsion_constructor_rejects_a_presentation_with_a_free_summand() -> None:
    relations = ZZ.free_module(0)
    generators = ZZ.free_module(1)
    presentation = relations.module_category().Mor(relations, generators).zero()

    with pytest.raises(ValueError, match="nonzero free summand"):
        FinitelyPresentedTorsionModules(ZZ)(presentation)


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
    ring = QQ.power_series_ring("t")
    module = FinitelyPresentedTorsionModules(ring).direct_sum_of_cyclics((ring.one(),))

    assert module.base_ring() is ring
    assert module.is_torsion()
    assert module.is_zero()
    assert module.projective_dimension() == 0


def test_zero_presented_module_has_only_its_zero_subobject_over_a_polynomial_pid() -> None:
    ring = __import__("dzack_research.preamble.all", fromlist=["GF"])
    pid = ring.GF(5).polynomial_ring("t")
    zero = FinitelyPresentedTorsionModules(pid).direct_sum_of_cyclics((pid.one(),))
    subobject = zero.subobject_on(())

    assert subobject.is_zero()
    assert subobject.inclusion().codomain() is zero
    assert subobject.inclusion()(subobject.zero()) == zero.zero()


def test_zero_torsion_module_has_zero_tor_over_a_polynomial_pid() -> None:
    from dzack_research.preamble.all import GF

    ring = GF(5).polynomial_ring("t")
    zero = FinitelyPresentedTorsionModules(ring).direct_sum_of_cyclics((ring.one(),))

    assert zero.tor(zero, 1).is_zero()
    assert zero.tor(zero, 1).cardinality() == zero.cardinality()


def test_zero_module_over_padic_field_is_projective_without_smith_normalization() -> None:
    from dzack_research.preamble.all import Qp

    field = Qp(3)
    zero = FinitelyPresentedTorsionModules(field).direct_sum_of_cyclics((field.one(),))

    assert zero.is_zero()
    assert zero.is_projective()
    assert zero.projective_dimension() == 0


def test_padic_dvr_cyclic_torsion_uses_the_owned_presentation_when_engine_echelon_leaves_the_ring() -> None:
    from dzack_research.preamble.all import Zp

    ring = Zp(2)
    module = FinitelyPresentedTorsionModules(ring).direct_sum_of_cyclics((ring(6),))

    assert module.base_ring() is ring
    assert module.is_torsion()
    assert module.module_rank() == 0
    assert module.projective_dimension() == 1


def test_padic_dvr_diagonal_relation_decides_classes_and_tor() -> None:
    from dzack_research.preamble.all import Zp

    ring = Zp(2)
    module = FinitelyPresentedTorsionModules(ring).direct_sum_of_cyclics((ring(6),))
    generator = module.module_generator(0)

    assert ring(6) * generator == module.zero()
    assert generator != module.zero()
    assert module.tor(module, 1).cardinality() == module.cardinality()


def test_padic_dvr_diagonal_relation_is_its_free_resolution_differential() -> None:
    from dzack_research.preamble.all import Zp

    ring = Zp(2)
    module = FinitelyPresentedTorsionModules(ring).direct_sum_of_cyclics((ring(6),))
    resolution = module.free_resolution(2)

    assert resolution.length() == 1
    assert resolution.differential(1) is module.presentation()
    assert resolution.augmentation().codomain() is module
    assert module.ext(ring.regular_module(), 1).cardinality() == module.cardinality()
