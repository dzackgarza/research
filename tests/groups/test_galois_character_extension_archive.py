"""Archive reconciliation for profinite-character factor extensions."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)


def test_cyclotomic_character_extension_matches_factorization_and_kernel() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    character = group.cyclotomic_character(3)
    extension = character.extension()

    assert extension is character.factor_extension()
    assert character.factorization().extension() is extension
    assert character.kernel().fixed_extension() is extension


def test_quadratic_character_extension_is_the_retained_finite_stage() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    character = group.quadratic_character(group.base_field()(2))

    assert character.extension() is character.factor_extension()
