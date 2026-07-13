r"""Lightweight Sage categories carrying a :class:`ModuliBase`."""

from __future__ import annotations

from sage.categories.category import Category

from .base import ModuliBase, default_base


class ModuliCategory(Category):
    r"""Category over an abstract moduli base (not numerical ``CC``)."""

    @staticmethod
    def __classcall_private__(cls, base: ModuliBase | None = None) -> ModuliCategory:
        if base is None:
            base = default_base()
        if not isinstance(base, ModuliBase):
            raise TypeError(f"expected ModuliBase; found {type(base)}")
        return super().__classcall__(cls, base)

    def __init__(self, base: ModuliBase) -> None:
        self._moduli_base = base
        Category.__init__(self)

    def moduli_base(self) -> ModuliBase:
        return self._moduli_base

    def base_ring(self) -> object:
        return self._moduli_base.sage_ring()
