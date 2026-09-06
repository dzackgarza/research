r"""Fixed loci of single automorphisms, restricted actions, and free actions.

Two specimens carry the mathematics.  The Artin--Schreier translation
``x -> x + 1`` of the affine line over ``GF(2)`` generates a free action: its
equalizer with the identity is empty because ``1 = 0`` has no solutions.  The
Klein four-group acting on the affine plane over ``GF(2)`` by a translation
and a shear has *no* common fixed point while one of its involutions has a
whole curve of them, which is why an empty ``X^G`` never implies freeness.
"""

from dzack_research.preamble.all import (
    GF,
    GObjects,
    Groups,
    PolynomialRing,
    Schemes,
    Spec,
    SpecFunctor,
)


def _translation_of_the_affine_line():
    r"""``C_2`` acting on ``A^1_{GF(2)}`` by ``x -> x + 1``."""
    field = GF(2)
    group = Groups.C(2)
    algebra = PolynomialRing(field, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    translation = SpecFunctor(field)(algebra.Mor(algebra)({"x": x + algebra.one()}))
    identity = scheme.categorical_identity_morphism()
    acted = GObjects(group, Schemes(field))(
        scheme,
        lambda element: identity if element == group.one() else translation,
    )
    return field, group, algebra, x, acted


def _klein_four_on_the_affine_plane():
    r"""``V_4`` acting on ``A^2_{GF(2)}`` by ``x -> x + 1`` and ``y -> y + x^2 + x``.

    Both commute and both are involutions in characteristic two, so the two
    chosen elements generate a Klein four-group; the shear is fixed exactly on
    ``x^2 + x = 0`` while the translation is fixed nowhere.
    """
    field = GF(2)
    symmetric = Groups.S(4)
    involutions = tuple(
        element for element in symmetric if element.order() == 2
    )
    first, second = next(
        (left, right)
        for left in involutions
        for right in involutions
        if left != right
        and left * right == right * left
        and (left * right).order() == 2
    )
    group = symmetric.subgroup([first, second])

    algebra = PolynomialRing(field, ("x", "y"))
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    scheme = Spec(algebra)
    translation = SpecFunctor(field)(
        algebra.Mor(algebra)({"x": x + algebra.one(), "y": y})
    )
    shear = SpecFunctor(field)(algebra.Mor(algebra)({"x": x, "y": y + x**2 + x}))
    identity = scheme.categorical_identity_morphism()

    generators = tuple(group.group_generators())
    images = {
        group.one(): identity,
        generators[0]: translation,
        generators[1]: shear,
        generators[0] * generators[1]: translation * shear,
    }
    acted = GObjects(group, Schemes(field))(scheme, lambda element: images[element])
    return field, group, algebra, x, y, generators, acted


def test_the_artin_schreier_translation_acts_freely_on_the_affine_line() -> None:
    field, group, algebra, _x, acted = _translation_of_the_affine_line()

    assert acted in GObjects(group, Schemes(field))
    # x + 1 = x has no solutions, so the equalizer with the identity is empty.
    assert acted.fixed_ideal().contains_ambient_element(algebra.one())
    assert acted.action_is_free() is True


def test_the_sign_of_a_translation_is_that_squaring_it_returns_the_identity() -> None:
    _field, group, algebra, x, acted = _translation_of_the_affine_line()
    generator = group.group_generators().unrank(0)
    pullback = acted.action_of(generator).coordinate_algebra_morphism()

    assert pullback(x) == x + algebra.one()
    assert pullback(pullback(x)) == x
    assert (
        acted.action_of(generator) * acted.action_of(generator)
        == acted.categorical_identity_morphism()
    )


def test_an_empty_common_fixed_locus_does_not_make_the_action_free() -> None:
    _field, _group, algebra, x, _y, generators, acted = _klein_four_on_the_affine_plane()

    # No point of the plane is fixed by the translation, hence none by V_4.
    assert acted.fixed_ideal().contains_ambient_element(algebra.one())
    # The shear fixes the curve x^2 + x = 0, so the action is not free.
    assert acted.action_is_free() is False
    shear_locus = acted.fixed_subobject_of(generators[1])
    assert shear_locus.defining_ideal_owned() == algebra.ideal(x**2 + x)
    assert shear_locus.ambient_scheme().acting_group().order() == 2
    # Only the shear has fixed points, so the union of the fixed loci of the
    # three involutions is the shear's own curve.
    assert acted.nontrivial_stabilizer_subscheme().defining_ideal_owned() == algebra.ideal(
        x**2 + x
    )


def test_restriction_along_a_subgroup_inclusion_keeps_the_scheme_and_the_action() -> None:
    field, group, algebra, x, y, generators, acted = _klein_four_on_the_affine_plane()
    shear_subgroup = group.subgroup([generators[1]])
    restriction = GObjects(group, Schemes(field)).restriction(shear_subgroup.inclusion())
    restricted = restriction(acted)

    assert restricted.acting_group() is shear_subgroup
    assert restricted.coordinate_algebra() is algebra
    original = acted.action_of(generators[1]).coordinate_algebra_morphism()
    transported = restricted.action_of(generators[1]).coordinate_algebra_morphism()
    assert transported(y) == original(y) == y + x**2 + x
    assert restricted.fixed_ideal() == algebra.ideal(x**2 + x)

    equivariant_identity = GObjects(group, Schemes(field)).Mor(acted, acted).identity()
    image = restriction(equivariant_identity)
    assert image.domain() is restricted
    assert image.underlying_arrow().coordinate_algebra_morphism()(x) == x
