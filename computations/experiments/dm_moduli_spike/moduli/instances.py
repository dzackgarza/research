r"""Named moduli-stack instances."""

from __future__ import annotations

from ..categories.base import SchemeOver
from .stack import DeligneMumfordModuliStack, DeligneMumfordModuliStackOver


def M_gn(g: int, n: int) -> DeligneMumfordModuliStack:
    r"""Universal open stack `\mathcal M_{g,n} \to \mathrm{Spec}(\mathbb Z)`."""
    return DeligneMumfordModuliStack(g, n, proper=False)


def Mbar_gn(g: int, n: int) -> DeligneMumfordModuliStack:
    r"""Universal proper stack `\overline{\mathcal M}_{g,n} \to \mathrm{Spec}(\mathbb Z)`."""
    return DeligneMumfordModuliStack(g, n, proper=True)


def M_gn_base_change(g: int, n: int, base: SchemeOver) -> DeligneMumfordModuliStackOver:
    r"""Base change `\mathcal M_{g,n} \times_{\mathrm{Spec}(\mathbb Z)} S`."""
    return M_gn(g, n).base_change(base)


def Mbar_gn_base_change(g: int, n: int, base: SchemeOver) -> DeligneMumfordModuliStackOver:
    r"""Base change `\overline{\mathcal M}_{g,n} \times_{\mathrm{Spec}(\mathbb Z)} S`."""
    return Mbar_gn(g, n).base_change(base)
