r"""Stabilizers in the orthogonal group of the hyperbolic plane."""

from dzack_research.preamble.all import ZZ, Lattices


def test_in_o_u_the_vector_e_has_trivial_stabilizer_and_its_line_a_stabilizer_of_order_two() -> None:
    r"""\(O(U)=\{\pm1,\pm\sigma\}\) with \(\sigma\) the swap \(e\leftrightarrow f\): an
    isometry fixes the isotropic vectors \(\{\pm e,\pm f\}\) setwise and is determined
    by the image of \(e\).  Only \(1\) fixes \(e\); \(\pm1\) carry \(\mathbb Ze\) onto
    itself, \(\pm\sigma\) send it to \(\mathbb Zf\).
    """
    lattice = Lattices(ZZ)("U")
    group = lattice.O()
    e = lattice.basis_vector(0)
    line = e.sublattice().inclusion()

    assert group.order() == 4
    assert group.stabilizer(e).order() == 1
    assert group.setwise_stabilizer(line).order() == 2
    assert group.pointwise_stabilizer(line).order() == 1
