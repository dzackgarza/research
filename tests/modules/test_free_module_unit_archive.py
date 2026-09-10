"""Archive reconciliation for the unit of the free-module construction."""

import pytest

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModuleOn,
)


def test_canonical_free_generator_recovers_its_framing_label() -> None:
    module = FreeModuleOn(ZZ, ("alpha", "beta"))

    for label in module.module_generating_set():
        generator = module.module_generator(label)
        assert generator.underlying_set_element() == label


def test_non_generator_linear_combinations_have_no_underlying_label() -> None:
    module = FreeModuleOn(ZZ, ("alpha", "beta"))
    alpha = module.module_generator("alpha")
    beta = module.module_generator("beta")

    with pytest.raises(ValueError):
        (alpha + beta).underlying_set_element()
    with pytest.raises(ValueError):
        (2 * alpha).underlying_set_element()
    with pytest.raises(ValueError):
        module.zero().underlying_set_element()
