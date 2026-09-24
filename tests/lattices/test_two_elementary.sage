from dzack_research.preamble.all import *


def test_delta_distinguishes_coeven_and_coodd_discriminant_forms() -> None:
    assert NamedLattices.U_2.two_elementary_invariants() == nikulin_invariants(2, 2, 0)
    assert NamedLattices.Z_2.two_elementary_invariants() == nikulin_invariants(1, 1, 1)
    assert NamedLattices.E10_2.two_elementary_invariants() == nikulin_invariants(10, 10, 0)


def test_block_search_recovers_the_hand_counted_rows() -> None:
    expected_counts = {
        (2, 2, 0): 1,
        (10, 10, 0): 1,
        (10, 10, 1): 3,
    }
    for (rank, length, delta), expected in expected_counts.items():
        candidates = two_elementary_orthogonal_sums(
            signature_pair(1, rank - 1), length, delta
        )
        assert candidates.cardinality() == expected
        expected_invariants = nikulin_invariants(rank, length, delta)
        assert all(
            candidate.two_elementary_invariants() == expected_invariants
            for candidate in candidates
        )


def test_gluing_A1_to_the_8_along_the_all_ones_class_gives_the_8_6_0_genus() -> None:
    r"""\(A_1^8\) has \((r, a, \delta) = (8, 8, 1)\).  The class \(c = \sum g_i\) of
    \(A_{A_1^8} = (\tfrac12\mathbb Z/\mathbb Z)^8\) has \(q(c) = 8\cdot(-\tfrac12) = -4
    \equiv 0 \bmod 2\).  Classes orthogonal to \(c\) are the even-weight sums, so the
    overlattice has discriminant \(c^\perp/c \cong (\mathbb Z/2)^6\) with integral
    values \(-k/2\), \(k\) even: \((8, 6, 0)\).  For 2-elementary even lattices the
    signature and \((r, a, \delta)\) determine the genus (Nikulin, Integral symmetric
    bilinear forms, Thm. 3.6.2)."""
    root_line = Lattices(ZZ)("A1")
    lattice = sum((root_line,) * 8)
    discriminant = lattice.discriminant_module()
    all_ones = sum(discriminant.module_generators(), discriminant.zero())

    assert lattice.two_elementary_invariants() == nikulin_invariants(8, 8, 1)
    assert all_ones.q() == discriminant.quadratic_value_module().zero()

    inclusion = lattice.overlattice(all_ones)
    overlattice = inclusion.codomain()

    assert inclusion.index() == 2
    assert overlattice.is_even()
    assert overlattice.two_elementary_invariants() == nikulin_invariants(8, 6, 0)
    assert overlattice.genus() == NegativeDefTwoElementary[(8, 6, 0)][0].genus()
