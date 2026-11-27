r"""Alternating bilinear modules: ``Modules(R).WithForms().Bilinear().Alternating()``.

An alternating bilinear form satisfies ``b(v, v) = 0`` for all ``v``,
which implies ``b(v, w) = -b(w, v)`` (skew-symmetry) when ``2`` is invertible.
"""

from __future__ import annotations

from typing import final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import BilinearModulesCategory


class AlternatingBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with an alternating bilinear form.

    Canonical chain: ``Modules(R).WithForms().Bilinear().Alternating()``.

    An ``R``-bilinear form ``b`` is *alternating* iff ``b(v, v) = 0`` for
    all ``v \in M``.  Equivalently, ``b(v, w) = -b(w, v)`` whenever ``2``
    is invertible in ``R``.  The Gram matrix has zero diagonal.

    .. NOTE::

        Alternating forms are orthogonal to the ``Symmetric`` axiom: a form
        that is both symmetric and alternating has ``b(v, w) = 0`` for all
        ``v, w`` (assuming ``\mathrm{char}(R) \neq 2``).
    """

    _base_category_class_and_axiom = (BilinearModulesCategory, "Alternating")
    _defining_predicates = ("is_alternating",)

    class ParentMethods:
        @override
        @final
        def is_alternating(self) -> bool:
            return True

        @final
        def is_isotropic(self) -> bool:
            r"""Introduced here: every element satisfies ``b(v, v) = 0``."""
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


AlternatingBilinearModulesObject = AlternatingBilinearModulesCategory.ParentMethods
AlternatingBilinearModulesElement = AlternatingBilinearModulesCategory.ElementMethods
AlternatingBilinearModulesMorphism = AlternatingBilinearModulesCategory.MorphismMethods
