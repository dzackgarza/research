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

from .._sage_types import SageRing


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
        if isinstance(ring, SageRing):
            return bool(ring.has_coerce_map_from(ZZ))
        try:
            assert callable(ring), f"ring must be callable for Z-embed probe; found {type(ring)!r}; ring={ring!r}; owned boundary=AffineScheme.is_z_scheme"
            ring(ZZ.one())
            return True
        except TypeError, ValueError, AttributeError:
            return False

    def standard_open(self, element: object) -> AffineScheme:
        r"""Standard open `D(f) = \mathrm{Spec}(R_f)` for `f \in R`.

        Localization uses Sage's ``ring.localization(element)`` when available.
        The open immersion `D(f) \hookrightarrow \mathrm{Spec}(R)` is formally étale
        (flat + unramified); see :class:`~dm_moduli_spike.geometry.stacks.FormallyEtaleSchemeCertificate`.
        """
        ring = self._ring
        assert hasattr(ring, "localization"), f"ring must expose localization() for standard opens; found {type(ring)!r}"
        localized = ring.localization(element)
        return AffineScheme(localized)

    def _repr_(self) -> str:
        return f"Spec({self._ring})"


def spec(ring: object) -> AffineScheme:
    r"""Functor `\mathrm{Spec}` from commutative rings to affine schemes."""
    return AffineScheme(ring)


def check_z_scheme(S: AffineScheme) -> None:
    r"""Require the canonical `\mathbb Z`-algebra structure on `S = \mathrm{Spec}(R)`."""
    if not S.is_z_scheme():
        raise TypeError(f"base change along the canonical map to Spec(ZZ) requires a Z-scheme; {S} is not")


def complex_numbers_ring() -> object:
    r"""Exact algebraic surrogate for `\mathbf C`: the field of algebraic numbers.

    Uses ``QQbar``, not a floating ``RR[i]/(i^2+1)`` model.
    """
    from sage.rings.qqbar import QQbar

    return QQbar


def spec_complex() -> AffineScheme:
    r"""``Spec(QQbar)`` as an exact surrogate for ``Spec(\mathbf C)``."""
    return spec(complex_numbers_ring())
