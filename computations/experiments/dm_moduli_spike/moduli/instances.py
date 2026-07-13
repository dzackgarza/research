r"""Named moduli-stack instances."""

from __future__ import annotations

from ..categories import ComplexNumbers, default_base
from ..categories.base import ModuliBase
from .stack import DeligneMumfordModuliStack


def M_gn(g: int, n: int, base: ModuliBase | None = None) -> DeligneMumfordModuliStack:
    r"""Open Deligne--Mumford stack `\mathcal M_{g,n}` of smooth pointed curves."""
    return DeligneMumfordModuliStack(g, n, base if base is not None else default_base(), proper=False)


def Mbar_gn(g: int, n: int, base: ModuliBase | None = None) -> DeligneMumfordModuliStack:
    r"""Proper Deligne--Mumford stack `\overline{\mathcal M}_{g,n}` of stable pointed curves."""
    return DeligneMumfordModuliStack(g, n, base if base is not None else default_base(), proper=True)
