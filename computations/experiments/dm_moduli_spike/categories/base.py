r"""Abstract base rings for moduli semantics.

Numerical :class:`sage.rings.complex_double.ComplexField` (``CC``) is inexact.
The default base is :class:`sage.rings.qqbar.QQbar`, an exact algebraically closed
subfield of `\mathbf C` suitable for algebraic-geometric membership tests.
"""

from __future__ import annotations

from sage.structure.unique_representation import UniqueRepresentation


class ModuliBase(UniqueRepresentation):
    r"""Exact/abstract base field object for moduli and coarse-space semantics."""

    def __init__(self) -> None:
        from sage.rings.qqbar import QQbar

        self._ring = QQbar

    def sage_ring(self) -> object:
        return self._ring

    def _repr_(self) -> str:
        return "ModuliBase(QQbar)"


def default_base() -> ModuliBase:
    return ModuliBase()


def ComplexNumbers() -> ModuliBase:
    r"""Exact algebraic base standing in for `\mathbf C` (not numerical ``CC``)."""
    return ModuliBase()
