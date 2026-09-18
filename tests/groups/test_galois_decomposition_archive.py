r"""Archive reconciliation for decomposition, inertia, and Frobenius objects."""

from dzack_research.preamble.all import QQ, QuadraticField
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.groups import Subgroups
from dzack_research.preamble.categories.group.profinite.galois_decomposition import (
    PrimeProlongation,
)
from dzack_research.preamble.categories.group.profinite.profinite_groups import (
    ProfiniteGroups,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/profinite/galois_decomposition.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py",
    "disposition": "reconciled-live-owner",
}


def test_chosen_decomposition_and_inertia_groups_project_to_finite_quotients() -> None:
    group = AbsoluteGaloisGroup(QQ)
    field = QuadraticField(5, "a")
    stage = group.extension_data(field)
    quotient = group.finite_quotient(stage)
    prime_above_two = field.primes_above(2)[0]
    prolongation = PrimeProlongation(2, lambda _extension: prime_above_two)
    assert prolongation in Objects()

    decomposition = group.decomposition_group(2, prolongation=prolongation)
    inertia = group.inertia_group(2, prolongation=prolongation)

    assert decomposition.ambient() is group
    assert inertia.ambient() is group
    assert decomposition in ProfiniteGroups()
    assert inertia in ProfiniteGroups()
    assert decomposition in Subgroups(group)
    assert inertia in Subgroups(group)
    assert decomposition.one() == group.one()
    assert inertia.one() == group.one()
    assert decomposition.image(quotient).order() == 2
    assert inertia.image(quotient).order() == 1
    assert decomposition.conjugacy_class() == group.decomposition_group_class(2)
    assert inertia.conjugacy_class() == group.inertia_group_class(2)


def test_frobenius_is_retained_as_a_conjugacy_class_with_finite_image() -> None:
    group = AbsoluteGaloisGroup(QQ)
    field = QuadraticField(5, "a")
    stage = group.extension_data(field)
    quotient = group.finite_quotient(stage)
    prime_above_two = field.primes_above(2)[0]

    frobenius = group.frobenius_class(2)
    image = frobenius.image(quotient, prime_above_two)

    assert frobenius.ambient() is group
    assert frobenius.conjugacy_class() is frobenius
    assert image.representative() != quotient.one()


def test_choice_independent_class_returns_a_chosen_representative() -> None:
    group = AbsoluteGaloisGroup(QQ)
    field = QuadraticField(5, "a")
    prime_above_two = field.primes_above(2)[0]
    prolongation = PrimeProlongation(2, lambda _extension: prime_above_two)

    conjugacy_class = group.decomposition_group_class(2)
    representative = conjugacy_class.representative(prolongation)

    assert representative.conjugacy_class() == conjugacy_class
    assert representative.ambient() is group
