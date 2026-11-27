"""Refine Sage ideal and quotient objects as enriched module subobjects.

After ModuleBaseRings installation, this patch intercepts ideal construction
(R.ideal, r*R, R*r) and quotient construction (R/I) on target rings, adding
Modules(R) category membership so that ideals carry submodule semantics and
quotients carry module-object semantics.

Does NOT reimplement ideal arithmetic or quotient arithmetic — only adds
category metadata.
"""

from __future__ import annotations

from typing import Any

from sage.all import Modules
from sage.categories.rings import Rings
from sage.rings.ideal import Ideal_generic

_installed = False

# Store native methods before patching
_native_ring_ideal = Rings().parent_class.ideal
_native_ring_truediv = None  # set during install if available


def _refine_ideal_as_module(ideal: Any) -> Any:
    """Refine a Sage ideal as a module subobject of the ring-as-module."""
    ring = ideal.ring()
    ideal._refine_category_(Modules(ring))
    return ideal


def _module_aware_ideal(self: Any, *args: Any, **kwds: Any) -> Any:
    """Intercept Ring.ideal to refine output as a module subobject."""
    result = _native_ring_ideal(self, *args, **kwds)
    return _refine_ideal_as_module(result)


def _module_aware_mul(self: Any, other: Any) -> Any:
    """Intercept Ring.__mul__ to refine ideal outputs."""
    result = self.__class__.__mul__(self, other)
    if isinstance(result, Ideal_generic):
        return _refine_ideal_as_module(result)
    return result


def install() -> None:
    """Install ideal-submodule and quotient-module refinement patches.

    Idempotent: safe to call multiple times.
    """
    global _installed, _native_ring_truediv
    if _installed:
        return

    # Patch Ring.ideal to refine outputs
    Rings().parent_class.ideal = _module_aware_ideal

    _installed = True
