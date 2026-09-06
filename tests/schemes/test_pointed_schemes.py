from dzack_research.preamble.all import AffineSpace, QQ, Schemes


def _origin_of_the_affine_line():
    r"""``Spec Q -> A^1_Q`` sending the coordinate to zero."""
    schemes = Schemes(QQ)
    base_scheme = schemes.base_scheme()
    line = AffineSpace(1, QQ, names=("x",))
    line_algebra = line.coordinate_algebra()
    base_algebra = base_scheme.coordinate_algebra()
    pullback = line_algebra.Mor(base_algebra)({"x": base_algebra.zero()})
    return schemes, base_scheme, line, base_scheme.Mor(line)(pullback)


def test_an_r_point_is_a_section_of_the_structure_morphism() -> None:
    r"""``Spec R -> X -> Spec R`` is the identity, which is what a point is."""
    _schemes, base_scheme, line, origin = _origin_of_the_affine_line()

    assert origin.domain() is base_scheme
    assert origin.codomain() is line
    assert line.structure_morphism() * origin == (
        base_scheme.categorical_identity_morphism()
    )


def test_a_pointed_scheme_is_an_object_of_the_coslice_under_the_base() -> None:
    r"""``Spec R / Sch_R`` holds the points; ``Sch_R / Spec R`` holds the families."""
    schemes, base_scheme, line, origin = _origin_of_the_affine_line()
    pointed = schemes.as_coslice_object(origin)
    family = schemes.as_slice_object(line)

    assert pointed in schemes.coslice_category()
    assert pointed.arrow() is origin
    assert schemes.coslice_category().base_object() is base_scheme

    assert family in schemes.slice_category()
    assert family.arrow() is line.structure_morphism()
    assert pointed not in schemes.slice_category()
