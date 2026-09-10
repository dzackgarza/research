r"""Archive reconciliation for finite-quotient profinite character Homs.

The archive used a bespoke ``ProfiniteCharacterHomsets`` category.  The live
owner is the shared continuous group Hom: cyclotomic and quadratic characters,
Galois restriction maps, and their restrictions all live in that same Hom
construction rather than a parallel character-only morphism graph.
"""

from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.galois_characters import (
    CyclotomicCharacter,
)
from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    ContinuousGroupHomset,
    continuous_group_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import GF


def test_continuous_group_hom_is_canonical_for_exact_endpoints() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    character = CyclotomicCharacter(group, 3)
    homset = continuous_group_homset(group, character.codomain())

    assert isinstance(homset, ContinuousGroupHomset)
    assert character.parent() is homset
    assert continuous_group_homset(group, character.codomain()) is homset
    assert homset.domain() is group
    assert homset.codomain() is character.codomain()


def test_nontrivial_cyclotomic_character_retains_factor_kernel_and_restriction() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    character = CyclotomicCharacter(group, 3)
    frobenius = group.frobenius()

    assert character(frobenius) != character.codomain().one()
    assert character.is_continuous()
    assert character.factorization().domain() is group
    assert character.factorization().extension() is character.factor_extension()

    kernel = character.kernel()
    assert kernel.supergroup() is group
    assert kernel.fixed_extension() is character.factor_extension()
    assert kernel.index() == 2

    restricted = character.restrict(kernel)
    restricted_hom = continuous_group_homset(kernel, character.codomain())
    assert restricted.parent() is restricted_hom
    assert restricted.domain() is kernel
    assert restricted.codomain() is character.codomain()
    assert restricted.is_continuous()
