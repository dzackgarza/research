r"""Categories of algebraic curves over a base scheme.

Hierarchy (over `B` in `\mathrm{Sch}/B`):

.. code-block:: text

    ModuliCategory(B)
      └── Curves(B)
            └── SmoothCurves(B)
                  └── PointedCurves(B) / PointedCurves(B, g, n)
                        └── StablePointedCurves(B, g, n)

These declare the geometric hierarchy.  Concrete curve *objects* are Sage
:class:`~sage.schemes.curves.curve.Curve_generic` instances wrapped in
:mod:`dm_moduli_spike._landscape.curves.pointed`.  This package does **not**
claim Sage supplies Deligne--Mumford stacks or a universal family over
`\mathcal M_{g,n}`.
"""

from __future__ import annotations

from sage.categories.category import Category

from .foundation import ModuliCategory
from .schemes import Schemes


class Curves(ModuliCategory):
    r"""Algebraic curves over a base scheme `B`."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.base_scheme())]

    def __contains__(self, obj: object) -> bool:
        from .membership import pointed_curve_in_category

        try:
            return pointed_curve_in_category(obj, self) or super().__contains__(obj)
        except Exception:
            return super().__contains__(obj)


class SmoothCurves(Curves):
    r"""Smooth curves over `B`."""

    def super_categories(self) -> list[Category]:
        return [Curves(self.base_scheme())]


class PointedCurves(SmoothCurves):
    r"""Smooth `n`-pointed curves of genus `g` over `B`.

    Call as ``PointedCurves(B)`` for the untyped pointed-curve category, or
    ``PointedCurves(B, g, n)`` to fix genus and marking count.
    """

    @staticmethod
    def __classcall_private__(
        cls,
        base: object,
        g: int | None = None,
        n: int | None = None,
    ) -> PointedCurves:
        from .base import AffineScheme

        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        if (g is None) ^ (n is None):
            raise TypeError("PointedCurves(B, g, n) requires both g and n, or neither")
        if g is not None:
            g = int(g)
            n = int(n)  # type: ignore[arg-type]
            if g < 0 or n < 0:
                raise ValueError(f"expected nonnegative (g, n); found ({g}, {n})")
        return super().__classcall__(cls, base, g, n)

    def __init__(self, base: object, g: int | None = None, n: int | None = None) -> None:
        self._g = g
        self._n = n
        SmoothCurves.__init__(self, base)

    def genus(self) -> int | None:
        return self._g

    def number_of_markings(self) -> int | None:
        return self._n

    def super_categories(self) -> list[Category]:
        return [SmoothCurves(self.base_scheme())]

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


class StablePointedCurves(PointedCurves):
    r"""Stable `n`-pointed curves of genus `g` over `B` (DM compactification fibers).

    Call as ``StablePointedCurves(B, g, n)`` or ``StablePointedCurves(B, g, I)``
    with a finite marking set ``I``.
    """

    @staticmethod
    def __classcall_private__(
        cls,
        base: object,
        g: int | None = None,
        n: object | None = None,
    ) -> StablePointedCurves:
        from sage.rings.integer import Integer

        from .base import AffineScheme

        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        if (g is None) ^ (n is None):
            raise TypeError("StablePointedCurves(B, g, n) requires both g and n, or neither")
        if g is not None:
            g = int(g)
            if isinstance(n, (int, Integer)):
                nn = int(n)
            else:
                nn = len(tuple(n))  # type: ignore[arg-type]
            if g < 0 or nn < 0:
                raise ValueError(f"expected nonnegative (g, n); found ({g}, {nn})")
            if 2 * g - 2 + nn <= 0:
                raise ValueError(f"({g}, {nn}) is not a stable range")
            n = nn
        return super(PointedCurves, cls).__classcall__(cls, base, g, n)

    def __init__(self, base: object, g: int | None = None, n: int | None = None) -> None:
        self._g = g
        self._n = n
        # Skip PointedCurves.__init__ UniqueRepresentation path; init as SmoothCurves.
        SmoothCurves.__init__(self, base)

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
            return super().__contains__(obj)
        except Exception:
            return super().__contains__(obj)


def _marking_tuple(I: object) -> tuple[object, ...]:
    from sage.rings.integer import Integer

    if isinstance(I, (int, Integer)):
        return tuple(range(1, int(I) + 1))
    return tuple(I)


class CurveFamilies(ModuliCategory):
    r"""Families of curves over a base scheme `S`."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.base_scheme())]

    def __contains__(self, obj: object) -> bool:
        from ..curves.families import CurveFamily

        return isinstance(obj, CurveFamily)


class PointedCurveFamilies(CurveFamilies):
    r"""Families of pointed curves with marking set `I` over `S`."""

    @staticmethod
    def __classcall_private__(cls, base: object, I: object | None = None) -> PointedCurveFamilies:
        from .base import AffineScheme

        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        marks = None if I is None else _marking_tuple(I)
        return super().__classcall__(cls, base, marks)

    def __init__(self, base: object, I: tuple[object, ...] | None = None) -> None:
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
    def __classcall_private__(
        cls,
        base: object,
        g: int | None = None,
        I: object | None = None,
    ) -> StablePointedCurveFamilies:
        from .base import AffineScheme

        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        if (g is None) ^ (I is None):
            raise TypeError("StablePointedCurveFamilies(S, g, I) requires both g and I, or neither")
        marks = None if I is None else _marking_tuple(I)
        gg = None if g is None else int(g)
        if gg is not None and marks is not None and 2 * gg - 2 + len(marks) <= 0:
            raise ValueError(f"({gg}, {len(marks)}) is not a stable range")
        return super(PointedCurveFamilies, cls).__classcall__(cls, base, gg, marks)

    def __init__(self, base: object, g: int | None = None, I: tuple[object, ...] | None = None) -> None:
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
