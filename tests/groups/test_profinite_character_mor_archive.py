r"""Archive reconciliation for finite-quotient profinite character Mors.

The archive used a bespoke ``ProfiniteCharacterHomsets`` category.  The live
owner is the shared continuous group Mor: cyclotomic and quadratic characters,
Galois restriction maps, and their restrictions all live in that same Mor
construction rather than a parallel character-only morphism graph.
"""

from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.galois_characters import (
    CyclotomicCharacter,
)
from dzack_research.preamble.categories.rings.ring_foundation import GF

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/profinite/galois_characters.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/profinite/galois_characters.py",
    "disposition": "reconciled-live-owner",
    "owner_overrides": {
        "ProfiniteCharacterHomsets": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
        "ProfiniteCharacterHomsets.super_categories": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
        "ProfiniteCharacterHomsets.ParentMethods": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
        "ProfiniteCharacterHomsets.ElementMethods": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
        "ProfiniteCharacterHomsets.ElementMethods.extension": "src/dzack_research/preamble/categories/group/profinite/galois_characters.py",
        "ProfiniteCharacterHomsets.ElementMethods.kernel": "src/dzack_research/preamble/categories/group/profinite/galois_characters.py",
        "ProfiniteCharacterHomsets.ElementMethods.restrict": "src/dzack_research/preamble/categories/group/profinite/galois_characters.py",
        "profinite_character_homset": "src/dzack_research/preamble/categories/group/profinite/galois_quotient.py",
    },
}




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
    restricted_mor = kernel.continuous_morphisms_to(character.codomain())
    assert restricted.parent() is restricted_mor
    assert restricted.domain() is kernel
    assert restricted.codomain() is character.codomain()
    assert restricted.is_continuous()
