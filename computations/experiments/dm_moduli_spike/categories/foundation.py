r"""Lightweight Sage categories over a base `B` in `\mathrm{Sch}/B`."""

from __future__ import annotations

from sage.categories.category import Category

from .base import AffineScheme, spec


class ModuliCategory(Category):
    r"""Category of objects over a fixed base scheme `B`."""

    @staticmethod
    def __classcall_private__(cls, base: AffineScheme | None = None) -> ModuliCategory:
        if base is None:
            from sage.rings.integer_ring import ZZ

            base = spec(ZZ)
        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        return super().__classcall__(cls, base)

    def __init__(self, base: AffineScheme) -> None:
        self._base = base
        Category.__init__(self)

    def base_scheme(self) -> AffineScheme:
        return self._base
