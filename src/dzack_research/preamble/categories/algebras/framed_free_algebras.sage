r"""Free commutative algebras on arbitrary sets.

``FreeAlgebraOnSet(R, S)`` realizes the free commutative R-algebra on a set S:

\[
    \operatorname{FreeAlg}_R(S) = R[\operatorname{Mon}(S)]
\]

As an R-module, this is ``FreeModuleOnSet(R, Mon(S))`` where Mon(S) is the
free commutative monoid on S (monomials in S).  Multiplication is the monoid
operation on Mon(S) extended R-bilinearly.

The set S is construction data.  It need not be finite, countable, or ordered.
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.monoids.free_abelian_monoid import FreeAbelianMonoid
from sage.structure.parent import Parent


class FramedFreeAlgebras(Category_over_base_ring):
    r"""Free R-algebras equipped with the canonical map \(S \to U(\operatorname{FreeAlg}_R(S))\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed free algebras"

    def super_categories(self) -> list:
        return [
            FreeAlgebras(self.base_ring()),
            FramedAlgebras(self.base_ring()),
            FramedFreeModules(self.base_ring()),
        ]


class FreeAlgebraOnSetElement(FreeModuleOnSetElement):
    r"""An element of ``FreeAlgebraOnSet`` with bilinear multiplication."""

    def _mul_(self, other: Any) -> "FreeAlgebraOnSetElement":
        assert (
            isinstance(other, FreeAlgebraOnSetElement)
            and other.parent() is self.parent()
        ), "free-algebra multiplication requires elements of one parent"
        parent = self.parent()
        zero = parent.base_ring().zero()
        coefficients = {}
        for left_monomial, left_coefficient in self.coefficients().items():
            for right_monomial, right_coefficient in other.coefficients().items():
                monomial = left_monomial * right_monomial
                coefficients[monomial] = coefficients.get(monomial, zero) + (
                    left_coefficient * right_coefficient
                )
        return parent.element_class(parent, coefficients)


class FreeAlgebraOnSet(FreeModuleOnSet):
    r"""The free commutative R-algebra on the set S.

    As an R-module, this is \(F_R(\operatorname{Mon}(S))\): the free module
    on the free commutative monoid on S.  Multiplication is the monoid
    operation extended R-bilinearly.

    Inherits generating set, generator morphism, element construction,
    and linear combination from ``FreeModuleOnSet``.
    """

    Element = FreeAlgebraOnSetElement

    def __init__(self, base_ring: Any, generating_set: Any) -> None:
        self._algebra_generating_set = generating_set
        monoid = _as_set(FreeAbelianMonoid(generating_set))
        FreeModuleOnSet.__init__(self, base_ring, monoid)
        refine(self, FramedFreeAlgebras(base_ring))

    def algebra_generating_set(self) -> Parent:
        r"""Return the original set S (not Mon(S))."""
        return self._algebra_generating_set

    def algebra_generator(self, s: Any) -> Any:
        r"""Return the degree-1 monomial [s] in FreeAlg_R(S)."""
        assert s in self._algebra_generating_set, (
            f"{s!r} is not in {self._algebra_generating_set}"
        )
        monomial = self.generating_set().gen(s)
        return self.generator(monomial)

    def product_on_generators(self, s: Any, t: Any) -> Any:
        r"""Return the product of algebra generators s and t."""
        return self.algebra_generator(s) * self.algebra_generator(t)

    def one(self) -> Any:
        r"""Return the multiplicative identity (the empty monomial)."""
        return self.generator(self.generating_set().one())

    def _repr_(self) -> str:
        return f"Free {self.base_ring()}-algebra on {self._algebra_generating_set}"


def FreeAlgebraOn(base_ring: Any, generating_set: Any) -> FreeAlgebraOnSet:
    r"""Construct \(\operatorname{FreeAlg}_R(S)\) on the supplied set S."""
    generating_set = _as_set(generating_set)
    return FreeAlgebraOnSet(base_ring, generating_set)
