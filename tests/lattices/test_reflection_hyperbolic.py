r"""Reflection groups of hyperbolic lattices, and Vinberg's enumeration.

Vinberg's algorithm enumerates the walls of a fundamental polyhedron for
\(W(L)\).  It is a semi-decision procedure: it halts with a certificate when
the polyhedron closes, so a completed search proves reflectivity while a
bounded one proves nothing.  The tests below state what a completed search
delivers on \(U\oplus A_1\), and check Vinberg's root-length bound against the
two Bogachev-Kolpakov ternary lattices, where the bound is what makes "does
this lattice have a root" a finite question.

Allcock's edgewalk answers the same question and terminates on every input, so
it decides where Vinberg's algorithm semi-decides; the last test states that
agreement, or the shared absence of the program that realizes it.

Sources: Vinberg, *On groups of unit elements of certain quadratic forms*,
Mat. Sb. 87 (1972); Vinberg, *Hyperbolic reflection groups*, Russian Math.
Surveys 40 (1985); Bogachev and Kolpakov, *Thin hyperbolic reflection groups*,
arXiv:2112.14642v4, sections 6.1 and 6.2.  The edgewalk is taken from its
implementation in ``polyhedral_common``, ``src_lorentzian/edgewalk.h``.
"""

import pytest
from py_polyhedral.binaries import binary_available

from dzack_research.preamble.all import HyperbolicLattices, Lattices, ZZ, finite_ordered_set
from dzack_research.preamble.engine_capabilities import EngineCapabilityUnavailable


def u_plus_a1():
    r"""Return \(U\oplus A_1\), of signature \((1,2)\), as a hyperbolic lattice."""
    return HyperbolicLattices(ZZ)(Lattices(ZZ)("U") + Lattices(ZZ)("A1"))




def test_vinbergs_criterion_bounds_the_root_lengths_of_the_bogachev_kolpakov_lattices() -> None:
    r"""Every root length divides twice the last invariant factor.

    Bogachev and Kolpakov, arXiv:2112.14642v4 section 6.2, citing Vinberg: for
    a root \(r\), \(q(r)\) divides twice the last invariant factor of the
    correlation, which is the exponent of the discriminant group.  For the
    section 6.1 lattice the invariant factors are \(1, 49, 49\), so every root
    length divides \(98\); for the section 6.2 lattice they are
    \(1, 49, 2401\), so every root length divides \(4802 = 2\cdot 7^4\).  That
    bound is why the paper can say the second lattice has no roots at all: what
    would otherwise be an unbounded search is a check of four candidate
    lengths.
    """
    with_roots = HyperbolicLattices(ZZ)(Lattices.BogachevKolpakovNonReflective)
    without_roots = HyperbolicLattices(ZZ)(Lattices.BogachevKolpakovWithoutRoots)

    expected_lengths = finite_ordered_set(
        (ZZ(1), ZZ(2), ZZ(7), ZZ(14), ZZ(49), ZZ(98))
    )
    lengths = with_roots.possible_root_lengths()
    assert lengths.cardinality() == expected_lengths.cardinality()
    assert all(
        lengths[position] == expected_lengths[position]
        for position in range(int(lengths.cardinality()))
    )

    lengths = without_roots.possible_root_lengths()
    expected_divisors = ZZ(4802).divisors()
    assert lengths.cardinality() == expected_divisors.cardinality()
    assert all(
        lengths[position] == expected_divisors[position]
        for position in range(int(lengths.cardinality()))
    )
    for candidate in (49, 98, 2401, 4802):
        assert candidate in lengths, "a candidate length the paper had to exclude"


def test_the_root_length_forty_nine_case_is_excluded_by_a_local_obstruction() -> None:
    r"""The shortest candidate length of the section 6.2 lattice fails over \(\mathbb Z_7\).

    Bogachev and Kolpakov, arXiv:2112.14642v4 section 6.2: for \(f(r)=49\) the
    crystallographic conditions force \(k_1=m_1\), \(k_2=7m_2-3m_3\) and
    \(k_3=7m_3\), leaving

    .. MATH::

        q(r) = f(r)/49 = 49m_2^2 + 14m_1m_3 - 28m_2m_3 + 6m_3^2,

    and the paper concludes that \(q\) does not integrally represent \(1\).
    The certificate is checked here rather than quoted: modulo \(7\) the first
    three coefficients vanish and \(q\equiv 6m_3^2\); the squares modulo \(7\)
    are \(\{0,1,2,4\}\), so \(q\) takes only \(\{0,3,5,6\}\) and never \(1\).
    It therefore fails to represent \(1\) already over \(\mathbb Z_7\), hence
    over \(\mathbb Z\).  The remaining candidate lengths \(98\), \(2401\) and
    \(4802\) are excluded by analogous arguments in the paper.

    This is how a root-length bound becomes a proof that a lattice has no
    roots: the bound makes the candidate set finite, and each candidate falls
    to a local obstruction.
    """
    residues = {
        (49 * m2**2 + 14 * m1 * m3 - 28 * m2 * m3 + 6 * m3**2) % 7
        for m1 in range(7)
        for m2 in range(7)
        for m3 in range(7)
    }

    assert residues == {0, 3, 5, 6}, "q reduces to 6 m_3^2 modulo 7"
    assert 1 not in residues, "q represents 1 over neither ZZ_7 nor ZZ"

    without_roots = HyperbolicLattices(ZZ)(Lattices.BogachevKolpakovWithoutRoots)
    assert 49 in without_roots.possible_root_lengths(), "49 was a candidate to exclude"


def test_vinberg_enumeration_closes_the_polyhedron_of_u_plus_a1() -> None:
    r"""The search on \(U\oplus A_1\) completes, which certifies reflectivity.

    What a completed search delivers is the wall set of a fundamental
    polyhedron.  Each wall is the mirror of a root, so each accepted vector is
    a root of the lattice, its reflection is an involution of \(O(L)\), and its
    length obeys Vinberg's bound.  Those are the claims here; the number of
    walls is not asserted, because it depends on the controlling vector the
    engine chose.
    """
    lattice = u_plus_a1()
    roots = lattice.vinberg_simple_roots(max_decompositions=200)

    assert lattice.is_reflective(max_decompositions=200) is True
    assert roots.cardinality() >= 3, "a polyhedron in H^2 has at least three walls"

    lengths = lattice.possible_root_lengths()
    identity = lattice.O().one()
    for root in roots:
        assert root.is_root()
        assert abs(root.q()) in lengths, "Vinberg's criterion bounds the length"
        reflection = lattice.reflection(root)
        assert reflection in lattice.O()
        assert reflection * reflection == identity
        assert reflection(root) == -root




def test_a_lattice_that_represents_zero_has_a_noncompact_fundamental_domain() -> None:
    r"""\(U\oplus A_1\) is reflective and not cocompact.

    \(U\) is isotropic, so the light cone of \(L\otimes\mathbb R\) meets the
    lattice, and the fundamental polyhedron has a vertex on the boundary of
    hyperbolic space.  A polyhedron is compact exactly when it has finite
    volume and no such ideal vertex, so the domain here has finite volume and
    is not compact, which is the common hyperbolic case rather than a defect.
    """
    lattice = u_plus_a1()

    assert lattice.is_reflective(max_decompositions=200) is True
    assert lattice.is_cocompact(max_decompositions=200) is False


def test_the_edgewalk_decides_reflectivity_where_vinbergs_algorithm_semi_decides_it() -> None:
    r"""Allcock's edgewalk answers the same question with a stronger certificate.

    Vinberg's algorithm halts only on a reflective lattice, so it proves
    reflectivity and never disproves it.  The edgewalk walks the edges of a
    fundamental polyhedron and terminates on every input, reporting the
    obstruction when there is no such polyhedron, so it decides.  On
    \(U\oplus A_1\) the two agree, and the walls the edgewalk reports are
    roots of the lattice like the walls Vinberg's enumeration reports.

    The edgewalk is realized by ``LORENTZ_ReflectiveEdgewalk`` of
    ``polyhedral_common``.  Where that program is not on ``PATH`` the question
    is refused by the shared capability layer, which names the provider and
    the command that builds it; no other engine is substituted, because no
    other engine decides this.
    """
    lattice = u_plus_a1()

    if not binary_available("LORENTZ_ReflectiveEdgewalk"):
        with pytest.raises(EngineCapabilityUnavailable) as refusal:
            lattice.edgewalk_is_reflective()

        absence = refusal.value.absent
        assert refusal.value.capability == "lorentzian_edgewalk_fundamental_domain"
        assert absence[0].provider == "polyhedral-common-via-py-polyhedral"
        assert not absence[1:]
        assert "LORENTZ_ReflectiveEdgewalk" in absence[0].provisioning
        return

    assert lattice.edgewalk_is_reflective() is True
    assert lattice.is_reflective(max_decompositions=200) is True

    walls = lattice.edgewalk_simple_roots()
    assert walls.cardinality() >= 3, "a polyhedron in H^2 has at least three walls"

    lengths = lattice.possible_root_lengths()
    identity = lattice.O().one()
    for wall in walls:
        assert wall.is_root()
        assert abs(wall.q()) in lengths, "Vinberg's criterion bounds the length"
        reflection = lattice.reflection(wall)
        assert reflection in lattice.O()
        assert reflection * reflection == identity
