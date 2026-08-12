r"""The continuous surjection \(G_K\twoheadrightarrow\operatorname{Gal}(L/K)\).

For \(L/K\) finite Galois inside \(K^{\mathrm{sep}}\), there is an exact
sequence
\[
1\longrightarrow G_L\longrightarrow G_K
\longrightarrow \operatorname{Gal}(L/K)\longrightarrow1.
\]
Moreover,
\[
G_K\simeq\varprojlim_{L/K\ \mathrm{finite\ Galois}}
\operatorname{Gal}(L/K),
\]
so ``finite_quotient(L)`` is not an approximation to \(G_K\); it is
literally one of the defining coordinates of the profinite group.

The restriction map is the surjection in that sequence.  Its kernel is
the open subgroup \(G_L\).
"""

from sage.categories.groups import Groups as SageGroups
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Group, Ring


class GaloisRestrictionMap(Morphism):
    r"""The continuous surjection \(G_K\twoheadrightarrow\operatorname{Gal}(L/K)\)."""

    def __init__(
        self, domain: "Group", codomain: "Group", extension: "Ring"
    ) -> None:
        Morphism.__init__(self, Hom(domain, codomain, SageGroups()))
        self._extension = extension

    def extension(self) -> "Ring":
        r"""Return the finite Galois extension \(L/K\)."""
        return self._extension

    def kernel(self) -> "OpenAbsoluteGaloisSubgroup":
        r"""Return \(G_L\), the open subgroup that is the kernel."""
        open_subgroup: "OpenAbsoluteGaloisSubgroup" = self.domain().open_subgroup(
            self._extension
        )
        return open_subgroup

    def _repr_(self) -> str:
        return (
            f"Continuous surjection:\n"
            f"  From: {self.domain()}\n"
            f"  To:   {self.codomain()}"
        )