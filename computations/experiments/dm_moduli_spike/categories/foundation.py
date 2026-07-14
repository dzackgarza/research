r"""Lightweight Sage categories over a base `B` in `\mathrm{Sch}/B`."""

from __future__ import annotations

from sage.categories.category import Category
from sage.structure.unique_representation import UniqueRepresentation

from .base import AffineScheme, spec


class ModuliCategory(Category):
    r"""Category of objects over a fixed base scheme `B`."""

    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> ModuliCategory:
        if args:
            base_arg = args[0]
            rest = args[1:]
        else:
            base_arg = kwargs.pop("base", None)
            rest = ()
        assert not kwargs, f"unexpected ModuliCategory classcall kwargs {sorted(kwargs)!r}; owned boundary=ModuliCategory.__classcall_private__"
        base: AffineScheme
        if base_arg is None:
            from sage.rings.integer_ring import ZZ

            base = spec(ZZ)
        else:
            assert isinstance(base_arg, AffineScheme), f"expected AffineScheme; found {type(base_arg)!r}; owned boundary=ModuliCategory.__classcall_private__"
            base = base_arg
        result = UniqueRepresentation.__classcall__(cls, base, *rest)
        assert isinstance(result, ModuliCategory), f"UniqueRepresentation classcall must return ModuliCategory; found {type(result)!r}"
        return result

    def __init__(self, base: AffineScheme, *args: object, **kwargs: object) -> None:
        self._base = base
        self._axioms: frozenset[str] = frozenset()
        Category.__init__(self)

    def base_scheme(self) -> AffineScheme:
        return self._base

    def _repr_object_names(self) -> str:
        return self.__class__.__name__
