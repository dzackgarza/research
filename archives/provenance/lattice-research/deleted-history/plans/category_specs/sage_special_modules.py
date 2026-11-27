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

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.homsets import HomsetsCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    Cardinality = Any
    Ideal = Any
    Matrix = Any
    RingElement = Any
    RModule = Any
    RModuleElement = Any
    RModuleMorphism = Any
    SubModule = Any

    Lattice = Any
    DiscriminantGroup = Any
    OrthogonalGroup = Any


class FinitelyPresentedModulesOverPID(CategoryWithAxiom_over_base_ring):
    r"""Finitely presented modules over a (commutative) PID.

    Refines ``Modules(R).FinitelyPresented()`` for ``R`` a PID, where every
    finitely presented module decomposes as a direct sum of cyclic modules.
    """

    def extra_super_categories(self):
        return [
            self.base_category().FinitelyPresented(),
            self.base_category().OverPID(),
        ]

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
        def free_part(self) -> RModule:
            r"""Free summand ``R^k`` of ``M = R^k \oplus T``."""
            ...

        @abstract_method
        def torsion_part(self) -> RModule:
            r"""Torsion summand ``T`` of ``M = R^k \oplus T``."""
            ...

        def free_rank(self) -> int:
            return sum(1 for r in self.invariant_factors() if r.is_zero())

        @abstract_method
        def element_from_vector(
            self, vec: Sequence[RingElement]
        ) -> RModuleElement: ...

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

    # ------------------------------------------------------------------
    # Homsets
    # ------------------------------------------------------------------

    class Homsets(HomsetsCategory):
        class ParentMethods:
            @abstract_method
            def from_dict(
                self, mapping: dict
            ) -> RModuleMorphism: ...

            @abstract_method
            def from_matrix(self, M: Matrix) -> RModuleMorphism: ...

            @abstract_method
            def from_images(
                self, images: Sequence[RModuleElement]
            ) -> RModuleMorphism: ...

        class ElementMethods:
            @abstract_method
            def to_dict(self) -> dict: ...

            @abstract_method
            def to_matrix(self) -> Matrix: ...

            @abstract_method
            def to_list(self) -> list: ...

            @abstract_method
            def to_tuple(self) -> tuple: ...

            @abstract_method
            def to_function(self): ...

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

            def is_p_elementary(self, p: RingElement) -> bool:
                r"""``M`` is p-elementary iff ``M == M.p_part(p)``."""
                return self == self.p_part(p)

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

            @abstract_method
            def orthogonal_group(self) -> OrthogonalGroup:
                r"""``O(L)``."""
                ...

            @abstract_method
            def special_orthogonal_group(self) -> OrthogonalGroup:
                r"""``SO(L)``."""
                ...

            @abstract_method
            def stable_orthogonal_group(self) -> OrthogonalGroup:
                r"""``O^+(L)``."""
                ...

            @abstract_method
            def stable_special_orthogonal_group(self) -> OrthogonalGroup:
                r"""``SO^+(L)``."""
                ...
