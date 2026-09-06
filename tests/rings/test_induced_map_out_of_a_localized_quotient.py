r"""The universal property of localization holds over a quotient-ring source.

The coordinate axes are \(A=\mathbf Q[x,y]/(xy)\).  Inverting \(\bar x\) gives
\(A[1/\bar x]\), the punctured \(x\)-axis, on which \(\bar y=0\) because
\(\bar x\bar y=0\) and \(\bar x\) is invertible.

\(A\) represents no division of one element by another, so the induced map has
to be computed from the numerator and the denominator a fraction already
carries.  That is the whole content of the universal property: a map out of
\(A\) carrying \(\bar x\) to a unit extends uniquely, by \(a/s\mapsto
g(a)g(s)^{-1}\).

Two targets.  The localization itself, where uniqueness makes the induced map
the identity; and \(\mathbf Q\), where evaluating \(\bar x\) at one and
\(\bar y\) at zero respects \(xy=0\) and sends \(\bar y/\bar x\) to zero.
"""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras import (
    FinitelyPresentedAlgebra,
    SymmetricAlgebraOn,
    algebra_homset,
)


def _axes_and_punctured_axis():
    r"""Return ``A = QQ[x,y]/(xy)``, its two generators, and ``A[1/x]``."""
    polynomial = SymmetricAlgebraOn(QQ, ("x", "y"))
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    axes = FinitelyPresentedAlgebra(polynomial, [x * y])
    return axes, axes.algebra_generator("x"), axes.algebra_generator("y")


def test_the_map_induced_by_the_localization_map_is_the_identity() -> None:
    axes, xbar, ybar = _axes_and_punctured_axis()
    punctured = axes.localization(xbar)

    induced = punctured.induced_morphism(punctured.localization_map())

    fraction = punctured.fraction(ybar, xbar)
    assert induced(fraction) == fraction
    assert induced(fraction) * punctured(xbar) == punctured(ybar)
    assert induced(punctured.fraction(axes.one(), xbar)) * punctured(xbar) == punctured.one()


def test_an_evaluation_that_inverts_the_character_extends_to_the_localization() -> None:
    axes, xbar, ybar = _axes_and_punctured_axis()
    punctured = axes.localization(xbar)
    evaluation = algebra_homset(axes, QQ)({"x": QQ.one(), "y": QQ.zero()})

    induced = punctured.induced_morphism(evaluation)

    assert induced.domain() is punctured
    assert induced.codomain() is QQ
    assert induced(punctured.fraction(ybar, xbar)) == QQ.zero()
    assert induced(punctured.fraction(axes.one(), xbar)) == QQ.one()
    assert induced(punctured.localization_map()(xbar)) == QQ.one()
