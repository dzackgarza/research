r"""Base change and restriction of scalars along a ring morphism.

For \(f:R\to S\) there are two functors between module categories:

- **base change** \(F=-\otimes_RS:\mathbf{Mod}(R)\to\mathbf{Mod}(S)\);
- **restriction of scalars** \(G:\mathbf{Mod}(S)\to\mathbf{Mod}(R)\), reading
  an \(S\)-module over \(R\) through \(f\).

\(F\dashv G\).  Neither is an endofunctor, and neither is invertible.

Getting the adjunction's direction right is what makes the unit statable.
\(F(M)=M\otimes_RS\) is an \(S\)-module, so \(M\to F(M)\) is not a morphism in
either category: its source lives in \(\mathbf{Mod}(R)\) and its target in
\(\mathbf{Mod}(S)\).  The unit is
\(\eta_M:M\to G(F(M))\), whose codomain is \(M\otimes_RS\) *restricted back to
\(R\)* -- that restriction is exactly what makes source and target comparable.
The counit is \(\varepsilon_N:F(G(N))\to N\) in \(\mathbf{Mod}(S)\).

Restriction is not an inverse: \(G(F(L))\) for a lattice \(L\) is
\(L\otimes\mathbb Q\) read additively over \(\mathbb Z\), not \(L\).  Getting
a lattice back requires choosing one inside its rational span, which is what
saturation does.
"""

from sage.categories.functor import Functor
from sage.structure.sage_object import SageObject


class BaseChangeFunctor(Functor):
    r"""\(-\otimes_RS:\mathbf{Mod}(R)\to\mathbf{Mod}(S)\) along \(f:R\to S\)."""

    def __init__(self, ring_map: "Morphism") -> None:
        self._ring_map = ring_map
        Functor.__init__(
            self, Modules(ring_map.domain()), Modules(ring_map.codomain())
        )

    def ring_map(self) -> "Morphism":
        return self._ring_map

    def _apply_functor(self, module: "Module") -> "Module":
        r"""Return \(M\otimes_RS\).

        A free module base-changes to the free module on the same framing
        set: the generators do not move, only the ring they are combined
        over does.
        """
        return BasedFreeModule(
            self._ring_map.codomain(), module.module_generating_set()
        )

    def _apply_functor_to_morphism(self, morphism: "ModuleMorphism") -> "ModuleMorphism":
        r"""Return \(f\otimes S\), the same matrix read over \(S\)."""
        source, target = self(morphism.domain()), self(morphism.codomain())
        return module_homset(source, target)(
            {
                label: zipsum(
                    row, target.module_generators(), target.zero()
                )
                for label, row in zip(
                    source.module_generating_set(),
                    morphism.matrix().change_ring(self._ring_map.codomain()).rows(),
                )
            }
        )

    def _repr_(self) -> str:
        return f"Base change along {self._ring_map}"


class RestrictionOfScalarsFunctor(Functor):
    r"""\(\mathbf{Mod}(S)\to\mathbf{Mod}(R)\) along \(f:R\to S\)."""

    def __init__(self, ring_map: "Morphism") -> None:
        self._ring_map = ring_map
        Functor.__init__(
            self, Modules(ring_map.codomain()), Modules(ring_map.domain())
        )

    def ring_map(self) -> "Morphism":
        return self._ring_map

    def _apply_functor(self, module: "Module") -> "Module":
        return BasedFreeModule(
            self._ring_map.domain(), module.module_generating_set()
        )

    def _repr_(self) -> str:
        return f"Restriction of scalars along {self._ring_map}"


class BaseChangeAdjunction(Adjunction):
    r"""\(-\otimes_RS\dashv\) restriction of scalars."""

    def __init__(self, ring_map: "Morphism") -> None:
        self._ring_map = ring_map
        Adjunction.__init__(
            self,
            BaseChangeFunctor(ring_map),
            RestrictionOfScalarsFunctor(ring_map),
        )

    def unit(self, module: "Module") -> "ModuleMorphism":
        r"""Return \(\eta_M:M\to G(F(M))\), \(m\mapsto m\otimes 1\).

        The codomain is \(M\otimes_RS\) *restricted to \(R\)*.  Without that
        restriction there is no morphism to speak of: \(M\) is an \(R\)-module
        and \(M\otimes_RS\) is an \(S\)-module, and a map between them belongs
        to no single category.
        """
        restricted = self._right_adjoint(self._left_adjoint(module))
        return module_homset(module, restricted)(
            {
                label: restricted.module_generator(label)
                for label in module.module_generating_set()
            }
        )

    def counit(self, module: "Module") -> "ModuleMorphism":
        r"""Return \(\varepsilon_N:F(G(N))\to N\) in \(\mathbf{Mod}(S)\)."""
        extended = self._left_adjoint(self._right_adjoint(module))
        return module_homset(extended, module)(
            {
                label: module.module_generator(label)
                for label in module.module_generating_set()
            }
        )

    def _repr_(self) -> str:
        return f"Base change adjunction along {self._ring_map}"
