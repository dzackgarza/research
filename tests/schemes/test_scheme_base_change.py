r"""Base change of schemes along a ring map, and the slice adjunction along a base morphism."""

from dzack_research.preamble.all import (
    QQ,
    AffineSchemes,
    AffineSpaces,
    FiberProductSchemes,
    IntegralSchemes,
    NormalSchemes,
    ProjectiveSchemes,
    ProjectiveSpaces,
    QuadraticField,
    Schemes,
    SmoothSchemes,
    Algebras,
)


def _extension():
    field = QuadraticField(2, "s")
    return field, QQ.Mor(field)(lambda element: field(element))


def test_base_change_of_the_cuspidal_cubic_is_the_cubic_over_the_extension() -> None:
    field, ring_map = _extension()
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    algebra = plane.coordinate_ring()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    cusp = plane.closed_subscheme(y**2 - x**3)
    change = Schemes(ring_map.domain()).base_change_functor(ring_map)

    ordinary_changed_plane = AffineSpaces(field)(2, names=("x", "y"))
    changed_plane = change(plane)
    changed_cusp = change(cusp)
    # The session spelling names the object, not the functor.
    assert plane.base_change(ring_map) is changed_plane
    assert cusp.base_change(ring_map) is changed_cusp
    assert changed_plane is not ordinary_changed_plane
    assert ordinary_changed_plane not in FiberProductSchemes(field)
    assert changed_plane in AffineSpaces(field)
    assert changed_cusp in AffineSchemes(field)
    assert changed_cusp in FiberProductSchemes(field)
    assert changed_cusp.relative_dimension() == 1
    assert changed_cusp.fiber_product_base() is (QQ).affine_spectrum()
    assert changed_cusp.left_projection().codomain() is cusp
    assert changed_cusp.right_projection().codomain() is (field).affine_spectrum()
    changed_algebra = changed_cusp.coordinate_algebra()
    x_changed = changed_algebra.algebra_generator("x")
    y_changed = changed_algebra.algebra_generator("y")
    assert changed_algebra.base_ring() is field
    assert y_changed**2 == x_changed**3
    projection = changed_cusp.left_projection().coordinate_algebra_morphism()
    assert projection(cusp.coordinate_algebra().algebra_generator("y")) == y_changed

    # The base-change square commutes: X' -> X -> Spec Q equals X' -> Spec K -> Spec Q.
    left_square = cusp.structure_morphism() * changed_cusp.left_projection()
    right_square = change.base_morphism() * changed_cusp.right_projection()
    assert left_square == right_square

    # A morphism over Q base-changes to a morphism over K with commuting squares.
    inclusion = cusp.inclusion()
    changed_inclusion = change(inclusion)
    assert changed_inclusion.domain() is changed_cusp
    assert changed_inclusion.codomain() is changed_plane
    assert changed_plane.left_projection() * changed_inclusion == inclusion * changed_cusp.left_projection()
    assert changed_inclusion.is_closed_immersion()


def test_base_change_transports_automorphisms_and_satisfies_the_identity_and_composition_laws() -> None:
    field, ring_map = _extension()
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    algebra = plane.coordinate_ring()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    swap = Algebras(QQ).Associative().Unital().Commutative().spectrum()(algebra.Mor(algebra)({"x": y, "y": x}))
    change = Schemes(ring_map.domain()).base_change_functor(ring_map)

    changed_swap = change(swap)
    changed_plane = change(plane)
    assert changed_swap.domain() is changed_plane
    assert changed_swap * changed_swap == changed_plane.categorical_identity_morphism()
    assert changed_plane.structure_morphism() * changed_swap == changed_plane.structure_morphism()
    assert changed_plane.left_projection() * changed_swap == swap * changed_plane.left_projection()

    # Along the identity the projection is an isomorphism: a closed immersion
    # whose scheme-theoretic image is everything.
    identity_change = Schemes(QQ).base_change_functor(QQ.Mor(QQ).identity())
    trivial = identity_change(plane)
    assert trivial.left_projection().is_closed_immersion()
    assert trivial.left_projection().scheme_theoretic_image().defining_ideal_owned() == algebra.ideal(algebra.zero())

    # Base change along K -> K after Q -> K agrees with base change along Q -> K
    # up to the canonical isomorphism, computed as the cone map into the composite.
    twice = Schemes(field).base_change_functor(field.Mor(field).identity())(changed_plane)
    comparison = changed_plane.from_pullback_cone(
        changed_plane.left_projection() * twice.left_projection(),
        twice.right_projection(),
    )
    assert comparison.domain() is twice
    assert comparison.codomain() is changed_plane
    assert comparison.is_closed_immersion()
    assert comparison.scheme_theoretic_image().defining_ideal_owned() == changed_plane.coordinate_algebra().ideal(
        changed_plane.coordinate_algebra().zero()
    )


def test_composition_along_a_base_morphism_is_left_adjoint_to_pullback() -> None:
    r"""``Sigma_g ⊣ g^*`` for the closed point ``g: Spec Q -> A^1_t`` at ``t = 0``.

    The family ``xy = t`` over the ``t``-line pulls back to its special
    fibre ``xy = 0`` over the point, and the counit of the adjunction is the
    projection of that fibre into the family.
    """
    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    presentation = parameter.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family_algebra = (presentation).quotient_by_relations((x * y - t,))
    residue_algebra = parameter.quotient_ring(parameter.ideal(t))
    spec = Algebras(parameter).Associative().Unital().Commutative().spectrum()
    line = Schemes(parameter).base_scheme()
    family = spec(family_algebra)
    point = spec(residue_algebra)
    base_morphism = point.structure_morphism()
    adjunction = base_morphism.slice_base_change_adjunction()
    over_line = adjunction.right_adjoint().domain()
    over_point = adjunction.left_adjoint().domain()

    family_object = over_line(family.structure_morphism())
    special_fibre = adjunction.right_adjoint()(family_object)
    assert special_fibre in over_point
    assert special_fibre.arrow().codomain() is point
    fibre_algebra = special_fibre.arrow().domain().coordinate_algebra()
    assert fibre_algebra.algebra_generator("x") * fibre_algebra.algebra_generator("y") == fibre_algebra.zero()

    counit = adjunction.counit(family_object)
    assert counit.domain() is adjunction.left_adjoint()(special_fibre)
    assert counit.codomain() is family_object
    assert counit.left().codomain() is family

    unit = adjunction.unit(special_fibre)
    assert unit.domain() is special_fibre
    # Triangle identity at the special fibre: counit after Sigma(unit) is the identity.
    composite = counit * adjunction.left_adjoint()(unit)
    assert composite == over_line.Mor(composite.domain(), composite.codomain()).identity()
    assert composite.left() == adjunction.left_adjoint()(special_fibre).arrow().domain().categorical_identity_morphism()

    # The Hom-set bijection round-trips the identity of the pulled-back family.
    identity = over_point.Mor(special_fibre, special_fibre).identity()
    transposed = adjunction.hom_set_isomorphism_inverse(identity, codomain=family_object)
    assert transposed == counit
    back = adjunction.hom_set_isomorphism_forward(transposed, source=special_fibre)
    assert back == identity


def test_projective_space_base_change_is_the_selected_nonaffine_pullback() -> None:
    field, ring_map = _extension()
    line = ProjectiveSpaces(QQ)(1)
    change = Schemes(ring_map.domain()).base_change_functor(ring_map)

    ordinary_target_line = ProjectiveSpaces(field)(1)
    changed = change(line)

    assert changed is not ordinary_target_line
    assert ordinary_target_line not in FiberProductSchemes(field)
    assert changed in FiberProductSchemes(field)
    assert changed in ProjectiveSpaces(field)
    assert changed in ProjectiveSchemes(field)
    assert changed in Schemes(field).QuasiProjective()
    assert changed in Schemes(field).Separated()
    assert changed in Schemes(field).FiniteType()
    assert changed in SmoothSchemes(field)
    assert changed in IntegralSchemes(field)
    assert changed in NormalSchemes(field)
    assert changed.scheme_base_ring() is field
    assert changed.relative_dimension() == 1
    assert changed.fiber_product_base() is (QQ).affine_spectrum()
    assert changed.left_projection().codomain() is line
    assert changed.right_projection().codomain() is (field).affine_spectrum()

    left_square = line.structure_morphism() * changed.left_projection()
    right_square = change.base_morphism() * changed.right_projection()
    assert left_square == right_square

    factor = changed.from_pullback_cone(
        changed.left_projection(),
        changed.right_projection(),
    )
    assert factor.domain() is changed
    assert factor.codomain() is changed
    assert changed.left_projection() * factor == changed.left_projection()
    assert changed.right_projection() * factor == changed.right_projection()
