"""Form-value objects K/R for the synthetic lattice category.

A symmetric form does not land in the base ring R once it descends to a finite
quotient; it lands in a quotient module K/R (bilinear) or K/2R (quadratic), where
K = Frac(R). This module exposes a thin K/R-shaped interface for those value objects.

v1 concrete path (RAT-value-ring): R = ZZ, K = QQ, so the value objects are
QQ/(level * ZZ). Sage already provides exactly these as ``QmodnZ`` (Q/nZ,
``sage.groups.additive_abelian.qmodnz``): the bilinear value module is QQ/ZZ and the
even-quadratic value module is QQ/2ZZ. We REUSE QmodnZ rather than duplicate it.

General Dedekind K/R is explicitly OUT of v1 scope: a non-ZZ base ring fails loud.
"""

from __future__ import annotations

from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ


def value_module(base_ring=ZZ, level=ZZ.one()):
    """The K/R form-value object K/(level * R), K = Frac(R).

    For R = ZZ this is QQ/(level * ZZ), returned as a Sage ``QmodnZ``:
    ``value_module(ZZ, 1)`` is QQ/ZZ (bilinear values), ``value_module(ZZ, 2)`` is
    QQ/2ZZ (even-quadratic values). A form value is then a rational mod level*ZZ.

    Only R = ZZ is in v1 scope; any other base ring fails loud.
    """
    if base_ring is not ZZ:
        raise NotImplementedError(
            "K/R value objects are implemented only for R=ZZ in this spike "
            f"(general Dedekind K/R is out of v1 scope); found R={base_ring}"
        )
    return QmodnZ(QQ(level))


def bilinear_value_module(base_ring=ZZ):
    """The bilinear form-value object K/R (QQ/ZZ for R = ZZ)."""
    return value_module(base_ring, ZZ.one())


def quadratic_value_module(base_ring=ZZ, level=2 * ZZ.one()):
    """The quadratic form-value object K/(level * R) (QQ/2ZZ for the even case)."""
    return value_module(base_ring, level)


if __name__ == "__main__":
    # ponytail: one self-check that fails if the K/R wiring breaks.
    import sage.all  # noqa: F401  # standalone run needs Sage lazy imports resolved
    b = bilinear_value_module()
    q = quadratic_value_module()
    assert b is QmodnZ(QQ(1)) and b.n == 1, b
    assert q is QmodnZ(QQ(2)) and q.n == 2, q
    assert b(QQ(2) / 3) == b(QQ(2) / 3 + 1)  # QQ/ZZ collapses integer shifts
    assert value_module(ZZ, 1) == QmodnZ(QQ(1))
    try:
        value_module(QQ)
    except NotImplementedError:
        pass
    else:
        raise AssertionError("non-ZZ base ring must fail loud")
    print("value_objects self-check ok")
