from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import Lattice, LatticeRootSystem, assert_equal

U = Lattice.U()
H3 = Lattice.hyperbolic(rank=3)


def test_hyperbolic_lattice_constructor_contract():
    """
    method: hyperbolic

    Hyperbolic-class contract:
    constructor produces rank-2 U with Gram [[0,1],[1,0]].
    Scaling/twisting is done via `twist(k)`, not constructor arguments.
    """
    assert_equal(U.rank(), 2, "HyperbolicLattice rank mismatch")
    assert_equal(U.gram(), ((0, 1), (1, 0)), "HyperbolicLattice gram mismatch")


def test_hyperbolic_vinberg_on_u_matches_affine_a1_root_system():
    """
    method: vinberg

    Hyperbolic-class contract:
    `vinberg()` computes a fundamental domain for the full Coxeter reflection group.
    For the hyperbolic plane `U`, the associated reflection root system is affine A1.
    We assert this via isomorphism to a statically constructed affine A1 root system.
    """
    vinberg_data = U.vinberg()
    assert_equal(
        vinberg_data.root_system().is_isomorphic(LatticeRootSystem.A_affine(1)),
        True,
        "Vinberg root-system mismatch on U",
    )


def test_lattice_root_system_isomorphism_contract():
    """
    method: is_isomorphic

    Root-system contract:
    isomorphic Cartan presentations are detected as equivalent, while non-isomorphic
    Cartan data are rejected.
    """
    affine_a1 = LatticeRootSystem.A_affine(1)
    affine_a1_copy = LatticeRootSystem.A_affine(1)
    finite_a2 = LatticeRootSystem.A(2)

    assert_equal(affine_a1.is_isomorphic(affine_a1_copy), True, "Root-system isomorphism expected true")
    assert_equal(affine_a1.is_isomorphic(finite_a2), False, "Root-system isomorphism expected false")


def test_hyperbolic_vinberg_simple_roots_have_reflective_norms():
    """
    method: simple_roots

    Hyperbolic-class contract:
    returned simple roots are reflective roots; for the `H3` fixture norms are in {-2, -4}.
    """
    allowed_norms = {-2, -4}
    V = H3.vinberg()
    roots = V.simple_roots()
    bad = [(tuple(r), H3.norm(r)) for r in roots if H3.norm(r) not in allowed_norms]
    assert not bad, (
        "Vinberg root norms mismatch: "
        f"allowed={allowed_norms}, violating_roots={bad}"
    )
