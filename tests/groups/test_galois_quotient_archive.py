r"""Archive reconciliation for finite Galois quotients and restriction maps."""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    exact_embeddings,
    field_generators,
)
from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    extensions_along,
    restrict_along,
)


def test_restriction_map_is_the_actual_finite_galois_quotient_coordinate() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    stage = group.finite_extension(4)
    quotient = group.finite_quotient(stage)
    restriction = group.restriction_map(stage)

    assert restriction.domain() is group
    assert restriction.codomain() is quotient
    assert restriction.is_continuous()
    assert restriction.is_surjective()
    assert restriction(frobenius**3 * frobenius**2) == (
        restriction(frobenius**3) * restriction(frobenius**2)
    )

    kernel = restriction.kernel()
    assert kernel.supergroup() is group
    assert kernel.index() == 4
    assert frobenius not in kernel
    assert frobenius**4 in kernel


def test_restrict_along_and_extensions_along_solve_the_same_commuting_square() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    degree_two = group.finite_extension(2)
    degree_four = group.finite_extension(4)
    quotient_two = group.finite_quotient(degree_two)
    quotient_four = group.finite_quotient(degree_four)
    restriction_two = group.restriction_map(degree_two)
    restriction_four = group.restriction_map(degree_four)

    smaller_generator = field_generators(degree_two.field())[0]
    compatible = tuple(
        embedding
        for embedding in exact_embeddings(degree_two.field(), degree_four.field())
        if degree_four.embedding()(embedding(smaller_generator))
        == degree_two.embedding()(smaller_generator)
    )
    assert len(compatible) == 1
    inclusion = compatible[0]

    sigma = restriction_four(frobenius)
    tau = restriction_two(frobenius)
    assert restrict_along(sigma.action(), inclusion) == tau.action()

    extensions = extensions_along(
        tau.action(),
        inclusion,
        tuple(candidate.action() for candidate in quotient_four),
    )
    assert extensions.cardinality() == 2
    assert sigma.action() in extensions


def test_lift_fiber_is_a_coset_of_the_restriction_kernel() -> None:
    group = AbsoluteGaloisGroup(GF(5))
    frobenius = group.frobenius()
    stage = group.finite_extension(4)
    restriction = group.restriction_map(stage)
    finite_element = restriction(frobenius**3)
    coset = group.lifts(finite_element)

    assert coset.kernel() == restriction.kernel()
    assert coset.representative() == frobenius**3
    assert frobenius**3 in coset
