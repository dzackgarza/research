r"""Archive reconciliation for the torsion-module category."""


from dzack_research.preamble.all import (
    FinitelyPresentedTorsionModules,
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
