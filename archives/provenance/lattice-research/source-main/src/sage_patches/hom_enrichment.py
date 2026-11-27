"""Hom-space enrichment for enriched modules.

Adds End() and Aut() constructors to Modules(R) category parent methods,
routing through Sage's existing homset infrastructure. Native Sage homset
and morphism methods (from_matrix, kernel, cokernel, etc.) are preserved.
"""

from __future__ import annotations

from typing import Any

from sage.all import Modules
from sage.categories.modules import Modules as ModulesCategory

_installed = False


def install() -> None:
    """Install End/Aut constructors on Modules category.

    Idempotent: safe to call multiple times.
    """
    global _installed
    if _installed:
        return

    if not hasattr(ModulesCategory.ParentMethods, "End"):

        def _end(self: Any) -> Any:
            return self._Hom_(self, category=Modules(self.base_ring()))

        ModulesCategory.ParentMethods.End = _end

    if not hasattr(ModulesCategory.ParentMethods, "Aut"):

        def _aut(self: Any) -> Any:
            return self.End()

        ModulesCategory.ParentMethods.Aut = _aut

    _installed = True
