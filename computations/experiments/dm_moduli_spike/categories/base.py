r"""Schemes, the :func:`spec` functor, and objects of `\mathrm{Sch}/B`.

* :func:`spec` is the functor from commutative rings to affine schemes.
* :class:`SchemeOver` records an object `X \to B` of `\mathrm{Sch}/B` (here,
  affine on both sides).
* Base change along `S \to \mathrm{Spec}(\mathbb Z)` is recorded by pairing a
  universal moduli object with a :class:`SchemeOver` base; `S`-points are the
  same data.
"""

from __future__ import annotations

from sage.structure.unique_representation import UniqueRepresentation


class AffineScheme(UniqueRepresentation):
    r"""Affine scheme `\mathrm{Spec}(R)` for a commutative ring `R`."""

    __slots__ = ("_ring", "_sage")

    def __init__(self, ring: object) -> None:
        from sage.schemes.generic.spec import Spec

        self._ring = ring
        self._sage = Spec(ring)

    def ring(self) -> object:
        return self._ring

    def sage_scheme(self) -> object:
        return self._sage

    def _repr_(self) -> str:
        return f"Spec({self._ring})"


def spec(ring: object) -> AffineScheme:
    r"""Functor `\mathrm{Spec}` from commutative rings to affine schemes."""
    return AffineScheme(ring)


class SchemeOver(UniqueRepresentation):
    r"""Object `X \to B` of `\mathrm{Sch}/B` (affine `X`, affine base `B`)."""

    __slots__ = ("_scheme", "_base")

    def __init__(self, scheme: AffineScheme, base: AffineScheme) -> None:
        if not isinstance(scheme, AffineScheme) or not isinstance(base, AffineScheme):
            raise TypeError("expected AffineScheme arguments")
        self._scheme = scheme
        self._base = base

    def scheme(self) -> AffineScheme:
        r"""The scheme `X`."""
        return self._scheme

    def base(self) -> AffineScheme:
        r"""The base `B` in `\mathrm{Sch}/B`."""
        return self._base

    def sage_scheme(self) -> object:
        return self._scheme.sage_scheme()

    def _repr_(self) -> str:
        return f"{self._scheme} over {self._base}"


def scheme_over(ring: object, *, base_ring: object) -> SchemeOver:
    r"""\mathrm{Spec}(R) as an object of `\mathrm{Sch}/\mathrm{Spec}(R_0)` via `R_0 \to R`."""
    return SchemeOver(spec(ring), spec(base_ring))


def complex_numbers_ring() -> object:
    r"""\mathbb C \cong \mathbb R[x]/(x^2+1)` with formal generator `i`."""
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
    from sage.rings.real_mpfr import RR

    R = PolynomialRing(RR, names="i")
    i = R.gen()
    return R.quotient(R.ideal(i**2 + 1))


def spec_complex() -> AffineScheme:
    r"""\mathrm{Spec}(\mathbb C)` for the symbolic model :func:`complex_numbers_ring`."""
    return spec(complex_numbers_ring())
