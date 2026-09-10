r"""Archive reconciliation for open subschemes through distinguished opens.

The archived open-subscheme role supplied only the chosen immersion.  The live
scheme owner represents the standard affine case more strongly: ``D(f)`` is an
actual scheme subobject whose inclusion is induced by ``A -> A[1/f]`` and
retains the distinguished element.  Nested distinguished opens retain their
actual inclusion morphism as well.
"""

from dzack_research.preamble.all import AffineSpace, OpenImmersions, QQ, Schemes


def test_distinguished_open_is_the_live_open_subobject_with_localized_algebra() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    x, _y = plane.coordinate_algebra().algebra_generators()
    open_x = plane.distinguished_open(x)

    assert open_x in Schemes(QQ)
    assert open_x in OpenImmersions(plane)
    assert open_x.inclusion().domain() is open_x
    assert open_x.inclusion().codomain() is plane
    assert open_x.is_distinguished_open()
    assert open_x.distinguished_open_element() == x

    localization = open_x.inclusion().coordinate_algebra_morphism()
    assert localization.domain() is plane.coordinate_algebra()
    assert localization.codomain() is open_x.coordinate_algebra()
    assert localization(x).is_unit()


def test_nested_distinguished_open_retains_the_actual_open_immersion() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    x, y = plane.coordinate_algebra().algebra_generators()
    open_x = plane.distinguished_open(x)
    open_xy = plane.distinguished_open(x * y)

    inclusion = open_xy.inclusion_into(open_x)

    assert open_xy in OpenImmersions(plane)
    assert open_x in OpenImmersions(plane)
    assert inclusion.domain() is open_xy
    assert inclusion.codomain() is open_x
    assert open_x.inclusion() * inclusion == open_xy.inclusion()
