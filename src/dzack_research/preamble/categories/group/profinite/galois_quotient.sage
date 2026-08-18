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

Concretely, a subfield of \(M\) is a field \(L\) together with an
embedding \(j:L\hookrightarrow M\), and restricting an automorphism
\(\sigma\) of \(M\) to \(L\) means solving
\[
j\circ\tau=\sigma\circ j
\]
for \(\tau\in\operatorname{Aut}(L)\).  Read in the other direction, the
same equation says which automorphisms of \(M\) extend a given
\(\tau\).  :func:`restrict_along` solves it for \(\tau\);
:func:`extensions_along` solves it for \(\sigma\).
"""

from sage.categories.groups import Groups as SageGroups
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    from sage.categories.groups import Group
    from sage.categories.rings import Ring


def restrict_along(automorphism: Morphism, embedding: Morphism) -> Morphism:
    r"""Return the restriction \(\tau\) of ``automorphism`` along ``embedding``.

    ``embedding`` is \(j:L\hookrightarrow M\) and ``automorphism`` is
    \(\sigma:M\to M\); the returned \(\tau:L\to L\) is the unique
    automorphism with \(j\circ\tau=\sigma\circ j\).

    An automorphism of \(L\) is determined by where it sends a primitive
    element, so \(\tau\) is found by computing \(\sigma(j(\gamma))\) and
    recognizing it among the finitely many \(j(\tau'(\gamma))\).  A
    \(\tau\) exists exactly when \(\sigma\) preserves the subfield
    \(j(L)\), which is automatic when \(L\) is normal over the base.
    """
    subfield = embedding.domain()
    generator = subfield.gen()
    image = automorphism(embedding(generator))
    candidates = [
        candidate
        for candidate in subfield.embeddings(subfield)
        if embedding(candidate(generator)) == image
    ]
    assert len(candidates) == 1, (
        f"{automorphism} does not restrict to {subfield} along {embedding}: "
        f"it sends {embedding(generator)} to {image}, "
        f"which is not the image of an automorphism of {subfield}"
    )
    restriction: Morphism = candidates[0]
    return restriction


def extensions_along(
    automorphism: Morphism, embedding: Morphism, candidates: "Iterable[Morphism]"
) -> "list[Morphism]":
    r"""Return those ``candidates`` restricting to ``automorphism`` along ``embedding``.

    ``embedding`` is \(j:L\hookrightarrow M\), ``automorphism`` is
    \(\tau:L\to L\), and ``candidates`` are automorphisms of \(M\); the
    result is \(\{\sigma:\sigma\circ j=j\circ\tau\}\).  When
    ``candidates`` is all of \(\operatorname{Gal}(M/K)\) and \(M/K\) is
    Galois, this is the coset \(\sigma_0\operatorname{Gal}(M/L)\), and it
    is nonempty because every \(\tau\) extends (Stacks 0BME).
    """
    generator = embedding.domain().gen()
    source = embedding(generator)
    target = embedding(automorphism(generator))
    return [
        candidate for candidate in candidates if candidate(source) == target
    ]


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