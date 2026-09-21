"""Archive reconciliation for the unit of the free-module construction."""

import pytest

from dzack_research.preamble.all import ZZ

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/framed_free_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py",
    "owner_overrides": {
        "FramedFreeModules.ParentMethods.module_generator_morphism": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "FramedFreeModules.ParentMethods.Mor": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_canonical_free_generator_recovers_its_framing_label() -> None:
    module = ZZ.free_module(("alpha", "beta"))

    for label in module.module_generating_set():
        generator = module.module_generator(label)
        assert generator.underlying_set_element() == label


def test_non_generator_linear_combinations_have_no_underlying_label() -> None:
    module = ZZ.free_module(("alpha", "beta"))
    alpha = module.module_generator("alpha")
    beta = module.module_generator("beta")

    with pytest.raises(ValueError):
        (alpha + beta).underlying_set_element()
    with pytest.raises(ValueError):
        (2 * alpha).underlying_set_element()
    with pytest.raises(ValueError):
        module.zero().underlying_set_element()


def test_archived_framed_free_module_surface_is_owned_by_the_live_free_module() -> None:
    module = ZZ.free_module(("alpha", "beta"))
    alpha = module.module_generator("alpha")
    beta = module.module_generator("beta")
    framing = module.framing_morphism()
    generator_map = module.module_generator_morphism()

    assert alpha.monomial_coefficients() == {"alpha": ZZ.one()}
    assert beta.monomial_coefficients() == {"beta": ZZ.one()}
    generators = module.module_generators()
    assert repr(generators) == "{[alpha], [beta]}"
    assert generators[0] == alpha
    assert tuple(generators) == (alpha, beta)
    assert generator_map.domain() is module.module_generating_set()
    assert generator_map.codomain() is module
    assert generator_map("alpha") == alpha
    assert framing.codomain() is module
    assert module.is_torsion_free() is True

    endomorphism = module.module_category().Mor(module, module)({"alpha": beta, "beta": alpha})
    assert endomorphism(alpha) == beta
    assert endomorphism(beta) == alpha
