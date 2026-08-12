r"""Base change of algebras along a ring morphism.

For \(f:R\to S\) the module-level \(-\otimes_RS\) lifts to algebras: the
product of two elements is written in the generators, and transporting the
coefficients along \(f\) respects it, so \(A\otimes_RS\) is an \(S\)-algebra
and the assignment is functorial.

This is the functor a number field is a value of.  \(K\) over
\(\operatorname{Frac}(R)\) and the \(R\)-algebra \(A\) underlying it are
related by \(F(A)=K\) for \(F=-\otimes_R\operatorname{Frac}(R)\), and stating
that needs \(F\) as an object -- calling a ``base_change`` method states
nothing, because a method call is not an arrow and cannot be composed,
compared, or asked for its domain.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.structure.parent import Parent

    # The algebra noun, taken the way the lexicon takes ``Ring``: the
    # category's own ``ParentMethods``.
    from dzack_research.preamble.categories.algebras.algebras import Algebras

from sage.categories.functor import Functor


class AlgebraBaseChangeFunctor(Functor):
    r"""\(-\otimes_RS:\mathbf{Alg}(R)\to\mathbf{Alg}(S)\) along \(f:R\to S\)."""

    def __init__(self, ring_map: "Morphism") -> None:
        # Local: the algebra node reaches this module through number fields, so
        # a module-level import would close that cycle.
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        self._ring_map = ring_map
        Functor.__init__(
            self,
            Algebras(ring_map.domain()),
            Algebras(ring_map.codomain()),
        )

    def ring_map(self) -> "Morphism":
        r"""Return \(f\), the morphism the coefficients travel along."""
        return self._ring_map

    def _apply_functor(self, algebra: "Algebras.ParentMethods") -> "Parent":
        r"""Return \(A\otimes_RS\).

        The presentation does not move: the same generators, the same
        relations with their coefficients carried along \(f\).  That is what
        makes the value of this functor a *presented* algebra rather than a
        tensor product one still has to identify.
        """
        # Local: importing the ring node here would close a cycle, and the
        # module is built by the time this method runs.
        from dzack_research.preamble.categories.rings.rings import engine_ring

        # Both sides cross to the engine: a session names owned rings, so the
        # map it obtained starts at one, and only the engine's name for a ring
        # is common to both spellings.
        assert engine_ring(algebra.base_ring()) is engine_ring(self._ring_map.domain()), (
            f"{algebra} is an algebra over {algebra.base_ring()}, and this "
            f"functor starts from {self._ring_map.domain()}"
        )
        base_changed: "Parent" = algebra.base_change(self._ring_map)
        return base_changed

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        r"""Return \(g\otimes S\), the same generator images over \(S\).

        An algebra map out of a presented algebra is fixed by where the
        generators go, so its base change is fixed by the images of those --
        transported along \(f\), which is the only thing this functor does.
        """
        source = self(morphism.domain())
        target = self(morphism.codomain())
        base_changed: "Morphism" = source.hom(
            {
                label: target._base_change_relation(
                    morphism(morphism.domain().algebra_generator(label)),
                    self._ring_map,
                    target,
                )
                for label in source.algebra_generating_set()
            },
            target,
        )
        return base_changed

    def _repr_(self) -> str:
        return f"Base change of algebras along {self._ring_map}"


def algebra_base_change(ring_map: "Morphism") -> AlgebraBaseChangeFunctor:
    r"""Return \(-\otimes_RS\) for the ring morphism ``ring_map``."""
    return AlgebraBaseChangeFunctor(ring_map)
