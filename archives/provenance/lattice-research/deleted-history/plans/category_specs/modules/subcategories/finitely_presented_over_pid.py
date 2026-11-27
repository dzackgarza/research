r"""Spec for finitely presented modules over a PID.

This category owns most module constructions in ``Modules(R)`` and the
general spec should delegate concrete representations here.

Every object is represented by an ordered list of ring elements (which may
include zero), encoding a preferred decomposition of M:

    list = [0_1, ..., 0_n, r_1, ..., r_m]
        ==> M := R \oplus ... \oplus R \oplus R/r_1 \oplus ... \oplus R/r_m
                 (n free summands)             (m torsion summands)

This representation is *not* equal to the SNF of M -- it is isomorphic to
it.  Concretely, to compute ``coker(f: M -> N)``:

    1. Compute the Smith normal form ``D = SNF(A_f)`` together with
       ``U * A_f * V = D``.
    2. Define Q to be the module abstractly determined by D, with
       generators ``q_i``.
    3. The morphism ``\pi: N -> Q`` sending the generators ``n_i`` of N to
       ``q_i`` is then represented by ``U`` with each row interpreted mod
       the corresponding ``d_i``.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, final, override

from sage.matrix.matrix2 import Matrix as SageMatrix
from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction

if TYPE_CHECKING:
    from ...types import (
        DiscriminantGroup,
        Integer,
        Matrix,
        RingElement,
        RModMorphism,
        RModule,
        RModuleElement,
    )


class FinitelyPresentedModulesOverPID(CategoryWithAxiom_over_base_ring):
    r"""Finitely presented modules over a (commutative) PID.

    Canonical chain: ``Modules(R).FinitelyPresented().OverPID()``.

    Constructor target: matrix presentations and Sage ``FGP_Module`` quotient
    constructors refine here.

    Refines ``Modules(R).FinitelyPresented()`` for ``R`` a PID, where every
    finitely presented module decomposes as a direct sum of cyclic modules.
    """

    @override
    @final
    def extra_super_categories(self):
        return [
            self.base_category().FinitelyPresented(),
            self.base_category().OverPID(),
        ]

    @classmethod
    @final
    def from_matrix(cls, module_category, matrix: Matrix) -> RModule:
        r"""Return the finitely presented module ``coker(matrix)`` over a PID."""
        assert isinstance(matrix, SageMatrix), f"Matrix presentation must be a Sage matrix: {matrix}"
        return module_category.from_invariant_factors(matrix.elementary_divisors())

    # ------------------------------------------------------------------
    # ParentMethods
    # ------------------------------------------------------------------

    class ParentMethods:
        @abstract_method
        def order(self) -> RingElement:
            r"""Generator of ``Ann_R(M)``."""
            ...

        @abstract_method
        def invariant_factors(self) -> Sequence[RingElement]:
            r"""Return ``[0, ..., 0, r_1, ..., r_n]`` with the leading zeros
            encoding the free summands ``R^n``.
            """
            ...

        @abstract_method
        def invariants(self, include_ones: bool = False) -> tuple[RingElement, ...]:
            r"""Return the nonzero invariant factors, optionally including unit factors."""
            ...

        @abstract_method
        def smith_form_gens(self) -> tuple[RModuleElement, ...]:
            r"""Return generators compatible with the Smith decomposition."""
            ...

        @abstract_method
        def free_part(self) -> RModule:
            r"""Free summand ``R^k`` of ``M = R^k \oplus T``."""
            ...

        @abstract_method
        def torsion_part(self) -> RModule:
            r"""Torsion summand ``T`` of ``M = R^k \oplus T``."""
            ...

        @final
        def free_rank(self) -> Integer:
            return sum(1 for r in self.invariant_factors() if r.is_zero())

        @abstract_method
        def element_from_vector(self, vec: Sequence[RingElement]) -> RModuleElement: ...

        @abstract_method
        def V(self) -> RModule: ...

        @abstract_method
        def W(self) -> RModule: ...

        @abstract_method
        def optimized(self) -> RModule: ...

        @abstract_method
        def hom(self, images: Sequence[RModuleElement] | Matrix) -> RModMorphism: ...

    # ------------------------------------------------------------------
    # ElementMethods
    # ------------------------------------------------------------------

    class ElementMethods:
        @abstract_method
        def to_vector(self) -> Sequence[RingElement]: ...

        @abstract_method
        def order(self) -> RingElement:
            r"""Generator of ``Ann_R(m) = Ann_R(<m>)``."""
            ...

    class MorphismMethods: ...

    # ------------------------------------------------------------------
    # Hom category
    # ------------------------------------------------------------------

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstract_method
            def from_dict(self, mapping: dict[RModuleElement, RModuleElement]) -> RModMorphism: ...

            @abstract_method
            def from_matrix(self, M: Matrix) -> RModMorphism: ...

            @abstract_method
            def from_images(self, images: Sequence[RModuleElement]) -> RModMorphism: ...

        class ElementMethods:
            @abstract_method
            def to_dict(self) -> dict[RModuleElement, RModuleElement]: ...

            @abstract_method
            def to_matrix(self) -> Matrix: ...

            @abstract_method
            def to_list(self) -> list[RModuleElement]: ...

            @abstract_method
            def to_tuple(self) -> tuple[RModuleElement, ...]: ...

            @abstract_method
            def to_function(self) -> Callable[[RModuleElement], RModuleElement]: ...

        class MorphismMethods: ...

    # ------------------------------------------------------------------
    # Torsion subcategory
    # ------------------------------------------------------------------

    class Torsion(CategoryWithAxiom_over_base_ring):
        r"""Finitely presented torsion modules over a PID."""

        class ParentMethods:
            @abstract_method
            def p_part(self, p: RingElement) -> RModule:
                r"""Factor ``(R/p)^n`` of ``T`` in the decomposition
                ``M = F + T``.
                """
                ...

            @final
            def is_p_elementary(self, p: RingElement) -> bool:
                r"""``M`` is p-elementary iff ``M == M.p_part(p)``."""
                return self == self.p_part(p)

        class ElementMethods: ...
        class MorphismMethods: ...

    # ------------------------------------------------------------------
    # Lattices subcategory
    # ------------------------------------------------------------------

    class Lattices(CategoryWithAxiom_over_base_ring):
        r"""Finitely presented torsion-free modules over a PID equipped
        with a symmetric, nondegenerate, integral bilinear form.
        """

        class ParentMethods:
            @abstract_method
            def determinant(self) -> RingElement: ...

            @abstract_method
            def discriminant_group(self) -> DiscriminantGroup: ...

        class ElementMethods: ...
        class MorphismMethods: ...
