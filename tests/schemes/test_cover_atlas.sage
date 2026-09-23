r"""Distinguished open covers of the affine line."""

from dzack_research.preamble.all import *


def test_intersections_of_distinguished_opens_of_the_line_are_distinguished_by_the_product() -> None:
    r"""On \(\mathbf A^1_{\mathbf Q}\), \(D(f)\cap D(g) = D(fg)\), independently of the order of the factors; the opens
    \(D(x), D(1-x), D(2-x)\) cover the line since \(x + (1-x) = 1\).

    Source: Hartshorne, *Algebraic Geometry*, II.2 (distinguished opens); Stacks Project, Tag 01HR.
    """
    R = QQ["x"]
    x = R.gen()
    line = Schemes(QQ)(R)
    cover = line.distinguished_open_cover(x, 1 - x, 2 - x)

    assert cover.intersection(0, 1).distinguished_open_element() == x * (1 - x)
    assert cover.intersection(1, 0).distinguished_open_element() == x * (1 - x)
    assert cover.intersection(0, 1, 2).distinguished_open_element() == x * (1 - x) * (2 - x)
    assert R.ideal(x, 1 - x, 2 - x) == R.ideal(R.one())
