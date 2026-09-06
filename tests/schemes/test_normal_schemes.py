r"""Normality of affine and projective space, read off the base ring.

A scheme is normal when its local rings are integrally closed domains.
Affine ``n``-space over ``R`` is covered by ``R[x_1,...,x_n]`` and projective
``n``-space by the degree-zero parts of its graded localizations, which are
again polynomial rings on ``n`` variables, so both are normal exactly when
``R`` is.  The criterion stated in the preamble is that ``R`` is a principal
ideal domain, hence a unique factorization domain, hence integrally closed.

The last assertion of each test is what separates the criterion from an
unconditional placement: over a base that is not even a domain, nothing is
asserted normal.
"""

from dzack_research.preamble.all import (
    AffineSpace,
    NormalSchemes,
    ProjectiveSpace,
    QQ,
    Spec,
    ZZ,
    Zmod,
)


def test_affine_space_is_normal_over_a_principal_ideal_domain() -> None:
    line = AffineSpace(1, ZZ)
    plane = AffineSpace(2, QQ)

    assert line in NormalSchemes(ZZ)
    assert line.is_normal()
    assert plane in NormalSchemes(QQ)

    # The criterion reads the base: Z/12 is not a domain, so A^1 over it is
    # not asserted normal, and an unconditional placement would say it is.
    residues = Zmod(12)
    assert Spec(residues, base_ring=residues) not in NormalSchemes(residues)


def test_projective_space_is_normal_over_a_principal_ideal_domain() -> None:
    projective_line = ProjectiveSpace(1, QQ)
    projective_plane = ProjectiveSpace(2, ZZ)

    assert projective_line in NormalSchemes(QQ)
    assert projective_plane in NormalSchemes(ZZ)
    assert projective_plane.is_normal()


def test_the_base_scheme_and_the_witness_of_the_category_are_normal() -> None:
    r"""``Spec Z`` is normal, and the category exhibits a member of itself."""
    assert Spec(ZZ, base_ring=ZZ) in NormalSchemes(ZZ)
    assert NormalSchemes(ZZ).an_object() in NormalSchemes(ZZ)
    assert NormalSchemes(QQ).an_object() in NormalSchemes(QQ)
