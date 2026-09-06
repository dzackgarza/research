r"""An adopted ring acts on itself as a module without hand-written state.

A number field \(K\) is an algebra over \(\mathbf Q\), hence a
\(\mathbf Q\)-module, whether the preamble adopts a Sage parent for it or
constructs it from a presentation.  The module level owes such a parent two
things: the scalar ring it is a module over, and the action of that ring on
its elements.  Both come from the construction, so \(r\cdot x\) is ordinary
multiplication syntax and no leaf writes anything about its scalars.

The specimens are the Gaussian field \(\mathbf Q(i)\), which the preamble
adopts, and its chosen presentation \(\mathbf Q[x]/(x^2+1)\), which the
preamble constructs.  The assertions are the module axioms the action has to
satisfy on the generator \(i\): repeated addition is multiplication by an
integer scalar, and halving twice recovers the element.
"""

from dzack_research.preamble.all import (
    Modules,
    QQ,
    QuadraticField,
)


def _half():
    return QQ(1) / QQ(2)


def test_the_rationals_act_on_the_adopted_gaussian_field() -> None:
    gaussian = QuadraticField(-1, "i")
    primitive = gaussian.primitive_element()

    assert gaussian.base_ring() is QQ
    assert gaussian in Modules(QQ)
    assert QQ(3) * primitive == primitive + primitive + primitive
    assert _half() * primitive + _half() * primitive == primitive


def test_the_rationals_act_on_the_presented_gaussian_algebra() -> None:
    gaussian = QuadraticField(-1, "i").as_algebra()
    primitive = gaussian.algebra_generator("i")

    assert gaussian.base_ring() is QQ
    assert gaussian in Modules(QQ)
    assert QQ(3) * primitive == primitive + primitive + primitive
    assert _half() * primitive + _half() * primitive == primitive
