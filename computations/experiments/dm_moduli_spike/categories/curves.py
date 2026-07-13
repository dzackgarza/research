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


class StablePointedCurves(PointedCurves):
    r"""Stable `n`-pointed curves of genus `g` over `B` (DM compactification fibers)."""

    @staticmethod
    def __classcall_private__(
        cls,
        base: object,
        g: int | None = None,
        n: int | None = None,
    ) -> StablePointedCurves:
        from .base import AffineScheme

        if not isinstance(base, AffineScheme):
            raise TypeError(f"expected AffineScheme; found {type(base)}")
        if (g is None) ^ (n is None):
            raise TypeError("StablePointedCurves(B, g, n) requires both g and n, or neither")
        if g is not None:
            g = int(g)
            n = int(n)  # type: ignore[arg-type]
            if g < 0 or n < 0:
                raise ValueError(f"expected nonnegative (g, n); found ({g}, {n})")
            if 2 * g - 2 + n <= 0:
                raise ValueError(f"({g}, {n}) is not a stable range")
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
