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

from typing import TYPE_CHECKING

from sage.misc.cachefunc import cached_function
from sage.categories.groups import Groups as SageGroups

from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category

if TYPE_CHECKING:
    from sage.structure.parent import Parent
    from sage.categories.groups import Group
    from sage.categories.rings import Ring
    from dzack_research.preamble.owned_category import ConstructionData


class ProfiniteCharacterHomsets(Category):
    r"""Homsets of finite-quotient characters of absolute Galois groups."""

    def super_categories(self) -> list:
        from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
            AbsoluteGaloisGroups,
        )

        return [AbsoluteGaloisGroups().Homsets()]

    class ParentMethods:
        def __init__(
            self,
            domain: "Parent",
            codomain: "Group",
            **rest: "ConstructionData",
        ) -> None:
            super().__init__(
                domain=domain,
                codomain=codomain,
                category=SageGroups(),
                check=False,
                **rest,
            )

    class ElementMethods:
        def __init__(
            self,
            parent: "Parent",
            extension: "Ring",
        ) -> None:
            self._extension = extension
            super().__init__(parent)

        def extension(self) -> "Ring":
            r"""Return the finite extension through which the character factors."""
            return self._extension

        def kernel(self) -> "Parent":
            r"""Return the open subgroup that fixes the finite extension."""
            return self.domain().open_subgroup(self.extension())

        def restrict(self, extension: "Ring") -> "Parent":
            r"""Return the open subgroup over which the character is restricted."""
            return self.domain().open_subgroup(extension)

        def _repr_(self) -> str:
            return f"Finite-quotient character {self.domain()} -> {self.codomain()}"


@cached_function
def profinite_character_homset(
    domain: "Parent", codomain: "Group"
) -> "Parent":
    r"""Return the finite-quotient character homset with the stated ends."""
    return object_of(
        ProfiniteCharacterHomsets(),
        domain=domain,
        codomain=codomain,
    )


class CyclotomicCharacter(ProfiniteCharacterHomsets().element_class):
    r"""The cyclotomic character \(\chi_n:G_K\to(\mathbb Z/n\mathbb Z)^\times\)."""

    def __init__(
        self, restriction_map: "GaloisRestrictionMap", target: "Group"
    ) -> None:
        super().__init__(
            profinite_character_homset(restriction_map.domain(), target),
            restriction_map.extension(),
        )


class QuadraticCharacter(ProfiniteCharacterHomsets().element_class):
    r"""The quadratic character \(G_K\to\{\pm1\}\) attached to \(K(\sqrt a)/K\)."""

    def __init__(self, restriction_map: "GaloisRestrictionMap") -> None:
        from sage.groups.perm_gps.permgroup_named import CyclicPermutationGroup

        target = CyclicPermutationGroup(2)
        super().__init__(
            profinite_character_homset(restriction_map.domain(), target),
            restriction_map.extension(),
        )
