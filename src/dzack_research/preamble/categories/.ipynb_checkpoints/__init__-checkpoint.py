r"""Categories defined to organize the preamble's method-installation surface.

Each category owns ``ParentMethods`` and/or ``ElementMethods``.  Objects are
routed into these categories via ``custom_refine_category``, which corrects
Sage's MRO so that category methods override native class methods.

Sage's ``_refine_category_`` only updates ``obj._category`` — it does not
change the class MRO.  Since Python resolves methods through the MRO first,
native class methods always shadow category methods.  ``custom_refine_category``
fixes this for **parents** by creating a new dynamic class with
``ParentMethods`` BEFORE the native class and assigning it via ``__class__``.

EXAMPLES::

    sage: from dzack_research.preamble.categories import IntegralLattices
    sage: IntegralLattices()._repr_object_names()
    'integral lattices'
"""

from __future__ import annotations

from typing import Any

from .integral_lattices import IntegralLattices
from .discriminant_groups import DiscriminantQuadraticModules
from .hyperbolic_lattices import HyperbolicLattices

__all__ = [
    "IntegralLattices",
    "DiscriminantQuadraticModules",
    "HyperbolicLattices",
    "custom_refine_category",
]


def custom_refine_category(obj: Any, cat: Any) -> None:
    r"""Refine an object into the given category with MRO correction.

    Sage's ``_refine_category_`` updates ``obj._category`` but does **not**
    change the object's class MRO.  This function additionally forces the
    category's ``ParentMethods`` to take priority over native class methods
    by creating a new dynamic class with the mixin before the native class
    and assigning it via ``__class__``.

    EXAMPLES::

        sage: from dzack_research.preamble.categories import (
        ....:     custom_refine_category, IntegralLattices)
        sage: L = IntegralLattice(matrix(ZZ, [[0,1],[1,0]]))
        sage: custom_refine_category(L, IntegralLattices())
        sage: type(L).direct_sum.__qualname__.startswith('IntegralLattices')
        True
    """
    from sage.structure.parent import Parent

    obj._refine_category_(cat)

    if isinstance(obj, Parent) and hasattr(cat, "ParentMethods"):
        _fix_parent_mro(obj, cat.ParentMethods)


def _fix_parent_mro(parent: Any, pm_cls: Any) -> None:
    """Put ParentMethods before the native class via __class__ assignment."""
    import warnings as _w

    current = type(parent)
    if pm_cls in current.__mro__:
        return
    new_cls = type(current.__name__, (pm_cls, current), {})
    try:
        parent.__class__ = new_cls
    except TypeError as _e:
        _w.warn(
            f"__class__ assignment failed for {type(parent).__name__} "
            f"with {pm_cls.__name__}: {_e}",
            RuntimeWarning,
            stacklevel=2,
        )
