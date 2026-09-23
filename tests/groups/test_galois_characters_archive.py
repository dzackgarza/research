r"""Archive reconciliation for continuous absolute-Galois characters.

The archive required genuine morphisms with domain, codomain, kernel and
restriction.  The live owner keeps those maps and additionally retains the
finite Galois extension through which each continuous character factors.
"""

from dzack_research.preamble.all import GF, AbsoluteGaloisGroup


def test_cyclotomic_character_is_an_actual_continuous_morphism() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    character = group.cyclotomic_character(3)
    frobenius = group.frobenius()

    assert character.parent() is group.Mor(character.codomain())
    assert character.domain() is group
    assert character.is_continuous()
    assert character.factor_extension().degree() == 2
    assert character.factorization().domain() is group
    assert character(group.one()) == character.codomain().one()
    assert character(frobenius**5) == character(frobenius**2) * character(frobenius**3)


def test_character_kernel_and_restriction_are_actual_group_maps() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    character = group.quadratic_character(2)
    frobenius = group.frobenius()
    kernel = character.kernel()

    assert kernel.supergroup() is group
    assert kernel.index() == 2
    assert frobenius not in kernel
    assert frobenius**2 in kernel

    restricted = character.restrict(kernel)
    assert restricted.parent() is kernel.Mor(character.codomain())
    assert restricted.domain() is kernel
    assert restricted.codomain() is character.codomain()
    assert restricted.is_continuous()
    assert restricted(kernel.one()) == character.codomain().one()


