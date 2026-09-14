r"""Archive reconciliation for noncanonical absolute-Galois realization choices.

The archive stored a global ``GaloisChoicePolicy`` on the parent.  The live
owner makes the mathematically relevant choices explicit construction data:
finite stages retain the selected embedding into the chosen closure, and local
objects require a selected prime prolongation.  No hidden global policy is
needed to recover either choice.
"""

from dzack_research.preamble.all import QQ, QuadraticField
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    exact_embeddings,
)
from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
    PrimeProlongation,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/profinite/galois_choice_policy.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py",
    "owner_overrides": {
        "GaloisChoicePolicy.choose_prolongation": "src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_selected_extension_embedding_is_literal_construction_data() -> None:
    group = AbsoluteGaloisGroup(QQ)
    field = QuadraticField(5, "a")
    candidates = tuple(exact_embeddings(field, group.algebraic_closure()))

    assert len(candidates) >= 2
    selected = candidates[-1]
    stage = group.extension_data(field, embedding=selected)

    assert stage.field() is field
    assert stage.embedding() == selected
    assert stage.embedding() * stage.base_embedding() == group.base_embedding()
    assert group.open_subgroup(stage).fixed_extension().embedding() == selected


def test_local_prolongation_is_explicit_data_not_a_hidden_parent_choice() -> None:
    group = AbsoluteGaloisGroup(QQ)
    field = QuadraticField(5, "a")
    stage = group.extension_data(field)
    prime_above_two = field.primes_above(2)[0]
    prolongation = PrimeProlongation(2, lambda extension: prime_above_two)

    decomposition = group.decomposition_group(2, prolongation=prolongation)
    inertia = group.inertia_group(2, prolongation=prolongation)

    assert decomposition.prolongation() is prolongation
    assert inertia.prolongation() is prolongation
    assert prolongation.base_prime() == 2
    assert prolongation.at(stage) == prime_above_two
