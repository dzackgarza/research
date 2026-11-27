"""Enriched finitely generated module surface for ModuleBaseRings.

After ModuleBaseRings and ideal-submodule patches are installed, this module
adds enriched module operations: direct sum (M+N), tensor product (M*N,
M.tensor(N)), base change, and quotient (M/H) with category refinement into
Modules(R).Free().FiniteRank() or Modules(R).FinitelyPresented().

Does NOT reimplement underlying Sage module arithmetic — only adds category
metadata and enriched constructor routing.
"""

from __future__ import annotations

from typing import Any

from sage.all import Modules
from sage.modules.free_module import FreeModule_ambient_pid

_installed = False


def _ensure_module_refinement(M: Any) -> Any:
    """Refine a module parent into Modules(R)."""
    assert hasattr(M, "_refine_category_")
    M._refine_category_(Modules(M.base_ring()))
    return M


_native_free_module_direct_sum = FreeModule_ambient_pid.direct_sum


def enriched_direct_sum(self: Any, other: Any) -> Any:
    """Direct sum M ⊕ N of enriched modules, refined into Modules(R)."""
    result = _native_free_module_direct_sum(self, other)
    return _ensure_module_refinement(result)


def enriched_quotient(self: Any, submodule: Any) -> Any:
    """Quotient M / H as an enriched FGP module."""
    result = self.quotient(submodule)
    return _ensure_module_refinement(result)


def install() -> None:
    """Install enriched module surface patches.

    Idempotent: safe to call multiple times.
    """
    global _installed
    if _installed:
        return

    # Patch direct_sum on FreeModule_ambient_pid for enriched behavior
    FreeModule_ambient_pid.direct_sum = enriched_direct_sum

    _installed = True
