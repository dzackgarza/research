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
    QQ,
    ZZ,
    FiberProductSchemes,
)


def _line_over(ring):
    r"""``A^1_R`` built as a spectrum, so its coordinate algebra names it back."""
    line = (ring.polynomial_ring("x")).affine_spectrum(base_ring=ring)
    structure = line.structure_morphism()
    return line, line.scheme_category().fiber_product(structure, structure)


def test_the_affine_line_squared_over_the_base_is_the_affine_plane() -> None:
    line, plane = _line_over(ZZ)

    assert plane in FiberProductSchemes(ZZ)
    assert plane.relative_dimension() == 2
    assert plane.coordinate_algebra().algebra_generating_set().cardinality() == 2
    assert plane.fiber_product_base() is line.base_scheme()

    left_projection, right_projection = plane.fiber_product_projections()
    construction = plane.fiber_product_construction()
    left_map, right_map = plane.fiber_product_cospan()
    assert construction.cospan()[0] is left_map
    assert construction.cospan()[1] is right_map
    assert construction.projections()[0] is left_projection
    assert construction.projections()[1] is right_projection
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
    assert witness.fiber_product_base() is (ZZ).affine_spectrum(base_ring=ZZ)


def test_fiber_of_the_first_projection_over_the_origin_is_an_affine_line() -> None:
    line, plane = _line_over(QQ)
    algebra = line.coordinate_algebra()
    x = algebra.algebra_generator("x")
    origin = line.closed_subscheme(x)
    first_projection = plane.fiber_product_projections()[0]
    fiber = first_projection.codomain().scheme_category().fiber_product(
        first_projection,
        origin.inclusion(),
    )

    assert fiber.fiber_product_base() is line
    assert fiber.left_projection().codomain() is plane
    assert fiber.right_projection().codomain() is origin
    assert fiber.relative_dimension() == 1
    assert first_projection * fiber.left_projection() == (
        origin.inclusion() * fiber.right_projection()
    )
