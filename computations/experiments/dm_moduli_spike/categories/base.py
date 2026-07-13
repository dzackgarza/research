r"""The :func:`spec` functor and affine schemes.

:func:`spec` is the functor from commutative rings to affine schemes.  Every
affine scheme `\mathrm{Spec}(R)` is a `\mathbb Z`-scheme via the canonical
structure morphism induced by `\mathbb Z \to R` (when `R` is a `\mathbb Z`-algebra).

Base change of the universal moduli stacks along `S \to \mathrm{Spec}(\mathbb Z)`
uses only that canonical morphism.  Users pass `S = \mathrm{Spec}(R)`; they do not
declare base rings or package ``Sch/B`` data by hand.
"""

from __future__ import annotations

from sage.rings.integer_ring import ZZ
from sage.structure.unique_representation import UniqueRepresentation


class AffineScheme(UniqueRepresentation):
    r"""Affine scheme `\mathrm{Spec}(R)`."""

    __slots__ = ("_ring", "_sage")

    def __init__(self, ring: object) -> None:
        from sage.schemes.generic.spec import Spec

        self._ring = ring
        self._sage = Spec(ring)

    def ring(self) -> object:
        return self._ring

    def sage_scheme(self) -> object:
        return self._sage

    def structure_target(self) -> AffineScheme:
        r"""Target of the canonical structure morphism `X \to \mathrm{Spec}(\mathbb Z)`."""
        return spec(ZZ)

    def is_z_scheme(self) -> bool:
        r"""True when the canonical `\mathbb Z \to R` algebra map exists."""
        ring = self._ring
        try:
            return ring.has_coerce_map_from(ZZ)  # type: ignore[attr-defined]
        except AttributeError:
            try:
                ring(ZZ.one())  # noqa: S101 — probe canonical Z embed
                return True
            except (TypeError, ValueError):
                return False

    def _repr_(self) -> str:
        return f"Spec({self._ring})"


def spec(ring: object) -> AffineScheme:
    r"""Functor `\mathrm{Spec}` from commutative rings to affine schemes."""
    return AffineScheme(ring)


def check_z_scheme(S: AffineScheme) -> None:
    r"""Require the canonical `\mathbb Z`-algebra structure on `S = \mathrm{Spec}(R)`."""
    if not S.is_z_scheme():
        raise TypeError(
            f"base change along the canonical map to Spec(ZZ) requires a Z-scheme; {S} is not"
        )


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
