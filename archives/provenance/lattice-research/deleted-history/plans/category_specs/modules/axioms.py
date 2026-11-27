r"""Axiomatic subcategory mixin classes for ``Modules(R)``.

Every class here is a ``CategoryWithAxiom_over_base_ring`` wired into
``Modules`` in ``__init__.py`` via the axiom-registration loop.

Naming follows the project convention: ``Modules(R)`` is our category,
``SageModules(R)`` is Sage's; ``CommutativeRings()`` is our
``Rings().Commutative()``, ``SageCommutativeRings`` is Sage's, etc.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.homsets import HomsetsCategory
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    from typing import Protocol

    from sage.categories.morphism import Morphism
    from sage.rings.ideal import Ideal_generic
    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer
    from sage.structure.element import Element
    from sage.structure.parent import Parent

    Cardinality = Integer | InfinityElement
    RingElement = Element
    RModule = Parent
    RModuleElement = Element
    RModuleMorphism = Morphism
    SubModule = Parent
    Ideal = Ideal_generic

    class OrderedSet(Protocol):
        def cardinality(self) -> Cardinality: ...

        def __getitem__(self, key: object) -> RModuleElement: ...


# ---------------------------------------------------------------------------
# Base-ring property subcategories
# ---------------------------------------------------------------------------


class _OverIntegralDomain(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_integral_domain()

    class ParentMethods:
        def is_over_integral_domain(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


class _OverDedekindDomain(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        return [self.base_category().OverIntegralDomain()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_dedekind_domain()

    class ParentMethods:
        def is_over_dedekind_domain(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


class _OverPID(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        return [self.base_category().OverDedekindDomain()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_pid()

    class ParentMethods:
        def is_over_pid(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


class _OverCommutativeRing(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_commutative_ring()

    class ParentMethods:
        def is_over_commutative_ring(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


class _OverField(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        return [self.base_category().OverPID()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_field()

    class ParentMethods:
        def is_over_field(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


class _OverLocalRing(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_local_ring()

    class ParentMethods:
        def is_over_local_ring(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


class _OverCompleteRing(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_complete_ring()

    class ParentMethods:
        def is_over_complete_ring(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


# ---------------------------------------------------------------------------
# Homological axioms (Free / Torsion / Torsionfree / Projective)
# ---------------------------------------------------------------------------


class _FreeFiniteRank(CategoryWithAxiom_over_base_ring):
    def extra_super_categories(self):
        r"""A finite-rank free module is exactly a finitely generated free module.

        TODO: a finite-rank free module over a finite ring is itself finite.
        TODO: externalize this category entirely.
        """
        return [self.base_category().FinitelyGenerated()]

    class ParentMethods:
        @abstract_method
        def basis(self, *args, **kwds): ...

        @abstract_method
        def dimension(self) -> Cardinality: ...

    class ElementMethods: ...

    class MorphismMethods: ...


class _Free(CategoryWithAxiom_over_base_ring):
    r"""Free R-modules.  Does not assume finitely generated or finitely
    presented; e.g. ``\bigoplus_{z \in CC} CC`` is a free CC-module.
    """

    def extra_super_categories(self):
        r"""Every free R-module is projective."""
        return [self.base_category().Projective()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_free()

    class SubcategoryMethods:
        @cached_method
        def FiniteRank(self):
            r"""Subcategory where the rank is finite, so M \cong R^n for some n < \infty."""
            return self._with_axiom("FiniteRank")

    FiniteRank = _FreeFiniteRank

    class ParentMethods:
        def is_free(self) -> bool:
            return True

        @abstract_method
        def rank(self) -> Cardinality:
            r"""Rank is only well-defined for free R-modules; equals the
            cardinality of any generating set (which may be infinite).
            """
            return self.gens().cardinality()


class _Torsion(CategoryWithAxiom_over_base_ring):
    r"""TODO: a torsion module over a finite ring is finite."""

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_torsion()

    class ParentMethods:
        def is_torsion(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


class _Torsionfree(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_torsionfree()

    class ParentMethods:
        def is_torsionfree(self) -> bool:
            return True

        def annihilator(self) -> Ideal:
            r"""Ann_R(M) = <0>, the zero ideal of R regarded as an R-submodule of R."""
            R = self.base_ring()
            return R.ideal(R.zero())

    class ElementMethods: ...

    class MorphismMethods: ...


class _Projective(CategoryWithAxiom_over_base_ring):
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_projective()

    class ParentMethods:
        def is_projective(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...


# ---------------------------------------------------------------------------
# Generation properties
# ---------------------------------------------------------------------------


class _WithOrderedGeneratingSet(CategoryWithAxiom_over_base_ring):
    r"""There exists an ordered set ``S = {s_1 <= s_2 <= ...}`` and a
    surjection ``f: R^S \cong R[s_1] \oplus R[s_2] \oplus ... -> M`` where
    the direct sum is ordered.  ``S`` need not be finite.
    """

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_ordered_generating_set()

    class ParentMethods:
        def has_ordered_generating_set(self) -> bool:
            return True

        @abstract_method
        def gens(self) -> OrderedSet: ...

        def ngens(self) -> Cardinality:
            return self.gens().cardinality()

        def gen(self, i):
            return self.gens()[i]

    class Homsets(HomsetsCategory):
        class ParentMethods:
            @abstract_method
            def from_function(self, f: Callable[[RModuleElement], RModuleElement]):
                r"""A morphism f: M_1 -> M_2 can be defined from a
                set-theoretic function f: S_1 -> S_2 on the generating sets.
                """
                ...

    class ElementMethods: ...

    class MorphismMethods:
        @abstract_method
        def to_function(self) -> Callable[[RModuleElement], RModuleElement]: ...


class _FinitelyGenerated(CategoryWithAxiom_over_base_ring):
    r"""Modules M which admit a surjection f: R^n -> M for some n < \infty.

    Implies a preferred choice of generating set.  Does NOT imply finitely
    presented: ker(f) need not be finitely generated.  Counterexample: any
    ideal I in a non-Noetherian ring.
    """

    def extra_super_categories(self):
        return [self.base_category().WithOrderedGeneratingSet()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_finitely_generated()

    class ParentMethods:
        def is_finitely_generated(self) -> bool:
            return True


class _FinitelyPresented(CategoryWithAxiom_over_base_ring):
    r"""Modules M that can be written as <S | R> with S \subseteq M a finite
    generating set and R a finite set of relations.

    Equivalently, M can be written as ``M := coker_R(f: R^m -> R^n)``.
    Finitely presented implies finitely generated, but the converse fails:
    if R is non-Noetherian and I \subseteq R is an ideal that is not
    finitely generated, then R/I is finitely generated but not finitely
    presented (the presentation 0 -> I -> R -> R/I -> 0 has non-fg kernel).
    """

    def extra_super_categories(self):
        r"""If the base ring (or category of base rings) is finite, then every
        finitely presented module is itself finite.
        """
        from . import Categories, FinSet

        result = [self.base_category().FinitelyGenerated()]
        R = self.base_ring()
        if (R in Categories() and R.is_subcategory(FinSet)) or R in FinSet:
            result.append(FinSet)
        return result

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_finitely_presented()

    class ParentMethods:
        def is_finitely_presented(self) -> bool:
            return True


# ---------------------------------------------------------------------------
# Ideals as a named subcategory of Modules(R).Subobjects()
# ---------------------------------------------------------------------------


class _RIdeals(CategoryWithAxiom_over_base_ring):
    r"""Ideals of R viewed as submodules of R^1.

    This is the named-subcategory entry point ``Modules(R).RIdeals``; the
    parallel ring-side refinement lives in the private ring ideal bridge.
    """

    def extra_super_categories(self):
        return [self.base_category().Subobjects()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_ideal()

    class ParentMethods:
        def is_ideal(self) -> bool:
            return True

        # gens() not defined unless R is Noetherian.
        # don't leak the sage ideal: refine all ring-related categories
        ...

    class ElementMethods: ...

    class MorphismMethods: ...


# ---------------------------------------------------------------------------
# Forms axiom subcategories
# ---------------------------------------------------------------------------


class _WithForms(CategoryWithAxiom_over_base_ring):
    r"""Non-full subcategory of pairs (M, f) with f a form on M."""

    class ParentMethods:
        @abstract_method
        def form(self) -> RModuleMorphism: ...

    class SubcategoryMethods:
        @cached_method
        def Bilinear(self):
            r"""(M, b) with b: M \otimes_R M -> S, possibly degenerate."""
            return self._with_axiom("Bilinear")

        @cached_method
        def Quadratic(self):
            r"""(M, q) with q: M -> S^\sigma, possibly degenerate."""
            return self._with_axiom("Quadratic")

        @cached_method
        def Symmetric(self):
            return self._with_axiom("Symmetric")

        @cached_method
        def Alternating(self):
            return self._with_axiom("Alternating")

        @cached_method
        def Nondegenerate(self):
            return self._with_axiom("Nondegenerate")

        @cached_method
        def Integral(self):
            return self._with_axiom("Integral")

        @cached_method
        def Rational(self):
            return self._with_axiom("Rational")


class _BilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules with a bilinear form b: M \otimes_R M -> S."""

    class ParentMethods:
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.form().b(v, w)


class _QuadraticModules(CategoryWithAxiom_over_base_ring):
    r"""Modules with a quadratic form q: M -> S^\sigma."""

    class ParentMethods:
        def q(self, v: RModuleElement) -> RModuleElement:
            return self.form().q(v)
