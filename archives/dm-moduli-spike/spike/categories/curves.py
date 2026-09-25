r"""Categories of algebraic curves over a base scheme.

Hierarchy (over `B`):

.. code-block:: text

    Curves(B)
      ├── SmoothCurves(B)
      └── PointedCurves(B) / PointedCurves(B, g, n)
            ├── SmoothPointedCurves(B, g, n)   # join with SmoothCurves
            └── StablePointedCurves(B, g, I)   # nodal stable; not under Smooth

Pointed curves need not be smooth: boundary fibers of the DM compactification
are stable nodal pointed curves.
"""

from __future__ import annotations

from sage.categories.category import Category
from sage.structure.unique_representation import UniqueRepresentation

from .._typing_utils import as_int
from .base import AffineScheme
from .foundation import ModuliCategory
from .schemes import schemes_over


class Curves(ModuliCategory):
    r"""Algebraic curves over a base scheme `B`."""

    def super_categories(self) -> list[Category]:
        return [schemes_over(self.base_scheme())]

    def __contains__(self, obj: object) -> bool:
        from .membership import pointed_curve_in_category

        try:
            return bool(pointed_curve_in_category(obj, self) or super().__contains__(obj))
        except Exception:
            return bool(super().__contains__(obj))


class SmoothCurves(Curves):
    r"""Smooth curves over `B`."""

    def super_categories(self) -> list[Category]:
        return [Curves(self.base_scheme())]


class PointedCurves(Curves):
    r"""Pointed curves of genus `g` over `B` (not necessarily smooth).

    Call as ``PointedCurves(B)`` or ``PointedCurves(B, g, n)``.
    """

    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> PointedCurves:
        assert len(args) >= 1, "PointedCurves(B, g=None, n=None) requires base"
        base = args[0]
        g = args[1] if len(args) > 1 else kwargs.pop("g", None)
        n = args[2] if len(args) > 2 else kwargs.pop("n", None)
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        if (g is None) ^ (n is None):
            raise TypeError("PointedCurves(B, g, n) requires both g and n, or neither")
        gg: int | None = None
        nn: int | None = None
        if g is not None:
            gg = as_int(g)
            assert n is not None
            nn = as_int(n)
            if gg < 0 or nn < 0:
                raise ValueError(f"expected nonnegative (g, n); found ({gg}, {nn})")
        result = UniqueRepresentation.__classcall__(cls, base, gg, nn)
        assert isinstance(result, PointedCurves), f"classcall must return PointedCurves; found {type(result)!r}"
        return result

    def __init__(self, base: AffineScheme, g: int | None = None, n: int | None = None) -> None:
        self._g = g
        self._n = n
        Curves.__init__(self, base)

    def genus(self) -> int | None:
        return self._g

    def number_of_markings(self) -> int | None:
        return self._n

    def super_categories(self) -> list[Category]:
        return [Curves(self.base_scheme())]

    def __contains__(self, obj: object) -> bool:
        from .membership import pointed_curve_in_category

        try:
            if pointed_curve_in_category(obj, self):
                if self._g is not None and hasattr(obj, "arithmetic_genus"):
                    if int(obj.arithmetic_genus()) != self._g:
                        return False
                if self._n is not None and hasattr(obj, "number_of_markings"):
                    if int(obj.number_of_markings()) != self._n:
                        return False
                return True
            return super().__contains__(obj)
        except Exception:
            return super().__contains__(obj)


class SmoothPointedCurves(PointedCurves):
    r"""Smooth pointed curves: join of ``PointedCurves`` and ``SmoothCurves``."""

    def super_categories(self) -> list[Category]:
        base = self.base_scheme()
        if self._g is None:
            return [PointedCurves(base), SmoothCurves(base)]
        return [PointedCurves(base, self._g, self._n), SmoothCurves(base)]


class StablePointedCurves(PointedCurves):
    r"""Stable pointed curves of genus `g` over `B` (may be nodal).

    Not a subcategory of smooth curves.
    """

    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> StablePointedCurves:
        from collections.abc import Iterable

        from sage.rings.integer import Integer

        assert len(args) >= 1, "StablePointedCurves(B, g=None, n=None) requires base"
        base = args[0]
        g = args[1] if len(args) > 1 else kwargs.pop("g", None)
        n = args[2] if len(args) > 2 else kwargs.pop("n", None)
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        if (g is None) ^ (n is None):
            raise TypeError("StablePointedCurves(B, g, n) requires both g and n, or neither")
        gg: int | None = None
        nn: int | None = None
        if g is not None:
            gg = as_int(g)
            assert n is not None
            if isinstance(n, (int, Integer)):
                nn = as_int(n)
            else:
                assert isinstance(n, Iterable), f"expected marking count or iterable; found {type(n)!r}"
                nn = len(tuple(n))
            if gg < 0 or nn < 0:
                raise ValueError(f"expected nonnegative (g, n); found ({gg}, {nn})")
            if 2 * gg - 2 + nn <= 0:
                raise ValueError(f"({gg}, {nn}) is not a stable range")
        result = UniqueRepresentation.__classcall__(cls, base, gg, nn)
        assert isinstance(result, StablePointedCurves), f"classcall must return StablePointedCurves; found {type(result)!r}"
        return result

    def __init__(self, base: AffineScheme, g: int | None = None, n: int | None = None) -> None:
        self._g = g
        self._n = n
        Curves.__init__(self, base)

    def super_categories(self) -> list[Category]:
        base = self.base_scheme()
        if self._g is None:
            return [PointedCurves(base)]
        return [PointedCurves(base, self._g, self._n)]

    def __contains__(self, obj: object) -> bool:
        from .membership import pointed_curve_in_category

        try:
            if pointed_curve_in_category(obj, self):
                if self._g is not None and hasattr(obj, "arithmetic_genus"):
                    if int(obj.arithmetic_genus()) != self._g:
                        return False
                if self._n is not None and hasattr(obj, "number_of_markings"):
                    if int(obj.number_of_markings()) != self._n:
                        return False
                return True
            return False
        except Exception:
            return False


def _marking_tuple(I: object) -> tuple[object, ...]:
    from collections.abc import Iterable

    from sage.rings.integer import Integer

    if isinstance(I, (int, Integer)):
        return tuple(range(1, int(I) + 1))
    assert isinstance(I, Iterable), f"expected marking count or iterable; found {type(I)!r}"
    return tuple(I)


class CurveFamilies(ModuliCategory):
    r"""Families of curves over a base scheme `S`."""

    def super_categories(self) -> list[Category]:
        return [schemes_over(self.base_scheme())]

    def __contains__(self, obj: object) -> bool:
        from ..curves.families import CurveFamily

        return isinstance(obj, CurveFamily)


class PointedCurveFamilies(CurveFamilies):
    r"""Families of pointed curves with marking set `I` over `S`."""

    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> PointedCurveFamilies:
        assert len(args) >= 1, "PointedCurveFamilies(B, I=None) requires base"
        base = args[0]
        I = args[1] if len(args) > 1 else kwargs.pop("I", None)
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        marks = None if I is None else _marking_tuple(I)
        result = UniqueRepresentation.__classcall__(cls, base, marks)
        assert isinstance(result, PointedCurveFamilies), f"classcall must return PointedCurveFamilies; found {type(result)!r}"
        return result

    def __init__(self, base: AffineScheme, I: tuple[object, ...] | None = None) -> None:
        self._I = I
        CurveFamilies.__init__(self, base)

    def marking_set(self) -> tuple[object, ...] | None:
        return self._I

    def super_categories(self) -> list[Category]:
        return [CurveFamilies(self.base_scheme())]

    def __contains__(self, obj: object) -> bool:
        from ..curves.families import PointedCurveFamily

        if not isinstance(obj, PointedCurveFamily):
            return False
        if self._I is not None and tuple(obj.marking_set()) != tuple(self._I):
            return False
        return True


class StablePointedCurveFamilies(PointedCurveFamilies):
    r"""Families of stable pointed curves of genus `g` with markings `I` over `S`."""

    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> StablePointedCurveFamilies:
        assert len(args) >= 1, "StablePointedCurveFamilies(S, g=None, I=None) requires base"
        base = args[0]
        g = args[1] if len(args) > 1 else kwargs.pop("g", None)
        I = args[2] if len(args) > 2 else kwargs.pop("I", None)
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        if (g is None) ^ (I is None):
            raise TypeError("StablePointedCurveFamilies(S, g, I) requires both g and I, or neither")
        marks = None if I is None else _marking_tuple(I)
        gg = None if g is None else as_int(g)
        if gg is not None and marks is not None and 2 * gg - 2 + len(marks) <= 0:
            raise ValueError(f"({gg}, {len(marks)}) is not a stable range")
        result = UniqueRepresentation.__classcall__(cls, base, gg, marks)
        assert isinstance(result, StablePointedCurveFamilies), f"classcall must return StablePointedCurveFamilies; found {type(result)!r}"
        return result

    def __init__(self, base: AffineScheme, g: int | None = None, I: tuple[object, ...] | None = None) -> None:
        self._g = g
        self._I = I
        CurveFamilies.__init__(self, base)

    def genus(self) -> int | None:
        return self._g

    def marking_set(self) -> tuple[object, ...] | None:
        return self._I

    def super_categories(self) -> list[Category]:
        base = self.base_scheme()
        if self._I is None:
            return [PointedCurveFamilies(base)]
        return [PointedCurveFamilies(base, self._I)]

    def __contains__(self, obj: object) -> bool:
        from ..curves.families import StablePointedCurveFamily

        if not isinstance(obj, StablePointedCurveFamily):
            return False
        if self._g is not None and int(obj.genus()) != self._g:
            return False
        if self._I is not None and tuple(obj.marking_set()) != tuple(self._I):
            return False
        return True
