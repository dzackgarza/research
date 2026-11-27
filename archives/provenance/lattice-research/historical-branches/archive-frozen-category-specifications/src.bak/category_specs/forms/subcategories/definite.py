r"""Definite bilinear modules: ``Modules(R).WithForms().Bilinear().Definite()``.

A symmetric bilinear form is *definite* iff it is either positive-definite
(``b(v, v) > 0`` for all nonzero ``v``) or negative-definite
(``b(v, v) < 0`` for all nonzero ``v``).  Signature ``(p, q)`` satisfies
``q = 0`` (positive-definite) or ``p = 0`` (negative-definite).
"""

from __future__ import annotations

from abc import abstractmethod
from typing import final, override, TypeAlias

from ...cat import CategoryWithAxiom_over_base_ring
from .symmetric import (
    SymmetricBilinearModulesCategory,
    SymmetricBilinearModulesMorphism,
)


class DefiniteBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a definite (positive or negative definite)

    Canonical chain: ``Modules(R).WithForms().Bilinear().Symmetric().Definite()``.
    symmetric bilinear form.

    A symmetric bilinear form ``b`` is *definite* iff every nonzero vector
    satisfies ``b(v, v) \ne 0`` with a consistent sign.  For a positive-definite
    form ``b(v, v) > 0``; for negative-definite ``b(v, v) < 0``.

    Definite forms are automatically nondegenerate: if ``b(v, v) > 0`` for
    all nonzero ``v``, then ``v \ne 0 \Rightarrow b(v, -) \ne 0``.

    EXAMPLES::

        sage: A2 = Lattice.A(2)   # not tested; root lattice, negative definite
        sage: C = Modules(ZZ).WithForms().Bilinear().Symmetric().Definite()
        sage: A2 in C   # not tested
        True
    """

    _base_category_class_and_axiom = (SymmetricBilinearModulesCategory, "Definite")
    _defining_predicates = ("is_definite",)

    class ParentMethods:
        @override
        @final
        def is_definite(self) -> bool:
            return True

        @override
        @final
        def is_indefinite(self) -> bool:
            return False

        @override
        @final
        def is_nondegenerate(self) -> bool:
            r"""Definite implies nondegenerate."""
            return True

        @abstractmethod
        def is_positive_definite(self) -> bool:
            r"""Return ``True`` iff ``b(v, v) > 0`` for all nonzero ``v``."""
            ...

        @abstractmethod
        def is_negative_definite(self) -> bool:
            r"""Return ``True`` iff ``b(v, v) < 0`` for all nonzero ``v``."""
            ...

    class ElementMethods:
        @override
        @final
        def is_anisotropic(self) -> bool:
            r"""Every nonzero element of a definite module is anisotropic."""
            return not self.is_zero()



DefiniteBilinearModulesObject : TypeAlias = DefiniteBilinearModulesCategory.ParentMethods
DefiniteBilinearModulesElement : TypeAlias = DefiniteBilinearModulesCategory.ElementMethods
DefiniteBilinearModulesMorphism : TypeAlias = SymmetricBilinearModulesMorphism
