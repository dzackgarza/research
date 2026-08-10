r"""Characters of \(G_K\) as Sage morphisms.

For \(n\) prime to \(\operatorname{char}K\), the action on roots of
unity gives the cyclotomic character
\[
\chi_n:G_K\longrightarrow
\operatorname{Aut}(\mu_n)\cong(\mathbb Z/n\mathbb Z)^\times.
\]
Taking the inverse system for \(n=\ell^r\) gives the actual
\(\ell\)-adic cyclotomic representation
\(\chi_\ell:G_K\to\mathbb{Z}_\ell^\times\).

If \(\operatorname{char}K\ne2\), every \(a\in K^\times\) gives the
quadratic character associated to \(K(\sqrt a)/K\).  More generally
Kummer theory gives
\[
H^1(G_K,\mu_n)\cong K^\times/K^{\times n}
\]
for \(n\) invertible in \(K\).

These are genuine Sage morphisms, not metadata::

    chi.domain() is G
    chi.codomain()
    chi.kernel()
    chi.restrict(L)

all have real meanings.
"""

from sage.categories.groups import Groups as SageGroups
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism


class CyclotomicCharacter(Morphism):
    r"""The cyclotomic character \(\chi_n:G_K\to(\mathbb Z/n\mathbb Z)^\times\)."""

    def __init__(self, restriction_map, target) -> None:
        Morphism.__init__(
            self, Hom(restriction_map.domain(), target, SageGroups())
        )
        self._restriction_map = restriction_map
        self._target = target

    def domain(self):
        return self._restriction_map.domain()

    def codomain(self):
        return self._target

    def kernel(self):
        return self._restriction_map.kernel()

    def restrict(self, L):
        r"""Restrict the character along \(G_L\hookrightarrow G_K\)."""
        return self._restriction_map.domain().open_subgroup(L)

    def _repr_(self) -> str:
        return f"Cyclotomic character {self.domain()} -> {self._target}"


class QuadraticCharacter(Morphism):
    r"""The quadratic character \(G_K\to\{\pm1\}\) attached to \(K(\sqrt a)/K\)."""

    def __init__(self, restriction_map) -> None:
        from sage.groups.perm_gps.permgroup_named import CyclicPermutationGroup

        target = CyclicPermutationGroup(2)
        Morphism.__init__(
            self, Hom(restriction_map.domain(), target, SageGroups())
        )
        self._restriction_map = restriction_map

    def domain(self):
        return self._restriction_map.domain()

    def kernel(self):
        return self._restriction_map.kernel()

    def _repr_(self) -> str:
        return f"Quadratic character on {self.domain()}"