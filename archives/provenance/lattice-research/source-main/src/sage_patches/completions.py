"""Completion and localization install hook for ModuleBaseRings.

ModuleBaseRings.ParentMethods owns the stable completion/localization aliases.
This module only ensures that the category is installed before callers use those
methods.

Gate: only active on rings installed with ModuleBaseRings.
"""

from __future__ import annotations

_installed = False


def install() -> None:
    """Install ModuleBaseRings completion/localization refinement.

    Idempotent: safe to call multiple times.
    """
    global _installed
    if _installed:
        return

    from src.sage_patches import ring_base_category

    ring_base_category._install_module_base_rings()

    _installed = True
