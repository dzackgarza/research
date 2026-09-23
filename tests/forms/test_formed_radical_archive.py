r"""The radical of a degenerate lattice and the nondegenerate quotient."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_affine_A1_lattice_modulo_its_radical_is_the_A1_root_lattice() -> None:
    r"""``[[2, -2], [-2, 2]]`` has radical ``Z(e1 + e2)``, and the quotient is ``<2> = A1``.

    ``b(e1 + e2, e_i) = 0``; in the quotient the class of ``e1`` has norm 2.
    """
    affine = Lattices(ZZ)([[2, -2], [-2, 2]])
    e1, e2 = affine.basis()
    radical = affine.radical()
    (r,) = radical.basis()
    quotient = affine.radical_quotient()

    assert not affine.is_nondegenerate()
    assert radical.module_rank() == 1
    assert radical.inclusion()(r) in (e1 + e2, -e1 - e2)
    assert radical.inclusion().is_primitive()
    assert quotient.module_rank() == 1
    assert quotient.is_nondegenerate()
    assert quotient.is_isometric_to(Lattices(ZZ)([[2]]))


def test_nondegenerate_hyperbolic_plane_has_zero_radical() -> None:
    r"""``U`` is unimodular, so its radical is 0 and ``U / rad U = U``."""
    u = Lattices(ZZ)("U")

    assert u.radical().module_rank() == 0
    assert u.radical_quotient().is_isometric_to(u)
