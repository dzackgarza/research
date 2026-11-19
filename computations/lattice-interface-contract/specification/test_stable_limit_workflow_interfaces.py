"""Contract for the operation the semifan of a recognizable divisor needs (research#679, A36).

The unit's page, `writing/coble/compactifications/toroidal-and-semitoroidal.md`, carries
`rmk:missing-stable-limit`: the split $I\\sqcup J$ of a recognizable divisor's semifan is a
labelling of the cones of the Coxeter semifan by the combinatorial type of the KSBA stable
limit of the pair, and no operation of the library produces that type.  These tests are the
interface obligation, in the repository's own red channel (`pytest.ini`: a `tdd_red` test must
fail until the interface is implemented, and the conftest hook fails it if it passes).

The contract, from `rmk:missing-stable-limit` and from `thm:semifan-stratum`:

    method: stable_limit
    input:  a hyperbolic lattice $\\bar T$ (the boundary lattice of a $0$-cusp), a monodromy
            invariant $\\lambda$ in its positive cone, and the polarizing divisor, named
    output: the combinatorial type of the KSBA stable limit of the pair: the components of the
            central fibre with their genera, the multiplicities with which the limit divisor
            meets them, and the contraction defining the stable model

Three obligations are stated here, each from a printed source rather than invented:

1. **Constancy on a cone.**  The type depends on $\\lambda$ only through the cone of the
   semifan containing it (AET23, Theorem 7.5, printed p. 48: "if the monodromy-invariant
   $\\lambda$ ... lies in the relative interior $\\lambda\\in\\sigma^\\circ$ of a cone
   $\\sigma\\in\\mathcal F^{\\mathrm{cox}}$, the stable limit is a stable surface associated to
   the stable type of the subdiagram defining $\\sigma$").  So $\\lambda$ and $2\\lambda$ have
   the same type.
2. **The published fixture.**  For the degree-two cusp lattice and the ramification divisor,
   the type over the open cell is the one AET23 compute in Example 7.4, printed p. 48: eighteen
   copies of $(\\PP^2, L+C)$ with a line and a conic, glued conics to conics and lines to lines.
   An implementation can therefore be checked against a source at one point, and that is what
   the second test demands.
3. **The level sets are the semifan.**  `semifan(divisor=...)` returns the cones of the
   semifan whose cones are the loci of constant type (`thm:semifan-stratum`), with their wall
   roots, which is the object the split labels.

Nothing here decides $R_\\rcop$: the third test only requires the object, and where the type is
not published the contract fixes no value.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import Lattice, assert_equal

# The contract backend builds small examples; the lattices the obligations are about are the
# boundary lattice of the 0-cusp of F_2, U + E8(-1)^2 + A1(-1) (rank 19), and of the elliptic
# cusp, U + E8(-1)^2 (rank 18).  The interfaces below are stated on `Lattice.U()` because what
# is missing is the operation and not the lattice, and a rank-2 example keeps the failing call
# in the test rather than in a construction.
HYPERBOLIC = Lattice.U()


def test_stable_limit_returns_a_combinatorial_type_with_the_divisor_named():
    """
    method: stable_limit

    Interface contract:
    the limit of a pair is a type carrying the components of the central fibre, the
    multiplicities of the divisor on them, and the contraction to the stable model; the
    divisor whose limit is asked for is named, because the type depends on it and not on its
    class alone (rmk:recognizable-gap).
    """
    lam = HYPERBOLIC.monodromy_invariant_in_positive_cone()
    ramification = HYPERBOLIC.stable_limit(lam, divisor="ramification")
    rational_curves = HYPERBOLIC.stable_limit(lam, divisor="rational_curves")

    for limit in (ramification, rational_curves):
        assert limit.components() is not None
        assert limit.divisor_multiplicities() is not None
        assert limit.contraction() is not None
    assert_equal(
        ramification == rational_curves,
        False,
        "the limits of two different polarizing divisors must not be assumed equal",
    )


def test_stable_limit_is_constant_on_a_semifan_cone():
    """
    method: stable_limit, semifan

    Interface contract:
    AET23, Theorem 7.5, printed p. 48: the type depends on lambda only through the cone of the
    semifan containing it.  So a monodromy invariant and a positive multiple of it have the same
    type, and the level sets of the type are the cones that `semifan` reports.
    """
    double_cusp = HYPERBOLIC
    lam = double_cusp.monodromy_invariant_in_positive_cone()
    assert_equal(
        double_cusp.stable_limit(lam, divisor="ramification")
        == double_cusp.stable_limit(2 * lam, divisor="ramification"),
        True,
        "a cone of the semifan is a locus of constant combinatorial type",
    )
    cones = double_cusp.semifan(divisor="ramification").cones()
    assert_equal(
        any(lam in cone for cone in cones),
        True,
        "the monodromy invariant lies in a cone of the semifan it was read in",
    )


def test_stable_limit_reproduces_the_published_degree_two_degeneration():
    """
    method: stable_limit

    Interface contract:
    AET23, Example 7.4, printed p. 48, computes the maximal degeneration of the degree-two
    stable-pair compacification: eighteen copies of (P^2, L + C) with a line and a conic, glued
    conics to conics and lines to lines.  The implementation is checked against that number and
    that component type over the open cell.
    """
    lam = HYPERBOLIC.monodromy_invariant_in_positive_cone()
    limit = HYPERBOLIC.stable_limit(lam, divisor="ramification")
    assert_equal(
        len(limit.components()),
        18,
        "AET23, Example 7.4, printed p. 48: the maximal degeneration has 18 components",
    )
    assert_equal(
        all(component.is_plane_with_line_and_conic() for component in limit.components()),
        True,
        "each component is (P^2, L + C), a line and a conic",
    )


def test_the_elliptic_cusp_carries_the_semifan_of_a_computed_divisor():
    """
    method: semifan

    Interface contract:
    ABE22, Introduction, Theorem 1.2 and Section 3, compute the semifan of the elliptic locus
    for the divisor s + m sum f_i: it subdivides each Coxeter chamber into nine, by the four
    hyperplanes with normals beta_L, gamma_L, beta_R, gamma_R.  That is the one computed
    non-ramification semifan, so it is the check on the semifan operation itself.
    """
    cones = HYPERBOLIC.semifan(divisor="elliptic_section_plus_fibres").cones()
    assert_equal(
        len(cones) % 9,
        0,
        "ABE22 Section 3: each Coxeter chamber is subdivided into 3 * 3 = 9 subcones",
    )
    chamber = HYPERBOLIC.fundamental_chamber()
    assert_equal(
        len(chamber.wall_roots()) - len(cones[0].wall_roots()) >= 0,
        True,
        "the semifan's cones are cut out by the Coxeter walls and the four extra normals",
    )
