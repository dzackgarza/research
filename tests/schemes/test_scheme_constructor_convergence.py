r"""Basic scheme notation delegates to the owning scheme categories."""

from dzack_research.preamble.all import (
    QQ,
    AffineSchemes,
    AffineSpaces,
    ProjectiveSpaces,
)


def test_spec_notation_is_the_affine_scheme_category_constructor() -> None:
    algebra = QQ.polynomial_ring("x")

    declared = AffineSchemes(QQ)(algebra)
    notation = (algebra).affine_spectrum(base_ring=QQ)

    assert declared is notation
    assert declared.coordinate_algebra() is algebra
    assert declared.scheme_base_ring() is QQ
    assert declared.structure_morphism().domain() is declared


def test_affine_space_notation_is_the_affine_space_category_constructor() -> None:
    declared = AffineSpaces(QQ)(2, names=("x", "y"))
    notation = AffineSpaces(QQ)(2, names=("x", "y"))

    assert declared is notation
    assert declared in AffineSpaces(QQ)
    assert declared.coordinate_algebra().algebra_generating_set().cardinality() == 2


def test_projective_space_notation_is_the_projective_space_category_constructor() -> None:
    declared = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    notation = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))

    assert declared is notation
    assert declared in ProjectiveSpaces(QQ)
    assert declared.scheme_base_ring() is QQ


def test_scheme_subobjects_retain_one_selected_inclusion_construction() -> None:
    line = AffineSpaces(QQ)(1, names=("x",))
    x = line.coordinate_algebra().algebra_generator("x")
    closed = line.closed_subscheme(x)
    opened = line.distinguished_open(x)

    assert closed.scheme_subobject_construction().inclusion() is closed.inclusion()
    assert closed.inclusion().codomain() is line
    assert opened.scheme_subobject_construction().inclusion() is opened.inclusion()
    assert opened.inclusion().codomain() is line
    assert (
        opened.scheme_subobject_construction().distinguished_open_element()
        == opened.distinguished_open_element()
        == x
    )
