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

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category
from sage.rings.integer import Integer as SageInteger

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        DiscriminantGroup,
        Integer,
        Matrix,
        RingElement,
        RMod,
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
    def extra_super_categories(self) -> list[Category]:
        return [
            self.base_category().FinitelyPresented(),
            self.base_category().OverPID(),
        ]

    @classmethod
    @final
    def from_matrix(cls, module_category: RMod, matrix: Matrix) -> RModule:
        r"""Return the finitely presented module ``coker(matrix)`` over a PID."""
        return module_category.from_invariant_factors(matrix.elementary_divisors())

    # ------------------------------------------------------------------
    # ParentMethods
    # ------------------------------------------------------------------

    class ParentMethods:
        @abstractmethod
        def order(self) -> RingElement:
            r"""Generator of ``Ann_R(M)``."""
            ...

        @abstractmethod
        def invariant_factors(self) -> Sequence[RingElement]:
            r"""Return ``[0, ..., 0, r_1, ..., r_n]`` with the leading zeros
            encoding the free summands ``R^n``.
            """
            ...

        @abstractmethod
        def invariants(self, include_ones: bool = False) -> tuple[RingElement, ...]:
            r"""Return the nonzero invariant factors, optionally including unit
            factors.
            """
            ...

        @abstractmethod
        def smith_form_gens(self) -> tuple[RModuleElement, ...]:
            r"""Return generators compatible with the Smith decomposition."""
            ...

        @abstractmethod
        def free_part(self) -> RModule:
            r"""Free summand ``R^k`` of ``M = R^k \oplus T``."""
            ...

        @abstractmethod
        def torsion_part(self) -> RModule:
            r"""Torsion summand ``T`` of ``M = R^k \oplus T``."""
            ...

        @final
        def free_rank(self) -> Integer:
            return SageInteger(sum(r.is_zero() for r in self.invariant_factors()))

        @abstractmethod
        def element_from_vector(self, vec: Sequence[RingElement]) -> RModuleElement:
            ...

        @abstractmethod
        def V(self) -> RModule: ...

        @abstractmethod
        def W(self) -> RModule: ...

        @abstractmethod
        def optimized(self) -> RModule: ...

        @abstractmethod
        def hom(self, images: Sequence[RModuleElement] | Matrix) -> RModMorphism:
            ...

        @abstractmethod
        def cardinality(self) -> Cardinality:
            """Return the cardinality of this finitely presented module when finite."""
            ...

        @abstractmethod
        def is_finite(self) -> bool:
            """Return whether this finitely presented module is finite."""
            ...

        @abstractmethod
        def annihilator(self) -> RingElement:
            """Return the annihilator ideal generator for this finitely presented PID module."""
            ...

        @abstractmethod
        def elementary_divisors(self) -> tuple[RingElement, ...]:
            """Return elementary divisors for the PID presentation."""
            ...

        @abstractmethod
        def ngens(self) -> int:
            """Return the number of distinguished generators in the presentation."""
            ...

        @abstractmethod
        def smith_form_gen(self, i: int) -> RModuleElement:
            """Return the ``i``-th Smith-form generator."""
            ...

        @abstractmethod
        def linear_combination_of_smith_form_gens(
            self, v: Sequence[RingElement]
        ) -> RModuleElement:
            """Return the element represented by Smith-basis coordinates ``v``."""
            ...

        @abstractmethod
        def gens_to_smith(self) -> Matrix:
            """Return the change-of-generators matrix from distinguished generators to Smith generators."""
            ...

        @abstractmethod
        def smith_to_gens(self) -> Matrix:
            """Return the change-of-generators matrix from Smith generators to distinguished generators."""
            ...

        @abstractmethod
        def gens_vector(self, x: RModuleElement, *, reduce: bool = True) -> object:
            """Return coordinates of ``x`` in the distinguished generators."""
            ...

        @abstractmethod
        def coordinate_vector(self, x: RModuleElement) -> object:
            """Return the canonical presentation coordinates of ``x``."""
            ...

        @final
        def cover(self) -> RModule:
            """Return the covering module V in the finite presentation V/W."""
            return self.V()

        @final
        def relations(self) -> RModule:
            """Return the relation submodule W in the finite presentation V/W."""
            return self.W()

    # ------------------------------------------------------------------
    # ElementMethods
    # ------------------------------------------------------------------

    class ElementMethods:
        @abstractmethod
        def to_vector(self) -> Sequence[RingElement]: ...

        @abstractmethod
        def order(self) -> RingElement:
            r"""Generator of ``Ann_R(m) = Ann_R(<m>)``."""
            ...

        @final
        def coordinate_vector(self) -> object:
            """Return this element's coordinates in its finitely presented parent."""
            return self.to_vector()

    # ------------------------------------------------------------------
    # Hom category
    # ------------------------------------------------------------------

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstractmethod
            def from_dict(
                self, mapping: dict[RModuleElement, RModuleElement]
            ) -> RModMorphism:
                ...

            @abstractmethod
            def from_matrix(self, M: Matrix) -> RModMorphism: ...

            @abstractmethod
            def from_images(self, images: Sequence[RModuleElement]) -> RModMorphism:
                ...

        class ElementMethods:
            @abstractmethod
            def generator_images(self) -> tuple[RModuleElement, ...]:
                r"""Return the images of the domain's presentation generators."""
                ...

            @final
            def im_gens(self) -> tuple[RModuleElement, ...]:
                r"""Sage-compatible spelling for presentation-generator images."""
                return self.generator_images()

            @abstractmethod
            def to_dict(self) -> dict[RModuleElement, RModuleElement]: ...

            @abstractmethod
            def to_matrix(self) -> Matrix: ...

            @abstractmethod
            def to_list(self) -> list[RModuleElement]: ...

            @abstractmethod
            def to_tuple(self) -> tuple[RModuleElement, ...]: ...

            @abstractmethod
            def to_function(self) -> Callable[[RModuleElement], RModuleElement]: ...

            @abstractmethod
            def kernel(self) -> RModule:
                """Return the kernel as a finitely presented module or submodule."""
                ...

            @abstractmethod
            def image(self) -> RModule:
                """Return the image as a finitely presented module or submodule."""
                ...

            @abstractmethod
            def lift(self, y: RModuleElement) -> RModuleElement:
                """Lift a codomain element through this homomorphism when possible."""
                ...

    # ------------------------------------------------------------------
    # Torsion subcategory
    # ------------------------------------------------------------------

    class Torsion(CategoryWithAxiom_over_base_ring):
        r"""Finitely presented torsion modules over a PID."""

        class ParentMethods:
            @abstractmethod
            def p_part(self, p: RingElement) -> RModule:
                r"""Factor ``(R/p)^n`` of ``T`` in the decomposition
                ``M = F + T``.
                """
                ...

            @final
            def is_p_elementary(self, p: RingElement) -> bool:
                r"""``M`` is p-elementary iff ``M == M.p_part(p)``."""
                return bool(self == self.p_part(p))

        class ElementMethods: ...


    # ------------------------------------------------------------------
    # Lattices subcategory
    # ------------------------------------------------------------------

    class Lattices(CategoryWithAxiom_over_base_ring):
        r"""Finitely presented torsion-free modules over a PID equipped
        with a symmetric, nondegenerate, integral bilinear form.
        """

        class ParentMethods:
            @abstractmethod
            def determinant(self) -> RingElement: ...

            @abstractmethod
            def discriminant_group(self) -> DiscriminantGroup: ...

        class ElementMethods: ...
