r"""Symmetric bilinear modules: ``Modules(R).WithForms().Bilinear().Symmetric()``.

A symmetric bilinear form satisfies ``b(v, w) = b(w, v)`` for all ``v``, ``w``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import BilinearModulesCategory

if TYPE_CHECKING:
    from ...types import SubModule


class SymmetricBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a symmetric bilinear form ``b: M \times M \to S``.

    Canonical chain: ``Modules(R).WithForms().Bilinear().Symmetric()``.

    An ``R``-bilinear form ``b`` is *symmetric* iff ``b(v, w) = b(w, v)``
    for all ``v, w \in M``.  The Gram matrix ``G`` is symmetric: ``G = G^T``.

    Symmetric forms support:
    - ``orthogonal_submodule_to(S)`` — ``S^\perp``
    - ``v.perp()`` — element-level orthogonal complement

    Neither requires nondegeneracy.
    """

    _base_category_class_and_axiom = (BilinearModulesCategory, "Symmetric")
    _defining_predicates = ("is_symmetric",)

    class ParentMethods:
        @override
        @final
        def is_symmetric(self) -> bool:
            return True

        @abstract_method
        def is_definite(self) -> bool:
            r"""Introduced here: decide whether the symmetric form has one sign."""
            ...

        @abstract_method
        def is_indefinite(self) -> bool:
            r"""Introduced here: decide whether the symmetric form has both signs."""
            ...

        @abstract_method
        def is_positive_definite(self) -> bool:
            r"""Introduced here: decide whether all nonzero self-products are positive."""
            ...

        @abstract_method
        def is_negative_definite(self) -> bool:
            r"""Introduced here: decide whether all nonzero self-products are negative."""
            ...

        @abstract_method
        def orthogonal_submodule_to(self, S: SubModule) -> SubModule:
            r"""Return ``S^\perp = \{v \in M : b(v, s) = 0 \,\forall s \in S\}``.

            Always a submodule of ``self``.  ``S^\perp = S`` iff ``S`` is
            totally isotropic.  Does **not** require nondegeneracy.
            """
            ...

    class ElementMethods:
        @abstract_method
        def perp(self) -> SubModule:
            r"""Return the orthogonal complement ``v^\perp`` of this element.

            ``v^\perp = \{w \in M : b(v, w) = 0\}``, a submodule of the
            parent.  Does **not** require nondegeneracy.

            EXAMPLES::

                sage: U = Lattice.U()          # not tested
                sage: e = U.gen(0)             # not tested
                sage: e.perp()                 # not tested
                Rank-1 sublattice ...
            """
            ...

    class MorphismMethods: ...


SymmetricBilinearModulesObject = SymmetricBilinearModulesCategory.ParentMethods
SymmetricBilinearModulesElement = SymmetricBilinearModulesCategory.ElementMethods
SymmetricBilinearModulesMorphism = SymmetricBilinearModulesCategory.MorphismMethods
