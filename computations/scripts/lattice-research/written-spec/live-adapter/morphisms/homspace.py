"""Hom-space wrappers and End/Aut constructors for formed modules."""

from typing import Any

from sage.categories.modules import Modules


def formed_hom(domain: Any, codomain: Any) -> Any:
    """Return the Hom-set for formed modules."""
    return domain._Hom_(codomain, category=Modules(domain.base_ring()))


def formed_end(module: Any) -> Any:
    """Return End(M) = Hom(M,M) for a formed module."""
    return formed_hom(module, module)
