r"""The fibre product of two schemes over the base scheme.

``Spec R`` is terminal in ``Sch/R``, so a cospan into it has the structure
morphisms as its two legs and the span of coordinate algebras sits under
``R``, the initial object of ``CAlg_R``.  A colimit under the initial object
is the colimit of the discrete diagram, so ``X x_{Spec R} Y`` is
``Spec(A tensor_R B)`` and the map induced by a cone is the coproduct's own
factorization.

The universal property is what these tests assert: the diagonal induced by
the pair ``(id, id)`` composes with each projection back to the identity.
"""

from dzack_research.preamble.all import (
    FiberProductSchemes,
    PolynomialRing,
    QQ,
    Spec,
    ZZ,
    scheme_fiber_product,
)


def _line_over(ring):
    r"""``A^1_R`` built as a spectrum, so its coordinate algebra names it back."""
    line = Spec(PolynomialRing(ring, "x"), base_ring=ring)
    return line, scheme_fiber_product(line.structure_morphism(), line.structure_morphism())


def test_the_affine_line_squared_over_the_base_is_the_affine_plane() -> None:
    line, plane = _line_over(ZZ)

    assert plane in FiberProductSchemes(ZZ)
    assert plane.relative_dimension() == 2
    assert plane.coordinate_algebra().algebra_generating_set().cardinality() == 2
    assert plane.fiber_product_base() is line.base_scheme()

    left_projection, right_projection = plane.fiber_product_projections()
    assert left_projection.codomain() is line
    assert right_projection.codomain() is line
    assert left_projection.domain() is plane


def test_the_diagonal_is_the_map_induced_by_the_pair_of_identities() -> None:
    line, plane = _line_over(QQ)
    identity = line.categorical_identity_morphism()

    diagonal = plane.from_pullback_cone(identity, identity)
    left_projection, right_projection = plane.fiber_product_projections()

    assert diagonal.domain() is line
    assert diagonal.codomain() is plane
    assert left_projection * diagonal == identity
    assert right_projection * diagonal == identity


def test_the_category_exhibits_a_fibre_product_of_affine_spaces() -> None:
    r"""The witness of the category is ``A^1 x_{Spec Z} A^1``, built from affine space."""
    witness = FiberProductSchemes(ZZ).an_object()

    assert witness in FiberProductSchemes(ZZ)
    assert witness.relative_dimension() == 2
    assert witness.fiber_product_base() is Spec(ZZ, base_ring=ZZ)
